# 瀑布式/AOS新研系统设计 Skill
**Waterfall / AOS New Product System Design Skill**

**文档版本**：v1.0
**基于准则版本**：系统设计准则 v3.3
**基于指南版本**：瀑布式系统设计指南 v3.2
**对应场景**：01-waterfall（原始需求全部齐备，从零开始完整设计 AOS 企业运营体系）

---

## 一句话场景描述

当 AOS 企业运营体系的原始需求已经全部收集和确认，需要从原始需求分析开始，逐层推导至产品架构，生成完整的、符合系统设计准则的 AOS 系统设计文档集。

## 适用条件

- ✅ AOS 原始需求已经完全收集和确认
- ✅ 需要从头到尾进行完整的系统设计（从 OR → SR → BA → SysReq → PA）
- ✅ 设计周期相对固定，需求变更较少
- ✅ 适合 AOS 新研（greenfield）项目或关键子系统的首次设计

## 依据B：两层产品关系说明

本目录下的文档是产品A（AOS 企业运营体系）的**AI辅助文档实例**，是产品B产品架构（PA）的末级节点。

核心认知：
- **来源**：本目录文档基于产品B的AI辅助文档模板（位于 `10-pipeline-design/.../03-pipeline-system-design-ai-support/01-pipeline-system-design-waterfall/`）定制，属于**结构复用、内容定制**（复用水-1件场景的文档结构，内容面向 AOS 领域）
- **产品B的PA节点**：这些文档是产品B产品架构中"03-aos-system-design-ai-support/01-waterfall/"节点的具体实例
- **使用者**：团队A（运营体系开发者）使用这些文档进行 AOS 企业运营体系的系统设计
- **维护者**：团队B（流水线开发者 + AI）负责维护和更新这些实例文档

## 不适用条件

- ❌ AOS 需求还在不断变化（应使用敏捷式场景 02-agile）
- ❌ 已有部分设计文档需要继承（应使用敏捷式场景 02-agile）
- ❌ 需要快速迭代和反馈（应使用敏捷式场景 02-agile）
- ❌ AOS 已有系统运行但文档缺失（应使用逆向工程场景 03-reverse-engineering）
- ❌ AOS 已上线需要快速修复（应使用 DevOps 场景 04-devops）

## 输入

| 输入 | 说明 | 来源 |
|------|------|------|
| AOS 原始需求 | 来自各相关方（业务部门、管理者、IT 部门等）的未经规范化的原始表述 | 会议纪要、邮件、已有文档、用户反馈、法规合规要求 |
| 系统设计准则 v3.3 | 总纲，定义5层结构、六步法、三条核心规则 | `01-aos-system-design-standards/01-system-design-standards.md` |
| 各层设计规范 | 各层的架构定义、详细定义、映射规则 | `01-aos-system-design-standards/` 下各层规范 |
| AOS 瀑布式设计指南 | 6步操作流程和质量要求 | `02-aos-system-design-guidelines/01-waterfall-design-guide.md` |

## 输出

AI 按 6 步流程依次生成以下 AOS 设计文档集：

| 步骤 | 产出文档 |
|------|---------|
| 第1步 | AOS 原始需求文档（含末级需求分解）、相关方需求架构定义文档（树形结构 + 映射关系表） |
| 第2步 | AOS 相关方需求功能部分详细定义文档、业务架构定义文档（IPO清单 + 映射关系表） |
| 第3步 | AOS 系统需求功能部分架构定义文档 |
| 第4步 | AOS 相关方需求非功能部分详细定义、系统需求非功能部分架构定义文档 |
| 第5步 | AOS 系统需求详细定义文档、产品架构定义文档（架构定义 + 详细定义） |
| 第6步 | AOS 需求追溯矩阵、验证报告 |

## AI 能力边界和约束

### AI 可以做的

- ✅ AOS 原始需求的规范化处理（格式统一、术语标准化、四项检查）
- ✅ 功能需求和非功能需求的分离
- ✅ 需求分解到末级（按原子性原则和1:1约束）
- ✅ 冲突检测和重复检测（语义对比、相似度分析）
- ✅ 按 N:1 关联性将末级需求分组，形成架构末级节点
- ✅ 基于架构末级节点生成详细定义分解
- ✅ 生成业务架构 IPO（Input/Process/Output）定义
- ✅ 执行 IPO 去重（复用→改进→新增三级策略）
- ✅ 按 0-9 级层级结构组织功能需求架构
- ✅ 按 0-6 级平行架构组织非功能需求架构
- ✅ 需求映射关系的建立和验证
- ✅ 符合性分析的编写
- ✅ 追溯矩阵的生成

### AI 不可以做的（需要运营体系开发者确认）

- ❌ 优先级判定（P0/P1/P2/P3）— 需人工确认
- ❌ 冲突检测中的最终决策（保留哪条、如何合并）— 需业务相关方确认
- ❌ 业务架构 IPO 的业务语义正确性 — 需业务人员审核
- ❌ 非功能需求的量化指标数值（响应时间、并发数等）— 需架构师确认
- ❌ AOS 产品架构的技术栈选择 — 需技术团队确认
- ❌ 最终版本号的确定 — 需项目负责人确认

## 角色分工

| 角色 | 职责 |
|------|------|
| **运营体系开发者**（人） | 确认原始需求，审核 AI 每一步的产出，处理 AI 标记的待确认项，确定最终版本号 |
| **AI**（执行者） | 按本目录下的 workflow-prompts.md 依次执行 6 步，生成文档初稿，遇到边界问题标记待确认，完成后运行 checklist.md 自检 |
| **业务相关方**（人） | 提出 AOS 业务需求和设计要求，审核需求分解和架构定义的业务正确性 |

## 涉及的规范文档

- [系统设计准则（总纲）](../01-aos-system-design-standards/01-system-design-standards.md)
- [原始需求规范](../01-aos-system-design-standards/02-original-requirements-specification.md)
- [相关方需求规范](../01-aos-system-design-standards/03-stakeholder-requirements-specification.md)
- [业务架构规范](../01-aos-system-design-standards/04-business-architecture-specification.md)
- [系统需求规范](../01-aos-system-design-standards/05-system-requirements-specification.md)
- [产品架构规范](../01-aos-system-design-standards/06-product-architecture-specification.md)
- [瀑布式系统设计指南](../02-aos-system-design-guidelines/01-waterfall-design-guide.md)

---

**文档版本**：v1.0
**创建日期**：2026-05-17
**状态**：✅ 完成
