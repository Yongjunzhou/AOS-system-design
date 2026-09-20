"""LLM 环节：分段理解（map）→ 要点摘要（reduce）；顺带产出专有名词校正表。

这一步是整条流水线里唯一无法用确定性代码替代的部分：判别"哪里听错了"和
"这期在讲什么"都依赖语义理解。脚本负责的是把长稿切窗、并发/顺序调用、
合并结果、以及对校正表做安全性校验（原文里必须真的出现、过于常见的词一律拒绝）。
"""
from __future__ import annotations

import json
import re

from .util import log, ts

MAP_SYSTEM = """你是中文播客转写稿的整理助手。用户给你一段机器转写的播客文稿（每行形如 `[时:分:秒] 正文`）。
请完成两件事，只输出 JSON：

1. `要点`：这段讲了什么。逐条给 `{"时间": "时:分:秒", "内容": "..."}`，时间取该要点开始的时刻，
   内容要写具体的人名、公司、数字、判断，不要写空话。8~20 条。
2. `校正`：指出这段里**因语音识别造成的**专有名词／术语错误。逐条给
   `{"识别": "稿中实际出现的错串", "应为": "正确写法", "依据": "判断来源"}`。

`校正` 的硬要求：
- `识别` 必须是文稿里**真实出现过的字面串**（原样复制，不要改写、不要臆造）。
- 只列人名、公司名、产品名、书名、专业术语、成语这类确定性错误。
- 语境依赖的普通词（例如「成绩」可能是「层级」也可能是真的「成绩」）一律不要列。
- 拿不准的不要列；宁可少列。没有就返回空数组。
- 依据写清判断来源，如「节目官方简介」「上下文指某公司」「人名统一」。
"""

REDUCE_SYSTEM = """你是中文播客整理助手。用户给你一档播客的元信息与**按时序排列的分段要点**，
请据此写出这期的整合版要点摘要。只输出 JSON，字段如下：

{
  "一句话主旨": "200 字以内，说清这期的核心论点",
  "时间轴": [{"时间": "时:分:秒–时:分:秒", "内容": "..."}],
  "核心观点": [{"标题": "小标题", "正文": "一段解释"}],
  "值得记住的一段": {"语境": "这段话出现的场合与上下文", "引文": "最有力量的原话"}
}

要求：
- `时间轴` 覆盖全程、按时序，每条用**粗体**点出该段主题词，写具体的人、公司、数字、判断。
- `核心观点` 7~10 条，抓非共识判断与具体类比、数字，不要复述时间轴。
- 只依据给定的分段要点，不要引入未出现的内容，也不要编造引文。
"""


def _seg_lines(items, limit: int | None = None) -> str:
    out = []
    for s, _e, t in items:
        out.append(f"[{ts(s)}] {t}")
    text = "\n".join(out)
    return text[:limit] if limit else text


def map_windows(llm, windows, known_names=None, progress=log):
    """逐窗理解。返回 (要点列表, 校正列表)。

    known_names 是标题/节目信息里能确定的真实人名（主播、嘉宾），写进提示词，
    否则模型容易漏掉「小骏→小珺」这类同音错写。
    """
    points, corrections = [], []
    names = [n for n in (known_names or []) if n]
    known = ""
    if names:
        known = ("本期已知人名（来自标题与节目信息，请特别注意稿中是否有音近的错写）："
                 + "、".join(names) + "。\n\n")
    for i, win in enumerate(windows, 1):
        span = f"{ts(win[0][0])}–{ts(win[-1][1])}"
        progress(f"[llm] 分段理解 {i}/{len(windows)} {span}（{sum(len(x[2]) for x in win)} 字）")
        try:
            data = llm.chat_json(MAP_SYSTEM, f"{known}本段覆盖节目时间 {span}。\n\n{_seg_lines(win)}")
        except Exception as exc:
            progress(f"[llm] 第 {i} 窗失败，跳过：{exc}")
            continue
        for p in data.get("要点", []) or []:
            if p.get("内容"):
                points.append({"时间": str(p.get("时间", "")).strip(), "内容": str(p["内容"]).strip()})
        for c in data.get("校正", []) or []:
            if c.get("识别") and c.get("应为"):
                corrections.append({
                    "识别": str(c["识别"]).strip(),
                    "应为": str(c["应为"]).strip(),
                    "依据": str(c.get("依据", "")).strip(),
                    "窗口": i,
                })
    return points, corrections


COMPRESS_SYSTEM = """你是中文播客整理助手。用户给你一批（按时序的）分段要点，条数偏多。
请把它们**合并压缩**成不超过 15 条，保留时间信息与关键的人名、公司、数字、判断，
合并同一话题的相邻条目，丢掉重复与空话。只输出 JSON：{"要点": [{"时间": "时:分:秒", "内容": "..."}]}
"""


def compress_points(llm, points, per_batch: int = 60, progress=log):
    """分段要点过多时先分层压缩，避免汇总调用超出模型输出预算。"""
    out = []
    for i in range(0, len(points), per_batch):
        batch = points[i: i + per_batch]
        lines = [f'- {p["时间"]} {p["内容"]}' for p in batch]
        progress(f"[llm] 压缩要点 {i//per_batch + 1}/{-(-len(points)//per_batch)}（{len(batch)} 条）")
        try:
            data = llm.chat_json(COMPRESS_SYSTEM, "\n".join(lines))
            got = [{"时间": str(p.get("时间", "")).strip(), "内容": str(p.get("内容", "")).strip()}
                   for p in (data.get("要点") or []) if p.get("内容")]
            out.extend(got or batch)
        except Exception as exc:
            progress(f"[llm] 压缩失败，保留原批次：{exc}")
            out.extend(batch)
    return out


def reduce_summary(llm, meta: dict, points, progress=log):
    """把分段要点汇总成整期要点摘要。条数过多时先分层压缩。"""
    while len(points) > 80:
        points = compress_points(llm, points, progress=progress)
    lines = [f'- {p["时间"]} {p["内容"]}' for p in points]
    head = (
        f"播客：{meta.get('podcast','')}\n"
        f"期号：{meta.get('episode_no','')}\n"
        f"标题：{meta.get('title','')}\n"
        f"主播：{meta.get('host','')}\n"
        f"嘉宾：{meta.get('guest','')}\n"
        f"时长：{meta.get('duration_text','')}\n"
    )
    progress(f"[llm] 汇总要点（{len(points)} 条分段要点）")
    return llm.chat_json(REDUCE_SYSTEM, f"{head}\n分段要点如下：\n" + "\n".join(lines),
                         max_tokens=8192)


def dedupe_corrections(corrections, full_text: str, max_hits: int = 30):
    """校验校正表：识别串必须在原文出现；过于常见或疑似误伤的一律拒绝。

    同一错串在不同窗口给出不同答案时**保留先到的那个**并记录冲突——早先的实现把两条
    都丢掉，会连带丢掉正确的那条。
    """
    seen, kept, rejected, conflicts = {}, [], [], []
    for c in corrections:
        wrong, right = c["识别"], c["应为"]
        if wrong == right:
            continue
        if wrong in seen:
            if seen[wrong]["应为"] != right:
                conflicts.append((wrong, seen[wrong]["应为"], right))
            continue
        hits = full_text.count(wrong)
        if hits == 0:
            rejected.append((wrong, "原文中不存在，疑似模型臆造"))
            continue
        if hits > max_hits:
            rejected.append((wrong, f"原文出现 {hits} 次，疑似常见词，拒绝全局替换"))
            continue
        seen[wrong] = c
        kept.append(c)
    return kept, rejected, conflicts


VERIFY_SYSTEM = """你是中文文稿的校对。用户给出若干「疑似语音识别错误」的候选，每条附它在稿中的上下文。
逐条判断：`accept`（确认该改）、`reject`（不该改、或拿不准）、`amend`（该改，但正确写法与候选不同）。
只输出 JSON：{"结果": [{"识别": "候选里的错串", "应为": "最终正确写法", "判定": "accept|reject|amend", "理由": "..."}]}

判定务必保守：拿不准就 reject——错改比不改更糟。
特别注意：如果上下文（或并列出现的同一说法）里已经有正确写法，以它为准。
例如稿中同一句既出现「红历史」又出现「从历史」，正确写法应是「从历史」，而不是另造一个词。
"""


def verify_corrections(llm, corrections, segments, known_names=None, span: int = 45, progress=log):
    """对校正候选做上下文复核，剔掉"改错方向"的条目。

    map 阶段模型只看到局部，容易把「红历史」猜成「人类历史」；这里把候选连同它在稿中的
    真实上下文再交给模型判一次，并要求它优先采信稿中已出现的正确写法。

    known_names 是节目信息里能确定的人名，必须一并给出——否则复核会因为「稿中查不到
    正确写法」而否掉「小骏→小珺」这种本来就只能靠节目信息确认的修正。
    """
    if not corrections:
        return [], []
    names = [n for n in (known_names or []) if n]
    head = ("本期已知人名（权威，来自标题与节目信息）：" + "、".join(names) + "。\n\n") if names else ""
    full = "".join(s[2] for s in segments)
    items = []
    for c in corrections:
        wrong = c["识别"]
        ctxs, pos = [], 0
        while len(ctxs) < 3:
            i = full.find(wrong, pos)
            if i < 0:
                break
            ctxs.append(full[max(0, i - span): i + len(wrong) + span])
            pos = i + len(wrong)
        items.append({"识别": wrong, "应为": c["应为"], "次数": full.count(wrong),
                      "上下文": ctxs})
    user = head + json.dumps(items, ensure_ascii=False, indent=1)
    try:
        data = llm.chat_json(VERIFY_SYSTEM, user)
    except Exception as exc:
        progress(f"[llm] 校正复核失败，保留全部候选：{exc}")
        return corrections, []

    verdicts = {r.get("识别"): r for r in (data.get("结果") or [])}
    kept, rejected = [], []
    for c in corrections:
        v = verdicts.get(c["识别"])
        if not v:
            kept.append(c)
            continue
        judge = str(v.get("判定", "")).lower()
        if judge == "reject":
            rejected.append((c["识别"], v.get("理由", "复核判定不该改")))
            continue
        if judge == "amend" and v.get("应为"):
            c = dict(c, 应为=str(v["应为"]).strip(), 依据=(v.get("理由") or c.get("依据", "")))
        kept.append(c)
    return kept, rejected


def apply_corrections(segments, corrections):
    """应用校正表，返回 (新片段, [[识别, 应为, 处数, 依据], ...])。"""
    table, texts = [], None
    for c in corrections:
        n = sum(s[2].count(c["识别"]) for s in segments)
        if n:
            table.append([c["识别"], c["应为"], n, c.get("依据", "")])
    out = []
    for s, e, text in segments:
        for c in corrections:
            if c["识别"] in text:
                text = text.replace(c["识别"], c["应为"])
        out.append([s, e, text])
    table.sort(key=lambda r: -r[2])
    return out, table


def correct_any(obj, corrections):
    """递归地把校正表套用到任意嵌套结构里的字符串（用于回灌分段要点与摘要）。

    摘要是基于转写稿生成的，若不回灌，摘要里会残留「曾敏」而正文已是「曾鸣」。
    """
    if isinstance(obj, str):
        for c in corrections:
            if c["识别"] in obj:
                obj = obj.replace(c["识别"], c["应为"])
        return obj
    if isinstance(obj, list):
        return [correct_any(x, corrections) for x in obj]
    if isinstance(obj, dict):
        return {k: correct_any(v, corrections) for k, v in obj.items()}
    return obj


def guest_from_title(title: str) -> str:
    """从「153. 和曾鸣聊产业史观：…」里猜嘉宾名。"""
    m = re.search(r"[和跟与]\s*([\u4e00-\u9fff]{2,4})\s*(?:聊|谈|对话|对谈)", title)
    if m:
        return m.group(1)
    m = re.search(r"对话\s*([\u4e00-\u9fff]{2,4})", title)
    if m:
        return m.group(1)
    return ""
