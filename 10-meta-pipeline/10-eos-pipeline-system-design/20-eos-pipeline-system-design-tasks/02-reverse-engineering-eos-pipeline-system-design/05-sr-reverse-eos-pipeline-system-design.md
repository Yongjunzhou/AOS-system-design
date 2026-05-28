# task-05：相关方需求推导

**对应场景**：02-reverse-engineering · 第5步
**对应 AI 模板**：`03-eos-pipeline-system-design-ai-support/02-reverse-engineering-eos-pipeline-system-design/workflow-prompts.md` 第5步

---

## 目标

从 BA IPO 反向推导相关方需求（SR），包括架构定义和详细定义。

## 上下文继承

```
从哪里来：
  - 第4步产出：业务架构文档（IPO 清单 + 去重报告）
  - 第4步同步建立的相关方需求骨架
  - 第4步决策记录

去哪里：
  - 本步产出 → 第6步（OR 反向推导）的 SR 输入
  - 非功能部分从 SysReq-NFR 反推（不经过 BA 层）
```

---

## 输入

| 输入 | 说明 |
|------|------|
| BA 架构定义 | task-04 产出 |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 分析活动：BA→SR 追溯验证 | AI | 需求说明符合性分析（从 BA IPO 能否反推清晰的相关方需求描述）+ 需求性能符合性分析（SR 层指标是否覆盖 BA 要求） |
| 2 | 从 BA IPO 聚合 SR-F 架构末级节点 | AI | 功能部分从 BA IPO 反推，按 SR-F 分类聚合 |
| 3 | SR 架构定义 | AI | 树形结构 + 映射关系表 |
| 4 | SR 详细定义分解 | AI | 每个 SR 架构末级节点分解到详细定义末级 |
| 5 | 非功能部分推导（SR-NFR） | AI | 从 SysReq-NFR 反推 SR-NFR（独立于功能分支并行） |
| 6 | 建立 SR → BA 映射 | AI | 追溯关系表 |
| 7 | 结果审核 | 人类 | 确认 SR 推导的合理性 |

## 人类审核要点

- [ ] SR 架构是否准确反映了业务需求
- [ ] 功能与非功能需求的分离是否正确
- [ ] 功能部分和非功能部分的服务对象定义是否清晰
- [ ] SR 详细定义末级是否满足 1:1 约束
- [ ] 从 BA IPO 聚合的 SR 是否保持了自然的业务语义
- [ ] SR-NFR 的量化指标是否合理

## 质量门禁

- [ ] BA→SR 追溯验证已执行
- [ ] SR 架构定义完成（功能 + 非功能）
- [ ] SR 详细定义分解完成
- [ ] 功能部分和非功能部分分离完成
- [ ] SR-F 和 SR-NFR 各架构末级节点编号已分配
- [ ] SR → BA 映射关系建立
- [ ] 运行 rule-conformance-review 进行符合性审查
- [ ] 按审查修复流程处理问题

## 产出

| 文件 | 说明 |
|------|------|
| 相关方需求架构定义 | `10-eos-pipeline-system-product-data/02-stakeholder-requirements-architecture.md` |
| 相关方需求详细定义 | `10-eos-pipeline-system-product-data/03-stakeholder-requirements-detailed.md` |
