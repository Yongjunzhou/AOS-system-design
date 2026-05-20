# task-04：业务架构影响分析

**对应场景**：03-agile · 第4步
**对应 AI 模板**：`03-aos-system-design-ai-support/03-agile-aos-system-design/workflow-prompts.md` 第4步

---

## 目标

将 SR 增量映射到业务架构，更新 BA IPO 定义。

## 输入

| 输入 | 说明 |
|------|------|
| SR 增量定义 | task-03 产出 |
| 现有 BA 文档（基线） | 基线中的 BA 层 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | BA 影响分析 | AI | 判断新增 IPO / 修改现有 IPO / 淘汰 IPO |
| 2 | IPO 增量定义 | AI | 新增 IPO 定义 I/P/O，修改 IPO 标注变化 |
| 3 | 更新映射关系表 | AI | SR → BA 映射 |
| 4 | 结果审核 | 人类 | 确认 BA 更新 |

## 人类审核要点

- [ ] IPO 变化决策（新增/修改/淘汰）— 需确认
- [ ] IPO 去重是否已执行

## 质量门禁

- [ ] BA 增量定义完成
- [ ] 映射关系表已更新
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 更新后的 BA 文档 | `10-aos-system-product-data/04-business-architecture.md` |
