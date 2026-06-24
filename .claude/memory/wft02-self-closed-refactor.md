---
name: wft02-self-closed-refactor
description: wft02 从 A/B 两阶段重构为三路径自闭环——wft02-biz（STR-F→A2+Bn）和 wft02-eng（STR-E→A1）
metadata:
  type: project
---

# wft02 自闭环重构完成

## 核心决策

### 1. 从 A/B 两阶段到 biz/eng 自闭环

wft02 的 biz 和 eng 两条路径各自闭环——设计+资产对准+写回在同一 Skill 内完成，不再拆分为 wft02a（设计）+ wft02b（资产维护）。原 wft02a（v3.18）和 wft02b（v2.13）保持不变作为历史参考。

### 2. 路径划分

| | wft02-biz | wft02-eng |
|------|-----------|-----------|
| 输入 | STR-F（from wft01-biz） | STR-E（from wft01-eng） |
| 设计对象 | A2（xx业务运行系统）+ Bn（平台输出产品） | A1（业务配置平台） |
| 设计核心 | 十链消费 → 业务定义 + 场景定义 | 配置单元消费 → 引擎配置 IPO |
| 资产 | 23(A2+Bn) + 24 + 26 + 27 | 23(A1) + 25 |
| 生命周期 | 待确认方案→可以架构映射→在架构映射→已架构映射（待补充架构映射） | 同 |

### 3. 核心简化（相对 wft02a/b）

- 消除活动 STR/BA 节点锁定——取消单节点限制
- 消除 `待资产写回` 中间态——人类确认直接 = `可以架构映射`
- Q1/Q2/Q3 统一写回，不设二次确认门禁
- 03 详细定义融入 BA 节点（写在 04-*.md BA 节点块内）
- STR 缺口反馈融入变更传播协议
- 消除跨 Skill 活动锁转交/释放机制

### 4. 文档布局

严格对齐 wft01-biz v1.12 / wft01-eng v2.0 的章节结构：
§一 职责定位 → §二 输入与路由 → §三 文档加载规则 → §四 操作流程（Start→1→2→3→4→Step End + 变更传播协议）→ §五 增量标记输出 → §六 回退规则 → §七 与原文件关系 → §八 变更记录

### 5. 产出文件

- `eos-wft02-biz-str2ba.md`（v1.0）
- `eos-wft02-eng-str2ba.md`（v1.0）
- `91-doc-paired-skill-spec.md`（v2.1）同步更新状态机、全链路映射、人机交互

**Why:** wft02 是 STR→BA 的第二步，STR-F 和 STR-E 两种类型的处理逻辑差异大（十链消费 vs 配置单元法），但设计→资产→写回的闭环结构相同。自闭环消除 A/B 交接的人机交互开销，与 wft01 形成对称的上下游结构——wft01-biz→wft02-biz→wft03，wft01-eng→wft02-eng→wft03。

**How to apply:** wft03~05 后续若考虑从 A/B 迁移到自闭环，直接复用 wft01/wft02 的 Step 结构和生命周期模型。wft02a/b 保留在目录中作为历史参考，与 wft01a/b 对称。
