# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AOS 是企业运营体系（Enterprise Operation System）的简称。本仓库包含两个系统设计项目，共用同一套设计准则和方法论，通过 AI Skill 实现流程自动化。

### 两层产品关系

企业需要开发并持续优化一个 IT 化甚至 AI 化的运营体系，以支持其各业务运行。围绕这一目标，存在两层产品关系：

- **产品A — AOS 企业运营体系**：企业实际运行所依赖的 IT/AI 化运营系统。**团队A** 负责开发和优化产品A，其系统设计人员在开展产品A的系统设计工作时需要工具支持。
- **产品B — 运营体系系统设计流水线**：为团队A的系统设计人员打造的"设计工具"，帮助他们高质量、高效率地完成产品A的系统设计。**团队B** 负责开发产品B。

**团队B的构成与分工**：
- **流水线开发者（用户）**：负责产品B的架构和系统设计决策
- **AI 成员**：按流水线开发者的指令深度参与产品B的开发

**一句话总结**：产品B是"设计工具"，产品A是"用这个工具来设计的目标系统"。本仓库中，团队B（用户 + AI）的当前工作就是设计和开发产品B本身。

### 产品开发四阶段

产品开发一般分为四个阶段：

| 阶段 | 名称 | 说明 |
|------|------|------|
| 阶段1 | **系统设计** | 从原始需求出发，经过五层结构（OR → SR → BA → SysReq → PA），开发出产品架构，定义每个架构末级节点（构件）的需求和实现策略 |
| 阶段2 | **构件开发** | 对产品架构中所有需要新开发或改进的构件，根据其需求定义，开发出满足需求的制品（artifact） |
| 阶段3 | **系统集成与交付** | 根据集成方案，沿产品架构的树形层级从叶子节点逐级向上集成至根节点，形成满足系统需求的完整产品，交付用户基于相关方需求测试确认 |
| 阶段4 | **系统运维** | 暂不关注 |

**产品B的范围**：严格限定在阶段1（系统设计）。原因：系统设计是产品开发中最重要也是难度最大的阶段，且团队时间有限。

### 仓库中的两个项目

| 概念 | 仓库目录 | 说明 |
|------|---------|------|
| 产品B的开发空间 | `00-pipeline-design/` | 产品B（流水线）的完整开发工作空间 |
| 产品A的开发空间 | `50-aos-design/` | 产品A（AOS）的完整开发工作空间 |

每个项目下按产品开发阶段组织为三个子目录：

| 阶段子目录 | 00（产品B） | 50（产品A） |
|-----------|------------|------------|
| 阶段1：系统设计 | `10-pipeline-system-design/` | `10-aos-system-design/` |
| 阶段2：构件开发 | `20-pipeline-component-dev/` | `20-aos-component-dev/`（待扩展） |
| 阶段3：集成交付 | `30-pipeline-integration-delivery/` | `30-aos-integration-delivery/`（待扩展） |

`50-aos-design/10-aos-system-design/` 目录中包含两类内容：

| 子目录 | 性质 | 说明 |
|--------|------|------|
| `01-aos-system-design-standards/` | 产品B的构件 | 设计准则（引用共享准则） |
| `02-aos-system-design-guidelines/` | 产品B的构件 | 设计指南（引用共享指南） |
| `03-aos-system-design-ai-support/` | 产品B的构件 | AI 辅助文档，为团队A提供系统设计支持 |
| `06-aos-system-design-tasks/` | 产品B的构件 | 任务定义，为团队A提供系统设计操作规程 |
| `10-aos-system-product-data/` | 产品A的设计输出 | 基于产品同构性定义的标准产品数据模板，由团队A填入产品A的具体设计内容 |

### 产品B的产品架构与 AOS 系统设计目录的关系

**核心认知**：产品B的产品架构末级节点，对应的交付物就是 `50-aos-design/10-aos-system-design/` 下除 `10-aos-system-product-data/` 之外的所有文档（01/02/03/06）。这些文档是产品B交付给团队A使用的工具和规范。`10-aos-system-product-data/` 是团队A使用产品B的工具后产出的产品A设计内容，是产品B的**输出物**，不是产品B的构件。

**产品同构性与内容复用**：产品B和产品A共用同一套五层结构和设计方法论，因此 `10-aos-system-design/` 下各子目录可基于产品B的对应文档定义起始版本：

| AOS 子目录 | 同构来源（产品B） | 复用策略 |
|-----------|-----------------|---------|
| `01-aos-system-design-standards/` | `00-pipeline-design/.../01-system-design-standards/` | 直接引用，100% 复用 |
| `02-aos-system-design-guidelines/` | `00-pipeline-design/.../02-system-design-guidelines/` | 直接引用，100% 复用 |
| `03-aos-system-design-ai-support/` | `00-pipeline-design/.../03-system-design-ai-support/` | 结构复用，内容需定制（场景不同） |
| `06-aos-system-design-tasks/` | 流水线的 6 个核心任务定义 | 结构复用，内容需定制（操作对象不同） |
| `10-aos-system-product-data/` | `00-pipeline-design/.../10-system-product-data/` | 仅文件名和模板结构复用，内容由团队A填入 |

## 五层结构与核心规则

```
第1层：原始需求及分析 (OR)
    ↓ N:1 分配
第2层：相关方需求 (SR)
    ├─ 架构末级节点 ↔ 详细定义末级节点
    │
    ├─ 功能部分 ↓ N:1 分配
    │   第3层：业务架构 (BA)（独立存在，仅架构定义，无详细定义）
    │   └─ 架构末级节点（IPO）
    │        ↓ IPO 直接映射（去重后）
    │   第4层：系统需求 (SysReq)
    │   ├─ 架构末级节点 ↔ 详细定义末级节点
    │   └─ ↓ N:1 分配
    │       第5层：产品架构 (PA)
    │       └─ 架构末级节点 ↔ 详细定义末级节点
    │
    └─ 非功能部分 ↓ N:1 分配（不经过 BA）
        第4层：系统需求-NFR (SysReq-NFR)
        └─ ↓ N:1 分配
            第5层：产品架构 (PA)
```

**三条核心规则**（§3.2）：
- **规则1：1:1 分配约束**：每条详细定义末级节点只能分配到下层方案中唯一一个架构末级节点
- **规则2：N:1 承接支持**：一个架构末级节点可以承接多个上层详细定义末级节点
- **规则3：双向追溯**：支持从上层需求追溯到下层方案，也支持从下层方案反向追溯到上层需求

### 核心设计概念

> 来源：准则 §1.5–§1.7

1. **架构定义与详细定义分离**（§1.5.1）：每层文档分为架构定义（树形结构）和详细定义（对架构末级节点的逐条细化），二者分别对应独立的产品数据文件
2. **详细定义的双重身份**（§1.5.2）：详细定义既是本层架构定义的细化（向内），又是下层方案的需求（向下传递）
3. **需求—方案配对**（§1.6.1）：文档按需求文档和方案文档成对组织，上层的详细定义 = 下层方案的需求
4. **同步设计与两阶段工作流程**（§1.5.3）：在开展上层详细定义的同时，同步开展下层方案架构定义；先快速约定结构骨架并建立映射关系（阶段一），再并行填充详细内容（阶段二）
5. **架构末级节点四要素结构**（§1.7.1）：每个架构末级节点包含四个要素——定义、所映射的上层需求、符合性分析、下游指导
6. **每层三个活动：分解、分配、分析**（§1.5.1）：每层设计都包含分解（将需求分解为末级节点）、分配（将末级节点映射到下层架构）、分析（符合性验证）三个活动

**补充说明**：
- 每条需求 = 需求描述 + 性能指标（性能指标随需求一起流转）
- 非功能需求采用平行体系，SR-NFR → SysReq-NFR → PA，不经过业务架构
- 业务架构（BA）的特殊性：BA 是唯一只有架构定义、没有详细定义的层级；BA 使用 IPO（Input-Process-Output）模型作为基本设计单位，去重后直接映射到 SysReq
- 分析活动贯穿全过程：每完成一次分配，都需要进行符合性分析，确认下层方案是否正确承接了上层需求

## 实际目录结构

```
00-pipeline-design/                             # 产品B的完整开发空间
├── 10-pipeline-system-design/                  # 阶段1：流水线的系统设计
│   ├── 01-system-design-standards/             # ★ 通用设计准则（两个项目共享）
│   │   └── 01-system-design-standards.md       # 核心：5层结构、映射规则
│   ├── 02-system-design-guidelines/            # ★ 四种场景的设计指南（共享）
│   │   ├── 01-waterfall-design-guide.md
│   │   ├── 02-agile-design-guide.md
│   │   ├── 03-reverse-engineering-guide.md
│   │   └── 04-devops-design-guide.md
│   ├── 03-system-design-ai-support/            # 流水线产品的 AI 辅助文档
│   │   ├── 00-ai-document-requirements-understanding.md
│   │   ├── 01-waterfall/
│   │   ├── 02-agile/
│   │   ├── 03-reverse-engineering/
│   │   └── 04-devops/
│   └── 10-system-product-data/                 # ★ 流水线的标准产品数据（9 份文档）
├── 20-pipeline-component-dev/                  # 阶段2：流水线的构件开发（待扩展）
└── 30-pipeline-integration-delivery/           # 阶段3：流水线的集成交付（待扩展）

50-aos-design/                                  # 产品A的完整开发空间
├── 10-aos-system-design/                       # 阶段1：AOS的系统设计（当前工作范围）
│   ├── 01-aos-system-design-standards/         # 引用通用准则（产品B构件）
│   ├── 02-aos-system-design-guidelines/        # 引用通用指南（产品B构件）
│   ├── 03-aos-system-design-ai-support/        # AOS 专用 AI 辅助文档（产品B构件）
│   │   ├── 01-greenfield/
│   │   ├── 02-optimization/
│   │   ├── 03-domain-analysis/
│   │   └── 04-integration-design/
│   ├── 06-aos-system-design-tasks/             # AOS 的 6 个核心任务（产品B构件）
│   │   ├── 01-aos-normalization/
│   │   ├── 02-aos-sr-ba-design/
│   │   ├── 03-aos-ba-sysreq-design/
│   │   ├── 04-aos-nfr-design/
│   │   ├── 05-aos-sysreq-pa-design/
│   │   └── 06-aos-traceability/
│   └── 10-aos-system-product-data/             # AOS 的产品数据（产品A设计输出）
├── 20-aos-component-dev/                       # 阶段2：AOS的构件开发（待扩展）
└── 30-aos-integration-delivery/                # 阶段3：AOS的集成交付（待扩展）

200-put-on-hold/                                # 归档的历史文件
99-sessions/                                    # 历史会话记录
```

## 开发六步法（6 个核心任务）

> 名称来源：准则 §3.1「开发六步法」

| 步骤 | 正式名称 | 目标 |
|------|---------|------|
| Step 1 | 原始需求分析及相关方需求架构定义 | 收集、规范化、分解原始需求，检测冲突和重复，建立 SR 架构 |
| Step 2 | 相关方需求功能部分详细定义及业务架构定义 | SR 功能部分详细定义，同步设计 BA 架构并建立映射 |
| Step 3 | 系统需求功能部分架构定义 | 将 BA IPO 去重后映射到 SysReq 架构末级节点 |
| Step 4 | 相关方需求非功能部分详细定义及系统需求非功能部分架构定义 | SR-NFR 详细定义，同步设计 SysReq-NFR 架构并建立映射 |
| Step 5 | 系统需求详细定义及产品架构定义 | SysReq 详细定义（6-9级分解），同步设计 PA 架构并建立映射 |
| Step 6 | 双向追溯验证 | 验证完整追溯链路，生成符合性报告 |

流水线产品的任务定义在 `00-pipeline-design/10-pipeline-system-design/03-system-design-ai-support/` 各场景目录下；AOS 项目的任务定义在 `50-aos-design/10-aos-system-design/06-aos-system-design-tasks/` 下。

## 四种设计场景

| 场景 | 适用情况 | 周期 | 指南 |
|------|---------|------|------|
| 瀑布式 | 全新系统，需求明确 | 30-48天 | `02-design-guidelines/01-waterfall-design-guide.md` |
| 敏捷式 | 迭代开发，需求渐进 | 13-21天 | `02-design-guidelines/02-agile-design-guide.md` |
| 逆向工程 | 已有系统补文档 | 16-26天 | `02-design-guidelines/03-reverse-engineering-guide.md` |
| DevOps | 小变更快速交付 | 几小时-3天 | `02-design-guidelines/04-devops-design-guide.md` |

## 三个关键角色

| 角色 | 职责 |
|------|------|
| **流水线开发者** | 开发、维护和优化系统设计流水线本身 |
| **AI** | 按流水线开发者指令执行自动化任务 |
| **AOS 开发者** | 使用流水线进行企业运营体系的系统设计（含需求提出者、业务流程开发者、信息系统开发者） |

## 关键设计文件

- `00-pipeline-design/10-pipeline-system-design/01-system-design-standards/01-system-design-standards.md` — 核心设计准则（5层结构、映射规则、术语定义）
- `00-pipeline-design/10-pipeline-system-design/02-system-design-guidelines/05-quick-reference-card.md` — 快速参考卡
- `00-pipeline-design/10-pipeline-system-design/03-system-design-ai-support/00-ai-document-requirements-understanding.md` — AI 文档理解要求
- `00-pipeline-design/10-pipeline-system-design/10-system-product-data/README.md` — 流水线产品数据概览
- `50-aos-design/10-aos-system-design/03-aos-system-design-ai-support/00-overview.md` — AOS AI 辅助概览

## 产品数据文件（每个项目通用结构）

两个项目的产品数据（`10-system-product-data/` 和 `10-aos-system-product-data/`）都遵循相同结构：

| 文件 | 内容 |
|------|------|
| `01-original-requirements.md` | 原始需求 |
| `02-stakeholder-requirements-architecture.md` | 相关方需求架构定义 |
| `03-stakeholder-requirements-detailed.md` | 相关方需求详细定义 |
| `04-business-architecture.md` | 业务架构 |
| `05-system-requirements-architecture.md` | 系统需求架构定义 |
| `06-system-requirements-detailed.md` | 系统需求详细定义 |
| `07-product-architecture.md` | 产品架构 |
| `08-traceability-matrix.md` | 追溯矩阵 |
| `09-verification-report.md` | 验证报告 |

## 文档规范

- 所有文档使用 Markdown + Mermaid 格式
- 版本号格式：`v[主版本].[次版本]`
- 中文为主体语言，术语附英文对照
