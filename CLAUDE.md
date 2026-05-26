# CLAUDE.md

为 Claude Code 提供本仓库的项目上下文。方法论的完整定义见通用设计准则 v2.4（以下简称"准则"），此处仅在摘要层面引用关键概念以便快速查阅。

---

## 一、项目概览

### 三个产品

| 产品 | 说明 | 开发空间 |
|------|------|---------|
| **企业运营体系（EOS）** | 被构建和运维的目标系统——IT/AI 化的企业运营系统，覆盖市场、研发、生产、售后和管理等业务 | `20-eos-design/`（设计），`30-eos-operation/`（产品本体） |
| **EOS 流水线** | 服务于 EOS 全生命周期的流水线，由**设计线**（系统设计）、**开发线**（组件开发）、**集成线**（集成交付）、**运维线**（系统运维）四子线组成。当前仅设计线已完成 | 构件位于 `20-eos-design/.../01~04-*` |
| **元流水线** | 用于设计 EOS 流水线的流水线。按四阶段开发：系统设计（已完成）、构件开发/集成交付/系统运维（待扩展） | `10-meta-pipeline/` |

### 三层构造链

```
元流水线 ──系统设计──→ 元流水线产品架构（含系统设计子线）
  └── 系统设计子线 ──系统设计──→ EOS 流水线 ──使用──→ EOS
```

| 层 | 内容 | 产出位置 |
|----|------|---------|
| **第1层** | 元流水线构建：构建元流水线自身 + 用其设计 EOS 流水线 | `10-meta-pipeline/` |
| **第2层** | EOS 流水线构建：展开为各子线的操作规程（准则/指南/AI 辅助/任务定义） | `20-eos-design/.../01~04-*` |
| **第3层** | EOS 构建与运维：使用 EOS 流水线做系统设计（当前）、开发、集成、运维 | `20-eos-design/` |

### 目录结构

```
00-general/                                         # 通用方法论（独立于三个产品）
└── 10-general-system-design-standards/
    ├── 01-general-system-design-standards.md        # 通用设计准则 v2.4（方法论核心）
    ├── 02-general-system-design-4modes-guide.md     # 通用设计指南（四种方法框架）
    ├── 03-specification-template.md                 # 规范文档通用模板
    └── 04-general-terminology-glossary.md           # 通用术语对照

10-meta-pipeline/                                   # 元流水线——EOS 流水线开发空间
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

30-eos-operation/                   # EOS 产品本体（待填充）
200-put-on-hold/                    # 归档
99-sessions/                        # 历史会话记录
```

---

## 二、系统设计方法

### 核心文档

- [通用设计准则 v2.4](00-general/10-general-system-design-standards/01-general-system-design-standards.md) — 方法论核心：术语体系（§一）、四条工程化设计原则（§二）、文档结对设计（§三）、业务架构设计（§四）、系统设计过程（§五）、验收标准（§六）、检查清单（§七）
- [通用设计指南](00-general/10-general-system-design-standards/02-general-system-design-4modes-guide.md) — 四种设计场景的方法框架
- [元流水线设计准则](10-meta-pipeline/10-eos-pipeline-system-design/01-eos-pipeline-system-design-specification/01-eos-pipeline-system-design-standards.md)
- [快速参考卡](10-meta-pipeline/10-eos-pipeline-system-design/02-eos-pipeline-system-design-guidelines/05-eos-pipeline-system-quick-reference-card.md)

### 四条工程化设计原则（§二）

| 原则 | 要义 | 解决的问题 |
|------|------|-----------|
| **需求相对** | "需求"和"方案"不是文档固有标签，而是相对角色 | 设计链如何跨层衔接 |
| **详概分离** | 每份文档由架构定义和详细定义两个子文档构成 | 单层文档如何组织 |
| **文档结对** | 上层需求详细定义末级与下层方案架构定义末级配对同步设计 | 跨层文档如何协同 |
| **基于资产** | 架构节点基于已有资产按复用→改进→新增优先级生成 | 架构节点如何生成 |

### 五层设计链路（§5.1）

```
第1层：原始需求及分析 [需求] (OR)
    ↓ N:1 分配
第2层：相关方需求 [需求/方案] (SR)
    ├─ 架构末级节点 ↔ 详细定义末级节点
    │
    ├─ 功能部分 ↓ N:1 分配
    │   第3层：业务架构 [方案] (BA)（独立存在）
    │   └─ 架构末级节点（IPO）—— 仅架构定义，无详细定义
    │        ↓ IPO 直接映射（去重后）
    │   第4层：系统需求 [需求/方案] (SysReq)
    │   ├─ 架构末级节点 ↔ 详细定义末级节点
    │   └─ ↓ N:1 分配
    │       第5层：产品架构 [方案] (PA)
    │       ├─ 架构末级节点 ↔ 详细定义末级节点
    │
    └─ 非功能部分 ↓ N:1 分配
        第4层：系统需求（非功能）[需求/方案] (SysReq-NFR)
        ├─ 架构末级节点 ↔ 详细定义末级节点
        └─ ↓ N:1 分配
            第5层：产品架构 [方案] (PA)
```

### 三个核心设计活动（§三）

**需求分解及分析** — 将父需求的功能和指标无重叠无遗漏地切分为子需求：

| 工作面 | 内容 | 检查要点 |
|--------|------|---------|
| **语义分解** | 将父需求的功能平整切分到子需求 | 覆盖完整性（不漏）、不超出性（不增）、逻辑一致性（不矛盾）、约束继承（不失） |
| **指标分解** | 先识别运算关系，再将父需求性能指标分配到子需求 | 3 场景：可拆分（子项组合运算满足父指标）、下放（同值继承）、暂不分解（标注向下一层传递）；分解方法及计算依据需明确记录 |

反模式：过分解（混入实现细节）、欠分解（粒度过粗无法分配）、影子需求（引入未确认内容）、约束丢失（非功能约束在子需求中消失）。

**需求分配及分析** — 末级需求条目按 1:1 约束分配到下层方案架构末级节点（N:1）：

| 检查 | 问题 | 通过条件 | 违规后果 |
|------|------|---------|---------|
| **全覆盖** | 是否所有末级需求都已分配？ | 映射覆盖 100% | 未分配的需求在下层方案中无对应设计 |
| **1:1 约束** | 每条需求是否分配到唯一架构末级节点？ | 无需求映射到多个节点 | 同一需求在多个节点中重复实现 |
| **N:1 合理性** | 每个节点承接的需求数量是否合理？ | 按语义相关性判定（>8 过度合并，1 条偏细） | 过少→粒度过细；过多→职责过宽 |

**符合性分析** — 验证每个架构末级节点是否充分满足所承接的需求集合：

| 维度 | 检查项 |
|------|--------|
| **语义符合性** | 方案节点定义是否覆盖承接需求的核心语义？映射是否语义匹配？分析有实质内容而非套话？ |
| **指标符合性** | 先识别方案节点与需求指标间的运算关系，再基于该关系计算比较；结论明确记录为**满足/降级/丢失**；测量条件和统计方式可验证 |

**时序关系**：

```text
需求分解 → 自检（覆盖/不超出/一致性/约束继承 + 指标分解验算）
    ↓
需求分配 → 自检（全覆盖/1:1/N:1合理性）
    ↓
符合性分析 → 自检（语义符合性 + 指标符合性）

分析活动贯穿全过程：每完成一次分配，立即执行符合性分析，而非集中后补。
```

### 六步工作流程（§五）

| 步 | 正式名称 | 目标 |
|----|---------|------|
| 1 | 原始需求分析及相关方需求架构定义 | 收集、规范化、分解原始需求，检测冲突和重复，建立 SR 架构 |
| 2 | 相关方需求功能部分详细定义及业务架构定义 | SR 功能部分详细定义，同步设计 BA 架构并建立映射 |
| 3 | 系统需求功能部分架构定义 | 将 BA IPO 去重后映射到 SysReq 架构末级节点 |
| 4 | 相关方需求非功能部分详细定义及系统需求非功能部分架构定义 | SR-NFR 详细定义，同步设计 SysReq-NFR 架构并建立映射 |
| 5 | 系统需求详细定义及产品架构定义 | SysReq 功能与非功能分别分解至原子粒度并分配到 PA 架构末级节点，同步设计 PA 架构并建立映射 |
| 6 | 双向追溯验证 | 验证完整追溯链路，生成符合性报告 |

元流水线的任务定义在 `10-meta-pipeline/10-eos-pipeline-system-design/04-eos-pipeline-system-design-tasks/` 各场景目录下；EOS 流水线的任务定义在 `20-eos-design/10-eos-system-design/04-eos-system-design-tasks/` 下。

---

## 三、产品数据文件

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

## 四、四种设计场景

| 场景 | 适用情况 | 周期 | 指南 |
|------|---------|------|------|
| 瀑布式 | 全新系统，需求明确 | 30-48天 | [瀑布式指南](10-meta-pipeline/10-eos-pipeline-system-design/02-eos-pipeline-system-design-guidelines/01-waterfall-eos-pipeline-system-design-guide.md) |
| 敏捷式 | 迭代开发，需求渐进 | 13-21天 | [敏捷式指南](10-meta-pipeline/10-eos-pipeline-system-design/02-eos-pipeline-system-design-guidelines/03-agile-eos-pipeline-system-design-guide.md) |
| 逆向工程 | 已有系统补文档 | 16-26天 | [逆向工程指南](10-meta-pipeline/10-eos-pipeline-system-design/02-eos-pipeline-system-design-guidelines/02-reverse-engineering-eos-pipeline-system-design-guide.md) |
| DevOps | 小变更快速交付 | 几小时-3天 | [DevOps 指南](10-meta-pipeline/10-eos-pipeline-system-design/02-eos-pipeline-system-design-guidelines/04-devops-eos-pipeline-system-design-guide.md) |

---

## 五、三个关键角色

| 角色 | 职责 | 参与层 |
|------|------|--------|
| **元流水线开发者** | 开发、维护和优化元流水线，主导系统设计 | 第1层 |
| **AI** | 按元流水线开发者指令执行自动化任务（需求分解/分配/符合性分析等系统设计操作） | 第1层 |
| **EOS 构建与运维者** | 使用 EOS 流水线对 EOS 进行系统设计、组件开发、集成交付和运维 | 第2~3层 |

---

## 六、文档规范

- 所有文档使用 Markdown + Mermaid 格式
- 版本号格式：`v[主版本].[次版本]`
- 中文为主体语言，术语附英文对照
