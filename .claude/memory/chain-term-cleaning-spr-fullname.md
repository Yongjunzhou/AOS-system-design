---
name: chain-term-cleaning-spr-fullname
description: 链级术语清扫（2026-08-27）——规范化需求→规范化的相关方需求（术语全称化），55 文件，spr 缩写零迁移
metadata:
  type: project
---

**链级术语清扫（2026-08-27，提交 5afb168，人类指示）**：第 1 层需求术语「规范化需求」→「**规范化的相关方需求**」（术语全称化：需求来源=相关方、加工程度=规范化）。与 [[wft01-nfr-deep-review]] 的 OR 清扫形成第三环：`OR → 规范化需求 → 规范化的相关方需求`。

**范围 55 文件**（EOS 设计子线 + 资产 + EOS 规格 + 通用规范 + CLAUDE.md）：
- EOS 设计子线 `10-pl4eos-subpl-sysdev/` 33 文件：ort00~03（主 v0.36/v0.63/v0.40/v0.67）+ wft01~06 三链主文档+SKILL（biz v3.34/v1.30、eng v10.15/v1.24、nfr v6.2/v1.11、wft02-biz v9.14、wft02-eng v10.13、wft03-biz v10.13、wft04-nfr v5.14、wft05-eng v10.15、wft06 v3.8）+ 91 规范 v5.49 + agile/reverse 任务定义
- 资产 `80-pl4eos-2-eosdata/` 14 文件：01 v3.2/02 v2.5/08 v2.3/09 v2.2/10 v1.2/21 v1.2/22 v1.7/25 v2.7 + 状态表/材料/README
- EOS 规格 `00-pl4eos-spec/` 2 文件（v1.8/v2.2）+ 通用规范 `00-generalspec/` 3 文件（v2.4/v2.5/v2.9）+ CLAUDE.md

**关键决策**：
- **spr 缩写/节点 ID/文件名/脚本协议零迁移**——`spr`=Specified Stakeholder Requirements，缩写天然兼容；`spr-XXX` 节点 ID、`01-eos-specified-requirements.md` 文件名、read-node.sh 协议全部不动，只动中文术语
- **通用规范同步**（人类裁决「都处理了吧」）——术语表「相关方需求=Stakeholder Requirements (SR)，**第 2 层**」与「规范化的相关方需求（第 1 层）」字面层递，区分成立；方法论五层链「规范化需求→SR→BP→SysReq→PA」→「规范化的相关方需求→SR→…」
- **保护边界**：`补充规范化需求材料` 家族保留（v3.32 已定名「补充原始需求材料」，wft02 等仍有 64 处正文残留，**待单独收尾**）+ 历史变更记录行保留原词
- 版本 34 文件 +1 + 变更记录补行 26 文件 + 修订日期统一 2026-08-27（顺带修 ort02 修订日期笔误 2026-08-242）

**挂账**：
- `补充规范化需求材料` 正文残留 64 处（wft02-biz 等）——v3.32 只统一了 wft01 系文件名，正文概念名待单轮清扫（对齐「补充原始需求材料」/「业务需求增补」按语境分支）
- read-node.sh 支持格式描述「规范化的相关方需求-NNN」与实际资产节点 ID `spr-NNN` 脱节（历史遗留，可后续校准）
- 记忆库 ba-* 系列仍用旧 BA 术语（[[pending-memory-ba-bp-term]]），本次清扫后中文「规范化需求」在记忆库历史描述中保留原词属惯例
