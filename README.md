# AOS 系统设计项目

## 项目概述

AOS 是企业运营体系（Enterprise Operation System）的简称。本仓库包含通用方法论基础（`00-general/`）和两个系统设计项目，共用同一套设计准则和方法论，通过 AI 辅助实现流程自动化。

**两层产品关系**：
- **产品B — `10-pipeline-design/`**：运营体系系统设计流水线（"设计工具"）
- **产品A — `50-aos-design/`**：AOS 企业运营体系（"用工具设计的目标系统"）

本准则所关注的企业，业务范围涵盖机载设备的市场、研发、生产、售后及经营管理。

---

## 目录结构

```
00-general/                                          # 通用方法论基础（产品无关）
├── 10-general-design-standards/                    # 通用准则、指南、模板、术语
│   ├── 01-general-design-standards.md              # 通用设计准则（五层结构、核心规则、术语）
│   ├── 02-general-design-4modes-guide-overview.md  # 通用设计指南（四种方法框架）
│   ├── 03-specification-template.md                # 规范文档通用模板
│   └── 04-general-terminology-glossary.md          # 核心术语英中对照
├── 20-conformance-review-tools/                    # 文档符合性审查工具
│   ├── 01-conformance-review.md                    # 审查方法论文档
│   ├── 02-check-numbering.sh                       # 编号格式一致性检查
│   ├── 03-check-links.sh                           # 超链接有效性检查
│   └── 04-check-version.sh                         # 版本号格式检查

10-pipeline-design/                                 # 产品B的完整开发空间
├── 10-pipeline-system-design/                      # 阶段1：系统设计
│   ├── 01-pipeline-system-design-standards/        # Pipeline准则（通用方法论 + 流水线专有）
│   │   ├── 01-pipeline-design-standards.md  #   核心：5层结构、映射规则、流水线六步法
│   │   ├── 02 ~ 06                                 #   各层设计规范（OR/SR/BA/SysReq/PA）
│   │   └── 07-pipeline-terminology-glossary.md  #   术语表
│   ├── 02-pipeline-system-design-guidelines/       # 四种场景的设计指南
│   │   ├── 01-pipeline-system-waterfall-design-guide.md
│   │   ├── 02-pipeline-system-agile-design-guide.md
│   │   ├── 03-pipeline-system-reverse-engineering-guide.md
│   │   ├── 04-pipeline-system-devops-design-guide.md
│   │   └── 05-pipeline-system-quick-reference-card.md
│   ├── 03-pipeline-system-design-ai-support/       # 流水线产品的 AI 辅助文档
│   │   ├── 00-ai-document-requirements-understanding.md
│   │   ├── 01-pipeline-system-design-waterfall/
│   │   ├── 02-pipeline-system-design-agile/
│   │   ├── 03-pipeline-system-design-reverse-engineering/
│   │   └── 04-pipeline-system-design-devops/
│   └── 10-pipeline-system-product-data/            # 流水线的标准产品数据（9 份文档）
├── 20-pipeline-component-dev/                      # 阶段2：构件开发（待扩展）
└── 30-pipeline-integration-delivery/               # 阶段3：集成交付（待扩展）

50-aos-design/                                      # 产品A的完整开发空间
├── 10-aos-system-design/                           # 阶段1：系统设计（当前工作范围）
│   ├── 01-aos-system-design-standards/             # 参考 Pipeline 准则（产品B构件）
│   ├── 02-aos-system-design-guidelines/            # 参考 Pipeline 指南（产品B构件）
│   ├── 03-aos-system-design-ai-support/            # AOS 专用 AI 辅助文档（产品B构件）
│   │   ├── 00-overview.md
│   │   ├── 01-aos-system-design-waterfall/
│   │   ├── 02-aos-system-design-agile/
│   │   ├── 03-aos-system-design-reverse-engineering/
│   │   └── 04-aos-system-design-devops/
│   ├── 06-aos-system-design-tasks/                 # AOS 的 6 个核心任务（产品B构件）
│   │   ├── 01-aos-normalization/
│   │   ├── 02-aos-sr-ba-design/
│   │   ├── 03-aos-ba-sysreq-design/
│   │   ├── 04-aos-nfr-design/
│   │   ├── 05-aos-sysreq-pa-design/
│   │   └── 06-aos-traceability/
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

## 6 个核心任务

| 任务 | 名称 | 目标 |
|------|------|------|
| Task 1 | 需求规范化 | 收集、规范化、分解原始需求，检测冲突和重复 |
| Task 2 | SR → BA 映射 | 将相关方需求映射到业务架构末级节点 |
| Task 3 | BA → SysReq 映射 | 将业务架构映射到系统需求末级节点 |
| Task 4 | SR-NFR → SysReq-NFR 映射 | 非功能需求的平行映射 |
| Task 5 | SysReq → PA 映射 | 将系统需求映射到产品架构末级节点 |
| Task 6 | 端到端追溯分析 | 验证完整追溯链路，生成符合性报告 |

流水线产品的任务定义在 `10-pipeline-design/10-pipeline-system-design/03-pipeline-system-design-ai-support/` 各场景目录下；AOS 项目的任务定义在 `50-aos-design/10-aos-system-design/06-aos-system-design-tasks/` 下。

---

## 四种设计场景

| 场景 | 适用情况 | 周期 | 指南 |
|------|---------|------|------|
| 瀑布式 | 全新系统，需求明确 | 30-48天 | `02-pipeline-system-design-guidelines/01-pipeline-system-waterfall-design-guide.md` |
| 敏捷式 | 迭代开发，需求渐进 | 13-21天 | `02-pipeline-system-design-guidelines/02-pipeline-system-agile-design-guide.md` |
| 逆向工程 | 已有系统补文档 | 16-26天 | `02-pipeline-system-design-guidelines/03-pipeline-system-reverse-engineering-guide.md` |
| DevOps | 小变更快速交付 | 几小时-3天 | `02-pipeline-system-design-guidelines/04-pipeline-system-devops-design-guide.md` |

---

## 三个关键角色

| 角色 | 职责 |
|------|------|
| **流水线开发者** | 开发、维护和优化系统设计流水线本身 |
| **AI** | 按流水线开发者指令执行自动化任务 |
| **AOS 开发者** | 使用流水线进行企业运营体系的系统设计（含需求提出者、业务流程开发者、信息系统开发者） |

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

**最后更新**：2026-05-17  
**版本**：v4.0
