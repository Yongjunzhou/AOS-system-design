---
name: design-split-pattern
description: 瀑布式系统设计 Skill 的"设计开发+资产维护"两阶段分离模式
metadata:
  type: project
---

所有 wft skill 统一拆分为"设计开发（Phase 1）"和"资产维护（Phase 2）"两个阶段，中间以人类审阅为门禁。

**Why:** "基于资产的设计"不应只是文档中的原则，而应通过流程结构强制体现——不走完资产匹配阶段，方案卡在 `待资产落账` 进不了下一站。

**How to apply:** 每个 skill 的 Phase 2 执行同构六步骤：资产环境加载→实体提取→资产匹配决策(Q1/Q2/Q3)→写回主资产→反向引用更新→状态推进。差异仅在具体资产文档和匹配逻辑上。详细方案见 [90-design-split-pattern.md](../../20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/90-design-split-pattern.md)

**试点建议:** wft05 资产维护空白最大（无 Q1/Q2/Q3 框架、无跨轮引用、无反向引用），最适合作为首个实施试点。
