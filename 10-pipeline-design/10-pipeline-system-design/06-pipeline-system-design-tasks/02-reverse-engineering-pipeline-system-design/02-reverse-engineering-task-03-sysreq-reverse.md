# task-03：系统需求推导

**对应场景**：02-reverse-engineering · 第3步
**对应 AI 模板**：`03-pipeline-system-design-ai-support/03-pipeline-system-design-reverse-engineering/workflow-prompts.md` 第3步

---

## 目标

从 PA 组件反向推导系统需求。先从组件职责反推 SysReq 9 级场景活动，再从 9 级聚合为 5 级架构。

## 输入

| 输入 | 说明 |
|------|------|
| PA 架构定义 | task-02 产出 |
| 现有设计文档和模板 | 产物原始内容（作为推导参考） |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 分析 PA 组件职责 | AI | 每个组件的业务功能是什么 |
| 2 | 反推 SysReq 9 级场景活动 | AI | 组件需要什么系统场景活动来支撑其功能 |
| 3 | 聚合 9 级为 5 级架构 | AI | 按 0-9 级层级结构组织 |
| 4 | 非功能需求推导 | AI | 从组件约束反推 SysReq-NFR |
| 5 | 建立 SysReq → PA 映射关系 | AI | 追溯关系表 |
| 6 | 结果审核 | 人类 | 确认推导的合理性 |

## 人类审核要点

- [ ] 推导的 SysReq 是否准确反映了组件的实际需求
- [ ] 9 级场景活动是否完整覆盖了组件功能
- [ ] 非功能需求量化指标是否合理

## 质量门禁

- [ ] SysReq 9 级场景活动推导完成
- [ ] 功能架构 0-9 级组织完成
- [ ] 非功能架构 0-6 级定义完成
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 系统需求架构定义 + 详细定义 | `10-pipeline-system-product-data/05-system-requirements-architecture.md` + `06-system-requirements-detailed.md` |
