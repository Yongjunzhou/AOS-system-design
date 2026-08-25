# CLAUDE.md

为 Claude Code 提供本仓库的项目上下文和关键文件导航。系统设计方法论完整定义见[通用设计规范 v1.0](00-generalspec/01-generalspec-sysdev.md)。

---

## 一、项目概览

### 三个产品

| 产品 | 说明 | 开发空间 |
|------|------|---------|
| **企业运营体系（EOS）** | 被构建和运维的目标系统——企业运营体系的**信息化形态**（流水线类产品），覆盖市场、研发、生产、售后和管理等业务。当前实现形态为可配置平台 | `20-pl4eos/`（设计），`30-eos/`（产品本体） |
| **EOS 流水线** | 服务于 EOS 全生命周期的流水线，由**设计线**（系统设计）、**开发线**（组件开发）、**集成线**（集成交付）、**运维线**（系统运维）四子线组成。当前仅设计线已完成 | `20-pl4eos/`（流水线构件） |
| **元流水线** | 用于设计 EOS 流水线的流水线。按四阶段开发：系统设计（已完成）、构件开发/集成交付/系统运维（待扩展） | `10-pl4pleos/` |

### 三层构造链

```
元流水线 ──系统设计──→ 元流水线产品架构（含系统设计子线）
  └── 系统设计子线 ──系统设计──→ EOS 流水线 ──使用──→ EOS
```

| 层 | 内容 | 产出位置 |
|----|------|---------|
| **第1层** | 元流水线构建：构建元流水线自身 + 用其设计 EOS 流水线 | `10-pl4pleos/` |
| **第2层** | EOS 流水线构建：展开为各子线的操作规程（准则/指南/AI 辅助/任务定义） | `20-pl4eos/10-pl4eos-subpl-sysdev/` |
| **第3层** | EOS 构建与运维：使用 EOS 流水线做系统设计（当前）、开发、集成、运维 | `20-pl4eos/` |

### 目录结构

```
00-generalspec/                                     # 通用方法论（独立于三个产品）
├── 00-doc-conventions.md          # 文档编写约定
├── 01-generalspec-sysdev.md    # 通用设计规范 v1.0（方法论核心 + 四种设计模式，合并版）
├── 02-generalspec-comdev.md    # 构件开发通用规范（待编写）
├── 03-generalspec-sysint.md     # 集成交付通用规范（待编写）
├── 04-generalspec-sysops.md     # 系统运维通用规范（待编写）
├── 06-generalspec-glossary.md           # 通用术语对照 v2.3
└── README.md                                    # 目录说明

10-pl4pleos/                                        # 元流水线——产出 EOS 流水线的流水线
├── 00-pl4pleos-spec/                   # 设计描述文档
│   ├── 01-pl4pleos-spec-sysdev.md     #   系统设计规范
│   ├── 02-pl4pleos-spec-comdev.md     #   构件开发规范（待编写）
│   ├── 03-pl4pleos-spec-sysint.md     #   集成交付规范（待编写）
│   ├── 04-pl4pleos-spec-sysops.md     #   系统运维规范（待编写）
│   ├── 06-pl4pleos-glossary.md        #   术语对照
│   └── README.md                      #   目录说明
├── 10-pl4pleos-subpl-sysdev/           # 系统设计子线
│   ├── 00-presysdev-4-pl4eos/         #   对 EOS 流水线的 OR 预处理
│   ├── 10-wfsysdev-4-pl4eos/          #   对 EOS 流水线的瀑布式系统设计（6 任务）
│   ├── 20-resysdev-4-pl4eos/          #   对 EOS 流水线的逆向工程（8 任务）
│   ├── 30-agsysdev-4-pl4eos/          #   对 EOS 流水线的敏捷系统设计（8 任务）
│   ├── 40-opsysdev-4-pl4eos/          #   对 EOS 流水线的 DevOps（4 任务）
│   └── README.md
├── 20-pl4pleos-subpl-comdev/           # 构件开发子线（待扩展）
├── 30-pl4pleos-subpl-sysint/           # 集成交付子线（待扩展）
├── 40-pl4pleos-subpl-sysops/           # 系统运维子线（待扩展）
└── 80-pl4pleos-2-pl4eosdata/           # 运行数据—元流水线到 pl4eos 的产品数据

20-pl4eos/                                          # EOS 流水线——产出 EOS 的流水线
├── 00-pl4eos-spec/                     # 设计描述文档
│   ├── 01-pl4eos-spec-sysdev.md       #   系统设计规范
│   ├── 02-pl4eos-spec-comdev.md       #   构件开发规范（待编写）
│   ├── 03-pl4eos-spec-sysint.md       #   集成交付规范（待编写）
│   ├── 04-pl4eos-spec-sysops.md       #   系统运维规范（待编写）
│   ├── 06-pl4eos-glossary.md          #   术语对照
│   └── README.md                      #   目录说明
├── 10-pl4eos-subpl-sysdev/             # 系统设计子线
│   ├── 00-presysdev-4-eos/         #   对 EOS 的 OR 预处理（两子步骤）
│   ├── 10-wfsysdev-4-eos/             #   对 EOS 的瀑布式系统设计（6 任务）
│   ├── 20-resysdev-4-eos/             #   对 EOS 的逆向工程（8 任务）
│   ├── 30-agsysdev-4-eos/             #   对 EOS 的敏捷系统设计（8 任务）
│   ├── 40-opsysdev-4-eos/             #   对 EOS 的 DevOps（4 任务）
│   └── README.md
├── 20-pl4eos-subpl-comdev/             # 构件开发子线（待扩展）
├── 30-pl4eos-subpl-sysint/             # 集成交付子线（待扩展）
├── 40-pl4eos-subpl-sysops/             # 系统运维子线（待扩展）
├── 50-pl4eos-subpl-bizcfg/             # 业务配置子线（待扩展）
└── 80-pl4eos-2-eosdata/                # 运行数据—EOS 流水线到 EOS 的产品数据

30-eos/                   # EOS 产品本体（四条流水线的运行结果）
│   ├── 00-eos-product-spec/        # 产品规格（设计线产出）
│   ├── 10-eos-engines/             # 引擎实现（开发线产出）
│   ├── 20-eos-configs/             # 配置定义（开发线产出）
│   ├── 30-eos-deployment/          # 部署交付（集成线产出）
│   └── 40-eos-operation/           # 运维数据（运维线产出）
100-topic-research/                 # 研习素材库（学习笔记/概念讨论/研究报告，主项目素材）
50-research/                         # 教材子项目（自包含子目录，见 §九 子项目）
40-review/                          # 审查与评审（待补充）
90-hold/                            # 暂存归档
80-sessions/                        # 历史会话记录
```

---

## 二、关键设计文件

- [通用设计规范 v1.0](00-generalspec/01-generalspec-sysdev.md) — 第一部分（§一~§十 + 附录A~B）：术语体系、四条工程化设计原则、文档结对设计（两阶段工作法）、各层架构末级节点识别方法、业务流程设计（两种 BP 开发方法）、产品架构设计（三独立原则）、系统设计过程（六步工作法）、验收标准、设计检查清单、常见错误与FAQ；第二部分（§十一~§十四 + 附录C~D）：四种设计模式（PACE 维度、选择框架、切换规则）、三种核心设计活动的跨模式差异、质量门禁矩阵、通用指南与产品指南的关系
- [通用术语对照表 v2.4](00-generalspec/06-generalspec-glossary.md) — 核心术语英中对照
- [EOS系统设计规范 v1.0](20-pl4eos/00-pl4eos-spec/01-pl4eos-spec-sysdev.md) — EOS 产品特有设计规则（平台链/业务链、三层工作层面、端到端业务框架）+ 四种设计模式
- [元流水线设计规范 v1.0](10-pl4pleos/00-pl4pleos-spec/01-pl4pleos-spec-sysdev.md)

元流水线的操作规程（任务定义）位于 `10-pl4pleos/10-pl4pleos-subpl-sysdev/` 各 Skill 目录下；EOS 流水线的任务定义位于 `20-pl4eos/10-pl4eos-subpl-sysdev/` 各 Skill 目录下。

---

## 三、关键术语

| 术语 | 指代 | 说明 |
|------|------|------|
| **目标产品** | 产品 A | 正在被系统设计的产品，统一称谓 |
| **输出产品** | 产品 B | 流水线生产出来的产品，仅流水线类有此概念 |
| **用户角色** | — | 与目标产品交互的所有外部实体（操作用户、外部系统、保障者、自然环境等） |
| **用户角色架构锚定法** | — | BP 开发的通用方法，以全量用户角色集为推导锚点 |
| **输出产品架构锚定法** | — | 流水线类产品的 BP 特化路径，以输出产品 PA 节点类型为推导锚点 |

---

## 四、输出产品的数据文件

数据文件描述流水线**输出产品**的规格——即流水线上承载/跑的数据。元流水线的输出产品是 EOS 流水线（pl4eos），EOS 流水线的输出产品是 EOS 本体。两者遵循相同结构（模板见 `00-doc-conventions.md`）：

| 文件 | 内容 |
|------|------|
| `01-specified-requirements.md` | 规范化需求 |
| `02-business-summary-architecture.md` | 业务流程概要架构定义 |
| `03-business-summary-detailed.md` | 业务流程概要详细定义 |
| `04-business-detailed.md` | 业务流程详细 |
| `05-function-summary-architecture.md` | 系统功能概要架构定义 |
| `06-function-detailed.md` | 系统功能详细定义 |
| `07-product-summary.md` | 产品概要 |
| `08-traceability-matrix.md` | 追溯矩阵 |
| `09-verification-report.md` | 验证报告 |

---

## 五、四种设计场景

| 场景 | 适用情况 | 周期 | 操作指引 |
|------|---------|------|---------|
| 瀑布式 | 全新系统，需求明确 | 30-48天 | — |
| 敏捷式 | 迭代开发，需求渐进 | 13-21天 | — |
| 逆向工程 | 已有系统补文档 | 16-26天 | — |
| DevOps | 小变更快速交付 | 几小时-3天 | — |

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

---

## 八、项目记忆

### 记忆存储位置

本仓库的记忆文件位于项目根目录下的 `.claude/memory/`，纳入 Git 版本管理。这是记忆的**权威存储**，跨设备共享。

每台设备上还存在一个本机 auto-memory 路径（`C:\Users\<用户名>\.claude\projects\e--mywork-AOS\memory\`），由 Claude Code 系统自动加载。该路径是 `.claude/memory/` 的**运行时镜像**，不纳入版本管理。

### 共享工作流程

```
设备A ──→ .claude/memory/ 修改 ──→ git commit ──→ git push
                                                      ↓
设备B ──→ git pull ──→ .claude/memory/ 同步 ──→ 复制到本机 auto-memory 路径
```

1. **写入记忆**：Claude Code 将记忆文件写入 `.claude/memory/`（写入时会同步到本机 auto-memory 路径以供系统加载）
2. **共享记忆**：修改后提交 git 并推送，另一台设备 pull 后即获得全部记忆
3. **同步机制**：每台设备 pull 后，需将 `.claude/memory/` 中新文件复制到本机 auto-memory 路径（或让 Claude Code 在会话中自动完成同步）
4. **在同一台设备上追加记忆后**：提交 git → 推送到远程 → 另一台设备 pull 即可获得

### 文件规范

- 格式：Markdown 文件，每条记忆一个文件，带 YAML frontmatter（name / description / metadata.type）
- `MEMORY.md` 为索引文件，列出所有记忆文件的一行摘要
- 文件名可保持自然风格（kebab-case 或 snake_case），`MEMORY.md` 中正确引用即可

---

## 九、子项目

### 子项目隔离原则

本仓库是一个大项目（AOS 主线），下可挂**多个子项目**。每个子项目**自包含在一个子目录中**：它的产出文件、独立记忆、子 CLAUDE.md **全部只在该子目录内**，与主项目及其他子项目互不干扰。主项目只在本章保留一行指针，不复制子项目内部内容。

### 子项目指针区

| 子项目 | 位置 | 独立记忆 | 说明 |
|--------|------|---------|------|
| 教材子项目 | `50-research/` | `50-research/记忆/` | 概念研习笔记（01~08）→ 两个产出：教材书（`教材书/`）+ 培训教材（`培训教材/`）。子项目导航与记忆隔离协议见 [`50-research/CLAUDE.md`](50-research/CLAUDE.md) |

### 执行路径约定

- **处理主项目（AOS）**：工作目录 = 仓库根，读本 CLAUDE.md + 主记忆（`.claude/memory/`）。**不触碰子项目目录内容**，除非用户明确要求。
- **处理子项目（如教材）**：先 `cd 50-research`（工作目录切到子目录），读 `50-research/CLAUDE.md` + `50-research/记忆/`。**不把子项目内容写入主 `.claude/memory/`**；会话结束把最新状态同步回子项目记忆。
- **判断归属**：任务涉及的内容落在哪个目录 → 按该目录的 CLAUDE.md 与记忆执行。主项目任务不主动读子项目记忆，子项目任务不主动读主项目记忆。

### 提交边界（单仓库 + 约定分区）

仓库是**单一 git 仓库**，子项目不建独立 git。提交时按目录语义分区：

- 主项目改动与子项目改动**分别 commit**（各自语义独立，commit message 注明归属）。
- 处理主项目时，不把子项目改动混入本次提交；处理子项目时，不把主项目改动混入。
- 新子项目创建时：建子目录 → 建子 CLAUDE.md（复制隔离协议模板）→ 建 `记忆/`（独立 MEMORY.md + 主记忆）→ 在本章指针区加一行。

---

## 十、工作风格

- **禁止选项式交互**：讨论/确认事项时一律自由散文陈述（背景 + 问题 + 建议 + 理由），不用选项卡片/选项卡界面让用户做多选题；用户自由回答"改/不改/怎么改"，再据其指示执行（2026-08-25 用户定）。教材子项目侧同步记录于 [`50-research/记忆/feedback-no-option-interaction.md`](50-research/记忆/feedback-no-option-interaction.md) 及 [`50-research/CLAUDE.md`](50-research/CLAUDE.md) 工作风格节。
