# CLAUDE.md

This file provides guidance to Claude Code when working with this repository. It focuses on project-specific context—methodology foundations are defined in the general design standards and referenced here rather than duplicated.

---

## 项目概览

本项目包含三个目的：

1. **构建运营体系之系统设计流水线（产品L）** —— 使运营体系的系统设计从手工作坊式的文档撰写，转变为结构化、可追溯、AI 辅助的工业化生产过程。
2. **基于流水线开展运营体系系统设计（产品M）** —— 使用产品L产出的工具，对企业运营体系进行完整的系统设计，产出产品M的产品数据。
3. **探索产品开发方法论** —— 通过产品L和产品M的实践，验证和提炼可复用的产品开发方法论。

仓库包含三部分内容：
- **`00-general/`** — 通用系统设计方法论（与具体产品无关的准则、指南、模板、术语）
- **`10-pipeline-design/`** — 产品L（系统设计流水线）的完整开发工作空间
- **`50-aos-design/`** — 产品M（AOS 企业运营体系）的完整开发工作空间

**当前范围**：
- 流水线：严格限定在流水线开发四阶段中的阶段1（系统设计），即从原始需求到产品架构的完整设计链路
- 运营体系：产品开发全过程，即系统设计、组件开发、系统集成与交付、系统运维

---

## 两个产品与三层工作层面

### 两个产品

- **产品L — 系统设计流水线**：为运营体系"设计运营体系本身"这项业务提供方法支撑的知识工具型构件。**团队L** 负责开发产品L。
- **产品M — AOS 企业运营体系**：企业实际运行所依赖的 IT/AI 化运营系统，涵盖市场、研发、生产、售后等业务，同时也包含"设计运营体系本身"这项业务。**团队M** 负责开发和优化产品M。

### 三个工作层面

| 层面 | 内容 | 负责方 | 仓库位置 |
|------|------|--------|---------|
| **第1层：自指设计** | 产品L用统一方法论对其自身需求进行系统设计，推导出产品L的产品架构 | 团队L | `10-pipeline-design/` |
| **第2层：交付物构建** | 将产品L的系统设计产物（准则、指南、AI辅助文档、任务定义）适配到产品M的上下文，形成团队M使用的设计工具 | 团队L | `50-aos-design/.../01~04-*` |
| **第3层：使用工具设计产品M** | 团队M使用第2层产出的工具，对运营体系进行系统设计，产出产品M的9份产品数据文档 | 团队M | `50-aos-design/.../10-product-data/` |

### 产品L的构件在产品M系统设计中的作用

团队M在设计产品M时，直接使用产品L的 PA 构件作为设计依据和操作规程：

| 知识组件（产品L的 PA 构件） | 在产品M的系统设计中充当 |
|---------|----------------------|
| **准则**（standards） | 规定五层结构、映射规则等设计规范 |
| **指南**（guidelines） | 四种场景的设计步骤指导 |
| **AI辅助文档**（ai-support） | AI 成员执行自动化任务的依据 |
| **任务定义**（tasks） | 每一步的具体操作流程 |

**团队L的构成**：
- **流水线开发者（用户）**：负责产品L的架构和系统设计决策
- **AI 成员**：按流水线开发者的指令深度参与产品L的开发

---

## 产品L的产品架构与 AOS 系统设计目录的关系

**核心认知**：产品L的产品架构末级节点，对应的交付物就是 `50-aos-design/10-aos-system-design/` 下除 `10-aos-system-product-data/` 之外的所有文档（01/02/03/04）。这些文档是产品L交付给团队M使用的工具和规范。`10-aos-system-product-data/` 是团队M使用产品L的工具后产出的产品M设计内容，是产品L的**输出物**，不是产品L的构件。

**三层工作面对应的目录关系**：

| 层面 | 工作内容 | 仓库位置 |
|------|---------|---------|
| 第1层：自指设计 | 团队L用五层结构对产品L进行系统设计，产出产品L的产品数据 | `10-pipeline-design/10-pipeline-system-design/10-pipeline-system-product-data/`（9份产品数据） |
| 第2层：交付物构建 | 团队L基于同构性，将产品L的准则/指南/AI辅助/任务适配为产品M的设计工具 | `50-aos-design/10-aos-system-design/{01,02,03,04}-*`（产品L的构件） |
| 第3层：使用工具设计产品M | 团队M使用第2层工具，对产品M进行系统设计，产出产品M的产品数据 | `50-aos-design/10-aos-system-design/10-aos-system-product-data/`（产品M的设计输出） |

**产品同构性与内容参考**：产品L和产品M共用同一套五层结构和设计方法论。通用方法论核心位于 [`00-general/`](00-general/)，各产品在此基础上参考适配：

| AOS 子目录 | 参考来源 | 策略 |
|-----------|---------|------|
| `01-aos-system-design-standards/` | `00-general/10-general-design-standards/01-general-design-standards.md` + `10-pipeline-design/.../01-pipeline-system-design-standards/` | 通用方法论参考通用准则，流水线示例参考 Pipeline |
| `02-aos-system-design-guidelines/` | `00-general/10-general-design-standards/02-general-design-4modes-guide-overview.md` + `10-pipeline-design/.../02-pipeline-system-design-guidelines/` | 通用方法框架参考通用指南，示例参考 Pipeline |
| `03-aos-system-design-ai-support/` | `10-pipeline-design/.../03-pipeline-system-design-ai-support/` | 结构参考，内容需定制（场景不同） |
| `04-aos-system-design-tasks/` | 流水线的 4 场景任务定义 | 结构参考，内容需定制（操作对象不同） |
| `10-aos-system-product-data/` | `10-pipeline-design/.../10-pipeline-system-product-data/` | 文件名和模板结构参考，内容由团队M填入 |

---

## 实际目录结构

```
00-general/                                     # 通用方法论基础
├── 10-general-design-standards/               # 通用准则、指南、模板、术语
│   ├── 01-general-design-standards.md          # 通用设计准则（方法论核心，v2.1）
│   ├── 02-general-design-4modes-guide-overview.md # 通用设计指南
│   ├── 03-specification-template.md            # 规范文档通用模板
│   └── 04-general-terminology-glossary.md      # 通用术语对照

10-pipeline-design/                             # 产品L的完整开发空间
├── 10-pipeline-system-design/                  # 阶段1：流水线的系统设计
│   ├── 01-pipeline-system-design-standards/    # Pipeline准则（通用方法论 + 流水线专有）
│   │   └── 01-pipeline-design-standards.md
│   ├── 02-pipeline-system-design-guidelines/   # 四种场景的设计指南
│   │   ├── 01-waterfall-pipeline-system-design-guide.md
│   │   ├── 03-agile-pipeline-system-design-guide.md
│   │   ├── 02-reverse-engineering-pipeline-system-design-guide.md
│   │   └── 04-devops-pipeline-system-design-guide.md
│   ├── 03-pipeline-system-design-ai-support/   # 流水线产品的 AI 辅助文档
│   │   ├── 00-ai-document-requirements-understanding.md
│   │   ├── 01-waterfall-pipeline-system-design/
│   │   ├── 03-agile-pipeline-system-design/
│   │   ├── 02-reverse-engineering-pipeline-system-design/
│   │   └── 04-devops-pipeline-system-design/
│   ├── 04-pipeline-system-design-tasks/        # 流水线的操作规程（26 个任务文档）
│   │   ├── 01-waterfall-pipeline-system-design/
│   │   ├── 03-agile-pipeline-system-design/
│   │   ├── 02-reverse-engineering-pipeline-system-design/
│   │   └── 04-devops-pipeline-system-design/
│   └── 10-pipeline-system-product-data/        # 流水线的标准产品数据（9 份文档）
├── 20-pipeline-component-dev/                  # 阶段2：流水线的构件开发（待扩展）
└── 30-pipeline-integration-delivery/           # 阶段3：流水线的集成交付（待扩展）

50-aos-design/                                  # 产品M的完整开发空间
├── 10-aos-system-design/                       # 阶段1：AOS的系统设计（当前工作范围）
│   ├── 01-aos-system-design-standards/         # 参考 Pipeline 准则（产品L构件）
│   ├── 02-aos-system-design-guidelines/        # 参考 Pipeline 指南（产品L构件）
│   ├── 03-aos-system-design-ai-support/        # AOS 专用 AI 辅助文档（产品L构件）
│   │   ├── 01-waterfall-aos-system-design/
│   │   ├── 03-agile-aos-system-design/
│   │   ├── 02-reverse-engineering-aos-system-design/
│   │   └── 04-devops-aos-system-design/
│   ├── 04-aos-system-design-tasks/             # AOS 的 4 场景任务定义（产品L构件）
│   │   ├── 01-waterfall-aos-system-design/     # 瀑布式 6 个任务
│   │   ├── 03-agile-aos-system-design/         # 敏捷式 8 个任务
│   │   ├── 02-reverse-engineering-aos-system-design/ # 逆向工程 8 个任务
│   │   └── 04-devops-aos-system-design/        # DevOps 4 个任务
│   └── 10-aos-system-product-data/             # AOS 的产品数据（产品M设计输出）
├── 20-aos-component-dev/                       # 阶段2：AOS的构件开发（待扩展）
└── 30-aos-integration-delivery/                # 阶段3：AOS的集成交付（待扩展）

200-put-on-hold/                                # 归档的历史文件
99-sessions/                                    # 历史会话记录
```

---

## 五层结构与核心规则

> **方法论基础**：详见 [`00-general/10-general-design-standards/01-general-design-standards.md`](00-general/10-general-design-standards/01-general-design-standards.md) §三「5层结构概要」和 §四「设计方法」

### 五层设计链路

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

### 三条核心规则

- **规则1：1:1 分配约束**：每条详细定义末级节点只能分配到下层方案中唯一一个架构末级节点
- **规则2：N:1 承接支持**：一个架构末级节点可以承接多个上层详细定义末级节点
- **规则3：双向追溯**：支持从上层需求追溯到下层方案，也支持从下层方案反向追溯到上层需求

### 核心设计概念

| 概念 | 定义 |
|------|------|
| **架构定义与详细定义分离** | 每层方案分为架构定义（树形结构）和详细定义（对架构末级节点的逐条细化） |
| **详细定义的双重身份** | 既是本层架构定义的细化（向内），又是下层方案的需求（向下传递） |
| **需求—方案配对** | 文档按需求文档和方案文档成对组织，上层的详细定义 = 下层方案的需求 |
| **同步设计** | 在开展上层详细定义的同时，同步开展下层方案架构定义（即使只是结构骨架） |
| **两阶段工作流程** | 先快速约定结构骨架并建立映射关系（阶段一），再并行填充详细内容（阶段二） |
| **架构末级节点四要素** | 定义、所映射的上层需求、符合性分析、下游指导 |
| **每层三个核心设计活动** | 需求分解及分析、需求分配及分析、架构承接需求分析 |

### 补充说明

- 每条需求 = 需求描述 + 性能指标（性能指标随需求一起流转）
- 非功能需求采用平行体系，SR-NFR → SysReq-NFR → PA，不经过业务架构
- 业务架构（BA）是唯一只有架构定义、没有详细定义的层级；BA 使用 IPO 模型，去重后直接映射到 SysReq
- 分析活动贯穿全过程：每完成一次分配，都需要进行符合性分析

---

## 开发六步法（6 个核心任务）

> 名称来源：通用设计准则 §4.1「六步工作流程」

| 步骤 | 正式名称 | 目标 |
|------|---------|------|
| Step 1 | 原始需求分析及相关方需求架构定义 | 收集、规范化、分解原始需求，检测冲突和重复，建立 SR 架构 |
| Step 2 | 相关方需求功能部分详细定义及业务架构定义 | SR 功能部分详细定义，同步设计 BA 架构并建立映射 |
| Step 3 | 系统需求功能部分架构定义 | 将 BA IPO 去重后映射到 SysReq 架构末级节点 |
| Step 4 | 相关方需求非功能部分详细定义及系统需求非功能部分架构定义 | SR-NFR 详细定义，同步设计 SysReq-NFR 架构并建立映射 |
| Step 5 | 系统需求详细定义及产品架构定义 | SysReq 详细定义（6-9级分解），同步设计 PA 架构并建立映射 |
| Step 6 | 双向追溯验证 | 验证完整追溯链路，生成符合性报告 |

流水线产品的任务定义在 `10-pipeline-design/10-pipeline-system-design/04-pipeline-system-design-tasks/` 各场景目录下；AOS 项目的任务定义在 `50-aos-design/10-aos-system-design/04-aos-system-design-tasks/` 下。

---

## 四种设计场景

> 通用方法框架参见 [`00-general/10-general-design-standards/02-general-design-4modes-guide-overview.md`](00-general/10-general-design-standards/02-general-design-4modes-guide-overview.md)

| 场景 | 适用情况 | 周期 | Pipeline 指南 |
|------|---------|------|-------------|
| 瀑布式 | 全新系统，需求明确 | 30-48天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/01-waterfall-pipeline-system-design-guide.md` |
| 敏捷式 | 迭代开发，需求渐进 | 13-21天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/03-agile-pipeline-system-design-guide.md` |
| 逆向工程 | 已有系统补文档 | 16-26天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/02-reverse-engineering-pipeline-system-design-guide.md` |
| DevOps | 小变更快速交付 | 几小时-3天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/04-devops-pipeline-system-design-guide.md` |

---

## 三个关键角色

| 角色 | 职责 | 参与的层面 |
|------|------|-----------|
| **流水线开发者** | 开发、维护和优化系统设计流水线本身（主导第1层自指设计和第2层交付物构建） | 第1层、第2层 |
| **AI** | 按流水线开发者指令执行自动化任务（协助第1层和第2层工作） | 第1层、第2层 |
| **AOS 开发者** | 使用流水线进行企业运营体系的系统设计（主导第3层，含需求提出者、业务流程开发者、信息系统开发者） | 第3层 |

---

## 产品数据文件（每个项目通用结构）

两个项目的产品数据（`10-pipeline-system-product-data/` 和 `10-aos-system-product-data/`）都遵循相同结构（模板参考 `00-general/10-general-design-standards/03-specification-template.md`）：

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

---

## 关键设计文件

- [`00-general/10-general-design-standards/01-general-design-standards.md`](00-general/10-general-design-standards/01-general-design-standards.md) — 通用设计准则 v2.1（方法论核心：五层结构、核心规则、六步法、分解/分配/分析、验收标准）
- [`00-general/10-general-design-standards/02-general-design-4modes-guide-overview.md`](00-general/10-general-design-standards/02-general-design-4modes-guide-overview.md) — 通用设计指南（四种方法框架）
- [`00-general/10-general-design-standards/03-specification-template.md`](00-general/10-general-design-standards/03-specification-template.md) — 规范文档通用模板
- [`00-general/10-general-design-standards/04-general-terminology-glossary.md`](00-general/10-general-design-standards/04-general-terminology-glossary.md) — 通用术语对照
- [`10-pipeline-design/10-pipeline-system-design/01-pipeline-system-design-standards/01-pipeline-design-standards.md`](10-pipeline-design/10-pipeline-system-design/01-pipeline-system-design-standards/01-pipeline-design-standards.md) — 流水线设计准则（通用方法论 + 流水线专有）
- [`10-pipeline-design/10-pipeline-system-design/02-pipeline-system-design-guidelines/05-pipeline-system-quick-reference-card.md`](10-pipeline-design/10-pipeline-system-design/02-pipeline-system-design-guidelines/05-pipeline-system-quick-reference-card.md) — 快速参考卡
- [`10-pipeline-design/10-pipeline-system-design/03-pipeline-system-design-ai-support/00-ai-document-requirements-understanding.md`](10-pipeline-design/10-pipeline-system-design/03-pipeline-system-design-ai-support/00-ai-document-requirements-understanding.md) — AI 文档理解要求
- [`10-pipeline-design/10-pipeline-system-design/10-pipeline-system-product-data/README.md`](10-pipeline-design/10-pipeline-system-design/10-pipeline-system-product-data/README.md) — 流水线产品数据概览
- [`50-aos-design/10-aos-system-design/03-aos-system-design-ai-support/00-overview.md`](50-aos-design/10-aos-system-design/03-aos-system-design-ai-support/00-overview.md) — AOS AI 辅助概览

---

## 文档规范

- 所有文档使用 Markdown + Mermaid 格式
- 版本号格式：`v[主版本].[次版本]`
- 中文为主体语言，术语附英文对照

---

## 免重复说明

以下方法论内容已完整定义于 [`00-general/10-general-design-standards/01-general-design-standards.md`](00-general/10-general-design-standards/01-general-design-standards.md)，本文档不再展开：

| 内容 | 准则章节 |
|------|---------|
| 信息处理模式十三类（跨领域通用 + 领域特有） | §1.7.4 |
| 产品类型与产品架构形态（知识/软件/实物） | §1.7.3 |
| 架构增量变更的资产优先原则（Reuse → Improve → Add） | §4.3 |
| 端到端业务框架（三类客户、三个维度、项目间接口、业务分解方法） | §1.8 |
| 需求的分解、分配与分析（语义分解、指标分解、三项分配检查、符合性分析） | §二 |
| 功能需求与非功能需求分类体系 | §1.10 |
| 节点编号规则（架构末级/详细定义末级） | §1.9 |
| 产品同构性与设计制品参考策略 | §1.7.1-§1.7.2 |
| 验收标准与检查清单 | §五、§六 |
| 常见错误 | §七 |
