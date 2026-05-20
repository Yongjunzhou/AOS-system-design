# task-06：双向追溯验证

**对应场景**：01-waterfall · 第6步
**对应 AI 模板**：`03-aos-system-design-ai-support/01-waterfall-aos-system-design/workflow-prompts.md` 第6步

---

## 目标

验证从 OR 到 PA 的完整追溯链路，输出追溯矩阵和验证报告。

## 输入

| 输入 | 说明 |
|------|------|
| 全部设计文档 | task-01 ~ task-05 的全部产出 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 1:1 分配约束验证 | AI | 逐层检查：OR→SR→BA→SysReq→PA |
| 2 | N:1 承接支持验证 | AI | 检查每个节点的承接数量和合理性 |
| 3 | 双向追溯验证 | AI | 正向 OR→PA 和反向 PA→OR |
| 4 | 生成追溯矩阵 | AI | 端到端映射关系表 |
| 5 | 生成验证报告 | AI | 含问题清单和建议措施 |
| 6 | 结果审核 | 人类 | 确认验证结论 |

## 人类审核要点

- [ ] 验证报告中的未通过项和待确认项
- [ ] 追溯链路是否存在断点

## 质量门禁

- [ ] 1:1 约束通过率 100%
- [ ] N:1 承接合理性通过
- [ ] 双向追溯完整率通过
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 追溯矩阵 | `10-aos-system-product-data/08-traceability-matrix.md` |
| 验证报告 | `10-aos-system-product-data/09-verification-report.md` |
