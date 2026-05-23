# EOS 系统设计准则

> 设计线构件：为团队M开展EOS（企业运营体系）的系统设计提供设计准则支持。

本目录包含 EOS 视角独立的全部系统设计准则文档（共7份规范）：

| 文件 | 说明 | 版本 | 来源 |
|------|------|------|------|
| [01-eos-system-design-standards.md](01-eos-system-design-standards.md) | EOS 系统设计准则总纲（含 §3.3 组织资产优先原则） | v2.4 | 基于流水线 v3.10 全面修订 |
| [02-eos-original-requirements-specification.md](02-eos-original-requirements-specification.md) | EOS 原始需求规范 | v1.3 | 基于流水线 v1.5 独立适配 |
| [03-eos-stakeholder-requirements-specification.md](03-eos-stakeholder-requirements-specification.md) | EOS 相关方需求规范 | v1.2 | 基于流水线 v2.5 独立适配 |
| [04-eos-business-architecture-specification.md](04-eos-business-architecture-specification.md) | EOS 业务架构规范 | v1.3 | 基于流水线 v2.5 独立适配 |
| [05-eos-system-requirements-specification.md](05-eos-system-requirements-specification.md) | EOS 系统需求规范 | v1.2 | 基于流水线 v1.6 独立适配 |
| [06-eos-product-architecture-specification.md](06-eos-product-architecture-specification.md) | EOS 产品架构规范 | v1.2 | 基于流水线 v1.8 独立适配（仅保留软件产品视图） |
| [07-eos-system-design-terminology-glossary.md](07-eos-system-design-terminology-glossary.md) | EOS 术语对照表 | v1.1 | 基于流水线 v1.4 独立适配（含 PA 分解三因素术语和绩效考核业务领域术语） |

**版本策略**：
- 通用方法论核心（五层结构、三条核心规则、基本术语、验收标准）基于 [`00-general/10-general-system-design-standards/01-general-system-design-standards.md`](../../../../00-general/10-general-system-design-standards/01-general-system-design-standards.md) 通用准则
- 流水线领域的参考示例基于设计线（`10-pipeline-design/.../01-pipeline-system-design-specification/`）的对应文档，通过"依据B分离模式"进行独立适配
- **适配原则**：核心方法论保持不变，所有示例从流水线领域替换为 EOS 绩效考核领域
- 规范内容随通用标准和流水线版本迭代同步更新

适用于EOS系统设计过程（阶段1）。
