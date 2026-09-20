"""组装：把片段与摘要拼成整合版 Markdown（本仓库既定体例）＋ SRT 字幕。"""
from __future__ import annotations

import os
import re

from .util import next_index, slugify, srt_ts, ts

PARA_MIN = 110     # 段落累计字数下限（收在句末才断）
PARA_MAX = 200     # 强制断段上限


def group_paragraphs(segments):
    """把逐句片段合并成可读段落，保留段首时间戳。"""
    groups, cur = [], None
    for s, e, t in segments:
        if cur is None:
            cur = [s, e, t]
            continue
        cur[2] += t
        cur[1] = e
        if (len(cur[2]) >= PARA_MIN and cur[2][-1] in "。！？") or len(cur[2]) >= PARA_MAX:
            groups.append(cur)
            cur = None
    if cur:
        groups.append(cur)
    return groups


def write_srt(segments, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for i, (s, e, t) in enumerate(segments, 1):
            f.write(f"{i}\n{srt_ts(s)} --> {srt_ts(e)}\n{t}\n\n")


def output_tail(meta: dict) -> str:
    """文件名主干（不含 NN- 编号前缀）：<播客简称><期号>-<话题>。"""
    podcast = slugify(meta.get("podcast", ""), 24)
    head = f"{podcast}{meta.get('episode_no', '')}"
    topic = slugify(meta.get("topic", ""), 30)
    if head and topic:
        return f"{head}-{topic}"
    return head or topic or slugify(meta.get("title", ""), 40) or "podcast"


def resolve_index(outdir: str, tail: str, num: int | None = None) -> int:
    """决定编号：显式指定 > 复用同名文件的已有编号 > 目录里下一个空位。

    复用是为了让「同一集重跑」覆盖原文件，而不是每次都多出一个新编号。
    """
    if num is not None:
        return num
    if os.path.isdir(outdir):
        hits = [int(m.group(1)) for name in os.listdir(outdir)
                if (m := re.match(r"^(\d+)-(.+)\.md$", name)) and m.group(2) == tail]
        if hits:
            return min(hits)
    return next_index(outdir)


def _timeline_table(rows) -> str:
    out = ["| 时间 | 内容 |", "|---|---|"]
    for r in rows or []:
        t = str(r.get("时间", "")).replace("–", "–")
        out.append(f"| {t} | {str(r.get('内容','')).strip()} |")
    return "\n".join(out)


def _key_points(items) -> str:
    out = []
    for i, k in enumerate(items or [], 1):
        out.append(f"**{i}. {str(k.get('标题','')).strip()}**\n{str(k.get('正文','')).strip()}")
    return "\n\n".join(out)


def _corrections_table(table) -> str:
    if not table:
        return "| 转写识别 | 校正为 | 处数 | 依据 |\n|---|---|---|---|\n| — | — | 0 | 本期未检出需要校正的专有名词 |"
    lines = ["| 转写识别 | 校正为 | 处数 | 依据 |", "|---|---|---|---|"]
    for wrong, right, n, basis in table:
        lines.append(f"| {wrong} | {right} | {n} | {basis or '同音误识别，按上下文校正'} |")
    return "\n".join(lines)


def build_markdown(meta: dict, segments, summary: dict, corr_table, stats: dict) -> str:
    title = meta.get("md_title") or meta.get("title", "")
    n_corr = sum(r[2] for r in corr_table)
    notes = [
        "本稿为机器转写，除下列处理外不做任何改写：",
        f"①**补标点**——原始转写几乎没有标点，用中文标点恢复模型"
        f"（`{meta.get('punct_model','')}`）逐字补出，这是本次唯一的生成性处理，位置可能有个别偏差；"
        f"②**清除语音识别的复读幻觉**——丢弃整段样板幻觉 {stats.get('dropped', 0)} 段、"
        f"截断复读环 {stats.get('repeats', 0)} 处；"
        f"③**校正专有名词 {n_corr} 处**，逐条列于下文「术语校正清单」。",
        "口语中的重复、语气词、吞字与自我修正均未删改，以保留原貌。",
    ]
    if stats.get("gaps_repaired"):
        notes.append(f"另有 {stats['gaps_repaired']} 处时间缺口（相邻片段间隔 >{stats.get('gap_min', 45):.0f}s）已定点补转。")

    parts = [f"# {title}", ""]
    meta_rows = [
        ("播客", meta.get("podcast", "")),
        ("主播", meta.get("host", "")),
        ("嘉宾", meta.get("guest", "")),
        ("时长", meta.get("duration_text", "")),
        ("链接", meta.get("source", "")),
        ("转写", f"{meta.get('asr_model','Whisper large-v3 / Apple MLX')}，全程本地运行，未上传云服务"),
    ]
    parts.append("|  |  |")
    parts.append("|---|---|")
    for k, v in meta_rows:
        if v:
            parts.append(f"| **{k}** | {v} |")
    parts.append("")
    parts.append("> 说明：" + "".join(notes))
    parts.append("")
    parts.append("> **本文件为整合版**，包含「要点摘要」与「完整逐字稿」两部分，可单独阅读或检索。")
    parts.append(f"> 同源逐句字幕（SRT 格式，{len(segments)} 条）与本目录同名 `.srt` 文件对应；"
                 f"其文本内容已全部包含在下方逐字稿中。")
    parts += ["", "---", "", "## 目录", "",
              "- [第一部分 · 要点摘要](#第一部分--要点摘要)",
              "- [第二部分 · 完整逐字稿](#第二部分--完整逐字稿)",
              "", "---", "", "## 第一部分 · 要点摘要", ""]

    if summary:
        parts += ["### 一句话主旨", "", str(summary.get("一句话主旨", "")).strip(), "", "---", ""]
        parts += ["### 时间轴", "", _timeline_table(summary.get("时间轴")), "", "---", ""]
        parts += ["### 核心观点", "", _key_points(summary.get("核心观点")), "", "---", ""]
    else:
        parts += ["> 本次以 `--no-llm` 运行，未生成要点摘要。", "", "---", ""]

    parts += ["### 术语校正清单", "",
              f"> 全稿共校正 {n_corr} 处。除标注**仍存疑**者外，均为同音误识别。", "",
              _corrections_table(corr_table), "", "---", ""]

    if summary:
        mem = summary.get("值得记住的一段") or {}
        ctx, quote = str(mem.get("语境", "")).strip(), str(mem.get("引文", "")).strip()
        parts += ["### 值得记住的一段", ""]
        if ctx:
            parts.append(f"语境：{ctx}")
            parts.append("")
        if quote:
            parts.append(f"**“{quote.strip('“”\"')}”**")
            parts.append("")
        parts += ["---", ""]

    body = group_paragraphs(segments)
    parts += ["## 第二部分 · 完整逐字稿", "",
              f"> 共 {len(body)} 段、约 {stats.get('chars', 0)} 字，"
              f"时间戳覆盖 {ts(segments[0][0]) if segments else '00:00:00'}–"
              f"{ts(segments[-1][1]) if segments else '00:00:00'}。"
              f"每段方括号内为节目内时间（时:分:秒）。", ""]
    for s, _e, t in body:
        parts.append(f"**[{ts(s)}]** {t}")
        parts.append("")
    return "\n".join(parts).rstrip() + "\n"


def emit(outdir: str, basename: str, markdown: str, segments):
    """写出 md 与 srt。basename 需已含 NN- 前缀。"""
    os.makedirs(outdir, exist_ok=True)
    md_path = os.path.join(outdir, basename + ".md")
    srt_path = os.path.join(outdir, basename + ".srt")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    write_srt(segments, srt_path)
    return md_path, srt_path
