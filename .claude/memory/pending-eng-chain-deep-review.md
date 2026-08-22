---
name: pending-eng-chain-deep-review
description: eng 链深审已执行 + A1 树 4 层架构升级落地（配置信息组=末级=PL5）——2026-08-22
metadata:
  node_type: memory
  type: project
  modified: 2026-08-22
---

用户计划**新开对话深入审视 eng 链，重点关注业务链**（2026-08-22 定，biz 链深审完成后）。

**2026-08-22 深审已执行 + A1 树 4 层架构升级落地**（人类逐项裁决后实施）。深审结论：①五大重点关注项（FR-ENG 线索回路 / FR-BIZ 指标约束包 / CU 设计权 / biz↔eng 对称性 / 并行路径）全部闭环；②内部引用/锚点无悬空（B 组干净）；③核心发现并裁决升级——**配置信息组是 A1 产品树真正的末级节点**（可独立交付/验收的能力单元），A1 树 4 层（产品→引擎→CU[PL4]→配置信息组[PL5 末级]），A1 无 WBS（Bn 保留）；④同批：A1 锁定态全链操作化（wft02/wft03/wft05 补「锁定写回」，对齐 wft04 E5）+ C1（wft04/wft05 SKILL `PA层待处理-*`→`PA层收敛-*`）+ C2（wft02 SKILL Step End 占位）+ D2（wft05 Q2/Q3→Q2/Q3/Q4）。详见 [[eng-chain-five-layer-framework]] 架构升级段。

**当前版本（2026-08-22 深审+架构升级后）**：wft01-eng v9.7 / wft02-eng v10.2 / wft03-eng v9.2 / wft04-eng v1.1 / wft05-eng v10.2；SKILL wft01 v1.12 / wft02 v1.11 / wft03 v1.6 / wft04 v1.2 / wft05 v1.5。91 规范 v5.31。对照文件 = `20-pl4eos/10-pl4eos-subpl-sysdev/10-wfsysdev-4-eos/eos-wft0X-eng-*.md` + 各 SKILL。

**「重点关注业务链」理解**（待新会话与用户确认口径）：聚焦 eng 链与 biz 链的**衔接/承接/对称性**——
- **FR-ENG 候选线索回路**：wft03-biz 产出 FR-ENG 候选线索 → ort00→ort03 → wft01-eng（91 §4.4/§10.1 门禁），核对回路两端口径
- **FR-BIZ 指标约束包**：wft03-biz 装配 → wft05-eng 消费（§10.2 跨路径依赖），核对约束包格式/消费契约是否一致
- **CU 设计权**：biz 不得设计 CU（91 §3.3/§10.1），eng 五步设计 CU（wft01 承接→wft02 详设→wft03 功能概要→wft04 组件业务→wft05 三类组件），核对边界
- **biz↔eng 对称性**：输出文档↔CU（各自 PL5 末级）、wft03-biz 配置需求方案↔wft03-eng 功能概要/wft04-eng 功能详细（同写 05）、STR-E 双重身份（A2 业务配置人员场景业务/A1 能力场景，91 §5.1/§八）
- **并行路径**：91 §10.1 全景图 biz/eng/nfr 三路径并行 + 汇合条件（wft05-eng 同时消费功能详细 SR-F + FR-BIZ 指标约束包 + NFR 约束包）

**复用 biz 链深审的方法**（上一轮 b86266a 已提交）：①锚点机械比对（跨文件 `#锚点` 是否截断/失效，§x.y.z 是否悬空）；②**资产结构核对**（biz 轮重大教训：wft03 §5.6 的 26→24 流程定义机制建立在 24/26 不存在的资产结构上——eng 链的 25 引擎资产 / 26 文档定义 / 28 看板指标消费前需核对实际字段结构）；③SKILL 与主文件执行规则一致性（biz 轮发现 wft03 SKILL 写回表与主文件 v9.8 矛盾）；④语义承接审查（STR-E→BP(A1)→功能概要→功能详细→PA 的映射）。

**提示**：eng 链五个 SKILL 最新变更记录多在 2026-08-21（主文件已到 v9.6/v10.1/v9.1/v1.1/v10.1），SKILL 同步状态需核对（biz 轮三个 SKILL 均落后主文件两版）。eng 链 02 详设基准 = Downloads PDF v1.5.2（记忆 [[eng-chain-five-layer-framework]]）。

相关：[[pending-biz-chain-deep-review]]（biz 链深审已完成，C 组六项口径留待下轮）、[[eng-chain-five-layer-framework]]、[[skill-step-framework-unify-biz-standard]]。
