# 通用术语对照表
**General Terminology Glossary**

**文档版本**：v1.0
**创建日期**：2026-05-18
**用途**：统一与具体产品无关的核心设计术语，便于国际化和技术交流。

---

## 一、文档类型

| 中文 | 英文 | 说明 |
|------|------|------|
| 准则 | Standards / Principles | 理论基础、规范要求、设计原则 |
| 指南 | Guide / Handbook | 实践指导、操作步骤、工作手册 |
| 参考卡 | Quick Reference Card | 快速查阅、速记、便携版 |
| 索引 | Index | 导航、查找工具 |
| 规范 | Specification | 针对特定设计层的详细规范和标准 |

---

## 二、5层结构

| 中文 | 英文 | 说明 |
|------|------|------|
| 原始需求 | Original Requirements (OR) | 第1层，用户或相关方的原始需求 |
| 相关方需求 | Stakeholder Requirements (SR) | 第2层，原始需求的方案和后续需求 |
| 业务架构 | Business Architecture (BA) | 第3层，相关方需求功能部分的方案 |
| 系统需求 | System Requirements (SysReq) | 第4层，业务架构和非功能需求的方案 |
| 产品架构 | Product Architecture (PA) | 第5层，系统需求的方案和实现 |

---

## 三、基本术语

| 中文 | 英文 | 说明 |
|------|------|------|
| 需求文档 | Requirements Document | 描述系统应该做什么（What） |
| 方案文档 | Solution Document | 描述如何满足需求（How），由架构定义和详细定义组成 |
| 需求—方案配对 | Requirement-Solution Pair | 需求与方案成对出现，需求是对方案的要求，方案是对需求的满足 |
| 文档的双重属性 | Dual Role of Document | 一个文档可同时扮演两种角色——对上层的方案和对下层的需求 |
| 架构定义 | Architecture Definition | 以架构末级节点为基本单位，构建方案的层级结构并建立对上层需求的映射 |
| 详细定义 | Detailed Definition | 对架构末级节点进行详细设计分解，使每条末级条目在后续方案的架构中有唯一的承接点 |
| 架构末级节点 | Architecture Leaf Node | 方案分类和组织的最大条目，是需求映射的关键层级 |
| 详细定义末级节点 | Detailed Definition Leaf Node | 对架构末级节点分解后得到的末级条目，是分配到后续方案架构末级节点的源头 |
| 详细定义的双重身份 | Dual Identity of Detailed Definition | 既是当前方案架构定义的细化（向内），又是后续方案的需求（向下） |
| 同步设计 | Synchronous Design | 在开展上层详细定义的同时，同步开展下层方案架构定义 |

---

## 四、需求类型

| 中文 | 英文 | 说明 |
|------|------|------|
| 功能需求 | Functional Requirements (FR) | 系统应该提供什么功能 |
| 非功能需求 | Non-Functional Requirements (NFR) | 系统应该满足什么质量特性 |
| 末级需求 | Leaf-level Requirements | 不可再分的原子性需求 |

---

## 五、核心约束

| 中文 | 英文 | 说明 |
|------|------|------|
| 1:1分配约束 | One-to-One Allocation Constraint | 每条详细定义末级节点只能分配到下层方案中唯一一个架构末级节点 |
| N:1承接支持 | Many-to-One Acceptance Support | 下层方案中一个架构末级节点可以承接上层需求的多个详细定义末级节点 |
| 双向追溯 | Bidirectional Traceability | 支持从上层需求追溯到下层方案，也支持从下层方案反向追溯到上层需求 |
| 符合性分析 | Compliance Analysis | 通过分析验证方案如何满足所承接的上层需求 |
| 映射关系 | Mapping Relationship | 需求和方案之间的对应关系 |

---

## 六、四种设计方法

| 中文 | 英文 | 说明 |
|------|------|------|
| 瀑布式 | Waterfall | 从原始需求开始的完整正向系统设计 |
| 敏捷式 | Agile | 在现有设计基础上处理增量需求的迭代设计 |
| 逆向工程 | Reverse Engineering | 从已有产品（代码/图纸）反向推导系统设计 |
| DevOps | DevOps | 快速响应生产环境问题和紧急需求 |

---

## 七、操作流程

| 中文 | 英文 | 说明 |
|------|------|------|
| 分解 | Decomposition | 将架构末级节点逐层分解为更细的末级条目 |
| 分配 | Allocation | 将详细定义末级节点按1:1约束分配到下层方案架构末级节点 |
| 分析 | Analysis | 验证分解的充分性和分配的正确性 |
| 需求分解 | Requirements Decomposition | 将需求分解到末级 |
| 需求映射 | Requirements Mapping | 将需求映射到方案 |
| 影响分析 | Impact Analysis | 分析变更的影响范围 |
| 完整性验证 | Completeness Verification | 验证所有需求都被映射 |
| 一致性验证 | Consistency Verification | 验证映射关系的一致性 |
| 产品同构性 | Product Homomorphism | 共享同一方法论的产品，其设计结构具有相同的形式 |
| 设计制品参考 | Design Artifact Reference | 基于同构性，不同产品间设计制品的参考策略（直接参考、结构化参考、模板参考） |

---

## 八、质量与验证

| 中文 | 英文 | 说明 |
|------|------|------|
| 需求说明符合性分析 | Requirements Compliance Analysis | 检查方案是否充分满足所承接的需求 |
| 需求性能符合性分析 | Performance Compliance Analysis | 验证设计方案能否达到性能指标要求 |
| 追溯矩阵 | Traceability Matrix | 需求和方案之间的端到端映射矩阵 |
| 验证报告 | Verification Report | 完整性和一致性的验证报告 |
