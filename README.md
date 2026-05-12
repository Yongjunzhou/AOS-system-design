# 系统设计治理项目

## 项目目标

1. 从企业各业务部门对信息系统的相关方需求开始分析、分解和分配，设计开发业务架构、信息系统需求规格、信息系统产品架构
2. 开发并持续优化相关方需求、业务架构、系统需求和产品架构的模板或范例、设计准则，形成组织资产
3. 开发并持续优化系统设计流水线，形成 Skill 化的组织资产，作为后续开发的 AI 资产
4. 将已有相关方需求、业务架构、系统需求和产品架构按照范例和准则转化为项目的产品数据
5. 后续新增相关方需求，则按照设计准则、模板或范例，综合已有产品数据，补充完善相关方需求、业务架构、系统需求、产品架构

## 核心设计准则

### 5 条核心准则（按流程顺序）
0. **准则 0**：占位符规范与两阶段工作流程
1. **准则 1**：相关方需求规范化与初步设计
2. **准则 2**：相关方需求→业务架构分配
3. **准则 3**：业务架构→系统需求分配
4. **准则 4**：系统需求→产品架构分配

详见 `01-standards/guidelines/README.md`

## 核心创新

### 非功能需求架构

采用平行的架构体系，独立于业务架构设计，确保非功能需求的完整性和可追溯性：

- **质量特性需求**：性能、可靠性、安全性、可用性、可维护性等
- **环境适应性需求**：兼容性、可扩展性、可移植性、集成适应性等
- **可实现性需求**：可生产性、可测试性、可交付性、可部署性、可操作性、可运维性、可退役性等

非功能需求采用 0-6 级层级结构，与业务架构平行，最终映射到系统需求和产品架构。

### 两阶段工作流程

采用"占位符"机制实现上下游文档的解耦和并行工作：

- **第一阶段**（1-2 小时）：占位符创建
  - 下游团队快速扫描上游文档
  - 为每个上游末级节点创建对应的占位符
  - 建立映射关系，冻结占位符结构
  
- **第二阶段**（2-6 天）：具体设计
  - 下游团队填充占位符的具体内容
  - 确保与上游文档的映射关系一致
  - 为下游文档预留占位符

**优势**：
- ✅ 时间缩短 30-50%（从 2-3 周缩短到 1-1.5 周）
- ✅ 团队可以独立工作，不需要频繁同步
- ✅ 清晰的工作启动点，避免过度的同步迭代

详见 `02-pipeline/workflows.md`

## 目录结构

```
01-standards/          # 标准和模板
├── guidelines/        # 5条设计准则
│   ├── README.md
│   ├── guideline-0-placeholder.md
│   ├── guideline-1-normalization.md
│   ├── guideline-2-sr-to-ba-mapping.md
│   ├── guideline-3-ba-to-sr-mapping.md
│   └── guideline-4-sr-to-pa-mapping.md
├── checklists/        # 检查清单
│   └── placeholder-checklist.md
├── templates/         # 结构模板
└── patterns/          # 可复用的内容模式

02-pipeline/           # 设计流水线（AI资产）
├── skills/            # 9个 Skill（自动化资产）
├── tools/             # 验证和报告工具
├── workflows.md       # 新增需求处理流程（14步）和两阶段工作流程详解

03-products/           # 项目产出
├── projects/          # 按项目组织
│   ├── project-a/
│   └── project-b/
└── index.md           # 项目索引
```

## 快速开始

1. 了解核心概念
   - 阅读 `01-standards/guidelines/README.md` 了解 5 条准则
   - 阅读 `02-pipeline/workflows.md` 了解新增需求处理流程和两阶段工作流程

2. 参考模板和准则
   - 参考 `01-standards/templates/` 中的模板
   - 遵循 `01-standards/guidelines/` 中的设计准则

3. 新增需求处理
   - 按照 `02-pipeline/workflows.md` 的 14 步流程处理
   - 使用 `01-standards/checklists/placeholder-checklist.md` 验证占位符质量

4. 项目产出
   - 项目产出保存到 `03-products/projects/` 下
   - 每个项目包含 7 个文件：requirements.md、business-architecture.md、system-requirements.md、product-architecture.md、analysis.md、mappings.md、changelog.md

## 新增需求处理流程（14 步）

1. 收集原始需求 → 记录到 `analysis.md`
2. 规范化 + 分解 → 使用相应 Skill
3. 冲突检测 + 重复检测 → 使用相应 Skill
4. 分类和建议 → 记录到 `analysis.md`
5. 人工确认 → 相关方确认
6-8. 【第一阶段】占位符创建 → BA、SysReq、PA 占位符
9-11. 【第二阶段】同步设计 → SR↔BA、BA↔SysReq、SysReq↔PA
12. 完整追溯链验证
13. 多对一和语义覆盖验证
14. 更新 `mappings.md` 和 `changelog.md`
