# AOS 系统设计项目

## 项目概述

本项目包含三个目的：

1. **构建运营体系之系统设计流水线（产品B）** —— 使运营体系的系统设计从手工作坊式的文档撰写，转变为结构化、可追溯、AI 辅助的工业化生产过程。
2. **基于流水线开展运营体系系统设计（产品A）** —— 使用产品B产出的工具，对企业运营体系进行完整的系统设计，产出产品A的产品数据。
3. **探索产品开发方法论** —— 通过产品B和产品A的实践，验证和提炼可复用的产品开发方法论。

仓库包含三部分内容：
- **`00-general/`** — 通用系统设计方法论（与具体产品无关的准则、指南、模板、术语）
- **`10-pipeline-design/`** — 产品B（系统设计流水线）的完整开发工作空间
- **`50-aos-design/`** — 产品A（AOS 企业运营体系）的完整开发工作空间

**当前范围**：严格限定在产品开发四阶段中的阶段1（系统设计），即从原始需求到产品架构的完整设计链路。

### 产品关系核心认知

**产品A（运营体系）** 涵盖市场、研发、生产、售后等业务，同时也包含**"设计运营体系本身"**这项业务。

运营体系中的不同业务活动可按信息处理模式分为13类：计划事务、工单事务、审批流程、合规事务、规范知识、指标看板、进展追踪、信息台账、xBOM（跨领域通用），以及设备IO、领域分析、领域建模、领域算法（领域特有）。

不同模式的活动需要不同的系统来实现，因此产品A必然表现为多个异构信息系统的组合。其中前9类跨领域通用的处理模式可以统一到同一个信息化平台中。后4类领域特有的处理模式各自独立。

**产品B（系统设计流水线）** 处理的是需求项、架构节点、追溯链接这类元信息，属于**规范知识类**处理模式，原生输出形态就是文档+AI，因此以文档形态存在即可满足需求。

**产品B在产品A中的位置：**

运营体系涵盖市场、研发、生产、售后等业务，同时也包含**"设计运营体系本身"**这项业务——产品B就是支撑这项业务的方法和工具集。产品B的 PA 构件（准则、指南、AI辅助文档、任务定义）被放置在 `50-aos-design/10-aos-system-design/` 目录下，作为团队A设计产品A时的操作规程。

**产品B的构件在产品A中的作用：**

| 知识组件（产品B的 PA 构件） | 在产品A的系统设计中充当 |
|---------|----------------------|
| **准则**（standards） | 规定五层结构、映射规则等设计规范 |
| **指南**（guidelines） | 四种场景的设计步骤指导 |
| **AI辅助文档**（ai-support） | AI 成员执行自动化任务的依据 |
| **任务定义**（tasks） | 每一步的具体操作流程 |

### 运营体系中的端到端业务框架

#### 端到端的定义

**从需求提出到需求满足**。

#### 三类客户与三个业务维度

企业有三类客户，每类客户的需求构成一个业务维度：

| 客户类型 | 提出的需求 | 对应的业务维度 |
|---------|-----------|--------------|
| 产品用户/客户 | 产品订货合同、产品研发需求、售后服务需求 | **主价值链** |
| 上级/监管方 | 经营管理目标、合规及资质取证、年度审核 | **管理监管** |
| 内部员工 | 对人、资金、物料、设备、设施、工具、数据、知识资产等需求 | **支持服务** |

三个维度不是层级拆分，而是同一企业业务的三个视角。同一项目同时受三个维度作用——归属于某个维度，被其他维度管理，向其他维度提需求。

#### 项目间接口原则

需求在端到端项目A的具体业务运行中产生，接收方是端到端项目B整体（BA 2级），B接收后自主决定内部如何分解响应，A不需要了解B的内部结构。三种接口关系：

| 关系 | 本质 | 适用范围 |
|-----|------|---------|
| 上下游 | 链式传递 | 主价值链内部 |
| 管理/被管理 | 下达要求、监督考核 | 管理监管 → 其他维度 |
| 支持/被支持 | 提出需求、统筹满足 | 支持服务 → 其他维度 |

#### 端到端项目业务分解方法

端到端项目的业务分解从**被实现对象的系统架构**中工程化推导而来：

```
端到端项目（BA 2级）
├── 价值业务 ← 由项目的"产品"决定
│     └── 项目产出什么（广义产品/服务）
│           └── 该产品的系统架构 → 架构节点类型
│                 └── 每个节点类型 → 一个从需求提出到需求满足的端到端业务
└── 管理业务 ← 项目本身的管控活动（目标、进度、成本、质量等）
```

项目的系统设计（五层方法论）产出系统架构，架构节点类型定义了价值业务的边界。详见 [`CLAUDE.md`](CLAUDE.md) 中「运营体系中的端到端业务框架」一节。

### 产品类型决定 PA 形态

产品A和产品B遵循同一套五层方法论，但 PA 产物形态不同——不是因为方法论不同，而是因为**产品类型和消费方式不同**：

| 维度 | 产品B（流水线） | 产品A（运营体系） |
|------|---------------|-----------------|
| **产品类型** | 知识/方法工具 | 企业管理信息系统 |
| **PA 构件本质** | 知识制品（准则、指南、AI辅助、任务定义） | 软件模块（前端、后端、数据） |
| **用户** | 系统设计人员（人 + AI）阅读和遵循 | 企业员工操作和使用 |
| **消费方式** | 阅读→理解→遵循；AI 读取→执行 | 运行→交互→执行业务操作 |
| **阶段2 任务** | 完善文档内容 | 编码实现、测试、部署 |
| **最终形态** | 文档集 + AI Skill | 可运行的信息系统 |

> 产品形态是连续谱。产品B不是"不能"表现为信息系统（可以做成低代码设计平台），而是"文档 + AI"的形态对运营体系开发者而言刚好够用。

### 设计原则：组织资产优先

当新增上层需求需要分配给下层方案时，架构末级节点的变更遵循以下优先级：

1. **复用（Reuse）** — 现有节点已完整覆盖需求，直接建立映射，无需变更
2. **改进（Improve）** — 通过扩展（Extend）、拆分（Split）、合并（Merge）使现有节点承接
3. **新增（Add）** — 仅当复用和改进都不可行时，才创建新末级节点

**认知基础**：每个架构末级节点都是组织资产——承载了已投入的设计工作、已建立的下游映射关系和已通过的验证记录。优先尊重和保护已有资产，是控制设计成本、维护追溯链完整性的关键。详见 [`CLAUDE.md`](CLAUDE.md) 中「架构增量变更的资产优先原则」一节。

### 三层工作层面

| 层面 | 内容 | 负责方 | 仓库位置 |
|------|------|--------|---------|
| **第1层：自指设计** | 运营体系包含"设计运营体系本身"这项业务：产品B用统一方法论对其自身需求进行系统设计，推导出产品B的产品架构 | 团队B | `10-pipeline-design/` |
| **第2层：交付物构建** | 将产品B的系统设计产物（准则、指南、AI辅助文档、任务定义）适配到产品A的上下文，形成团队A使用的设计工具 | 团队B | `50-aos-design/.../01~04-*` |
| **第3层：使用工具设计产品A** | 团队A使用第2层产出的工具，对运营体系进行系统设计，产出产品A的9份产品数据文档 | 团队A | `50-aos-design/.../10-product-data/` |

**两个产品**：
- **产品B — 系统设计流水线**：为运营体系"设计运营体系本身"这项业务提供方法支撑的知识工具型构件。**团队B** 负责开发产品B。
- **产品A — AOS 企业运营体系**：企业实际运行所依赖的 IT/AI 化运营系统。**团队A** 负责开发和优化产品A。

**团队B的构成**：流水线开发者（用户）+ AI 成员

---

## 目录结构

```
00-general/                                          # 通用方法论基础（产品无关）
├── 10-general-design-standards/                    # 通用准则、指南、模板、术语
│   ├── 01-general-design-standards.md              # 通用设计准则（五层结构、核心规则、术语）
│   ├── 02-general-design-4modes-guide-overview.md  # 通用设计指南（四种方法框架）
│   ├── 03-specification-template.md                # 规范文档通用模板
│   └── 04-general-terminology-glossary.md          # 核心术语英中对照

10-pipeline-design/                                 # 产品B的完整开发空间
├── 10-pipeline-system-design/                      # 阶段1：系统设计
│   ├── 01-pipeline-system-design-standards/        # Pipeline准则（通用方法论 + 流水线专有）
│   │   ├── 01-pipeline-design-standards.md  #   核心：5层结构、映射规则、流水线六步法
│   │   ├── 02 ~ 06                                 #   各层设计规范（OR/SR/BA/SysReq/PA）
│   │   └── 07-pipeline-terminology-glossary.md  #   术语表
│   ├── 02-pipeline-system-design-guidelines/       # 四种场景的设计指南
│   │   ├── 01-waterfall-pipeline-system-design-guide.md
│   │   ├── 03-agile-pipeline-system-design-guide.md
│   │   ├── 02-reverse-engineering-pipeline-system-design-guide.md
│   │   ├── 04-devops-pipeline-system-design-guide.md
│   │   └── 05-pipeline-system-quick-reference-card.md
│   ├── 03-pipeline-system-design-ai-support/       # 流水线产品的 AI 辅助文档
│   │   ├── 00-ai-document-requirements-understanding.md
│   │   ├── 01-waterfall-pipeline-system-design/
│   │   ├── 03-agile-pipeline-system-design/
│   │   ├── 02-reverse-engineering-pipeline-system-design/
│   │   └── 04-devops-pipeline-system-design/
│   └── 10-pipeline-system-product-data/            # 流水线的标准产品数据（9 份文档）
├── 20-pipeline-component-dev/                      # 阶段2：构件开发（待扩展）
└── 30-pipeline-integration-delivery/               # 阶段3：集成交付（待扩展）

50-aos-design/                                      # 产品A的完整开发空间
├── 10-aos-system-design/                           # 阶段1：系统设计（当前工作范围）
│   ├── 01-aos-system-design-standards/             # 参考 Pipeline 准则（产品B构件）
│   ├── 02-aos-system-design-guidelines/            # 参考 Pipeline 指南（产品B构件）
│   ├── 03-aos-system-design-ai-support/            # AOS 专用 AI 辅助文档（产品B构件）
│   │   ├── 00-overview.md
│   │   ├── 01-waterfall-aos-system-design/
│   │   ├── 03-agile-aos-system-design/
│   │   ├── 02-reverse-engineering-aos-system-design/
│   │   └── 04-devops-aos-system-design/
│   ├── 04-aos-system-design-tasks/                 # AOS 的 4 场景任务定义（产品B构件）
│   │   ├── 01-waterfall-aos-system-design/     # 瀑布式 6 个任务
│   │   ├── 03-agile-aos-system-design/         # 敏捷式 8 个任务
│   │   ├── 02-reverse-engineering-aos-system-design/ # 逆向工程 8 个任务
│   │   └── 04-devops-aos-system-design/        # DevOps 4 个任务
│   └── 10-aos-system-product-data/                 # AOS 的产品数据（产品A设计输出）
├── 20-aos-component-dev/                           # 阶段2：构件开发（待扩展）
└── 30-aos-integration-delivery/                    # 阶段3：集成交付（待扩展）

200-put-on-hold/                                    # 归档的历史文件
99-sessions/                                        # 历史会话记录
```

---

## 五层结构与核心规则

### 五层设计链路

```
第1层：原始需求 (OR)
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

| 规则 | 名称 | 定义 |
|------|------|------|
| 规则1 | **1:1 分配约束** | 每条详细定义末级节点只能分配到下层方案中唯一一个架构末级节点 |
| 规则2 | **N:1 承接支持** | 一个架构末级节点可以承接多个上层详细定义末级节点 |
| 规则3 | **双向追溯** | 支持从上层需求追溯到下层方案，也支持从下层方案反向追溯到上层需求 |

---

## 开发六步法（6 个核心任务）

| 步骤 | 名称 | 目标 |
|------|------|------|
| Step 1 | 原始需求分析及相关方需求架构定义 | 收集、规范化、分解原始需求，检测冲突和重复，建立 SR 架构 |
| Step 2 | 相关方需求功能部分详细定义及业务架构定义 | SR 功能部分详细定义，同步设计 BA 架构并建立映射 |
| Step 3 | 系统需求功能部分架构定义 | 将 BA IPO 去重后映射到 SysReq 架构末级节点 |
| Step 4 | 相关方需求非功能部分详细定义及系统需求非功能部分架构定义 | SR-NFR 详细定义，同步设计 SysReq-NFR 架构并建立映射 |
| Step 5 | 系统需求详细定义及产品架构定义 | SysReq 详细定义（6-9级分解），同步设计 PA 架构并建立映射 |
| Step 6 | 双向追溯验证 | 验证完整追溯链路，生成符合性报告 |

流水线产品的任务定义在 `10-pipeline-design/10-pipeline-system-design/04-pipeline-system-design-tasks/` 各场景目录下；AOS 项目的任务定义在 `50-aos-design/10-aos-system-design/04-aos-system-design-tasks/` 下。

---

## 四种设计场景

| 场景 | 适用情况 | 周期 | 指南 |
|------|---------|------|------|
| 瀑布式 | 全新系统，需求明确 | 30-48天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/01-waterfall-pipeline-system-design-guide.md` |
| 敏捷式 | 迭代开发，需求渐进 | 13-21天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/03-agile-pipeline-system-design-guide.md` |
| 逆向工程 | 已有系统补文档 | 16-26天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/02-reverse-engineering-pipeline-system-design-guide.md` |
| DevOps | 小变更快速交付 | 几小时-3天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/04-devops-pipeline-system-design-guide.md` |

---

## 三个关键角色

| 角色 | 职责 | 参与的层面 |
|------|------|-----------|
| **流水线开发者** | 开发、维护和优化系统设计流水线本身 | 第1层、第2层 |
| **AI** | 按流水线开发者指令执行自动化任务 | 第1层、第2层 |
| **AOS 开发者** | 使用流水线进行企业运营体系的系统设计（含需求提出者、业务流程开发者、信息系统开发者） | 第3层 |

---

## 产品数据文件结构

两个项目的产品数据（`10-pipeline-system-product-data/` 和 `10-aos-system-product-data/`）都遵循相同的 9 份文档结构：

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

## 关键文件

| 文件 | 说明 |
|------|------|
| `10-pipeline-design/10-pipeline-system-design/01-pipeline-system-design-standards/01-pipeline-design-standards.md` | 核心设计准则（5层结构、映射规则、术语定义） |
| `10-pipeline-design/10-pipeline-system-design/02-pipeline-system-design-guidelines/05-pipeline-system-quick-reference-card.md` | 快速参考卡 |
| `10-pipeline-design/10-pipeline-system-design/03-pipeline-system-design-ai-support/00-ai-document-requirements-understanding.md` | AI 文档理解要求 |
| `10-pipeline-design/10-pipeline-system-design/10-pipeline-system-product-data/README.md` | 流水线产品数据概览 |
| `50-aos-design/10-aos-system-design/03-aos-system-design-ai-support/00-overview.md` | AOS AI 辅助概览 |
| `CLAUDE.md` | Claude Code 项目指导 |

---

## 文档规范

- 所有文档使用 Markdown + Mermaid 格式
- 版本号格式：`v[主版本].[次版本]`
- 中文为主体语言，术语附英文对照

---

**最后更新**：2026-05-22  
**版本**：v4.2
