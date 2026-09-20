#!/usr/bin/env python3
"""podcast2md —— 播客音频 → 整合版 Markdown 文稿。

一条命令跑完：取源 → 下载 → 本地转写 → 缺口质检补转 → 补标点 → LLM 摘要与
专有名词校正 → 组装 md/srt。中间产物逐段落盘，中断可续跑。

用法：
    python podcast2md.py <小宇宙链接|本地音频> [-o 输出目录] [选项]
详见 README.md。
"""
from __future__ import annotations

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from p2m import asr, compose, enrich, fetch, punct
from p2m.llm import DEFAULT_BASE_URL, DEFAULT_MODEL, LLM
from p2m.util import chunk_windows, log, read_json, setup_console, slugify, ts, write_json


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        prog="podcast2md", description="播客音频 → 整合版 Markdown 文稿",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("source", help="小宇宙单集链接，或本地音频文件路径")
    p.add_argument("-o", "--outdir", default=".", help="输出目录（默认当前目录）")
    p.add_argument("-w", "--work", default=None, help="中间产物目录（默认 <outdir>/.podcast2md/<slug>）")
    p.add_argument("--limit", type=float, default=0.0, help="只处理前 N 秒（调试用）")
    p.add_argument("--chunk", type=float, default=600.0, help="转写分块秒数（默认 600）")
    p.add_argument("--asr-backend", default="auto", choices=["auto", "mlx", "faster-whisper"],
                   help="转写后端：auto 按平台自动选（Apple Silicon 走 mlx，其余走 faster-whisper）")
    p.add_argument("--asr-model", default=None,
                   help="模型名；默认 Apple Silicon 用 mlx-community/whisper-large-v3-mlx，其余用 large-v3")
    p.add_argument("--device", default="cpu", help="faster-whisper 设备：cpu / cuda")
    p.add_argument("--compute-type", default="int8",
                   help="faster-whisper 精度：CPU 用 int8，NVIDIA 卡用 float16")
    p.add_argument("--threads", type=int, default=0, help="faster-whisper CPU 线程数，0=自动")
    p.add_argument("--punct-model", default=punct.DEFAULT_PUNCT_MODEL)
    p.add_argument("--gap-min", type=float, default=45.0, help="判定吞内容的间隔阈值（秒）")
    p.add_argument("--no-repair", action="store_true", help="跳过缺口补转")
    p.add_argument("--comma-th", type=float, default=0.9, help="标点模型逗号置信度阈值")
    p.add_argument("--no-llm", action="store_true", help="跳过 LLM 摘要与校正")
    p.add_argument("--no-verify", action="store_true", help="跳过校正表的 LLM 上下文复核")
    p.add_argument("--api-key", default=None)
    p.add_argument("--base-url", default=os.environ.get("PODCAST2MD_BASE_URL", DEFAULT_BASE_URL))
    p.add_argument("--model", default=os.environ.get("PODCAST2MD_MODEL", DEFAULT_MODEL))
    p.add_argument("--window-chars", type=int, default=6000, help="LLM 分段理解的字数窗口")
    p.add_argument("--corrections", default=None, help="额外校正表 JSON（{\"识别\":\"应为\"}）")
    p.add_argument("--host", default=None, help="主播（默认取播客作者）")
    p.add_argument("--guest", default=None, help="嘉宾")
    p.add_argument("--name", default=None, help="输出文件名主干（不含编号前缀）")
    p.add_argument("--num", type=int, default=None, help="输出编号前缀（默认自动取下一个）")
    p.add_argument("--force", action="store_true", help="忽略已有中间产物，全部重跑")
    return p.parse_args(argv)


def build_meta(args, asr_model: str, backend: str) -> dict:
    backend_label = ("Apple MLX 本地推理" if backend == "mlx"
                     else f"faster-whisper 本地推理（device={args.device}, {args.compute_type}）")
    src = args.source
    meta_path_hint = None
    if re.match(r"^https?://", src):
        log(f"[meta] 抓取单集页 {src}")
        ep = fetch.fetch_episode(src)
        meta = {
            "title": ep["title"],
            "podcast": ep["podcast"],
            "host": args.host or ep["author"],
            "duration": ep["duration"],
            "audio_url": ep["audio_url"],
            "source": src,
        }
    else:
        audio_abs = os.path.abspath(src)
        meta = {
            "title": os.path.splitext(os.path.basename(audio_abs))[0],
            "podcast": "", "host": args.host or "", "duration": 0,
            "audio_url": "", "source": audio_abs, "local_audio": audio_abs,
        }
    meta["episode_no"] = fetch.parse_episode_no(meta["title"])
    topic_full = fetch.parse_topic(meta["title"]) or meta["title"]
    meta["topic"] = topic_full.split("：")[0].strip()
    meta["guest"] = args.guest or enrich.guest_from_title(meta["title"])
    meta["duration_text"] = ts(meta["duration"]) if meta.get("duration") else ""
    meta["asr_model"] = f"{asr_model}（{backend_label}）"
    meta["punct_model"] = args.punct_model
    # 体例标题：<来源> <期号> · 对话<嘉宾>：<话题>
    head = " ".join(x for x in (meta["podcast"], meta["episode_no"]) if x)
    topic = topic_full
    if meta["guest"]:
        m = re.match(rf"^(?:和|跟|与){re.escape(meta['guest'])}(?:聊|谈|对话)\s*", topic)
        if m:
            topic = topic[m.end():].replace("：", "——", 1)
    meta["md_title"] = f"{head} · 对话{meta['guest']}：{topic}" if meta["guest"] else (f"{head} · {topic}".strip(" ·"))
    return meta


def main(argv=None) -> int:
    setup_console()
    args = parse_args(argv)
    backend = asr.resolve_backend(args.asr_backend)
    asr_model = args.asr_model or asr.default_model(backend)
    meta = build_meta(args, asr_model, backend)

    slug = slugify(f"{meta.get('podcast','')}{meta.get('episode_no','')}-{meta.get('topic','')}") or "podcast"
    work = args.work or os.path.join(args.outdir, ".podcast2md", slug)
    os.makedirs(work, exist_ok=True)
    write_json(os.path.join(work, "meta.json"), meta)
    log(f"[work] 中间产物目录 {work}")

    # 1) 音频
    if meta.get("local_audio"):
        audio_path = meta["local_audio"]
    else:
        audio_path = fetch.download(meta["audio_url"], os.path.join(work, "audio.m4a"), meta.get("source", ""))

    # 2) 转写（分块、可续跑）
    audio = asr.decode(audio_path, limit=args.limit)
    segs = asr.transcribe(audio, work, backend, asr_model, chunk=args.chunk,
                          device=args.device, compute_type=args.compute_type,
                          threads=args.threads, force=args.force)

    # 3) 缺口质检 + 补转
    stats = {"gap_min": args.gap_min, "gaps_repaired": 0}
    if args.no_repair:
        segs = asr.merge_chunks(work)
    else:
        n_gaps = len(asr.find_gaps(asr.merge_chunks(work, fix=False), args.gap_min))
        segs = asr.repair_gaps(audio, work, backend, asr_model, gap_min=args.gap_min,
                              device=args.device, compute_type=args.compute_type,
                              threads=args.threads, force=args.force)
        stats["gaps_repaired"] = n_gaps
    log(f"[asr] 片段合计 {len(segs)} 条，覆盖至 {ts(segs[-1][1]) if segs else '-'}")

    # 4) 补标点（缓存）
    punct_path = os.path.join(work, "segments_punct.json")
    if os.path.exists(punct_path) and not args.force:
        log("[punct] 复用已有的标点结果")
        segs = read_json(punct_path)
    else:
        segs = punct.restore(segs, model=args.punct_model, comma_th=args.comma_th)
        write_json(punct_path, segs)

    # 5) 规则清理（样板幻觉 / 复读环 / 标点规范）
    segs, qc = punct.normalize(segs)
    stats.update(qc)
    stats["chars"] = sum(len(s[2]) for s in segs)

    # 6) LLM：分段理解 + 汇总 + 校正表
    summary, corr_table = {}, []
    manual = read_json(args.corrections, {}) if args.corrections else {}
    if args.no_llm:
        log("[llm] --no-llm，跳过摘要与校正")
    else:
        llm = LLM(model=args.model, base_url=args.base_url, api_key=args.api_key)
        cache = os.path.join(work, "llm_windows.json")
        if os.path.exists(cache) and not args.force:
            log("[llm] 复用已有的分段理解结果")
            cached = read_json(cache, {})
            points, raw_corr = cached["points"], cached["corrections"]
        else:
            known = [meta.get("host", ""), meta.get("guest", "")]
            points, raw_corr = enrich.map_windows(
                llm, list(chunk_windows(segs, args.window_chars)), known_names=known)
            write_json(cache, {"points": points, "corrections": raw_corr})
        # 先定校正表（含上下文复核），再回灌给分段要点，最后汇总——否则摘要里会残留「曾敏」而正文已是「曾鸣」
        kept, rejected, conflicts = enrich.dedupe_corrections(raw_corr, "".join(s[2] for s in segs))
        for w, a, b in conflicts:
            log(f"[llm] 校正「{w}」在不同窗口给出「{a}」/「{b}」，保留前者")
        if not args.no_verify:
            kept, v_rejected = enrich.verify_corrections(
                llm, kept, segs, known_names=[meta.get("host", ""), meta.get("guest", "")])
            rejected += v_rejected
        for w, why in rejected:
            log(f"[llm] 拒绝校正「{w}」：{why}")
        for wrong, right in (manual or {}).items():
            kept.append({"识别": wrong, "应为": right, "依据": "人工指定"})
        summary = enrich.reduce_summary(llm, meta, enrich.correct_any(points, kept))
        summary = enrich.correct_any(summary, kept)
        write_json(os.path.join(work, "llm_summary.json"), summary)
        segs, corr_table = enrich.apply_corrections(segs, kept)
        stats["chars"] = sum(len(s[2]) for s in segs)

    # 7) 组装
    md = compose.build_markdown(meta, segs, summary, corr_table, stats)
    tail = compose.output_tail(meta)
    index = compose.resolve_index(args.outdir, tail, args.num)
    basename = args.name or f"{index:02d}-{tail}"
    md_path, srt_path = compose.emit(args.outdir, basename, md, segs)
    log(f"[done] {md_path}")
    log(f"[done] {srt_path}")
    print(md_path)
    print(srt_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
