# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AOS（Architecture & Orchestration System）是一个系统设计治理项目，核心目标是将企业系统设计流程标准化、资产化、自动化。它定义了从「相关方需求」到「产品架构」的完整四层设计链路，并通过 AI Skill 实现流程自动化。

## 四层映射模型

```
相关方需求 (SR) ──N:1──→ 业务架构 5级 (BA) ──N:1──→ 系统需求 5级 (SysReq) ──N:1──→ 产品架构末级 (PA)
                                                                    ↓
                                                            SysReq 9级（场景活动）
```

**功能需求流**：
- **SR → BA 5级**：N:1 多对一映射（多条相关方需求可分配至一个 BA 5 级节点）
- **BA 5级 → SysReq 5级**：N:1 多对一映射（一个业务组件可能在多个业务上应用）
- **SysReq 9级 → PA末级**：N:1 多对一映射（多个场景活动可映射到一个前后端组件）
- **1:1 约束**：每条需求只能分配到唯一的承接点

**非功能需求流**（平行体系）：
```
相关方非功能需求 (SR-NFR) ──N:1──→ 非功能需求架构 (NFR-Arch) ──N:1──→ 系统非功能需求 (SysReq-NFR)
```

- 非功能需求采用**平行的架构体系**，与功能需求独立设计
- 非功能需求在系统需求层面直接承接，不经过业务架构
- 非功能需求承接层也在第 5 级，与功能需求承接层平行

## 业务架构层级结构（0-5 级）

业务架构采用 5 级层级结构，其中 **5 级节点（组件）是承接相关方需求的关键层级**。根据实现方式分为两类：

### 配置方式实现的业务需求

| 层级 | 名称 | 说明 |
|------|------|------|
| 0级 | 架构根节点 | 整个系统的顶层根节点 |
| 1级 | 业务域 | 按业务领域划分 |
| 2级 | 端到端项目 | 跨越多个业务域的项目 |
| 3级 | 项目业务对象架构节点 | 端到端业务的架构节点 |
| 4级 | 工作包（WBS） | 对象架构节点下的工作分解结构 |
| **5级** | **业务组件（承接层）** | **★ 承接相关方需求的关键层级**<br>- 计划定义、流程定义、工单定义、指标定义等<br>- ★ 末级，不再分解 |

### 开发方式实现的业务需求

| 层级 | 名称 | 说明 |
|------|------|------|
| 0级 | 架构根节点 | 整个系统的顶层根节点 |
| 1级 | 流程与信息化业务域 | 平台开发相关业务域 |
| 2级 | AOS 平台开发项目 | 平台开发项目 |
| 3级 | 平台引擎 | 各类引擎（流程引擎、工单引擎等） |
| 4级 | 引擎配置工作包 | 各类引擎配置工作包 |
| **5级** | **配置业务（承接层）** | **★ 承接相关方需求的关键层级**<br>- 工作包所包含的聚集在一个 tab 上的配置业务<br>- ★ 末级，不再分解 |

**关键设计点**：
- 相关方需求（SR）最终映射到 5 级的业务组件或配置业务
- 5 级节点是 N:1 多对一映射的承接点（一个业务组件可能在多个业务上应用）
- 5 级是末级，不再向下分解

## 系统需求架构层级结构（0-9 级）

系统需求架构采用 9 级层级结构，其中 **5 级节点（组件实例）是承接 BA 5 级节点的关键层级**。功能需求分支的完整结构如下：

| 层级 | 名称 | 说明 |
|------|------|------|
| 0级 | 根节点 | 整个系统的顶层根节点 |
| 1级 | 独立信息系统 | 一个独立的信息系统 |
| 2级 | 功能/非功能需求 | 功能需求分支或非功能需求分支（分支点） |
| **功能需求分支** | | |
| 3级 | 业务组件类型 | 流程、工单、计划、指标等业务组件类型 |
| 4级 | 业务组件小类 | 业务组件类型下的小类分类 |
| **5级** | **组件实例（承接层）** | **★ 承接 BA 5 级节点的关键层级**<br>- 具体的组件实例<br>- 与 BA 5 级节点是 N:1 映射关系 |
| 6级 | 功能模块 | 以标签页为载体的功能模块<br>- 一个组件实例可能有多个功能模块 |
| 7级 | 系统用例 | 在标签页上提供的功能<br>- 以功能按钮或右键菜单为载体 |
| 8级 | 用例场景 | 系统用例的具体场景<br>- ★ 映射到产品架构末级节点 |
| 9级 | 场景活动 | 用例场景的具体活动步骤 |

**关键设计点**：
- BA 5 级节点映射到 SysReq 5 级节点（N:1 关系）
- SysReq 5 级节点是系统功能需求的清单（BA 所有 5 级节点去重后）
- SysReq 6-9 级是组件实例的内部分解
- SysReq 9 级（场景活动）映射到产品架构末级节点（N:1 关系）

## 非功能需求架构层级结构（0-6 级）

非功能需求采用**平行的架构体系**，独立于业务架构设计，其中 **5 级节点是承接相关方非功能需求的关键层级**：

| 层级 | 名称 | 说明 |
|------|------|------|
| 0级 | 非功能需求根节点 | 整个系统的非功能需求顶层根节点 |
| 1级 | 需求类别 | 三大类：质量特性需求、环境适应性需求、可实现性需求 |
| 2级 | 需求类型 | 具体类型（如：性能、安全、可测试性、可部署性等） |
| 3级 | 需求子类型 | 子类型（如：响应时间、吞吐量、数据加密、自动化部署等） |
| 4级 | 需求细分 | 对第 3 级的更细分类 |
| **5级** | **非功能需求承接层** | **★ 承接相关方非功能需求的关键层级**<br>- 具体的需求名称<br>- 需求描述<br>- 量化指标定义<br>- 验证方法 |
| 6级 | 操作序列/验证标准 | 非功能需求的验证步骤和标准 |

**非功能需求三大类**：

1. **质量特性需求**（Quality Attributes）
   - 性能需求（Performance）
   - 可靠性需求（Reliability）
   - 安全性需求（Security）
   - 可用性需求（Availability）
   - 可维护性需求（Maintainability）

2. **环境适应性需求**（Environmental Adaptation）
   - 兼容性需求（Compatibility）
   - 可扩展性需求（Scalability）
   - 可移植性需求（Portability）
   - 集成适应性需求（Integration Adaptability）

3. **可实现性需求**（Implementability）
   - 可生产性需求（Producibility）
   - 可测试性需求（Testability）
   - 可交付性需求（Deliverability）
   - 可部署性需求（Deployability）
   - 可操作性需求（Operability）
   - 可运维性需求（Maintainability in Operations）
   - 可退役性需求（Retirability）

**关键设计点**：
- 相关方非功能需求（SR-NFR）最终映射到 5 级的非功能需求承接层节点
- 5 级非功能需求承接层节点是 N:1 多对一映射的承接点
- 非功能需求承接层节点必须有完整的上级节点链，直到非功能需求根节点
- 6 级操作序列是非功能需求的验证细节，不参与需求映射

## 4 条核心设计准则

| 准则 | 内容 | 对应文件 |
|------|------|----------|
| 准则 1 | 需求规范化、分解、初步 BA 设计、冲突/重复检测、分类确认 | `01-standards/guidelines/guideline-1-normalization.md` |
| 准则 2 | SR → BA 映射（N:1 分配） | `01-standards/guidelines/guideline-2-sr-to-ba-mapping.md` |
| 准则 3 | BA → SysReq 映射（N:1 分配） | `01-standards/guidelines/guideline-3-ba-to-sr-mapping.md` |
| 准则 4 | SysReq → PA 映射（N:1 分配） | `01-standards/guidelines/guideline-4-sr-to-pa-mapping.md` |

## 9 个 AI Skill（自动化资产）

按处理流程排列：`requirement-normalization` → `requirement-decomposition` → `conflict-detection` → `duplicate-detection` → `business-pattern-matching` → `architecture-pattern-matching` → `sr-to-ba-mapping` → `ba-to-sr-mapping` → `sr-to-pa-mapping`

所有 Skill 定义位于 `02-pipeline/skills/`，每个 Skill 描述特定任务的输入、输出和处理步骤。

## 新增需求处理流程（12 步）

1. 收集原始需求
2. 规范化 + 分解（调用 Skill）
3. 冲突检测（调用 Skill）
4. 重复检测（调用 Skill）
5. 分类和建议
6. 人工确认
7. SR ↔ BA 同步设计（调用 Skill，满足准则 2）
8. BA ↔ SysReq 同步设计（调用 Skill，满足准则 3）
9. SysReq ↔ PA 同步设计（调用 Skill，满足准则 4）
10. 验证映射关系
11. 更新映射矩阵
12. 更新版本日志

详见 `02-pipeline/workflows.md`。

## 两阶段工作流程（解耦模式）

为了实现上下游文档的相对独立性和多个团队的并行工作，采用**"两阶段工作流程"**模式：

### 第一阶段：占位符创建（快速，1-2 小时）

- 下游团队快速扫描上游文档
- 识别所有末级节点
- 在下游文档中创建对应的占位符
- 建立上下游的映射关系
- 冻结占位符结构

### 第二阶段：具体设计（深入，2-6 天）

- 下游团队填充占位符的具体内容
- 设计业务流程、系统需求、产品架构等
- 为下一层级预留占位符
- 验证设计的完整性和一致性
- 冻结下游文档

**优势**：
- ✅ 上下游文档相对独立
- ✅ 多个团队可以并行工作
- ✅ 时间缩短 30-50%
- ✅ 避免过度的同步迭代

详见 `02-pipeline/workflows.md` 和 `01-standards/guidelines/guideline-placeholder.md`。

## Key Commands

```bash
# 验证项目映射关系
python 02-pipeline/tools/validate.py --project <project-name> --check all

# 生成追溯矩阵报告
python 02-pipeline/tools/generate-report.py --project <project-name> --report traceability

# 生成项目汇总报告
python 02-pipeline/tools/generate-report.py --project <project-name> --report summary
```

## Project Structure

```
01-standards/        # 组织资产：5 条准则 + 4 个模板 + 业务模式库 + 质量检查清单
02-pipeline/         # 自动化资产：9 个 Skill + 2 个工具脚本 + 工作流定义
03-products/         # 产品数据：按项目组织的设计文档
04-platform-docs/    # 平台文档：快速开始指南、相关方需求等
.claude/             # Claude Code 配置
```

每个项目目录（`03-products/projects/<project-name>/`）包含 7 个文件：
`requirements.md`、`business-architecture.md`、`system-requirements.md`、`product-architecture.md`、`analysis.md`（需求分析核心）、`mappings.md`（映射矩阵核心）、`changelog.md`。

## 关键设计文件

- `04-platform-docs/quick-start-guide.md` — ★ 新用户快速开始指南（5分钟快速了解）
- `04-platform-docs/pipeline-stakeholder-requirements.md` — 相关方需求完整定义
- `02-pipeline/workflows.md` — 12 步新增需求处理流程（触发所有工作的总入口）
- `01-standards/guidelines/README.md` — 5 条准则总览
- `01-standards/checklists/quality-checklist.md` — ★ 质量检查清单（可操作的检查工具）
- `01-standards/patterns/business-patterns.md` — ★ 业务模式库（10+ 个常见模式）
- `03-products/projects/<name>/analysis.md` — ★ 原始需求→规范化→分解→确认的完整链路
- `03-products/projects/<name>/mappings.md` — ★ SR→BA→SysReq→PA 的 N:1 映射关系

## 文档规范

- 所有文档使用 Markdown + Mermaid 格式
- 版本号格式：`v[主版本].[次版本]`
- 变更记录统一写入 `changelog.md`
