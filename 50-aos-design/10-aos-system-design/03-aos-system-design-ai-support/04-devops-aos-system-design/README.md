# AOS DevOps 快速修复系统设计 Skill
**AOS DevOps / Quick Fix System Design Skill**

**文档版本**：v1.0
**基于准则版本**：系统设计准则 v3.3
**基于指南版本**：DevOps 系统设计指南 v3.2
**对应场景**：04-devops（AOS 运营系统已上线，发现 bug 或紧急需求，需快速响应和最小化变更）

---

## 一句话场景描述

AOS 企业运营体系已上线运行，在使用过程中发现 bug 或紧急需求，需要在几小时到 2-3 天内快速响应，通过最小化变更修复问题并保持系统设计文档的一致性。

## 适用条件

- ✅ AOS 运营系统已上线运行
- ✅ 在使用过程中发现 bug 或紧急需求
- ✅ 需要快速响应（几小时到 1-2 天）
- ✅ 需要最小化变更，避免影响现有运营功能
- ✅ 适合 DevOps 团队快速迭代

## 不适用条件

- ❌ 需要进行大规模运营体系重构
- ❌ 影响范围超过 50%
- ❌ 需要完整的系统设计从头开始
- ❌ AOS 未上线（应使用瀑布式或敏捷式场景）

## 依据B：两层产品关系说明

本目录下的文档是产品A（AOS 企业运营体系）的 **AI辅助文档实例**，是产品B产品架构（PA）的末级节点。

核心认知：
- **来源**：本目录文档基于产品B的 AI 辅助文档模板（位于 `10-pipeline-design/.../03-pipeline-system-design-ai-support/04-pipeline-system-design-devops/`）定制，属于**结构复用、内容定制**（复用 DevOps 3种模式/4步流程的文档结构，内容面向 AOS 领域）
- **产品B的PA节点**：这些文档是产品B产品架构中"03-aos-system-design-ai-support/04-devops/"节点的具体实例
- **使用者**：团队A（运营体系开发者）使用这些文档对 AOS 运营系统进行 DevOps 快速修复
- **维护者**：团队B（流水线开发者 + AI）负责维护和更新这些实例文档

**产品类型说明**：AOS 为 IT/AI 化运营系统（软件产品），其 PA 分类为"前端 / 后端 / 数据 / 基础设施"。

## 三种处理模式

| 模式 | 影响范围 | 响应时间 | 适用场景 |
|------|---------|---------|---------|
| **模式1：快速修复** | 仅 PA（产品架构） | 几小时 | AOS UI bug、绩效参数调整、前端逻辑修复 |
| **模式2：局部设计** | SysReq + PA | 1 天 | AOS 运营功能 bug、小功能需求、系统性能优化 |
| **模式3：完整设计** | 跨多层（SR/BA/SysReq/PA） | 2-3 天 | AOS 业务流程 bug、重要运营功能需求、架构优化 |

## 输入

| 输入 | 说明 | 来源 |
|------|------|------|
| AOS 现有完整系统设计文档集 | 5 层设计文档 + 映射矩阵 | 已有设计产出 |
| AOS 问题报告/紧急需求 | bug 描述、错误日志、用户反馈、运营数据 | 生产监控、运营人员反馈 |
| 系统设计准则 v3.3 | 总纲，定义 5 层结构、三条核心规则 | `01-aos-system-design-standards/01-system-design-standards.md` |
| 各层设计规范 | 各层的架构定义、详细定义、映射规则 | `01-aos-system-design-standards/` 下各层规范 |
| DevOps 系统设计指南 v3.2 | 3 种模式、4 步流程、决策树 | `02-aos-system-design-guidelines/04-devops-design-guide.md` |

## 输出

AI 按 4 步流程依次产出以下内容：

| 步骤 | 模式 | 产出文档 |
|------|------|---------|
| 第1步 | 通用 | 问题分类与优先级、影响范围评估、选定处理模式 |
| 第2步 | 模式1 | 修改后的 AOS PA 文档（架构定义 + 详细定义）+ 验证报告 |
| 第3步 | 模式2 | 修改后的 AOS SysReq 文档 + PA 文档 + 验证报告 |
| 第4步 | 模式3 | 修改后的 AOS 多层文档集（SR/BA/SysReq/PA）+ 验证报告 |

## AI 能力边界和约束

### AI 可以做的

- ✅ AOS 问题分类（bug/功能需求/性能优化）和紧急程度评估
- ✅ AOS 影响范围快速评估（定位受影响的层和节点）
- ✅ 处理模式选择（根据影响范围推荐模式）
- ✅ 快速定位到具体的 AOS 架构末级节点
- ✅ 生成简化格式的修复条目（含原问题、修改内容、符合性分析）
- ✅ 使用增量标记（`~` 修改 / `+` 新增）生成增量内容
- ✅ 更新映射关系表
- ✅ 更新符合性分析
- ✅ 回归验证（修改是否引入新问题）
- ✅ 版本号和变更日志更新

### AI 不可以做的（需要运营体系开发者确认）

- ❌ 优先级判定（P0/P1/P2）— 需产品经理确认
- ❌ AOS bug 根本原因的最终诊断 — 需开发人员现场分析
- ❌ AOS 性能优化方案的选择（改算法 vs 加缓存 vs 加资源）— 需架构师确认
- ❌ 模式选择的最终决定 — 需运营体系开发者确认
- ❌ 是否需要升级为更完整的模式 — 需架构师确认
- ❌ 最终版本号的确定 — 需项目负责人确认

## 角色分工

| 角色 | 职责 |
|------|------|
| **运营体系开发者**（人） | 确认问题分类和优先级，审核 AI 的修复方案，决定处理模式，确定最终版本号 |
| **AI**（执行者） | 按本目录下的 workflow-prompts.md 执行影响评估，生成修复条目，更新映射关系，运行 checklist.md 自检 |
| **AOS 业务相关方**（人） | 报告运营问题，协助定位根因，验证修复效果 |

## 涉及的规范文档

- [系统设计准则（总纲）](../01-aos-system-design-standards/01-system-design-standards.md)
- [原始需求规范](../01-aos-system-design-standards/02-original-requirements-specification.md)
- [相关方需求规范](../01-aos-system-design-standards/03-stakeholder-requirements-specification.md)
- [业务架构规范](../01-aos-system-design-standards/04-business-architecture-specification.md)
- [系统需求规范](../01-aos-system-design-standards/05-system-requirements-specification.md)
- [产品架构规范](../01-aos-system-design-standards/06-product-architecture-specification.md)
- [DevOps 系统设计指南](../02-aos-system-design-guidelines/04-devops-design-guide.md)

---

**文档版本**：v1.0
**创建日期**：2026-05-18
**状态**：✅ 完成
