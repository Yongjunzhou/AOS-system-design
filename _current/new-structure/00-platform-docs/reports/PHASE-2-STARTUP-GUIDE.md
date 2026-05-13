# 📋 第二阶段启动指南 - 资产迁移

**阶段**：第二阶段 - 资产迁移
**预计日期**：2026-05-14 ~ 2026-05-17
**预计耗时**：3-5天（可并行处理）
**状态**：⏳ 准备启动

---

## 🎯 第二阶段目标

将现有的资产（guidelines、templates、checklists、skills、workflows）迁移到新的任务目录结构中，并创建新的资产（特别是Task 4和Task 6）。

---

## 📊 资产迁移清单

### Task 1：需求规范化

**来源**：`01-standards/guidelines/guideline-1-normalization.md` 等

**迁移任务**：
- [ ] 迁移 `guideline-normalization.md` → `01-normalization/guidelines/`
- [ ] 迁移 `sr-template.md` → `01-normalization/templates/`
- [ ] 迁移 `sr-nfr-template.md` → `01-normalization/templates/`
- [ ] 迁移 `normalization-checklist.md` → `01-normalization/checklists/`
- [ ] 迁移 `requirement-normalization.md` → `01-normalization/skills/`
- [ ] 迁移 `requirement-decomposition.md` → `01-normalization/skills/`
- [ ] 迁移 `conflict-detection.md` → `01-normalization/skills/`
- [ ] 迁移 `duplicate-detection.md` → `01-normalization/skills/`
- [ ] 迁移 `task-1-workflow.md` → `01-normalization/workflows/`
- [ ] 创建 `normalization-example.md` → `01-normalization/examples/`

**预计耗时**：1天

---

### Task 2：SR → BA映射

**来源**：`01-standards/guidelines/guideline-2-sr-to-ba-mapping.md` 等

**迁移任务**：
- [ ] 迁移 `guideline-sr-to-ba-mapping.md` → `02-sr-ba-design/guidelines/`
- [ ] 迁移 `ba-template.md` → `02-sr-ba-design/templates/`
- [ ] 迁移 `sr-to-ba-checklist.md` → `02-sr-ba-design/checklists/`
- [ ] 迁移 `business-pattern-matching.md` → `02-sr-ba-design/skills/`
- [ ] 迁移 `sr-to-ba-mapping.md` → `02-sr-ba-design/skills/`
- [ ] 迁移 `task-2-workflow.md` → `02-sr-ba-design/workflows/`
- [ ] 创建 `sr-to-ba-example.md` → `02-sr-ba-design/examples/`

**预计耗时**：1天

---

### Task 3：BA → SysReq映射

**来源**：`01-standards/guidelines/guideline-3-ba-to-sr-mapping.md` 等

**迁移任务**：
- [ ] 迁移 `guideline-ba-to-sysreq-mapping.md` → `03-ba-sysreq-design/guidelines/`
- [ ] 迁移 `sysreq-template.md` → `03-ba-sysreq-design/templates/`
- [ ] 迁移 `ba-to-sysreq-checklist.md` → `03-ba-sysreq-design/checklists/`
- [ ] 迁移 `architecture-pattern-matching.md` → `03-ba-sysreq-design/skills/`
- [ ] 迁移 `ba-to-sysreq-mapping.md` → `03-ba-sysreq-design/skills/`
- [ ] 迁移 `task-3-workflow.md` → `03-ba-sysreq-design/workflows/`
- [ ] 创建 `ba-to-sysreq-example.md` → `03-ba-sysreq-design/examples/`

**预计耗时**：1天

---

### Task 4：SR-NFR → SysReq-NFR映射（新增）

**来源**：无（需要创建）

**创建任务**：
- [ ] 创建 `guideline-sr-nfr-to-sysreq-nfr.md` → `04-sr-nfr-design/guidelines/`
- [ ] 创建 `sysreq-nfr-template.md` → `04-sr-nfr-design/templates/`
- [ ] 创建 `sr-nfr-design-checklist.md` → `04-sr-nfr-design/checklists/`
- [ ] 创建 `sr-nfr-to-sysreq-nfr-mapping.md` → `04-sr-nfr-design/skills/`
- [ ] 创建 `task-4-workflow.md` → `04-sr-nfr-design/workflows/`
- [ ] 创建 `sr-nfr-design-example.md` → `04-sr-nfr-design/examples/`

**参考资料**：
- `04-sr-nfr-design/README.md` — 任务定义
- `RESTRUCTURE-PLAN.md` — 详细的任务定义

**预计耗时**：1.5天

---

### Task 5：SysReq → PA映射

**来源**：`01-standards/guidelines/guideline-4-sr-to-pa-mapping.md` 等

**迁移和创建任务**：
- [ ] 迁移 `guideline-sysreq-to-pa-mapping.md` → `05-sysreq-pa-design/guidelines/`
- [ ] 迁移 `pa-template.md` → `05-sysreq-pa-design/templates/`
- [ ] 迁移 `sysreq-to-pa-checklist.md` → `05-sysreq-pa-design/checklists/`
- [ ] 创建 `nfr-tradeoff-checklist.md` → `05-sysreq-pa-design/checklists/`
- [ ] 迁移 `sysreq-to-pa-mapping.md` → `05-sysreq-pa-design/skills/`
- [ ] 迁移 `task-5-workflow.md` → `05-sysreq-pa-design/workflows/`
- [ ] 创建 `sysreq-to-pa-example.md` → `05-sysreq-pa-design/examples/`

**预计耗时**：1.5天

---

### Task 6：端到端符合性分析（新增）

**来源**：无（需要创建）

**创建任务**：
- [ ] 创建 `guideline-traceability-analysis.md` → `06-traceability-analysis/guidelines/`
- [ ] 创建 `traceability-matrix-template.md` → `06-traceability-analysis/templates/`
- [ ] 创建 `compliance-report-template.md` → `06-traceability-analysis/templates/`
- [ ] 创建 `traceability-checklist.md` → `06-traceability-analysis/checklists/`
- [ ] 创建 `traceability-analysis.md` → `06-traceability-analysis/skills/`
- [ ] 创建 `task-6-workflow.md` → `06-traceability-analysis/workflows/`
- [ ] 创建 `traceability-example.md` → `06-traceability-analysis/examples/`

**参考资料**：
- `06-traceability-analysis/README.md` — 任务定义
- `RESTRUCTURE-PLAN.md` — 详细的任务定义

**预计耗时**：1.5天

---

### 共享资产迁移

**来源**：`01-standards/patterns/`、`01-standards/templates/` 等

**迁移任务**：
- [ ] 迁移 `business-patterns.md` → `07-shared-assets/patterns/`
- [ ] 创建 `architecture-patterns.md` → `07-shared-assets/patterns/`
- [ ] 迁移 `quality-checklist.md` → `07-shared-assets/quality-standards/`
- [ ] 迁移 `design-decision-template.md` → `07-shared-assets/quality-standards/`
- [ ] 迁移 `validate.py` → `07-shared-assets/tools/`
- [ ] 迁移 `generate-report.py` → `07-shared-assets/tools/`

**预计耗时**：0.5天

---

## 🔄 迁移步骤

### 步骤1：准备工作
1. 确认所有源文件位置
2. 确认迁移目标位置
3. 备份原有文件（可选）

### 步骤2：迁移现有资产
1. 复制文件到新位置
2. 更新文件中的相对路径和链接
3. 验证文件内容完整性

### 步骤3：创建新资产
1. 根据README.md中的任务定义创建新文件
2. 参考现有资产的格式和结构
3. 确保内容完整和准确

### 步骤4：验证和提交
1. 验证所有文件都已迁移
2. 验证所有链接都正确
3. 提交git commit

---

## 📝 迁移模板

### 迁移现有文件的步骤

```bash
# 1. 复制文件
cp 01-standards/guidelines/guideline-1-normalization.md 01-normalization/guidelines/guideline-normalization.md

# 2. 更新文件中的相对路径（如果有）
# 例如：../patterns/ → ../../07-shared-assets/patterns/

# 3. 验证文件
cat 01-normalization/guidelines/guideline-normalization.md

# 4. 提交
git add 01-normalization/guidelines/guideline-normalization.md
git commit -m "feat: 迁移guideline-normalization.md到Task 1"
```

### 创建新文件的步骤

```bash
# 1. 创建文件（参考README.md中的任务定义）
cat > 04-sr-nfr-design/guidelines/guideline-sr-nfr-to-sysreq-nfr.md << 'EOF'
# 非功能相关方需求设计指南

## 概述
...

## 关键活动
...

## 最佳实践
...
EOF

# 2. 验证文件
cat 04-sr-nfr-design/guidelines/guideline-sr-nfr-to-sysreq-nfr.md

# 3. 提交
git add 04-sr-nfr-design/guidelines/guideline-sr-nfr-to-sysreq-nfr.md
git commit -m "feat: 创建非功能相关方需求设计指南"
```

---

## 🎯 并行工作建议

由于资产迁移可以并行进行，建议分工如下：

**方案A：按任务分工（推荐）**
- 人员1：Task 1 + Task 2
- 人员2：Task 3 + Task 4
- 人员3：Task 5 + Task 6 + 共享资产

**方案B：按资产类型分工**
- 人员1：所有guidelines
- 人员2：所有templates
- 人员3：所有checklists + skills
- 人员4：所有workflows + examples

**方案C：集中式**
- 1人负责所有资产迁移

---

## 📋 每日检查清单

### 第一天（2026-05-14）
- [ ] Task 1资产迁移完成
- [ ] Task 2资产迁移完成
- [ ] git commit已提交

### 第二天（2026-05-15）
- [ ] Task 3资产迁移完成
- [ ] Task 4资产创建完成
- [ ] git commit已提交

### 第三天（2026-05-16）
- [ ] Task 5资产迁移和补充完成
- [ ] Task 6资产创建完成
- [ ] git commit已提交

### 第四天（2026-05-17）
- [ ] 共享资产迁移完成
- [ ] 所有链接验证完成
- [ ] 最终git commit已提交

---

## ✅ 第二阶段完成标准

第二阶段完成时，应该满足以下条件：

- [ ] 所有Task 1-3的现有资产都已迁移
- [ ] 所有Task 4和Task 6的新资产都已创建
- [ ] 所有Task 5的资产都已迁移和补充
- [ ] 所有共享资产都已迁移
- [ ] 所有文件中的相对路径都已更新
- [ ] 所有链接都已验证
- [ ] 所有git commit都已提交
- [ ] 原有文档已保留

---

## 📞 需要帮助？

如果在迁移过程中遇到问题：

1. **查看参考资料**
   - 查看对应任务的README.md
   - 查看RESTRUCTURE-PLAN.md中的任务定义

2. **查看示例**
   - 查看现有资产的格式和结构
   - 参考类似的资产进行创建

3. **联系项目经理**
   - 报告遇到的问题
   - 请求帮助或指导

---

## 🚀 准备好开始了吗？

第二阶段是重构的关键阶段。完成这个阶段后，新的架构就基本成形了。

**让我们开始吧！** 🎉

---

**第二阶段预计开始**：2026-05-14
**第二阶段预计完成**：2026-05-17
**总体进度**：20% → 60%（完成第一、二阶段）
