---
name: eos-wft01-nfr-or2str
description: NFR OR→STR-NFR 角色非功能需求分类设计。接收正式NFR OR（≤10条），
             完成OR→STR-NFR角色NFR分类设计（语境提取→分类需求清单→22资产对齐→完备性检查），
             将22分类对齐结论写回22资产，形成可进入wft04-nfr的STR-NFR节点。
---

# eos-wft01-nfr · NFR OR → STR-NFR 角色非功能需求分类设计

> **设计依据**：[eos-wft01-nfr-or2str.md](../eos-wft01-nfr-or2str.md)（人类方案——权威源）
> **运行时协议**：[91-eos-biz-eng-spec.md](../91-eos-biz-eng-spec.md) 附录A（入口条件/读取协议/反馈交互/Step End输出模板）
> **领域规范**：[91-eos-biz-eng-spec.md](../91-eos-biz-eng-spec.md)

---

## 一、职责定位

### 负责与不负责

| 负责 | 不负责（路由指向） |
|------|-------------------|
| 接收正式 NFR OR（≤10条），校验类型/状态/语境 | FR-BIZ 业务场景和输出文档设计 → `wft01-biz` |
| 识别角色语境 + 22 分类路径，按四元组（角色+语境+维度+对象）匹配已有 STR-NFR | FR-ENG 平台能力场景和 CU 候选设计 → `wft01-eng` |
| 生成 NFR 分类需求清单 + 逐项判定 22-Q1/Q2/Q3/Q3+（全量 `[推断]`） | 将 NFR 定性诉求转为系统量化指标/阈值/测试方法 → `wft04-nfr` |
| 检出分类/适用范围/验证语义三类缺口 → 生成补充 NFR OR 材料 | 生成 SysReq-NFR、页面 NFR、CU/PA 组件约束 → `wft04-nfr` |
| 人类确认后写回 22 资产 + OR→`已分配` + STR-NFR→`可以NFR设计` | 修改 22 已确认分类维度的权威定义（本 Skill 只写引用和候选建议） |
| 接收 wft04 退回的 `需wft01修订` STR-NFR，按人类方案修订 | — |

### 上下游衔接

| 方向 | Skill | 交接内容 |
|------|-------|---------|
| 上游 | OR 预处理（`ort03`） | 正式 NFR OR 写入 `01-*.md`，状态=`待处理`。通过 `## AI可以处理节点` 的"待 wft01-nfr 处理"分节检测 |
| 下游 | `wft04-nfr` | 消费 `可以NFR设计`/`待补充NFR设计` 的 STR-NFR，量化为 SysReq-NFR 与页面 NFR。缺陷时退回 `需wft01修订`+缺失说明 |
| 同级 | `wft01-biz`、`wft01-eng` | 各自处理 FR-BIZ / FR-ENG，本 Skill 输入校验检出后退出并提示路由 |

---

## 二、操作流程

### Step Start · 前置校验与路由

**入口检测**（按 [91 规范 §A.4](../91-eos-biz-eng-spec.md#a4-入口条件与优先级step-start)）：

```bash
# 1. 读取待处理节点
bash ../scripts/read-section.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md "AI可以处理节点"
bash ../scripts/read-section.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md "AI可以处理节点"
```

**输入校验**（按顺序，命中即退出）：

| 条件 | 判定 | 动作 |
|------|------|------|
| STR-NFR 状态=`需wft01修订` 且人类未提供改进方案 | 退回方案缺失 | 输出 wft04 缺失说明 → **退出** |
| OR 状态≠`待处理` | 不可处理 | 输出当前状态 → **退出** |
| OR 类型为 FR-BIZ | 路由错误 | 输出类型分布 + 路由指引（→ `wft01-biz`）→ **退出** |
| OR 类型为 FR-ENG | 路由错误 | 输出类型分布 + 路由指引（→ `wft01-eng`）→ **退出** |
| OR 为业务配置实例 | 不适用 | 标记并提示不进入 NFR 设计 → **退出** |
| OR >10 条 | 软提示 | 输出超限提示 → 人类确认 |
| 无任何待处理 | — | 输出"无待处理对象"→ **退出** |

**退回优先**：存在 `需wft01修订` STR-NFR → 检查人类是否提供改进方案。已提供 → 读取缺失说明，走 Phase B 修订。未提供 → 输出缺失说明 → **退出**。

---

### Step 1 · 设计材料加载

**1. 版本感知**：

```bash
bash ../scripts/detect-changes.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md
bash ../scripts/detect-changes.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md
```

检出 `HAS_CHANGES=1` → AI 检查变更行，理解人类是否做了非预期修改，必要时标记 `[需确认]`。

**2. 加载本轮 NFR OR 条目**：

```bash
# 获取待处理 OR 节点 ID 列表
bash ../scripts/read-section.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md "待 wft01-nfr 处理"

# 逐节点读取正文
bash ../scripts/read-node.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md <OR-ID>
```

**3. 加载已有 STR-NFR 节点**（用于宿主匹配）：

```bash
# 读取 STR 树画像和节点索引
bash ../scripts/read-section.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md "STR树画像"
bash ../scripts/read-section.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md "STR节点索引"

# 按需读取候选 STR-NFR 节点块（同角色/同语境/同分类维度）
bash ../scripts/read-node.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md <STR-NFR-ID>
```

**4. 加载资产全貌**：

| 资产 | 用途 |
|------|------|
| `21-eos-stakeholder-roles.md` | 角色定义、业务域和角色类型线索 |
| `22-eos-nfr-taxonomy.md` | NFR 一级类目/分类维度清单（运行时动态读取，不缓存） |

**按需扩大原则**：仅在索引无法定位、候选冲突、追溯断裂或人类明确要求时扩大读取范围。禁止默认加载全文件正文。

---

### Step 2 · 方案反馈处理

**触发条件**：Step Start 检出 `需wft01修订` STR-NFR，或上一轮 Step End 的反馈等待中人类提出修改意见。

**处理规则**：

1. 从当前轮次对话上下文或退回缺失说明中读取人类反馈意图
2. **逐条处理**（按人类反馈内容）：
   - AI 输出方案后人类直接回复修改意见 → 在当前轮次继续对话处理
   - wft04 退回的 `需wft01修订` → 下一轮 Skill 调用时走 Step Start 退回优先
3. 修改后检查是否仍满足该 STR-NFR 所承接的 NFR OR 需求
4. 修改导致结构性变更（角色语境/分类维度/需求清单重组）→ 按需重入 Step 3
5. 全部条目获人类认可 → STR-NFR → `可以NFR设计`
6. **元信息维护**：

```bash
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md bump-version
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md update-head
```

---

### Step 3 · 角色 NFR 分类设计

#### Phase A — OR 语境提取与路由

对每条新 OR：
1. 从已加载的 OR 节点块中提取关注角色、业务/平台语境、非功能诉求、待量化线索和适用对象线索
2. **路径归属判定**——OR 实际描述业务流程/输出文档 → 退回 `wft01-biz`；OR 实际描述引擎能力/CU → 退回 `wft01-eng`；OR 为具体配置数据 → 标记不进入；OR 描述质量属性/运行约束 → 进入 wft01-nfr
3. **宿主匹配**——OR 的四元组（角色+语境+分类维度+适用对象）落入已有 STR-NFR 分类边界 → Phase B；否则 → 待聚合池 → Phase C

待聚合池按**同一角色 + 同一语境 + 同一 22 分类维度**分组。

#### Phase B — 修订已有 STR-NFR

**执行顺序**：

1. **要素提取**——从本轮 OR 提取关注角色、业务/平台语境、非功能诉求、待量化线索和适用对象线索（详见 human spec §2.4.1）
2. **边界匹配检查**——确认 OR 在 STR-NFR 边界内（详见 human spec §2.4.3）：

| 匹配结果 | 动作 |
|---------|------|
| 直接归入（仅补强） | 追加 OR 来源 |
| 新增需求项 | 加入分类需求清单 |
| 边界扩展 | 更新适用范围线索 + 输出变更声明 |
| 分类冲突 | 标记 `[需裁决]`，必要时拆分 |
| 宿主误匹配 | 退回待聚合池 |

3. **需求项关系检测**——比对已有基线（详见 human spec §2.5.3）：

| 关系 | 判定 | 处理 |
|------|------|------|
| 确认 | 需求项匹配+22分类一致+来源非OR明示 | 来源升级 |
| 无新增 | 需求项匹配+全部已OR明示 | 追加引用+增量合并 |
| 22判定变更 | 需求项匹配+22判定不同 | 更新22判定+变更原因 |
| 补充 | 需求项不匹配 | 新增到清单 |
| 过时 | 基线需求项未被本轮覆盖 | `[过时]`+保留不删 |

4. **变更影响声明**——判定变更类型，写入 STR-NFR 节点末尾（详见 human spec §2.7）

#### Phase C — 新建 STR-NFR

**执行顺序**：

1. **确定角色语境**——从 OR 语义提取关注角色、业务/平台语境、链身份
2. **判定 22 分类路径**——从 22 资产动态读取一级类目和分类维度，按 OR 语义匹配。全量标注 `[推断]`（22-Q1/Q2/Q3/Q3+ 判据见附录 A.2）
3. **生成分类需求清单**——识别需求项→去重收敛→逐项判定来源类型与待量化线索→标注字段（详见 human spec §2.5.1~§2.5.2）
4. **执行完备性检查**——五项：角色语境清楚/分类维度单一/适用对象有线索/待量化线索保留/分类资产对齐明确
5. **组装 STR-NFR**——写入 `02-*.md`，完整要素见 human spec §2.1.2

> **待量化线索的处理**：wft01-nfr 只记录 OR 中出现的数值、比较词和验证条件，**不将其转为系统量化指标**（该职责在 wft04-nfr）。如 OR 说"页面查询要在2秒内响应"，wft01 记录 `待量化线索：OR提到"2秒内"和"页面查询响应"`。

---

### Step 4 · 补充 NFR 与变更声明

按每个 STR-NFR 独立执行。新建 → 全量检查；修订 → 仅当分类维度拓扑变化时重验闭合。

**1. NFR 闭合检查**——三类缺口：

| 检出条件 | 缺口类型 | 处理 |
|---------|---------|------|
| 关注角色缺失 | `[需澄清]` | 不生成补充材料 |
| 适用对象缺失 | `补充OR` | 进入补充 NFR 材料生成 |
| 可验证语义缺失 | `澄清项` | 进入补充 NFR 材料生成 |
| 分类维度冲突 | `分类裁决` | 输出分类裁决项 |
| 一个 OR 混合多个维度 | `拆分建议` | 输出拆分建议，退回 OR 预处理 |

**2. 要素机械检查**——逐 STR-NFR：用户角色/业务域/一级类目非空、分类需求清单非空且逐项标注、22 分类对齐到位、变更影响声明已写入。发现即标注 `[覆盖缺口]`。

**3. 补充 NFR 材料生成**——写入 `../../80-pl4eos-2-eosdata/00-origin-requirement-materials/10-raw-files/<YYYYMMDD>-<STR-NFR名称>补充原始需求材料.md`，登记到 OR 原料状态表。

---

### Step 5 · 资产写回与落账

仅写回状态=`可以NFR设计` 的 STR-NFR 节点。Step 3 新产出留待下一轮。

**写回操作**：
1. 遍历已确认 STR-NFR，按 22 分类对齐结果写回 22 资产——Q1 追加引用（去重），Q2 引用+候选扩展说明（标注 `[推断]`），Q3/Q3+ 写入候选分类建议（标注 `[推断]`/`[需裁决]`）。不写系统量化指标
2. 对应 OR 条目 → `已分配`

**元信息维护**（用脚本，不手动）：

```bash
# 更新文件头
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md bump-version
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md update-head
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md bump-version
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md update-head
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/22-eos-nfr-taxonomy.md bump-version
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/22-eos-nfr-taxonomy.md update-head

# 追加 AI最近变更 记录
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md add-recent-change "wft01-nfr" "资产写回" "<STR-NFR-ID>" "22 分类引用写回"

# 移出已完成节点
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md move-node "<OR-ID>" "wft01-nfr" "done"
```

---

### Step End · 运行结束输出（含反馈等待）

按三区模板（[91 规范 §A.3.2](../91-eos-biz-eng-spec.md#a32-step-end-输出模板三区结构)）输出方案摘要。

**输出后不要结束对话。** 等待人类反馈：

> 以上是本轮方案。直接回复修改意见即可：
> - "适用范围应限定为采购单列表页"
> - "整体确认"
> - "批量导入并发性能的 22 分类改为 Q2"

**AI 处理反馈规则**：

| 人类输入 | AI 动作 |
|---------|--------|
| 显式修改指令（"X 改为 Y"） | 定位条目 → Edit 修改 → 追加 `[已处理]` → 输出修改摘要 → 继续等待 |
| 质疑/讨论（"为什么选 X？"） | 解释理由，不自动修改，继续等待决策 |
| 整体确认（"可以"/"整体确认"） | 全部条目追加 `[同意] [已处理]` → **整理本次反馈总结**（见下）→ 推进状态 → Step 5 落账 → 结束 |
| 模糊意见（"粒度太粗"） | 尝试具体化追问，引导可执行指令 |

**反馈总结**（仅在人类"整体确认"后执行）：

```bash
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md add-recent-change "wft01-nfr" "反馈处理" "<STR-NFR-ID>" "<AI 总结的反馈要点>"
```

摘要示例：`22判定修正：批量导入并发性能 Q1→Q2；新增待量化线索"高峰期并发数"`

---

## 三、AI 标记约定

四类增量标记（`[新增]`/`[变更]`/`[确认]`/`[需裁决]`）的定义详见 [91 规范 §A.3.1](../91-eos-biz-eng-spec.md#a31-ai-增量标记)。

每次 Step 3 完成后，向人类输出增量清单，格式如：

```text
=== STR-NFR-PERF-001 本轮更新清单 ===

[新增] 承接 OR-NFR-001, OR-NFR-002（共2条）

分类需求清单
  [新增] "页面查询响应时间"（系统性能，22-Q1）  待量化线索：OR提到"高峰期"和"列表查询"
  [新增] "批量导入并发性能"（系统性能，22-Q2）  待量化线索：OR提到"并发使用"

完备性检查
  角色语境清楚 ✓ / 分类维度单一 ✓ / 适用对象有线索 ✓
  → [需裁决] "操作不绕路"归入产品易用性还是操作人机工效
```

---

## 附录A：判据速查

### A.1 STR-NFR 归组四元组

| 锚点 | 说明 |
|------|------|
| 用户角色 | 提出或承受该非功能诉求的角色、外部系统或保障者 |
| 业务/平台语境 | 业务域、产品类型、STR-F/STR-E 线索或横切平台能力 |
| NFR 分类维度 | 22 资产中的一级类目 + 分类维度 |
| 适用对象线索 | 可能约束的 STR-F、STR-E、业务域、平台能力、页面类型、具体页面 ID 或全局对象 |

### A.2 22 分类资产对齐判定

| 判定 | 条件 | 动作 |
|------|------|------|
| **22-Q1** | OR 语义明确落入已有已确认分类维度 | 引用已有分类维度 |
| **22-Q2** | OR 是已有分类维度的子类、扩展场景或边界细化 | 引用已有 + 提出候选扩展说明，等待 wft04 校验 |
| **22-Q3** | 现有一级类目可承载，但缺少分类维度 | 提出候选新增分类维度建议，标记 `[需裁决]` |
| **22-Q3+** | 现有一级类目也无法承载 | 提出候选新增一级类目 + 分类维度建议，标记 `[需裁决]` |

状态敏感规则：`已确认` 可稳定引用；`候选`/`疑似` 只能作为线索，引用时标记 `[需裁决]`；`废弃` 不得作为归属。

### A.3 Phase B 边界匹配结果

| 结果 | 判定 | 动作 |
|------|------|------|
| 直接归入 | 新 OR 只补强已有需求项 | 追加来源，标记 `[确认]` |
| 新增需求项 | 角色语境和分类不变，但新增分类需求 | 加入清单，标记 `[新增]` |
| 边界扩展 | 适用范围线索扩展但仍属同一分类 | 修订 STR-NFR，输出变更声明 |
| 分类冲突 | 分类维度需改变或跨维度 | 标记 `[需裁决]`，必要时拆分 |
| 宿主误匹配 | 不属于同一角色语境或分类维度 | 退回待聚合池 |

### A.4 Phase B 需求项关系检测

| 关系 | 判定 | 处理 |
|------|------|------|
| 确认 | 需求项匹配+22分类一致+来源非OR明示 | 来源升级 |
| 无新增 | 需求项匹配+全部已OR明示 | 追加引用+增量合并 |
| 22判定变更 | 需求项匹配+22判定不同 | 更新22判定+变更原因 |
| 补充 | 需求项不匹配 | 新增到清单 |
| 过时 | 基线需求项未被本轮覆盖 | `[过时]`+保留不删 |

### A.5 STR-NFR 完备性判据

| 检查项 | 通过标准 | 不通过处理 |
|--------|----------|------------|
| 角色语境清楚 | 能定位提出者或承受者 | 生成澄清型补充 NFR |
| 分类维度单一 | 一个 STR-NFR 只表达同一角色语境下的一类 NFR 分类维度 | 拆分 STR-NFR 或退回 OR 重切 |
| 适用对象有线索 | 至少能标注全局/业务域/STR-F/STR-E/平台能力中的一种线索 | 标记适用范围缺口 |
| 待量化线索保留 | OR 中的数值、比较词、验证条件未丢失 | 补齐记录，不自行量化 |
| 分类资产对齐明确 | 22 判定已完成，Q3/Q3+ 有建议 | 标记 `[需裁决]` |

### A.6 NFR 闭合检查三类缺口

| 检出条件 | 缺口类型 | 处理 |
|---------|---------|------|
| 关注角色缺失 | `[需澄清]` | 不生成补充材料 |
| 适用对象缺失 | `补充OR` | 进入补充 NFR 材料生成 |
| 可验证语义缺失 | `澄清项` | 进入补充 NFR 材料生成 |
| 分类维度冲突 | `分类裁决` | 输出分类裁决项 |
| 一个 OR 混合多个维度 | `拆分建议` | 输出拆分建议，退回 OR 预处理 |

### A.7 STR-NFR 节点生命周期状态流转

```
待确认方案 ──人类确认──→ 可以NFR设计 ──wft04锁定──→ 在NFR设计 ──wft04完成──→ 已NFR设计
     ↑                        ↑                         │
     │                        │               wft04退回  │
     │                        │                         ↓
     └─── wft01修订 ────── 需wft01修订 ←───────────────┘

上游变更分流：
  可以NFR设计 → 可以NFR设计（版本递增）
  在NFR设计   → 在NFR设计（版本递增）
  已NFR设计   → 待补充NFR设计
```

### A.8 需求项来源类型

| 来源类型 | 含义 |
|---------|------|
| `OR明示` | OR 文本中直接说出该非功能质量诉求 |
| `OR隐含` | OR 未直接说出，但不补充则质量期望存在逻辑缺口 |
| `同类语境推断` | 同角色同业务域已有 STR-NFR 的类似 NFR 分类模式 |
| `资产线索推断` | 22 资产中已有与当前角色语境匹配的分类维度，但 OR 未提及 |

---

## 附录B：脚本接口速查

| 脚本 | 用法 | 说明 |
|------|------|------|
| `read-section.sh` | `bash ../scripts/read-section.sh <文件> <分节名>` | 提取 ##/### 分节完整内容 |
| `read-node.sh` | `bash ../scripts/read-node.sh <文件> <节点ID>` | 按节点ID提取节点块（支持 OR-NNN / STR-NFR-XXX / @node-xxx 等） |
| `detect-changes.sh` | `bash ../scripts/detect-changes.sh <文件>` | 检测人类自上次 AI 运行以来的文档变更 |
| `update-meta.sh` | `bash ../scripts/update-meta.sh <文件> <操作>` | 维护文件元信息（bump-version / update-head / add-recent-change / move-node） |

所有脚本路径相对于 `eos-wft01-nfr-or2str/` 目录。

---

## 变更记录

| 日期 | 版本 | 说明 |
|------|------|------|
| 2026-07-20 | v1.0 | 初始版本——从人类方案文档 v5.1 提取 Skill，脚本化数据访问，领域知识引用人类方案 |
