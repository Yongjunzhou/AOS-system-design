---
name: or-baseline-management-zone-simplification
description: OR 基线文档管理区精简为元信息+状态表两项，移除详细条目区和需求统计区
metadata:
  type: project
---

OR 基线文档（`01-eos-original-requirements.md`）管理区精简为仅含两项：文档元信息 + OR基线条目进展状态及处理建议一览表（父子行状态表）。

**移除的内容：**
- OR 基线条目区（`### OR-XXX` 详细条目段落）—— 与正文区分析建议块内容重复
- 需求统计区（`### 需求统计` 占位）—— 可从 1.4 子表推导，冗余

**设计依据：**
- OR 基线条目区的详细内容（描述、指标、出处等）在正文区分析建议块中已有，执行后正文区原地保留，无需在管理区重复存放
- OR 基线条目区中的分解子项（`OR-XXX-a → SR-PF-00XX`）是 t01 将规范化 OR 分配到 SR 架构节点的产出，应属于 SR 架构文档（`02-eos-stakeholder-requirements-architecture.md`），不应放在 OR 基线文档中

**Why:** 消除管理区与正文区的内容重复，厘清文档职责边界——OR 基线文档仅追踪 OR 自身状态和摘要，t01 的分解映射结果由 SR 架构文档承载。

**How to apply:** 后续所有 Skill 中涉及 OR 基线管理区的操作，仅指向状态表的更新（由 1.4 子表推导），不再写入段落格式的详细 OR 条目。OR 条目详细内容始终在正文区。
