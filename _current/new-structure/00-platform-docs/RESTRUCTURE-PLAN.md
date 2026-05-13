# AOS 流水线重构计划

## 概述

将AOS平台从"资产类型驱动"（standards/pipeline/products）重构为"任务驱动"（01-task-*/08-products），使每个任务都是相对独立的工作单元。

## 6个任务的完整定义

### Task 1：新增原始需求规范化

**目标**：将原始需求转化为规范化的相关方需求（SR）

**输入**：
- 原始需求文档（可能格式不统一、表述不清）

**输出**：
- `sr-functional.md`：规范化的功能相关方需求（SR）
- `sr-nfr.md`：规范化的非功能相关方需求（SR-NFR）
- 占位符：标记待确认项

**关键活动**：
1. 需求规范化（Skill：requirement-normalization）
2. 需求分解（Skill：requirement-decomposition）
3. 冲突检测（Skill：conflict-detection）
4. 重复检测（Skill：duplicate-detection）
5. 分类和确认

**检查清单**：normalization-checklist.md

---

### Task 2：功能相关方需求设计 + 业务架构初步设计

**目标**：将功能相关方需求（SR）映射到业务架构（BA），完成BA 0-5级设计

**输入**：
- `sr-functional.md`（来自Task 1）

**输出**：
- `ba-design.md`：BA 0-5级完整结构（5级是承接层）
- `sr-to-ba-mapping.md`：SR → BA的N:1映射矩阵
- 占位符：为BA 5级节点预留下游映射关系

**关键活动**：
1. 业务模式匹配（Skill：business-pattern-matching）
2. SR → BA映射（Skill：sr-to-ba-mapping）
3. BA 5级节点定义和确认

**检查清单**：sr-to-ba-checklist.md

**关键约束**：
- BA 5级是末级，不再分解
- BA 5级节点是承接SR的关键层级
- 一个BA 5级节点可以承接多条SR（N:1关系）

---

### Task 3：业务架构细化 + 系统功能需求架构设计

**目标**：将业务架构（BA）映射到系统功能需求（SysReq），完成SysReq 0-9级设计

**输入**：
- `ba-design.md`（来自Task 2）
- `sr-to-ba-mapping.md`（来自Task 2）

**输出**：
- `sysreq-functional.md`：SysReq 0-9级（功能分支）完整结构
- `ba-to-sysreq-mapping.md`：BA → SysReq的N:1映射矩阵
- 占位符：为SysReq 9级节点预留PA映射关系

**关键活动**：
1. 架构模式匹配（Skill：architecture-pattern-matching）
2. BA → SysReq映射（Skill：ba-to-sysreq-mapping）
3. SysReq 5级节点定义（承接BA 5级）
4. SysReq 6-9级节点分解（功能模块、用例、场景、活动）

**检查清单**：ba-to-sysreq-checklist.md

**关键约束**：
- SysReq 5级是承接BA 5级的关键层级（N:1关系）
- SysReq 9级（场景活动）是最细粒度，映射到PA末级
- SysReq 6-9级是组件实例的内部分解

---

### Task 4：非功能相关方需求设计 + 系统非功能需求架构设计

**目标**：将非功能相关方需求（SR-NFR）直接映射到系统非功能需求（SysReq-NFR），完成SysReq-NFR 0-5级设计

**输入**：
- `sr-nfr.md`（来自Task 1）

**输出**：
- `sysreq-nfr.md`：SysReq-NFR 0-5级完整结构
- `sr-nfr-to-sysreq-nfr-mapping.md`：SR-NFR → SysReq-NFR的N:1映射矩阵
- 占位符：为SysReq-NFR 5级节点预留PA权衡关系

**关键活动**：
1. SR-NFR → SysReq-NFR映射（Skill：sr-nfr-to-sysreq-nfr-mapping）
2. SysReq-NFR 5级节点定义（承接SR-NFR）
3. 非功能需求分类（质量特性、环境适应性、可实现性）

**检查清单**：sr-nfr-design-checklist.md

**关键约束**：
- 非功能需求是平行体系，不经过业务架构层
- SR-NFR直接映射到SysReq-NFR（无中间层）
- SysReq-NFR 5级是承接层，也是末级

---

### Task 5：系统需求设计 + 产品架构设计

**目标**：将系统功能需求和非功能需求映射到产品架构（PA），完成PA末级节点设计和非功能权衡

**输入**：
- `sysreq-functional.md`（来自Task 3）
- `ba-to-sysreq-mapping.md`（来自Task 3）
- `sysreq-nfr.md`（来自Task 4）
- `sr-nfr-to-sysreq-nfr-mapping.md`（来自Task 4）

**输出**：
- `pa-design.md`：PA末级节点设计（前后端组件）
- `sysreq-to-pa-mapping.md`：SysReq 9级 → PA末级的N:1映射矩阵
- `nfr-tradeoff-decisions.md`：非功能权衡决策和理由

**关键活动**：
1. SysReq → PA映射（Skill：sysreq-to-pa-mapping）
2. PA末级节点定义（前后端组件）
3. 非功能权衡分析和决策
4. 技术栈选型和架构决策

**检查清单**：
- sysreq-to-pa-checklist.md
- nfr-tradeoff-checklist.md

**关键约束**：
- PA末级节点 = 前后端组件
- SysReq 9级（场景活动）映射到PA末级（N:1关系）
- 非功能需求在PA层面进行权衡和优化

---

### Task 6：端到端符合性分析

**目标**：验证从SR到BA、SysReq、PA的完整链路，确保需求追溯的完整性和一致性

**输入**：
- 所有层级的设计文档（Task 1-5的所有输出）
- 所有映射矩阵

**输出**：
- `traceability-matrix.md`：完整的追溯矩阵（SR → BA → SysReq → PA）
- `compliance-report.md`：符合性分析报告
- `defect-list.md`：缺陷清单（遗漏、冲突、不一致）

**关键活动**：
1. 追溯矩阵生成（Skill：traceability-analysis）
2. 符合性检查
3. 缺陷识别和分类
4. 改进建议

**检查清单**：traceability-checklist.md

**关键约束**：
- 每条SR必须追溯到至少一个BA 5级节点
- 每个BA 5级节点必须追溯到至少一个SysReq 5级节点
- 每个SysReq 9级节点必须追溯到至少一个PA末级节点
- 所有SR-NFR必须追溯到SysReq-NFR 5级节点

---

## 目录结构详解

### 01-normalization/

```
01-normalization/
├── README.md                          # 任务概述和快速开始
├── guidelines/
│   └── guideline-normalization.md     # 需求规范化指南
├── templates/
│   ├── sr-template.md                 # 功能相关方需求模板
│   └── sr-nfr-template.md             # 非功能相关方需求模板
├── checklists/
│   └── normalization-checklist.md     # 规范化检查清单
├── skills/
│   ├── requirement-normalization.md   # Skill定义
│   ├── requirement-decomposition.md
│   ├── conflict-detection.md
│   └── duplicate-detection.md
├── workflows/
│   └── task-1-workflow.md             # 12步工作流
└── examples/
    └── normalization-example.md       # 真实案例示例
```

### 02-sr-ba-design/ 到 06-traceability-analysis/

结构类似，每个任务目录包含：
- `README.md`：任务概述
- `guidelines/`：该任务的指南
- `templates/`：该任务的输出模板
- `checklists/`：该任务的检查清单
- `skills/`：该任务的AI Skill定义
- `workflows/`：该任务的工作流
- `examples/`：该任务的示例

### 07-shared-assets/

跨任务共享的资产：
- `patterns/`：业务模式库、架构模式库
- `quality-standards/`：质量检查清单、设计决策模板
- `tools/`：验证工具、报告生成工具

### 08-products/

产品数据按项目和任务组织：
```
08-products/projects/<project-name>/
├── 01-normalization/
├── 02-sr-ba-design/
├── 03-ba-sysreq-design/
├── 04-sr-nfr-design/
├── 05-sysreq-pa-design/
├── 06-traceability-analysis/
└── changelog.md
```

---

## 迁移步骤

### 第一阶段：框架搭建（1-2天）

1. 创建新的目录结构
2. 为每个任务创建README.md
3. 为每个任务创建基础的guidelines/、templates/、checklists/、skills/、workflows/、examples/目录

### 第二阶段：资产迁移（3-5天）

1. **Task 1**：迁移normalization相关资产
2. **Task 2**：迁移sr-to-ba-mapping相关资产
3. **Task 3**：迁移ba-to-sysreq-mapping相关资产
4. **Task 4**：补充sr-nfr-to-sysreq-nfr相关资产（新增）
5. **Task 5**：迁移sysreq-to-pa-mapping相关资产，补充nfr-tradeoff相关资产
6. **Task 6**：迁移traceability-analysis相关资产

### 第三阶段：文档更新（2-3天）

1. 更新CLAUDE.md
2. 更新快速开始指南
3. 更新所有交叉引用
4. 创建迁移指南

### 第四阶段：验证和优化（1-2天）

1. 验证所有链接
2. 测试工作流
3. 收集反馈
4. 微调结构

---

## 关键设计原则

1. **任务独立性**：每个任务目录包含完整的资源，可以独立工作
2. **清晰的输入输出**：每个任务明确定义输入和输出
3. **占位符机制**：在各任务阶段直接创建占位符，支持两阶段工作流
4. **映射矩阵**：每个任务都生成映射矩阵，支持追溯
5. **检查清单**：每个任务都有检查清单，确保质量
6. **示例驱动**：每个任务都有真实案例示例，降低学习成本

---

## 预期收益

✅ **易用性提升**：新用户可以快速找到特定任务的所有资源
✅ **并行工作**：多个团队可以同时在不同任务上工作
✅ **质量保证**：每个任务都有明确的检查清单和验证机制
✅ **知识积累**：每个任务的最佳实践集中在一个地方
✅ **版本管理**：每个任务的资产可以独立版本化
✅ **可维护性**：结构清晰，易于维护和扩展
