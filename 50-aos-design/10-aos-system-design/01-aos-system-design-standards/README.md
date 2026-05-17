# AOS 系统设计准则

> 产品B构件：为团队A开展产品A（AOS企业运营体系）的系统设计提供设计准则支持。

本目录包含 AOS 视角独立的全部系统设计准则文档（共7份规范 + 1份模板）：

| 文件 | 说明 | 版本 | 来源 |
|------|------|------|------|
| [00-specification-template.md](00-specification-template.md) | 规范文档通用模板 | v 参考流水线 | 引用流水线通用模板 |
| [01-system-design-standards.md](01-system-design-standards.md) | AOS 系统设计准则总纲 | v1.0 | 基于流水线 v3.3 独立适配 |
| [02-original-requirements-specification.md](02-original-requirements-specification.md) | AOS 原始需求规范 | v1.0 | 基于流水线 v1.2 独立适配 |
| [03-stakeholder-requirements-specification.md](03-stakeholder-requirements-specification.md) | AOS 相关方需求规范 | v1.0 | 基于流水线 v2.2 独立适配 |
| [04-business-architecture-specification.md](04-business-architecture-specification.md) | AOS 业务架构规范 | v1.0 | 基于流水线 v2.1 独立适配 |
| [05-system-requirements-specification.md](05-system-requirements-specification.md) | AOS 系统需求规范 | v1.0 | 基于流水线 v1.2 独立适配 |
| [06-product-architecture-specification.md](06-product-architecture-specification.md) | AOS 产品架构规范 | v1.0 | 基于流水线 v1.4 独立适配（仅保留软件产品视图） |
| [07-terminology-glossary.md](07-terminology-glossary.md) | AOS 术语对照表 | v1.0 | 基于流水线 v1.2 独立适配（含绩效考核业务领域术语） |

**版本策略**：
- 所有规范基于流水线产品B（`00-pipeline-design/.../01-system-design-standards/`）的对应文档，通过"依据B分离模式"进行独立适配
- **适配原则**：核心方法论（五层结构、三条核心规则）保持不变，所有示例从流水线领域替换为 AOS 绩效考核领域
- 规范内容随流水线版本迭代同步更新

适用于产品A系统设计过程（阶段1）。
