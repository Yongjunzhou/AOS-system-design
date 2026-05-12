# AOS 流水线重构导航指南

## 📋 重构概览

AOS平台已从"资产类型驱动"（standards/pipeline/products）重构为"任务驱动"（01-task-*/08-products），使每个任务都是相对独立的工作单元。

## 🎯 6个核心任务

```
Task 1: 新增原始需求规范化
   ↓
Task 2: 功能相关方需求设计 + 业务架构初步设计
   ↓
Task 3: 业务架构细化 + 系统功能需求架构设计
   ↓
Task 5: 系统需求设计 + 产品架构设计
   ↑
Task 4: 非功能相关方需求设计 + 系统非功能需求架构设计
   ↓
Task 6: 端到端符合性分析
```

## 📁 新的目录结构

```
AOS/
├── 00-platform-docs/              # 平台总体文档
│   ├── quick-start-guide.md       # 5分钟快速开始
│   ├── project-directory-structure.md
│   └── ...
│
├── 01-task-normalization/         # Task 1：需求规范化
├── 02-task-sr-ba-design/          # Task 2：SR → BA映射
├── 03-task-ba-sysreq-design/      # Task 3：BA → SysReq映射
├── 04-task-sr-nfr-design/         # Task 4：SR-NFR → SysReq-NFR映射
├── 05-task-sysreq-pa-design/      # Task 5：SysReq → PA映射
├── 06-task-traceability-analysis/  # Task 6：端到端符合性分析
│
├── 07-shared-assets/              # 跨任务共享资产
│   ├── patterns/
│   ├── quality-standards/
│   └── tools/
│
└── 08-products/                   # 产品数据（按项目组织）
    └── projects/
        └── <project-name>/
            ├── 01-normalization/
            ├── 02-sr-ba-design/
            ├── 03-ba-sysreq-design/
            ├── 04-sr-nfr-design/
            ├── 05-sysreq-pa-design/
            ├── 06-traceability-analysis/
            └── changelog.md
```

## 🚀 快速开始

### 对于新用户

1. 阅读 [00-platform-docs/quick-start-guide.md](00-platform-docs/quick-start-guide.md)（5分钟）
2. 选择你要参与的任务
3. 进入对应的任务目录，阅读README.md

### 对于项目经理

1. 了解 [6个核心任务](#6个核心任务) 的流程
2. 查看 [08-products/projects/](08-products/projects/) 下的项目数据
3. 使用 [07-shared-assets/tools/](07-shared-assets/tools/) 中的工具生成报告

### 对于设计师

1. 进入对应的任务目录（例如 [02-task-sr-ba-design/](02-task-sr-ba-design/)）
2. 阅读 `guidelines/` 中的指南
3. 查看 `templates/` 中的模板
4. 参考 `examples/` 中的示例
5. 使用 `checklists/` 中的检查清单

## 📚 每个任务的结构

每个任务目录（01-task-* 到 06-task-*）都包含：

```
XX-task-name/
├── README.md                      # 任务概述和快速开始
├── guidelines/                    # 该任务的指南
│   └── guideline-*.md
├── templates/                     # 该任务的输出模板
│   └── *-template.md
├── checklists/                    # 该任务的检查清单
│   └── *-checklist.md
├── skills/                        # 该任务的AI Skill定义
│   └── *.md
├── workflows/                     # 该任务的工作流
│   └── task-*-workflow.md
└── examples/                      # 该任务的示例
    └── *-example.md
```

## 🔗 任务之间的关系

### 功能需求流

```
Task 1: SR（功能）
   ↓
Task 2: BA 0-5级
   ↓
Task 3: SysReq 0-9级（功能分支）
   ↓
Task 5: PA末级（前后端组件）
```

### 非功能需求流（平行体系）

```
Task 1: SR-NFR
   ↓
Task 4: SysReq-NFR 0-5级
   ↓
Task 5: PA非功能权衡
```

### 符合性分析

```
Task 6: 端到端追溯 + 符合性检查
```

## 📊 映射关系

| 映射 | 关系 | 任务 |
|------|------|------|
| SR → BA 5级 | N:1 | Task 2 |
| BA 5级 → SysReq 5级 | N:1 | Task 3 |
| SysReq 9级 → PA末级 | N:1 | Task 5 |
| SR-NFR → SysReq-NFR 5级 | N:1 | Task 4 |

## 🛠️ 共享资产

### 07-shared-assets/patterns/

- `business-patterns.md`：业务模式库（10+个常见模式）
- `architecture-patterns.md`：架构模式库

### 07-shared-assets/quality-standards/

- `quality-checklist.md`：质量检查清单
- `design-decision-template.md`：设计决策模板

### 07-shared-assets/tools/

- `validate.py`：验证项目映射关系
- `generate-report.py`：生成追溯矩阵报告

## 📖 关键文档

| 文档 | 位置 | 用途 |
|------|------|------|
| 快速开始指南 | [00-platform-docs/quick-start-guide.md](00-platform-docs/quick-start-guide.md) | 新用户5分钟快速了解 |
| 重构计划 | [RESTRUCTURE-PLAN.md](RESTRUCTURE-PLAN.md) | 了解重构的详细计划 |
| 项目指南 | [CLAUDE.md](CLAUDE.md) | 项目总体指导 |

## 🔄 工作流程

### 新增项目的12步工作流

1. **Task 1**：收集原始需求 → 规范化 → 生成SR和SR-NFR
2. **Task 2**：SR → BA映射 → 生成BA 0-5级
3. **Task 3**：BA → SysReq映射 → 生成SysReq 0-9级（功能）
4. **Task 4**：SR-NFR → SysReq-NFR映射 → 生成SysReq-NFR 0-5级
5. **Task 5**：SysReq → PA映射 + 非功能权衡 → 生成PA末级
6. **Task 6**：端到端追溯 + 符合性检查 → 生成报告

### 两阶段工作流程

**第一阶段：占位符创建（快速，1-2小时）**
- 在各任务中快速创建占位符
- 建立上下游映射关系
- 冻结占位符结构

**第二阶段：具体设计（深入，2-6天）**
- 填充占位符的具体内容
- 完成详细设计
- 验证设计完整性

## ✅ 检查清单

### 项目启动前

- [ ] 阅读 [CLAUDE.md](CLAUDE.md)
- [ ] 阅读 [00-platform-docs/quick-start-guide.md](00-platform-docs/quick-start-guide.md)
- [ ] 了解 [6个核心任务](#6个核心任务)
- [ ] 了解 [新的目录结构](#新的目录结构)

### 每个任务完成前

- [ ] 阅读任务的README.md
- [ ] 阅读任务的guidelines/
- [ ] 查看任务的templates/
- [ ] 参考任务的examples/
- [ ] 使用任务的checklists/进行检查
- [ ] 更新产品数据目录中的文件
- [ ] 更新changelog.md

## 🤝 协作建议

### 并行工作

由于任务之间的相对独立性，可以进行以下并行工作：
- Task 2和Task 4可以并行进行（功能和非功能需求设计）
- Task 3和Task 4可以并行进行（功能和非功能需求架构设计）
- Task 5可以在Task 3和Task 4完成后进行

### 团队分工

- **需求团队**：负责Task 1
- **业务架构团队**：负责Task 2和Task 3
- **系统架构团队**：负责Task 4和Task 5
- **质量团队**：负责Task 6

## 📞 获取帮助

- **快速问题**：查看对应任务的README.md中的"常见问题"
- **详细指南**：查看对应任务的guidelines/
- **示例参考**：查看对应任务的examples/
- **工具支持**：使用07-shared-assets/tools/中的工具

## 📝 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-05-12 | 初始版本 |

---

**下一步**：选择你要参与的任务，进入对应的任务目录开始工作！
