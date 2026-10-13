---
name: ch11-real-examples
description: 上网检索"符合新标准架构定义（42010:2022 §3.2 两块）"的公开范例——判据、六类候选与出处链接、证据等级、三项待裁
metadata:
  type: progress
---

# ch11 真实范例检索：符合新标准架构定义的公开范例（2026-10-13）

> **性质**：**进行中的工作**（`progress-`）。起因＝用户令「**你上网搜，找找符合新标准架构定义的范例**」。**本轮只检索、只回话，未改任何正文、未落库**。
> **准绳**（唯一）＝ ISO/IEC/IEEE 42010:2022 **§3.2** 两块：**X 块**＝实体在其环境中的**基本概念或属性**；**Z 块**＝管住该实体及其**相关生存周期过程**怎么**实现**、怎么**演化**的**管控原则**。配套：42020:2019 **§8.2 c)**（概念化成果句）／**§8.4 e) f)**（制定 principles 与 precepts、implications）／42010:2022 **§5.2.2**（*can pertain to*＝外延不是产出）／15288:2023 **§3.13 名词 design**＋**§6.4.5**（元素与关系的规格归**设计定义过程**）。

## 一 筛选两问（本轮一切判断按此）

1. 它给出的是不是**这两样**——基本概念或属性 ＋ 管控原则？
2. 它有没有把**元素与关系／结构图**当**架构本身**（那样是**设计**，不是架构）？

**两条互相独立的轴**：(a) **定义口径**合格（架构是什么）；(b) **描述结构**合格（42010 §5／§6 的 AD 要件：相关方／关切／视角／视图／模型种类／对应关系／理由）。**多数公开件只过一条轴**。

## 二 标准自带的范例（一手，本机正本可逐字复核）

| 位置 | 内容 |
|---|---|
| 42010:2022 §5.4（md L517~L545） | 相关方视角 **5 例**；方面 **3 例**（飞机／计算机／通信网） |
| 42010:2022 §5.4／附录 C（L1537~L1541） | 视角与模型种类例：**ArchiMate**（层×方面×基础视角）／**SysML**（图类型＋一等构造）／**UAFP** |
| 42010:2022 附录 A（L1477~L1505） | **整车 AD 例**：软件应用视图件 × ECU 视图件的**对应关系**（矩阵，Fig A.2）＋对应方法 M1／M2／M3／M4 |
| 42010:2022 附录 C（L2025／L2089） | 架构框架清单；**RM-ODP 五视角**（enterprise／information／computational／engineering／technology） |
| 42010:2022 §5.6（L963） | **视图之外**的 AD 信息可含**架构原则、模式、风格、理由**——"原则"在描述里的位置 |
| 42020:2019 §8.4（L2048／L2052） | **EXAMPLE 1**＝"架构可按原则规定：各元素用同一处存数据"；**EXAMPLE 2**＝precept"钩子" |
| 42020:2019 §8.2 c)（L1582） | 成果句：*key concepts and properties, and the principles guiding its formulation, application and evolution* |
| 42020:2019 §8.4 例（L2104） | 概念化工作产品可记为 problem formulations／solution structures／**principles and guidelines** |

**用途**：教材里最省事的范例（自带标准语汇、可逐条对表）；**缺点＝碎片化，不是完整 AD**。

## 三 定义口径合格的真实范例（公开、可引）

| 范例 | 为什么合格 | 出处 |
|---|---|---|
| **NORA**（荷兰政府参考架构）★ 最贴 | 定义句**逐词对应** 2022 两块（注：英文版用 entity，本定义译为 object）；明文**架构≠设计**（ontwerp＝未来现实的表征）；内容组织＝**架构原则→含义（implicaties）→核心价值观／质量目标**；原则定义＝"基于一种信念的、普遍适用的基本规则" | [定义页](https://begrippen.noraonline.nl/basisbegrippen/id/begrip/architectuur)｜[原则总览](https://www.noraonline.nl/wiki/Architectuurprincipes)｜[全部原则](https://www.noraonline.nl/wiki/Alle_Architectuurprincipes) |
| **W3C《Architecture of the World Wide Web, Vol 1》**(2004) | 三块基本概念（identification／interaction／formats）＋成体系的 principle／constraint／good practice **总表**＋§5 General Architecture Principles | [w3.org/TR/webarch](https://www.w3.org/TR/webarch/) |
| **RFC 1958《Architectural Principles of the Internet》**(IAB 1996) | 互联网架构＝一组原则（目标 connectivity／工具 IP／智能 end-to-end）＋演化原则；并明说"运行代码的工程反馈比任何架构原则更重要" | [rfc-editor.org/rfc/rfc1958.txt](https://www.rfc-editor.org/rfc/rfc1958.txt) |
| **Fielding《REST》第 5 章**(2000) | 架构风格＝**一组约束**（client-server／stateless／cache／uniform interface／layered／code-on-demand）；三种视图（process／connector／data）＋元素表 | [ics.uci.edu/…/rest_arch_style.htm](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm) |

**共同点**：实体是公共基础设施，架构**几乎全部由基本概念＋原则承载**，没有"结构图当架构"。

## 四 描述结构合格的 AD 范例（真实项目／完整 AD）

| 范例 | 现状 |
|---|---|
| **Health-Watcher AD**（42010/IEEE 1471 编者 Rich Hilliard 的示范件） | 最经典的完整 AD 范例；**本次取不到原文**（iso-architecture.org 两次 fetch 失败）；且属 **2011 时代件**——结构可借，定义口径不可照抄 |
| **欧盟项目交付物** | ORCHESTRA2020 [D3.1](https://orchestra2020.eu/wp-content/uploads/2021/07/D3.1-Initial-use-cases-for-multimodal-traffic-management.pdf)（明说"架构描述遵循 ISO/IEC/IEEE 42010"）／[D3.3](https://orchestra2020.eu/wp-content/uploads/2021/07/D3.3-Final-PMA-for-multimodal-traffic-management.pdf)（用 entity of interest）／[DEMETER D3.1](https://h2020-demeter.eu/wp-content/uploads/2020/10/D3.1-DEMETER-reference-architecture_v1.0.pdf)／[ICOS D2.2](https://icos-project.eu/files/deliverables/D2.2_ICOS_Design_v1.0.pdf)／[NEPHELE D2.2](https://nephele-project.eu/sites/nephele/files/public/content-files/deliverables/nephele_d2.2.pdf)——**证据等级＝搜索索引片段（PDF 本机取不了全文）** |
| **学术案例** | 格罗宁根大学学位论文（[Complete_thesis.pdf](https://research.rug.nl/files/20570212/Complete_thesis.pdf)，含 ATD viewpoints × concerns 表）；IEEE 2025《[An ISO/IEC/IEEE 42010:2022 Standard-Based Adaptation for Systems-of-Systems](https://ieeexplore.ieee.org/abstract/document/11024185)》（付费墙，仅摘要级） |
| **模板** | [jam01/SDD-Template](https://github.com/jam01/SDD-Template)（IEEE 1016-2009 ＋ ISO/IEC/IEEE 42010 模板）——空白骨架，非范例内容 |

## 五 看着像、其实不合格（防误用）

- **arc42／C4 model**：构件／运行时／部署视图为主，是**设计口径的结构安排**，不分架构与设计，无 Z 块。
- **各类"架构图集"**（Kubernetes、云厂商架构文档）：实现结构＋组件交互，实体／关切／原则不成体系。
- **云厂商 Well-Architected 类框架**（AWS／Azure／Google）：有原则（Z 块），但**没有单一实体与关切集**，属框架／清单。
- **Gaia-X Architecture Document 3.1**（[docs.gaia-x.eu](https://docs.gaia-x.eu/technical-committee/architecture-document/latest/)）：真实、公开、可读（本轮读了 Gaia-X context 全节），但按**生态／规则／信任框架**组织，**未命中 42010 两块定义**——要用须注明。
- **TOGAF 原则模板**：pubs.opengroup.org 返回 **401**，本轮未取到原文。

## 六 待裁三项（未决）

1. **是否落库**：以上要不要整理成研究报告（如 37 号）或独立的"真实范例清单"，落 `00-系统工程相关研究报告/`？现在**只在对话里＋本记忆**。
2. **取不到原文的件怎么办**：Health-Watcher（站点不可达）与各 PDF（本机 web_fetch 不支持 `application/pdf`）——是换链接／找镜像，还是只按片段级证据用？
3. **是否并入 ch11 阶段三／四取料**：ch11 正缺"读者可见的机制链"的实例（见 [`pending-ch11-revision-35.md`](pending-ch11-revision-35.md)／35 号 §⑥⑦⑬⑰）。

## 七 合规判定（2026-10-13 追加·应"这些范例合乎标准吗"）

**★ 结构性事实（一切判定的前提）**：42010:2022 **Clause 4** 只给**五种合规主张**——**AD（Clause 6）／ADF（7.1）／ADL（7.2）／架构视角规格（8.1）／模型种类规格（8.2）**，且**"裁剪既不需要也不允许"**（正本 L407）。**"架构"本身不是合规判据**（§3.2 只是术语）；标准也**不**规定架构或 AD 的质量条件（Annex A L1289，那是评价的事）。故"合不合标准"**必须先问以哪种身份**。

| 档 | 范例 | 定义口径（§3.2 两块） | AD 要件（Clause 6） | 判定 |
|---|---|---|---|---|
| 1 | 附录 F 的 ADF 清单（GERAM／**IIAF**／4+1／NAF／DoDAF／OASIS SOA RAF／RM-ODP／TOGAF／UAF／Zachman）；RM-ODP 五视角 | — | — | **标准自己认可**：正本 L2011"Each of them conforms to applicable requirements of **7.1**"；附录 C.7 五视角可作合规 AD 的视角来源（L1803） |
| 2 | NORA｜W3C webarch｜RFC 1958｜REST | **对齐**（两块在；NORA 逐词对应） | **不成立**（无相关方／视角／视图／对应关系／理由装置；NORA 本轮未读到这套要件） | **合的是"定义"，不合的是"描述要求"**——不可写成"符合 42010:2022 的范例" |
| 3 | Health-Watcher｜EU 交付物｜IEEE 2025 论文｜SDD-Template | 2011 口径或未核 | 自称参照、非合规主张 | **2011 合规 ≠ 2022 合规**（2022 新增 model kinds 等合规案例，正本 L141）；"follows the guidelines"是方法参照，非 Clause 4 主张 |
| 4 | arc42｜C4｜云厂商图集｜Well-Architected｜Gaia-X 3.1 | — | **不合** | arc42 第 5 节原文即"structure of source code, modularization"（设计范畴）且无 Clause 6 装置；C4 是画图模型（可作 §8.2 模型种类素材）；Gaia-X 按生态／信任框架组织（已读原文，未命中两块） |

**★ 本书要防的混合错误**：把档 2 当"符合标准"来写，等于把**定义位**与**描述位**缝成一条——与"只盯定义、不许偏差"的准绳相抵。ch11 的正确用法＝它们只示范"架构＝概念或属性＋原则"这**一半**（定义位）；描述位要用档 1 或按 Clause 6 逐条核过的 AD。

## 八 第二轮深挖（2026-10-13）：四路代理 ＋ 主笔自查 —— 结论与交付物

**展示件（本工作件，§一~§八 全记录）**：`.work-ch11/真实范例核查-展示件.md`。

### 8.1 取用办法（两轮踩出来的，后续复用）
- **绕行代理**：`https://api.cors.lol/?url=<URL编码>` → 可取 **Wayback 快照**与直连不通的站点（有 429 速率限制，需间隔重试）；`api.allorigins.win` 到 archive.org 返 522。
- **★ PDF 现在能读（有限制）**：`https://api.cors.lol/?url=https%3A%2F%2Fr.jina.ai%2F<URL编码的目标PDF>` → 先转 Markdown 再取回（不再触发 `unsupported content type`）。限制：429 速率限制；**图不可见**（故 6.7／6.8 的 view component／legend 仍不可判）；**Zenodo 经此仍 403**。
- 直连可用：w3.org／rfc-editor.org／noraonline.nl／saf.gfse.org／omg.org／docs.oasis-open.org／arc42.org／bundeswehr.de（PDF）／softsysarchitect.net。直连不可用：iso-architecture.org、web.archive.org、dodcio(403)、pubs.opengroup(401)、github raw、cloud.google.com、c4model.com。

### 8.2 判定结果（四档，详见展示件 §三、§七、§8.3）
- **A＋B 双满足＝0 件**（两轮合计逐件判定 **60+ 件**）。
- **双双最接近＝HEDGE-IoT D2.4**（Horizon Europe 101136216，2026，170 页，全文已读）：明文 `2.2 ISO/IEC/IEEE 42010:2022 Model`；Z 块"Design Principles Established:"；X 块 `4.1 Architecture Vocabulary and Concepts`＋五层概念栈；B 侧关切明文／`TABLE 21 – VIEWPOINT SUMMARY`／**correspondences 明文**／`4.5.1 Architecture Overview and Design Rationale`。**A、B 均判"部分"**（A：原则未逐条挂到实体属性论证；B：缺 6.3／6.6 七要素／6.7-6.8 model kind 与 legend）。
- **描述位**最能站住：**OASIS SOA-RAF**（唯一逐条落实 1471 六要件；缺口＝2022 新增件）｜**GfSE SAF**（`Concern｜Stakeholder & Rationale｜Viewpoint` 三列表，形态基准；明文引 **ISO 42010:2022**，但 Standard Traceability 挂 15288:2023＋SEHB V5）｜**UAF 附录 B Sample Problem**（v1.2＝formal/22-07-09，v1.3＝formal/25-10-06；PDF）。
- **定义位**最能站住：**NORA／GEMMA 定义条目**（＝2022 两块，且明文架构≠设计）｜**W3C webarch**（概念＋原则总表）。**★ 版本分野的现实证据**：GEMMA 术语浮层仍用 **2011 版**定义式（belichaamd in zijn elementen, relaties…）——同一荷兰体系两版并存。
- **★ 官方侧自降**：42010 官网"Using ISO/IEC/IEEE 42010"清单里，**Health-Watcher 自称 "work-in-progress in need of completion/update"（CD1 草案）**，**SBSCS AD 自称 "the `hello world` equivalent"**。
- **★ ECSS 定论**：现行 144 项标准**无 architecture 标准**；ECSS-E-ST-10C Rev.1 **全部 DRD 无 ADD，只有 DDF／DJF／System concept report／Function tree／Specification tree** → **ECSS 走 15288 式设计定义路线**（"架构≠design"在标准体系层面对上）。
- **B 侧最有力**：**GEMMA Architectuurprincipes**（唯一 rationale 明文）｜**GC Service & Digital Target EA Whitepaper**（stakeholders＋principles＋concerns 同现）｜**ISO/IEC 30141:2024 ED2**（唯一明文 "conformance with ISO/IEC/IEEE 42010:2022" 的标准，摘要级）。
- **判据 A 的区分力实测**：EU "Architecture Definition"、NASA ADD、O-RAN AD、3GPP System architecture（**§4.1 实际标题＝"General concepts"**）大多落在 A 明确排除的那一类；公开侧名为 architecture 的文件绝大多数是"结构＋接口型"或"战略框架＋条目型"，**概念层常被外置**（ICAO 在 GATMOC Doc 9854、ECSS 在 System concept report）。
- **产品数据（机读）**：**UAF XMI（元模型）**｜**AD42010 Metamodel & UML Profile（Sparx .eap，待核）**｜**NORA 原则导出（json/csv/rss/rdf）**｜**GfSE SAF 的 SysML 规格与 Profile（框架层）**；**实例级 AD 数据件仍无公开件**。
- **A 路其余**：Hilliard 的 **ADCA**（`softsysarchitect.net/adca/`，已读原文）＝42010 合规评估方案，已发 **ArchiMate 2.1／GSAF v1.0／TOGAF 9.1** 三份 conformity forecast（对象是**框架／ADL**，且自称不能作符合性依据）；ADMBW↔NAF4↔UAF↔SAF 映射页（`saf.gfse.org/userdoc/mapuaf2saf.html`）确认四体系互映、**concern 已进其词汇层**。

### 8.3 交付物（外部检索报告，**未编号、未裁决**）
`00-系统工程相关研究报告/架构交付物检索-42010符合性逐件判定-2026-10-13.md`（145 KB）｜`00-系统工程相关研究报告/架构交付物检索-目标3-航天国防交通-2026-10-13.md`（58 KB）。**均属工作件**，是否并入正式编号（如 37 号）或移入 `.work-ch11/` **待用户裁**。

### 8.4 待裁（五条）
①是否落库为编号报告；②取不到原文／片段级件如何处置；③是否并入 ch11 阶段三·四取料；④两份检索报告放哪；⑤HEDGE-IoT D2.4 要不要升"满足"（需再取 `TABLE 21` 表体与 4.5.2 视图件，受速率限制与"图不可见"两条限制）。

### 8.5 C 路（MBSE 产品数据）要点 —— 机读件最好的三件

- **★ EIRA v7.0.0（欧盟 [code.europa.eu/eira/eira](https://code.europa.eu/eira/eira)）＝本轮"产品数据"最强件**：三件套 `.archimate`／`.xml`（ArchiMate 交换 4.98 MB）／**`_SKOS.rdf`**。`.xml` 每个 ABB 的 documentation 带结构化字段：**`LOST view:`／`Interoperability Saliency:`（管控理由）／`Interoperability Dimension:`／`Viewpoint: …viewpoint`／`EIF Layer:`／`Areas of concern per role`**；SKOS 顶层概念逐字含 **`view`／`viewpoint`／`iopDimension`／`adr_decision`／`iopSaliency`／`EIFPrinciplePrinciple`**。**A＝部分（中）／B＝部分（较强：6.4、6.5、6.6、6.7/6.8；缺 6.2、6.9、6.10）**。
- **GfSE SAF-SysMLV2**：20 具名 stakeholder（带 doc）／≥30 concern（带 doc＋绑定）／~50 viewpoint（frame concern，**但除 `SystemContextDefinitionViewpoint` 外 purpose doc 皆空**）／view＋`render`／FFDS 示例模型 → **B＝部分（较强：6.2/6.4/6.6/6.7/6.8；缺 6.1/6.3/6.9/6.10）**。
- **UAF 1.2/1.3 XMI**＝公开文件里 Clause 6 构造最集中者（包注解 *"Stakeholders: …"*／*"Concerns: …"*／`…Viewpoint`），但**是 Profile 规格**（A 不满足），B 部分。
- **★ 实证"规格能装 ≠ 数据件装了"**：`archimate3_View.xsd` 能承载 6.2/6.4/6.6/6.8（`ViewpointType{concern*,viewpointPurpose,…}`＋`ConcernType{stakeholders?}`），而官方 **ArchiSurance** 里 9 条 `Principle` **全无 documentation**、`viewpoint="N"` 是整数编码、**Stakeholder／Concern 0 处**。
- **DoDAF DM2 PES**：现役四个 XSD **全部 CAC Required**；官方原话"examples … available to DM2 Working Group members" → **公网无官方示例架构数据**；唯一疑似＝`DataPhrase_To_DM2 Database with Sample Data_r1.accdb`（未打开）。
- **★ B 的三处普遍缺口（全批统计）**：**① 6.9 对应关系与对应方法——0 件填"对应方法"；② 6.6 的"模型种类与 legend／典型相关方／来源"——只有 SAF 一件填了来源；③ 6.10 决策与理由——只有 SysML v2 `@Rationale`／AADL goaldoc `rationale`／EIRA SKOS `adr_decision` 三处且非结构化。**
- **可得性分级**：公开可下＝ArchiSurance／Open Group 示例／GEMMA 七 xml／EIRA／SAF／AADL osate examples／Capella samples／SysML v2 示例；需注册＝Open Group C19C ZIP；**需 CAC＝DoDAF DM2 PES 全部 XSD**；需 DM2 WG 成员＝DoDAF 官方示例 XML；已死＝IDEAS Group 站点、AGA 旧域名。
- **待补证三处（最易得→最有价值）**：① `GfSE/SAF-Specification/_data/*.json`（尤 **`rationales.json` 211 KB**；主笔试 jsdelivr 两路径均 **404**，正文未取到）② `DataPhrase_To_DM2 …Sample Data_r1.accdb` ③ **`AD42010 Metamodel and UML Profile`（apg.box.com）**。

### 8.6 A 路终报 ＋ C 路更正（交叉校正要点，2026-10-13）

**官方示范件：全数「无法判定」（PDF 是硬边界）**——Health-Watcher AD（官网自述 *"work-in-progress in need of completion/update"*，CD1 草案；片段 *"tbd: This is a mixed bag of diagrams and tables"*）｜SBSCS AD（官网称 *"the `hello world` equivalent"*）｜SBSCS Example AD（Wayback 返回 *"[HTML content omitted: unable to convert safely.]"*）｜**UAF Sample Problem**（实体＝**民用海上搜救 SAR，场景 "Yacht in Distress"**；v1.3＝`formal/25-10-06`、v1.2＝`formal/22-07-09`、v1.1＝`dtc/19-06-18`）｜**RM-ODP 是唯一"标准本体带具名系统示例"的 ADF**：**ITU-T X.906 Annex A＝Templeman Library system**（五视点全套）、**X.901 §12＝四例**、**X.911 Annex B**（目录级已读官方原文）｜ArchiSurance Y163／ArchiMetal Y164／NAF v4.1／IIRA／GERAM(404)／Kruchten。

**★ 用词级更正**：UAF 官方原话是 *"are **aligned with** ISO/IEC/IEEE 42010:2011"*，**不是 "conform to"**；该句在 1.0／1.1 页不存在。**凡写"UAF 符合 42010"＝改写升级。**
**★ "示例模型数据"＝确认级否定**：OMG `machine-readable` 清单**只有 8 行元模型／测量库**；厂商侧唯一可下载模型类是 Astah **空模板**（*"diagrams … with empty contents"*）；Sparx 仅一张 SAR 视图件 replica。
**★ 框架≠AD 的官方反证句（可直接进教材，均已读原文）**：DoDAF *"independent of any specific agency"*｜Zachman *"IS NOT a methodology … IS the ontology"*／*"is a metamodel"*｜ISO 15704:2019 *"does not define standard enterprises, standard organizational structures, standard enterprise processes, or standard enterprise data"*｜SOA-RAF *"is not a concrete architecture"*／*"not a complete blueprint"*｜IIRA *"architectural template and methodology … design their own systems"*｜TOGAF *"methodology and framework"*。
**★ 口径提醒**：42010 官网 `42010/ads/` 讲的是 **2011 版 Clause 5**（*"conforms … when it meets the requirements in Clause 5"*）——引用其"关切须被视角框定""每视角恰好一视图"等句必须标 2011。
**★ 附录 F 前提已结清**：A 路报告"未能核实附录 F 清单"——**本库正本可核**（L2011 *"Each of them conforms to applicable requirements of 7.1."* ＋ L2025 清单）。

**C 路更正（覆盖 §8.5 的 EIRA 表述）**：EIRA `.xml`／`.archimate` 全量计数 `Principle=56`／`Goal=76`／`Requirement=60`／`Stakeholder=5`（`Business`／`Legal Entity`／`Public Administration`／`Individual`／`Organisation`），concern 借 **`Grouping`** 承载；**`<viewpoints>` 容器／`<viewpoint` 元素／`viewpoint=` 属性全为 0**，那 437 处 `viewpoint` 是**自定义 property 取值**，14 处 `rationale` 皆散文 → **A 部分（接近满足）／B 部分（较强；6.6 只有视角名无规格内容、6.9 无、6.10 非结构化）**。`CarTool-EC/EIRA/hints/vp_goal_realization.html` 含 `Stakeholders:/Concerns:/Purpose:/Scope:`＝**真正的视角规格文本**。**ArchiMetal**：`Goal=17／Assessment=14／Requirement=7／Driver=6／Stakeholder=4`、31 具名 viewpoint、79 view → A 部分（中）／B 部分（较强）。**ArchiSurance `Goal=0`**（子代理的 7 不可复现）。**GEMMA Archi 仓库**：`Principle=33`（带 GAP-ID 与 NORA 链接）／`Constraint=534`／`View=364` → A 部分（中）／B 部分（弱）。**NORA ArchiMate 仓库＝Kennismodel/元模型 → A 不满足**。**Papyrus** `InformationModeling.configuration` 含 stakeholders／viewpoints／modelKinds → A 不满足／B 部分。**AGA `architecture.digital.gov.au`＝403**。

**★ 能力边界**：**Node `fetch` 可用**（Node v24.15.0；探针 `.work-ch11/probe.mjs`；可达 `api.github.com`，命中匿名 403 速率限制）；**`r.jina.ai` 在本网络不可达**（DNS 非公网 IP，四次重试 `fetch failed`）→ **PDF→Markdown 路由不通**，**PDF／二进制仍是硬边界**。

**结论不变**：A＋B 双满足＝**0 件**；产品数据最好三件＝**EIRA／GfSE SAF-SysMLV2／UAF XMI**。

### 8.7 收尾负面结果（C 路最后一封）

- **★ `GfSE/SAF-Specification/_data/*.json` 存在性未复现 → 不得记为"已存在"**：三分支（`main`／`master`／`develop`）× `_data/{viewpoints,stakeholders,concerns,rationales}.json`、`docs/_data/…`、`userdoc/_data/…` **共 18 条路径全无命中**；jsDelivr 对该仓库报 **403 "Package size exceeded the configured limit of 50 MB"**（说明 `main` 存在）；`api.github.com` **403 限流**，tree API 无法复核。须在能浏览仓库树的环境先确认存在性。**`GfSE/SAF-SysMLV2` 那条线不受影响**（`stakeholders_library.sysml`／`concerns/*`／`viewpoints.sysml`／`Views/SystemContextDefinition_View.sysml`／`examples/ffds/ffds.sysml` 逐件已读原文）。
- **Node 大二进制下载未跑通**：写 `Buffer` 取 DM2 `.accdb`(962 KB) 与 Capella `.zip`(3.07 MB) **300 s 超时、无输出**；隔离测试 800 B README 亦 `fetch failed` → **Node 出网间歇性**；**只有文本小件稳定**（四件全量元素级复算＝硬证据：`Archisurance.xml` 151 KB／`ArchiMetal.xml` 696 KB／`EIRA v7.0.0.xml` 4.9 MB／`EIRA v7.0.0.archimate` 4.1 MB）。
- **★ B「满足」全批＝0**：EIRA 与 ArchiMetal 的"满足"判定**被全量复算推翻**（均判"部分"）；**全批无一件填写 6.9 的"对应方法"**。
- **定稿排序**：**EIRA v7.0.0（A 部分接近／B 部分较强）＞ArchiMetal.xml（A 部分中／B 部分较强）＞GfSE SAF-SysMLV2（A 不满足／B 部分较强）＞UAF 机读 XMI**。
- **未取到（维持）**：EIRA `.owl`/`.ttl` 本体；AGA（403）；NORA SMW 导出端点（403 "Request forbidden by administrative rules"）；GEMMA 部分导出；DoDAF `.accdb`；Capella／OpenMBEE 各 `.zip`/`.mdzip` 内部；`AD42010`（apg.box.com）；GfSE `_data/*.json`。
