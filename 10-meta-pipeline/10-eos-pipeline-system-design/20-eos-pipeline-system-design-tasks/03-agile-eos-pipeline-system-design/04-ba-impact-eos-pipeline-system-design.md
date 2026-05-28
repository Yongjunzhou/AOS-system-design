# task-04：业务架构影响分析

**对应场景**：03-agile · 第4步
**对应 AI 模板**：`03-eos-pipeline-system-design-ai-support/03-agile-eos-pipeline-system-design/workflow-prompts.md` 第4步

---

## 目标

分析新需求对业务架构的影响，输出 BA 增量定义。

## 上下文继承

```
从哪里来：
  - task-03 产出：SR 增量定义
  - 参考基线：现有 BA 文档（IPO 清单 + 映射关系表）

去哪里：
  - 本步产出 → task-05（SysReq 影响分析）的 BA 增量定义
  - 同步产出 → BA → SysReq 骨架映射（为 task-05 提供输入）
```

---

## 输入

| 输入 | 说明 |
|------|------|
| SR 增量定义 | task-03 产出 |
| 现有 BA 文档（基线） | 基线中的 BA 层 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 分析活动：BA 影响分析 | AI | 需求说明符合性分析（新 SR 详细定义末级是否能由现有业务组件承接）+ 需求性能符合性分析（性能指标是否从 SR 正确继承） |
| 2 | IPO 去重检查 | AI | 三级去重 |
| 3 | BA 增量条目定义 | AI | 增量标记 |
| 4 | 同步设计 SysReq 骨架 | AI | BA → SysReq 骨架映射 |
| 5 | 结果审核 | 人类 | 确认 IPO 定义 |

## 人类审核要点

- [ ] BA IPO 业务语义是否正确
- [ ] IPO 去重是否合理
- [ ] IPO 的 Input/Process/Output 三维定义是否完整
- [ ] SysReq 骨架是否已同步建立

## 质量门禁

- [ ] 分析活动：BA 影响分析已执行
- [ ] BA 增量定义完成
- [ ] IPO 去重完成
- [ ] BA → SysReq 骨架映射已更新
- [ ] 运行 rule-conformance-review 进行符合性审查
- [ ] 按审查修复流程处理问题

## 产出

| 文件 | 说明 |
|------|------|
| 更新后的 BA 文档 | `10-eos-pipeline-system-product-data/04-business-architecture.md` |
