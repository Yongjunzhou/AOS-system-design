# task-04：业务架构影响分析

**对应场景**：03-agile · 第4步
**对应 AI 模板**：`03-pipeline-system-design-ai-support/02-pipeline-system-design-agile/workflow-prompts.md` 第4步

---

## 目标

分析新需求对业务架构的影响，输出 BA 增量定义。

## 输入

| 输入 | 说明 |
|------|------|
| SR 增量定义 | task-03 产出 |
| 现有 BA 文档（基线） | 基线中的 BA 层 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | BA 影响分析 | AI | 更新策略决策（映射/修改/新建） |
| 2 | IPO 去重检查 | AI | 三级去重 |
| 3 | BA 增量条目定义 | AI | 增量标记 |
| 4 | 同步设计 SysReq 骨架 | AI | BA → SysReq 骨架映射 |
| 5 | 结果审核 | 人类 | 确认 IPO 定义 |

## 人类审核要点

- [ ] BA IPO 业务语义是否正确
- [ ] IPO 去重是否合理

## 质量门禁

- [ ] BA 增量定义完成
- [ ] BA → SysReq 骨架映射已更新
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 更新后的 BA 文档 | `10-pipeline-system-product-data/04-business-architecture.md` |
