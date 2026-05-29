# CLAUDE.md

为 Claude Code 提供本仓库的项目上下文和关键文件导航。系统设计方法论完整定义见[通用设计准则 v2.5](00-general/10-general-system-design-standards/01-general-system-design-standards.md)。

---

## 一、项目概览

### 三个产品

| 产品 | 说明 | 开发空间 |
|------|------|---------|
| **企业运营体系（EOS）** | 被构建和运维的目标系统——企业运营体系的**信息化形态**（流水线类产品），覆盖市场、研发、生产、售后和管理等业务。当前实现形态为可配置平台 | `20-eos-design/`（设计），`30-eos/`（产品本体） |
| **EOS 流水线** | 服务于 EOS 全生命周期的流水线，由**设计线**（系统设计）、**开发线**（组件开发）、**集成线**（集成交付）、**运维线**（系统运维）四子线组成。当前仅设计线已完成 | 构件位于 `20-eos-design/.../01~04-*` |
| **元流水线** | 用于设计 EOS 流水线的流水线。按四阶段开发：系统设计（已完成）、构件开发/集成交付/系统运维（待扩展） | `10-eos-pipeline-design/` |

### 三层构造链

```
元流水线 ──系统设计──→ 元流水线产品架构（含系统设计子线）
  └── 系统设计子线 ──系统设计──→ EOS 流水线 ──使用──→ EOS
```

| 层 | 内容 | 产出位置 |
|----|------|---------|
| **第1层** | 元流水线构建：构建元流水线自身 + 用其设计 EOS 流水线 | `10-eos-pipeline-design/` |
| **第2层** | EOS 流水线构建：展开为各子线的操作规程（准则/指南/AI 辅助/任务定义） | `20-eos-design/.../01~04-*` |
| **第3层** | EOS 构建与运维：使用 EOS 流水线做系统设计（当前）、开发、集成、运维 | `20-eos-design/` |

### 目录结构

```
00-general/                                         # 通用方法论（独立于三个产品）
└── 10-general-system-design-standards/
    ├── 01-general-system-design-standards.md        # 通用设计准则 v2.5（方法论核心）
    ├── 02-general-system-design-4modes-guide.md     # 通用设计指南（四种方法框架）
    ├── 03-specification-template.md                 # 规范文档通用模板
    └── 04-general-terminology-glossary.md           # 通用术语对照 v2.3

10-eos-pipeline-design/                                   # 元流水线——EOS 流水线开发空间
└── 10-eos-pipeline-system-design/                  # 元流水线的系统设计（当前范围）
    ├── 01-*specification/                              # 准则（通用方法论 + 元流水线专有）
    ├── 02-*guidelines/                                 # 四种场景的设计指南
    ├── 03-*ai-support/                                 # AI 辅助文档
    ├── 04-*tasks/                                      # 26 个操作规程任务文档
    └── 10-*product-data/                               # 9 份标准产品数据文档

20-eos-design/                                     # EOS 开发空间
├── 10-eos-system-design/                          # EOS 系统设计（当前工作范围）
│   ├── 01-*specification/                              # 准则（EOS 流水线—设计线构件）
│   ├── 02-*guidelines/                                 # 指南（EOS 流水线—设计线构件）
│   ├── 03-*ai-support/                                 # AI 辅助文档
│   ├── 04-*tasks/                                      # 4 场景任务定义
│   └── 10-*product-data/                               # EOS 产品数据
├── 20-eos-component-dev/                           # 构件开发（待扩展）
└── 30-eos-integration-delivery/                    # 集成交付（待扩展）

30-eos/                   # EOS 产品本体（四条流水线的运行结果）
│   ├── 01-product-specification/            # 产品规格（设计线产出）
│   ├── 02-engines/                          # 引擎实现（开发线产出）
│   ├── 03-configurations/                   # 配置定义（开发线产出）
│   ├── 04-deployment/                       # 部署交付（集成线产出）
│   └── 05-operation/                        # 运维数据（运维线产出）
200-put-on-hold/                    # 归档
99-sessions/                        # 历史会话记录
```

---

## 二、关键设计文件

- [通用设计准则 v2.5](00-general/10-general-system-design-standards/01-general-system-design-standards.md) — 方法论核心：术语体系（§一）、四条工程化设计原则（§二）、文档结对设计（§三）、业务架构设计（§四，含两种 BA 开发方法：用户角色架构锚定法 §4.2.1 + 输出产品架构锚定法 §4.2.2）、系统设计过程（§五）、验收标准（§六）、检查清单（§七）
- [通用设计指南 v2.1](00-general/10-general-system-design-standards/02-general-system-design-4modes-guide.md) — 四种设计场景的方法框架
- [通用术语对照表 v2.3](00-general/10-general-system-design-standards/04-general-terminology-glossary.md) — 核心术语英中对照
- [EOS系统设计准则 v3.1](20-eos-design/10-eos-system-design/10-eos-system-design-specification/01-eos-system-design-standards.md) — EOS 产品特有设计规则（平台链/业务链、三层工作层面、端到端业务框架）
- [元流水线设计准则](10-eos-pipeline-design/10-eos-pipeline-system-design/10-eos-pipeline-system-design-specification/01-eos-pipeline-system-design-standards.md)
- [元流水线 AI 文档理解要求](10-eos-pipeline-design/10-eos-pipeline-system-design/30-eos-pipeline-system-design-ai-support/00-ai-document-requirements-understanding.md)
- [EOS AI 辅助概览](20-eos-design/10-eos-system-design/30-eos-system-design-ai-support/00-overview.md)

元流水线的操作规程（任务定义）位于 `10-eos-pipeline-design/10-eos-pipeline-system-design/20-eos-pipeline-system-design-tasks/` 各场景目录下；EOS 流水线的任务定义位于 `20-eos-design/10-eos-system-design/20-eos-system-design-tasks/` 下。

---

## 三、关键术语

| 术语 | 指代 | 说明 |
|------|------|------|
| **目标产品** | 产品 A | 正在被系统设计的产品，统一称谓 |
| **输出产品** | 产品 B | 流水线生产出来的产品，仅流水线类有此概念 |
| **用户角色** | — | 与目标产品交互的所有外部实体（操作用户、外部系统、保障者、自然环境等） |
| **用户角色架构锚定法** | — | BA 开发的通用方法，以全量用户角色集为推导锚点 |
| **输出产品架构锚定法** | — | 流水线类产品的 BA 特化路径，以输出产品 PA 节点类型为推导锚点 |

---

## 四、产品数据文件

元流水线和 EOS 的产品数据遵循相同结构（模板见 `03-specification-template.md`）：

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

## 五、四种设计场景

| 场景 | 适用情况 | 周期 | 操作指引 |
|------|---------|------|---------|
| 瀑布式 | 全新系统，需求明确 | 30-48天 | [瀑布式工作流](10-eos-pipeline-design/10-eos-pipeline-system-design/30-eos-pipeline-system-design-ai-support/01-waterfall-eos-pipeline-system-design/workflow-prompts.md) |
| 敏捷式 | 迭代开发，需求渐进 | 13-21天 | [敏捷式工作流](10-eos-pipeline-design/10-eos-pipeline-system-design/30-eos-pipeline-system-design-ai-support/03-agile-eos-pipeline-system-design/workflow-prompts.md) |
| 逆向工程 | 已有系统补文档 | 16-26天 | [逆向工程工作流](10-eos-pipeline-design/10-eos-pipeline-system-design/30-eos-pipeline-system-design-ai-support/02-reverse-engineering-eos-pipeline-system-design/workflow-prompts.md) |
| DevOps | 小变更快速交付 | 几小时-3天 | [DevOps 工作流](10-eos-pipeline-design/10-eos-pipeline-system-design/30-eos-pipeline-system-design-ai-support/04-devops-eos-pipeline-system-design/workflow-prompts.md) |

---

## 六、三个关键角色

| 角色 | 职责 | 参与层 |
|------|------|--------|
| **元流水线开发者** | 开发、维护和优化元流水线，主导系统设计 | 第1层 |
| **AI** | 按元流水线开发者指令执行自动化任务（需求分解/分配/符合性分析等系统设计操作） | 第1层 |
| **EOS 构建与运维者** | 使用 EOS 流水线对 EOS 进行系统设计、组件开发、集成交付和运维 | 第2~3层 |

---

## 七、文档规范

- 所有文档使用 Markdown + Mermaid 格式
- 版本号格式：`v[主版本].[次版本]`
- 中文为主体语言，术语附英文对照
