---
name: pending-or-table-c-authority
description: 待决——规范化的相关方需求基线条目状态表（表C）该由状态文档承载还是转为需求文档内嵌
metadata: 
  node_type: memory
  type: project
  originSessionId: 5ff7b330-61c6-4f82-a69e-77b676f52e87
  modified: 2026-09-19T13:15:50.427Z
---

**待决**，2026-09-19 自 `.Codex/memory/` 迁入本目录并核校。

## 问题

「表C — 规范化的相关方需求基线条目处理进度」现落在状态文档
`20-pl4eos/80-pl4eos-2-eosdata/00-origin-requirement-materials/01-eos-sysdev-status.md`。
待决的是：是否反转为由需求文档
`20-pl4eos/80-pl4eos-2-eosdata/01-eos-specified-requirements.md` 内嵌承载，
状态文档只留汇总视图。

## 支持反转的理由

条目正文、反馈、分析建议都落在需求文档；`ort03`／`wft01`／`wft06` 消费表C 时同时要读条目本体。
「状态跟着对象走、状态文档做汇总视图」的规则与其他对象一致。

## 未执行的原因

原记「本轮上下文用量不足，不宜做高影响改造，避免出现两边都像权威源的过渡状态」。

## 迁入核校结论

原记引用的 `20-pl4eos/80-pl4eos-2-eosdata/01-eos-original-requirements.md` 已更名为
`01-eos-specified-requirements.md`（v3.2），且其中**并无表C**——原记「需求文档中的表C为派生视图」
的前提已不成立。启动前须重新判定该问题是否仍然存在。

相关：[[or-baseline-single-zone-state-machine]]、[[or-baseline-management-zone-simplification]]
