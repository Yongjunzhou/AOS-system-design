# task-02：相关方需求功能部分详细定义及业务架构定义

**对应场景**：01-waterfall · 第2步
**对应 AI 模板**：`03-pipeline-system-design-ai-support/01-pipeline-system-design-waterfall/workflow-prompts.md` 第2步

---

## 目标

沿功能分支推进，对 SR 架构末级节点进行详细定义分解，同步设计业务架构 IPO。

## 输入

| 输入 | 说明 |
|------|------|
| SR 架构定义（功能部分 SR-F） | task-01 产出 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 分析活动：架构定义验证 | AI | 检查映射完整性、性能指标量化 |
| 2 | SR 功能部分详细定义 | AI | 分解到每条末级只需映射到一个 BA IPO |
| 3 | 业务架构 IPO 定义 | AI | 为每个 IPO 定义 I/P/O，执行三级去重 |
| 4 | 同步建立 SysReq 架构骨架 | AI | 每个去重后 IPO 建立 SysReq 5 级节点占位符 |
| 5 | 结果审核 | 人类 | 审核 IPO 的业务语义正确性 |

## 人类审核要点

- [ ] BA IPO 的业务语义是否正确——需业务人员/领域专家审核
- [ ] IPO 去重是否合理
- [ ] 架构骨架映射关系是否准确

## 质量门禁

- [ ] SR 详细定义末级已分解到可映射粒度
- [ ] BA IPO 定义完整（I/P/O）
- [ ] SysReq 架构骨架已同步建立
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 相关方需求详细定义文档 | `10-pipeline-system-product-data/03-stakeholder-requirements-detailed.md` |
| 业务架构定义文档 | `10-pipeline-system-product-data/04-business-architecture.md` |
