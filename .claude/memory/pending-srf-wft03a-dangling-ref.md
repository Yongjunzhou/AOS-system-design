---
name: pending-srf-wft03a-dangling-ref
description: 92-srf-classification-spec.md 引用不存在的 eos-wft03a-ba2sr-design.md，且 wft03a/wft03b 概念与实际文件（wft03-biz/eng-bp2sr）不符，待裁决
metadata:
  type: project
---

2026-08-12 在 BA→BP 术语完整同步时发现：`92-srf-classification-spec.md` 第 7/312 行引用 `eos-wft03a-ba2sr-design.md`，但该文件不存在；第 3 行概述提及"wft03a/wft03b 执行 SR-F 分类设计"，与实际文件（仅 `eos-wft03-biz-bp2sr` / `eos-wft03-eng-bp2sr`）不符。

**待办**：需裁决——(a) 重建 `eos-wft03a-bp2sr-design.md` 并更新 92-srf 引用；(b) 将 92-srf 引用改为实际存在的 wft03-biz/eng 文件；(c) 删除悬空引用。涉及 wft03a/wft03b 概念是否仍有效。

**Why**：悬空引用会让 92-srf 的读者/AI 找不到被引文件，破坏可执行规则的可追溯性。
**How to apply**：下次审视 92-srf 或 wft03 系列时处理；裁决前保持现状，不擅自创建/删除文件。相关 [[91-spec-v4-engine-restructure]]。
