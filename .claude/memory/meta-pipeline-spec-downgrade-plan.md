---
name: meta-pipeline-spec-downgrade-plan
description: 计划将 01-pl4pleos-spec-sysdev.md 从完整规范降级为方法论说明+工程导航
metadata:
  type: project
---

# 元流水线规范降级计划

**提出日期**：2026-06-02
**状态**：待实施

## 问题

元流水线（A1）和 EOS 流水线（A2）同为"流水线类×AI SKILL"，套用同一套规范模板导致
`01-pl4pleos-spec-sysdev.md`（1178 行）实质上是 A2 规范的复制品，独立维护意义不大。

## 方案

将 `10-pl4pleos/00-pl4pleos-spec/01-pl4pleos-spec-sysdev.md` 从"完整系统设计规范"
降级为一份简短的方法论说明 + 工程导航文档，包含：

1. 元流水线概念解释（三层构造链顶层）
2. A1→A2→A3→B 产品链关系
3. 工程阅读导航：通用规范 → A2 规范 → A3 规范
4. 当前建设状态

目录结构保留不变，但不把 A1 当作需要独立维护系统设计规范的产品。

## 关联记忆

- [[two-tier-isomorphic-structure]]
- [[delivery-framework-two-types]]
