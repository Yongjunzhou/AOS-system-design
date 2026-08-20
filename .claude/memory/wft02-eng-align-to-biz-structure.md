---
name: wft02-eng-align-to-biz-structure
description: 2026-08-20 新对话任务——以 wft02-biz v8.9 + wft01-eng v8.8 为标杆调整优化 wft02-eng（人类方案 v8.6→知识层三章重构 + SKILL v1.0 同步），参照 [[wft01-eng-align-to-biz-structure]] 趟通的路子
metadata:
  type: project
---

2026-08-20 记录（wft01-eng v8.8 会话收尾，人类预告「新开对话调整优化 wft02-eng，以 wft02-biz + wft01-eng 为标杆」）。

**目标**：以 [wft02-biz v8.9](../../20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/eos-wft02-biz-str2bp.md)（biz 家族知识层三章已完成）+ [wft01-eng v8.8](../../20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/eos-wft01-eng-or2str.md)（eng 路径已趟通）为标杆，调整优化 [wft02-eng（v8.6，809 行）](../../20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/eos-wft02-eng-str2bp.md) + SKILL（390 行，v1.0）。

**wft02-eng 现状（v8.6，2026-08-14，旧结构）**：§一 职责定位 / §二 A1 配置单元 BP 设计基础（概念混排：2.1 A1 配置单元架构 BP / 2.2 CU 配置能力 / 2.3 A2 上下文与触发追溯 / 2.4 BP 要素提取规则 / 2.5 CU 收敛与依赖推断规则 / 2.6 BP 节点生命周期 / 2.7 BP 变更传播协议）/ §三 操作流程（Step 布局 + 3.1~3.7）/ §四 AI 标记 / §五 变更记录——与 wft01-eng v8.3 改造前骨架完全一样。缺：知识层三章拆分、转换总览、转换原理、自检清单、Step 布局人类参与/执行模式列、反馈双轨、提交基线、确认状态状态机。

**标杆结构**：wft02-biz v8.9 = §一 职责定位 / §二 基本概念（转换总览[转换方法六步一条链 + **语言层级** + 规则地图] + 2.1~2.5 概念）/ §三 设计原理与判据（3.1 转换原理 + 3.2~3.5）/ §四 BP 节点演进（生命周期+变更传播）/ §五 操作流程（Step 布局含人类参与/执行模式列 + 5.1~5.8）/ §六 AI 标记 / §七 自检清单 / §八 变更记录。wft01-eng v8.8 = 同款但**转换总览无语言层级**（人类裁决严格镜像 wft01-biz）。

**关键决策点（新对话需裁决）**：
1. **语言层级**：wft02-biz 有（STR-F 业务语言→BP 架构语言→wft03 配置语言）；wft01-eng 无（严格镜像 wft01-biz）。wft02-eng 是否加语言层级（STR-E→CU BP→wft03-eng 配置语言）？参照 wft01-eng 先例倾向不加，待确认。
2. 结构映射：知识层三章如何拆（概念/原理判据/演进），内容按 eng 特化（CU BP、A1 配置单元、A2 上下文）。
3. Step 框架对齐 wft01-eng v8.8（Step Start 四子节 / Step 4 命名名副实 / Step End 三角色四区——eng 路径三角色落地）。

**参照先例**：[[wft01-eng-align-to-biz-structure]]（本次会话趟通的路子：审查列发现→知识层三章重构→原理方法审视 M/L→张力点分析 A~D→可行性结语→Step 框架对齐）；[[wft02-biz-v80-knowledge-layer-restructure]]；[[wft03-biz-v90-knowledge-layer-restructure]]

**链级注意（新对话直接应用，不需重新讨论）**：
1. 反馈双轨已链级统一（91 §A.5 v5.20 / wft01-biz v3.13 / wft02 v8.9 / wft03 v9.3）——直接对齐。
2. 提交基线顺序（wft01-eng v8.5 M1 + wft01-biz SKILL v1.10）：AI最近变更→滚动删除→git commit→文件头，AI 最近变更 随基线入库。
3. eng 路径术语：主责能力域/目标引擎（支撑引擎属 biz 路径不适用）；CU 是 STR-E 细分节点。
4. 新对话开始时先提交当前未提交改动（wft01-eng v8.8 全套 + 50-reserch 培训教材 3 文件）。

**Why:** 人类预告下一会话任务，跨会话交接价值高。
**How to apply:** 新对话开始时先读本记忆 + [[wft01-eng-align-to-biz-structure]]（趟通样板）；先通读 wft02-eng 全文对照双标杆列差距（等确认），再按结构映射实施；完成后回写本记忆（关闭待办）。
