# task-01：现有产物梳理与架构分析

**对应场景**：02-reverse-engineering · 第1步
**对应 AI 模板**：`03-pipeline-system-design-ai-support/02-reverse-engineering-pipeline-system-design/workflow-prompts.md` 第1步
**对应设计指南**：[逆向工程系统设计指南 第1步](../../02-pipeline-system-design-guidelines/02-reverse-engineering-pipeline-system-design-guide.md#第1步现有产物梳理与架构分析)

---

## 目标

全面梳理产品B（系统设计流水线）现有的所有产物，理解当前的目录结构和文件组织方式，建立完整的产物全局视图，为后续逆向推导提供基础。

## 上下文继承

```
从哪里来：
  - 直接输入：项目目录结构、现有设计文档/指南/AI辅助文档/产品数据
  - 参考文档：通用方法论（00-general/）、Skill 定义（.claude/skills/）
  - 涉及规范：产品架构规范 §2

预期产出：
  1. 产物总览清单（产物分类 + 架构层级映射）
  2. 覆盖盲区标记

本步决策对后续的影响：
  - 产物分类结果直接影响第2步 PA 组件识别
  - 覆盖盲区标记影响第7步验证的检查范围
  - 架构层级映射为后续所有逆向推导提供分类基础
```

---

## 输入

| 输入 | 路径 |
|------|------|
| 项目目录结构 | 整个仓库根目录 |
| 现有设计文档 | `01-pipeline-system-design-standards/` |
| 现有设计指南 | `02-pipeline-system-design-guidelines/` |
| 现有 AI 辅助文档 | `03-pipeline-system-design-ai-support/` |
| 现有产品数据模板 | `10-pipeline-system-product-data/` |
| 通用方法论 | `00-general/` |
| Skill 定义 | `.claude/skills/rule-conformance-review/` |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 生成完整目录树 | AI | 列出仓库全部目录和文件（排除 .git、node_modules 等无关目录） |
| 2 | 按架构层级分类现有产物 | AI | 将每个文件归类到 OR/SR/BA/SysReq/PA 中对应该层结构的类型。注意：现有产物并非按五层结构组织，分类是推导起点，并非最终归属 |
| 3 | 识别产物类型 | AI | 标注每份产物的类型：规范定义 / 设计指南 / 操作模板 / 产品数据模板 / 工具脚本 / 其他 |
| 4 | 分析活动：初版架构评估 | AI | 需求说明符合性分析（产物覆盖度、盲区识别：哪些产物已在但未正式化）+ 需求性能符合性分析（从产物特征反推性能指标范围） |
| 5 | 汇总输出 | AI | 按模板生成产物总览清单 |

## 人类审核要点

- [ ] 产物清单是否完整？是否有遗漏的目录或文件？
- [ ] 覆盖盲区的判断是否准确？
- [ ] 分类是否合理——某产物是否应该归到不同的架构层级？
- [ ] 功能模块分类与 PA 组件候选的对应关系是否合理
- [ ] 关键技术决策记录是否完整

## AI 模板

详见 `03-pipeline-system-design-ai-support/02-reverse-engineering-pipeline-system-design/workflow-prompts.md` 第1步"现有产物梳理与架构分析"。

## 质量门禁

- [ ] 产物总览清单已生成
- [ ] 覆盖盲区已标记
- [ ] 架构层级分类已标注
- [ ] 初版架构评估已执行
- [ ] 人类开发者已审核确认清单完整性
- [ ] 按审查修复流程处理问题

## 产出

| 文件 | 说明 |
|------|------|
| 产物总览清单（产物分类 + 架构层级映射） | 本文件（产物清单定义 + 架构层级映射） |
