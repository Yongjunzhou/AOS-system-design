# 系统设计指南：英文术语对照表

**文档版本**：v1.1  
**创建日期**：2026-05-14  
**用途**：统一英文术语，便于国际化和技术交流

---

## 📋 核心术语对照

### 基本定义

| 中文 | 英文 | 说明 |
|------|------|------|
| 企业运营体系 | Enterprise Operation System (AOS) | 企业运营体系的简称，本准则所关注企业的业务范围涵盖机载设备的市场、研发、生产、售后及经营管理 |
| 运营体系开发之系统设计流水线 | System Design Pipeline for AOS Development | 从原始需求到产品架构的完整系统设计工具，AOS开发者在使用该流水线进行运营体系开发 |

### 文档类型

| 中文 | 英文 | 说明 |
|------|------|------|
| 准则 | Standards / Principles | 理论基础、规范要求、设计原则 |
| 指南 | Guide / Handbook | 实践指导、操作步骤、工作手册 |
| 参考卡 | Quick Reference Card | 快速查阅、速记、便携版 |
| 索引 | Index | 导航、查找工具 |

### 文档名称

| 中文 | 英文 | 文件名 |
|------|------|--------|
| 运营体系开发之系统设计准则 | System Design Standards for AOS Development | 01-system-design-standards.md |
| 瀑布式系统设计指南 | Waterfall System Design Guide | 01-waterfall-design-guide.md |
| 敏捷式系统设计指南 | Agile System Design Guide | 02-agile-design-guide.md |
| 逆向工程指南 | Reverse Engineering Guide | 03-reverse-engineering-guide.md |
| DevOps系统设计指南 | DevOps System Design Guide | 04-devops-design-guide.md |
| 系统设计实践指南：快速参考卡 | System Design Handbook: Quick Reference Card | 05-quick-reference-card.md |
| 设计准则变更追溯指南 | Standards Change Traceability Guide | 06-standards-change-traceability.md |

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
# 运营体系开发之系统设计准则
System Design Standards for AOS Development
```

**术语中**：
```
1:1分配约束（One-to-One Allocation Constraint）
```

**文件名中**：
```
01-system-design-standards.md
01-waterfall-design-guide.md
05-quick-reference-card.md
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
Attendees: Product Manager, Architect, Requirements Analyst
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
01-system-design-standards.md (中文)
01-system-design-standards-en.md (英文)
01-system-design-standards-zh.md (中文)
```

---

## 📝 术语更新记录

| 日期 | 更新内容 | 版本 |
|------|---------|------|
| 2026-05-13 | 初版发布，包含核心术语对照 | v1.0 |
| 2026-05-14 | 更新术语表以匹配设计准则 v2.2：移除质量指标术语，补充基本术语，更新场景分类和文件引用 | v1.1 |

---

**文档生成时间**：2026-05-14  
**文档版本**：v1.1  
**状态**：✅ 完成

**下一步**：
- 根据实际使用情况补充新术语
- 定期审查和更新术语表
- 收集团队反馈，优化术语选择
