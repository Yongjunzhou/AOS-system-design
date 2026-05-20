# task-03：系统需求逆向推导

**对应场景**：02-reverse-engineering · 第3步
**对应 AI 模板**：`03-aos-system-design-ai-support/02-reverse-engineering-aos-system-design/workflow-prompts.md` 第3步

---

## 目标

从 PA 组件反向推导系统需求，建立 SysReq 架构。

## 输入

| 输入 | 说明 |
|------|------|
| PA 架构定义 | task-02 产出 |
| 现有设计文档（含需求类文档） | 仓库中已有的需求描述 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 从 PA 组件推导 SysReq 9 级场景活动 | AI | 每个组件的功能描述 → 反向推导所需的场景活动 |
| 2 | 组织 0-9 级层级结构 | AI | 将 9 级场景活动向上归并为 5 级节点 → 功能模块 → 系统功能 |
| 3 | 非功能约束整理 | AI | 从已有文档提取非功能需求，按 0-6 级组织 |
| 4 | 结果审核 | 人类 | 确认推导的合理性 |

## 人类审核要点

- [ ] SysReq 推导逻辑是否合理
- [ ] PA → SysReq 的映射是否准确
- [ ] 非功能约束是否有遗漏

## 质量门禁

- [ ] SysReq 架构定义完成（功能 + 非功能）
- [ ] PA → SysReq 映射关系建立
- [ ] 运行 conformance-review 进行符合性审查

## 产出

| 文件 | 说明 |
|------|------|
| 系统需求架构定义 | `10-aos-system-product-data/05-system-requirements-architecture.md` |
