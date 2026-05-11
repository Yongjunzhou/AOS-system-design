# 系统设计治理项目

## 项目目标

1. 从企业各业务部门对信息系统的相关方需求开始分析、分解和分配，设计开发业务架构、信息系统需求规格、信息系统产品架构
2. 开发并持续优化相关方需求、业务架构、系统需求和产品架构的模板或范例、设计准则，形成组织资产
3. 开发并持续优化系统设计流水线，形成 Skill 化的组织资产，作为后续开发的 AI 资产
4. 将已有相关方需求、业务架构、系统需求和产品架构按照范例和准则转化为项目的产品数据
5. 后续新增相关方需求，则按照设计准则、模板或范例，综合已有产品数据，补充完善相关方需求、业务架构、系统需求、产品架构

## 核心设计准则

### 4 条核心准则（按流程顺序）
1. **准则 1**：相关方需求规范化与初步设计
2. **准则 2**：相关方需求→业务架构分配
3. **准则 3**：业务架构→系统需求分配
4. **准则 4**：系统需求→产品架构分配

详见 `01-standards/guidelines/README.md`

## 目录结构

```
01-standards/          # 标准和模板
├── guidelines/        # 4条设计准则
│   ├── README.md
│   ├── guideline-1-normalization.md
│   ├── guideline-2-sr-to-ba-mapping.md
│   ├── guideline-3-ba-to-sr-mapping.md
│   └── guideline-4-sr-to-pa-mapping.md
├── templates/         # 结构模板
└── patterns/          # 可复用的内容模式

02-pipeline/           # 设计流水线（AI资产）
├── skills/            # 9个 Skill（自动化资产）
├── tools/             # 验证和报告工具
└── workflows.md       # 新增需求处理流程

03-products/           # 项目产出
├── projects/          # 按项目组织
│   ├── project-a/
│   └── project-b/
└── index.md           # 项目索引
```

## 快速开始

1. 参考 `01-standards/templates/` 中的模板
2. 遵循 `01-standards/guidelines/README.md` 中的设计准则
3. 新增需求时，按照 `02-pipeline/workflows.md` 的流程处理
4. 项目产出保存到 `03-products/projects/` 下

## 新增需求处理流程

1. 收集原始需求 → 记录到 `analysis.md`
2. 规范化 + 分解 → 使用相应 Skill
3. 冲突检测 + 重复检测 → 使用相应 Skill
4. 分类和建议 → 记录到 `analysis.md`
5. 人工确认 → 相关方确认
6. 同步设计 → 更新各层级文档
7. 验证映射 → 运行验证工具
8. 更新 `mappings.md` 和 `changelog.md`
