# 系统设计流水线：英文术语对照表

**文档版本**：v1.2  
**创建日期**：2026-05-18  
**用途**：统一英文术语，便于国际化和技术交流。本文档服务于设计线（系统设计流水线）的开发和使用。

---

## 📋 核心术语对照

### 基本定义

| 中文 | 英文 | 说明 |
|------|------|------|
| 运营体系系统设计流水线 | System Design Pipeline for Enterprise Operation System | 从原始需求到产品架构的完整系统设计工具，简称"流水线"，是本产品的名称 |
| 流水线开发者 | Pipeline Developer | 开发和维护系统设计流水线的团队成员（设计线开发团队） |
| 运营体系开发者 | EOS Developer | 使用流水线进行企业运营体系系统设计的开发者（EOS设计团队） |
| 企业运营体系 | Enterprise Operation System (EOS) | 流水线的目标设计对象——企业的 IT/AI 化运营系统 |

### 文档类型

| 中文 | 英文 | 说明 |
|------|------|------|
| 准则 | Standards / Principles | 理论基础、规范要求、设计原则 |
| 指南 | Guide / Handbook | 实践指导、操作步骤、工作手册 |
| 参考卡 | Quick Reference Card | 快速查阅、速记、便携版 |
| 索引 | Index | 导航、查找工具 |
| 规范 | Specification | 针对特定设计层的详细规范和标准 |

### 流水线产品架构构件

| 中文 | 英文 | 说明 |
|------|------|------|
| 规范与准则 | Standards & Principles | 定义设计标准和方法的理论基础文件 |
| 操作指南 | Operation Guide / Handbook | 指导不同场景下操作流程的实践文档 |
| AI辅助文档 | AI Assistance Documents | 支持AI成员参与系统设计的辅助文档 |
| 任务定义 | Task Definitions | 规范化操作规程和步骤的定义文件 |
| 产品数据 | Product Data | 系统设计过程中产出的结构化数据文件 |

### 文档名称

| 中文 | 英文 | 文件名 |
|------|------|--------|
| 系统设计准则总纲 | System Design Standards | 01-pipeline-system-design-standards.md |
| 原始需求规范 | Original Requirements Specification | 02-pipeline-original-requirements-specification.md |
| 相关方需求规范 | Stakeholder Requirements Specification | 03-pipeline-stakeholder-requirements-specification.md |
| 业务架构规范 | Business Architecture Specification | 04-pipeline-business-architecture-specification.md |
| 系统需求规范 | System Requirements Specification | 05-pipeline-system-requirements-specification.md |
| 产品架构规范 | Product Architecture Specification | 06-pipeline-product-architecture-specification.md |
| 术语对照表 | Terminology Glossary | 07-pipeline-terminology-glossary.md |
| 规范模板 | Specification Template | 00-general/10-general-system-design-standards/03-specification-template.md |
| 瀑布式设计指南 | Waterfall System Design Guide | 01-waterfall-pipeline-system-design-guide.md |
| 敏捷式设计指南 | Agile System Design Guide | 03-agile-pipeline-system-design-guide.md |
| 逆向工程指南 | Reverse Engineering Guide | 02-reverse-engineering-pipeline-system-design-guide.md |
| DevOps设计指南 | DevOps System Design Guide | 04-devops-pipeline-system-design-guide.md |
| 快速参考卡 | Quick Reference Card | 05-pipeline-system-quick-reference-card.md |

### 基本术语（v2.2新增）

| 中文 | 英文 | 说明 |
|------|------|------|
| 需求文档 | Requirements Document | 描述系统应该做什么 |
| 方案文档 | Solution Document | 描述如何满足需求，由架构定义和详细定义组成 |
| 需求—方案配对 | Requirement-Solution Pair | 需求与方案成对出现 |
| 文档的双重属性 | Dual Role of Document | 一个文档可同时是方案和需求 |
| 架构定义 | Architecture Definition | 构建方案的层级结构，建立对上层需求的映射 |
| 详细定义 | Detailed Definition | 对架构末级节点进行详细设计分解 |
| 架构末级节点 | Architecture Leaf Node | 方案分类和组织的最大条目，需求映射的关键层级 |
| 详细定义末级节点 | Detailed Definition Leaf Node | 分配到后续方案架构末级节点的源头 |
| 详细定义的双重身份 | Dual Identity of Detailed Definition | 既是当前方案的细化，又是后续方案的需求 |

---

## 🏗️ 系统设计流水线术语

### 5层结构

| 中文 | 英文 | 说明 |
|------|------|------|
| 原始需求 | Original Requirements | 第1层，用户或相关方的原始需求 |
| 相关方需求 | Stakeholder Requirements | 第2层，原始需求的方案和后续需求 |
| 业务架构 | Business Architecture | 第3层，相关方需求功能部分的方案 |
| 系统需求 | System Requirements | 第4层，业务架构和非功能需求的方案 |
| 产品架构 | Product Architecture | 第5层，系统需求的方案和实现 |

### 需求类型

| 中文 | 英文 | 说明 |
|------|------|------|
| 功能需求 | Functional Requirements | 系统应该提供什么功能 |
| 非功能需求 | Non-Functional Requirements | 系统应该满足什么质量特性 |
| 末级需求 | Leaf-level Requirements | 不可再分的原子性需求 |
| 相关方需求 | Stakeholder Requirements | 从相关方角度定义的需求 |

---

## 🎯 核心约束术语

| 中文 | 英文 | 说明 |
|------|------|------|
| 1:1分配约束 | One-to-One Allocation Constraint | 每条需求分配到唯一的方案条目 |
| N:1承接支持 | Many-to-One Acceptance Support | 每个方案条目可承接多条需求 |
| 双向追溯 | Bidirectional Traceability | 需求和方案之间的双向导航 |
| 符合性分析 | Compliance Analysis | 方案如何满足需求的分析 |
| 映射关系 | Mapping Relationship | 需求和方案之间的对应关系 |
| 组织资产优先 | Organizational Asset Priority | 新增需求时优先复用/改进现有架构节点，最后新增的原则，遵循"复用→改进→新增"的优先级顺序 |

### 产品架构分解原则（v1.4新增）

| 中文 | 英文 | 说明 |
|------|------|------|
| 信息模型内聚性 | Information Model Cohesion | 判断多个业务活动是否操作同一组核心实体，决定 PA 构件合并或分离的因素 |
| NFR Profile 相容性 | NFR Profile Compatibility | 判断不同业务活动的非功能需求是否相互冲突，NFR 冲突时不应共享同一构件 |
| 信息处理模式一致性 | Information Processing Pattern Consistency | 判断业务活动消费和生产信息的方式是否一致，不同模式倾向分离为不同构件 |
| 三因素决策矩阵 | Three-Factor Decision Matrix | 综合信息模型、NFR Profile、信息模式三个因素判断 PA 构件合并/分离的决策工具 |

---

## 📊 操作流程术语

### 四种场景

| 中文 | 英文 | 说明 |
|------|------|------|
| 瀑布式 | Waterfall | 从原始需求开始的完整系统设计 |
| 敏捷式 | Agile | 在现有设计基础上处理增量需求 |
| 逆向工程 | Reverse Engineering | 从代码和图纸反向推导系统设计 |
| DevOps | DevOps | 快速响应生产环境的问题和紧急需求 |

### 操作步骤

| 中文 | 英文 | 说明 |
|------|------|------|
| 需求分解 | Requirements Decomposition | 将需求分解到末级 |
| 需求映射 | Requirements Mapping | 将需求映射到方案 |
| 影响分析 | Impact Analysis | 分析变更的影响范围 |
| 完整性验证 | Completeness Verification | 验证所有需求都被映射 |
| 一致性验证 | Consistency Verification | 验证映射关系的一致性 |

---


## 🎓 最佳实践术语

| 中文 | 英文 | 说明 |
|------|------|------|
| 最佳实践 | Best Practices | 经过验证的最优做法 |
| 关键成功因素 | Critical Success Factors | 成功的关键要素 |
| 关键风险 | Key Risks | 需要重点关注的风险 |
| 应对措施 | Mitigation Measures | 应对风险的措施 |
| 增量处理 | Incremental Processing | 分阶段处理需求 |
| 影响范围最小化 | Impact Minimization | 最小化变更的影响范围 |

---

## 📚 相关术语

| 中文 | 英文 | 说明 |
|------|------|------|
| 系统设计流水线 | System Design Pipeline | 从需求到架构的完整设计流程 |
| 方法论 | Methodology | 系统的工作方法和原理 |
| 架构设计 | Architecture Design | 系统的整体结构设计 |
| 需求管理 | Requirements Management | 需求的收集、分析、追溯 |
| 追溯矩阵 | Traceability Matrix | 需求和方案的映射矩阵 |
| 符合性报告 | Compliance Report | 符合性验证的报告 |

---

## 🔄 文档体系术语

| 中文 | 英文 | 说明 |
|------|------|------|
| 文档体系 | Documentation System | 多份文档的组织体系 |
| 文档集 | Documentation Set | 相关文档的集合 |
| 快速参考 | Quick Reference | 快速查阅的资源 |
| 学习路径 | Learning Path | 循序渐进的学习计划 |
| 角色指南 | Role-based Guide | 针对特定角色的指南 |

---

## 💡 使用建议

### 在文档中使用英文

**标题中**：
```
# 系统设计流水线准则
System Design Pipeline Standards
```

**术语中**：
```
1:1分配约束（One-to-One Allocation Constraint）
```

**文件名中**：
```
01-pipeline-system-design-standards.md
01-waterfall-pipeline-system-design-guide.md
05-pipeline-system-quick-reference-card.md
```

### 在交流中使用英文

**邮件主题**：
```
System Design Standards Review
System Design Handbook - Scenario 1 Implementation
```

**会议记录**：
```
Topic: System Design Pipeline Methodology
Attendees: Pipeline Developer, AI Member
```

---

## 📖 术语使用示例

### 准则 vs 指南

**准则（Standards）**：
- "系统设计准则定义了5层结构"
- "System Design Standards define the 5-layer structure"

**指南（Handbook）**：
- "系统设计指南提供了四种场景的操作步骤"
- "System Design Handbook provides operational procedures for four scenarios"

### 需求 vs 方案

**需求（Requirements）**：
- "原始需求、相关方需求、系统需求"
- "Original Requirements, Stakeholder Requirements, System Requirements"

**方案（Solution）**：
- "相关方需求是原始需求的方案"
- "Stakeholder Requirements are the solution to Original Requirements"

### 映射 vs 追溯

**映射（Mapping）**：
- "将需求映射到方案"
- "Map requirements to solutions"

**追溯（Traceability）**：
- "建立双向追溯"
- "Establish bidirectional traceability"

---

## 🌐 国际化建议

### 文档翻译

如果需要将文档翻译成英文，建议：
1. 使用本对照表中的标准术语
2. 保持中英文对照的格式
3. 在首次出现时标注英文
4. 建立术语表供参考

### 多语言支持

建议的文件命名方式：
```
01-system-design-specification.md (中文)
01-system-design-specification-en.md (英文)
01-system-design-specification-zh.md (中文)
```

---

## 📝 术语更新记录

| 日期 | 更新内容 | 版本 |
|------|---------|------|
| 2026-05-13 | 初版发布，包含核心术语对照 | v1.0 |
| 2026-05-14 | 更新术语表以匹配设计准则 v2.2：移除质量指标术语，补充基本术语，更新场景分类和文件引用 | v1.1 |
| 2026-05-18 | 纯化为流水线产品专属术语表：更新基本定义和文档名称，新增流水线产品架构构件分类 | v1.2 |
| 2026-05-18 | 修正使用建议中的 EOS 标题和角色示例 | v1.3 |
| 2026-05-22 | 新增产品架构分解原则术语（信息模型内聚性、NFR Profile相容性、信息处理模式一致性、三因素决策矩阵），对齐准则 v3.10 | v1.4 |

---

**文档生成时间**：2026-05-22  
**文档版本**：v1.4  
**状态**：✅ 完成

**下一步**：
- 根据流水线实际使用情况补充新术语
- 定期审查和更新术语表（与准则和规范文档保持同步）
- 收集团队L反馈，优化术语选择
