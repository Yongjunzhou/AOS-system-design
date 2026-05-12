# ✅ AOS 流水线重构方案 - 完整设计

## 📋 执行摘要

基于你的4个关键确认，我已经为AOS平台设计了一个**完整的流水线重构方案**。这个方案将AOS从"资产类型驱动"重构为"任务驱动"，使每个任务都是相对独立的工作单元。

**重构周期**：约10天（5个阶段）
**预计完成日期**：2026-05-21

---

## 🎯 重构核心

### 从这样...

```
01-standards/          ← 准则、模板、检查清单
02-pipeline/           ← Skill、工具、工作流
03-products/           ← 产品数据
04-platform-docs/      ← 平台文档

问题：前后交联多，新用户难以快速上手
```

### ...到这样

```
01-task-normalization/         ← Task 1：需求规范化
02-task-sr-ba-design/          ← Task 2：SR → BA映射
03-task-ba-sysreq-design/      ← Task 3：BA → SysReq映射
04-task-sr-nfr-design/         ← Task 4：SR-NFR → SysReq-NFR映射
05-task-sysreq-pa-design/      ← Task 5：SysReq → PA映射
06-task-traceability-analysis/ ← Task 6：端到端符合性分析
07-shared-assets/              ← 跨任务共享资产
08-products/                   ← 产品数据（按任务组织）

优势：每个任务自洽，新用户可快速找到需要的资源
```

---

## 🔄 6个核心任务

### Task 1：新增原始需求规范化
- **输入**：原始需求
- **输出**：规范化的SR（功能）+ SR-NFR（非功能）
- **关键活动**：规范化、分解、冲突检测、重复检测
- **目录**：`01-task-normalization/`

### Task 2：功能相关方需求设计 + 业务架构初步设计
- **输入**：SR（功能）
- **输出**：BA 0-5级完整结构
- **映射关系**：SR → BA（N:1）
- **目录**：`02-task-sr-ba-design/`

### Task 3：业务架构细化 + 系统功能需求架构设计
- **输入**：BA 5级节点
- **输出**：SysReq 0-9级（功能分支）
- **映射关系**：BA → SysReq（N:1）
- **目录**：`03-task-ba-sysreq-design/`

### Task 4：非功能相关方需求设计 + 系统非功能需求架构设计
- **输入**：SR-NFR
- **输出**：SysReq-NFR 0-5级
- **映射关系**：SR-NFR → SysReq-NFR（N:1，无中间层）✅
- **目录**：`04-task-sr-nfr-design/`

### Task 5：系统需求设计 + 产品架构设计
- **输入**：SysReq（功能）+ SysReq-NFR（非功能）
- **输出**：PA末级（前后端组件）✅ + 非功能权衡决策
- **映射关系**：SysReq → PA（N:1）
- **目录**：`05-task-sysreq-pa-design/`

### Task 6：端到端符合性分析
- **输入**：所有设计文档
- **输出**：追溯矩阵 + 符合性报告 + 缺陷清单
- **关键活动**：追溯分析、符合性检查、缺陷识别
- **目录**：`06-task-traceability-analysis/`

---

## 📁 新的目录结构

```
AOS/
├── 00-platform-docs/              # 平台总体文档
│
├── 01-task-normalization/         # Task 1
│   ├── README.md                  # 任务概述
│   ├── guidelines/                # 指南
│   ├── templates/                 # 模板
│   ├── checklists/                # 检查清单
│   ├── skills/                    # AI Skill定义
│   ├── workflows/                 # 工作流
│   └── examples/                  # 示例
│
├── 02-task-sr-ba-design/          # Task 2
├── 03-task-ba-sysreq-design/      # Task 3
├── 04-task-sr-nfr-design/         # Task 4
├── 05-task-sysreq-pa-design/      # Task 5
├── 06-task-traceability-analysis/ # Task 6
│
├── 07-shared-assets/              # 跨任务共享资产
│   ├── patterns/
│   │   ├── business-patterns.md
│   │   └── architecture-patterns.md
│   ├── quality-standards/
│   │   ├── quality-checklist.md
│   │   └── design-decision-template.md
│   └── tools/
│       ├── validate.py
│       └── generate-report.py
│
└── 08-products/                   # 产品数据
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

---

## ✅ 关键确认的实现

### 1️⃣ 非功能需求直接映射（无中间层）

```
SR-NFR
  ↓ [N:1映射]
SysReq-NFR 5级
  ↓ [权衡决策]
PA非功能权衡

✅ 在Task 4中实现
✅ 不经过业务架构层
✅ 在Task 5中进行权衡决策
```

### 2️⃣ 产品架构末级 = 前后端组件

```
前端组件：页面、功能模块、UI组件、前端服务
后端组件：API端点、业务服务、数据访问层、第三方集成

✅ 在Task 5中定义
✅ 是可以独立开发、测试、部署的最小单位
```

### 3️⃣ 占位符在各任务阶段直接完成

```
Task 2：为BA 5级节点预留下游映射关系
Task 3：为SysReq 9级节点预留PA映射关系
Task 4：为SysReq-NFR 5级节点预留PA权衡关系

✅ 支持两阶段工作流程
✅ 不需要单独的占位符创建阶段
```

### 4️⃣ Task 5和6合并

```
Task 5：系统需求设计 + 产品架构设计
  - 功能需求 → PA末级
  - 非功能需求 → PA权衡决策
  - 统一处理，确保协调

✅ 功能和非功能在同一个任务中处理
✅ 便于进行权衡决策
```

---

## 📊 映射关系总览

| 映射 | 关系 | 任务 | 说明 |
|------|------|------|------|
| SR → BA 5级 | N:1 | Task 2 | 多条需求可映射到一个业务组件 |
| BA 5级 → SysReq 5级 | N:1 | Task 3 | 一个业务组件可在多个业务上应用 |
| SysReq 9级 → PA末级 | N:1 | Task 5 | 多个场景活动可映射到一个组件 |
| SR-NFR → SysReq-NFR 5级 | N:1 | Task 4 | 多条非功能需求可映射到一个承接层 |

---

## 🚀 迁移计划（5个阶段）

### 第一阶段：框架搭建（1-2天）
- 创建所有目录结构
- 创建所有README.md文件
- ✅ **已完成**：6个任务的README已创建

### 第二阶段：资产迁移（3-5天）
- 迁移现有的guidelines、templates、checklists、skills、workflows
- 创建新的资产（特别是Task 4和Task 5）
- 创建示例文件

### 第三阶段：产品数据迁移（2-3天）
- 按照新的目录结构组织产品数据
- 更新所有产品数据文件的路径

### 第四阶段：文档更新（2-3天）
- 更新CLAUDE.md
- 更新快速开始指南
- 更新所有交叉引用

### 第五阶段：验证和优化（1-2天）
- 验证所有链接
- 测试所有工作流
- 收集反馈

**总耗时**：约10天

---

## 📚 已创建的文档

### 在项目根目录

✅ `RESTRUCTURE-PLAN.md` — 详细的重构计划
✅ `NAVIGATION-GUIDE.md` — 导航指南
✅ `MIGRATION-CHECKLIST.md` — 迁移检查清单

### 在任务目录

✅ `01-task-normalization/README.md`
✅ `02-task-sr-ba-design/README.md`
✅ `03-task-ba-sysreq-design/README.md`
✅ `04-task-sr-nfr-design/README.md`
✅ `05-task-sysreq-pa-design/README.md`
✅ `06-task-traceability-analysis/README.md`

### 在memory目录

✅ `restructure_summary.md` — 完整的重构方案总结
✅ `restructure_plan.md` — 详细的重构计划

---

## 🎓 使用指南

### 对于新用户

1. 阅读 `NAVIGATION-GUIDE.md`（10分钟）
2. 选择你要参与的任务
3. 进入对应的任务目录，阅读README.md（5分钟）
4. 阅读任务的guidelines/（10-20分钟）
5. 查看任务的examples/（10分钟）
6. 开始工作

### 对于项目经理

1. 阅读 `NAVIGATION-GUIDE.md`
2. 了解6个核心任务的流程
3. 查看产品数据目录
4. 使用工具生成报告

### 对于设计师

1. 进入对应的任务目录
2. 阅读README.md和guidelines/
3. 查看templates/和examples/
4. 使用checklists/进行检查

---

## 💡 重构的优势

| 方面 | 当前 | 重构后 |
|------|------|--------|
| **新用户上手时间** | 1-2天 | 30分钟 |
| **任务查找时间** | 10-20分钟 | 2-3分钟 |
| **并行工作能力** | 困难 | 容易 |
| **知识积累** | 分散 | 集中 |
| **维护成本** | 高 | 低 |
| **扩展性** | 差 | 好 |

---

## 🔗 关键文档链接

| 文档 | 位置 | 用途 |
|------|------|------|
| **导航指南** | `NAVIGATION-GUIDE.md` | 了解整个重构方案 |
| **重构计划** | `RESTRUCTURE-PLAN.md` | 了解详细的重构计划 |
| **迁移检查清单** | `MIGRATION-CHECKLIST.md` | 跟踪迁移进度 |
| **Task 1 README** | `01-task-normalization/README.md` | Task 1快速开始 |
| **Task 2 README** | `02-task-sr-ba-design/README.md` | Task 2快速开始 |
| **Task 3 README** | `03-task-ba-sysreq-design/README.md` | Task 3快速开始 |
| **Task 4 README** | `04-task-sr-nfr-design/README.md` | Task 4快速开始 |
| **Task 5 README** | `05-task-sysreq-pa-design/README.md` | Task 5快速开始 |
| **Task 6 README** | `06-task-traceability-analysis/README.md` | Task 6快速开始 |

---

## ✨ 下一步行动

### 立即行动

1. **审核方案**
   - [ ] 阅读本文档
   - [ ] 阅读 `NAVIGATION-GUIDE.md`
   - [ ] 阅读 `RESTRUCTURE-PLAN.md`

2. **确认无误**
   - [ ] 确认6个任务的定义
   - [ ] 确认新的目录结构
   - [ ] 确认迁移计划

3. **批准开始**
   - [ ] 批准开始迁移
   - [ ] 分配迁移团队
   - [ ] 设定完成日期

### 迁移阶段

1. **按照 `MIGRATION-CHECKLIST.md` 进行迁移**
2. **定期更新迁移进度**
3. **收集团队反馈**

### 迁移完成后

1. **验证所有功能正常**
2. **收集用户反馈**
3. **进行微调和优化**
4. **删除旧目录**（如果确认不再需要）

---

## 📞 问题和建议

如果你有任何问题或建议，请：

1. 查看对应任务的README.md中的"常见问题"
2. 查看对应任务的guidelines/
3. 查看对应任务的examples/
4. 联系我进行讨论

---

**重构方案版本**：v1.0
**创建日期**：2026-05-12
**预计完成日期**：2026-05-21

**状态**：✅ 方案设计完成，等待批准开始迁移
