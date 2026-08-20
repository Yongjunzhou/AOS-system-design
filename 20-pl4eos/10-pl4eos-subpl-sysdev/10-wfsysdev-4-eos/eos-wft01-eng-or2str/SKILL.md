---
name: eos-wft01-eng-or2str
description: FR-ENG OR→STR-E 平台能力场景业务设计。接收正式FR-ENG OR（≤10条），
             完成OR→STR-E平台能力场景设计（溯源→能力链→CU候选→完备性检查），
             写回23/25资产名称级引用，形成可进入wft02-eng的STR-E节点。
---

# eos-wft01-eng · FR-ENG OR → STR-E 平台能力场景业务设计

> **设计依据**：[eos-wft01-eng-or2str.md](../eos-wft01-eng-or2str.md)（人类方案——权威源）
> **运行时协议**：[91-eos-biz-eng-spec.md](../91-eos-biz-eng-spec.md) 附录A（入口条件/读取协议/反馈交互/Step End输出模板）
> **领域规范**：[91-eos-biz-eng-spec.md](../91-eos-biz-eng-spec.md)

---

## 一、职责定位

### 负责与不负责

| 负责 | 不负责（路由指向） |
|------|-------------------|
| 接收正式 FR-ENG OR（≤10条），校验类型/状态/主责能力域 | FR-BIZ 业务场景和输出文档设计 → `wft01-biz` |
| 识别主责能力域（引擎专属/平台共享）+ 配置/治理目标 + 可独立验收结果 | NFR 分类与量化 → `wft01-nfr` / `wft04-nfr` |
| 按三元组（能力域+目标+验收结果）匹配已有 STR-E | CU 配置页面、配置要素、校验保存规则 → `wft02-eng` |
| 名称级识别 CU 候选 + 构建能力链 + 完备性检查 | 配置页面、操作活动、页面功能需求 → `wft03-eng` |
| 检出能力链缺口 → 生成补充 FR-ENG OR 材料 | 前后端组件、接口和实现边界 → `wft05-eng` |
| 人类确认后推进 STR-E→`可以分解分配` + OR→`已分配` | 25 资产中引擎/CU 模型的正式定义（本 Skill 仅名称级候选引用） |
| 接收 wft02-eng 退回的 `需wft01修订` STR-E，按人类方案修订 | — |

### 上下游衔接

| 方向 | Skill | 交接内容 |
|------|-------|---------|
| 上游 | OR 预处理（`ort03`） | 正式 FR-ENG OR 写入 `01-*.md`，状态=`待处理`。通过 `## AI可以处理节点` 的"待 wft01-eng 处理"分节检测。wft03-biz 产生的引擎能力缺口线索须先经人类确认+完整通过 ort00→ort03 才能进入 |
| 下游 | `wft02-eng` | 消费 `可以分解分配`/`待补充分解分配` 的 STR-E，展开 CU BP。缺陷时退回 `需wft01修订`+缺失说明 |
| 同级 | `wft01-biz`、`wft01-nfr` | 各自处理 FR-BIZ / NFR，本 Skill 输入校验检出后退出并提示路由 |

---

## 二、操作流程

### Step Start · 前置校验与路由

**入口检测**（按 [91 规范 §A.4](../91-eos-biz-eng-spec.md#a4-入口条件与优先级step-start)）：

```bash
bash ../scripts/read-section.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md "AI可以处理节点"
bash ../scripts/read-section.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md "AI可以处理节点"
```

**输入校验**（按顺序，命中即退出）：

| 条件 | 判定 | 动作 |
|------|------|------|
| STR-E 状态=`需wft01修订` 且人类未提供改进方案 | 退回方案缺失 | 输出 wft02-eng 缺失说明 → **退出** |
| OR 状态≠`待处理` | 不可处理 | 输出当前状态 → **退出** |
| OR 类型为 FR-BIZ | 路由错误 | 输出类型分布 + 路由指引（→ `wft01-biz`）→ **退出** |
| OR 类型为 NFR | 路由错误 | 输出类型分布 + 路由指引（→ `wft01-nfr`）→ **退出** |
| OR 为业务配置实例 | 不适用 | 标记并提示 → **退出** |
| OR 是 wft03-biz 线索但未转正式 OR | 未正式化 | 提示先确认并写入 `01-*.md` → **退出** |
| OR 无法判定唯一主责能力域或独立验收结果 | 归属不明 | 标记 `需澄清` → **退出** |
| OR >10 条 | 软提示 | 输出超限提示 → 人类确认 |
| 无任何待处理 | — | 输出"无待处理对象"→ **退出** |

**退回优先**：存在 `需wft01修订` STR-E → 检查人类是否提供改进方案。已提供 → 读取缺失说明，走 Phase B 修订。未提供 → 输出缺失说明 → **退出**。

---

### Step 1 · 设计材料加载

**1. 版本感知**：

```bash
bash ../scripts/detect-changes.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md
bash ../scripts/detect-changes.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md
```

**2. 加载本轮 OR + 已有 STR-E**：

```bash
bash ../scripts/read-section.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md "待 wft01-eng 处理"
bash ../scripts/read-node.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md <OR-ID>
bash ../scripts/read-section.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md "STR树画像"
bash ../scripts/read-node.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md <STR-E-ID>
```

**3. 加载资产全貌**：

| 资产 | 用途 |
|------|------|
| `23-eos-output-architecture.md` 资产全貌层 | A1 产品/引擎归属锚点 |
| `24-eos-business-assets.md` 资产全貌层 | 业务运行对象与平台治理对象线索 |
| `25-eos-engine-models.md` §1.1 | 引擎/CU 类型清单（运行时动态读取，不缓存） |

**按需扩大原则**：仅在索引无法定位、候选冲突、追溯断裂或人类明确要求时扩大读取范围。

---

### Step 2 · 方案反馈处理

**触发条件**：Step Start 检出 `需wft01修订` STR-E，或上一轮 Step End 的反馈等待中人类提出修改意见。

**反馈双轨**（人类任选其一，详见人类方案 §5.3）：①AI 对话反馈——Step End 后不结束对话，直接回复修改意见，AI 即时处理；②线下文档修订——打开 `01/02-*.md` 在确认状态字段标注 `[同意]`/`[修改]`/`[驳回]` 或直接编辑方案内容（自由文本），经 Step 1 变更感知 git diff 检测后按 §A.5 处理。两轨等价均落账（追 `[已处理]`）。

**处理规则**：

1. 从当前轮次对话或退回缺失说明中读取人类反馈意图
2. **逐条处理**——AI 输出方案后人类直接回复 → 当前轮次继续；wft02 退回 → 下一轮走 Step Start 退回优先
3. 修改后检查是否仍满足 OR 需求
4. 结构性变更（边界/能力链/CU 候选重组）→ 按需重入 Step 3
5. 全部条目获认可 → STR-E → `可以分解分配`
6. **元信息维护**：

```bash
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md bump-version
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md update-head
```

**AI 处理反馈规则**：

| 人类输入 | AI 动作 |
|---------|--------|
| 显式修改指令 | 定位条目 → Edit 修改 → 追加 `[已处理]` → 输出修改摘要 → 继续等待 |
| 质疑/讨论 | 解释理由，不自动修改，继续等待决策 |
| 整体确认 | 全部条目追加 `[同意] [已处理]` → **整理反馈总结** → 推进状态 → Step 5 落账 → 结束 |
| 模糊意见 | 尝试具体化追问 |
| 线下修订检出（git diff 发现确认状态标注/自由文本编辑） | 定位条目 → Edit 修订 → 追加 `[已处理]` → 输出修改摘要 → 继续等待 |

**反馈总结**：

```bash
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md add-recent-change "wft01-eng" "反馈处理" "<STR-E-ID>" "<AI总结的反馈要点>"
```

---

### Step 3 · 场景业务设计

#### Phase A — OR 溯源与路由

对每条新 OR：
1. 提取触发来源、能力诉求、运行期结果、主责能力域（详见 human spec §3.2.1）
2. **路径归属判定**——OR 实际为业务文档/流程 → 退回 `wft01-biz`；OR 为性能/安全等约束 → 退回 nfr 路径；OR 仅为配置数据 → 标记不进入
3. **宿主匹配**——OR 的三元组（主责能力域+配置/治理目标+独立验收结果）落入已有 STR-E → Phase B；否则 → 待聚合池 → Phase C

待聚合池按**主责能力域（引擎）**分组。

#### Phase B — 修订已有 STR-E

1. **要素提取**——从本轮 OR 提取触发来源、能力诉求、运行期结果、主责能力域
2. **场景匹配检查**——确认 OR 与 STR-E 的三元组一致（详见 human spec §3.2.3）：

| 匹配结果 | 动作 |
|---------|------|
| 场景匹配（三元组一致） | 进入 CU 关系检测 |
| 同域不同场景 | 匹配其他 STR-E 或触发 Phase C 新建 |
| 共享依赖 | 写入依赖关系，不复制 CU |
| 主责不匹配 | 退回待聚合池 |

3. **CU 候选关系检测**——比对已有基线（详见 human spec §3.3.3）：

| 关系 | 判定 | 处理 |
|------|------|------|
| 确认 | CU匹配+引擎相同+来源非OR明示 | 来源升级 |
| 无新增 | CU匹配+全部已OR明示 | 追加引用+增量合并 |
| 引擎归属变更 | CU匹配+引擎不同 | 更新引擎+变更原因 |
| 补充 | CU不匹配 | 新增到候选清单 |
| 过时 | 基线CU未被本轮覆盖 | `[过时]`+保留不删 |

4. **变更影响声明**——判定变更类型，写入 STR-E 节点末尾

#### Phase C — 新建 STR-E

1. **确定主责能力域**——从 OR 语义提取，判定为引擎专属或平台共享
2. **定义能力场景范围**——配置/治理目标 → 系统处理要求 → 运行期制品/构件/功能 → 可用性确认（终点=OR 显式覆盖、不得在终点后扩展，详见 human spec §3.2.2）
3. **构建能力链**——按四段排列（配置意图→系统处理→运行期产出→可用确认）
4. **识别 CU 候选**——名称级列出可能触及的 CU，逐候选标注来源类型和粒度判断（详见 human spec §3.3.1~§3.3.2）
5. **标注 OR 类型**——逐条 OR 判定五种 FR-ENG OR 类型之一（配置生成类/构件扩展类/布局组件扩展类/横切治理类/运行支撑类），不用于划分 STR-E 边界
6. **组装 STR-E**——写入 `02-*.md`，完整要素见 human spec §2.1.2

---

### Step 4 · FR-ENG 需求增补

按每个 STR-E 独立执行。新建 → 全量检查；修订 → 仅当能力链拓扑变化时重验闭合。

**1. 能力链闭合检查**——四段：配置/治理意图 → 系统处理要求 → 运行期制品/构件/功能 → 可用性确认。配置/治理意图段缺失→`补充OR`；系统处理要求段缺失→`补充OR`；运行期制品/构件/功能段缺失→`补充OR`；可用性确认段缺失（判据不明确）→`澄清项`。

**2. 要素机械检查**——引擎名称/场景边界非空、能力诉求/运行期结果有标注、追溯链完整、CU 候选清单非空且逐条标注来源类型和粒度判断、变更影响声明已写入。

**3. 补充 FR-ENG 材料生成**——写入 `../../80-pl4eos-2-eosdata/00-origin-requirement-materials/10-raw-files/<YYYYMMDD>-<STR-E名称>补充原始需求材料.md`，登记到 OR 原料状态表。与 wft03-biz 缺口线索同一管道（人类方案 §5.5）：经确认 + ort00→ort03 转正式 FR-ENG OR，不豁免预处理链。

---

### Step 5 · 资产写回与落账

仅写回状态=`可以分解分配` 的 STR-E 节点。Step 3 新产出留待下一轮。

**写回操作**：
1. 遍历已确认 STR-E，按主责类型和能力域写回 23 资产——已有引擎追加引用（去重），新引擎/共享能力域候选写入建议
2. 遍历 CU 候选，写回 25 资产——仅名称级引用或模型建议，不写详细定义
3. 对应 OR 条目 → `已分配`

**提交基线 + 元信息维护**（用脚本，不手动；顺序对齐人类方案 §5.6，AI 最近变更 随基线入库）：

```bash
# 追加 AI最近变更 记录 + 移出已完成节点（先于提交，随基线入库）
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md add-recent-change "wft01-eng" "资产写回" "<STR-E-ID>" "23/25 资产写回"
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md move-node "<OR-ID>" "wft01-eng" "done"

# 提交本轮 AI 产出（链级不变式：基线 = 最后 AI 提交，git diff <HEAD @上次 AI 运行>..HEAD 只含人类变更）
git add -A && git commit -m "[AI] wft01-eng 资产写回（Co-Authored-By: Claude）"

# 更新文件头（HEAD = 刚提交的基线 hash）
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md bump-version
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/01-eos-original-requirements.md update-head
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md bump-version
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/02-eos-stakeholder-requirements-architecture.md update-head
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/23-eos-output-architecture.md bump-version
bash ../scripts/update-meta.sh ../../80-pl4eos-2-eosdata/23-eos-output-architecture.md update-head
```

---

### Step End · 运行结束输出（含反馈等待）

按三区模板输出方案摘要：

```text
当前状态：<待确认方案 / 可以分解分配>
  修订 STR-E-XXX（+N OR，v{N-1}→v{N}）/ 新建 STR-E-YYY（新能力场景，聚合 K 条 OR，v1）
  场景不匹配 OR-WWW（本轮退回待聚合池，留待重新匹配其他 STR-E）
资产落账：<23 引擎引用写回 + 25 CU候选引用写回 / 未落账>
补充原始需求材料：<无 / YYYYMMDD-STR-E名称-补充原始需求材料.md>（已登记 OR 原料状态表）

一、方案反馈
  A. 整体确认 → 回复「整体确认」，快捷同意全部未标注条目
  B. 局部修改 → 在确认状态中标注 [修改]：...
  C. 驳回重做 → 在确认状态中标注 [驳回]：...

二、下一步
  本Skill → 选择 FR-ENG OR 或 `需wft01修订` 的 STR-E 节点重新运行
  后续    → STR-E-XXX（可以分解分配）、STR-E-ZZZ（待补充分解分配）→ wft02-eng
```

**输出后不要结束对话**，等待人类反馈。

---

## 三、AI 标记约定

四类增量标记（`[新增]`/`[变更]`/`[确认]`/`[需裁决]`）的定义详见 [91 规范 §A.3.1](../91-eos-biz-eng-spec.md#a31-ai-增量标记)。

每次 Step 3 完成后，向人类输出增量清单：

```text
=== STR-E-XXXX 本轮更新清单 ===

[新增] 承接 OR-ENG-001, OR-ENG-002（共2条，类型：配置生成类）

能力链
  [新增] 流程配置意图 → 校验保存 → 发布装载 → 单据页流程按钮与节点能力可用
  CU 候选
    [新增] "流程节点配置"（@engine-flow）  来源：OR明示
    [新增] "流转规则配置"（@engine-flow）  来源：OR隐含

完备性检查
  能力链闭合 ⚠
  → 补充 FR-ENG 材料: 20260720-流程发布配置补充原始需求材料.md
```

---

## 附录A：判据速查

### A.1 STR-E 归组三元组 + FR-ENG OR 五种类型

**归组锚点**：`主责能力域 + 配置/治理目标 + 可独立验收结果`。主责类型分引擎专属和平台共享。

**OR 类型**（不用于划分 STR-E 边界，仅作 OR 级特征标注）：

| 类型 | 触发源 | 场景终点 |
|------|--------|---------|
| 配置生成类 | 配置人员提出或维护引擎配置 | 配置通过校验并在运行期生效 |
| 构件扩展类 | 业务页面需要新增构件能力 | 目标布局组件可渲染该构件 |
| 布局组件扩展类 | 现有布局组件无法承载 | 新/扩展组件可被引擎调用 |
| 横切治理类 | 权限/审计/版本等治理需要 | 横切规则对目标对象稳定生效 |
| 运行支撑类 | 业务页面需要引擎能力调用 | 引擎能力可被调用并产生可追溯结果 |

### A.2 能力链四段

```
配置/治理意图 → 系统处理要求 → 运行期制品/构件/功能 → 可用性确认
```

### A.3 CU 候选来源类型

| 来源类型 | 含义 |
|---------|------|
| `OR明示` | OR 文本直接说出该 CU |
| `OR隐含` | 不推出该 CU 则能力链存在逻辑缺口 |
| `构件缺口推断` | 现有构件无法满足，推断需要新构件配置 CU |
| `布局组件缺口推断` | 现有布局组件无法承载，推断需要新布局组件配置 CU |
| `同类引擎推断` | 同引擎类型已有 STR-E 的类似 CU 模式 |
| `模型线索推断` | 25 资产中已有匹配 CU 定义，但 OR 未提及 |

### A.4 CU 候选粒度判断

| 判定 | 说明 |
|------|------|
| `可展开` | 粒度适合 wft02-eng 直接展开 |
| `过粗待拆` | 需要拆分为多个独立 CU |
| `过细待并` | 应合并到已有 CU |
| `边界待确认` | 与已有 CU 的边界不清 |

### A.5 Phase B 场景匹配结果

| 结果 | 判定 | 动作 |
|------|------|------|
| 场景匹配 | 三元组一致 | 进入 CU 关系检测 |
| 同域不同场景 | 能力域相同但目标/验收不同 | 匹配其他 STR-E 或新建 |
| 共享依赖 | 能力由已有共享 STR-E 提供 | 写入依赖关系，不复制 CU |
| 主责不匹配 | OR 归属其他能力域 | 退回待聚合池 |

### A.6 Phase B CU 候选关系检测

| 关系 | 判定 | 处理 |
|------|------|------|
| 确认 | CU匹配+引擎相同+来源非OR明示 | 来源升级 |
| 无新增 | CU匹配+全部已OR明示 | 追加引用+增量合并 |
| 引擎归属变更 | CU匹配+引擎不同 | 更新引擎+变更原因 |
| 补充 | CU不匹配 | 新增到候选清单 |
| 过时 | 基线CU未被本轮覆盖 | `[过时]`+保留不删 |

### A.7 STR-E 完备性判据

| 检查项 | 判据 | 缺口处理 |
|--------|------|----------|
| 能力链闭合 | 配置意图能走到运行期可用 | 生成补充 FR-ENG |
| 主责归属明确 | 只有一个主责能力域 | 标记 `需澄清` |
| 场景可独立验收 | 目标和结果可独立判定 | 合并或降为依赖 |
| 共享不重复 | 共享 CU 只在共享 STR-E 定义一次 | 删除重复 CU |
| CU 可展开 | 候选足以让 wft02-eng 定位 | 标记 `[需裁决]` |
| 缺口层级正确 | 构件/布局组件/CU 级区分清楚 | 改写缺口说明 |

### A.8 STR-E 节点生命周期状态流转

```
待确认方案 ──人类确认──→ 可以分解分配 ──wft02锁定──→ 在分解分配 ──wft02完成──→ 已分解分配
     ↑                        ↑                         │
     │                        │               wft02退回  │
     │                        │                         ↓
     └─── wft01修订 ────── 需wft01修订 ←───────────────┘

上游变更分流：
  可以分解分配 → 可以分解分配（版本递增）
  在分解分配   → 在分解分配（版本递增）
  已分解分配   → 待补充分解分配
```

---

## 附录B：脚本接口速查

| 脚本 | 用法 | 说明 |
|------|------|------|
| `read-section.sh` | `bash ../scripts/read-section.sh <文件> <分节名>` | 提取 ##/### 分节完整内容 |
| `read-node.sh` | `bash ../scripts/read-node.sh <文件> <节点ID>` | 按节点ID提取节点块 |
| `detect-changes.sh` | `bash ../scripts/detect-changes.sh <文件>` | 检测人类自上次 AI 运行以来的文档变更 |
| `update-meta.sh` | `bash ../scripts/update-meta.sh <文件> <操作>` | 维护文件元信息（bump-version / update-head / add-recent-change / move-node） |

所有脚本路径相对于 `eos-wft01-eng-or2str/` 目录。

---

## 变更记录

| 日期 | 版本 | 说明 |
|------|------|------|
| 2026-08-19 | v1.4 | 人类方案 Step 框架对齐 wft01-biz（v8.8）同步——Step 3 标题去 STR-E 前缀（「场景业务设计」）、Step 4 标题改名（「FR-ENG 需求增补」）。AI 执行规则语义不变 |
| 2026-08-19 | v1.3 | 人类方案原理深度分析落定（v8.6）同步——Step 4 补充 FR-ENG 材料生成补管道句（与 wft03-biz 缺口线索同一管道：经确认 + ort00→ort03 转正式 FR-ENG OR，不豁免预处理链）。AI 执行规则语义不变 |
| 2026-08-19 | v1.2 | 人类方案原理与方法审视修复（v8.5）同步——Step 4 能力链闭合检查三段→四段（配置/治理意图→系统处理要求→运行期制品/构件/功能→可用性确认，对齐 §2.2.1 四段）；Step 5 补 git 提交基线（顺序：AI最近变更 → git add+commit → 文件头，链级不变式，对齐人类方案 §5.6）；Phase C 定义能力场景范围补「终点=OR 显式覆盖、不得在终点后扩展」。AI 执行规则语义不变 |
| 2026-08-19 | v1.1 | 人类方案知识层三章重构（§二 概念 / §三 原理与判据 / §四 节点演进，对齐 wft01-biz v3.13）同步——Step 2 补「反馈双轨」（AI 对话反馈 + 线下文档修订经 git diff 检出，两轨等价，对齐 91 §A.5 v5.20）；Step End AI 处理反馈规则表补「线下修订检出」行；human spec § 引用迁移（§2.4.1→§3.2.1 / §2.4.3→§3.2.3 / §2.5.1~2→§3.3.1~2 / §2.5.3→§3.3.3）。AI 执行规则语义不变 |
| 2026-07-20 | v1.0 | 初始版本——从人类方案文档 v8.2 提取 Skill，脚本化数据访问，领域知识引用人类方案 |
