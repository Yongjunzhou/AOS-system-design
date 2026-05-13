# AOS 系统设计项目 - 目录结构方案及详细说明

**文档日期**：2026-05-11  
**项目名称**：系统设计治理项目（AOS - Architecture & Orchestration System）  
**版本**：v2.0  
**编制人**：系统设计团队

---

## 一、项目概述

### 项目定义

AOS 是一个**系统设计治理和标准化**的组织级项目，建立从相关方需求到产品架构的完整链路，确保每一个需求都能被清晰地追溯和实现。

### 项目核心特性

✅ **结构化管理** - 规范化管理相关方需求、业务架构、系统需求、产品架构  
✅ **多对一映射** - 建立清晰的层级映射关系，确保每层级有唯一的承接点  
✅ **自动化支持** - 9 个 Skill + 工具脚本支持流水线自动化  
✅ **质量保证** - 规范化、分解、冲突检测、重复检测、人工确认的完整流程  
✅ **易于扩展** - 简化的目录结构，便于添加新项目

---

## 二、项目目标

1. **系统设计能力建设** - 设计业务架构、系统需求、产品架构
2. **组织资产积累** - 开发模板、准则、模式库，形成可复用资产
3. **设计流水线建设** - 形成 Skill 化的 AI 资产
4. **产品数据转化** - 将已有内容按照范例和准则转化为产品数据
5. **增量需求处理** - 后续新增需求按照准则进行规范化处理

---

## 三、核心设计准则（4 条）

### 按流程顺序的 4 条核心准则

#### 准则 1：相关方需求规范化与初步设计准则
- 需求完整性：9 个必填字段
- 需求分解：达到原子需求级别
- 初步设计BA承接层：三层优先级（配置改进 → 引擎改进 → 引擎开发）
- 冲突检测：直接冲突、间接冲突、可合并冲突
- 重复检测：完全重复、部分重复、相似重复
- 分类与确认：新增/改进/重复/冲突

#### 准则 2：相关方需求→业务架构分配准则
- **多对一映射**：N 条相关方需求 → 1 个业务架构承接层节点
- **一对一约束**：1 条相关方需求 → 唯一的业务架构承接层节点
- **语义覆盖**：业务架构承接层节点完全承接相关方需求语义
- **分配验证**：完整性检查、语义覆盖验证
- **无法分配处理**：再分解或创建新节点

#### 准则 3：业务架构→系统需求分配准则
- **N:1 多对一映射**：一个业务组件可能在多个业务上应用，多个 BA 5 级节点 → 1 个 SysReq 5 级节点
- **1:1 约束**：1 个业务架构 5 级节点 → 唯一的系统需求 5 级节点
- **去重机制**：BA 的所有 5 级节点去重后作为系统功能需求的清单
- **功能需求分解**：SysReq 5 级 → 6 级（功能模块）→ 7 级（系统用例）→ 8 级（用例场景）→ 9 级（场景活动）
- **非功能需求**：具体的量化指标（性能、安全、可用性等），作为系统约束

#### 准则 4：系统需求→产品架构分配准则
- **N:1 多对一映射**：多个 SysReq 9 级节点（场景活动）→ 1 个 PA 末级节点（前后端组件）
- **1:1 约束**：1 个系统需求 9 级节点 → 唯一的产品架构末级节点
- **功能实现**：产品架构末级节点完全实现系统需求的功能
- **非功能约束验证**：产品架构末级节点满足所有相关的非功能约束
- **反向迭代**：当约束无法满足时，向上迭代调整系统需求、业务架构、相关方需求

---

## 四、完整目录结构（新的任务驱动架构）

```
AOS/
├── README.md                                    # 项目总览
├── CLAUDE.md                                    # Claude Code 指导
│
├── 01-normalization/                       # Task 1：需求规范化
│   ├── README.md                                # 任务概述和快速开始
│   ├── guidelines/                              # 规范化指南
│   ├── templates/                               # 规范化模板
│   ├── checklists/                              # 规范化检查清单
│   ├── skills/                                  # 相关 Skill
│   ├── workflows/                               # 工作流定义
│   └── examples/                                # 规范化示例
│
├── 02-sr-ba-design/                        # Task 2：SR → BA 映射
│   ├── README.md                                # 任务概述和快速开始
│   ├── guidelines/                              # 映射指南
│   ├── templates/                               # 映射模板
│   ├── checklists/                              # 映射检查清单
│   ├── skills/                                  # 相关 Skill
│   ├── workflows/                               # 工作流定义
│   └── examples/                                # 映射示例
│
├── 03-ba-sysreq-design/                    # Task 3：BA → SysReq 映射
│   ├── README.md                                # 任务概述和快速开始
│   ├── guidelines/                              # 映射指南
│   ├── templates/                               # 映射模板
│   ├── checklists/                              # 映射检查清单
│   ├── skills/                                  # 相关 Skill
│   ├── workflows/                               # 工作流定义
│   └── examples/                                # 映射示例
│
├── 04-sr-nfr-design/                       # Task 4：SR-NFR → SysReq-NFR 映射
│   ├── README.md                                # 任务概述和快速开始
│   ├── guidelines/                              # 映射指南
│   ├── templates/                               # 映射模板
│   ├── checklists/                              # 映射检查清单
│   ├── skills/                                  # 相关 Skill
│   ├── workflows/                               # 工作流定义
│   └── examples/                                # 映射示例
│
├── 05-sysreq-pa-design/                    # Task 5：SysReq → PA 映射
│   ├── README.md                                # 任务概述和快速开始
│   ├── guidelines/                              # 映射指南
│   ├── templates/                               # 映射模板
│   ├── checklists/                              # 映射检查清单
│   ├── skills/                                  # 相关 Skill
│   ├── workflows/                               # 工作流定义
│   └── examples/                                # 映射示例
│
├── 06-traceability-analysis/               # Task 6：端到端追溯分析
│   ├── README.md                                # 任务概述和快速开始
│   ├── guidelines/                              # 分析指南
│   ├── templates/                               # 分析模板
│   ├── checklists/                              # 分析检查清单
│   ├── skills/                                  # 相关 Skill
│   ├── workflows/                               # 工作流定义
│   └── examples/                                # 分析示例
│
├── 07-shared-assets/                            # 共享资产
│   ├── patterns/                                # 可复用模式库
│   │   ├── business-patterns.md                 # 业务模式
│   │   └── architecture-patterns.md             # 架构模式
│   ├── quality-standards/                       # 质量标准
│   │   ├── quality-checklist.md                 # 质量检查清单
│   │   └── design-decision-template.md          # 设计决策模板
│   └── tools/                                   # 工具脚本
│       ├── validate.py                          # 验证工具
│       └── generate-report.py                   # 报告生成工具
│
├── 08-products/                                 # 产品数据
│   ├── index.md                                 # 产品索引
│   └── projects/
│       ├── project-a/
│       │   ├── 01-normalization/                # Task 1 输出
│       │   │   ├── raw-requirements.md
│       │   │   └── ...
│       │   ├── 02-sr-ba-design/                 # Task 2 输出
│       │   │   ├── ba-design.md
│       │   │   ├── sr-to-ba-mapping.md
│       │   │   └── ...
│       │   ├── 03-ba-sysreq-design/             # Task 3 输出
│       │   │   ├── sysreq-functional.md
│       │   │   ├── ba-to-sysreq-mapping.md
│       │   │   └── ...
│       │   ├── 04-sr-nfr-design/                # Task 4 输出
│       │   │   ├── sr-nfr-to-sysreq-nfr-mapping.md
│       │   │   └── ...
│       │   ├── 05-sysreq-pa-design/             # Task 5 输出
│       │   │   ├── pa-design.md
│       │   │   ├── sysreq-to-pa-mapping.md
│       │   │   ├── nfr-tradeoff-decisions.md
│       │   │   └── ...
│       │   ├── 06-traceability-analysis/        # Task 6 输出
│       │   │   ├── traceability-matrix.md
│       │   │   ├── compliance-report.md
│       │   │   ├── defect-list.md
│       │   │   └── ...
│       │   └── changelog.md                     # 项目变更日志
│       └── project-b/
│           └── [同 project-a 结构]
│
├── 00-platform-docs/                            # 平台文档
│   ├── quick-start-guide.md                     # 快速开始指南
│   ├── pipeline-stakeholder-requirements.md     # 相关方需求定义
│   └── project-directory-structure.md           # 本文档
│
└── .claude/
    ├── settings.json
    └── memory/
```

---

## 五、任务驱动架构的优势

### 1. 独立的工作单元
- 每个任务是独立的工作单元，包含完整的资源
- 支持多个团队并行工作
- 清晰的输入/输出定义，便于协作

### 2. 完整的任务资源
- 每个任务包含：指南、模板、检查清单、Skill、工作流、示例
- 新手可以快速上手
- 经验丰富的人员可以快速参考

### 3. 共享资产库
- 业务模式库和架构模式库供所有任务使用
- 质量检查清单确保一致的质量标准
- 工具脚本支持自动化验证和报告生成

### 4. 清晰的产品数据组织
- 每个项目按照 6 个任务的输出进行组织
- 易于追溯每个任务的输出
- 支持增量更新和版本管理

---

## 六、关键文件详解

### 每个任务目录的结构

**README.md** - 任务概述和快速开始
- 任务目标和范围
- 快速开始指南
- 关键活动和输出
- 常见问题

**guidelines/** - 任务指南
- 详细的操作指南
- 最佳实践
- 常见陷阱和解决方案

**templates/** - 任务模板
- 输出文档的模板
- 示例和说明
- 填充指南

**checklists/** - 任务检查清单
- 质量检查清单
- 完整性检查清单
- 验证清单

**skills/** - 相关 Skill
- AI Skill 定义
- 输入/输出规范
- 处理逻辑说明

**workflows/** - 工作流定义
- 任务的详细工作流
- 步骤和决策点
- 交接标准

**examples/** - 任务示例
- 实际的示例项目
- 参考实现
- 最佳实践展示

---

## 七、产品数据组织

### 每个项目的结构

```
project-a/
├── 01-normalization/              # Task 1 输出
│   └── raw-requirements.md        # 规范化的相关方需求
├── 02-sr-ba-design/               # Task 2 输出
│   ├── ba-design.md               # 业务架构设计
│   └── sr-to-ba-mapping.md        # SR→BA 映射矩阵
├── 03-ba-sysreq-design/           # Task 3 输出
│   ├── sysreq-functional.md       # 系统功能需求
│   └── ba-to-sysreq-mapping.md    # BA→SysReq 映射矩阵
├── 04-sr-nfr-design/              # Task 4 输出
│   └── sr-nfr-to-sysreq-nfr-mapping.md  # SR-NFR→SysReq-NFR 映射矩阵
├── 05-sysreq-pa-design/           # Task 5 输出
│   ├── pa-design.md               # 产品架构设计
│   ├── sysreq-to-pa-mapping.md    # SysReq→PA 映射矩阵
│   └── nfr-tradeoff-decisions.md  # 非功能权衡决策
├── 06-traceability-analysis/      # Task 6 输出
│   ├── traceability-matrix.md     # 追溯矩阵
│   ├── compliance-report.md       # 符合性分析报告
│   └── defect-list.md             # 缺陷清单
└── changelog.md                   # 项目变更日志
```

### 文件统计

| 任务 | 输出文件数 | 说明 |
|------|-----------|------|
| Task 1 | 1 | 规范化的相关方需求 |
| Task 2 | 2 | 业务架构设计 + 映射矩阵 |
| Task 3 | 2 | 系统需求设计 + 映射矩阵 |
| Task 4 | 1 | 非功能需求映射矩阵 |
| Task 5 | 3 | 产品架构设计 + 映射矩阵 + 权衡决策 |
| Task 6 | 3 | 追溯矩阵 + 符合性报告 + 缺陷清单 |
| **总计** | **13** | 每个项目 13 个文件 |

---

## 八、新增需求处理流程

```
第1步：收集原始需求
   ↓ (记录到 Task 1)
第2步：执行 Task 1 - 需求规范化
   ├─ 规范化 + 分解 (Skill)
   ├─ 冲突检测 (Skill)
   ├─ 重复检测 (Skill)
   └─ 分类和建议
   ↓
第3步：人工确认
   ↓
第4步：执行 Task 2 - SR → BA 映射
   ├─ 创建占位符
   ├─ 设计业务架构
   └─ 建立映射关系
   ↓
第5步：执行 Task 3 - BA → SysReq 映射
   ├─ 创建占位符
   ├─ 设计系统需求
   └─ 建立映射关系
   ↓
第6步：执行 Task 4 - SR-NFR → SysReq-NFR 映射
   ├─ 设计非功能需求
   └─ 建立映射关系
   ↓
第7步：执行 Task 5 - SysReq → PA 映射
   ├─ 创建占位符
   ├─ 设计产品架构
   ├─ 建立映射关系
   └─ 记录权衡决策
   ↓
第8步：执行 Task 6 - 端到端追溯分析
   ├─ 验证追溯链路
   ├─ 生成符合性报告
   └─ 识别缺陷
   ↓
第9步：更新 changelog.md
   ↓
完成
```

---

## 九、使用指南

### 新增项目

1. 在 `08-products/projects/` 下创建 `project-x/` 目录
2. 创建 6 个子目录（01-normalization 到 06-traceability-analysis）
3. 参考 project-a 的结构和内容
4. 按照各任务的模板填充内容

### 新增需求

1. 收集原始需求
2. 按照 Task 1 的流程进行规范化
3. 按照 Task 2-6 的流程依次执行
4. 运行 `validate.py` 验证映射关系
5. 更新 `changelog.md`

### 生成报告

```bash
# 验证所有映射关系
python 07-shared-assets/tools/validate.py --project project-a --check all

# 生成追溯矩阵报告
python 07-shared-assets/tools/generate-report.py --project project-a --report traceability

# 生成项目汇总报告
python 07-shared-assets/tools/generate-report.py --project project-a --report summary
```

---

## 十、项目优势

### 1. 任务独立性
- 每个任务是独立的工作单元
- 支持多个团队并行工作
- 清晰的输入/输出定义

### 2. 资源完整性
- 每个任务包含所有必需的资源
- 新手可以快速上手
- 经验丰富的人员可以快速参考

### 3. 质量保证
- 每个任务都有检查清单
- 共享的质量标准
- 自动化验证工具

### 4. 易于扩展
- 新增项目只需复制结构
- 新增需求只需按照流程处理
- 支持持续优化和迭代

---

## 十一、实施建议

### 第一阶段：框架搭建（1-2 天）
- ✅ 创建 6 个任务目录
- ✅ 创建共享资产目录
- ✅ 创建产品数据目录

### 第二阶段：资产迁移（3-5 天）
- ✅ 迁移所有资产到各任务目录
- ✅ 创建新的资产（Task 4、Task 6）
- ✅ 创建共享资产

### 第三阶段：产品数据迁移（2-3 天）
- ✅ 按照新结构组织产品数据
- ✅ 创建所有必需的文件

### 第四阶段：文档更新（1 天）
- 更新 CLAUDE.md
- 更新快速开始指南
- 更新所有交叉引用

### 第五阶段：验证和优化（1 天）
- 验证所有链接
- 测试所有工作流
- 收集反馈

---

## 十二、总结

AOS 项目通过**任务驱动架构**，实现：

✅ 清晰的工作单元划分  
✅ 支持多个团队并行工作  
✅ 完整的资源和工具支持  
✅ 一致的质量标准  
✅ 易于扩展和维护  

这个项目可以**持续演进和优化**，随着实际应用的深入，不断改进任务定义、资源库和工具。

---

## 附录：快速参考

### 常用命令

```bash
# 验证项目映射关系
python 07-shared-assets/tools/validate.py --project project-a --check all

# 生成追溯矩阵报告
python 07-shared-assets/tools/generate-report.py --project project-a --report traceability

# 生成项目汇总报告
python 07-shared-assets/tools/generate-report.py --project project-a --report summary
```

### 重要文件速查

| 需要... | 查看文件 |
|--------|--------|
| 了解项目 | CLAUDE.md |
| 快速开始 | 00-platform-docs/quick-start-guide.md |
| 查看结构 | 00-platform-docs/project-directory-structure.md |
| Task 1 | 01-normalization/README.md |
| Task 2 | 02-sr-ba-design/README.md |
| Task 3 | 03-ba-sysreq-design/README.md |
| Task 4 | 04-sr-nfr-design/README.md |
| Task 5 | 05-sysreq-pa-design/README.md |
| Task 6 | 06-traceability-analysis/README.md |
| 共享资产 | 07-shared-assets/ |
| 示例项目 | 08-products/projects/project-a/ |

---

**最后更新**：2026-05-12  
**编制人**：系统设计团队  
**项目地址**：e:\mywork\AOS  
**文档版本**：v3.0（任务驱动架构）
