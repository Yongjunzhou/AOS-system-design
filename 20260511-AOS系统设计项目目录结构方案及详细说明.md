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
- **多对一映射**：N 个业务架构承接层节点 → 1 个系统需求承接层节点
- **一对一约束**：1 个业务架构承接层节点 → 唯一的系统需求承接层节点
- **语义覆盖**：系统需求完全实现业务架构承接层节点功能
- **功能需求**：清晰的操作描述、输入输出、业务规则
- **非功能需求**：具体的量化指标（性能、安全、可用性等）

#### 准则 4：系统需求→产品架构分配准则
- **多对一映射**：N 条系统需求 → 1 个产品架构承接层节点
- **一对一约束**：1 条系统需求 → 唯一的产品架构承接层节点
- **语义覆盖**：产品架构承接层节点完全实现系统需求
- **组件职责**：单一职责、清晰边界、独立测试
- **组件通信**：同步调用、异步消息、数据库共享、缓存

---

## 四、完整目录结构

```
AOS/
├── README.md                                    # 项目总览
├── PROJECT-STRUCTURE.md                         # 结构说明
├── 20260511-AOS系统设计项目目录结构方案及详细说明.md  # 本文档
│
├── 01-standards/                                # 组织资产
│   ├── guidelines/                              # 4条设计准则
│   │   ├── README.md                            # 准则总览
│   │   ├── guideline-1-normalization.md         # 需求规范化准则
│   │   ├── guideline-2-sr-to-ba-mapping.md      # SR→BA映射准则
│   │   ├── guideline-3-ba-to-sr-mapping.md      # BA→SysReq映射准则
│   │   └── guideline-4-sr-to-pa-mapping.md      # SysReq→PA映射准则
│   ├── templates/                               # 4个结构模板
│   │   ├── stakeholder-requirements-template.md
│   │   ├── business-architecture-template.md
│   │   ├── system-requirements-template.md
│   │   └── product-architecture-template.md
│   └── patterns/                                # 3个可复用模式
│       ├── business-patterns.md
│       ├── architecture-patterns.md
│       └── requirement-patterns.md
│
├── 02-pipeline/                                 # AI资产和流水线
│   ├── workflows.md                             # 12步处理流程
│   ├── skills/                                  # 9个Skill
│   │   ├── requirement-normalization.md
│   │   ├── requirement-decomposition.md
│   │   ├── conflict-detection.md
│   │   ├── duplicate-detection.md
│   │   ├── business-pattern-matching.md
│   │   ├── architecture-pattern-matching.md
│   │   ├── sr-to-ba-mapping.md
│   │   ├── ba-to-sr-mapping.md
│   │   └── sr-to-pa-mapping.md
│   └── tools/                                   # 工具脚本
│       ├── validate.py
│       └── generate-report.py
│
├── 03-products/                                 # 项目产出
│   ├── index.md
│   └── projects/
│       ├── project-a/
│       │   ├── requirements.md
│       │   ├── business-architecture.md
│       │   ├── system-requirements.md
│       │   ├── product-architecture.md
│       │   ├── analysis.md                    # ★ 核心：需求分析
│       │   ├── mappings.md                    # ★ 核心：映射矩阵
│       │   └── changelog.md
│       └── project-b/
│           └── [同 project-a 结构]
│
└── .claude/
    ├── settings.json
    └── memory/
```

---

## 五、关键文件详解

### analysis.md - 需求分析记录（★ 核心）

**用途**：记录新增需求的完整处理过程

**包含内容**：
1. 原始需求 - 原始输入和来源
2. 规范化过程 - 规范化结果和决策
3. 分解结果 - 分解后的需求列表
4. 冲突检测 - 检测到的冲突和分类
5. 重复检测 - 检测到的重复和分类
6. 分类结果 - 新增/改进/重复/冲突的分类
7. 建议处理 - 给出的处理建议
8. 人工确认 - 相关方的确认记录

**满足准则**：准则 1（需求规范化、分解、去重、分类、建议、人工确认）

### mappings.md - 映射关系矩阵（★ 核心）

**用途**：记录各层级的映射关系和完整追溯链

**包含内容**：
1. SR→BA 映射 - 相关方需求到业务架构的映射（N:1）
2. BA→SysReq 映射 - 业务架构到系统需求的映射（N:1）
3. SysReq→PA 映射 - 系统需求到产品架构的映射（N:1）
4. 完整追溯链 - SR 到 PA 的完整链路
5. 映射验证 - 多对一、语义覆盖、完整性验证

**满足准则**：准则 2-7（各层级的多对一映射和语义覆盖）

---

## 六、新增需求处理流程（12 步）

```
第1步：收集原始需求
   ↓ (记录到 analysis.md)
第2步：规范化 + 分解 (Skill)
   ↓
第3步：冲突检测 (Skill)
   ↓
第4步：重复检测 (Skill)
   ↓
第5步：分类和建议
   ↓ (记录到 analysis.md)
第6步：人工确认 ← 准则1
   ↓
第7步：相关方需求↔业务架构同步设计 (Skill) ← 准则2
   ↓
第8步：业务架构↔系统需求同步设计 (Skill) ← 准则3
   ↓
第9步：系统需求↔产品架构同步设计 (Skill) ← 准则4
   ↓
第10步：验证映射关系 (Tool) ← 准则5-7
   ↓
第11步：更新 mappings.md
   ↓
第12步：更新 changelog.md
   ↓
完成
```

---

## 七、多对一映射关系

```
相关方需求        业务架构         系统需求          产品架构
   ↓                ↓                ↓                ↓
SR-001          BA-NODE-001      SysReq-001      PA-COMP-001
SR-002     →                  →                →
SR-003                         SysReq-002      PA-COMP-002

3:1 映射    1:1 约束   N:1 映射    1:1 约束    N:1 映射    1:1 约束    2:1 映射
```

**核心规则**：
- 相关方需求→业务架构：多条需求可映射到一个节点，但每条需求只能映射到一个节点
- 业务架构→系统需求：多条需求可来自一个节点，但每个节点只能分解到一个需求承接层节点
- 系统需求→产品架构：多个组件可实现一个需求，但每条需求只能映射到一个架构节点

---

## 八、文件统计

### 按类别统计

| 类别 | 数量 | 说明 |
|------|------|------|
| 核心文档 | 3 | README.md, PROJECT-STRUCTURE.md, 本文档 |
| 准则文件 | 5 | guidelines/README.md + 4个详细准则 |
| 模板 | 4 | 相关方需求、业务架构、系统需求、产品架构 |
| 模式库 | 3 | 业务、架构、需求模式 |
| Skill | 9 | 自动化资产 |
| 工具脚本 | 2 | 验证和报告工具 |
| 流程文档 | 1 | workflows.md |
| **总计（不含项目文件）** | **27** | - |

### 项目文件（每项目）

每个项目包含 7 个文件：
- requirements.md（相关方需求）
- business-architecture.md（业务架构）
- system-requirements.md（系统需求）
- product-architecture.md（产品架构）
- analysis.md（★ 需求分析记录）
- mappings.md（★ 映射关系矩阵）
- changelog.md（版本变更日志）

---

## 九、使用指南

### 新增项目

1. 在 `03-products/projects/` 下创建 `project-x/` 目录
2. 复制 project-a 的所有文件作为模板
3. 按照 `01-standards/templates/` 中的模板填充内容
4. 参考 `01-standards/guidelines/README.md` 的设计准则

### 新增需求

1. 收集原始需求，记录到 `analysis.md`
2. 运行相应 Skill 进行规范化、分解、冲突检测、重复检测
3. 相关方进行人工确认
4. 运行 Skill 进行各层级映射（SR→BA、BA→SysReq、SysReq→PA）
5. 运行 `validate.py` 验证映射关系
6. 更新 `mappings.md` 和 `changelog.md`

### 生成报告

```bash
python 02-pipeline/tools/generate-report.py --project project-a --report traceability
```

获得 SR→BA→SysReq→PA 的完整追溯矩阵

---

## 十、项目优势

### 1. 结构清晰
- 简化的目录结构，易于理解和使用
- 明确的分工：standards、pipeline、products

### 2. 质量保证
- 4 条设计准则，确保各层级的质量
- 规范化、分解、冲突检测、重复检测、人工确认的完整流程
- 多对一映射和语义覆盖的验证

### 3. 自动化支持
- 9 个 Skill 支持各个环节的自动化
- 工具脚本支持验证和报告生成
- 减少手工操作，提高效率

### 4. 可复用资产
- 4 个模板确保结构一致
- 3 个模式库提供参考方案
- 组织级的知识积累和经验沉淀

### 5. 易于扩展
- 新增项目只需复制结构
- 新增需求只需按照流程处理
- 支持持续优化和迭代

---

## 十一、实施建议

### 第一阶段：项目初始化（1-2 周）
1. ✅ 创建项目结构（已完成）
2. 创建第一个项目（project-a）的实际数据
3. 填充相关方需求、业务架构、系统需求、产品架构
4. 测试和验证流程

### 第二阶段：流程验证（2-4 周）
1. 使用 workflows.md 处理新增需求
2. 完善 Skill 和工具的具体实现
3. 收集反馈，优化准则

### 第三阶段：推广应用（4 周以后）
1. 创建更多项目
2. 推广到其他业务部门
3. 持续优化和改进

---

## 十二、总结

AOS 项目通过**结构化**的目录组织、**标准化**的模板准则、**自动化**的 Skill 流水线，实现：

✅ 相关方需求的规范化和质量保证  
✅ 清晰的层级映射关系（多对一）  
✅ 完整的需求追溯链（SR→BA→SysReq→PA）  
✅ 组织级的设计资产积累  
✅ AI 支持的自动化设计流水线  

这个项目可以**持续演进和优化**，随着实际应用的深入，不断改进模板、准则、模式库和工具。

---

## 附录：快速参考

### 常用命令

```bash
# 验证项目映射关系
python 02-pipeline/tools/validate.py --project project-a --check all

# 生成追溯矩阵报告
python 02-pipeline/tools/generate-report.py --project project-a --report traceability

# 生成项目汇总报告
python 02-pipeline/tools/generate-report.py --project project-a --report summary
```

### 重要文件速查

| 需要... | 查看文件 |
|--------|--------|
| 了解项目 | README.md |
| 查看结构 | PROJECT-STRUCTURE.md |
| 了解准则 | 01-standards/guidelines/README.md |
| 查看模板 | 01-standards/templates/ |
| 理解流程 | 02-pipeline/workflows.md |
| 查看需求分析 | 03-products/projects/xxx/analysis.md |
| 查看映射关系 | 03-products/projects/xxx/mappings.md |

---

**最后更新**：2026-05-11  
**编制人**：系统设计团队  
**项目地址**：e:\mywork\AOS  
**文档版本**：v2.0
