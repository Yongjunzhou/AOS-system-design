# task-04：业务架构推导

**对应场景**：02-reverse-engineering · 第4步
**对应 AI 模板**：`03-pipeline-system-design-ai-support/03-pipeline-system-design-reverse-engineering/workflow-prompts.md` 第4步

---

## 目标

从 SysReq 9 级场景活动反推业务架构 IPO，建立 BA 定义和去重机制。

## 输入

| 输入 | 说明 |
|------|------|
| SysReq 详细定义 | task-03 产出 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 从 SysReq 9 级反推 BA IPO | AI | 每个 9 级活动所需的一个业务步骤 |
| 2 | IPO 定义 | AI | 每个 IPO 定义 I/P/O |
| 3 | IPO 三级去重 | AI | 复用→改进→新增 |
| 4 | 建立 BA → SysReq 映射 | AI | 追溯关系表 |
| 5 | 结果审核 | 人类 | 确认 IPO 定义和去重合理性 |

## 人类审核要点

- [ ] IPO 的业务语义是否正确
- [ ] IPO 去重是否合理
- [ ] IPO 名称是否使用"动词+名词"结构

## 质量门禁

- [ ] BA IPO 定义完整
- [ ] IPO 去重完成
- [ ] BA → SysReq 映射关系建立
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 业务架构定义文档 | `10-pipeline-system-product-data/04-business-architecture.md` |
