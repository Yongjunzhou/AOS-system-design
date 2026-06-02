# 运营体系（EOS）：英文术语对照表
**EOS System Design Glossary: English-Chinese Terminology**

**文档版本**：v2.1  
**创建日期**：2026-05-18  
**最近修订**：2026-05-28  
**用途**：统一英文术语，便于国际化和技术交流。本文档服务于EOS（企业运营体系·EOS）的设计和开发。

---

## 📋 核心术语对照

### 基本定义

| 中文 | 英文 | 说明 |
|------|------|------|
| 企业运营体系 | Enterprise Operation System (EOS) | 企业运营体系的简称，是EOS的名称，涵盖企业核心运营业务的 IT/AI 化系统 |
| EOS 开发者 | EOS Developer | 使用 EOS 流水线对 EOS 进行系统设计的成员。按职责分为引擎开发者（平台设计链）、业务组件配置者和业务配置者（业务设计链）三类角色 |
| 目标产品 | Target Product | 正在被系统设计的产品，统一称谓 |
| 四类构件 | Four Component Types | EOS 流水线 PA 的四类交付物：设计准则、设计指南、AI 辅助文档、任务定义 |

### 文档类型

| 中文 | 英文 | 说明 |
|------|------|------|
| 准则 | Standards / Principles | 理论基础、规范要求、设计原则 |
| 指南 | Guide / Handbook | 实践指导、操作步骤、工作手册 |
| 参考卡 | Quick Reference Card | 快速查阅、速记、便携版 |
| AI 辅助文档 | AI Support Document | 辅助 AI 参与系统设计的提示词、检查清单和范例 |
| 任务定义 | Task Definition | 各场景中各步骤的操作规程和输入输出定义 |
| 产品数据 | Product Data | 系统设计过程中产出的结构化数据 |

### 平台 PA 构件类型（软件类）

| 中文 | 英文 | 说明 |
|------|------|------|
| 前端组件 | Frontend Component | 用户交互界面层（页面组件、功能组件、交互组件） |
| 后端组件 | Backend Component | 业务逻辑处理层（API 服务、业务引擎、数据处理、消息处理） |
| 数据层 | Data Layer | 数据持久化层（关系型 DB、NoSQL、消息队列） |
| 基础设施 | Infrastructure | 运行环境和支撑层（API 网关、认证授权、监控告警、CI/CD） |

### 业务 PA 构件类型（配置类）

| 中文 | 英文 | 说明 |
|------|------|------|
| 表单定义 | Form Definition | 数据录入和展示的界面配置 |
| 标签页定义 | Tab Page Definition | 多视图切换配置 |
| 台账定义 | Ledger Definition | 数据列表和查询配置 |
| 菜单定义 | Menu Definition | 导航结构配置 |
| 流程定义 | Process Definition | 业务流程步骤和规则配置 |
| 指标定义 | Indicator Definition | 绩效指标计算配置 |

### 文档名称（EOS 系统设计）

| 中文 | 英文 | 文件名 |
|------|------|--------|
| EOS 系统设计规范 | EOS System Design Specification | 01-eos-system-design-specification.md |
| EOS 系统设计术语对照表 | EOS System Design Terminology Glossary | 04-eos-system-design-terminology-glossary.md |
| EOS AI辅助概览 | EOS AI Assistance Overview | 30-eos-system-design-ai-support/00-overview.md |
| EOS 瀑布式工作流模板 | EOS Waterfall Workflow Prompts | 30-eos-system-design-ai-support/01-waterfall-eos-system-design/workflow-prompts.md |
| EOS 逆向工程工作流模板 | EOS Reverse Engineering Workflow Prompts | 30-eos-system-design-ai-support/02-reverse-engineering-eos-system-design/workflow-prompts.md |
| EOS 敏捷式工作流模板 | EOS Agile Workflow Prompts | 30-eos-system-design-ai-support/03-agile-eos-system-design/workflow-prompts.md |
| EOS DevOps 工作流模板 | EOS DevOps Workflow Prompts | 30-eos-system-design-ai-support/04-devops-eos-system-design/workflow-prompts.md |
| EOS 产品数据 | EOS Product Data | 90-eos-system-product-data/ |

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

### EOS 特有框架术语

| 中文 | 英文 | 说明 |
|------|------|------|
| 三层工作层面 | Three Working Layers | EOS 系统设计的三个层面：第1层流水线设计、第2层构件开发、第3层使用工具设计 EOS |
| 平台设计链 | Platform Design Chain | 以引擎为产出目标的五层设计链路（OR→SR→BA→SysReq→PA），适用于引擎开发需求 |
| 业务设计链 | Business Design Chain | 以配置定义为产出目标的五层设计链路（OR→SR→BA→SysReq→PA），适用于业务配置需求 |
| 端到端项目业务 | E2E Project Business | BA 第2级，从需求提出到需求满足的完整闭环，是业务分解的核心单位 |
| 输出产品 | Output Product | 流水线类产品生产出来的产品，其 PA 节点类型作为流水线 BA IPO 的推导锚点 |
| 需求分流 | Requirement Diversion | 原始需求按引擎开发/业务配置/CAX 工具三种来源分类，分流至对应设计链或外部 |
| 同步设计 | Synchronous Design | 上层详细定义阶段同步建立下层架构结构骨架，而非串行执行 |
| 引擎 | Engine | EOS 平台的能力基础单元（表单引擎、流程引擎、工单引擎、台账引擎等），由引擎开发者实现 |
| 配置定义 | Configuration Definition | 使用引擎配置出的结构化定义（表单定义、台账定义、流程定义等），即业务链 PA 的产出形态 |

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
| 信息模型内聚性 | Information Model Cohesion | PA 分解三因素之一，判断构件内部数据/信息模型的紧密程度——强内聚的业务实体应归入同一构件 |
| NFR Profile 相容性 | NFR Profile Compatibility | PA 分解三因素之一，判断不同功能对非功能需求（性能/安全/可用性等）的要求是否相容——要求差异大的功能应分离到不同构件 |
| 信息处理模式一致性 | Information Processing Pattern Consistency | PA 分解三因素之一，判断业务活动的信息处理本质是否相同——不同模式（如联机事务处理 vs 批量分析）应分离到不同构件 |
| 三因素决策矩阵 | Three-Factor Decision Matrix | 综合信息模型内聚性、NFR Profile 相容性、信息处理模式一致性三个因素，判断哪些业务活动应合并为同一构件、哪些应分离的系统化决策方法

---

## 📊 EOS业务领域术语

### 绩效考核（业务示例）

| 中文 | 英文 | 说明 |
|------|------|------|
| 考核计划 | Appraisal Plan | 一次考核活动的完整计划和配置 |
| 评分维度 | Scoring Dimension | 考核的评估方面（如工作质量、完成率等） |
| 权重 | Weight | 各考核维度的相对重要性系数 |
| 评分指标 | Key Performance Indicator (KPI) | 量化的考核衡量指标 |
| 加权评分 | Weighted Score | 按权重计算后的评分结果 |
| 绩效报告 | Performance Report | 包含评分结果和分析的报告 |

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

## 💡 使用建议

### 在文档中使用英文

**标题中**：
```
# 企业运营体系（EOS）系统设计准则
EOS System Design Standards
```

**术语中**：
```
考核计划（Appraisal Plan）
```

**文件名中**：
```
01-eos-system-design-specification.md
04-eos-system-design-terminology-glossary.md
```

### 在交流中使用英文

**邮件主题**：
```
EOS System Design Review
EOS Performance Appraisal Module - Architecture Design
```

**会议记录**：
```
Topic: EOS Product Architecture Design
Attendees: EOS Developer, Business Analyst, System Architect
```

---

## 📖 术语使用示例

### 准则 vs 指南

**准则（Standards）**：
- "EOS 系统设计准则定义了5层结构"
- "EOS System Design Standards define the 5-layer structure"

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

### EOS 业务术语示例

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
01-eos-system-design-specification.md (中文)
10-eos-system-design-specification-en.md (英文)
10-eos-system-design-specification-zh.md (中文)
```

---

## 📝 术语更新记录

| 日期 | 更新内容 | 版本 |
|------|---------|------|
| 2026-05-18 | 初版发布，包含方法论核心术语和 EOS 绩效考核业务领域术语 | v1.0 |
| 2026-05-28 | 更新文档类型和文件名称对照，移除归档的层规范条目 | v2.0 |
| 2026-05-28 | 补充 EOS 特有框架术语（三层工作层面/两条设计链/端到端项目业务等）；扩展 PA 构件分类；精简绩效考核为业务示例；移除通用技术术语 | v2.1 |

---

**文档生成时间**：2026-05-28  
**文档版本**：v2.1  
**状态**：✅ 完成

**更新说明**：v2.1 重构了术语结构，补充了准则 v3.2 引入的核心框架术语，使术语表与当前准则全面对齐。
