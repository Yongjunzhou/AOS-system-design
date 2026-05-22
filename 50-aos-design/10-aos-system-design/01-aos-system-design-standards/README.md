# AOS 系统设计准则

> 产品L构件：为团队M开展产品M（AOS企业运营体系）的系统设计提供设计准则支持。

本目录包含 AOS 视角独立的全部系统设计准则文档（共7份规范）：

| 文件 | 说明 | 版本 | 来源 |
|------|------|------|------|
| [01-aos-system-design-standards.md](01-aos-system-design-standards.md) | AOS 系统设计准则总纲（含 §3.3 组织资产优先原则） | v2.4 | 基于流水线 v3.10 全面修订 |
| [02-aos-original-requirements-specification.md](02-aos-original-requirements-specification.md) | AOS 原始需求规范 | v1.3 | 基于流水线 v1.5 独立适配 |
| [03-aos-stakeholder-requirements-specification.md](03-aos-stakeholder-requirements-specification.md) | AOS 相关方需求规范 | v1.2 | 基于流水线 v2.5 独立适配 |
| [04-aos-business-architecture-specification.md](04-aos-business-architecture-specification.md) | AOS 业务架构规范 | v1.3 | 基于流水线 v2.5 独立适配 |
| [05-aos-system-requirements-specification.md](05-aos-system-requirements-specification.md) | AOS 系统需求规范 | v1.2 | 基于流水线 v1.6 独立适配 |
| [06-aos-product-architecture-specification.md](06-aos-product-architecture-specification.md) | AOS 产品架构规范 | v1.2 | 基于流水线 v1.8 独立适配（仅保留软件产品视图） |
| [07-aos-system-design-terminology-glossary.md](07-aos-system-design-terminology-glossary.md) | AOS 术语对照表 | v1.1 | 基于流水线 v1.4 独立适配（含 PA 分解三因素术语和绩效考核业务领域术语） |

**版本策略**：
- 通用方法论核心（五层结构、三条核心规则、基本术语、验收标准）基于 [`00-general/10-general-design-standards/01-general-design-standards.md`](../../../../00-general/10-general-design-standards/01-general-design-standards.md) 通用准则
- 流水线领域的参考示例基于产品L（`10-pipeline-design/.../01-pipeline-system-design-standards/`）的对应文档，通过"依据B分离模式"进行独立适配
- **适配原则**：核心方法论保持不变，所有示例从流水线领域替换为 AOS 绩效考核领域
- 规范内容随通用标准和流水线版本迭代同步更新

适用于产品M系统设计过程（阶段1）。
