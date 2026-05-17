# AOS 逆向工程系统设计 Skill
**AOS Reverse Engineering System Design Skill**

**文档版本**：v1.0
**基于准则版本**：系统设计准则 v3.3
**基于指南版本**：逆向工程系统设计指南 v3.2
**对应场景**：03-reverse-engineering（已有 AOS 运营系统代码或图纸，设计文档缺失或不达标）

---

## 一句话场景描述

AOS 企业运营体系已开发完成或接近完成，有完整的代码实现或架构图纸，但五层系统设计文档不全或不符合设计准则，需要从代码和图纸中逆向推导出完整的、符合准则的设计文档集。

## 适用条件

- ✅ AOS 运营系统已开发完成或接近完成
- ✅ 有详细的代码实现或架构图纸
- ✅ 技术文档不全或不符合设计准则
- ✅ 缺少从需求到架构的完整追溯链路
- ✅ 需要生成符合准则的系统设计文档

## 不适用条件

- ❌ AOS 代码不清晰或文档极度缺失（无法进行有效逆向推导）
- ❌ 原开发人员无法参与配合
- ❌ 需要快速完成，时间紧张
- ❌ AOS 尚在设计阶段（应使用瀑布式或敏捷式场景）

## 依据B：两层产品关系说明

本目录下的文档是产品A（AOS 企业运营体系）的 **AI辅助文档实例**，是产品B产品架构（PA）的末级节点。

核心认知：
- **来源**：本目录文档基于产品B的 AI 辅助文档模板（位于 `00-pipeline-design/.../03-system-design-ai-support/03-reverse-engineering/`）定制，属于**结构复用、内容定制**（复用逆向工程8步流程的文档结构，内容面向 AOS 领域）
- **产品B的PA节点**：这些文档是产品B产品架构中"03-aos-system-design-ai-support/03-reverse-engineering/"节点的具体实例
- **使用者**：团队A（运营体系开发者）使用这些文档对 AOS 运营系统进行逆向工程
- **维护者**：团队B（流水线开发者 + AI）负责维护和更新这些实例文档

**产品类型说明**：AOS 为 IT/AI 化运营系统（软件产品），其 PA 分类为"前端 / 后端 / 数据 / 基础设施"。

## 输入

| 输入 | 说明 | 来源 |
|------|------|------|
| AOS 代码和架构图纸 | 系统源码、架构图、模块图、数据流图等 | AOS 项目代码库、文档库 |
| AOS 现有技术文档（如有） | 已有但不完整的各类设计文档 | AOS 项目文档库 |
| 系统设计准则 v3.3 | 总纲，定义 5 层结构、三条核心规则 | `01-aos-system-design-standards/01-system-design-standards.md` |
| 各层设计规范 | 各层的架构定义、详细定义、映射规则 | `01-aos-system-design-standards/` 下各层规范 |
| 逆向工程系统设计指南 v3.2 | 8 步操作流程和质量要求 | `02-aos-system-design-guidelines/03-reverse-engineering-guide.md` |

## 输出

AI 按 8 步流程依次产出以下文档集：

| 步骤 | 产出文档 |
|------|---------|
| 第1步 | AOS 系统架构草图、功能模块清单、关键技术决策记录 |
| 第2步 | AOS 产品架构文档（架构定义 + 详细定义 + 映射关系表骨架） |
| 第3步 | AOS 系统需求文档（功能 0-9 级架构 + 非功能 0-6 级架构 + 详细定义 + 映射关系表） |
| 第4步 | AOS 业务架构文档（IPO 清单 + 去重报告 + 映射关系表） |
| 第5步 | AOS 相关方需求文档（架构定义 + 详细定义 + 映射关系表） |
| 第6步 | AOS 原始需求文档（含末级需求分解 + OR→SR 映射关系） |
| 第7步 | AOS 验证报告（1:1/N:1/双向追溯/符合性分析完整率） |
| 第8步 | 完整的 AOS 系统设计文档集（5 层）、需求映射矩阵、变更日志 |

## AI 能力边界和约束

### AI 可以做的

- ✅ AOS 代码结构分析和模块划分识别
- ✅ AOS 架构图纸解析和组件依赖关系提取
- ✅ AOS 功能清单提取和 4 大组件分类（前端/后端/数据/基础设施）
- ✅ 从代码实现反推 AOS 产品架构组件定义
- ✅ 从 PA 组件反推 SysReq 9 级场景活动
- ✅ 从 SysReq 反推 BA IPO（Input/Process/Output）
- ✅ 从 BA IPO 反推 SR 架构末级节点和详细定义
- ✅ 从 SR 架构末级节点聚合为 OR 条目和末级分解
- ✅ IPO 去重（复用→改进→新增三级策略）
- ✅ 按 0-9 级层级结构组织功能需求架构
- ✅ 按 0-6 级平行架构组织非功能需求架构
- ✅ AOS 需求映射关系的建立和验证
- ✅ 符合性分析的编写
- ✅ 追溯矩阵的生成
- ✅ 从代码实际性能特征反推性能指标（标注"反推值"）

### AI 不可以做的（需要运营体系开发者确认）

- ❌ 代码中缺失的业务逻辑判断 — 需原开发人员补充
- ❌ 架构图纸与代码实现不一致时的最终决策 — 需 AOS 架构师确认
- ❌ 业务架构 IPO 的业务语义正确性 — 需业务人员审核
- ❌ 非功能需求的量化指标数值（从代码反推的仅是参考值）— 需 AOS 架构师确认
- ❌ 原始需求的优先级判定 — 需产品经理确认
- ❌ 最终版本号的确定 — 需项目负责人确认

## 角色分工

| 角色 | 职责 |
|------|------|
| **运营体系开发者**（人） | 提供 AOS 代码和图纸，审核 AI 每步的逆向推导结果，处理 AI 标记的待确认项，确定最终版本号 |
| **AI**（执行者） | 按本目录下的 workflow-prompts.md 依次执行 8 步逆向推导，生成 AOS 设计文档初稿，标记待确认项，完成后运行 checklist.md 自检 |
| **AOS 业务相关方**（人） | 协助理解 AOS 业务逻辑和运营含义，确认逆向推导结果的业务正确性 |

## 涉及的规范文档

- [系统设计准则（总纲）](../01-aos-system-design-standards/01-system-design-standards.md)
- [原始需求规范](../01-aos-system-design-standards/02-original-requirements-specification.md)
- [相关方需求规范](../01-aos-system-design-standards/03-stakeholder-requirements-specification.md)
- [业务架构规范](../01-aos-system-design-standards/04-business-architecture-specification.md)
- [系统需求规范](../01-aos-system-design-standards/05-system-requirements-specification.md)
- [产品架构规范](../01-aos-system-design-standards/06-product-architecture-specification.md)
- [逆向工程系统设计指南](../02-aos-system-design-guidelines/03-reverse-engineering-guide.md)

---

**文档版本**：v1.0
**创建日期**：2026-05-18
**状态**：✅ 完成
