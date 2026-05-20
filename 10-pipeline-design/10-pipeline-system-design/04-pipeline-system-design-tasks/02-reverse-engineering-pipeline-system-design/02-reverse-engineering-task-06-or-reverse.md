# task-06：原始需求推导

**对应场景**：02-reverse-engineering · 第6步
**对应 AI 模板**：`03-pipeline-system-design-ai-support/03-pipeline-system-design-reverse-engineering/workflow-prompts.md` 第6步

---

## 目标

从 SR 详细定义末级节点聚合为原始需求条目，建立完整的 OR → SR 追溯关系。

## 输入

| 输入 | 说明 |
|------|------|
| SR 架构定义 + 详细定义 | task-05 产出 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 从 SR 详细定义聚合 OR 条目 | AI | 按业务功能聚类合并为完整的需求描述 |
| 2 | 原始需求规范化 | AI | 四项检查、功能/非功能分离 |
| 3 | 原始需求末级分解 | AI | 按原子性原则分解 |
| 4 | 建立 OR → SR 映射 | AI | 追溯关系表 |
| 5 | 冲突和重复维护 | AI | 标记矛盾项 |
| 6 | 结果审核 | 人类 | 确认 OR 推导的合理性 |

## 人类审核要点

- [ ] 从 SR 聚合的 OR 是否合理——是否能回到原始的需求场景
- [ ] 优先级判定（P0-P3）— 需人工确认
- [ ] 冲突检测的最终决策

## 质量门禁

- [ ] OR 条目聚合完成（含末级分解）
- [ ] OR → SR 映射关系建立
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 原始需求文档 | `10-pipeline-system-product-data/01-original-requirements.md` |
