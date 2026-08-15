---
name: ort01-feedback-git-baseline-protocol
description: ort01 反馈回路已重设计为 git 基线协议（人类方案 v0.41 / SKILL v2.24 / 91 v5.16，Step 1-6）；评审发现与待办见 02-eos-sysdev-review.md
metadata:
  type: project
---

ort01（人类方案 `eos-ort01-chunk.md` v0.41 / SKILL v2.24 / 91 §A.5 特化 v5.16）反馈回路已重设计为 **git 基线协议**（2026-08-15 审视落地 + 修复闭环）：

- **反馈单源**：人类直接编辑**文本化文档**（方案块/反馈区）表达反馈；切分文件是双方一致后的结果、不是反馈载体；AI 不写反馈区。
- **检测**：Step 1 `git diff <基线>` 检出变更 → 判读意图 → 记录到表 A `内容摘要`。基线 = 最近 AI 提交（`scripts/ai-commit.sh`，author=EOS-AI + `[AI]` 前缀 + Co-Authored-By）。
- **记录格式（v0.39 定义）**：内容摘要 = 「阶段摘要 ∥ 反馈记录」——有反馈时以 `‖ 反馈：<类型>（<要点>）` 分段追加（类型=调整/同意/确认不拆分/废弃/重新切分）；Step 2 处理完在记录末追 `[已处理]`。Step 2 入口判定 = 内容摘要含 `反馈：` 且无 `[已处理]`，按生命周期分流（`切分方案待确认` → 调整/同意/不拆分/废弃；`已切分` → 重切）。执行切分时阶段摘要写「已切分 N 片（见表 B）」（F2 裁决 B：切片清单归表 B，表 A「文本化文档」列始终指向 `.textualized.md`）。
- **步骤**：Start / **1** 变更检测与反馈汇总 / **2** 反馈处理（读表 A 记录执行）/ **3** 新增处理 / **4** 提交基线（ai-commit + 记录 hash 到状态文档 `HEAD @上次AI运行` 字段）/ **5** 反馈交互（输出三区摘要 + 对话收集，执行模式=对话）/ **6** 变更汇总（「汇总」口令 → 表 A + 提交，**同 Step 4 机制全量提交、交接即完整基线**；对话窗内文档编辑随汇总纳入基线，线下/运行后编辑由 Step 1 兜底）。Step 1~4 运行内自动；Step 5/6 为交互协议步骤（由人类结束/触发）。
- **原则**：先反馈后新增；交互前先提交；**交互只记录不处理**——对话反馈在「汇总」时统一记录到表 A，处理由 Step 2 基于记录执行；正文区原文被改 = 非切分反馈（保留提交、不记录、提示人类）。
- **基建**：`scripts/ai-commit.sh` 新建；状态文档与 ort00 §4.2 模板已补 `HEAD @上次AI运行` 字段；91 §A.5 补预处理链特化（试点 ort01，以 Step 4/5/6 替代通用「Step End」）。

**评审上下文**：第一轮发现 F1~F10、决策 D1~D8；第二轮（v0.38/v2.21 审视）发现 F11~F19 并已修复（人类方案 v0.41 / SKILL v2.24 / ort00 v0.25 / ort03 v0.33），决策 D9~D13 定案——**D11/F14 改判为 B：Step 6 恢复同 Step 4 机制全量提交（交接即完整基线）**；**F2 已裁决（D13，B）：表 A「文本化文档」列始终指向 `.textualized.md`，切片清单归表 B**。全部登记在仓库 `20-pl4eos/80-pl4eos-2-eosdata/00-origin-requirement-materials/02-eos-sysdev-review.md`。

**How to apply:** 继续审视 ort01 时，先读登记簿获取发现与待办；反馈机制按 git 基线协议理解（无对话口令方案反馈、AI 不写反馈区）。链级推广（ort00/02/03 加同构 Step 1）为登记簿待办。相关记忆：[[ort01-chunk-align-scene-business]]、[[chunk-file-three-segment-dual-track]]、[[ort01-three-category-focus-rows]]。
