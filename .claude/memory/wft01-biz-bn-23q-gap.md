---
name: wft01-biz-bn-23q-gap
description: 2026-06-30 发现 wft01-biz 缺少 Bn 侧 23-Q 判定——STR-F 只携带 A2 侧产品类型/构件类型，导致 wft02-biz Phase B 缺少 PL2/PL3 现成信息
metadata:
  type: project
---

## 问题

wft01-biz 的 23-Q 判定当前只产出 A2 侧的产品类型/构件类型，不产出 Bn 侧的 PL2（E2E 项目业务）和 PL3（构件类型）。

**证据链**：
- legacy `wft01b-or2str-settle.md` Step F-1 从 STR-F 读取"23 产品类型/构件类型"——legacy wft01a 在 23-Q 时同时判定了 A2 和 Bn 两侧
- legacy `wft02a-str2ba-design.md` §3A.1 直接使用上游提供的业务域/产品类型/构件类型生成 Bn 路径
- 当前 wft02-biz Phase B §3.4·1 的 E2E 项目业务和构件类型两列为空白——Phase B 没有 OR 上下文，无法准确推导

## 方向

wft01-biz 补上 Bn 侧 23-Q 判定：对每个场景部件，除了当前的 A2 侧产品路径对齐外，同时判定它在 Bn 产品架构中的 E2E 项目业务和构件类型归属。

## 影响

- **wft01-biz**：§3.4 23-Q 判定规则扩展 Bn 侧，场景部件要素新增 Bn E2E 项目业务/构件类型字段
- **wft02-biz Phase B**：PL2（E2E 项目业务）和 PL3（构件类型）可从 STR-F 直接读取，只负责 PL4 WBS 归纳

## 关联记忆

- [[wft02-eng-align-to-biz-structure]]
- [[wft02-biz-v240-review-session]]
