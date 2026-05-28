# task-04：业务架构推导

**对应场景**：02-reverse-engineering · 第4步
**对应 AI 模板**：`03-eos-pipeline-system-design-ai-support/02-reverse-engineering-eos-pipeline-system-design/workflow-prompts.md` 第4步

---

## 目标

从 SysReq 9 级场景活动反推业务架构 IPO，建立 BA 定义和去重机制。

## 上下文继承

```
从哪里来：
  - 第3步产出：系统需求文档（功能部分 + 非功能部分）
  - 第3步同步建立的业务架构骨架
  - 第3步决策记录

去哪里：
  - 本步产出 → 第5步（SR 反向推导）的 BA IPO 输入
  - 同步产出 → 相关方需求骨架（供第5步使用）
```

---

## 输入

| 输入 | 说明 |
|------|------|
| SysReq 详细定义 | task-03 产出 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 分析活动：SysReq→BA 追溯验证 | AI | 需求说明符合性分析（从 SysReq 5 级节点是否能推导出合理的 IPO）+ 需求性能符合性分析（业务层指标是否覆盖 SysReq 要求） |
| 2 | 从 SysReq 9 级反推 BA IPO | AI | 每个 9 级活动所需的一个业务步骤 |
| 3 | IPO 定义 | AI | 每个 IPO 定义 I/P/O |
| 4 | IPO 三级去重 | AI | 复用→改进→新增 |
| 5 | 同步建立相关方需求骨架 | AI | 为每个 BA IPO 创建 SR 架构末级节点占位符，建立骨架映射（为第5步做准备） |
| 6 | 建立 BA → SysReq 映射 | AI | 追溯关系表 |
| 7 | 结果审核 | 人类 | 确认 IPO 定义和去重合理性 |

## 人类审核要点

- [ ] IPO 的业务语义是否正确
- [ ] IPO 去重是否合理
- [ ] IPO 名称是否使用"动词+名词"结构
- [ ] IPO 的 Input/Process/Output 三维定义是否完整
- [ ] 去重后的 IPO 清单是否覆盖所有 SysReq 节点
- [ ] 相关方需求骨架是否已同步建立

## 质量门禁

- [ ] SysReq→BA 追溯验证已执行
- [ ] BA IPO 定义完整
- [ ] IPO 去重完成（去重前后数量对比已记录）
- [ ] BA → SysReq 映射关系建立
- [ ] 相关方需求骨架已同步建立（为第5步提供输入）
- [ ] 运行 rule-conformance-review 进行符合性审查
- [ ] 按审查修复流程处理问题

## 产出

| 文件 | 说明 |
|------|------|
| 业务架构定义子文档 | `10-eos-pipeline-system-product-data/04-business-architecture.md` |
