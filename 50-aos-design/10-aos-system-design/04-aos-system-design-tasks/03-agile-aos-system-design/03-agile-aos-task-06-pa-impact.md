# task-06：产品架构影响分析

**对应场景**：03-agile · 第6步
**对应 AI 模板**：`03-aos-system-design-ai-support/03-agile-aos-system-design/workflow-prompts.md` 第6步

---

## 目标

将 SysReq 增量映射到产品架构，更新 PA 构件定义。

## 输入

| 输入 | 说明 |
|------|------|
| SysReq 增量定义 | task-05 产出 |
| 现有 PA 文档（基线） | 基线中的 PA 层 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | PA 影响分析 | AI | 判断新增组件/修改/淘汰 |
| 2 | PA 增量定义 | AI | 更新组件定义、映射关系 |
| 3 | 非功能约束影响的增量评估 | AI | 检查 NFR 变化是否影响 PA |
| 4 | 结果审核 | 人类 | 确认 PA 更新 |

## 人类审核要点

- [ ] 组件变更决策（新增/修改/淘汰）
- [ ] 非功能约束的 PA 影响评估

## 质量门禁

- [ ] PA 增量定义完成
- [ ] 映射关系表已更新
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 更新后的 PA 文档 | `10-aos-system-product-data/07-product-architecture.md` |
