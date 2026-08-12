---
name: pending-memory-ba-bp-term
description: 记忆库中 ba-* 系列记忆仍用旧设计链术语 BA（业务架构），2026-08-11 起设计链第三层改为 BP（业务流程），待批量更新
metadata:
  type: project
---

2026-08-11 起设计链第三层术语 BA（业务架构）→ BP（业务流程），仓库文档已全量同步（提交 a6f719a + 35dfd34，2026-08-12）。但 `.claude/memory/` 中多个记忆仍用旧 BA 术语：ba-ipo-generalization、ba-two-product-types-output-product-role-scenario、ba_method_naming_output_product_anchoring、ba-ipo-definition-current、ba-five-level-hierarchy、ba_existence_reason、pipeline_class_derivation、project_ba_hierarchy、end_to_end_business_framework 等。

**待办**：逐条更新这些记忆文件的 BA→BP（仅设计链语境），保留"业务架构管理员"角色名与 4A 域 BA（07-generalspec-architecture-fundamentals §8）。

**Why**：记忆会在未来会话被加载，旧 BA 术语会误导后续写作与审查的术语一致性。
**How to apply**：处理时逐文件审查，区分设计链 BP 与 4A 域 BA；更新后同步到本机 auto-memory 路径。相关 [[feedback-layer-table-as-authority]]。
