# 系统设计指南：英文术语对照表

**文档版本**：v1.0  
**创建日期**：2026-05-13  
**用途**：统一英文术语，便于国际化和技术交流

---

## 📋 核心术语对照

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
| 产品开发系统设计准则 | System Design Standards for Product Development | 07-system-design-standards.md |
| 系统设计实践指南：三种场景的操作流程 | System Design Guidelines: Operational Procedures for Three Scenarios | 08-system-design-guidelines-scenarios.md |
| 系统设计实践指南：快速参考卡 | System Design Guidelines: Quick Reference Card | 09-system-design-guidelines-quick-reference.md |
| 系统设计指南文档体系 | System Design Documentation System | 10-documentation-system.md |
| 系统设计指南文档集总结 | System Design Documentation Summary | 11-documentation-summary.md |
| 系统设计指南文档索引 | System Design Documentation Index | 12-documentation-index.md |

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

### 三种场景

| 中文 | 英文 | 说明 |
|------|------|------|
| 反向工程 | Reverse Engineering | 从代码和图纸反向推导系统设计 |
| 新研产品 | New Product Development | 从原始需求开始进行系统设计 |
| 增量需求 | Incremental Requirements | 在现有系统设计基础上处理新需求 |

### 操作步骤

| 中文 | 英文 | 说明 |
|------|------|------|
| 需求分解 | Requirements Decomposition | 将需求分解到末级 |
| 需求映射 | Requirements Mapping | 将需求映射到方案 |
| 影响分析 | Impact Analysis | 分析变更的影响范围 |
| 完整性验证 | Completeness Verification | 验证所有需求都被映射 |
| 一致性验证 | Consistency Verification | 验证映射关系的一致性 |

---

## ✅ 质量保证术语

| 中文 | 英文 | 说明 |
|------|------|------|
| 检查清单 | Checklist | 质量检查的项目清单 |
| 质量指标 | Quality Metrics | 衡量质量的量化指标 |
| 映射覆盖率 | Mapping Coverage Rate | 被映射的需求占总需求的比例 |
| 符合性分析完整率 | Compliance Analysis Completeness Rate | 包含符合性分析的方案条目比例 |
| 超链接有效率 | Hyperlink Validity Rate | 有效超链接占总超链接的比例 |

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
# 产品开发系统设计准则
System Design Standards for Product Development
```

**术语中**：
```
1:1分配约束（One-to-One Allocation Constraint）
```

**文件名中**：
```
07-system-design-guidelines.md
08-system-design-guide-scenarios.md
09-quick-reference-card.md
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
- "系统设计指南提供了三种场景的操作步骤"
- "System Design Handbook provides operational procedures for three scenarios"

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
07-system-design-guidelines.md (中文)
07-system-design-guidelines-en.md (英文)
07-system-design-guidelines-zh.md (中文)
```

---

## 📝 术语更新记录

| 日期 | 更新内容 | 版本 |
|------|---------|------|
| 2026-05-13 | 初版发布，包含核心术语对照 | v1.0 |

---

**文档生成时间**：2026-05-13  
**文档版本**：v1.0  
**状态**：✅ 完成

**下一步**：
- 根据实际使用情况补充新术语
- 定期审查和更新术语表
- 收集团队反馈，优化术语选择
