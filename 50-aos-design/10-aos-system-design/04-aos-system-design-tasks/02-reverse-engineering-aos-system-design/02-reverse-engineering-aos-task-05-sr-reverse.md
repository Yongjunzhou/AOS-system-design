# task-05：相关方需求逆向推导

**对应场景**：02-reverse-engineering · 第5步
**对应 AI 模板**：`03-aos-system-design-ai-support/02-reverse-engineering-aos-system-design/workflow-prompts.md` 第5步

---

## 目标

从 BA 反向推导相关方需求，建立 SR 架构定义和详细定义。

## 输入

| 输入 | 说明 |
|------|------|
| BA IPO 定义 | task-04 产出 |
| 现有相关方需求描述 | 仓库中已有的需求类文档 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 从 BA IPO 反向推导 SR-F 架构末级节点 | AI | 每个 IPO 的业务活动 → 反向推导用户对系统的功能需求 |
| 2 | SR-NFR 整理 | AI | 从非功能约束派生 SR-NFR |
| 3 | SR 详细定义推导 | AI | 为每个 SR 架构末级节点推导详细分解条目 |
| 4 | OR 反向推导 | AI | 从 SR 末级反向还原原始需求描述 |
| 5 | 结果审核 | 人类 | 确认推导的合理性 |

## 人类审核要点

- [ ] SR 推导是否准确反映了用户意图
- [ ] SR-NFR 是否有遗漏
- [ ] OR 还原是否合理

## 质量门禁

- [ ] SR 架构定义和详细定义完成
- [ ] BA → SR → OR 映射关系建立
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 相关方需求文档 | `10-aos-system-product-data/02-*.md` + `03-*.md` |
