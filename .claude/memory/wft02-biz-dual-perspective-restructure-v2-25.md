---
name: wft02-biz-dual-perspective-restructure-v2-25
description: 2026-06-28 wft02-biz v2.24→v2.25 A2/Bn双视角独立行走重构——角色场景视角前置 + 双视角映射校验新设 + 治理角色引入
metadata:
  type: project
---

## 修改摘要

wft02-biz 以 A2（角色场景视角）/ Bn（产品视角）双框架重排 Step 3 四 Phase，联动 wft01-biz/eng 入口门禁加固。

### Phase 重新排列（v2.23→v2.25）

| 旧（v2.23） | 新（v2.25） | 核心变化 |
|---|---|---|
| Phase A: 输出产品 BA 设计 | **Phase A: 角色场景视角 BA 设计** | 首次前置于 Bn，独立沿 A2 菜单树/工作台行走 |
| Phase B: 场景业务编排设计 | **Phase B: 产品 Bn 视角 BA 设计** | 原 Phase A 内容移至此 |
| Phase C: 业务菜单方案设计 | **Phase C: 双视角映射与一致性校验** | 全新 Phase，检查 A2↔Bn 映射断裂/孤立/治理承接 |
| Phase D: 上层指标方案设计 | **Phase D: 菜单/权限/指标与治理能力缺口** | 扩展治理能力缺口识别（目录/版本/引用/质量/血缘） |

### 关键设计决策

1. **A2/Bn 两棵树独立行走**：A2 沿菜单树/工作台，Bn 沿业务产品资产树/数据资产目录，在 Phase C 交汇校验
2. **业务架构管理员 + 数据治理员**作为平台治理角色引入，在 wft01-biz 识别治理对象类型，在 wft02-biz 展开为治理菜单+Bn 资产树
3. **引擎缺口线索降级**：Step 4 从"自动写回 FR-ENG OR"改为"BA 节点内登记线索，待人类确认转化"——引擎缺口线索不再自动进入 eng 管道
4. **wft01-eng 入口门禁**：只接受正式 FR-ENG OR，不接受 wft02-biz 的派生线索
5. **原始需求材料登记**：平台治理角色原始需求材料作为 OR 原料入库（ORT-20260628-001）

### 影响链路

wft01-biz（识别治理角色+治理对象类型）→ wft02-biz（独立设计 A2 治理菜单 + Bn 治理资产树 + Phase C 校验映射 + Phase D 治理能力缺口 + Step 4 引擎能力线索）→ 人类确认后 → 正式 FR-ENG OR → wft01-eng（仅接受正式 FR-ENG OR）

### 记忆关联

- [[wft02-biz-step3-revision-v2-4]] — 之前的 Step 5 消减链路
- [[wft02-v23-restructure-complete]] — v2.3 四 Phase 同构基线
- [[wft02-pending-discussion]] — 待讨论议题
- [[wft02-revision-plan]] — 更早的 v3.0 规划（已部分被本次重构替代）
