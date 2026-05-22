# 运营体系（AOS）：英文术语对照表
**AOS System Design Glossary: English-Chinese Terminology**

**文档版本**：v1.0  
**创建日期**：2026-05-18  
**用途**：统一英文术语，便于国际化和技术交流。本文档服务于产品A（企业运营体系·AOS）的设计和开发。

---

## 📋 核心术语对照

### 基本定义

| 中文 | 英文 | 说明 |
|------|------|------|
| 企业运营体系 | Enterprise Operation System (AOS) | 企业运营体系的简称，是产品A的名称，涵盖企业核心运营业务的 IT/AI 化系统 |
| 运营体系开发者 | AOS Developer | 进行 AOS 系统设计的团队成员（产品A设计团队） |
| 系统设计流水线 | System Design Pipeline | 为 AOS 开发提供系统设计方法论和工具支持的设计工具 |

### 文档类型

| 中文 | 英文 | 说明 |
|------|------|------|
| 准则 | Standards / Principles | 理论基础、规范要求、设计原则 |
| 指南 | Guide / Handbook | 实践指导、操作步骤、工作手册 |
| 参考卡 | Quick Reference Card | 快速查阅、速记、便携版 |
| 规范 | Specification | 针对特定设计层的详细规范和标准 |
| 产品数据 | Product Data | 系统设计过程中产出的结构化数据 |

### AOS 产品架构构件

| 中文 | 英文 | 说明 |
|------|------|------|
| 前端应用 | Frontend Application | 用户交互界面层 |
| 后端服务 | Backend Service | 业务逻辑处理层 |
| 数据存储 | Data Storage | 数据持久化层 |
| 基础设施 | Infrastructure | 运行环境和支撑层 |

### 文档名称（AOS 系统设计）

| 中文 | 英文 | 文件名 |
|------|------|--------|
| AOS 系统设计准则总纲 | AOS System Design Standards | 01-aos-system-design-standards.md |
| AOS 原始需求规范 | AOS Original Requirements Specification | 02-aos-original-requirements-specification.md |
| AOS 相关方需求规范 | AOS Stakeholder Requirements Specification | 03-aos-stakeholder-requirements-specification.md |
| AOS 业务架构规范 | AOS Business Architecture Specification | 04-aos-business-architecture-specification.md |
| AOS 系统需求规范 | AOS System Requirements Specification | 05-aos-system-requirements-specification.md |
| AOS 产品架构规范 | AOS Product Architecture Specification | 06-aos-product-architecture-specification.md |
| AOS 术语对照表 | AOS Terminology Glossary | 07-aos-system-design-terminology-glossary.md |
| AOS AI辅助概览 | AOS AI Assistance Overview | 03-aos-system-design-ai-support/00-overview.md |
| AOS 产品数据 | AOS Product Data | 10-aos-system-product-data/ |

---

### 基本术语

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

## 🏗️ 系统设计方法论术语

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

---

## 📊 AOS业务领域术语

### 绩效考核核心概念

| 中文 | 英文 | 说明 |
|------|------|------|
| 绩效考核 | Performance Appraisal | 对员工或组织的工作表现进行系统化评估的过程 |
| 考核计划 | Appraisal Plan | 一次考核活动的完整计划和配置 |
| 考核周期 | Appraisal Cycle | 考核的时间跨度（月度/季度/年度） |
| 考核模板 | Appraisal Template | 定义考核维度和指标的标准化模板 |
| 评分维度 | Scoring Dimension | 考核的评估方面（如工作质量、完成率等） |
| 评分指标 | Scoring Indicator / KPI | 量化的考核衡量指标 |
| 权重 | Weight | 各考核维度的相对重要性系数 |
| 加权评分 | Weighted Score | 按权重计算后的评分结果 |

### 考核流程

| 中文 | 英文 | 说明 |
|------|------|------|
| 评分录入 | Score Entry | 考核者录入评分数据的过程 |
| 评分计算 | Score Calculation | 根据权重和规则计算最终评分 |
| 评分审核 | Score Review / Verification | 对评分结果进行审核和确认 |
| 绩效报告 | Performance Report | 包含评分结果和分析的报告 |
| 绩效面谈 | Performance Review Meeting | 基于绩效结果的面谈和反馈 |
| 申诉处理 | Appeal Process | 对考核结果提出异议的处理流程 |

### 技术术语

| 中文 | 英文 | 说明 |
|------|------|------|
| 前端应用 | Frontend Application | 用户交互界面的软件实现 |
| 后端服务 | Backend Service | 业务逻辑处理的软件实现 |
| 微服务 | Microservice | 独立部署和演进的业务服务单元 |
| RESTful API | RESTful API | 基于 REST 架构的 API 设计风格 |
| 数据持久化 | Data Persistence | 将数据保存到存储介质的过程 |
| 容器化 | Containerization | 使用容器技术打包和部署应用 |

---

## 🔄 操作流程术语

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

## 💡 使用建议

### 在文档中使用英文

**标题中**：
```
# 企业运营体系（AOS）系统设计准则
AOS System Design Standards
```

**术语中**：
```
考核计划（Appraisal Plan）
```

**文件名中**：
```
01-aos-system-design-standards.md
02-aos-original-requirements-specification.md
```

### 在交流中使用英文

**邮件主题**：
```
AOS System Design Review
AOS Performance Appraisal Module - Architecture Design
```

**会议记录**：
```
Topic: AOS Product Architecture Design
Attendees: AOS Developer, Business Analyst, System Architect
```

---

## 📖 术语使用示例

### 准则 vs 指南

**准则（Standards）**：
- "AOS 系统设计准则定义了5层结构"
- "AOS System Design Standards define the 5-layer structure"

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

### AOS 业务术语示例

**考核相关**：
- "创建月度考核计划"
- "Create a monthly appraisal plan"

**评分相关**：
- "按权重计算加权评分"
- "Calculate weighted scores according to weights"

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
01-aos-system-design-standards.md (中文)
01-aos-system-design-standards-en.md (英文)
01-aos-system-design-standards-zh.md (中文)
```

---

## 📝 术语更新记录

| 日期 | 更新内容 | 版本 |
|------|---------|------|
| 2026-05-18 | 初版发布，包含方法论核心术语和AOS绩效考核业务领域术语 | v1.0 |

---

**文档生成时间**：2026-05-18  
**文档版本**：v1.0  
**状态**：✅ 完成

**下一步**：
- 根据 AOS 实际设计过程中的术语使用情况补充新术语
- 与流水线版本术语表保持对照关系
- 收集团队A反馈，优化术语选择
