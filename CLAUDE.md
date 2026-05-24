# CLAUDE.md

本文为 Claude Code 提供本仓库的项目上下文和快速参考信息。方法论的完整定义见通用设计准则，本文仅在摘要层面引用关键概念以便快速查阅。

---

## 项目输出

| 产品 | 说明 | 开发空间 |
|------|------|---------|
| **企业运营体系（EOS）** | 被构建和运维的目标系统——IT/AI 化的企业运营系统，覆盖市场、研发、生产、售后和管理等业务 | 开发空间 `20-eos-design/`，产品本体 `30-eos-operation/` |
| **EOS 流水线** | 服务于 EOS 全生命周期的流水线，由**设计线**（系统设计）、**开发线**（组件开发）、**集成线**（集成交付）、**运维线**（系统运维）四个子流水线组成。当前设计线已完成，其余待开发 | 构件位于 `20-eos-design/.../01~04-*` |
| **元流水线** | 用于构建 EOS 流水线的工具和规则体系。采用自指设计，用自身方法论设计自身，产出 EOS 流水线的完整架构定义。自身按四阶段开发：系统设计（已完成）、构件开发（待扩展）、集成交付（待扩展）、系统运维（待扩展） | `10-pipeline-design/` |

---

## 项目概览

本项目包含四个目的：

1. **构建与运维 EOS** —— 使用 EOS 流水线（设计线/开发线/集成线/运维线）对 EOS 进行系统设计、组件开发、集成交付和系统运维。当前系统设计段已就绪，其余阶段待流水线对应子线完成后同步推进。

2. **构建 EOS 流水线** —— 构建设计线（当前工作范围）以及开发线、集成线、运维线（待扩展），形成完整的 EOS 全生命周期支撑能力。

3. **构建元流水线** —— 采用五层设计方法论进行自指设计，其产出物即为 EOS 流水线的完整架构定义。

4. **探索复杂产品开发方法论及实例** —— 通过三个产品的实践沉淀通用经验，含准则、模板、术语和实例。

仓库包含四部分内容：
- **`00-general/`** — 通用方法论（产品实践中沉淀的经验，独立于三个产品之外）
- **`10-pipeline-design/`** — 元流水线的完整开发工作空间
- **`20-eos-design/`** — EOS 的完整开发工作空间（内含 EOS 流水线构件）
- **`30-eos-operation/`** — EOS 产品本身—各业务线及业务数据

**当前工作重点**：
- **元流水线**：开发严格限定在系统设计，即从原始需求到产品架构的完整设计链路
- **EOS 流水线**：设计线已成型，其余三线待元流水线扩展后建设
- **EOS**：系统设计在进行中，构件开发/集成交付/系统运维待流水线对应子线就绪

---

## 三层产品构造链

本项目的三个产品按构造关系分为三层：**元流水线**（第1层）以自身为对象应用五层系统设计方法论（自指设计，详见 [`00-general/`](00-general/)），产出 **EOS 流水线**（第2层）；EOS 流水线用于构建与运维 **EOS**（第3层）。三者构成一条清晰的构造链：

```
元流水线 ──自指设计──→ EOS 流水线 ──使用──→ EOS
```

| 构造层 | 内容 | 产出位置 |
|--------|------|---------|
| **第1层：元流水线自指构建** | 元流水线用统一方法论对自身需求进行系统设计，推导出元流水线的产品架构，进而定义 EOS 流水线的完整架构 | `10-pipeline-design/` |
| **第2层：EOS 流水线构建** | 元流水线的 PA 构件（准则、指南、AI 辅助文档、任务定义）构成 EOS 流水线各子线的操作规程。这些构件嵌入在 EOS 的开发空间中 | `20-eos-design/.../01~04-*` |
| **第3层：流水线驱动的 EOS 构建与运维** | 使用 EOS 流水线对 EOS 进行系统设计（当前）、组件开发、系统集成、系统运维 | `20-eos-design/` |

### EOS 流水线的四个组成部分

EOS 流水线由四条子流水线组成，当前仅设计线已完成：

| 子流水线 | 简称 | 状态 | 构件位置 |
|---------|------|------|---------|
| 系统设计流水线 | 设计线 | 已完成 | `20-eos-design/.../01~04-*` |
| 组件开发流水线 | 开发线 | 待开发 | `20-eos-component-dev/` |
| 系统集成流水线 | 集成线 | 待开发 | `30-eos-integration-delivery/` |
| 系统运维流水线 | 运维线 | 待开发 | — |

### 元流水线的四个组成部分

元流水线按四阶段开发，当前仅系统设计已完成：

| 开发阶段 | 状态 | 位置 |
|---------|------|------|
| 系统设计 | 已完成 | `10-pipeline-design/10-pipeline-system-design/` |
| 组件开发 | 待扩展 | `10-pipeline-design/20-pipeline-component-dev/` |
| 集成交付 | 待扩展 | `10-pipeline-design/30-pipeline-integration-delivery/` |
| 系统运维 | 待扩展 | — |

### 产品同构性

三个产品共享同一套五层结构和设计方法论。通用方法论核心位于 [`00-general/`](00-general/)。

#### 元流水线

| 子目录 | 参考来源 | 策略 |
|--------|---------|------|
| `01-pipeline-system-design-specification/` | `00-general/` 通用准则 | 方法论核心参考通用准则，专有规则独立开发 |
| `02-pipeline-system-design-guidelines/` | `00-general/` 通用指南框架 | 框架参考，场景化定制 |
| `03-pipeline-system-design-ai-support/` | — | 自指设计，独立开发 |
| `04-pipeline-system-design-tasks/` | — | 自指设计，独立开发 |
| `10-pipeline-system-product-data/` | `00-general/03-specification-template.md` | 模板结构参考 |

#### EOS 流水线

| 子目录 | 参考来源 | 策略 |
|--------|---------|------|
| `01-eos-system-design-specification/` | `00-general/` 通用准则 + 元流水线对应构件 | 通用方法论参考通用准则，EOS 流水线设计阶段参考元流水线 |
| `02-eos-system-design-guidelines/` | `00-general/` 通用指南 + 元流水线对应构件 | 通用方法框架参考通用指南，示例参考元流水线 |
| `03-eos-system-design-ai-support/` | 元流水线对应构件 | 结构参考，内容需定制（场景不同） |
| `04-eos-system-design-tasks/` | 元流水线对应构件 | 结构参考，内容需定制（操作对象不同） |

#### EOS

| 目录 | 说明 |
|------|------|
| `10-eos-system-product-data/` | EOS 的产品定义在本项目范围内的体现——系统设计各层产出（OR→SR→BA→SysReq→PA），其中 `07-product-architecture.md` 定义业务模块结构 |
| `30-eos-operation/` | EOS 产品本体，含各业务线及业务数据。通过 EOS 流水线各子线逐步构建，最终形成可运行的运营体系 |

---

## 实际目录结构

```
00-general/                                     # 通用方法论基础
├── 10-general-system-design-standards/               # 通用准则、指南、模板、术语
│   ├── 01-general-system-design-standards.md          # 通用设计准则（方法论核心，v2.1）
│   ├── 02-general-system-design-4modes-guide.md # 通用设计指南
│   ├── 03-specification-template.md            # 规范文档通用模板
│   └── 04-general-terminology-glossary.md      # 通用术语对照

10-pipeline-design/                             # 元流水线的完整开发工作空间
├── 10-pipeline-system-design/                  # 元流水线的系统设计
│   ├── 01-pipeline-system-design-specification/    # 准则（通用方法论 + 元流水线专有）
│   │   └── 01-pipeline-system-design-standards.md
│   ├── 02-pipeline-system-design-guidelines/   # 四种场景的设计指南
│   │   ├── 01-waterfall-pipeline-system-design-guide.md
│   │   ├── 03-agile-pipeline-system-design-guide.md
│   │   ├── 02-reverse-engineering-pipeline-system-design-guide.md
│   │   └── 04-devops-pipeline-system-design-guide.md
│   ├── 03-pipeline-system-design-ai-support/   # 元流水线的 AI 辅助文档
│   │   ├── 00-ai-document-requirements-understanding.md
│   │   ├── 01-waterfall-pipeline-system-design/
│   │   ├── 03-agile-pipeline-system-design/
│   │   ├── 02-reverse-engineering-pipeline-system-design/
│   │   └── 04-devops-pipeline-system-design/
│   ├── 04-pipeline-system-design-tasks/        # 元流水线的操作规程（26 个任务文档）
│   │   ├── 01-waterfall-pipeline-system-design/
│   │   ├── 03-agile-pipeline-system-design/
│   │   ├── 02-reverse-engineering-pipeline-system-design/
│   │   └── 04-devops-pipeline-system-design/
│   └── 10-pipeline-system-product-data/        # 元流水线的标准产品数据（9 份文档）
├── 20-pipeline-component-dev/                  # 元流水线的构件开发（待扩展）
└── 30-pipeline-integration-delivery/           # 元流水线的集成交付（待扩展）

20-eos-design/                                  # EOS 的完整开发空间
├── 10-eos-system-design/                       # EOS 的系统设计（当前工作范围）
│   ├── 01-eos-system-design-specification/         # 准则（EOS 流水线—设计线构件）
│   ├── 02-eos-system-design-guidelines/        # 指南（EOS 流水线—设计线构件）
│   ├── 03-eos-system-design-ai-support/        # EOS 专用 AI 辅助文档（EOS 流水线—设计线构件）
│   │   ├── 01-waterfall-eos-system-design/
│   │   ├── 03-agile-eos-system-design/
│   │   ├── 02-reverse-engineering-eos-system-design/
│   │   └── 04-devops-eos-system-design/
│   ├── 04-eos-system-design-tasks/             # 4 场景任务定义（EOS 流水线—设计线构件）
│   │   ├── 01-waterfall-eos-system-design/     # 瀑布式 6 个任务
│   │   ├── 03-agile-eos-system-design/         # 敏捷式 8 个任务
│   │   ├── 02-reverse-engineering-eos-system-design/ # 逆向工程 8 个任务
│   │   └── 04-devops-eos-system-design/        # DevOps 4 个任务
│   └── 10-eos-system-product-data/             # EOS 的产品数据（EOS 设计输出）
├── 20-eos-component-dev/                       # EOS 的构件开发（待扩展）
└── 30-eos-integration-delivery/                # EOS 的集成交付（待扩展）

30-eos-operation/                               # EOS 产品本体（各业务线及业务数据）
├── ...                                         # （待填充）

200-put-on-hold/                                # 归档的历史文件
99-sessions/                                    # 历史会话记录
```

---

## 系统设计

### 五层结构与核心规则

> **方法论基础**：详见 [`00-general/10-general-system-design-standards/01-general-system-design-standards.md`](00-general/10-general-system-design-standards/01-general-system-design-standards.md) §三「5层结构概要」和 §四「设计方法」

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

### 需求的分解、分配与分析

三个核心设计活动顺序执行，每完成一个立即自检。

### 需求分解及分析

| 工作面 | 内容 | 检查要点 |
|--------|------|---------|
| **语义分解** | 将父需求的功能平整切分到子需求 | 覆盖完整性（不漏）、不超出性（不增）、逻辑一致性（不矛盾）、约束继承（不失） |
| **指标分解** | 将父需求性能指标分配到子需求 | 可拆分（子项之和≤父项）、下放（同指标继承）、暂不分解（标注向下一层传递） |

**常见反模式**：过分解（混入实现细节）、欠分解（粒度过粗无法分配）、影子需求（引入未确认内容）、约束丢失（非功能约束在子需求中消失）。

### 需求分配及分析

分解完成的末级需求条目分配到下层方案架构末级节点，执行三项检查：

| 检查 | 问题 | 通过条件 |
|------|------|---------|
| **全覆盖** | 是否所有末级需求都已分配？ | 映射覆盖 100% |
| **1:1 约束** | 每条需求是否分配到唯一架构末级节点？ | 无需求映射到多个节点 |
| **N:1 合理性** | 每个节点承接的需求数量是否合理？ | 推荐 2-5 条/节点 |

### 架构承接需求分析

确认每个架构末级节点是否充分满足所承接的需求集合：

| 维度 | 检查项 |
|------|--------|
| **语义符合性** | 方案节点定义是否覆盖承接需求的核心语义？映射是否语义匹配？分析是否有实质内容？ |
| **指标符合性** | 指标是否被显式承接？方案值是否不降级？指标是否可验证？覆盖全部承接需求的指标？ |

### 时序关系

```
需求分解 → 自检（覆盖/不超出/一致性/约束继承 + 指标分解验算）
    ↓
需求分配 → 自检（全覆盖/1:1/N:1合理性）
    ↓
架构承接需求分析 → 自检（语义符合性 + 指标符合性）

分析活动贯穿全过程：每完成一次分配，立即执行符合性分析，而非集中后补。
```

> 详见 [`00-general/10-general-system-design-standards/01-general-system-design-standards.md`](00-general/10-general-system-design-standards/01-general-system-design-standards.md) §二「需求的分解、分配与分析」

### 开发六步法（6 个核心任务）

> 名称来源：通用设计准则 §4.2「设计链路六步工作」

| 步骤 | 正式名称 | 目标 |
|------|---------|------|
| Step 1 | 原始需求分析及相关方需求架构定义 | 收集、规范化、分解原始需求，检测冲突和重复，建立 SR 架构 |
| Step 2 | 相关方需求功能部分详细定义及业务架构定义 | SR 功能部分详细定义，同步设计 BA 架构并建立映射 |
| Step 3 | 系统需求功能部分架构定义 | 将 BA IPO 去重后映射到 SysReq 架构末级节点 |
| Step 4 | 相关方需求非功能部分详细定义及系统需求非功能部分架构定义 | SR-NFR 详细定义，同步设计 SysReq-NFR 架构并建立映射 |
| Step 5 | 系统需求详细定义及产品架构定义 | SysReq 详细定义（6-9级分解），同步设计 PA 架构并建立映射 |
| Step 6 | 双向追溯验证 | 验证完整追溯链路，生成符合性报告 |

元流水线的任务定义在 `10-pipeline-design/10-pipeline-system-design/04-pipeline-system-design-tasks/` 各场景目录下；EOS 流水线（设计线）的任务定义在 `20-eos-design/10-eos-system-design/04-eos-system-design-tasks/` 下。

---

## 四种设计场景

> 通用方法框架参见 [`00-general/10-general-system-design-standards/02-general-system-design-4modes-guide.md`](00-general/10-general-system-design-standards/02-general-system-design-4modes-guide.md)

| 场景 | 适用情况 | 周期 | Pipeline 指南 |
|------|---------|------|-------------|
| 瀑布式 | 全新系统，需求明确 | 30-48天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/01-waterfall-pipeline-system-design-guide.md` |
| 敏捷式 | 迭代开发，需求渐进 | 13-21天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/03-agile-pipeline-system-design-guide.md` |
| 逆向工程 | 已有系统补文档 | 16-26天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/02-reverse-engineering-pipeline-system-design-guide.md` |
| DevOps | 小变更快速交付 | 几小时-3天 | `10-pipeline-design/.../02-pipeline-system-design-guidelines/04-devops-pipeline-system-design-guide.md` |

---

## 三个关键角色

| 角色 | 职责 | 参与构造层 |
|------|------|-----------|
| **元流水线开发者** | 开发、维护和优化元流水线（主导自指设计） | 第1层 |
| **AI** | 按元流水线开发者指令执行自动化任务 | 第1层 |
| **EOS 构建与运维者** | 使用 EOS 流水线对 EOS 进行系统设计、组件开发、集成交付和运维（含需求提出者、业务流程开发者、信息系统开发者） | 第2层、第3层 |

---

## 产品数据文件（每个项目通用结构）

元流水线和 EOS 的产品数据（`10-pipeline-system-product-data/` 和 `10-eos-system-product-data/`）都遵循相同结构（模板参考 `00-general/10-general-system-design-standards/03-specification-template.md`）：

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

- [`00-general/10-general-system-design-standards/01-general-system-design-standards.md`](00-general/10-general-system-design-standards/01-general-system-design-standards.md) — 通用设计准则 v2.1（方法论核心：五层结构、核心规则、六步法、分解/分配/分析、验收标准）
- [`00-general/10-general-system-design-standards/02-general-system-design-4modes-guide.md`](00-general/10-general-system-design-standards/02-general-system-design-4modes-guide.md) — 通用设计指南（四种方法框架）
- [`00-general/10-general-system-design-standards/03-specification-template.md`](00-general/10-general-system-design-standards/03-specification-template.md) — 规范文档通用模板
- [`00-general/10-general-system-design-standards/04-general-terminology-glossary.md`](00-general/10-general-system-design-standards/04-general-terminology-glossary.md) — 通用术语对照
- [`10-pipeline-design/10-pipeline-system-design/01-pipeline-system-design-specification/01-pipeline-system-design-standards.md`](10-pipeline-design/10-pipeline-system-design/01-pipeline-system-design-specification/01-pipeline-system-design-standards.md) — 元流水线设计准则
- [`10-pipeline-design/10-pipeline-system-design/02-pipeline-system-design-guidelines/05-pipeline-system-quick-reference-card.md`](10-pipeline-design/10-pipeline-system-design/02-pipeline-system-design-guidelines/05-pipeline-system-quick-reference-card.md) — 快速参考卡
- [`10-pipeline-design/10-pipeline-system-design/03-pipeline-system-design-ai-support/00-ai-document-requirements-understanding.md`](10-pipeline-design/10-pipeline-system-design/03-pipeline-system-design-ai-support/00-ai-document-requirements-understanding.md) — AI 文档理解要求
- [`10-pipeline-design/10-pipeline-system-design/10-pipeline-system-product-data/README.md`](10-pipeline-design/10-pipeline-system-design/10-pipeline-system-product-data/README.md) — 元流水线产品数据概览
- [`20-eos-design/10-eos-system-design/03-eos-system-design-ai-support/00-overview.md`](20-eos-design/10-eos-system-design/03-eos-system-design-ai-support/00-overview.md) — EOS AI 辅助概览

---

## 文档规范

- 所有文档使用 Markdown + Mermaid 格式
- 版本号格式：`v[主版本].[次版本]`
- 中文为主体语言，术语附英文对照

---

## 免重复说明

以下方法论内容已完整定义于 [`00-general/10-general-system-design-standards/01-general-system-design-standards.md`](00-general/10-general-system-design-standards/01-general-system-design-standards.md)，本文档不再展开：

| 内容 | 准则章节 |
|------|---------|
| 架构增量变更的资产优先原则（Reuse → Improve → Add） | §2.4.3 |
| 端到端业务框架（三类客户、三个维度、项目间接口、业务分解方法） | §1.8 |
| 功能需求与非功能需求分类体系 | §1.3 |
| 节点编号规则（架构末级/详细定义末级） | §3.4 |
| 产品同构性 | §1.6 |
| 设计制品参考策略 | §8.1 |
| 验收标准与检查清单 | §六、§七 |
