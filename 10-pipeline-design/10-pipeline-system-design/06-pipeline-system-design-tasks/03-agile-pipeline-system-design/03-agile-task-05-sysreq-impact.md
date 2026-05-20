# task-05：系统需求影响分析

**对应场景**：03-agile · 第5步
**对应 AI 模板**：`03-pipeline-system-design-ai-support/02-pipeline-system-design-agile/workflow-prompts.md` 第5步

---

## 目标

分析新需求对系统需求的影响，输出 SysReq 增量定义（同时处理功能和非功能分支）。

## 输入

| 输入 | 说明 |
|------|------|
| BA 增量定义 | task-04 产出 |
| 现有 SysReq 文档（基线） | 基线中的 SysReq 层 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | SysReq 影响分析 | AI | 功能和非功能分支分别分析 |
| 2 | SysReq 功能增量定义 | AI | 0-9 级架构增量 + 9 级场景活动 |
| 3 | SysReq 非功能增量定义 | AI | 0-6 级架构增量 |
| 4 | 同步设计 PA 骨架 | AI | SysReq → PA 骨架映射 |
| 5 | 结果审核 | 人类 | 确认 SysReq 更新 |

## 人类审核要点

- [ ] 功能分支增量与 BA 一致性
- [ ] 非功能指标量化是否合理

## 质量门禁

- [ ] SysReq 增量定义完成（功能 + 非功能）
- [ ] SysReq → PA 骨架映射已更新
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 更新后的 SysReq 文档 | `10-pipeline-system-product-data/05-*.md` + `06-*.md` |
