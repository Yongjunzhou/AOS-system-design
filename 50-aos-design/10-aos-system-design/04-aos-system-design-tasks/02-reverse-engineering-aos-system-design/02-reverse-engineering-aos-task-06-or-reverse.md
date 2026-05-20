# task-06：原始需求逆向推导

**对应场景**：02-reverse-engineering · 第6步
**对应 AI 模板**：`03-aos-system-design-ai-support/02-reverse-engineering-aos-system-design/workflow-prompts.md` 第6步

---

## 目标

从 SR 末级进一步验证和补全原始需求定义。

## 输入

| 输入 | 说明 |
|------|------|
| SR 架构定义 + 详细定义 | task-05 产出 |
| 原始需求原始表述 | 可用的原始需求资料 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | OR 末级补全 | AI | 基于 SR 末级完善 OR 末级清单 |
| 2 | 冲突检测 | AI | 检查 OR 末级之间的冲突和重复 |
| 3 | 映射关系验证 | AI | OR → SR 映射验证 |
| 4 | 结果审核 | 人类 | 确认 OR 完整性 |

## 人类审核要点

- [ ] OR 清单是否完整
- [ ] 冲突处理决策
- [ ] 是否有需要补充调研的原始需求

## 质量门禁

- [ ] OR 详细定义完整
- [ ] 冲突检测完成
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 原始需求详细定义 | `10-aos-system-product-data/01-original-requirements.md` |
