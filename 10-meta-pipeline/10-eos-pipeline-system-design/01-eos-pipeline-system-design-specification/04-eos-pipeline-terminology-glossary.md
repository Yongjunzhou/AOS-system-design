# EOS 流水线系统设计术语对照表
**EOS Pipeline System Design — Terminology Glossary**

**文档版本**：v2.0
**创建日期**：2026-05-28
**用途**：统一 EOS 流水线系统设计领域的英中术语对照，便于文档写作和国际交流。

---

## 核心概念

| 中文 | 英文 | 说明 |
|------|------|------|
| EOS 流水线 | EOS Pipeline | 服务于 EOS 全生命周期的流水线，由设计线/开发线/集成线/运维线四子线组成 |
| 元流水线 | Meta-Pipeline | 用于设计 EOS 流水线的流水线，当前处于系统设计阶段 |
| 输出产品架构锚定法 | Output Product Architecture Anchoring Method | 流水线类产品的 BA 开发特化方法：以输出产品的 PA 节点类型为推导锚点 |
| 用户角色架构锚定法 | User Role Architecture Anchoring Method | BA 开发的通用方法：以全量用户角色集为推导锚点 |
| 四类构件 | Four Component Types | EOS 流水线 PA 的四类交付物：设计准则、设计指南、AI 辅助文档、任务定义 |

## 三层工作层面

| 中文 | 英文 | 说明 |
|------|------|------|
| 第1层：流水线设计 | Layer 1: Pipeline Design | 用元流水线对 EOS 流水线进行系统设计，产出其产品架构 |
| 第2层：构件开发 | Layer 2: Component Development | 根据 PA 构件定义开发各构件的完整内容（准则/指南/AI辅助/任务定义） |
| 第3层：使用工具设计 EOS | Layer 3: EOS Design Using Tools | EOS 开发者使用第2层产出的工具对 EOS 进行系统设计 |

## 三个参与者

| 中文 | 英文 | 说明 |
|------|------|------|
| 流水线开发者 | Pipeline Developer | 开发、维护和优化 EOS 流水线本身 |
| AI | AI | 按流水线开发者指令执行自动化设计操作 |
| EOS 构建与运维者 | EOS Builder & Operator | 使用 EOS 流水线对 EOS 进行系统设计、开发、集成和运维 |

## 五层设计结构

| 层级 | 中文 | 英文 | 角色 |
|------|------|------|------|
| 第1层 | 原始需求 | Original Requirements (OR) | 仅需求 |
| 第2层 | 相关方需求 | Stakeholder Requirements (SR) | 需求/方案 |
| 第3层 | 业务架构 | Business Architecture (BA) | 仅方案 |
| 第4层 | 系统需求 | System Requirements (SysReq) | 需求/方案 |
| 第5层 | 产品架构 | Product Architecture (PA) | 仅方案 |

## 需求类型

| 中文 | 英文 | 说明 |
|------|------|------|
| 功能需求 | Functional Requirement (FR) | 系统必须执行的功能或服务，经 BA 路径分配 |
| 非功能需求 | Non-Functional Requirement (NFR) | 系统必须满足的质量属性，经平行路径分配 |
| 末级需求 | Leaf-level Requirement | 不可再分的原子粒度需求条目 |
| 架构末级节点 | Architecture Leaf Node | 方案文档树形结构的末级节点，承接上层需求 |
| 详细定义末级节点 | Detailed Definition Leaf Node | 对架构末级节点的细化分解，分配到下层方案 |

## 文档结构

| 中文 | 英文 | 说明 |
|------|------|------|
| 架构定义子文档 | Architecture Definition Sub-document | 树形结构组织内容，建立对上层需求的映射 |
| 详细定义子文档 | Detailed Definition Sub-document | 平铺列表对架构末级节点进行细化分解 |
| 需求/方案相对 | Requirement-Solution Relativity | 同一文档在不同层位兼具需求与方案双重身份 |
| 文档结对 | Document Pairing | 上层需求文档与下层方案文档成对设计 |

## 三个核心设计活动

| 中文 | 英文 | 说明 |
|------|------|------|
| 需求分解 | Requirements Decomposition | 将需求分解到原子粒度（语义分解四项自检 + 指标分解三场景） |
| 需求分配 | Requirements Allocation | 将末级条目按 1:1 约束映射到下层架构末级节点 |
| 符合性分析 | Compliance Analysis | 验证方案节点充分满足所承接的上层需求（语义 + 指标） |

## 设计约束

| 中文 | 英文 | 说明 |
|------|------|------|
| 1:1 分配约束 | One-to-One Allocation Constraint | 每条详细定义末级分配到下层唯一的架构末级节点 |
| N:1 承接 | Many-to-One Acceptance | 每个架构末级节点可承接多条上层末级条目 |
| 双向追溯 | Bidirectional Traceability | OR→PA 正向和 PA→OR 反向均可追踪 |
| 资产优先 | Organizational Asset Priority | 按复用→改进→新增优先级处理架构变更 |

## PA 节点定义三因素

| 中文 | 英文 | 说明 |
|------|------|------|
| 知识领域内聚性 | Knowledge Domain Cohesion | 操作同一知识领域的 SysReq 倾向合并为同一构件 |
| 质量要求相容性 | Quality Requirement Compatibility | 质量属性冲突的需求不应共享同一构件 |
| 交付形态相似性 | Delivery Form Similarity | 信息处理模式相同的需求倾向合并（同模式可共享，不同模式应分离） |
| 三因素决策矩阵 | Three-Factor Decision Matrix | 综合三因素判断 PA 构件合并/分离的决策工具 |

## 信息处理模式

| 中文 | 英文 | 说明 |
|------|------|------|
| 规范规则 | Standards & Rules | 条文式约束，人查阅/对照/引用 |
| 操作指南 | Operational Guide | 场景化指导，人阅读/理解/应用 |
| AI 指令 | AI Instructions | 结构化 Prompt，AI 直接解析执行 |
| 操作规程 | Operational Procedure | 分步骤任务，人+AI 协作执行 |
| 数据模板 | Data Template | 结构化数据框架，人+工具填写 |

## 四种设计场景

| 中文 | 英文 | 说明 |
|------|------|------|
| 瀑布式 | Waterfall | 从零开始的正向完整设计（OR→SR→BA→SysReq→PA） |
| 敏捷式 | Agile | 在现有设计基础上的增量迭代 |
| 逆向工程 | Reverse Engineering | 从已有构件反向推导至 OR |
| DevOps | DevOps | 最小化正向变更的快速修复 |

## 文档名称对照

| 中文 | 英文 | 文件名 |
|------|------|--------|
| EOS 流水线系统设计准则 | EOS Pipeline System Design Standards | 01-eos-pipeline-system-design-standards.md |
| 术语对照表 | Terminology Glossary | 04-eos-pipeline-terminology-glossary.md |
| 瀑布式设计指南 | Waterfall System Design Guide | 01-waterfall-eos-pipeline-system-design-guide.md |
| 逆向工程设计指南 | Reverse Engineering System Design Guide | 02-reverse-engineering-eos-pipeline-system-design-guide.md |
| 敏捷式设计指南 | Agile System Design Guide | 03-agile-eos-pipeline-system-design-guide.md |
| DevOps 设计指南 | DevOps System Design Guide | 04-devops-eos-pipeline-system-design-guide.md |
| 快速参考卡 | Quick Reference Card | 05-eos-pipeline-system-quick-reference-card.md |

---

## 术语使用示例

### 需求 vs 方案
- "原始需求、相关方需求、系统需求" — Original Requirements, Stakeholder Requirements, System Requirements
- "相关方需求是原始需求的方案" — Stakeholder Requirements are the solution to Original Requirements

### 分解 vs 分配 vs 符合性
- "将需求分解到末级" — Decompose requirements to leaf level
- "将末级条目分配到下层架构节点" — Allocate leaf items to lower-level architecture nodes
- "验证方案满足需求" — Verify solution satisfies requirements

---

**文档版本**：v2.0
**状态**：✅ 完成
