# task-07：验证

**对应场景**：02-reverse-engineering · 第7步
**对应 AI 模板**：`03-aos-system-design-ai-support/02-reverse-engineering-aos-system-design/workflow-prompts.md` 第7步

---

## 目标

验证完整逆向推导后各层之间的追溯链，输出验证报告。

## 输入

| 输入 | 说明 |
|------|------|
| 全部设计文档（OR → SR → BA → SysReq → PA） | task-01 ~ task-06 的全部产出 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 1:1 分配约束验证 | AI | 逐层检查每条详细定义末级的映射 |
| 2 | N:1 承接支持验证 | AI | 检查各层节点的承接数量合理性 |
| 3 | 双向追溯验证 | AI | OR → PA 和 PA → OR |
| 4 | 反向推导一致性验证 | AI | 逆向推导的上下游内容是否一致 |
| 5 | 生成追溯矩阵 | AI | 端到端映射关系表 |
| 6 | 生成验证报告 | AI | 含问题清单和建议 |

## 人类审核要点

- [ ] 验证报告中的未通过项
- [ ] 逆向推导后的设计是否自洽
- [ ] 是否存在"推导矛盾"——上层推导的结果和下层推导的结果不一致

## 质量门禁

- [ ] 1:1 约束通过率 100%
- [ ] 反向推导一致性通过
- [ ] 验证报告已生成
- [ ] **运行 conformance-review 进行完整符合性审查**（建立基线前的关键门禁）

## 产出

| 文件 | 说明 |
|------|------|
| 追溯矩阵 | `10-aos-system-product-data/08-traceability-matrix.md` |
| 验证报告 | `10-aos-system-product-data/09-verification-report.md` |
