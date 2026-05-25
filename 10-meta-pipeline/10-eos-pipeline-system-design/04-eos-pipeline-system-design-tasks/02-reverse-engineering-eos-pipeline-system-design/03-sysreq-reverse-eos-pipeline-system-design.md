# task-03：系统需求推导

**对应场景**：02-reverse-engineering · 第3步
**对应 AI 模板**：`03-eos-pipeline-system-design-ai-support/02-reverse-engineering-eos-pipeline-system-design/workflow-prompts.md` 第3步
**对应设计指南**：[逆向工程系统设计指南 第3步](../../02-eos-pipeline-system-design-guidelines/02-reverse-engineering-eos-pipeline-system-design-guide.md#第3步系统需求反向推导)

---

## 目标

从 PA 组件反向推导系统需求。先从组件职责反推 SysReq 9 级场景活动，再从 9 级聚合为 5 级架构。

## 上下文继承

```
从哪里来：
  - 第2步产出：产品架构定义文档（PA 组件定义 + 树形结构）
  - 第2步决策记录
  - 现有设计文档和模板（作为推导参考）

去哪里：
  - 本步产出 → 第4步（BA 反向推导）的 SysReq 输入
  - 同步产出 → 业务架构 5 级骨架（供第4步使用）
```

---

## 输入

| 输入 | 说明 |
|------|------|
| PA 架构定义 | task-02 产出 |
| 现有设计文档和模板 | 产物原始内容（作为推导参考） |

## 操作流程

| # | 操作 | 执行者 | 说明 |
|---|------|--------|------|
| 1 | 分析活动：PA→SysReq 追溯验证 | AI | 需求说明符合性分析（每个 PA 组件是否能反推合理的 SysReq 场景活动）+ 需求性能符合性分析（从组件实现特征反推 SysReq 性能指标） |
| 2 | 反推 SysReq 9 级场景活动 | AI | 组件需要什么系统场景活动来支撑其功能 |
| 3 | 聚合 9 级为 5 级架构 | AI | 按 0-9 级层级结构组织 |
| 4 | 非功能需求推导 | AI | 从组件约束反推 SysReq-NFR |
| 5 | 建立 SysReq → PA 映射关系 | AI | 追溯关系表 |
| 6 | 同步建立业务架构骨架 | AI | 为每个 SysReq 5 级节点创建 BA IPO 候选占位符，建立骨架映射（为第4步做准备） |
| 7 | 结果审核 | 人类 | 确认推导的合理性 |

## 人类审核要点

- [ ] 推导的 SysReq 是否准确反映了组件的实际需求
- [ ] 9 级场景活动是否完整覆盖了组件功能
- [ ] 非功能需求量化指标是否合理
- [ ] 功能与非功能分支的分离是否正确
- [ ] 业务架构骨架是否已同步建立
- [ ] 推导有效性评级分布是否合理

## 质量门禁

- [ ] PA→SysReq 追溯验证已执行
- [ ] SysReq 9 级场景活动推导完成
- [ ] 功能架构 0-9 级组织完成
- [ ] 非功能架构 0-6 级定义完成
- [ ] SysReq → PA 映射关系建立
- [ ] 业务架构骨架已同步建立
- [ ] 推导有效性评级已标注
- [ ] 运行 rule-conformance-review 进行符合性审查
- [ ] 按审查修复流程处理问题

## 产出

| 文件 | 说明 |
|------|------|
| 系统需求架构定义 + 详细定义 | `10-eos-pipeline-system-product-data/05-system-requirements-architecture.md` + `06-system-requirements-detailed.md` |
