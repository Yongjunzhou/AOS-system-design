# task-03：系统需求逆向推导

**对应场景**：02-reverse-engineering · 第3步
**对应 AI 模板**：`03-aos-system-design-ai-support/02-reverse-engineering-aos-system-design/workflow-prompts.md` 第3步
**对应设计指南**：[AOS 逆向工程系统设计指南 第3步](../../02-aos-system-design-guidelines/02-reverse-engineering-aos-system-design-guide.md#第3步系统需求反向推导)

---

## 目标

从 PA 组件反向推导系统需求，建立 SysReq 架构。

## 上下文继承

```
来源：第2步产出
产出：SysReq 架构定义（含 PA→SysReq 追溯映射表）
```

## 输入

| 输入 | 说明 |
|------|------|
| PA 架构定义 | task-02 产出 |
| 现有设计文档（含需求类文档） | 仓库中已有的需求描述 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 分析活动：PA→SysReq 追溯验证 | 人类+AI | 两类分析：(1) PA 组件职责分析——对每个 PA 组件反向追溯其满足的系统需求；(2) SysReq 场景完整性分析——评估反向推导出的系统场景是否覆盖了 PA 组件的全部职责 |
| 2 | 同步建立业务架构骨架 | AI | 在推导 SysReq 的同时，标记各场景活动所属的业务域，为后续 BA 反向推导建立骨架 |
| 3 | 组织 0-9 级层级结构 | AI | 将 9 级场景活动向上归并为 5 级节点 → 功能模块 → 系统功能 |
| 4 | 非功能约束整理 | AI | 从已有文档提取非功能需求，按 0-6 级组织 |
| 5 | 结果审核 | 人类 | 确认推导的合理性 |

## 人类审核要点

- [ ] SysReq 推导逻辑是否合理
- [ ] PA → SysReq 的映射是否准确
- [ ] 非功能约束是否有遗漏
- [ ] 同步建立的 BA 骨架是否合理——业务域划分是否能支撑后续 BA 反向推导
- [ ] SysReq 场景是否完整覆盖了 PA 组件的所有功能职责

## 质量门禁

- [ ] SysReq 架构定义完成（功能 + 非功能）
- [ ] PA → SysReq 映射关系建立且双向可追溯
- [ ] 业务架构骨架已同步建立并记录
- [ ] SysReq 场景活动无遗漏——每个 PA 组件至少映射到一个 SysReq 场景
- [ ] 运行 conformance-review 进行符合性审查
- [ ] 已按审查修复流程处理发现的问题

## 产出

| 文件 | 说明 |
|------|------|
| 系统需求架构定义 | `10-aos-system-product-data/05-system-requirements-architecture.md` |
