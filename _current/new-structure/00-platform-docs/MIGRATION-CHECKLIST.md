# AOS 流水线重构迁移检查清单

## 📋 重构阶段

### 第一阶段：框架搭建（1-2天）

#### 目录结构创建
- [ ] 创建 `01-normalization/` 目录
- [ ] 创建 `02-sr-ba-design/` 目录
- [ ] 创建 `03-ba-sysreq-design/` 目录
- [ ] 创建 `04-sr-nfr-design/` 目录
- [ ] 创建 `05-sysreq-pa-design/` 目录
- [ ] 创建 `06-traceability-analysis/` 目录
- [ ] 创建 `07-shared-assets/` 目录
- [ ] 创建 `08-products/` 目录

#### 每个任务目录的子目录
对于每个任务目录（01-task-* 到 06-task-*），创建：
- [ ] `guidelines/` 目录
- [ ] `templates/` 目录
- [ ] `checklists/` 目录
- [ ] `skills/` 目录
- [ ] `workflows/` 目录
- [ ] `examples/` 目录

#### 共享资产目录
- [ ] `07-shared-assets/patterns/` 目录
- [ ] `07-shared-assets/quality-standards/` 目录
- [ ] `07-shared-assets/tools/` 目录

#### README文件创建
- [ ] `01-normalization/README.md`
- [ ] `02-sr-ba-design/README.md`
- [ ] `03-ba-sysreq-design/README.md`
- [ ] `04-sr-nfr-design/README.md`
- [ ] `05-sysreq-pa-design/README.md`
- [ ] `06-traceability-analysis/README.md`

---

### 第二阶段：资产迁移（3-5天）

#### Task 1：需求规范化
- [ ] 迁移 `guideline-normalization.md`
- [ ] 迁移 `sr-template.md` 和 `sr-nfr-template.md`
- [ ] 迁移 `normalization-checklist.md`
- [ ] 迁移 Skill：`requirement-normalization.md`
- [ ] 迁移 Skill：`requirement-decomposition.md`
- [ ] 迁移 Skill：`conflict-detection.md`
- [ ] 迁移 Skill：`duplicate-detection.md`
- [ ] 迁移 `task-1-workflow.md`
- [ ] 创建 `normalization-example.md`

#### Task 2：SR → BA映射
- [ ] 迁移 `guideline-sr-to-ba-mapping.md`
- [ ] 迁移 `ba-template.md`
- [ ] 迁移 `sr-to-ba-checklist.md`
- [ ] 迁移 Skill：`business-pattern-matching.md`
- [ ] 迁移 Skill：`sr-to-ba-mapping.md`
- [ ] 迁移 `task-2-workflow.md`
- [ ] 创建 `sr-to-ba-example.md`

#### Task 3：BA → SysReq映射
- [ ] 迁移 `guideline-ba-to-sysreq-mapping.md`
- [ ] 迁移 `sysreq-template.md`
- [ ] 迁移 `ba-to-sysreq-checklist.md`
- [ ] 迁移 Skill：`architecture-pattern-matching.md`
- [ ] 迁移 Skill：`ba-to-sysreq-mapping.md`
- [ ] 迁移 `task-3-workflow.md`
- [ ] 创建 `ba-to-sysreq-example.md`

#### Task 4：SR-NFR → SysReq-NFR映射（新增）
- [ ] 创建 `guideline-sr-nfr-to-sysreq-nfr.md`
- [ ] 创建 `sysreq-nfr-template.md`
- [ ] 创建 `sr-nfr-design-checklist.md`
- [ ] 创建 Skill：`sr-nfr-to-sysreq-nfr-mapping.md`
- [ ] 创建 `task-4-workflow.md`
- [ ] 创建 `sr-nfr-design-example.md`

#### Task 5：SysReq → PA映射
- [ ] 迁移 `guideline-sysreq-to-pa-mapping.md`
- [ ] 迁移 `pa-template.md`
- [ ] 迁移 `sysreq-to-pa-checklist.md`
- [ ] 创建 `nfr-tradeoff-checklist.md`
- [ ] 迁移 Skill：`sysreq-to-pa-mapping.md`
- [ ] 迁移 `task-5-workflow.md`
- [ ] 创建 `sysreq-to-pa-example.md`

#### Task 6：端到端符合性分析
- [ ] 创建 `guideline-traceability-analysis.md`
- [ ] 创建 `traceability-matrix-template.md`
- [ ] 创建 `compliance-report-template.md`
- [ ] 创建 `traceability-checklist.md`
- [ ] 创建 Skill：`traceability-analysis.md`
- [ ] 创建 `task-6-workflow.md`
- [ ] 创建 `traceability-example.md`

#### 共享资产
- [ ] 迁移 `business-patterns.md` 到 `07-shared-assets/patterns/`
- [ ] 创建 `architecture-patterns.md` 到 `07-shared-assets/patterns/`
- [ ] 迁移 `quality-checklist.md` 到 `07-shared-assets/quality-standards/`
- [ ] 迁移 `design-decision-template.md` 到 `07-shared-assets/quality-standards/`
- [ ] 迁移 `validate.py` 到 `07-shared-assets/tools/`
- [ ] 迁移 `generate-report.py` 到 `07-shared-assets/tools/`

---

### 第三阶段：产品数据迁移（2-3天）

#### 产品数据目录结构
对于每个项目（`08-products/projects/<project-name>/`），创建：
- [ ] `01-normalization/` 目录
- [ ] `02-sr-ba-design/` 目录
- [ ] `03-ba-sysreq-design/` 目录
- [ ] `04-sr-nfr-design/` 目录
- [ ] `05-sysreq-pa-design/` 目录
- [ ] `06-traceability-analysis/` 目录

#### 产品数据迁移
对于每个项目，迁移：
- [ ] `raw-requirements.md` → `01-normalization/`
- [ ] `sr-functional.md` → `01-normalization/`
- [ ] `sr-nfr.md` → `01-normalization/`
- [ ] `ba-design.md` → `02-sr-ba-design/`
- [ ] `sr-to-ba-mapping.md` → `02-sr-ba-design/`
- [ ] `sysreq-functional.md` → `03-ba-sysreq-design/`
- [ ] `ba-to-sysreq-mapping.md` → `03-ba-sysreq-design/`
- [ ] `sysreq-nfr.md` → `04-sr-nfr-design/`
- [ ] `sr-nfr-to-sysreq-nfr-mapping.md` → `04-sr-nfr-design/`
- [ ] `pa-design.md` → `05-sysreq-pa-design/`
- [ ] `sysreq-to-pa-mapping.md` → `05-sysreq-pa-design/`
- [ ] `nfr-tradeoff-decisions.md` → `05-sysreq-pa-design/`
- [ ] `traceability-matrix.md` → `06-traceability-analysis/`
- [ ] `compliance-report.md` → `06-traceability-analysis/`
- [ ] `defect-list.md` → `06-traceability-analysis/`
- [ ] `changelog.md` → 项目根目录

---

### 第四阶段：文档更新（2-3天）

#### 主要文档更新
- [ ] 更新 `CLAUDE.md`
  - [ ] 更新项目概述
  - [ ] 更新四层映射模型
  - [ ] 更新6个任务定义
  - [ ] 更新新的目录结构
  - [ ] 更新关键命令
- [ ] 创建 `NAVIGATION-GUIDE.md`
- [ ] 创建 `RESTRUCTURE-PLAN.md`
- [ ] 更新 `00-platform-docs/quick-start-guide.md`
- [ ] 更新 `00-platform-docs/project-directory-structure.md`

#### 交叉引用更新
- [ ] 更新所有README.md中的相关资源链接
- [ ] 更新所有guidelines中的相关资源链接
- [ ] 更新所有templates中的相关资源链接
- [ ] 更新所有examples中的相关资源链接

#### 导航链接创建
- [ ] 在每个任务README中添加"前置任务"链接
- [ ] 在每个任务README中添加"后续任务"链接
- [ ] 在每个任务README中添加"相关资源"链接

---

### 第五阶段：验证和优化（1-2天）

#### 链接验证
- [ ] 验证所有内部链接是否正确
- [ ] 验证所有文件路径是否正确
- [ ] 验证所有相对路径是否正确

#### 内容验证
- [ ] 验证所有README.md的内容完整性
- [ ] 验证所有guidelines的内容完整性
- [ ] 验证所有templates的内容完整性
- [ ] 验证所有checklists的内容完整性

#### 工作流验证
- [ ] 测试Task 1的工作流
- [ ] 测试Task 2的工作流
- [ ] 测试Task 3的工作流
- [ ] 测试Task 4的工作流
- [ ] 测试Task 5的工作流
- [ ] 测试Task 6的工作流

#### 工具验证
- [ ] 测试 `validate.py` 工具
- [ ] 测试 `generate-report.py` 工具

#### 反馈收集
- [ ] 邀请核心团队成员进行审查
- [ ] 收集反馈意见
- [ ] 进行微调

---

## 📊 迁移进度跟踪

### 第一阶段进度
- [ ] 目录结构：___% 完成
- [ ] README文件：___% 完成
- **总体进度**：___% 完成

### 第二阶段进度
- [ ] Task 1资产：___% 完成
- [ ] Task 2资产：___% 完成
- [ ] Task 3资产：___% 完成
- [ ] Task 4资产：___% 完成
- [ ] Task 5资产：___% 完成
- [ ] Task 6资产：___% 完成
- [ ] 共享资产：___% 完成
- **总体进度**：___% 完成

### 第三阶段进度
- [ ] 产品数据目录结构：___% 完成
- [ ] 产品数据迁移：___% 完成
- **总体进度**：___% 完成

### 第四阶段进度
- [ ] 主要文档更新：___% 完成
- [ ] 交叉引用更新：___% 完成
- [ ] 导航链接创建：___% 完成
- **总体进度**：___% 完成

### 第五阶段进度
- [ ] 链接验证：___% 完成
- [ ] 内容验证：___% 完成
- [ ] 工作流验证：___% 完成
- [ ] 工具验证：___% 完成
- [ ] 反馈收集：___% 完成
- **总体进度**：___% 完成

---

## 🎯 关键里程碑

| 里程碑 | 目标日期 | 状态 |
|--------|---------|------|
| 框架搭建完成 | 2026-05-13 | ⏳ |
| 资产迁移完成 | 2026-05-16 | ⏳ |
| 产品数据迁移完成 | 2026-05-18 | ⏳ |
| 文档更新完成 | 2026-05-20 | ⏳ |
| 验证和优化完成 | 2026-05-21 | ⏳ |
| **重构完成** | **2026-05-21** | ⏳ |

---

## 📝 注意事项

### 迁移过程中
- 保留原有的目录结构，直到迁移完全完成
- 在新目录中创建所有文件，不要删除旧目录
- 定期提交git commit，记录迁移进度

### 迁移完成后
- 验证所有功能正常
- 收集用户反馈
- 删除旧目录（如果确认不再需要）
- 更新所有文档和指南

### 风险管理
- **风险**：链接断裂导致文档无法访问
  - **缓解**：在第五阶段进行全面的链接验证
- **风险**：内容遗漏导致功能不完整
  - **缓解**：在第二阶段进行详细的资产清单检查
- **风险**：用户不适应新的目录结构
  - **缓解**：创建详细的导航指南和快速开始指南

---

## ✅ 最终检查清单

迁移完成前，请确保：

- [ ] 所有目录都已创建
- [ ] 所有文件都已迁移
- [ ] 所有链接都已验证
- [ ] 所有内容都已检查
- [ ] 所有工作流都已测试
- [ ] 所有工具都已验证
- [ ] 所有文档都已更新
- [ ] 所有反馈都已收集
- [ ] 所有问题都已解决
- [ ] 迁移完成报告已生成

---

**迁移开始日期**：2026-05-12
**预计完成日期**：2026-05-21
**总耗时**：约10天
