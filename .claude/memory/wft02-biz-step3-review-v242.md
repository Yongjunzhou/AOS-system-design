---
name: wft02-biz-step3-review-v242
description: 2026-06-30 Step 3 审视→v3.0 重构——设计线与增补线分离，5 Step→8 Step
metadata:
  type: project
---

## v3.0 重构

基于 [v2.42 审视结论](wft02-biz-step3-review-v242.md) + 用户"业务需求与指标需求合一起 / 引擎需求单列"决策。

### 核心变化：设计线与增补线分离

```
设计线（只设计+识别缺口）          增补线（统一处理缺口→OR材料）
Step 3  角色场景视角 BA 设计      Step 6  业务需求增补（FR-BIZ 出口）
Step 4  输出产品视角 BA 设计      Step 7  引擎需求增补（FR-ENG 出口）
Step 5  平台菜单架构设计          Step 8  资产写回与落账
```

### Step 对比

| 旧 (v2.42) | 新 (v3.0) |
|------------|----------|
| Step 3 Phase A | Step 3 角色场景视角 BA 设计 |
| Step 3 Phase B | Step 4 输出产品视角 BA 设计 |
| Step 3 Phase C | Step 5 平台菜单架构设计 |
| （无） | Step 6 业务需求增补（新建） |
| Step 4 | Step 7 引擎需求增补 |
| Step 5 | Step 8 资产写回与落账 |

### 修改范围

- §一 职责定位：11 条完全重写，标注 Step 归属
- 概述段重写：三 Phase→三步设计+两步增补+一步写回
- Step 布局总览：重写
- §3.1/§3.2：保留为 Step 3~5 共享上下文
- Step 3 新增「向 Step 4 传递」接口
- Step 6 新建：OR 材料模板 + 处理流程
- 全文交叉引用 ~30 处：Phase A/B/C→Step 3/4/5 + Step 4/5→7/8
- 增量标记表 + 回退规则 + 设计示例 + Step End 全部更新
- 版本 v2.42→v3.0

## 关联记忆

- [[wft02-biz-phase-c-review-2026-06-30]] — v2.41 Phase C 删除
- [[wft01-biz-bn-23q-gap]] — Bn 侧 23-Q 判定缺口
