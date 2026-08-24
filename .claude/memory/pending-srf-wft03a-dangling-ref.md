---
name: pending-srf-wft03a-dangling-ref
description: 92-srf 悬空引用 wft03a —— 已解决（2026-08-17 修复）：wft03a/wft03b 旧模型已废弃，引用改现行 wft03-biz/eng
metadata:
  type: project
---

2026-08-12 发现 `92-srf-classification-spec.md` 引用不存在的 `eos-wft03a-ba2sr-design.md`，且概述提及"wft03a/wft03b"与现行文件不符。

**2026-08-17 已解决**：wft03a/wft03b 旧 a-b 对模型已废弃（归档 `90-hold/legacy-a-b-pairs/`），现行模型是 `eos-wft03-biz-bpd2sfh.md` / `eos-wft03-eng-bpd2sfh.md`。已把 92-srf 三处引用改现行文件（概述"wft03a/wft03b"→"wft03-biz/wft03-eng"、设计模式参考、§六 关系表），版本 v1.0→v1.1。

**Why**：悬空引用会让 92-srf 的读者/AI 找不到被引文件，破坏可执行规则的可追溯性。
**How to apply**：已解决，无待办。若后续 wft03 再重构，同步检查 92-srf 引用。相关 [[91-spec-v4-engine-restructure]]。
