# task-05：相关方需求推导

**对应场景**：02-reverse-engineering · 第5步
**对应 AI 模板**：`03-pipeline-system-design-ai-support/03-pipeline-system-design-reverse-engineering/workflow-prompts.md` 第5步

---

## 目标

从 BA IPO 反向推导相关方需求（SR），包括架构定义和详细定义。

## 输入

| 输入 | 说明 |
|------|------|
| BA 架构定义 | task-04 产出 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 从 BA IPO 聚合 SR 架构末级节点 | AI | 按 SR-F 和 SR-NFR 分类聚合 |
| 2 | SR 架构定义 | AI | 树形结构 + 映射关系表 |
| 3 | SR 详细定义分解 | AI | 每个 SR 架构末级节点分解到详细定义末级 |
| 4 | 建立 SR → BA 映射 | AI | 追溯关系表 |
| 5 | 结果审核 | 人类 | 确认 SR 推导的合理性 |

## 人类审核要点

- [ ] SR 架构是否准确反映了业务需求
- [ ] 功能与非功能需求的分离是否正确
- [ ] 功能部分和非功能部分的服务对象定义是否清晰

## 质量门禁

- [ ] SR 架构定义完成（功能 + 非功能）
- [ ] SR 详细定义分解完成
- [ ] SR → BA 映射关系建立
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 相关方需求架构定义 | `10-pipeline-system-product-data/02-stakeholder-requirements-architecture.md` |
| 相关方需求详细定义 | `10-pipeline-system-product-data/03-stakeholder-requirements-detailed.md` |
