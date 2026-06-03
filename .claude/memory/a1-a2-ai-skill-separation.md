---
name: a1-a2-ai-skill-separation
description: A1 与 A2 虽同为 AI Skill 产品且设计流程相同，但 AI SKILL 必须显性化为两套，分别承载各自的产品形态知识
metadata:
  type: project
---

# A1/A2 AI SKILL 分离决策

**确认日期**：2026-06-03

## 决策

A1（元流水线）和 A2（EOS 流水线）虽然同为"流水线类×AI Skill"产品，系统设计流程（OR→SR→BA→SysReq→PA）和 Skill 结构完全一致，但 AI SKILL **必须显性化为两套**：

| 维度 | A1 的 AI SKILL | A2 的 AI SKILL |
|------|---------------|---------------|
| 设计输出产品 | A2（EOS 流水线，AI Skill 产品） | A3（EOS，软件产品） |
| BA 锚定目标 | 输出产品=A2 → Skill 节点类型 | 输出产品=A3 → 引擎/配置节点类型 |
| PA 划分规则 | 三因素矩阵实例化为 AI Skill 产品 | 三因素矩阵实例化为 软件产品 |
| 产品语境知识 | 关于"如何设计 EOS 流水线" | 关于"EOS 应支持什么业务" |

## 原因

AI SKILL 内部固有的判断逻辑需要知道目标产品的形态才能做决策。若封装为同一套 SKILL 内部的条件分支，虽然可行但会降低显式性和可维护性。两套 SKILL 各自承载自己的产品形态知识，表述更清晰。

## 推论

- A1 和 A2 的设计线架构图相同（同为五层派生 + 四种设计模式），但每个 Skill 节点内的**规则内容**不同
- 通用设计规范作为方法论基础，不承担产品形态差异
- 产品形态差异由 A1 规范和 A2 规范分别定义，其 AI SKILL 各自实例化

## 相关记忆
- [[pl4eos-spec-mission]]
- [[delivery-framework-two-types]]
