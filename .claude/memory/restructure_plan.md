---
name: AOS流水线重构方案
description: 按6个任务重构目录结构，每个任务独立自洽
type: project
originSessionId: 5428fac3-4a16-44b1-a563-30eff722c1c0
---
## 重构后的6个任务

1. **Task 1：新增原始需求规范化**
   - 输入：原始需求
   - 输出：规范化的SR（功能）+ SR-NFR（非功能）
   - 占位符：在输出中标记待确认项

2. **Task 2：功能相关方需求设计 + 业务架构初步设计**
   - 输入：规范化的SR（功能）
   - 输出：BA 0-5级完整结构（5级是承接层）
   - 占位符：为BA 5级节点预留下游映射关系

3. **Task 3：业务架构细化 + 系统功能需求架构设计**
   - 输入：BA 5级节点
   - 输出：SysReq 0-9级（功能分支）完整结构
   - 占位符：为SysReq 9级节点预留PA映射关系

4. **Task 4：非功能相关方需求设计 + 系统非功能需求架构设计**
   - 输入：规范化的SR-NFR
   - 输出：SysReq-NFR 0-5级完整结构（直接映射，无中间层）
   - 占位符：为SysReq-NFR 5级节点预留PA权衡关系

5. **Task 5：系统需求设计 + 产品架构设计**
   - 输入：SysReq 0-9级（功能）+ SysReq-NFR 0-5级（非功能）
   - 输出：PA末级节点（前后端组件）+ 非功能权衡决策
   - 占位符：无

6. **Task 6：端到端符合性分析**
   - 输入：所有层级的设计文档
   - 输出：追溯矩阵 + 符合性报告 + 缺陷清单
   - 占位符：无

## 新的目录结构

```
AOS/
├── 00-platform-docs/              # 平台总体文档（不变）
│   ├── quick-start-guide.md
│   ├── project-directory-structure.md
│   └── ...
│
├── 01-task-normalization/         # Task 1：需求规范化
│   ├── guidelines/
│   │   └── guideline-normalization.md
│   ├── templates/
│   │   ├── sr-template.md
│   │   └── sr-nfr-template.md
│   ├── checklists/
│   │   └── normalization-checklist.md
│   ├── skills/
│   │   ├── requirement-normalization.md
│   │   ├── requirement-decomposition.md
│   │   ├── conflict-detection.md
│   │   └── duplicate-detection.md
│   ├── workflows/
│   │   └── task-1-workflow.md
│   ├── examples/
│   │   └── normalization-example.md
│   └── README.md
│
├── 02-task-sr-ba-design/          # Task 2：SR → BA映射 + BA初步设计
│   ├── guidelines/
│   │   └── guideline-sr-to-ba-mapping.md
│   ├── templates/
│   │   └── ba-template.md
│   ├── checklists/
│   │   └── sr-to-ba-checklist.md
│   ├── skills/
│   │   ├── business-pattern-matching.md
│   │   └── sr-to-ba-mapping.md
│   ├── workflows/
│   │   └── task-2-workflow.md
│   ├── examples/
│   │   └── sr-to-ba-example.md
│   └── README.md
│
├── 03-task-ba-sysreq-design/      # Task 3：BA → SysReq映射 + SysReq设计
│   ├── guidelines/
│   │   └── guideline-ba-to-sysreq-mapping.md
│   ├── templates/
│   │   └── sysreq-template.md
│   ├── checklists/
│   │   └── ba-to-sysreq-checklist.md
│   ├── skills/
│   │   ├── architecture-pattern-matching.md
│   │   └── ba-to-sysreq-mapping.md
│   ├── workflows/
│   │   └── task-3-workflow.md
│   ├── examples/
│   │   └── ba-to-sysreq-example.md
│   └── README.md
│
├── 04-task-sr-nfr-design/         # Task 4：SR-NFR → SysReq-NFR映射
│   ├── guidelines/
│   │   └── guideline-sr-nfr-to-sysreq-nfr.md
│   ├── templates/
│   │   └── sysreq-nfr-template.md
│   ├── checklists/
│   │   └── sr-nfr-design-checklist.md
│   ├── skills/
│   │   └── sr-nfr-to-sysreq-nfr-mapping.md
│   ├── workflows/
│   │   └── task-4-workflow.md
│   ├── examples/
│   │   └── sr-nfr-design-example.md
│   └── README.md
│
├── 05-task-sysreq-pa-design/      # Task 5：SysReq → PA映射 + PA设计
│   ├── guidelines/
│   │   └── guideline-sysreq-to-pa-mapping.md
│   ├── templates/
│   │   └── pa-template.md
│   ├── checklists/
│   │   ├── sysreq-to-pa-checklist.md
│   │   └── nfr-tradeoff-checklist.md
│   ├── skills/
│   │   └── sysreq-to-pa-mapping.md
│   ├── workflows/
│   │   └── task-5-workflow.md
│   ├── examples/
│   │   └── sysreq-to-pa-example.md
│   └── README.md
│
├── 06-task-traceability-analysis/  # Task 6：端到端符合性分析
│   ├── guidelines/
│   │   └── guideline-traceability-analysis.md
│   ├── templates/
│   │   ├── traceability-matrix-template.md
│   │   └── compliance-report-template.md
│   ├── checklists/
│   │   └── traceability-checklist.md
│   ├── skills/
│   │   └── traceability-analysis.md
│   ├── workflows/
│   │   └── task-6-workflow.md
│   ├── examples/
│   │   └── traceability-example.md
│   └── README.md
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
└── 08-products/                   # 产品数据（按项目组织）
    └── projects/
        └── <project-name>/
            ├── 01-normalization/
            │   ├── raw-requirements.md
            │   ├── sr-functional.md
            │   └── sr-nfr.md
            ├── 02-sr-ba-design/
            │   ├── ba-design.md
            │   └── sr-to-ba-mapping.md
            ├── 03-ba-sysreq-design/
            │   ├── sysreq-functional.md
            │   └── ba-to-sysreq-mapping.md
            ├── 04-sr-nfr-design/
            │   ├── sysreq-nfr.md
            │   └── sr-nfr-to-sysreq-nfr-mapping.md
            ├── 05-sysreq-pa-design/
            │   ├── pa-design.md
            │   ├── sysreq-to-pa-mapping.md
            │   └── nfr-tradeoff-decisions.md
            ├── 06-traceability-analysis/
            │   ├── traceability-matrix.md
            │   ├── compliance-report.md
            │   └── defect-list.md
            └── changelog.md
```

## 目录结构的优势

✅ **任务独立性**：每个任务目录包含完整的指南、模板、检查清单、Skill、工作流和示例
✅ **易于导航**：新用户可以快速找到特定任务的所有资源
✅ **并行工作**：多个团队可以同时在不同任务上工作，互不干扰
✅ **版本管理**：每个任务的资产可以独立版本化和更新
✅ **知识积累**：每个任务的示例和最佳实践集中在一个地方
✅ **产品数据对齐**：产品数据目录结构与任务流程完全对应

## 迁移策略

1. **第一步**：创建新的目录结构框架
2. **第二步**：逐个任务迁移现有资产
3. **第三步**：补充缺失的资产（特别是Task 4和Task 5）
4. **第四步**：更新所有交叉引用和导航链接
5. **第五步**：更新CLAUDE.md和快速开始指南
