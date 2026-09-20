"""标点：中文标点恢复模型（逐字打标）+ 规则清理。

背景：Whisper 对本类音频常常整篇不吐标点，提示词也救不回来，故外挂一个
标点恢复模型（p208p2002/zh-wiki-punctuation-restore），再用规则清掉两类误标：
夹在拉丁字母/数字之间的标点，以及虚词后不可能断句的逗号。
"""
from __future__ import annotations

import re

from .util import log

DEFAULT_PUNCT_MODEL = "p208p2002/zh-wiki-punctuation-restore"
BLOCK = 400        # 每次送模型的字符数
PAUSE_SENT = 0.55  # 段间停顿 ≥ 此值 → 段末给句号，否则给逗号


def restore(segments, model: str = DEFAULT_PUNCT_MODEL, comma_th: float = 0.9,
            device: str | None = None):
    """为无标点片段补标点。segments: [[start, end, text], ...]"""
    import torch
    from transformers import AutoModelForTokenClassification, AutoTokenizer

    tok = AutoTokenizer.from_pretrained(model)
    net = AutoModelForTokenClassification.from_pretrained(model)
    net.eval()
    id2label = {int(k): v for k, v in net.config.id2label.items()}

    blocks, cur, cur_len = [], [], 0
    for i, seg in enumerate(segments):
        if cur and cur_len + len(seg[2]) > BLOCK:
            blocks.append(cur)
            cur, cur_len = [], 0
        cur.append(i)
        cur_len += len(seg[2])
    if cur:
        blocks.append(cur)
    log(f"[punct] {len(segments)} 段 → {len(blocks)} 个模型窗口")

    texts, tail = {}, {}
    for bi, idxs in enumerate(blocks, 1):
        chars, spans, pos = [], [], 0
        for i in idxs:
            t = segments[i][2]
            spans.append((pos, pos + len(t), i))
            pos += len(t)
            chars.append(t)
        text = "".join(chars)

        enc = tok(text, return_offsets_mapping=True, return_tensors="pt",
                  truncation=True, max_length=512)
        offsets = enc.pop("offset_mapping")[0].tolist()
        with torch.no_grad():
            logits = net(**enc).logits[0]
        probs = torch.softmax(logits, dim=-1)
        conf, preds = probs.max(-1)
        preds, conf = preds.tolist(), conf.tolist()

        marks = {}
        for (cs, ce), p, cf in zip(offsets, preds, conf):
            if cs == ce:
                continue
            lab = id2label[p]
            if lab == "O":
                continue
            if lab == "S-，" and cf < comma_th:
                continue
            marks[cs] = lab[2:]

        for a, b, i in spans:
            buf = []
            for j, ch in enumerate(text[a:b]):
                buf.append(ch)
                mk = marks.get(a + j)
                if mk:
                    buf.append(mk)
            texts[i] = "".join(buf)
            tail[i] = marks.get(b - 1)
        if bi % 25 == 0 or bi == len(blocks):
            log(f"[punct] 窗口 {bi}/{len(blocks)}")

    out = []
    for i, (s, e, _) in enumerate(segments):
        t = texts[i]
        if tail.get(i) is None:
            if i + 1 < len(segments):
                t += "。" if (segments[i + 1][0] - e) >= PAUSE_SENT else "，"
            else:
                t += "。"
        out.append([s, e, t])
    joined = "".join(x[2] for x in out)
    log(f"[punct] 完成，标点密度 {len(joined)/max(1, sum(joined.count(c) for c in '。，？！、')):.1f} 字/处")
    return out


# Whisper 在 language="zh" 下有时吐繁体（实测 faster-whisper small 整段繁体，而 MLX
# large-v3 出简体）。文稿统一简体，所以一律过一道 opencc。
#
# 早先版本用一张手写的「繁体字符」表做触发判断，结果漏了「範」这类字，整段逃过转换——
# 判断谁需要转换本身就是件容易出错的事，不如无脑转，代价只是几秒。
_converter = None
_converter_tried = False


def _to_simplified(text: str) -> str:
    global _converter, _converter_tried
    if not _converter_tried:
        _converter_tried = True
        try:
            from opencc import OpenCC
            _converter = OpenCC("t2s")
        except Exception:
            log("[punct] 未安装 opencc，无法自动繁转简：pip install opencc-python-reimplemented")
    if _converter is None:
        return text
    return _converter.convert(text)


def clean(s: str) -> str:
    """规则清理：半角转全角、去掉不可能的断句、合并重复标点。"""
    s = re.sub(r"\s+", " ", s).strip()
    # 拉丁字母/数字之间的标点：H。ello / C，EO / 2.8。T
    s = re.sub(r"(?<=[A-Za-z0-9])[，。、；：！？](?=[A-Za-z])", "", s)
    s = re.sub(r"(?<=[A-Za-z])[，。、；：！？](?=[0-9])", "", s)
    # 虚词后不可能断句
    s = re.sub(r"(?<=成为)，", "", s)
    s = re.sub(r"(?<=[的和跟对在从把被让给也都还更最就])，", "", s)
    s = re.sub(r"，(?=[A-Za-z])", "", s)
    # 半角 → 全角
    s = s.replace(",", "，").replace("?", "？").replace("!", "！").replace(";", "；")
    s = re.sub(r"(?<!\d)\.(?!\d)", "。", s)
    s = re.sub(r"(?<!\d):(?!\d)", "：", s)
    s = s.replace("(", "（").replace(")", "）")
    # 重复/冲突标点
    for _ in range(3):
        s = re.sub(r"[，、]{2,}", "，", s)
        s = re.sub(r"([。！？；])[，、]+", r"\1", s)
        s = re.sub(r"[，、]+([。！？；])", r"\1", s)
        s = re.sub(r"([。！？；])\1+", r"\1", s)
    s = re.sub(r" +([，。！？；：、])", r"\1", s)
    return s.strip()


# 复读环：同一 3~15 字串连续出现 3 次以上（口语强调通常只重复 2 次，不动）
REPEAT3 = re.compile(r"(.{3,15}?)\1{2,}")

# Whisper 在静音段吐出的样板幻觉
BOILERPLATE = [
    "请不吝点赞", "订阅 转发 打赏", "明镜与点点栏目", "字幕由", "MING PAO",
    "谢谢大家观看", "感谢观看", "下期再见", "请使用简体中文转写",
]


def normalize(segments, drop_boilerplate: bool = True, drop_repeats: bool = True):
    """清理 + 去样板幻觉 + 截断复读环。

    返回 (片段, 统计)，统计含 dropped（丢弃样板段数）与 repeats（截断的复读环数）。
    """
    out, dropped, repeats = [], 0, 0
    for s, e, text in segments:
        t = _to_simplified(text)
        t = clean(t)
        if not t:
            continue
        if drop_boilerplate and any(b in t for b in BOILERPLATE):
            dropped += 1
            continue
        if drop_repeats:
            m = REPEAT3.search(t)
            if m:
                t = t[: m.start()] + m.group(1) + t[m.end():]
                repeats += 1
        out.append([s, e, t])
    if dropped or repeats:
        log(f"[punct] 丢弃样板幻觉 {dropped} 段、截断复读环 {repeats} 处")
    return out, {"dropped": dropped, "repeats": repeats}
