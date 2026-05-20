# task-04：业务架构逆向推导

**对应场景**：02-reverse-engineering · 第4步
**对应 AI 模板**：`03-aos-system-design-ai-support/02-reverse-engineering-aos-system-design/workflow-prompts.md` 第4步

---

## 目标

从 SysReq 反向推导业务架构 IPO，建立 BA 定义。

## 输入

| 输入 | 说明 |
|------|------|
| SysReq 架构定义 | task-03 产出 |
| 现有业务描述文档 | 仓库中已有的业务过程描述 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 从 SysReq 5 级节点反向推导 BA IPO | AI | 每个系统功能 → 反向追溯对应的业务活动 |
| 2 | IPO 定义推导 | AI | 为每个 IPO 推导 I/P/O 定义 |
| 3 | 去重处理 | AI | 识别推导结果中的重复 IPO |
| 4 | 结果审核 | 人类 | 确认推导的合理性 |

## 人类审核要点

- [ ] BA IPO 的业务语义是否正确
- [ ] SysReq → BA 的推导逻辑是否合理
- [ ] 是否有遗漏的业务过程

## 质量门禁

- [ ] BA IPO 定义完整（I/P/O）
- [ ] SysReq → BA 映射关系建立
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 业务架构定义文档 | `10-aos-system-product-data/04-business-architecture.md` |
