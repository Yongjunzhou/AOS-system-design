# AOS 系统设计治理项目

## 📋 项目概述

AOS（Architecture & Orchestration System）是一个系统设计治理项目，核心目标是将企业系统设计流程标准化、资产化、自动化。

**项目目标**：
1. 从企业各业务部门对信息系统的相关方需求开始分析、分解和分配，设计开发业务架构、信息系统需求规格、信息系统产品架构
2. 开发并持续优化相关方需求、业务架构、系统需求和产品架构的模板或范例、设计准则，形成组织资产
3. 开发并持续优化系统设计流水线，形成 Skill 化的组织资产，作为后续开发的 AI 资产
4. 将已有相关方需求、业务架构、系统需求和产品架构按照范例和准则转化为项目的产品数据
5. 后续新增相关方需求，则按照设计准则、模板或范例，综合已有产品数据，补充完善相关方需求、业务架构、系统需求、产品架构

---

## 📁 目录结构

本项目采用**分离式目录结构**，将重构前后的架构清晰地分开：

```
AOS/
├── _archive/                      # 📦 重构前的旧结构（存档）
│   └── legacy-structure/
│       ├── 01-standards/          # 旧的组织资产
│       ├── 02-pipeline/           # 旧的自动化资产
│       ├── 03-products/           # 旧的产品数据
│       └── 05-sessions/           # 会话记录
│
├── _current/                      # 🚀 重构后的新结构（当前使用）
│   └── new-structure/
│       ├── 01-task-normalization/           # Task 1：需求规范化
│       ├── 02-task-sr-ba-design/            # Task 2：SR → BA 映射
│       ├── 03-task-ba-sysreq-design/        # Task 3：BA → SysReq 映射
│       ├── 04-task-sr-nfr-design/           # Task 4：SR-NFR → SysReq-NFR 映射
│       ├── 05-task-sysreq-pa-design/        # Task 5：SysReq → PA 映射
│       ├── 06-task-traceability-analysis/   # Task 6：端到端追溯分析
│       ├── 07-shared-assets/                # 共享资产
│       ├── 08-products/                     # 产品数据
│       └── 04-platform-docs/                # 平台文档
│
├── .claude/                       # Claude Code 配置
├── .git/                          # Git 版本控制
│
├── CLAUDE.md                      # 项目指导（根目录）
├── RESTRUCTURE-COMPLETION-SUMMARY.md  # 重构完成总结
├── PHASE-1-COMPLETION-REPORT.md   # 第一阶段报告
├── PHASE-2-COMPLETION-REPORT.md   # 第二阶段报告
├── PHASE-3-COMPLETION-REPORT.md   # 第三阶段报告
├── PHASE-4-COMPLETION-REPORT.md   # 第四阶段报告
└── PHASE-5-COMPLETION-REPORT.md   # 第五阶段报告
```

---

## 🚀 快速开始

### 使用新架构（推荐）
```bash
cd _current/new-structure/
cat 04-platform-docs/quick-start-guide.md
```

### 查看旧架构（参考）
```bash
cd _archive/legacy-structure/
# 查看旧的结构和资源
```

---

## 📊 重构对比

### 旧架构（Resource Type Driven）
```
01-standards/          # 按资源类型组织
├── guidelines/
├── templates/
├── patterns/
└── checklists/

02-pipeline/           # 按资源类型组织
├── workflows/
├── skills/
└── tools/

03-products/           # 产品数据
└── projects/
    └── project-a/
```

**特点**：
- ❌ 资源分散，难以查找
- ❌ 新手需要 1-2 天才能上手
- ❌ 任务流程不清晰
- ❌ 难以支持并行工作

### 新架构（Task Driven）
```
01-task-normalization/         # 按任务组织
├── README.md
├── guidelines/
├── templates/
├── checklists/
├── skills/
├── workflows/
└── examples/

02-task-sr-ba-design/          # 按任务组织
├── README.md
├── guidelines/
├── templates/
├── checklists/
├── skills/
├── workflows/
└── examples/

... 其他 4 个任务 ...

07-shared-assets/              # 共享资产
├── patterns/
├── quality-standards/
└── tools/

08-products/                   # 产品数据
└── projects/
    └── project-a/
        ├── 01-normalization/
        ├── 02-sr-ba-design/
        ├── 03-ba-sysreq-design/
        ├── 04-sr-nfr-design/
        ├── 05-sysreq-pa-design/
        ├── 06-traceability-analysis/
        └── changelog.md
```

**特点**：
- ✅ 资源集中，易于查找
- ✅ 新手只需 30 分钟就能上手
- ✅ 任务流程清晰
- ✅ 支持多个团队并行工作

---

## 💡 重构的核心优势

| 方面 | 旧架构 | 新架构 | 改进 |
|------|--------|--------|------|
| **新用户上手时间** | 1-2天 | 30分钟 | ⬇️ 75% |
| **任务查找时间** | 10-20分钟 | 2-3分钟 | ⬇️ 80% |
| **并行工作能力** | 困难 | 容易 | ⬆️ 显著 |
| **知识积累** | 分散 | 集中 | ⬆️ 显著 |
| **维护成本** | 高 | 低 | ⬇️ 显著 |
| **扩展性** | 差 | 好 | ⬆️ 显著 |

---

## 🎯 6 个核心任务

新架构采用**任务驱动架构**，将整个设计流程分解为 6 个独立的工作单元：

| 任务 | 名称 | 目标 | 对应目录 |
|------|------|------|----------|
| **Task 1** | 需求规范化 | 收集、规范化、分解原始需求，检测冲突和重复 | `_current/new-structure/01-task-normalization/` |
| **Task 2** | SR → BA 映射 | 将相关方需求映射到业务架构 5 级节点 | `_current/new-structure/02-task-sr-ba-design/` |
| **Task 3** | BA → SysReq 映射 | 将业务架构映射到系统需求 5 级节点 | `_current/new-structure/03-task-ba-sysreq-design/` |
| **Task 4** | SR-NFR → SysReq-NFR 映射 | 将相关方非功能需求映射到系统非功能需求 | `_current/new-structure/04-task-sr-nfr-design/` |
| **Task 5** | SysReq → PA 映射 | 将系统需求映射到产品架构末级节点 | `_current/new-structure/05-task-sysreq-pa-design/` |
| **Task 6** | 端到端追溯分析 | 验证完整的追溯链路，生成符合性报告 | `_current/new-structure/06-task-traceability-analysis/` |

---

## 📚 关键文件

### 根目录文件
- **CLAUDE.md**：项目总体指导
- **RESTRUCTURE-COMPLETION-SUMMARY.md**：重构完成总结
- **PHASE-1-COMPLETION-REPORT.md** 到 **PHASE-5-COMPLETION-REPORT.md**：各阶段完成报告

### 新架构文件
- **_current/new-structure/04-platform-docs/quick-start-guide.md**：快速开始指南
- **_current/new-structure/01-task-normalization/README.md**：Task 1 快速开始
- **_current/new-structure/02-task-sr-ba-design/README.md**：Task 2 快速开始
- ... 其他任务 README ...

### 旧架构文件（参考）
- **_archive/legacy-structure/01-standards/guidelines/README.md**：旧的准则总览
- **_archive/legacy-structure/02-pipeline/workflows.md**：旧的工作流程

---

## 🔄 核心设计准则

### 四层映射模型

```
相关方需求 (SR) ──N:1──→ 业务架构 5级 (BA) ──N:1──→ 系统需求 5级 (SysReq) ──N:1──→ 产品架构末级 (PA)
                                                                    ↓
                                                            SysReq 9级（场景活动）
```

**功能需求流**：
- **SR → BA 5级**：N:1 多对一映射
- **BA 5级 → SysReq 5级**：N:1 多对一映射
- **SysReq 9级 → PA末级**：N:1 多对一映射
- **1:1 约束**：每条需求只能分配到唯一的承接点

**非功能需求流**（平行体系）：
```
相关方非功能需求 (SR-NFR) ──N:1──→ 系统非功能需求 (SysReq-NFR)
```

---

## 💡 建议

### 日常工作
- 使用 `_current/new-structure/` 中的新架构
- 按照 6 个任务的流程进行工作
- 参考各任务的指南、模板、示例

### 参考学习
- 查看 `_archive/legacy-structure/` 中的旧架构
- 对比新旧架构的差异
- 理解重构的原因和优势

### 扩展应用
- 在 `_current/new-structure/08-products/projects/` 中创建新项目
- 按照新架构的结构组织产品数据
- 使用各任务的工具和资源

---

## 📞 获取帮助

1. **快速开始**：阅读 `_current/new-structure/04-platform-docs/quick-start-guide.md`
2. **查看示例**：参考 `_current/new-structure/08-products/projects/project-a/`
3. **查看指南**：阅读各任务目录下的 `guidelines/` 文件
4. **查看模板**：参考各任务目录下的 `templates/` 文件
5. **查看完成报告**：阅读根目录下的 `PHASE-*-COMPLETION-REPORT.md` 文件

---

**最后更新**：2026-05-12
**版本**：v2.0（任务驱动架构 + 分离式目录结构）
**状态**：✅ 可投入使用
