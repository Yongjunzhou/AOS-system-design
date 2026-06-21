# EOS 系统设计追溯矩阵
**EOS System Design Traceability Matrix**

**文档版本**：v2.0
**创建日期**：2026-05-20
**修订日期**：2026-06-21
**状态**：骨架已改造，待填充
**文档类型**：验证类索引文档
**权威状态源**：本文档 `1. 追溯关系状态与处理队列`

> **文档定位**：EOS 系统设计端到端追溯关系的统一索引文件。本文档不复制 `01~07` 的正文，而是记录 OR、STR、BA、SysReq、PA 和资产文档之间的关系，支持按源节点、目标节点、关系类型和问题状态进行局部读取。

## AI读取文档说明

本文件是追溯关系索引文档，关系数量会随系统设计节点增长而增长。AI 读取本文件时应按需读取，不应默认读取全部追溯关系正文。

默认读取顺序：

1. 读取文档元信息和本说明，确认本文档只记录追溯关系和检查视图。
2. 读取 `0. 追溯矩阵全貌`，了解追溯层级、关系类型和覆盖范围。
3. 读取 `1. 追溯关系状态与处理队列`，确认本轮待补链、待验链或断链问题。
4. 读取 `2. 追溯关系索引 / 分片索引`，按源节点、目标节点或关系类型定位目标关系块。
5. 仅读取目标关系块、相关问题块，以及必要的覆盖率或约束检查视图。

扩大读取范围仅在以下情况允许：

- 源节点或目标节点无法通过索引定位。
- 追溯关系存在断链、重复分配或循环引用。
- 需要执行全局覆盖率、1:1 分配约束或 N:1 承接统计。
- 人类明确要求通读追溯矩阵。

禁止事项：

- 不得在常规 Skill 运行中默认读取全部追溯关系块。
- 不得将 `01~07` 正文复制到本文档。
- 不得只凭对话上下文判断追溯完成；关系必须写入索引或问题队列。

---

## 0. 追溯矩阵全貌

### 0.1 覆盖范围

| 层级 | 源文档 | 目标文档 | 关系目标 |
|------|--------|----------|----------|
| OR → STR | `01-eos-original-requirements.md` | `02-eos-stakeholder-requirements-architecture.md` | OR 末级分配到 STR 架构末级 |
| STR → STR-D | `02-eos-stakeholder-requirements-architecture.md` | `03-eos-stakeholder-requirements-detailed.md` | STR 架构节点细化为详细定义 |
| STR-D → BA | `03-eos-stakeholder-requirements-detailed.md` | `04-eos-business-architecture.md` | STR 详细定义由 BA 方案满足 |
| BA → SysReq | `04-eos-business-architecture.md` | `05-eos-system-requirements-architecture.md` | BA 末级节点映射为 SysReq 架构末级 |
| SysReq → SysReq-D | `05-eos-system-requirements-architecture.md` | `06-eos-system-requirements-detailed.md` | SysReq 架构节点细化为详细定义 |
| SysReq-D → PA | `06-eos-system-requirements-detailed.md` | `07-eos-product-architecture.md` | SysReq 详细活动或约束由 PA 组件承接 |
| 过程文档 → 资产 | `02~07` | `21~27` | 节点引用角色、NFR、输出产品、业务定义、引擎、文档和资源资产 |

### 0.2 关系类型

| 关系类型 | 含义 | 典型场景 |
|----------|------|----------|
| `derived_from` | 从上游材料或节点推导而来 | STR derived_from OR |
| `refines` | 对上游架构节点做详细化 | STR-D refines STR |
| `allocated_to` | 上游需求分配到下游方案节点 | OR allocated_to STR |
| `satisfies` | 下游节点满足上游需求 | BA satisfies STR-D |
| `implemented_by` | 需求或定义由组件承接 | SysReq implemented_by PA |
| `uses_asset` | 节点引用资产条目 | BA uses_asset @def-* |
| `produces_doc` | 节点产生文档资产 | BA produces_doc @doc-* |
| `consumes_doc` | 节点消费文档资产 | BA consumes_doc @doc-* |

### 0.3 覆盖率摘要

| 指标 | 值 | 最近更新 |
|------|-----|----------|
| OR 末级总数 | — | 2026-06-21 |
| 映射到 STR 的覆盖率 | — | 2026-06-21 |
| STR 详细定义末级总数 | — | 2026-06-21 |
| 映射到 SysReq 的覆盖率 | — | 2026-06-21 |
| SysReq 活动总数 | — | 2026-06-21 |
| 映射到 PA 的覆盖率 | — | 2026-06-21 |
| 端到端追溯链完整率 | — | 2026-06-21 |

---

## 1. 追溯关系状态与处理队列

### 1.1 当前活动项

| 待办ID | 待办类型 | 关联节点 | 关系类型 | 当前状态 | 活动锁 | 锁定Skill | 下一步Skill | AI建议 | 人类决策 | 反馈入口 | 最后更新 |
|--------|----------|----------|----------|----------|--------|-----------|-------------|--------|----------|----------|----------|
| — | 补链 / 验链 / 断链修复 / 重复分配处理 | — | — | — | 无 | — | — | — | — | — | 2026-06-21 |

### 1.2 断链与冲突队列

| 问题ID | 问题类型 | 源节点 | 目标节点 | 关系类型 | 影响层级 | 严重度 | AI建议 | 人类决策 | 目标块ID | 最后更新 |
|--------|----------|--------|----------|----------|----------|--------|--------|----------|----------|----------|
| — | 断链 / 重复分配 / 目标缺失 / 来源缺失 / 循环引用 | — | — | — | — | P1 / P2 / P3 | — | — | TRACE-ISSUE-TEMPLATE | 2026-06-21 |

---

## 2. 追溯关系索引 / 分片索引

### 2.1 分片索引

| 分片ID | 分片名称 | 范围 | 默认读取场景 | 关系数 | 入口 |
|--------|----------|------|--------------|--------|------|
| TRACE-SHARD-OR-STR | OR → STR | 原始需求到相关方需求架构 | `wft01` 验证 OR 分配 | — | `4.1 OR 到 STR 关系块` |
| TRACE-SHARD-STR-BA | STR → BA | STR 详细定义到 BA | `wft02` 验证 BA 满足关系 | — | `4.2 STR 到 BA 关系块` |
| TRACE-SHARD-BA-SYSREQ | BA → SysReq | BA 到系统需求 | `wft03` 验证映射 | — | `4.3 BA 到 SysReq 关系块` |
| TRACE-SHARD-SYSREQ-PA | SysReq → PA | 系统需求到产品架构 | `wft05` 验证组件承接 | — | `4.4 SysReq 到 PA 关系块` |
| TRACE-SHARD-ASSET | 过程文档 → 资产 | 对 `21~27` 的资产引用 | 资产一致性检查 | — | `4.5 资产引用关系块` |

### 2.2 关系索引

| 关系ID | 源节点 | 源文档 | 关系类型 | 目标节点 | 目标文档 | 状态 | 块ID | 最后更新 |
|--------|--------|--------|----------|----------|----------|------|------|----------|
| TRACE-TEMPLATE | — | — | derived_from / refines / allocated_to / satisfies / implemented_by / uses_asset | — | — | 模板 | TRACE-TEMPLATE | 2026-06-21 |

---

## 3. 规则区 / 口径区

### 3.1 1:1 分配约束

| 层间映射 | 检查项 | 期望结果 |
|----------|--------|----------|
| OR 末级 → STR 架构末级 | 每条 OR 末级分配到唯一 STR 架构末级 | 一条 OR 不应同时分配给多个 STR 末级 |
| STR-F 详细末级 → SysReq-F 架构末级 | 每条 STR-F 详细末级分配到唯一 SysReq-F 架构末级 | 一条 STR 详细定义不应同时分配给多个 SysReq-F |
| STR-NFR 详细末级 → SysReq-NFR 架构末级 | 每条 STR-NFR 详细末级分配到唯一 SysReq-NFR | 非功能需求分配唯一 |
| SysReq 9级活动 → PA 末级 | 每条 SysReq 活动分配到唯一 PA 末级 | 一个活动由一个 PA 末级主承接 |

### 3.2 N:1 承接口径

1. 下游架构末级可以承接多个上游末级，但应能解释聚合原因。
2. 承接数量过高时，应进入 `1.2 断链与冲突队列` 检查是否过度聚合。
3. 承接数量为 1 不必然错误，但应判断是否为设计意图。

---

## 4. 正文关系块

### 4.1 OR 到 STR 关系块

<!-- BLOCK: TRACE-TEMPLATE -->
#### TRACE-TEMPLATE 追溯关系模板

**当前状态**：模板
**关系类型**：derived_from / refines / allocated_to / satisfies / implemented_by / uses_asset
**块ID**：TRACE-TEMPLATE

| 要素 | 内容 |
|------|------|
| 源节点 | 上游节点 ID |
| 源文档 | 上游文档路径 |
| 目标节点 | 下游节点或资产 ID |
| 目标文档 | 下游文档路径 |
| 关系说明 | 说明两者之间的推导、分配、满足或引用关系 |
| 约束检查 | 是否满足 1:1、N:1 或资产引用口径 |
| 证据摘要 | 引用来源，不复制正文 |

##### 反馈区

| 日期 | 来源 | 反馈内容 | 处理状态 |
|------|------|----------|----------|
| — | — | — | — |

<!-- /BLOCK: TRACE-TEMPLATE -->

### 4.2 STR 到 BA 关系块

> STR 到 BA 关系复用 `TRACE-TEMPLATE` 格式，关系类型通常为 `satisfies`、`uses_asset`。

### 4.3 BA 到 SysReq 关系块

> BA 到 SysReq 关系复用 `TRACE-TEMPLATE` 格式，关系类型通常为 `allocated_to`、`refines`。

### 4.4 SysReq 到 PA 关系块

> SysReq 到 PA 关系复用 `TRACE-TEMPLATE` 格式，关系类型通常为 `implemented_by`。

### 4.5 资产引用关系块

> 资产引用关系复用 `TRACE-TEMPLATE` 格式，关系类型通常为 `uses_asset`、`produces_doc`、`consumes_doc`。

### 4.6 问题块

<!-- BLOCK: TRACE-ISSUE-TEMPLATE -->
#### TRACE-ISSUE-TEMPLATE 追溯问题模板

**当前状态**：模板
**问题类型**：断链 / 重复分配 / 目标缺失 / 来源缺失 / 循环引用
**块ID**：TRACE-ISSUE-TEMPLATE

| 要素 | 内容 |
|------|------|
| 问题描述 | 问题摘要 |
| 影响关系 | 关系 ID 或节点 ID |
| 影响范围 | 影响的层级、文档或下游 Skill |
| AI建议 | 修复建议 |
| 人类决策 | 人类确认结果 |
| 处理结果 | 已修复 / 待修复 / 驳回 |

<!-- /BLOCK: TRACE-ISSUE-TEMPLATE -->

---

## 5. 追溯关系

> 本文档自身的核心内容就是追溯关系索引。本区用于记录与外部验证、报告和资产文档的关系。

| 源节点 | 关系类型 | 目标节点 | 目标文档 | 状态 | 说明 |
|--------|----------|----------|----------|------|------|
| TRACE-* | verified_by | VER-* | `09-eos-sysdev-verification-report.md` | 模板 | 追溯关系由验证任务检查 |
| TRACE-ISSUE-* | reported_in | VER-ISSUE-* | `09-eos-sysdev-verification-report.md` | 模板 | 追溯问题进入验证报告 |

---

## 6. 反馈区 / 建议区

| 反馈ID | 来源 | 关联关系ID | 反馈类型 | 内容 | AI建议 | 人类决策 | 状态 | 最后更新 |
|--------|------|------------|----------|------|--------|----------|------|----------|
| — | — | — | 补链 / 修链 / 删除 / 合并 / 验证 | — | — | — | — | 2026-06-21 |

---

## 9. 文档版本与变更记录

| 日期 | 版本 | 变更类型 | 变更摘要 | 操作 Skill |
|------|------|----------|----------|-----------|
| 2026-06-21 | v2.0 | 结构改造 | 从静态追溯矩阵改为关系索引型文档，新增 AI 读取说明、状态队列、分片索引、关系块和问题块 | Codex |
| 2026-05-20 | v1.0 | 初始化 | 初始追溯矩阵模板 | — |
