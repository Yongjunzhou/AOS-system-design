---
name: feedback-validation-basis-intended-use
description: 确认（validation）的基准是产品的预期用途与使用，不是关切——关切管"漏没漏"，预期用途管"对不对"
metadata:
  type: feedback
---

用户 2026-09-24 裁定的**判据口径**：

> **确认的基准是产品的预期用途和使用，而非关切。**

**Why（我错在哪）：** 回答"为什么要开发相关方的关切"时，我援引 SEBoK《Stakeholder Needs Definition》的一句——`The outcome of the Stakeholder Needs Definition process is used as **the basis of System Validation**`——把它读成"**关切是确认的基准**"。这是把**输入**当成了**尺子**：SEBoK 那句话说的是"需要集合将作为确认的输入／对象之一"，而**判据（尺子）在标准里另有明文**，且不是关切。用户在下一轮直接点出。

**★ 出处位（用户 2026-09-24 追加裁定）：确认的依据来自 ISO 9000。** 即——**判据（尺子）一律以 ISO 9000 为准**，取其**术语标准**的性质：定义句即判据句。三级出处不可混引：

| 位 | 标准 | 取什么 | 不可取什么 |
|---|---|---|---|
| **依据位** | **ISO 9000:2026**（本项目存全文，含中英对照，属**一手**） | 术语与判据逐字——§3.11.14 确认／§3.11.12 验证／§3.11.13 试验 | — |
| **旁证位（过程侧）** | ISO/IEC/IEEE 15288（§6.4.11） | 谁在何时做、过程目的、产出物 | **不作判据依据**——它是**过程**标准，且其 purpose 为**开放模型**（objective／intended use／environment 并收），判据字面不收在 requirement 内 |
| **旁证位（阐释侧）** | SEBoK 等知识库 | 背景、机制解释 | **属二手性质**，其 "basis of System Validation" 一类措辞不得读成判据 |

（本项目 23 号 §2.1 已定：ISO 9000 与 15288 **不矛盾，是词法归属差异**；差别在 15288 承认参照系可以先于／大于需求，而 ISO 9000 的判据仍收在 requirement 内。落地引用时**以 ISO 9000 为据、以 15288 为旁证**。）

**正确口径（现行标准逐字＋本项目 23 号已定案）：**

- **确认的尺子＝「为特定预期用途或应用的要求」**。ISO 9000:2026 §3.11.14 逐字：*confirmation, through the provision of objective evidence, that **the requirements for a specific intended use or application** have been fulfilled*（通过提供客观证据，证实**针对特定预期用途或应用的要求**已得到满足）。ISO 9001:2015 §8.3.4 d）落地口径：确认＝产品和服务满足**预期用途**需求。
- **必须在"使用"中兑现**。ISO/IEC/IEEE 15288:2015 §6.4.11.1 逐字（本项目 23 号所引）：*objective evidence that the system, **when in use**, fulfills its business or mission objectives and stakeholder requirements, achieving its **intended use in its intended operational environment***；ISO 9000:2026 §3.11.14 注 3：**使用条件可真实、可模拟**。故"预期用途"＋"使用（情境／条件）"两件都要。（15288:2023 §6.4.11 条款号已核，**逐字未取**。）
- **关切的位置不是这里**：关切是①视角选择的锚（42010 的机制：视角 frames 关切、视图 addresses 关切）、②漏项检查的雷达、③需要与需求的来源。**关切不可验证、随人走、且互相冲突**（关切随立场走、需求随系统走；换人测试即此意），不能充当判决基准——冲突的东西只能当输入，不能当尺子。
- **判据在派生链之外**（23 号 §9.1）：预期用途的主体常是**未被显性化的隐含需求**（generally implied 支），需求基线只承载 stated；故确认须另配一个与派生链**异构**的参照层，载体是 **use specification／ConOps／使用情境／用例**，而不是逐条需求。
- **译名纪律**：`intended use or application` → **预期用途或应用**；「预期的使用」是**误导性译法**（use 取目的侧"用途"，不取动作侧"使用"）。本裁定里的"**使用**"指 `when in use`／使用情境与使用条件，与上述译名纪律不冲突。

**一句话**：**关切管"漏没漏"，预期用途管"对不对"。** 与本项目 32 号元规则「**判据对目标量，关切点管不漏**」同构——我上一条自己引了这条元规则，却没把它用到确认上。

**常见违例（见到即改）**：把 SeBoK 的 "basis of System Validation" 读成"关切是确认基准"／把确认的尺子写成"利益相关方需要与期望"（那是来源不是尺子）／把确认的尺子写成"目标"（目标是**评审**的尺子，ISO 9000:2026 §3.11.2；23 号已更正过 17 号等处）／把 use 译作"使用"而丢了"用途"。

**相关**：[[feedback-function-term-translation]]（同期裁定，同属译名与口径分寸）；本项目 23 号《判据体系研究报告》§2.1／§4.5／§5.1／§9.1／§10.7（判据阶梯五级与"链外两物"）、32 号 §6~§7（四类出口与元规则）。
