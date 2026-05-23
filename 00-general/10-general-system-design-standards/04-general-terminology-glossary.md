# 通用术语对照表
**General Terminology Glossary**

**文档版本**：v2.1
**创建日期**：2026-05-18
**修订日期**：2026-05-22
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
| 任务定义 | Task Definition | 描述特定操作规程的执行步骤和输入输出 |
| AI辅助文档 | AI Support Document | 为 AI 成员提供的系统设计辅助指引 |
| 产品数据 | Product Data | 按产品结构模板填入具体内容产生的设计输出 |

---

## 二、产品开发阶段

| 中文 | 英文 | 说明 |
|------|------|------|
| 系统设计 | System Design | 阶段1，从原始需求到产品架构的完整设计过程 |
| 构件开发 | Component Development | 阶段2，对架构末级节点（构件）根据需求定义开发制品 |
| 系统集成与交付 | System Integration & Delivery | 阶段3，沿架构树形层级从叶子节点逐级向上集成至根节点 |
| 系统运维 | System Operation & Maintenance | 阶段4，产品交付后的持续运行、监控、维护和优化 |
| 构件 | Component / Artifact | 产品架构末级节点，是系统设计阶段定义的构件 |

---

## 三、5层结构

| 中文 | 英文 | 说明 |
|------|------|------|
| 原始需求 | Original Requirements (OR) | 第1层，用户或相关方的原始需求 |
| 相关方需求 | Stakeholder Requirements (SR) | 第2层，原始需求的方案和后续需求 |
| 业务架构 | Business Architecture (BA) | 第3层，相关方需求功能部分的方案 |
| 系统需求 | System Requirements (SysReq) | 第4层，业务架构和非功能需求的方案 |
| 产品架构 | Product Architecture (PA) | 第5层，系统需求的方案和实现 |

---

## 四、基本术语

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
| 架构定义与详细定义分离 | Separation of Architecture & Detailed Definition | 每份方案由架构定义（树形结构+映射）和详细定义（分解细化）两个独立子文档组成 |
| 两阶段工作流程 | Two-phase Workflow | 先快速约定结构骨架并建立映射关系，再并行填充详细内容的工作模式 |
| 性能指标 | Performance Metric | 每条需求附带的可测量数值指标（响应时间、吞吐量、可用性等） |
| 分类和组织节点 | Classification/Organization Node | 架构末级节点之上的节点，用于对架构进行分类和组织 |
| 系统设计链路 | System Design Chain | 系统设计阶段中从原始需求到产品架构的完整设计链条（五层结构） |
| 三层工作层面 | Three Work Levels | 第1层自指设计（设计线设计自身）、第2层交付物构建（设计线的构件交付给团队M）、第3层使用工具设计EOS |
| 跨领域通用 | Cross-domain General | 信息处理模式中前9类可在不同业务领域间共享同一信息化平台 |
| 领域特有 | Domain-specific | 信息处理模式中后4类因领域差异需专用系统实现 |
| 自指关系 | Self-Reference | 运营体系包含设计自身的规则和工具——设计线（系统设计流水线）支撑"设计运营体系本身"这项业务 |
| 产品形态连续谱 | Product Morphology Spectrum | 产品从纯知识产品到纯软件产品到纯实物产品是连续谱，同一产品可沿谱演化 |
| 产品类型 | Product Type | 产品的本质分类（知识/方法类、软件类、实物类），决定PA产物形态 |
| 信息处理模式 | Information Processing Mode | 业务活动处理信息的方式分类：13种模式——计划事务、工单事务、审批流程、合规事务、规范知识、指标看板、进展追踪、信息台账、xBOM（跨领域通用），以及设备IO、领域分析、领域建模、领域算法（领域特有） |
| 知识组件的双重身份 | Dual Identity of Knowledge Components | EOS的知识组件（准则/指南/AI辅助/任务定义）同时是设计线的PA构件交付物和EOS的设计工具输入 |

---

## 五、需求类型

| 中文 | 英文 | 说明 |
|------|------|------|
| 功能需求 | Functional Requirements (FR) | 系统应该提供什么功能 |
| 非功能需求 | Non-Functional Requirements (NFR) | 系统应该满足什么质量特性 |
| 末级需求 | Leaf-level Requirements | 不可再分的原子性需求 |

### 非功能需求三级分类

| 一级分类 | 二级分类 | 英文 | 定义 |
|---------|---------|------|------|
| **质量特性** | 性能（效率） | Performance / Efficiency | 响应时间、吞吐量、资源利用率 |
| | 安全性 | Security | 保密性、完整性、不可抵赖性、可追溯性、身份认证 |
| | 可靠性 | Reliability | 成熟度（缺陷率）、容错性、可恢复性 |
| | 可用性 | Availability | 正常运行时间比例、故障转移能力 |
| | 易用性 | Usability | 易学性、易操作性、可访问性 |
| | 人机工效 | Ergonomics | 用户操作体验、认知负荷、操作效率 |
| | 韧性 | Resilience | 面对故障的适应和恢复能力 |
| | 功能正确性 | Functional Correctness | 功能实现的准确度、精度、完备性 |
| **环境适应性** | 可扩展性 | Scalability | 业务增长时平滑扩展的能力 |
| | 弹性 | Elasticity | 负载波动时动态调整资源的能力 |
| | 国际化 | Internationalization | 适应不同语言、地区、法规的能力 |
| | 可移植性 | Portability | 跨平台/跨环境部署的能力 |
| | 互操作性 | Interoperability | 与第三方系统对接交换数据的能力 |
| | 兼容性 | Compatibility | 向后兼容、与现有系统共存的能力 |
| | 可替换性 | Replaceability | 组件可被替代实现替换而不影响整体 |
| **可实现性** | 物料可采购性 | Procurability | 资源（软件许可、云资源、API等）采购的便捷程度和供应风险 |
| | 可生产性 | Manufacturability | 产出过程的复杂度高低，是否容易构建 |
| | 可测试性 | Testability | 功能和非功能指标是否容易验证 |
| | 可交付性 | Deliverability | 产品是否容易交付到用户手中 |
| | 可部署性 | Deployability | 是否容易在目标环境中安装上线 |
| | 可运维性 | Operability | 运行中是否容易监控、维护和排障 |
| | 可退役性 | Retirability | 下线时数据迁移和遗留清理是否容易操作 |
| | 经济可承受性 | Affordability | 所有活动的总成本是否在预算内 |

---

## 六、核心约束

| 中文 | 英文 | 说明 |
|------|------|------|
| 1:1分配约束 | One-to-One Allocation Constraint | 每条详细定义末级节点只能分配到下层方案中唯一一个架构末级节点 |
| N:1承接支持 | Many-to-One Acceptance Support | 下层方案中一个架构末级节点可以承接上层需求的多个详细定义末级节点 |
| 双向追溯 | Bidirectional Traceability | 支持从上层需求追溯到下层方案，也支持从下层方案反向追溯到上层需求 |
| 符合性分析 | Compliance Analysis | 通过分析验证方案如何满足所承接的上层需求 |
| 映射关系 | Mapping Relationship | 需求和方案之间的对应关系 |

---

## 七、四种设计方法

| 中文 | 英文 | 说明 |
|------|------|------|
| 瀑布式 | Waterfall | 从原始需求开始的完整正向系统设计 |
| 敏捷式 | Agile | 在现有设计基础上处理增量需求的迭代设计 |
| 逆向工程 | Reverse Engineering | 从已有产品（代码/图纸）反向推导系统设计 |
| DevOps | DevOps | 快速响应生产环境问题和紧急需求 |
| 正向完整设计 | Forward Complete Design | 瀑布式：逐层正向推导（OR → SR → BA → SysReq → PA） |
| 正向增量 | Forward Incremental | 敏捷式：分析影响范围 → 增量更新受影响的文档 |
| 反向推导 | Reverse Derivation | 逆向工程：从代码/图纸反向推导至原始需求 |
| 最小正向变更 | Minimal Forward Change | DevOps：定位 → 修复 → 验证的最小化变更路径 |

---

## 八、操作流程

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

---

## 九、节点编号规范

| 中文 | 英文 | 说明 |
|------|------|------|
| 架构末级节点编号 | Architecture Leaf Node Numbering | 格式：`{层前缀}[-{类型后缀}]-{序号}`，如 SR-F-001 |
| 详细定义末级节点编号 | Detailed Definition Leaf Node Numbering | 格式：`{所归属的架构末级节点ID}.{层内序号}`，如 SR-F-001.01 |
| 条目级编号 | Item-level Numbering | OR 层使用的编号方式（OR 无架构末级节点），如 OR-001 |
| 编号的稳定性 | ID Stability | 编号一旦分配即固定，不因树形结构调整而改变 |

---

## 十、设计制品参考策略

| 中文 | 英文 | 说明 |
|------|------|------|
| 产品同构性 | Product Homomorphism | 共享同一五层设计方法论的产品，其设计结构具有相同的形式 |
| 设计制品参考 | Design Artifact Reference | 基于同构性，不同产品间设计制品的参考策略 |
| 直接参考 | Direct Reference | 100% 参考内容，适用于设计准则、设计指南等通用制品 |
| 结构化参考 | Structural Reference | 结构参考、内容定制，适用于 AI 辅助文档、任务定义 |
| 模板参考 | Template Reference | 仅框架参考，适用于产品数据文件 |

---

## 十一、质量与验证

| 中文 | 英文 | 说明 |
|------|------|------|
| 需求说明符合性分析 | Requirements Compliance Analysis | 检查方案是否充分满足所承接的需求 |
| 需求性能符合性分析 | Performance Compliance Analysis | 验证设计方案能否达到性能指标要求 |
| 追溯矩阵 | Traceability Matrix | 需求和方案之间的端到端映射矩阵 |
| 验证报告 | Verification Report | 完整性和一致性的验证报告 |
