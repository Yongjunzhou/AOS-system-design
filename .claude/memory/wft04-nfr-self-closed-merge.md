---
name: wft04-nfr-self-closed-merge
description: 2026-06-28 wft04-nfr 自闭环合并——wft04a+04b 合并为单一 Skill，全链路 Skill 均已自闭环
metadata:
  type: project
---

## 修改摘要

wft04a-nfr-design + wft04b-nfr-settle 合并为单一自闭环 Skill `eos-wft04-nfr.md` v2.0。至此，91 规范中所有 Skill 均已完成自闭环迁移，无 Skill 仍采用 A/B 模式。

### 合并要点

| 变化项 | A/B 模式（旧） | 自闭环模式（新） |
|--------|--------------|----------------|
| 文件数 | 2 个（04a + 04b） | 1 个（04-nfr） |
| 确认机制 | Gate 1 + Gate 2 两阶段 | 一次确认覆盖全部 |
| 并发控制 | 活动锁 + 单 ID 待办 | 版本标记 + 消费追溯 + A/B/C 选项 |
| 入口状态 | `待分解分配+同意分解分配` | `可以NFR设计` / `待补充NFR设计` |

### 保留的 NFR 特有内容

1. 链身份（平台链/业务链/共享）
2. 三大类归类（质量特性/环境适应性/可实现性）
3. 分层约束表（全局/业务域/IPO + 影响级别/影响点）——wft05 消费 NFR 的核心接口
4. 22 候选区匹配与写回（升级/新增）
5. 03 详细定义展开（14 字段）
6. L1 补齐规则（模糊指标处理）

### 记忆关联

- [[wft05-biz-engine-cu-requirement-redefinition]] — 同日 wft05-biz v3.0
