---
name: design-split-pattern
description: 瀑布式系统设计 Skill 的"设计开发+资产维护"两阶段分离模式（v0.2 扩展）
metadata:
  type: project
---

所有 wft skill 统一拆分为"设计开发（Phase 1）"和"资产维护（Phase 2 上半）"和"详细定义展开（Phase 2 下半）"三个阶段，中间以两道人类审阅为门禁。

**Why:** "基于资产的设计"不应只是文档中的原则，而应通过流程结构强制体现——不走完资产匹配阶段，方案卡在 `待资产落账` 进不了下一站。另外，"详细定义由消费方产出"规律要求 Phase 2 下半展开当前层的详细条目。

**How to apply:**
- Phase 1 产出写入目标资产文档，状态=待确认方案（人类在资产文档上下文中审阅）
- Phase 2 上半 Q1/Q2/Q3 是**跨域资产归并**，补偿分区加载的盲区，非设计重审
- Phase 2 下半展开详细定义，入第二次人类门禁
- 详细定义由**消费方**产出，非生产方（wft02 产出 STR 详细定义，wft05 产出 SR 详细定义）
- 大文档（如 07-*.md）需内部分区支持按需加载，见通用规范 §3.9 和 EOS 流水线规范 §4.6

**Key design decisions from discussion (2026-06-17):**
- Phase 1 提案 **写入** 07-*.md（不另设提案暂存文件），状态=待确认方案区分提案/资产
- Phase 2 Q1/Q2/Q3 是跨域归并补偿（因为按域分区导致 Phase 1 看不到其他域的资产）
- 人类在 Phase 1 后需两件事：选材（05 状态表）+ 审阅（07 反馈区）
- Phase 2 上半机械执行不需要人类审阅

**试点建议:** wft05，详细方案见 [90-design-split-pattern.md](../../20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/90-design-split-pattern.md)
