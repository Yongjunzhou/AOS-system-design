---
name: product_relationship_reframe_complete
description: 产品M（AOS）与产品L的关系重构完成，以及更名记录——两层产品关系→三层工作层面，涉及两个设计准则文档
metadata: 
  node_type: memory
  type: project
  originSessionId: 821932d6-dd45-456c-85f4-e0e3230cd701
---

2026-05-22 完成了产品M（AOS）与产品L关系的全面重构。2026-05-22 renamed: 产品A→产品M, 产品B→产品L.

**核心变更**：将"两层产品关系"（工具—目标）重构为"三层工作层面"（第1层自指设计、第2层交付物构建、第3层使用工具设计产品M）

**涉及文档**：
- `10-pipeline-design/.../01-pipeline-design-standards.md` v3.6→v3.7
- `50-aos-design/.../01-aos-system-design-standards.md` v2.0→v2.1

**术语统一**：
- "两层产品关系" → "三层工作层面"
- "方法论/工具产品" → "知识/方法类产品" 
- "直接复用/模板化复用/模板复用" → "直接参考/结构化参考/模板参考"
- "自指关系" 定义对齐术语表
- 移除 "机载设备"/"经营管理" 领域限定词

**审查确认**：AOS 设计准则通过 28 轮规则符合性审查（规则文档：CLAUDE.md + README.md + 01-general-design-standards.md），24 轮语义审查全部通过，无规则违反。

**Why:** 两层关系模型过于简化，无法清晰表达"谁为谁生产什么"的分工——三个工作层面（自指设计→交付物构建→使用工具设计）更准确地描述了团队L和团队M之间的协作边界。
**How to apply:** 后续所有涉及产品M与产品L关系的讨论、文档编写和审查，使用三层工作层面框架。仓库路径对应关系：第1层→`10-pipeline-design/`、第2层→`50-aos-design/.../{01,02,03,04}-*`、第3层→`50-aos-design/.../10-product-data/`。
