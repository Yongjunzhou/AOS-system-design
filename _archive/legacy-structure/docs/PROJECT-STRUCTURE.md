# AOS 项目 - 完整目录结构

```
AOS/
├── README.md                                      # 项目总览、使用指南
│
├── 01-standards/                                  # 标准和模板（组织资产）
│   ├── guidelines/                                # 设计准则
│   │   ├── README.md                              # 准则总览
│   │   ├── guideline-1-normalization.md           # 需求规范化准则
│   │   ├── guideline-2-sr-to-ba-mapping.md        # SR→BA映射准则
│   │   ├── guideline-3-ba-to-sr-mapping.md        # BA→SysReq映射准则
│   │   └── guideline-4-sr-to-pa-mapping.md        # SysReq→PA映射准则
│   │
│   ├── templates/                                 # 结构模板
│   │   ├── stakeholder-requirements-template.md   # 相关方需求模板
│   │   ├── business-architecture-template.md      # 业务架构模板
│   │   ├── system-requirements-template.md        # 系统需求模板
│   │   └── product-architecture-template.md       # 产品架构模板
│   │
│   └── patterns/                                  # 可复用的内容模式
│       ├── business-patterns.md                   # 业务模式库
│       ├── architecture-patterns.md               # 架构模式库
│       └── requirement-patterns.md                # 需求模式库
│
├── 02-pipeline/                                   # 设计流水线（AI资产）
│   ├── workflows.md                               # 新增需求处理流程（12步）
│   │
│   ├── skills/                                    # 9个 Skill（自动化资产）
│   │   ├── requirement-normalization.md           # Skill: 需求规范化
│   │   ├── requirement-decomposition.md           # Skill: 需求分解
│   │   ├── conflict-detection.md                  # Skill: 冲突检测
│   │   ├── duplicate-detection.md                 # Skill: 重复检测
│   │   ├── business-pattern-matching.md           # Skill: 业务模式匹配
│   │   ├── architecture-pattern-matching.md       # Skill: 架构模式匹配
│   │   ├── sr-to-ba-mapping.md                    # Skill: SR→BA映射
│   │   ├── ba-to-sr-mapping.md                    # Skill: BA→SysReq映射
│   │   └── sr-to-pa-mapping.md                    # Skill: SysReq→PA映射
│   │
│   └── tools/                                     # 工具脚本
│       ├── validate.py                            # 验证工具（多对一、语义覆盖等）
│       └── generate-report.py                     # 报告生成工具（追溯、映射等）
│
├── 03-products/                                   # 项目产出（产品数据）
│   ├── index.md                                   # 项目索引
│   │
│   └── projects/                                  # 按项目组织
│       ├── project-a/
│       │   ├── requirements.md                    # 规范化和分解后的相关方需求
│       │   ├── business-architecture.md           # 业务架构
│       │   ├── system-requirements.md             # 系统需求
│       │   ├── product-architecture.md            # 产品架构
│       │   ├── analysis.md                        # 需求分析记录（★ 核心）
│       │   │   # 包含：原始需求 + 规范化 + 分解 + 冲突检测 + 重复检测
│       │   │   #      + 分类 + 建议 + 人工确认
│       │   ├── mappings.md                        # 映射关系矩阵（★ 核心）
│       │   │   # SR→BA→SysReq→PA 的多对一关系和追溯链
│       │   └── changelog.md                       # 版本变更日志
│       │
│       └── project-b/
│           └── [同 project-a 结构]
│
└── .claude/
    ├── settings.json                              # Claude Code 配置
    └── memory/                                    # 项目记忆
```

---

## 核心文件说明

### 标准和准则
- **01-standards/guidelines/README.md** - 4条设计准则的总览
- **01-standards/guidelines/** - 4个详细准则文件
- **01-standards/templates/** - 4个模板，确保结构一致
- **01-standards/patterns/** - 业务、架构、需求模式库

### 流水线和自动化
- **02-pipeline/workflows.md** - 12步新增需求处理流程
- **02-pipeline/skills/** - 9个 Skill 支持自动化
- **02-pipeline/tools/** - Python 工具脚本

### 项目产出
- **03-products/projects/xxx/analysis.md** - ★ 记录原始需求→规范化→分解→确认的完整链路
- **03-products/projects/xxx/mappings.md** - ★ 记录 SR→BA→SysReq→PA 的多对一映射关系

---

## 关键设计原则

### 多对一映射关系
```
SR (相关方需求) → BA (业务架构) → SysReq (系统需求) → PA (产品架构)
         N:1              N:1            N:1
```

### 4条核心准则
1. ✓ 需求规范化、分解、初步设计BA承接层、去重、分类、建议、人工确认
2. ✓ 相关方需求与业务架构同步设计（N:1 多对一映射，1:1 约束）
3. ✓ 业务架构与系统需求同步设计（N:1 多对一映射，1:1 约束）
4. ✓ 系统需求与产品架构同步设计（N:1 多对一映射，1:1 约束）
5. ✓ 多对一关系 + 语义承接（完整覆盖）

---

## 使用流程

### 新增需求处理
1. 收集原始需求 → 记录到 `analysis.md`
2. 规范化 + 分解 → 使用 Skill
3. 冲突/重复检测 → 使用 Skill
4. 分类和建议 → 人工确认
5. 同步设计 → 更新各层级文档 + 使用 Skill
6. 验证映射 → 运行 validate.py
7. 更新 mappings.md + changelog.md

### 查看追溯关系
```
运行：generate-report.py --project project-a --report traceability
查看：SR → BA → SysReq → PA 的完整链路
```

---

## 文件数量统计

| 类别 | 数量 |
|------|------|
| 模板 | 4 |
| 模式库 | 3 |
| Skill | 9 |
| 工具脚本 | 2 |
| 项目示例 | 8 |
| 指南和流程 | 2 |
| **总计** | **29+** |

---

## 立即可以做的事

1. ✓ 项目结构已创建
2. ✓ 所有模板已准备
3. ✓ 所有 Skill 框架已准备
4. ✓ 工作流程已定义
5. → 下一步：根据实际项目填充 project-a（或创建 project-b）
6. → 完善工具脚本（validate.py、generate-report.py）
