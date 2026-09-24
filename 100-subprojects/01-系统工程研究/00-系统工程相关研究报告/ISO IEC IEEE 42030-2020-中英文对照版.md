# ISO/IEC/IEEE 42030:2019《软件、系统与企业 — 架构评估框架》中英文对照版

> **本文件性质**：`ISO IEC IEEE 42030-2020.md` 的**逐段中英对照译本**。英文为源文（原文照录），中文为译文，置于对应英文段落之下。

> **对照体例**：正文英文段落原样保留，**其下紧跟中文译文**（与英文段落**同格式、同为齐左**）；条目标题、图题、表头等**短标识行**采用「英文 + 中文」同行并置；表格单元格内「英文 ／ 中文」并置。详见下方【对照体例说明】。

> **术语依据**：条款号与术语名以标准原文为准；中文译名以本项目**24 号研究报告附录 A 术语定译表**与 **GB/T 45630-2025**（等同采用 42010:2022）为先，未覆盖的术语依 ISO 通行译法。

---

## 【对照体例说明】

**非标准正文，译者所加。**

| # | 项 | 处理 |
|---|---|---|
| 1 | 正文段落 | 英文原文 → 其下紧跟**中文译文**，与英文同为齐左正文段落（不加引用、不加「译」字标记） |
| 2 | 列表 | **逐条紧跟**——每个英文列表项之下，紧接该条的中文 |
| 3 | 条目标题 / 图题 / 章标题 | 「英文 中文」同行并置；**条目挂多个英文名时**用 ` / ` 连接、英文串与中文之间改用 ` ｜ ` 分隔 |
| 4 | 注（NOTE）／示例（EXAMPLE）／来源（SOURCE） | 英文原样（引用块）→ 其下中文**同为引用块**：`> **注 N**：…`、`> **示例**：…`、`> **来源**：…` |
| 5 | 表格 | 单元格内「英文 ／ 中文」并置 |
| 6 | 图引用行 | 原样保留（不译）；图题已译 |
| 7 | 译者自注 | `> **译注**：…`——凡带「译注」字样者均为译者所加，不是原文 |
| 8 | 一词多义的分译 | 少数词按语境分译，不强行统一：`program` 指软件程序时译「程序」，指与 project 并列的管理单元时译「项目群」，指企业举措时译「计划」；`assessment`／`analysis`／`evaluation` 分译「评定／分析／评估」 |

---

## 转换说明 / About this file

(ISO/IEC/IEEE 42030:2019, IDT)
**转换说明 / About this file**
本文件由 `ISO IEC IEEE 42030-2020.docx` 转换生成，正文为**英文原文照录**，未作翻译或改写。
**源件性质（重要）**：本目录内没有 42030 的 PDF，只有这一份 docx；而它本身是 **CSA 采标件的 PDF→Word 转换产物**（`CSA ISO/IEC/IEEE 42030:20`，等同采用 ISO/IEC/IEEE 42030:2019）。因此它与另两份由 PDF 直转的文件不同，带三处源伤，均已尽量修补，仍存疑处如实标注：
1. **条款号在源件正文中整体丢失**（标题只剩 `Scope`／`General` 这样的文字）。本文件已从 docx 的 Word 自动编号定义中还原——每个编号组的 `w:start` 编码了续号（如第 4 章那组 L0 start=4），故 `1`~`8`、`4.3.1`、`A.1`、`A.3.2.1` 这类号**是还原所得，不是从版面抄录的**。还原结果与源件内交叉引用（如正文 `See A.4 for …`）自洽，但**用前建议对一次正版**。
2. **插图全部未收录（20 幅）**：源件把矢量插图切成了大量小位图碎片（图 A.5 碎成 16 块），部分图完全丢失；更要紧的是**位图与图题在文档流中整体错位**——图题集中在 337~462 段，而位图落在 843／907／968／1022 段，按「就近取图」会把图 B.1 的题注配上一块写着 `processes` 的碎片。**错图比无图有害，故一幅不取**，只在每处原位插入 `> **图未收录**` 说明。需原图请查正版 PDF。
3. **页眉页脚混入正文**且 `ISO/IEC/IEEE 42030:2019(E)` 被误标为 Heading 4，已按版式构件剔除。
**其他处理**：表格按 Word 表结构转 Markdown（跨页表被源件拆成多张，故表块数多于表数）；印刷目录已替换为按标题层级生成的 Markdown 目录；断行连字符已还原（`identi- fying` → `identifying`，`one- and` 类悬挂连字符保留）；封面与版权页照录于正文之前。
**校验**：拿源 docx 逐段回查，受检 1073 段中 **1068 段命中**；未命中的 5 段全部是**印刷目录行**（带页码的 `AE report recommendations 31`、`Annex A (informative) … 34` 等），按设计已由生成目录取代，非内容缺失。表格 33 块列数自洽，无残留控制符。

---

## 目录（Contents）

  - [Cover and copyright pages (source lay-out, verbatim) 封面与版权页（源版式，逐字照录）](#cover-and-copyright-pages-source-lay-out-verbatim-封面与版权页源版式逐字照录)
  - [Foreword 前言](#foreword-前言)
  - [Introduction 引言](#introduction-引言)
  - [Software, systems and enterprise — Architecture evaluation framework 软件、系统和企业 — 架构评估框架](#software-systems-and-enterprise-architecture-evaluation-framework-软件系统和企业-架构评估框架)
    - [1 Scope 范围](#1-scope-范围)
    - [2 Normative references 规范性引用文件](#2-normative-references-规范性引用文件)
    - [3 Terms and definitions 术语和定义](#3-terms-and-definitions-术语和定义)
      - [3.1 architecture 架构](#31-architecture-架构)
      - [3.2 architecture description 架构描述](#32-architecture-description-架构描述)
      - [3.3 architecture entity 架构实体](#33-architecture-entity-架构实体)
      - [3.4 architecture evaluation AE 架构评估 AE](#34-architecture-evaluation-ae-架构评估-ae)
      - [3.5 architecture evaluation framework 架构评估框架](#35-architecture-evaluation-framework-架构评估框架)
      - [3.6 concern 关注点](#36-concern-关注点)
      - [3.7 environment 环境](#37-environment-环境)
      - [3.8 factor 因素](#38-factor-因素)
      - [3.9 stakeholder 利益相关方](#39-stakeholder-利益相关方)
      - [3.10 value 价值](#310-value-价值)
    - [4 Conceptual foundation 概念基础](#4-conceptual-foundation-概念基础)
      - [4.1 General 总则](#41-general-总则)
      - [4.2 Architecture evaluation context 架构评估语境](#42-architecture-evaluation-context-架构评估语境)
      - [4.3 Architecture evaluation tiers 架构评估层级](#43-architecture-evaluation-tiers-架构评估层级)
        - [4.3.1 Evaluation synthesis 评估综合](#431-evaluation-synthesis-评估综合)
        - [4.3.2 Value assessment 价值评定](#432-value-assessment-价值评定)
        - [4.3.3 Architectural analysis 架构分析](#433-architectural-analysis-架构分析)
      - [4.4 Architecture evaluation conceptual model 架构评估概念模型](#44-architecture-evaluation-conceptual-model-架构评估概念模型)
      - [4.5 Comparison between assessment and analysis 评定与分析之比较](#45-comparison-between-assessment-and-analysis-评定与分析之比较)
      - [4.6 Architecture evaluation factors 架构评估因素](#46-architecture-evaluation-factors-架构评估因素)
      - [4.7 Customized architecture evaluation frameworks 定制的架构评估框架](#47-customized-architecture-evaluation-frameworks-定制的架构评估框架)
      - [4.8 Tailoring 裁剪](#48-tailoring-裁剪)
    - [5 Conformance 符合性](#5-conformance-符合性)
      - [5.1 General 总则](#51-general-总则)
      - [5.2 Creating AE artifacts 创建 AE 人工制品](#52-creating-ae-artifacts-创建-ae-人工制品)
      - [5.3 Using generic AE framework to conduct AE efforts 使用通用 AE 框架开展 AE 工作](#53-using-generic-ae-framework-to-conduct-ae-efforts-使用通用-ae-框架开展-ae-工作)
      - [5.4 Verbal forms for the expression of provisions 表述条款的动词形式](#54-verbal-forms-for-the-expression-of-provisions-表述条款的动词形式)
    - [6 Architecture evaluation framework elements 架构评估框架要素](#6-architecture-evaluation-framework-elements-架构评估框架要素)
      - [6.1 Evaluation synthesis 评估综合](#61-evaluation-synthesis-评估综合)
        - [6.1.1 General requirements 一般要求](#611-general-requirements-一般要求)
        - [6.1.2 Architecture evaluation objectives 架构评估目标](#612-architecture-evaluation-objectives-架构评估目标)
        - [6.1.3 Architecture evaluation approaches 架构评估途径](#613-architecture-evaluation-approaches-架构评估途径)
        - [6.1.4 Architecture evaluation factors 架构评估因素](#614-architecture-evaluation-factors-架构评估因素)
        - [6.1.5 Architecture evaluation results 架构评估结果](#615-architecture-evaluation-results-架构评估结果)
      - [6.2 Value assessment 价值评定](#62-value-assessment-价值评定)
        - [6.2.1 General requirements 一般要求](#621-general-requirements-一般要求)
        - [6.2.2 Value assessment objectives 价值评定目标](#622-value-assessment-objectives-价值评定目标)
        - [6.2.3 Value assessment methods 价值评定方法](#623-value-assessment-methods-价值评定方法)
        - [6.2.4 Value assessment factors 价值评定因素](#624-value-assessment-factors-价值评定因素)
        - [6.2.5 Value assessment results 价值评定结果](#625-value-assessment-results-价值评定结果)
      - [6.3 Architectural analysis 架构分析](#63-architectural-analysis-架构分析)
        - [6.3.1 General requirements 一般要求](#631-general-requirements-一般要求)
        - [6.3.2 Architectural analysis objectives 架构分析目标](#632-architectural-analysis-objectives-架构分析目标)
        - [6.3.3 Architectural analysis methods 架构分析方法](#633-architectural-analysis-methods-架构分析方法)
        - [6.3.4 Architectural analysis factors 架构分析因素](#634-architectural-analysis-factors-架构分析因素)
        - [6.3.5 Architectural analysis results 架构分析结果](#635-architectural-analysis-results-架构分析结果)
    - [7 Customized architecture evaluation frameworks 定制的架构评估框架](#7-customized-architecture-evaluation-frameworks-定制的架构评估框架)
      - [7.1 General requirements 一般要求](#71-general-requirements-一般要求)
      - [7.2 Framework requirements for architecture evaluation 对架构评估的框架要求](#72-framework-requirements-for-architecture-evaluation-对架构评估的框架要求)
      - [7.3 Framework requirements for value assessment 对价值评定的框架要求](#73-framework-requirements-for-value-assessment-对价值评定的框架要求)
      - [7.4 Framework requirements for architectural analysis 对架构分析的框架要求](#74-framework-requirements-for-architectural-analysis-对架构分析的框架要求)
      - [7.5 Framework requirements for architecture evaluation work products 对架构评估工作产品的框架要求](#75-framework-requirements-for-architecture-evaluation-work-products-对架构评估工作产品的框架要求)
    - [8 Architecture evaluation work products 架构评估工作产品](#8-architecture-evaluation-work-products-架构评估工作产品)
      - [8.1 General requirements 通用要求](#81-general-requirements-通用要求)
      - [8.2 Architecture evaluation plan 架构评估计划](#82-architecture-evaluation-plan-架构评估计划)
        - [8.2.1 AE plan requirements AE 计划要求](#821-ae-plan-requirements-ae-计划要求)
        - [8.2.2 AE plan recommendations AE 计划建议](#822-ae-plan-recommendations-ae-计划建议)
        - [8.2.3 AE plan permissions AE 计划许可事项](#823-ae-plan-permissions-ae-计划许可事项)
      - [8.3 Architecture evaluation report 架构评估报告](#83-architecture-evaluation-report-架构评估报告)
        - [8.3.1 AE report requirements AE 报告要求](#831-ae-report-requirements-ae-报告要求)
        - [8.3.2 AE report recommendations AE 报告建议](#832-ae-report-recommendations-ae-报告建议)
        - [8.3.3 AE report permissions AE 报告许可事项](#833-ae-report-permissions-ae-报告许可事项)
  - [Annex A (informative) — Value and quality concepts ｜ 附录 A（资料性）— 价值和质量概念](#annex-a-informative-value-and-quality-concepts-附录-a资料性-价值和质量概念)
    - [A.1 General 总则](#a1-general-总则)
    - [A.2 Evaluation factors 评估因素](#a2-evaluation-factors-评估因素)
    - [A.3 Value 价值](#a3-value-价值)
      - [A.3.1 General 总则](#a31-general-总则)
      - [A.3.2 What is “Value”? 什么是“价值”？](#a32-what-is-value-什么是价值)
      - [A.3.3 Value-focused thinking 价值导向思维](#a33-value-focused-thinking-价值导向思维)
      - [A.3.4 Value assessment of system architectures 系统架构的价值评定](#a34-value-assessment-of-system-architectures-系统架构的价值评定)
      - [A.3.5 Ring’s value model Ring 的价值模型](#a35-rings-value-model-ring-的价值模型)
      - [A.3.6 Stakeholder values, qualities and measures 利益相关方价值、质量与度量](#a36-stakeholder-values-qualities-and-measures-利益相关方价值质量与度量)
      - [A.3.7 Value articulation framework 价值表述框架](#a37-value-articulation-framework-价值表述框架)
    - [A.4 Quality 质量](#a4-quality-质量)
      - [A.4.1 General 总则](#a41-general-总则)
      - [A.4.2 What is “Quality”? 什么是“质量”？](#a42-what-is-quality-什么是质量)
      - [A.4.3 Architecture quality attributes 架构质量属性](#a43-architecture-quality-attributes-架构质量属性)
      - [A.4.4 Boehm and Nupul’s quality model and ontology Boehm 与 Nupul 的质量模型与本体](#a44-boehm-and-nupuls-quality-model-and-ontology-boehm-与-nupul-的质量模型与本体)
      - [A.4.5 The ISO/IEC 25000 family of standards on quality 关于质量的 ISO/IEC 25000 系列标准](#a45-the-isoiec-25000-family-of-standards-on-quality-关于质量的-isoiec-25000-系列标准)
        - [A.4.5.1 General 概述](#a451-general-概述)
        - [A.4.5.2 ISO/IEC 25000 Quality model framework ISO/IEC 25000 质量模型框架](#a452-isoiec-25000-quality-model-framework-isoiec-25000-质量模型框架)
  - [Annex B (informative) — Relationship to other standards ｜ 附录 B（资料性）— 与其他标准的关系](#annex-b-informative-relationship-to-other-standards-附录-b资料性-与其他标准的关系)
    - [B.1 ISO/IEC standards in the domain of systems and software engineering 系统和软件工程领域的 ISO/IEC 标准](#b1-isoiec-standards-in-the-domain-of-systems-and-software-engineering-系统和软件工程领域的-isoiec-标准)
    - [B.2 ISO standards in the domain of enterprise activities 企业活动领域的 ISO 标准](#b2-iso-standards-in-the-domain-of-enterprise-activities-企业活动领域的-iso-标准)
    - [B.3 Relationship between architecture standards 架构标准之间的关系](#b3-relationship-between-architecture-standards-架构标准之间的关系)
  - [Annex C (informative) — Architecture evaluation examples ｜ 附录 C（资料性）— 架构评估示例](#annex-c-informative-architecture-evaluation-examples-附录-c资料性-架构评估示例)
    - [C.1 General 总则](#c1-general-总则)
    - [C.2 Business and IT architecture evaluation 业务和 IT 架构评估](#c2-business-and-it-architecture-evaluation-业务和-it-架构评估)
      - [C.2.1 Situation 情境](#c21-situation-情境)
      - [C.2.2 Business/IT architecture — Evaluation synthesis 业务／IT 架构 — 评估综合](#c22-businessit-architecture-evaluation-synthesis-业务it-架构-评估综合)
      - [C.2.3 Business/IT architecture — Value assessment 业务／IT 架构 — 价值评定](#c23-businessit-architecture-value-assessment-业务it-架构-价值评定)
      - [C.2.4 Business/IT architecture — Architectural analysis 业务／IT 架构 — 架构分析](#c24-businessit-architecture-architectural-analysis-业务it-架构-架构分析)
    - [C.3 Software architecture evaluation 软件架构评估](#c3-software-architecture-evaluation-软件架构评估)
      - [C.3.1 Situation 情境](#c31-situation-情境)
      - [C.3.2 Software architecture — Evaluation synthesis 软件架构 — 评估综合](#c32-software-architecture-evaluation-synthesis-软件架构-评估综合)
      - [C.3.3 Software architecture — Value assessment 软件架构 — 价值评定](#c33-software-architecture-value-assessment-软件架构-价值评定)
      - [C.3.4 Software architecture — Architectural analysis 软件架构 — 架构分析](#c34-software-architecture-architectural-analysis-软件架构-架构分析)
    - [C.4 Service architecture evaluation 服务架构评估](#c4-service-architecture-evaluation-服务架构评估)
      - [C.4.1 Situation 情形](#c41-situation-情形)
      - [C.4.2 Service architecture — Evaluation synthesis 服务架构 — 评估综合](#c42-service-architecture-evaluation-synthesis-服务架构-评估综合)
      - [C.4.3 Service architecture — Value assessment 服务架构 — 价值评定](#c43-service-architecture-value-assessment-服务架构-价值评定)
      - [C.4.4 Service architecture — Architectural analysis 服务架构 — 架构分析](#c44-service-architecture-architectural-analysis-服务架构-架构分析)
    - [C.5 Enterprise architecture evaluation 企业架构评估](#c5-enterprise-architecture-evaluation-企业架构评估)
      - [C.5.1 Situation 情形](#c51-situation-情形)
      - [C.5.2 Enterprise architecture — Evaluation synthesis 企业架构 — 评估综合](#c52-enterprise-architecture-evaluation-synthesis-企业架构-评估综合)
      - [C.5.3 Enterprise architecture — Value assessment 企业架构 — 价值评定](#c53-enterprise-architecture-value-assessment-企业架构-价值评定)
      - [C.5.4 Enterprise architecture — Architectural analysis 企业架构 — 架构分析](#c54-enterprise-architecture-architectural-analysis-企业架构-架构分析)
  - [Annex D (informative) — Example architecture evaluation frameworks ｜ 附录 D（资料性）— 示例架构评估框架](#annex-d-informative-example-architecture-evaluation-frameworks-附录-d资料性-示例架构评估框架)
    - [D.1 General 总则](#d1-general-总则)
    - [D.2 Architecture Tradeoff Analysis Method (ATAM) 架构权衡分析方法（ATAM）](#d2-architecture-tradeoff-analysis-method-atam-架构权衡分析方法atam)
      - [D.2.1 Overview 概述](#d21-overview-概述)
        - [D.2.1.1 General 总则](#d211-general-总则)
        - [D.2.1.2 Purpose 目的](#d212-purpose-目的)
        - [D.2.1.3 Basic approach 基本途径](#d213-basic-approach-基本途径)
        - [D.2.1.4 Conceptual flow 概念流程](#d214-conceptual-flow-概念流程)
        - [D.2.1.5 Sequence of steps 步骤顺序](#d215-sequence-of-steps-步骤顺序)
        - [D.2.1.6 Expected results 预期结果](#d216-expected-results-预期结果)
      - [D.2.2 Evaluation synthesis 评估综合](#d22-evaluation-synthesis-评估综合)
      - [D.2.3 Value assessment 价值评定](#d23-value-assessment-价值评定)
      - [D.2.4 Architectural analysis 架构分析](#d24-architectural-analysis-架构分析)
      - [D.2.5 Evaluation plan and report 评估计划与报告](#d25-evaluation-plan-and-report-评估计划与报告)
    - [D.3 The Method Framework and QUASAR method 方法框架与 QUASAR 方法](#d3-the-method-framework-and-quasar-method-方法框架与-quasar-方法)
      - [D.3.1 Overview 概述](#d31-overview-概述)
      - [D.3.2 Evaluation synthesis 评估综合](#d32-evaluation-synthesis-评估综合)
      - [D.3.3 Value assessment 价值评定](#d33-value-assessment-价值评定)
      - [D.3.4 Architectural analysis 架构分析](#d34-architectural-analysis-架构分析)
      - [D.3.5 Evaluation plan and report 评估计划与报告](#d35-evaluation-plan-and-report-评估计划与报告)
    - [D.4 Analysis of Alternatives (AoA) 备选方案分析（AoA）](#d4-analysis-of-alternatives-aoa-备选方案分析aoa)
      - [D.4.1 Overview 概述](#d41-overview-概述)
        - [D.4.1.1 General 总则](#d411-general-总则)
        - [D.4.1.2 Basic approach 基本途径](#d412-basic-approach-基本途径)
        - [D.4.1.3 Study objectives 研究目标](#d413-study-objectives-研究目标)
        - [D.4.1.4 Maturity assessment 成熟度评定](#d414-maturity-assessment-成熟度评定)
        - [D.4.1.5 Risk assessment 风险评定](#d415-risk-assessment-风险评定)
      - [D.4.2 Evaluation synthesis 评估综合](#d42-evaluation-synthesis-评估综合)
      - [D.4.3 Value assessment 价值评定](#d43-value-assessment-价值评定)
      - [D.4.4 Architectural analysis 架构分析](#d44-architectural-analysis-架构分析)
      - [D.4.5 Evaluation plan and report 评估计划与报告](#d45-evaluation-plan-and-report-评估计划与报告)
  - [Bibliography 参考文献](#bibliography-参考文献)
  - [IEEE notices and abstract IEEE 声明与摘要](#ieee-notices-and-abstract-ieee-声明与摘要)
    - [Important Notices and Disclaimers Concerning IEEE Standards Documents 关于 IEEE 标准文件的重要声明与免责声明](#important-notices-and-disclaimers-concerning-ieee-standards-documents-关于-ieee-标准文件的重要声明与免责声明)
    - [Notice and Disclaimer of Liability Concerning the Use of IEEE Standards Documents 关于使用 IEEE 标准文件的声明与责任免责声明](#notice-and-disclaimer-of-liability-concerning-the-use-of-ieee-standards-documents-关于使用-ieee-标准文件的声明与责任免责声明)
    - [Translations 翻译](#translations-翻译)
    - [Official statements 正式声明](#official-statements-正式声明)
    - [Comments on standards 对标准的意见](#comments-on-standards-对标准的意见)
    - [Laws and regulations 法律和法规](#laws-and-regulations-法律和法规)
    - [Copyrights 版权](#copyrights-版权)
    - [Photocopies 影印](#photocopies-影印)
    - [Updating of IEEE Standards documents IEEE 标准文件的更新](#updating-of-ieee-standards-documents-ieee-标准文件的更新)
    - [Errata 勘误](#errata-勘误)
    - [Patents 专利](#patents-专利)
    - [Abstract and keywords 摘要与关键词](#abstract-and-keywords-摘要与关键词)

---

---

## Cover and copyright pages (source lay-out, verbatim) 封面与版权页（源版式，逐字照录）

(ISO/IEC/IEEE 42030:2019, IDT)

(ISO/IEC/IEEE 42030:2019, IDT)

National Standard of Canada

加拿大国家标准

Software, systems and enterprise — Architecture evaluation framework

软件、系统与企业 — 架构评估框架

(ISO/IEC/IEEE 42030:2019, IDT)

(ISO/IEC/IEEE 42030:2019, IDT)

Legal Notice for Standards

标准法律通告

Canadian Standards Association (operating as “CSA Group”) develops standards through a consensus standards development process approved by the Standards Council of Canada. This process brings together volunteers representing varied viewpoints and interests to achieve consensus and develop a standard. Although CSA Group administers the process and establishes rules to promote fairness in achieving consensus, it does not independently test, evaluate, or verify the content of standards.

加拿大标准协会（以“CSA Group”名义运营）通过经加拿大标准委员会批准的协商一致标准制定过程制定标准。该过程汇集代表各种观点与利益的志愿者，以达成协商一致并制定标准。尽管 CSA Group 管理该过程并制定规则以促进达成协商一致的公平性，但其并不独立检测、评估或验证标准的内容。

Disclaimer and exclusion of liability

免责声明与责任排除

This document is provided without any representations, warranties, or conditions of any kind, express or implied, including, without limitation, implied warranties or conditions concerning this document’s fitness for a particular purpose or use, its merchantability, or its non-infringement of any third party’s intellectual property rights. CSA Group does not warrant the accuracy, completeness, or currency of any of the information published in this document. CSA Group makes no representations or warranties regarding this document’s compliance with any applicable statute, rule, or regulation.

本文件在提供时不附带任何形式的陈述、担保或条件，无论明示或默示，包括但不限于关于本文件对特定目的或用途的适用性、其可销售性或其不侵犯任何第三方知识产权的默示担保或条件。CSA Group 不担保本文件中所载任何信息的准确性、完整性或时效性。CSA Group 不就本文件符合任何适用法律、规则或法规作出任何陈述或担保。

IN NO EVENT SHALL CSA GROUP, ITS VOLUNTEERS, MEMBERS, SUBSIDIARIES, OR AFFILIATED COMPANIES, OR THEIR EMPLOYEES, DIRECTORS, OR OFFICERS, BE LIABLE FOR ANY DIRECT, INDIRECT, OR INCIDENTAL DAMAGES, INJURY, LOSS, COSTS, OR EXPENSES, HOWSOEVER CAUSED, INCLUDING BUT NOT LIMITED TO SPECIAL OR CONSEQUENTIAL DAMAGES, LOST REVENUE, BUSINESS INTERRUPTION, LOST OR DAMAGED DATA, OR ANY OTHER COMMERCIAL OR ECONOMIC LOSS, WHETHER BASED IN CONTRACT, TORT (INCLUDING NEGLIGENCE), OR ANY OTHER THEORY OF LIABILITY, ARISING OUT OF OR RESULTING FROM ACCESS TO OR POSSESSION OR USE OF THIS DOCUMENT, EVEN IF CSA GROUP HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES, INJURY, LOSS, COSTS, OR EXPENSES.

在任何情况下，CSA Group、其志愿者、成员、子公司或关联公司，或其雇员、董事或高级管理人员，均不对任何直接、间接或附带的损害、伤害、损失、费用或开支承担责任，无论其因何引起，包括但不限于特殊或后果性损害、收入损失、业务中断、数据丢失或损坏，或任何其他商业或经济损失，亦无论其基于合同、侵权（包括过失）或任何其他责任理论，只要产生于或源自对本文件的访问、持有或使用，即使 CSA Group 已被告知此类损害、伤害、损失、费用或开支的可能性。

In publishing and making this document available, CSA Group is not undertaking to render professional or other services for or on behalf of any person or entity or to perform any duty owed by any person or entity to another person or entity. The information in this document is directed to those who have the appropriate degree of experience to use and apply its contents, and CSA Group accepts no responsibility whatsoever arising in any way from any and all use of or reliance on the information contained in this document.

在出版和提供本文件时，CSA Group 并不承诺为任何人或实体、或以任何人或实体的名义提供专业服务或其他服务，也不承诺履行任何人或实体对另一人或实体所负的任何义务。本文件中的信息面向具备适当经验程度以使用和应用其内容的人员；对于因以任何方式使用或依赖本文件所含信息而产生的任何责任，CSA Group 概不承担。

CSA Group is a private not-for-profit company that publishes voluntary standards and related documents. CSA Group has no power, nor does it undertake, to enforce compliance with the contents of the standards or other documents it publishes.

CSA Group 是一家出版自愿性标准及相关文件的私营非营利公司。CSA Group 无权、也不承诺强制执行其所出版标准或其他文件内容的符合性。

Intellectual property rights and ownership

知识产权与所有权

As between CSA Group and the users of this document (whether it be in printed or electronic form), CSA Group is the owner, or the authorized licensee, of all works contained herein that are protected by copyright, all trade-marks (except as otherwise noted to the contrary), and all inventions and trade secrets that may be contained in this document, whether or not such inventions and trade secrets are protected by patents and applications for patents. Without limitation, the unauthorized use, modification, copying, or disclosure of this document may violate laws that protect CSA Group’s and/or others’ intellectual property and may give rise to a right in CSA Group and/or others to seek legal redress for such use, modification, copying, or disclosure. To the extent permitted by licence or by law, CSA Group reserves all intellectual property rights in this document.

在 CSA Group 与本文件使用者（无论其为印刷形式还是电子形式）之间，对于本文件所含一切受版权保护的作品、一切商标（除另有相反说明者外），以及本文件可能含有的一切发明和商业秘密（无论此类发明和商业秘密是否受专利及专利申请保护），CSA Group 均为其所有者或经授权的被许可人。在不加限制的前提下，未经授权使用、修改、复制或披露本文件，可能违反保护 CSA Group 和／或其他方知识产权的法律，并可能使 CSA Group 和／或其他方有权就此种使用、修改、复制或披露寻求法律救济。在许可或法律允许的范围内，CSA Group 保留本文件中的一切知识产权。

Patent rights

专利权

Attention is drawn to the possibility that some of the elements of this standard may be the subject of patent rights. CSA Group shall not be held responsible for identifying any or all such patent rights. Users of this standard are expressly advised that determination of the validity of any such patent rights is entirely their own responsibility.

提请注意，本标准的某些要素可能涉及专利权。CSA Group 不应负责识别任何或所有此类专利权。特此明确告知本标准的使用者，任何此类专利权有效性的确定完全由其自行负责。

Authorized use of this document

本文件的授权使用

This document is being provided by CSA Group for informational and non-commercial use only. The user of this document is authorized to do only the following:

CSA Group 提供本文件仅用于信息参考和非商业用途。本文件的使用者仅被授权进行下列行为：

If this document is in electronic form:

如果本文件为电子形式：

load this document onto a computer for the sole purpose of reviewing it;

仅为查阅目的将本文件载入计算机；

search and browse this document; and print this document if it is in PDF format.

检索和浏览本文件；以及如果本文件为 PDF 格式，打印本文件。

Limited copies of this document in print or paper form may be distributed only to persons who are authorized by CSA Group to have such copies, and only if this Legal Notice appears on each such copy.

本文件印刷或纸质形式的有限份数，仅可分发给经 CSA Group 授权持有此类副本的人员，且仅当每份此类副本上均载有本法律通告时方可分发。

In addition, users may not and may not permit others to alter this document in any way or remove this Legal Notice from the attached standard;

此外，使用者不得、也不得允许他人：以任何方式改动本文件，或从所附标准中移除本法律通告；

sell this document without authorization from CSA Group; or make an electronic copy of this document.

未经 CSA Group 授权出售本文件；或制作本文件的电子副本。

If you do not agree with any of the terms and conditions contained in this Legal Notice, you may not load or use this document or make any copies of the contents hereof, and if you do make such copies, you are required to destroy them immediately. Use of this document constitutes your acceptance of the terms and conditions of this Legal Notice.

如果您不同意本法律通告所含的任何条款和条件，则不得载入或使用本文件，也不得制作本文件内容的任何副本；如果您制作了此类副本，则须立即将其销毁。使用本文件即构成您接受本法律通告的条款和条件。

Standards Update Service

标准更新服务

July 2020

2020 年 7 月

Title: Software, systems and enterprise — Architecture evaluation framework

标题：软件、系统与企业 — 架构评估框架

To register for e-mail notification about any updates to this publication go to store.csagroup.org click on Product Updates

注册以获取有关本出版物任何更新的电子邮件通知请访问 store.csagroup.org点击 Product Updates

The List ID that you will need to register for updates to this publication is 2428383.

注册本出版物更新所需的 List ID 为 2428383。

If you require assistance, please e-mail techsupport@csagroup.org or call 416-747-2233.

如需协助，请发送电子邮件至 techsupport@csagroup.org，或致电 416-747-2233。

Visit CSA Group’s policy on privacy at www.csagroup.org/legal to find out how we protect your personal information.

请访问 www.csagroup.org/legal 查阅 CSA Group 的隐私政策，以了解我们如何保护您的个人信息。

Canadian Standards Association (operating as “CSA Group”), under whose auspices this National Standard has been produced, was chartered in 1919 and accredited by the Standards Council of Canada to the National Standards system in 1973. It is a not-for-profit, nonstatutory, voluntary membership association engaged in standards development and certification activities.

加拿大标准协会（以“CSA Group”名义运营）主持制定了本国家标准；该协会于 1919 年获得特许，并于 1973 年经加拿大标准委员会认可，进入国家标准体系。它是一个从事标准制定与认证活动的非营利、非法定、自愿性会员制协会。

CSA Group standards reflect a national consensus of producers and users — including manufacturers, consumers, retailers, unions and professional organizations, and governmental agencies. The standards are used widely by industry and commerce and often adopted by municipal, provincial, and federal governments in their regulations, particularly in the fields of health, safety, building and construction, and the environment.

CSA Group 标准反映了生产者与使用者——包括制造商、消费者、零售商、工会与专业组织以及政府机构——的全国性共识。这些标准被工商业广泛使用，并常被市、省和联邦政府在其法规中采用，尤其是在健康、安全、建筑与施工以及环境领域。

Individuals, companies, and associations across Canada indicate their support for CSA Group’s standards development by volunteering their time and skills to Committee work and supporting CSA Group’s objectives through sustaining memberships. The more than 7000 committee volunteers and the 2000 sustaining memberships together form CSA Group’s total membership from which its Directors are chosen. Sustaining memberships represent a major source of income for CSA Group’s standards development activities.

加拿大各地的个人、公司和协会通过以下方式表明其对 CSA Group 标准制定工作的支持：志愿贡献其时间和技能参与委员会工作，以及通过持续会员资格支持 CSA Group 的目标。7000 多名委员会志愿者与 2000 个持续会员资格共同构成 CSA Group 的全体成员，其董事即从中产生。持续会员资格是 CSA Group 标准制定活动的一项主要收入来源。

CSA Group offers certification and testing services in support of and as an extension to its standards development activities. To ensure the integrity of its certification process, CSA Group regularly and continually audits and inspects products that bear the

CSA Group 提供认证与测试服务，以支持并延伸其标准制定活动。为确保其认证过程的完整性，CSA Group 定期并持续地审核和检查带有

CSA Group Mark.

CSA Group 标志的产品。

In addition to its head office and laboratory complex in Toronto, CSA Group has regional branch offices in major centres across Canada and inspection and testing agencies in eight countries. Since 1919, CSA Group has developed the necessary expertise to meet its corporate mission: CSA Group is an independent service organization whose mission is to provide an open and effective forum for activities facilitating the exchange of goods and services through the use of standards, certification and related services to meet national and international needs.

除位于多伦多的总部和实验室园区外，CSA Group 在加拿大各主要中心城市设有地区分支机构，并在八个国家设有检验与测试机构。自 1919 年以来，CSA Group 已积累必要的专业能力以实现其企业使命：CSA Group 是一家独立的服务组织，其使命是提供一个开放而有效的论坛，通过运用标准、认证及相关服务促进商品和服务的交换，以满足国家和国际需求。

For further information on CSA Group services, write to CSA Group

有关 CSA Group 服务的更多信息，请致函 CSA Group

178 Rexdale Boulevard Toronto, Ontario, M9W 1R3 Canada

178 Rexdale Boulevard Toronto, Ontario, M9W 1R3 Canada

A National Standard of Canada is a standard developed by a Standards Council of Canada (SCC) accredited Standards Development Organization, in compliance with requirements and guidance set out by SCC. More information on National Standards of Canada can be found at www.scc.ca.

加拿大国家标准是由加拿大标准理事会（SCC）认可的标准制定组织按照 SCC 规定的要求和指南制定而成的标准。有关加拿大国家标准的更多信息，可访问 www.scc.ca 获取。

SCC is a Crown corporation within the portfolio of Innovation, Science and Economic Development (ISED) Canada. With the goal of enhancing Canada's economic competitiveness and social well-being, SCC leads and facilitates the development and use of national and international standards. SCC also coordinates Canadian participation in standards development, and identifies strategies to advance Canadian standardization efforts.

SCC 是加拿大创新、科学与经济发展部（ISED）下属的皇家公司。以提升加拿大经济竞争力和社会福祉为目标，SCC 主导并促进国家和国际标准的制定与使用。SCC 还协调加拿大参与标准制定活动，并确定推进加拿大标准化工作的战略。

Accreditation services are provided by SCC to various customers, including product certifiers, testing laboratories, and standards development organizations. A list of SCC programs and accredited bodies is publicly available at www.scc.ca.

SCC 向各类客户提供认可服务，客户包括产品认证机构、测试实验室和标准制定组织。SCC 的项目清单及获认可机构清单在 www.scc.ca 上公开提供。

Standards Council of Canada 600-55 Metcalfe Street Ottawa, Ontario, K1P 6L5 Canada

加拿大标准理事会 600-55 Metcalfe Street Ottawa, Ontario, K1P 6L5 Canada

Cette Norme Nationale du Canada n’est disponible qu’en anglais.

本加拿大国家标准仅以英文提供。

Although the intended primary application of this Standard is stated in its Scope, it is important to note that it remains the responsibility of the users to judge its suitability for their particular purpose.

尽管本标准的预期主要应用已在其范围中说明，但需注意，判断本标准是否适用于使用者的特定目的仍由使用者负责。

®A trademark of the Canadian Standards Association, operating as “CSA Group”

®加拿大标准协会的商标，以“CSA Group”名义运营

National Standard of Canada

加拿大国家标准

Software, systems and enterprise — Architecture evaluation framework

软件、系统与企业 — 架构评估框架

(ISO/IEC/IEEE 42030:2019, IDT)

(ISO/IEC/IEEE 42030:2019, IDT)

Prepared by

编制单位

International Organization for Standardization/ International Electrotechnical Commission

国际标准化组织／国际电工委员会

Reviewed by

评审单位

®A trademark of the Canadian Standards Association, operating as “CSA Group”

®加拿大标准协会的商标，以“CSA Group”名义运营

Published in July 2020 by CSA Group

由 CSA Group 于 2020 年 7 月出版

A not-for-profit private sector organization

非营利性私营部门组织

178 Rexdale Boulevard, Toronto, Ontario, Canada M9W 1R3

178 Rexdale Boulevard, Toronto, Ontario, Canada M9W 1R3

To purchase standards and related publications, visit our Online Store at store.csagroup.org or call toll-free 1-800-463-6727 or 416-747-4044.

如需购买标准及相关出版物，请访问我们的在线商店 store.csagroup.org或拨打免费电话 1-800-463-6727 或 416-747-4044。

ICS 35.080

ICS 35.080

ISBN 978-1-4883-3082-7

ISBN 978-1-4883-3082-7

© 2020 Canadian Standards Association

© 2020 加拿大标准协会

All rights reserved. No part of this publication may be reproduced in any form whatsoever without the prior permission of the publisher.

版权所有。未经出版者事先许可，不得以任何形式复制本出版物的任何部分。

CSA ISO/IEC/IEEE 42030:20 Software, systems and enterprise — Architecture evaluation framework

CSA ISO/IEC/IEEE 42030:20 软件、系统与企业 — 架构评估框架

Software, systems and enterprise — Architecture evaluation framework (ISO/IEC/IEEE 42030:2019, IDT)

软件、系统与企业 — 架构评估框架 (ISO/IEC/IEEE 42030:2019, IDT)

CSA Preface

CSA 前言

Standards development within the Information Technology sector is harmonized with international standards development. Through the CSA Technical Committee on Information Technology (TCIT), Canadians serve as the SCC Mirror Committee (SMC) on ISO/IEC Joint Technical Committee 1 on Information Technology (ISO/IEC JTC1) for the Standards Council of Canada (SCC), the ISO member body for Canada and sponsor of the Canadian National Committee of the IEC. Also, as a member of the International Telecommunication Union (ITU), Canada participates in the International Telegraph and Telephone Consultative Committee (ITU-T).

信息技术领域的标准制定与国际标准制定相协调。通过 CSA 信息技术技术委员会（TCIT），加拿大人为加拿大标准理事会（SCC）担任 ISO/IEC 信息技术联合技术委员会 1（ISO/IEC JTC1）的 SCC 镜像委员会（SMC）；SCC 是加拿大的 ISO 成员机构，也是 IEC 加拿大国家委员会的发起方。此外，作为国际电信联盟（ITU）的成员，加拿大参加国际电报电话咨询委员会（ITU-T）。

For brevity, this Standard will be referred to as “CSA ISO/IEC/IEEE 42030” throughout.

为简化起见，本标准全文简称“CSA ISO/IEC/IEEE 42030”。

At the time of publication, ISO/IEC/IEEE 42030:2019 is available from ISO and IEC in English only. CSA Group will publish the French version when it becomes available from ISO and IEC.

在出版时，ISO/IEC/IEEE 42030:2019 仅以英文由 ISO 和 IEC 提供。待 ISO 和 IEC 提供法文版本后，CSA Group 将出版该法文版本。

The International Standard was reviewed by the CSA TCIT under the jurisdiction of the CSA Strategic Steering Committee on Information and Communications Technology and deemed acceptable for use in Canada. From time to time, ISO/IEC may publish addenda, corrigenda, etc. The TCIT will review these documents for approval and publication. For a listing, refer to the Current Standards Activities page at standardsactivities.csa.ca. This Standard has been formally approved, without modification, by the Technical Committee and has been developed in compliance with Standards Council of Canada requirements for National Standards of Canada. It has been published as a National Standard of Canada by CSA Group.

该国际标准由 CSA TCIT 在 CSA 信息与通信技术战略指导委员会的管辖下评审，并被认定可在加拿大使用。ISO/IEC 可不时发布附录、勘误表等文件。TCIT 将评审这些文件以供批准和出版。相关清单请参见 standardsactivities.csa.ca 上的“现行标准活动”页面。本标准已由该技术委员会正式批准，未作任何修改，其制定符合加拿大标准理事会关于加拿大国家标准的要求。本标准已由 CSA Group 作为加拿大国家标准出版。

© 2020 Canadian Standards Association

© 2020 加拿大标准协会

All rights reserved. No part of this publication may be reproduced in any form whatsoever without the prior permission of the publisher. ISO/IEC material is reprinted with permission. Where the words “this International Standard” appear in the text, they should be interpreted as “this National Standard of Canada”.

版权所有。未经出版者事先许可，不得以任何形式复制本出版物的任何部分。ISO/IEC 材料经许可重印。凡文中出现“本国际标准”字样之处，宜解释为“本加拿大国家标准”。

Inquiries regarding this National Standard of Canada should be addressed to CSA Group

有关本加拿大国家标准的垂询，宜向 CSA Group 提出

178 Rexdale Boulevard, Toronto, Ontario, Canada M9W 1R3 1-800-463-6727 • 416-747-4000 www.csagroup.org

178 Rexdale Boulevard, Toronto, Ontario, Canada M9W 1R3 1-800-463-6727 • 416-747-4000www.csagroup.org

To purchase standards and related publications, visit our Online Store at store.csagroup.org or call toll-free 1-800-463-6727 or 416-747-4044.

如需购买标准及相关出版物，请访问我们的在线商店 store.csagroup.org，或拨打免费电话 1-800-463-6727 或 416-747-4044。

July 2020 © 2020 Canadian Standards Association CSA/5

2020 年 7 月 © 2020 加拿大标准协会 CSA/5

CSA ISO/IEC/IEEE 42030:20 Software, systems and enterprise — Architecture evaluation framework

CSA ISO/IEC/IEEE 42030:20 软件、系统与企业 — 架构评估框架

This Standard is subject to review within five years from the date of publication, and suggestions for its improvement will be referred to the appropriate committee. The technical content of IEC and ISO publications is kept under constant review by IEC and ISO. To submit a proposal for change, please send the following information to inquiries@csagroup.org and include “Proposal for change” in the subject line:

本标准自出版之日起五年内将接受复审，其改进建议将转交相关委员会。IEC 和 ISO 出版物的技术内容由 IEC 和 ISO 持续复审。如需提交变更提案，请将下列信息发送至 inquiries@csagroup.org，并在主题栏中注明“Proposal for change”：

Standard designation (number);

标准编号（数字）；

relevant clause, table, and/or figure number;

相关条款、表和／或图的编号；

wording of the proposed change; and rationale for the change.

所提变更的措辞；以及变更的理由。

July 2020 © 2020 Canadian Standards Association CSA/6

2020 年 7 月 © 2020 加拿大标准协会 CSA/6

CSA Technical Committee on Information Technology

CSA 信息技术技术委员会

J. MacFie Microsoft Canada, Ottawa, Ontario, Canada

J. MacFie Microsoft Canada，加拿大安大略省渥太华

Category: Producer Interest

类别：生产者利益

Chair

主席

F. Coallier École de technologie supérieure (Université du Québec) (ÉTS),

F. Coallier 高等技术学院（魁北克大学）（ÉTS），

Montréal, Québec, Canada

加拿大魁北克省蒙特利尔

Category: General Interest

类别：一般利益

Vice-Chair

副主席

M. Ally Athabasca University, Edmonton, Alberta, Canada

M. Ally 阿萨巴斯卡大学，加拿大艾伯塔省埃德蒙顿

Non-voting

无表决权

R. Balderston Canadian Bank Note Company Limited, Ottawa, Ontario, Canada

R. Balderston Canadian Bank Note Company Limited，加拿大安大略省渥太华

Non-voting

无表决权

L. Bertsch Horizon Technologies Inc., Victoria, British Columbia, Canada

L. Bertsch Horizon Technologies Inc.，加拿大不列颠哥伦比亚省维多利亚

Non-voting

无表决权

J. Bérubé IDEgenic Inc.,

J. Bérubé IDEgenic Inc.，

Bromont, Québec, Canada

加拿大魁北克省布罗蒙

Category: General Interest

类别：一般利益

T. Capel Comgate Engineering Ltd., Ottawa, Ontario, Canada Category: General Interest

T. Capel Comgate Engineering Ltd.，加拿大安大略省渥太华 类别：一般利益

J. A. Carter University of Saskatchewan, Saskatoon, Saskatchewan, Canada

J. A. Carter 萨斯喀彻温大学，加拿大萨斯喀彻温省萨斯卡通

Non-voting

无表决权

P. Cotton Vancouver, British Columbia, Canada Non-voting

P. Cotton 加拿大不列颠哥伦比亚省温哥华 无表决权

D. Ferguson Lyngsoe Systems Ltd., Mississauga, Ontario, Canada Category: User Interest

D. Ferguson Lyngsoe Systems Ltd.，加拿大安大略省密西沙加 类别：用户利益

R. J. Gates Toronto, Ontario, Canada Non-voting

R. J. Gates 加拿大安大略省多伦多 无表决权

G. Gauthier Université du Québec à Montréal (UQAM), Montréal, Québec, Canada

G. Gauthier 魁北克大学蒙特利尔分校（UQAM），加拿大魁北克省蒙特利尔

Non-voting

无表决权

P. J. Haighton Organization Metrics, Ottawa, Ontario, Canada Category: User Interest

P. J. Haighton Organization Metrics，加拿大安大略省渥太华 类别：用户利益

V. A. Hailey The VHG Corporation, Gormley, Ontario, Canada

V. A. Hailey The VHG Corporation，加拿大安大略省戈姆利

Non-voting

无表决权

J. Harlan InterDigital Canada, Ltd., Montréal, Québec, Canada

J. Harlan InterDigital Canada, Ltd.，加拿大魁北克省蒙特利尔

Non-voting

无表决权

C. Ho Innovation, Science and Economic Development Canada,

C. Ho 加拿大创新、科学与经济发展部，

Ottawa, Ontario, Canada

加拿大安大略省渥太华

Non-voting

无表决权

G. K. Holman Crane Softwrights Ltd., Kars, Ontario, Canada

G. K. Holman Crane Softwrights Ltd.，加拿大安大略省卡斯

Non-voting

无表决权

W. Jager ECD Technology Ltd., Stittsville, Ontario, Canada

W. Jager ECD Technology Ltd.，加拿大安大略省斯蒂茨维尔

Non-voting

无表决权

A. W. Kark Witan Consulting Services Inc., Ottawa, Ontario, Canada

A. W. Kark Witan Consulting Services Inc.，加拿大安大略省渥太华

Non-voting

无表决权

F. A. Khan TwelveDot Inc.,

F. A. Khan TwelveDot Inc.，

Osgoode, Ontario, Canada

加拿大安大略省奥斯古德

Category: Producer Interest

类别：生产者利益

J. Knoppers Information Management Services Inc., Ottawa, Ontario, Canada

J. Knoppers Information Management Services Inc.，加拿大安大略省渥太华

Category: User Interest

类别：用户利益

A. LaBonté Québec, Québec, Canada

A. LaBonté 加拿大魁北克省魁北克市

Category: General Interest

类别：一般利益

G. Martin-Cocher BlackBerry Ltd.,

G. Martin-Cocher BlackBerry Ltd.，

Mississauga, Ontario, Canada

加拿大安大略省密西沙加

Non-voting

无表决权

C. P. Provencher Provencher InfoSec, Montréal, Québec, Canada Category: Producer Interest

C. P. Provencher Provencher InfoSec，加拿大魁北克省蒙特利尔 类别：生产者利益

A. Robinson Information Systems Architects, a Fountain Technical Services Group, Ottawa, Ontario, Canada

A. Robinson Information Systems Architects，Fountain Technical Services 集团旗下，加拿大安大略省渥太华

Non-voting

无表决权

D. Sheppard ConCon Management Services Corp., Toronto, Ontario, Canada

D. Sheppard ConCon Management Services Corp.，加拿大安大略省多伦多

Non-voting

无表决权

S. Tremblay Excelsa Technologies Consulting Inc., Navan, Ontario, Canada

S. Tremblay Excelsa Technologies Consulting Inc.，加拿大安大略省纳文

Non-voting

无表决权

I. Verhappen CIMA+,

I. Verhappen CIMA+，

Calgary, Alberta, Canada

加拿大艾伯塔省卡尔加里

Category: User Interest

类别：用户利益

A. Kostruba CSA Group,

A. Kostruba CSA Group，

Toronto, Ontario, Canada

加拿大安大略省多伦多

Project Manager

项目经理

INTERNATIONAL STANDARD ISO/IEC/

国际标准ISO/IEC/

IEEE 42030

IEEE 42030

First edition

第一版

2019-07

2019-07

Software, systems and enterprise — Architecture evaluation framework

软件、系统与企业 — 架构评估框架

Logiciel, systèmes et entreprise — Cadre d'évaluation de l'architecture

软件、系统与企业 — 架构评估框架

© ISO/IEC 2019

© ISO/IEC 2019

© IEEE 2019

© IEEE 2019

COPYRIGHT PROTECTED DOCUMENT

受版权保护的文件

© ISO/IEC 2019

© ISO/IEC 2019

© IEEE 2019

© IEEE 2019

All rights reserved. Unless otherwise specified, or required in the context of its implementation, no part of this publication may be reproduced or utilized otherwise in any form or by any means, electronic or mechanical, including photocopying, or posting on the internet or an intranet, without prior written permission. Permission can be requested from either ISO at the address below or ISO’s member body in the country of the requester.

版权所有。除非另有规定，或在实施本文件的语境中有所要求，未经事先书面许可，不得以任何形式或任何手段（电子的或机械的，包括影印以及在国际互联网或内联网上发布）复制或以其他方式利用本出版物的任何部分。许可可向 ISO（地址见下文）或向请求者所在国家的 ISO 成员机构申请。

ISO copyright office Institute of Electrical and Electronics Engineers, Inc

ISO 版权办公室 Institute of Electrical and Electronics Engineers, Inc

CP 401 • Ch. de Blandonnet 8 3 Park Avenue, New York

CP 401 • Ch. de Blandonnet 8 3 Park Avenue, New York

CH-1214 Vernier, Geneva NY 10016-5997, USA

CH-1214 Vernier, Geneva NY 10016-5997, USA

Tel. +41 22 749 01 11

电话：+41 22 749 01 11

Fax +41 22 749 09 47 copyright@iso.org stds.ipr@ieee.org www.iso.org www.ieee.org ii © IEEE 2019 – All rights reserved

传真：+41 22 749 09 47电子邮件：copyright@iso.org 电子邮件：stds.ipr@ieee.org网址：www.iso.org 网址：www.ieee.orgii © IEEE 2019 – 版权所有

---

## Foreword 前言

ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) form the specialized system for worldwide standardization. National bodies that are members of ISO or IEC participate in the development of International Standards through technical committees established by the respective organization to deal with particular fields of technical activity. ISO and IEC technical committees collaborate in fields of mutual interest. Other international organizations, governmental and non-governmental, in liaison with ISO and IEC, also take part in the work. In the field of information technology, ISO and IEC have established a joint technical committee, ISO/IEC JTC 1.

ISO（国际标准化组织）和 IEC（国际电工委员会）构成世界范围标准化的专门体系。作为 ISO 或 IEC 成员的国家机构，通过各该组织为处理特定技术活动领域而设立的技术委员会，参与国际标准的制定。ISO 与 IEC 的技术委员会在共同感兴趣的领域开展合作。与 ISO 和 IEC 有联络的其他国际组织，政府的和非政府的，也参与此项工作。在信息技术领域，ISO 和 IEC 设立了一个联合技术委员会，即 ISO/IEC JTC 1。

The procedures used to develop this document and those intended for its further maintenance are described in the ISO/IEC Directives, Part 1. In particular, the different approval criteria needed for the different types of ISO documents should be noted. This document was drafted in accordance with the rules given in the ISO/IEC Directives, Part 2 (see www.iso.org/directives).

用于制定本文件的程序以及旨在对其进一步维护的程序，在《ISO/IEC 导则 第1部分》中描述。尤其宜注意，不同类型的 ISO 文件需要不同的批准准则。本文件依据《ISO/IEC 导则 第2部分》给出的规则起草（见 www.iso.org/directives）。

IEEE Standards documents are developed within the IEEE Societies and the Standards Coordinating Committees of the IEEE Standards Association (IEEE-SA) Standards Board. The IEEE develops its standards through a consensus development process, approved by the American National Standards Institute, which brings together volunteers representing varied viewpoints and interests to achieve the final product. Volunteers are not necessarily members of the Institute and serve without compensation. While the IEEE administers the process and establishes rules to promote fairness in the consensus development process, the IEEE does not independently evaluate, test, or verify the accuracy of any of the information contained in its standards.

IEEE 标准文件由 IEEE 各协会以及 IEEE 标准协会（IEEE-SA）标准委员会的标准协调委员会制定。IEEE 通过协商一致制定过程来制定其标准，该过程由美国国家标准学会批准，它汇集代表各种观点和利益的志愿者以形成最终产品。志愿者不一定是该学会的成员，且不取报酬。尽管 IEEE 管理该过程并制定规则以促进协商一致制定过程中的公平性，但 IEEE 并不独立评估、测试或验证其标准中所含任何信息的准确性。

Attention is drawn to the possibility that some of the elements of this document may be the subject of patent rights. ISO and IEC shall not be held responsible for identifying any or all such patent rights. Details of any patent rights identified during the development of the document will be in the Introduction and/or on the ISO list of patent declarations received (see www.iso.org/patents).

提请注意，本文件的某些内容可能涉及专利权。ISO 和 IEC 不应负责识别任何或所有此类专利权。在制定本文件过程中识别出的任何专利权的细节，将载于引言和／或 ISO 已收到的专利声明清单（见 www.iso.org/patents）中。

Any trade name used in this document is information given for the convenience of users and does not constitute an endorsement.

本文件中使用的任何商品名称均为方便使用者而提供的信息，不构成对其的认可。

For an explanation of the voluntary nature of standards, the meaning of ISO specific terms and expressions related to conformity assessment, as well as information about ISO's adherence to the World Trade Organization (WTO) principles in the Technical Barriers to Trade (TBT), see www.iso

关于标准的自愿性质、与合格评定有关的 ISO 特定术语和表述的含义，以及有关 ISO 遵守世界贸易组织（WTO）《技术性贸易壁垒（TBT）协定》原则的信息，见 www.iso

.org/iso/foreword.html.

.org/iso/foreword.html.

This document was prepared by Joint Technical Committee ISO/IEC JTC 1, Information technology, Subcommittee SC 7, Software and systems engineering, in cooperation with the Systems and Software Engineering Standards Committee of the IEEE Computer Society, under the Partner Standards Development Organization cooperation agreement between ISO and IEEE.

本文件由 ISO/IEC JTC 1 信息技术技术委员会、SC 7 软件与系统工程分委员会，与 IEEE 计算机学会系统与软件工程标准委员会合作，依据 ISO 与 IEEE 之间的伙伴标准制定组织合作协议制定。

Any feedback or questions on this document should be directed to the user’s national standards body. A complete listing of these bodies can be found at www.iso.org/members.html.

对本文件的任何反馈或问题，宜提交给使用者所在国家的标准机构。这些机构的完整名录见 www.iso.org/members.html。

CSA ISO/IEC/IEEE 42030:20 v

CSA ISO/IEC/IEEE 42030:20 v

## Introduction 引言

The complexity of human-made systems has grown to an unprecedented level. This complexity leads to new opportunities and greater challenges for organizations that conceive, develop, industrialize, produce, maintain, utilize, recycle and dismantle enterprises, systems and software, and for various stakeholders that are impacted by these things. To address these opportunities and challenges, organizations increasingly apply concepts, principles, procedures and tools to drive better architecture strategies, make better architecture-related decisions, create more useful and effective architectures and improve architecture maturity. Architecture-related activities are not only strategic in nature; they are tactical and operational as well. Furthermore, the use of architecture frameworks, architecture description languages and generalist modeling languages have become common practice in commercial, public service, government, civil and military domains.

人造系统的复杂性已增长到前所未有的水平。这种复杂性为那些构思、开发、产业化、生产、维护、利用、回收和拆解企业、系统与软件的组织，以及受这些事物影响的各类利益相关方，带来了新的机遇和更大的挑战。为应对这些机遇与挑战，组织越来越多地运用概念、原则、程序与工具，以驱动更好的架构策略、作出更好的架构相关决策、创建更有用且更有效的架构并提高架构成熟度。架构相关活动不仅在性质上是战略性的，也是战术性和运行性的。此外，架构框架、架构描述语言和通用建模语言的使用，在商业、公共服务、政府、民用与军事领域已成为普遍做法。

The concept of architecture used in this document goes beyond the case where the architecture entity is a system. Architecture is increasingly being applied to things not normally thought of as systems, including entities with system-like structure and behavior such as enterprises, services, data, business functions, mission areas, product lines, families of systems, software items, etc. This allows for a more generalized usage of the concept of architecture when the evaluation elements specified in this document are applied.

本文件所用的架构概念不限于架构实体是系统的情形。架构正越来越多地应用于通常不被视为系统的事物，包括企业、服务、数据、业务功能、任务领域、产品线、系统族、软件项等具有类系统结构与行为的实体。这使得在应用本文件规定的评估要素时，能够更普遍地使用架构概念。

Architecture evaluations are performed for many reasons, such as:

实施架构评估的原因众多，例如：

a) determining if an entity of interest has been or is being architected in such a way that it fulfils its intended purpose (or can be changed in a way that suits a new purpose);

a) 确定所关注实体是否已经或正在以使其实现预期目的的方式被架构（或能按适合新目的的方式予以改变）；

b) evaluating the effectiveness and suitability of an architecture towards addressing stakeholder needs and expectations;

b) 评估架构在满足利益相关方需要和期望方面的有效性和适宜性；

c) identifying risks for mitigation;

c) 识别待缓解的风险；

d) identifying opportunities for the improvement of an entity or its architecture;

d) 识别改进实体或其架构的机会；

e) clarifying the problem space and stakeholder needs; and f) assessing progress towards meeting architecture objectives.

e) 澄清问题空间和利益相关方需要；以及f) 评定实现架构目标的进展。

Architecture evaluations can be performed on any kind of architecture, including a reference architecture, an architecture for a family of systems or an architecture for a product line where there are multiple kinds of architecture entities for a single architecture.

架构评估能对任何种类的架构实施，包括参考架构、系统族的架构或产品线的架构，其中单一架构对应多种架构实体。

This document provides a generic, conceptual guiding framework that can be used for the planning, execution and documentation of architecture evaluations. Execution is addressed by specification of evaluation elements that can be used during performance of an evaluation effort. Planning and documentation are addressed by specification of work products for the evaluation effort. An organization using this document can establish specific frameworks for the work products and the evaluation elements that can be used as the basis for multiple, recurring architecture evaluation efforts. An organization can also establish tools, methods, best practices, capabilities and resources based on the generic framework provided in this document. The generic framework makes it easier to compare evaluations and evaluation frameworks used in specific cases. Implementation of the proposed architecture framework will in time result in improvement of architecture maturity of the organization.

本文件提供一个通用的概念性指导框架，能用于架构评估的策划、执行与文档编制。执行通过对评估要素的规定予以处理，这些评估要素能在实施评估工作期间使用。策划与文档编制通过对该评估工作的工作产品的规定予以处理。使用本文件的组织能针对工作产品和评估要素建立专门框架，这些框架能用作多项重复性架构评估工作的基础。组织还能基于本文件提供的通用框架建立工具、方法、最佳实践、能力和资源。该通用框架使具体情形中所用的评估和评估框架更易于比较。所提议的架构框架的实施将适时促成组织架构成熟度的提升。

vi CSA ISO/IEC/IEEE 42030:20

vi CSA ISO/IEC/IEEE 42030:20

INTERNATIONAL STANDARD ISO/IEC/IEEE 42030:2019(E)

国际标准 ISO/IEC/IEEE 42030:2019(E)

## Software, systems and enterprise — Architecture evaluation framework 软件、系统和企业 — 架构评估框架

### 1 Scope 范围

This document specifies the means to organize and record architecture evaluations for enterprise, systems and software fields of application.

本文件规定了在企业、系统和软件应用领域中组织和记录架构评估的手段。

The aim of this document is to enable architecture evaluations that are used to:

本文件的目的是使架构评估能用于：

a) validate that architectures address the concerns of stakeholders;

a) 确认架构处理了利益相关方的关注点；

b) assess the quality of architectures with respect to their intended purpose;

b) 就架构的预期目的评定架构的质量；

c) assess the value of architectures to their stakeholders;

c) 评定架构对其利益相关方的价值；

d) determine whether architecture entities address their intended purpose;

d) 确定架构实体是否处理了其预期目的；

e) provide knowledge and information about architecture entities; f) assess progress towards achieving architecture objectives;

e) 提供关于架构实体的知识和信息；f) 评定实现架构目标的进展；

g) clarify understanding of problem space and of stakeholder needs and expectations;

g) 澄清对问题空间以及利益相关方需要和期望的理解；

h) identify risks and opportunities associated with architectures; and i) support decision making where architectures are involved.

h) 识别与架构相关的风险和机会；以及i) 在涉及架构时支持决策。

> **NOTE** This document addresses the evaluation of an architecture and not an evaluation of the architecture description’s suitability. Matters concerning the evaluation of the architecture description fall within the scope of the architecture conceptualization and architecture elaboration processes as defined in ISO/IEC/IEEE 42020. However, it is sometimes the case that the architecture description is evaluated concurrently with the evaluation of the architecture itself.

> **注**：本文件处理的是对架构的评估，而不是对架构描述适宜性的评估。与架构描述评估有关的事项属于 ISO/IEC/IEEE 42020 所定义的架构概念化过程和架构细化过程的范围。然而，有时会出现架构描述与架构本身的评估同时进行的情形。

The entity being evaluated can be of several kinds, as illustrated in the following examples: enterprise, organization, solution, system, subsystem, business, data (as a data element or data structure), application, information technology (as a collection), mission, product, service, software item, hardware item, etc. The kind of entity can also be a product line, family of systems, system of systems, etc. It also spans the variety of applications that utilize digital technology such as mobile, cloud, big data, robotics, Internet of Things (IoT), web, desktop, embedded systems, and so on.

被评估的实体能是若干种类，如下列示例所示：企业、组织、解决方案、系统、子系统、业务、数据（作为数据元素或数据结构）、应用、信息技术（作为集合）、使命、产品、服务、软件项、硬件项等。实体的种类还能是产品线、系统族、系统的系统等。它还涵盖利用数字技术的各类应用，如移动、云、大数据、机器人、物联网（IoT）、web、桌面、嵌入式系统等。

The generic Architecture Evaluation (AE) framework specified in this document can be used in support of the Architecture Evaluation process defined in ISO/IEC/IEEE 42020. Specific frameworks can be derived from this generic framework, which can provide a mapping to the system life cycle processes in ISO/IEC/IEEE 15288 or to the software life cycle processes in ISO/IEC/IEEE 12207.

本文件规定的通用架构评估（AE）框架能用于支持 ISO/IEC/IEEE 42020 所定义的架构评估过程。专门框架能由该通用框架导出，这些专门框架能提供到 ISO/IEC/IEEE 15288 中的系统生存周期过程或 ISO/IEC/IEEE 12207 中的软件生存周期过程的映射。

### 2 Normative references 规范性引用文件

There are no normative references in this document.

本文件没有规范性引用文件。

### 3 Terms and definitions 术语和定义

For the purposes of this document, the following terms and definitions apply.

下列术语和定义适用于本文件。

ISO, IEC and IEEE maintain terminological databases for use in standardization at the following addresses:

ISO、IEC 和 IEEE 为标准化用途维护术语数据库，地址如下：

- ISO Online browsing platform: available at https://www.iso.org/obp

- ISO 在线浏览平台：https://www.iso.org/obp

- IEC Electropedia: available at http://www.electropedia.org/

- IEC Electropedia：http://www.electropedia.org/

- IEEE Standards Dictionary Online: available at: http: /ieeexplore.ieee.org/xpls/dictionary.jsp

- IEEE Standards Dictionary Online：http: /ieeexplore.ieee.org/xpls/dictionary.jsp

> **NOTE** Definitions for other terms typically can be found in ISO/IEC/IEEE 247651).

> **注**：其他术语的定义通常能在 ISO/IEC/IEEE 247651) 中找到。

#### 3.1 architecture 架构

fundamental concepts or properties of an entity in its environment (3.7) and governing principles for the realization and evolution of this entity and its related life cycle processes

实体在其环境(3.7)中的基本概念或属性，以及用于实现和演进该实体及其相关生存周期过程的管控原则

> **Note 1 to entry:** Architecture entity (3.3) is the term used in this document when referring to the entity being architected or the entity subject to architecture processes. The fundamental concepts or properties of the architecture entity are usually intended to be embodied in the entity’s components, the relationships between components, and the relationships between the entity and its environment.

> **注 1**：架构实体(3.3)是本文件中用于指被架构的实体或受架构过程作用的实体的术语。架构实体的基本概念或属性通常旨在体现于实体的组件、组件之间的关系以及实体与其环境之间的关系之中。

> **Note 2 to entry:** The concept of architecture used in this document applies broadly to the entity being architected or evaluated. This allows for a more generalized usage when the elements in this document are applied.

> **注 2**：本文件所用的架构概念广泛适用于被架构或被评估的实体。这使得应用本文件中的各要素时能有更为通用的用法。

> **Note 3 to entry:** The entity to be architected can be of several kinds, as illustrated in the following examples: enterprise, organization, solution, system, subsystem, business, data (as a data element or data structure), application, information technology (as a collection), mission, product, service, software item, hardware item, product line, family of systems, system of systems, etc. It also spans the variety of applications that utilize digital technology such as mobile, cloud, big data, robotics, Internet of Things (IoT), web, desktop, embedded systems, and so on.

> **注 3**：被架构的实体能是若干种类，如下列示例所示：企业、组织、解决方案、系统、子系统、业务、数据（作为数据元素或数据结构）、应用、信息技术（作为集合）、使命、产品、服务、软件项、硬件项、产品线、系统族、系统的系统等。它还涵盖利用数字技术的各类应用，如移动、云、大数据、机器人、物联网（IoT）、web、桌面、嵌入式系统等。

> **Note 4 to entry:** Representation of the concepts or properties of an entity and governing principles is captured in architecture models.

> **注 4**：实体的概念或属性以及管控原则的表示，记录于架构模型之中。

> **Note 5 to entry:** Architectures can address a wide range of concerns (3.6) expressed, for example, through architecture views and models, as illustrated in the following examples associated with particular kinds of architectures such as: security architecture, functional architecture, physical architecture, resilience architecture, etc.

> **注 5**：架构能处理范围广泛的关注点(3.6)，这些关注点例如通过架构视图和模型来表达，正如下列与特定种类架构相关的示例所示：安全架构、功能架构、物理架构、韧性架构等。

> [SOURCE: ISO/IEC/IEEE 42020:2019, 3.3]

> **来源**：ISO/IEC/IEEE 42020:2019, 3.3

#### 3.2 architecture description 架构描述

work product used to express an architecture (3.1)

用于表达架构(3.1)的工作产品

> **Note 1 to entry:** This document does not require the existence or use of an architecture description when performing an architecture evaluation (3.4). Some value (3.10) assessment methods do not demand existence of documented architecture models or views. Examples are customer focus group, expert panels and quality workshops where sufficient knowledge of the architecture is in the people participating in use of these methods. The same is true for architectural analysis in that not all methods applied here necessarily need an explicit description of the architecture.

> **注 1**：本文件不要求在实施架构评估(3.4)时存在或使用架构描述。某些价值(3.10)评定方法并不要求存在形成文件的架构模型或架构视图。例如客户焦点小组、专家小组和质量研讨会，使用这些方法的人员本身即具备关于架构的充分知识。架构分析亦如此：此处所应用的方法并非全都需要架构的显式描述。

> [SOURCE: ISO/IEC/IEEE 42010:2011, 3.3, modified — The abbreviated term “AD” has been removed; Note 1 to entry has been added.]

> **来源**：ISO/IEC/IEEE 42010:2011, 3.3，修改——缩写术语“AD”已删除；增加了注 1。

1) System and software engineering — Vocabulary, available at www.computer.org/sevocab.

1) 系统与软件工程——词汇，可从 www.computer.org/sevocab 获取。

#### 3.3 architecture entity 架构实体

thing being characterized by an architecture (3.1)

由架构(3.1)刻画的事物

> **EXAMPLE** The following are kinds of architecture entities that can be dealt with by the architecture processes: enterprise, organization, solution, system (including software systems), subsystem, business, data (as a data element or data structure), application, information technology (as a collection), mission, product, service, software item, hardware item, product line, family of systems, system of systems, collection of systems, collection of applications, etc.

> **示例**：下列是能由架构过程处理的架构实体的种类：企业、组织、解决方案、系统（包括软件系统）、子系统、业务、数据（作为数据元素或数据结构）、应用、信息技术（作为集合）、任务、产品、服务、软件项、硬件项、产品线、系统族、系统的系统、系统集合、应用集合等。

> **Note 1 to entry:** When referring to the architecture itself of these architecture entities, it is common practice to place the name of the kind of entity in front of the word architecture. For example, the phrase system architecture is used when the thing being dealt with during the architecting effort is a system. Likewise, for the other kinds of entities that are being dealt with during the architecting effort.

> **注 1**：当指称这些架构实体自身的架构时，通常的做法是将实体种类的名称置于“架构”一词之前。例如，当架构工作期间所处理的事物是系统时，使用“系统架构”这一短语。对于架构工作期间所处理的其他种类的实体，同样如此。

> [SOURCE: ISO/IEC/IEEE 42020:2019, 3.6, modified — The words “considered, described, discussed, studied, or otherwise addressed during the architecting effort” have been replaced with “characterized by an architecture”.]

> **来源**：ISO/IEC/IEEE 42020:2019, 3.6，修改——“在架构工作期间被考虑、描述、讨论、研究或以其他方式处理的”一语已替换为“由架构刻画”。

#### 3.4 architecture evaluation AE 架构评估 AE

judgment about one or more architectures (3.1) with respect to the specified evaluation objectives EXAMPLE 1 Various kinds of judgments could be made during an architecture evaluation, such as validating that architectures address the concerns (3.6) of stakeholders (3.9), assessing the quality of architectures with respect to their intended purpose, assessing the value (3.10) of architectures or architecture entities to their stakeholders, determining whether architecture entities address their intended purpose, providing knowledge and information about architecture entities and identifying risks and opportunities associated with architectures.

针对规定的评估目标，对一个或多个架构(3.1)作出的判断在架构评估期间能作出各种判断，例如：确认架构是否应对利益相关方(3.9)的关注点(3.6)；针对架构的预期目的评定架构的质量；评定架构或架构实体对其利益相关方的价值(3.10)；确定架构实体是否满足其预期目的；提供关于架构实体的知识与信息；以及识别与架构相关的风险与机遇。

> **EXAMPLE 2** Examples of architecture evaluations are provided in Annex C.

> **示例 2**：架构评估的示例见附录 C。

> **Note 1 to entry:** A decision regarding disposition of the architecture is usually outside the scope of an AE effort, although it could be done in conjunction with the AE effort. The AE results are often reported to a decision maker who makes the actual determination of disposition based on those results and sometimes also on other factors (3.8) not considered by the AE effort. Sometimes this determination is called an “evaluation” but for the purpose of this document, the evaluation is limited to just the judgment with respect to relevant evaluation objectives.

> **注 1**：关于架构处置的决策通常不在 AE 工作的范围之内，尽管它能与 AE 工作结合进行。AE 结果常报告给决策者，由决策者基于这些结果、有时还基于 AE 工作未考虑的其他因素(3.8)作出实际的处置确定。有时这种确定被称为“评估”，但就本文件而言，评估仅限于针对相关评估目标作出的判断。

#### 3.5 architecture evaluation framework 架构评估框架

conventions, principles and practices for evaluating architectures (3.1) in a consistent and repeatable manner EXAMPLE Examples of AE frameworks are provided in Annex D for the following cases: Architecture Tradeoff Analysis Method (ATAM), the Method Framework and QUASAR method and Analysis of Alternatives (AoA).

以一致且可重复的方式评估架构(3.1)的惯例、原则与实践附录 D 针对下列情形给出了 AE 框架的示例：架构权衡分析方法（ATAM）、方法框架与 QUASAR 方法，以及备选方案分析（AoA）。

> **Note 1 to entry:** This framework can be generic in nature or specific to a domain of application, a collection of concerns (3.6) to be examined or a methodology. This document defines a generic AE framework and a specific AE framework can be derived from the generic framework.

> **注 1**：本框架本质上能是通用的，也能特定于某个应用域、待考察的关注点(3.6)集合或某种方法论。本文件定义了一个通用 AE 框架，特定 AE 框架能由该通用框架导出。

> **Note 2 to entry:** An AE framework can enable AE efforts to be performed in a more consistent and repeatable manner.

> **注 2**：AE 框架能使 AE 工作以更一致且可重复的方式开展。

> **Note 3 to entry:** The evaluation framework can consist of different sub-architecture frameworks for an entity with many layers or levels. These could be defined and consolidated as part of the comprehensive architecture framework package.

> **注 3**：对于具有许多层或层级的实体，评估框架能由不同的子架构框架构成。这些子架构框架能作为综合架构框架包的一部分加以定义和合并。

#### 3.6 concern 关注点

matter of interest or importance to a stakeholder (3.9)

对利益相关方(3.9)而言具有利害关系或重要性的事项

> **EXAMPLE** Affordability, agility, availability, dependability, flexibility, maintainability, reliability, resilience, usability and viability are examples of concerns. Survivability, depletion, degradation, loss, obsolescence are examples of concerns. The PESTEL mnemonic is a reminder of other possible areas of concern: political, economic, social, technological, environmental, and legal. A longer list of examples is provided in 4.2.

> **示例**：经济可承受性、敏捷性、可用性、可信性、灵活性、维修性、可靠性、韧性、易用性和生存能力是关注点的示例。抗毁性、耗尽、退化、损失、过时也是关注点的示例。PESTEL 助记符提示了其他可能的关注点领域：政治的、经济的、社会的、技术的、环境的和法律的。4.2 给出了更长的示例清单。

> **Note 1 to entry:** The concept of concern is similar to “quality attributes” as used in the ATAM. See Annex D for an overview of the ATAM approach. In ATAM, quality attributes are typically decomposed into concerns.

> **注 1**：关注点的概念与 ATAM 中所用的“质量属性”类似。ATAM 途径的概述见附录 D。在 ATAM 中，质量属性通常分解为关注点。

> **Note 2 to entry:** The concept of concern is similar to the concept of quality. See A.4 for an overview of the quality concept.

> **注 2**：关注点的概念与质量的概念类似。关于质量的概念的概述见 A.4。

> [SOURCE: ISO/IEC/IEEE 42020:2019, 3.8, modified — In EXAMPLE, reference to 4.2 has been added; Notes 1 and 2 to entry have been added.]

> **来源**：ISO/IEC/IEEE 42020:2019, 3.8，修改——在示例中增加了对 4.2 的引用；增加了注 1 和注 2。

#### 3.7 environment 环境

context determining the setting and circumstances of influences upon an architecture entity (3.3) or upon which the architecture entity can have an influence

决定对架构实体(3.3)的影响的场景与情形的语境，或该架构实体能对其施加影响的语境

> **Note 1 to entry:** There can be things beyond the environment that have an indirect impact on the architecture entity. It could be important to account for these indirect effects by incorporating these causative agents in the environment even though they are not usually considered to be within the immediate context. Value (3.10) chain analysis is an example of where this is done.

> **注 1**：可能存在环境之外、对架构实体有间接影响的事物。通过将这些致因因素纳入环境来考虑这些间接影响，可能是重要的，即使它们通常并不被认为处于直接语境之内。价值(3.10)链分析就是这样做的一个示例。

#### 3.8 factor 因素

circumstance, fact or influence that contributes to a result or outcome

促成结果或结局的情形、事实或影响

> **Note 1 to entry:** A factor is something that contributes causally to a result. Factors identification can sometimes be driven by knowledge of desired effects.

> **注 1**：因素是在因果上促成结果的某种事物。因素的识别有时能由对期望效果的了解所驱动。

#### 3.9 stakeholder 利益相关方

role, position, individual or organization having a right, share, claim or other interest in an architecture entity (3.3) or its architecture (3.1) that reflects their needs and expectations

对架构实体(3.3)或其架构(3.1)拥有权利、份额、主张或其他利益，且该利益反映其需要与期望的角色、职位、个人或组织

> [SOURCE: ISO/IEC/IEEE 42020:2019, 3.20]

> **来源**：ISO/IEC/IEEE 42020:2019, 3.20

#### 3.10 value 价值

regard that something is held to deserve; the importance, worth, or usefulness of something to somebody

某事物被认为值得的重视；某事物对某人的重要性、所值或有用性

> **Note 1 to entry:** Architecture evaluation (3.4) is focused primarily on the value of an architecture (3.1) with respect to stakeholder (3.9) concerns (3.6) or architecture objectives for that thing. However, sometimes the purpose of the evaluation effort is, by inference, to determine the impact of the architecture on the value of the architecture entity (3.3) when the entity is developed or evolved to align with the architecture concepts and properties.

> **注 1**：架构评估(3.4)主要关注架构(3.1)相对于利益相关方(3.9)关注点(3.6)或该事物的架构目标的价值。然而，有时评估工作的目的是通过推断来确定：当架构实体(3.3)被开发或演化以与架构概念和性质保持一致时，架构对该实体的价值的影响。

> **Note 2 to entry:** The determination of architecture value can take various aspects into account, such as worth, significance, importance, usefulness, benefit, and quality. These words have similar but not identical meaning. Worth is usually what one is willing to pay for something. Significance is about being worthy of attention. Importance is about the state or fact of being of great significance or value. Usefulness is about serving some purpose, or about being advantageous, helpful or of good effect. Benefit is about an advantage or profit gained from something. Quality is about the degree of excellence of something. Throughout this document, the term value is used to mean one or more of these other concepts, as appropriate.

> **注 2**：架构价值的确定能考虑各种方面体，如所值、意义、重要性、有用性、益处和质量。这些词的含义相似但不完全相同。所值通常是一个人愿意为某事物支付的代价。意义关乎值得关注。重要性关乎具有重大意义或价值的状态或事实。有用性关乎服务于某种目的，或关乎有益、有帮助或有良好效果。益处关乎从某事物获得的优势或收益。质量关乎某事物的卓越程度。在本文件中，术语“价值”用于按情况表示这些其他概念中的一个或多个。

> **Note 3 to entry:** Even though a new architecture could be found to be of greater value with respect to the current situation, this needs to be balanced against the costs and risks of adopting the new architecture. So, it is not necessarily the case that when examining architecture alternatives, the one with the maximum value is proposed as the preferred choice since the extra cost or risk of this architecture might not be worth the extra burden. This is sometimes referred to as the benefit-cost ratio or some other term with similar meaning.

> **注 3**：即使可能认定新架构相对于当前情形具有更大的价值，也需要将其与采用该新架构的成本和风险相权衡。因此，在考察架构备选方案时，并不必然提出具有最大价值的方案作为首选，因为该架构的额外成本或风险可能不值得额外的负担。这有时称为效益成本比或含义类似的其他术语。

> **Note 4 to entry:** Value is determined primarily in the Value Assessment Tier of the evaluation framework illustrated in Figure 1. Requirements on value assessment are specified in 6.2.

> **注 4**：价值主要在图 1 所示的评估框架的价值评定层级中确定。关于价值评定的要求在 6.2 中规定。

### 4 Conceptual foundation 概念基础

#### 4.1 General 总则

This clause introduces key concepts used in this document with respect to architecture evaluation. The terms and the concepts presented in this clause are used in Clauses 6 through 8 to express requirements. The conceptual model of architecture evaluation is presented in parts throughout this clause.

本章介绍本文档中与架构评估有关的各项关键概念。本章给出的术语与概念在第 6 章至第 8 章中用于表述要求。架构评估的概念模型在本章中分部分给出。

The generic AE framework work products and elements, illustrated in Figure 1 and specified in this document, can be used in support of the Architecture Evaluation process defined in ISO/IEC/IEEE 42020. Specific frameworks can be derived from this generic framework.

本文档规定并在图 1 中示出的通用 AE 框架工作产品与元素，能用于支持 ISO/IEC/IEEE 42020 中定义的架构评估过程。特定框架能从这一通用框架导出。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 1 — Generic architecture evaluation framework**

**图 1 — 通用架构评估框架**

These specific frameworks may range from those targeting industry segments, such as automotive or refinery operations, to those targeting common business processes, such as portfolio management and program planning, and to those targeting common business architectures, such as banking, retail, insurance, telecom, travel and hospitality, etc. Specific frameworks allow the user to capture and reuse concepts common to many enterprises and thereby increase the efficiency with which architectures can be evaluated.

这些特定框架的范围，可从针对行业细分领域（如汽车或炼油运营）的框架，到针对通用业务流程（如项目组合管理与项目群规划）的框架，再到针对通用业务架构（如银行、零售、保险、电信、旅游与酒店等）的框架。特定框架使用户能捕获并复用许多企业共有的概念，从而提高架构评估的效率。

Architecture evaluation makes a judgment with respect to how well architecture objectives have been or will be achieved. It can provide answers to an identified set of questions to, for example, provide inputs to strategic decision making (such as whether it would be cheaper in the long run to modify an existing architecture to close value gaps), or to produce a new architecture that better addresses current and future stakeholder needs. An architecture evaluation can also provide inputs to decisions made at the operational and tactical levels. For example, the evaluation may provide useful information regarding capability limitations of the entity in question.

架构评估就架构目标已实现或将要实现的程度作出判断。它能针对已识别的一组问题给出答案，例如为战略决策提供输入（如从长远看，修改现有架构以弥合价值差距是否更为经济），或为产生能更好地满足当前与未来利益相关方需求的新架构提供输入。架构评估还能为在运行层面与战术层面所作的决策提供输入。例如，评估可提供关于所涉实体能力局限的有用信息。

The subclauses below describe the elements used in each tier of the generic framework and describe the different kinds of specific frameworks that utilize these elements.

以下各条描述通用框架各层级所用的元素，并描述利用这些元素的不同种类的特定框架。

#### 4.2 Architecture evaluation context 架构评估语境

Figure 2 depicts the context of architecture evaluation in terms of key concepts and the relations between them.

图 2 按关键概念及概念间的关系描绘了架构评估的语境。

> **NOTE 1** The graphical notation used in this document is a simplified version of entity-relationship modeling. NOTE 2 Only the key associations are shown in the diagrams.

> **注 1**：本文档中使用的图形记号是实体—关系建模的简化版本。图中仅示出关键的关联。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 2 — Context of architecture evaluation**

**图 2 — 架构评估的语境**

The AE effort can be performed at many stages of entity development, including during conceptual design through to during the operation and maintenance. The evaluation may need to be updated to reflect changes as the entity design progresses through its lifecycle.

AE 工作能在实体开发的许多阶段进行，从概念设计期间直至运行与维护期间。随着实体设计在其生存周期中推进，评估可能需要更新以反映变化。

An AE effort is often performed to determine the potential or actual value of the associated architecture entity. However, the primary focus of the AE effort is on the value of the architecture itself even though the ultimate aim could be a determination of the value of the architecture entity, or the impact on the environment, or the impact on the business that uses the architecture entity, etc. But the value of the architecture entity or other benefits might be determined by some other effort, such as system analysis, requirements analysis, business needs analysis, portfolio management, program assessment and evaluation, environmental impact assessment, etc.

进行 AE 工作往往是为了确定相关联架构实体的潜在价值或实际价值。然而，AE 工作的主要着眼点在于架构本身的价值，即使其最终目的可能是确定该架构实体的价值，或对环境的影响，或对使用该架构实体的业务的影响等。但架构实体的价值或其他收益可能由其他某项工作确定，如系统分析、需求分析、业务需求分析、项目组合管理、项目群评定与评估、环境影响评定等。

Architecture evaluation makes a judgment regarding the extent to which architecture objectives have been or will be achieved. Because of this, it is dealing with the degree to which the architecture provides things such as needs satisfaction, feasibility, understandability, usability desired qualities.

架构评估就架构目标已实现或将要实现的程度作出判断。因此，它处理的是架构在多大程度上提供需求满足、可行性、可理解性、可用性等所期望的质量。

The environment within which the architecture entity is situated could provide strategic context for determining the ways in which the architecture evaluation is conducted. The environment could also be a key factor in understanding the nature of stakeholder concerns. States and modes of operation of the architecture entity are often from the usage perspective of entities in the environment.

架构实体所处的环境能为确定架构评估的开展方式提供战略语境。环境也可能是理解利益相关方关注点本质的关键因素。架构实体的状态与运行模式，往往来自环境中各实体的使用角度。

Stakeholders have interests in the architecture or associated architecture entities. These interests (called concerns) are usually the primary focus of architecture evaluation. This judgment provided by the AE effort represents the extent to which stakeholder concerns have been or will be satisfied by decisions that affect the associated architecture entities or their environments. This judgment can also represent the extent to which the architecture fulfills its intended purpose. Ways to measure this will be identified or specified during the AE effort along with the means by which these measures will be ascertained.

利益相关方在架构或相关联的架构实体中怀有利益。这些利益（称为关注点）通常是架构评估的主要着眼点。AE 工作所作出的这一判断，表示影响相关联架构实体或其环境的各项决策已在多大程度上或将在多大程度上满足利益相关方的关注点。这一判断还能表明架构在多大程度上实现其预期目的。衡量这一点的方式将在 AE 工作期间予以识别或规定，同时还将确定据以查明这些量度的手段。

> **NOTE 3** Determination of the extent to which concerns are satisfied could entail either measurement of the degree to which something is done or a determination of whether something is true or not. Pass/fail criteria could need to be established prior to performing the evaluation. These criteria could be defined in the AE plan or could be established by the organization as a matter of policy or directive.

> **注 3**：确定关注点得到满足的程度，既可能需要对某事项做到的程度进行测量，也可能需要判定某事项是否成立。可能需要在实施评估之前建立合格／不合格准则。这些准则可在 AE 计划中定义，也可由组织作为方针或指令事项予以建立。

> **EXAMPLE 1** Stakeholders include people and organizations such as: users, operators, acquirers, owners, suppliers, developers, builders and maintainers. It also includes authorities engaged in certifying the architecture entity for a variety of purposes such as its readiness for use, conformance to legal provisions and compliance with regulations and policies with respect to safety, security, privacy, environmental impact, etc., as well as evaluators such as funding agencies, integration authorities, governance boards, management boards, client representatives and regulatory authorities. Stakeholders can go beyond individuals and organizations to also include things like governmental bodies, supply chains, value chains, institutions, and social groups.

> **示例 1**：利益相关方包括个人与组织，如：用户、操作员、获取方、所有者、供方、开发者、构建方与维护方。它还包括为多种目的从事架构实体认证的机构，这些目的如：架构实体是否已可供使用、是否符合法律规定、是否遵守与安全、信息安全、隐私、环境影响等有关的法规与方针；也包括各类评估者，如资助机构、集成机构、治理委员会、管理委员会、客户代表与监管机构。利益相关方能超出个人与组织，还包括政府机关、供应链、价值链、各类机构与社会群体等。

> **EXAMPLE 2** Concerns include such things as: affordability, agility, alignment with business goals and strategies, autonomy, availability, behavior, business impact, capability, complexity, compliance to regulation, concurrency, control, cost, customer experience, data accessibility, deadlock, disposability, environment impact, error and exception handling, extensibility, evolvability, feasibility, flexibility, functionality, graceful degradation, information assurance, interoperability, inter-process communication, known limitations, maintainability, misuse, mission impact, modifiability, modularity, openness, performance, portability, privacy, quality of service, recoverability, reliability, resilience, resource utilization, schedule, security, shortcomings, state transitions through lifecycle, scalability, software and systems assurance (ISO/IEC 15026-1), structure, subsystem integration, architecture entity features, architecture entity properties, architecture entity purposes, usability, usage, viability, etc.

> **示例 2**：关注点包括下列各项：经济可承受性、敏捷性、与业务目标及战略的一致性、自主性、可用性、行为、业务影响、能力、复杂性、法规符合性、并发性、控制、成本、客户体验、数据可访问性、死锁、可弃置性、环境影响、错误与异常处理、可扩展性、可演化性、可行性、灵活性、功能、优雅降级、信息保证、互操作性、进程间通信、已知局限、可维护性、误用、任务影响、可修改性、模块化、开放性、性能、可移植性、隐私、服务质量、可恢复性、可靠性、韧性、资源利用、进度、信息安全、缺陷、生存周期中的状态转换、可伸缩性、软件与系统保证（ISO/IEC 15026-1）、结构、子系统集成、架构实体特征、架构实体属性、架构实体用途、易用性、使用、生存能力等。

> **EXAMPLE 3** The PESTEL mnemonic is a reminder of other possible areas of concern: political, economic, social, technological, environmental, and legal. Survivability, depletion, degradation, loss and obsolescence are other examples of areas of concern. Other mnemonics that could be useful include STEEPLED that adds ethics and demographic factors, SPELIT that adds intercultural factors, STEER that adds regulatory factors and STEP that adds ecological factors.

> **示例 3**：PESTEL 助记符提示了其他可能的关注领域：政治的、经济的、社会的、技术的、环境的和法律的。抗毁性、耗尽、退化、损失和过时也是关注领域的其他示例。其他可能有用的助记符包括：STEEPLED 增加伦理与人口因素，SPELIT 增加跨文化因素，STEER 增加监管因素，STEP 增加生态因素。

> **EXAMPLE 4** Examples of value include such things as: physiological well-being, safety from harm, feelings, aesthetics, price, savings, sense of belonging, self-esteem and self-actualization.

> **示例 4**：价值的示例包括：生理福祉、免受伤害的安全、情感、审美、价格、节省、归属感、自尊与自我实现。

Architecture principles, although not shown in the diagram, will shape the architecture and can perform a key role in the architecture evaluation. An understanding of these principles can help guide proper evaluation of an architecture. These principles will influence selection of AE factors used throughout the evaluation effort and help in the identification of relevant concerns. Architectural features and functions need to be consistent with the architecture principles. See Reference [17] and [18].

架构原则虽未在图中示出，但会塑造架构，并能在架构评估中发挥关键作用。理解这些原则有助于指导对架构进行适当的评估。这些原则将影响贯穿评估工作所用的 AE 因素的选取，并有助于识别相关关注点。架构特性与功能需与架构原则保持一致。见参考文献 [17] 和 [18]。

#### 4.3 Architecture evaluation tiers 架构评估层级

##### 4.3.1 Evaluation synthesis 评估综合

Synthesis involves the combination of results from multiple value assessments to determine to what extent the evaluation objectives will be achieved. Stakeholders who have concerns about the subject of the evaluation could have specific goals that should be addressed in the evaluation. (These concerns could be about the architecture, the architecture entity or both.) These goals should be considered when establishing the factors and objectives to be used in the evaluation. These goals might not correspond to the original goals for the architecture when it was initially conceived.

综合涉及将多项价值评定的结果组合起来，以确定评估目标将在多大程度上得以实现。对评估对象抱有关注点的利益相关方可能具有应在评估中予以处理的具体目标。（这些关注点可能关于架构、架构实体或二者兼有。）在确立评估所用的因素与目标时，宜考虑这些目标。这些目标可能并不对应于架构最初构想时的原有目标。

> **NOTE 1** The experts involved in the evaluation are also stakeholders and can bring important evaluation objectives that are not a known concern for traditional stakeholders (such as acquirer, user, service provider), but are concerns that the profession defines to be important (and where the evaluators could be the best placed stakeholders to represent the profession).

> **注 1**：参与评估的专家也是利益相关方，能提出重要的评估目标，而这些目标并非传统利益相关方（如获取方、用户、服务提供方）的已知关注点，而是本专业界认定为重要的关注点（且在此情形下，评估者可能是最能代表本专业的利益相关方）。

Architecture trade-offs are identified and characterized during architecture development. However, they can be revisited during the evaluation synthesis. Trade-offs among stakeholder concerns and feasibility limitations will be identified. Typical trade-offs to consider are the following: cost vs performance, cost vs schedule, weight vs speed, accuracy vs timeliness, acquisition cost vs operating cost, ease of use vs security, flexibility vs predictability, agility vs robustness, risk vs reward, etc. Trade-offs could be with respect to the various factors within a single architecture or across alternative architectures under examination.

架构权衡在架构开发期间得以识别和表征。但它们能在评估综合期间被重新审视。将识别利益相关方关注点之间以及可行性局限之间的权衡。宜考虑的典型权衡如下：成本与性能、成本与进度、重量与速度、精度与及时性、获取成本与运行成本、易用性与安全性、灵活性与可预测性、敏捷性与稳健性、风险与回报等。权衡可能针对单一架构内的各种因素，也可能针对所考察的多个备选架构。

An AE effort examines one or more architectures with respect to potential stakeholder concerns about the associated architecture entities. Figure 3 depicts AE elements that can be used in an evaluation synthesis effort in terms of the key concepts and the relations between them. Most of these concepts are also used in related standards described in Annex B.

AE 工作针对与相关架构实体有关的潜在利益相关方关注点，考察一个或多个架构。图 3 按关键概念及其相互关系，描绘了可在评估综合工作中使用的 AE 要素。这些概念大多也用于附录 B 所述的相关标准。

> **NOTE 2** Value is determined primarily in the Value Assessment Tier of the evaluation framework illustrated in Figure 1. Requirements on value assessment are specified in 6.2.

> **注 2**：价值主要在评估框架的价值评定层级中确定，如图1 所示。对价值评定的要求在 6.2 中规定。

The evaluation synthesis effort is the result of applying the concepts in the document during the evaluation of one or more architectures to determine their value to stakeholders or the extent to which the architecture objectives are satisfied.

评估综合工作是在对一个或多个架构进行评估期间应用本文件所述概念的结果，用以确定架构对利益相关方的价值，或架构目标得到满足的程度。

> **NOTE 3** The evaluation synthesis effort is usually a non-trivial exercise that requires a pre-defined mapping of attributes and issues (gaps in desired outcomes) across the lineage of interactions between stakeholders and assets (and the services they rely upon to get their jobs done) and with respect to dependencies on the designs, development efforts and operations (used to deliver those assets and services), and finally with respect to the architectural artifacts relied upon by the designers, developers, users and operators.

> **注 3**：评估综合工作通常并非易事，它要求对属性与问题（预期结果中的差距）作预先定义的映射，覆盖利益相关方与资产（以及他们为完成工作所依赖的服务）之间交互的整个谱系，并针对对设计、开发工作与运行（用于交付这些资产与服务）的依赖关系，最后还针对设计者、开发者、用户与运行者所依赖的架构人工制品。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 3 — Key concepts with respect to evaluation synthesis effort**

**图 3 — 关于评估综合工作的关键概念**

AE objectives are derived from one or more of the relevant concerns. One or more AE approaches are used to address the AE objectives. AE objectives assigned to an AE approach help to determine what concerns are relevant to that approach and what approaches are relevant to each concern. More than one approach could be used within a single evaluation effort to improve the ability to address different aspects of the architecture leading to more accurate, cost-effective and timely evaluations.

AE 目标源自一个或多个相关关注点。使用一个或多个 AE 途径来处理 AE 目标。分配给某一 AE 途径的 AE 目标有助于确定哪些关注点与该途径相关，以及哪些途径与每个关注点相关。在单次评估工作中能使用不止一种途径，以提升处理架构不同方面体的能力，从而形成更准确、更具成本效益且更及时的评估。

> **EXAMPLE 1** Examples of AE approaches are: review panel, prototype demonstration, system experiment, modeling and simulation, model walkthrough, technical analysis, compliance audit, concept review and user symposium.

> **示例 1**：AE 途径的示例包括：评审专家组、原型演示、系统实验、建模与仿真、模型走查、技术分析、合规审计、概念评审和用户研讨会。

> **EXAMPLE 2** Examples of AE objectives are:

> **示例 2**：AE 目标的示例包括：

- Will the business solution meet primary business needs?

- 业务解决方案能否满足主要业务需求？

- Is the system affordable?

- 系统是否可负担？

- Will the service be dependable?

- 服务是否可信赖？

- Will the product have sufficient market penetration?

- 产品能否具有充分的市场渗透率？

- What is the return on investment?

- 投资回报率是多少？

> **NOTE 4** The AE approach does not necessarily have to be highly structured or formal in nature, which is why this is not called a “method.” A method, on the other hand, is a particular form of procedure for accomplishing something, especially a systematic or established one.

> **注 4**：AE 途径在性质上不必高度结构化或高度正式，这正是其不称为“方法”的原因。而方法则是完成某事的特定规程形式，尤其是系统性或已确立的规程形式。

> **NOTE 5** Evaluation of artifacts used to guide the design, development and delivery of assets and/or services can provide useful insights when assessing the value of architecture(s).

> **注 5**：在评定架构的价值时，对用于指导资产和／或服务的设计、开发与交付的人工制品进行评估，能提供有益的洞见。

Evaluation factors are established based on relevant stakeholder concerns. The evaluation factors will contribute to addressing one or more of the evaluation objectives. The evaluation approach determines how necessary information will be gathered and processed, and how evaluation criteria will be applied on the processed information to generate evaluation results for use in the AE report.

评估因素依据相关利益相关方关注点确立。评估因素将有助于处理一个或多个评估目标。评估途径确定如何收集和处理必要信息，以及如何对处理后的信息应用评估准则，以生成供 AE 报告使用的评估结果。

The evaluation approach will use value assessment results as one of the criteria for making judgment(s) about the architecture. Other criteria for making these judgments could include such things as technical feasibility, operational suitability, backward/forward compatibility, technology maturity, budget constraints, time limits, window of opportunity, intellectual property advantages, etc.

评估途径将把价值评定结果用作对架构作出判断的准则之一。作出这些判断的其他准则可包括：技术可行性、运行适用性、向后／向前兼容性、技术成熟度、预算约束、时间限制、机会窗口、知识产权优势等。

> **NOTE 6** Evaluation factors could be derived from the desired outcomes that stakeholders are trying to obtain from the services and assets they rely upon.

> **注 6**：评估因素能取自利益相关方力图从其依赖的服务与资产中获得的预期结果。

> **EXAMPLE 3** Examples of AE factors are cost, schedule, performance and risk.

> **示例 3**：AE 因素的示例包括成本、进度、性能与风险。

The AE plan guides management and execution of the AE effort by specifying, among other things, the evaluation objectives. It documents the purpose and scope of the evaluation and the circumstances under which the AE effort will be conducted. It documents the expected schedule and resources to deliver the evaluation results. The AE plan describes the evaluation approaches that will be driven by the evaluation objectives. The AE plan, if appropriate, can also specify the methods to be used for value assessment and architectural analysis.

AE 计划通过规定评估目标等内容，指导 AE 工作的管理与执行。它记录了评估的目的与范围，以及开展 AE 工作所依据的情形。它记录了交付评估结果所预期的进度与资源。AE 计划描述将由评估目标驱动的评估途径。AE 计划在适当时还能规定用于价值评定与架构分析的方法。

The AE plan identifies necessary information sources, such as:

AE 计划识别必要的信息来源，如：

- those that are useful for creating an understanding of the architecture as a basis for generating evaluation results and drawing valid conclusions;

- 有助于形成对架构的理解、以作为生成评估结果和得出有效结论的基础者；

- those that are useful for creating an understanding of architecture entities as a basis for making relevant judgments about the architecture; and

- 有助于形成对架构实体的理解、以作为对架构作出相关判断的基础者；以及

- non-architecture-related sources, such as business plans, cost data, project schedules, software code and operating manuals.

- 非架构相关来源，如业务计划、成本数据、项目进度、软件代码和操作手册。

> **NOTE 7** The activities in the Architecture Evaluation process specified in ISO/IEC/IEEE 42020 can be used as a guide when planning an AE effort. The planning activity specified in that AE process provides recommended tasks for planning an AE effort.

> **注 7**：ISO/IEC/IEEE 42020 中规定的架构评估过程中的活动能在规划 AE 工作时用作指南。该 AE 过程中规定的规划活动提供了用于规划 AE 工作的推荐任务。

The overall conclusions of the AE effort are provided in AE reports along with any supporting data and information.

AE 工作的总体结论连同任何支持性数据与信息在 AE 报告中提供。

> **NOTE 8** More than one report could be needed to address different audiences or possibly be provided as interim reports along the way. For example, the sponsor could receive a highly detailed report while the decision maker could receive a high-level summary with only the factors most relevant to the decision at hand. There could be a sensitive or classified version of the report for people with the appropriate clearances and another version that only contains unclassified or less sensitive information.

> **注 8**：为面向不同受众，可能需要不止一份报告，也可能在过程中以中期报告的形式提供。例如，发起方可收到一份高度详细的报告，而决策者可收到一份高层级摘要，其中仅包含与当前决策最相关的因素。报告可有面向具有相应权限的人员的敏感或涉密版本，另有仅包含非密或敏感度较低信息的版本。

##### 4.3.2 Value assessment 价值评定

Value assessment is a determination regarding the amount and kind of value a stakeholder can expect from the architecture. Value can be defined as either a qualitative description or a quantitative extent of this expectation from the use, possession or operation of the architecture entity.

价值评定是关于利益相关方可从架构预期获得的价值数量与种类的判定。价值能定义为针对来自架构实体的使用、拥有或运行的这一预期所作的定性描述或定量程度。

> **EXAMPLE 1** In some cases, the mere possession of an architecture entity can provide value to a stakeholder. For example, holding gold in the vault can provide security to the owner. A nation possessing a strong defensive capability can provide security to the citizens, hoping they never have to use such a capability.

> **示例 1**：在某些情况下，仅拥有架构实体即可为利益相关方提供价值。例如，在金库中持有黄金能为所有者提供安全保障。国家拥有强大的防御能力能为公民提供安全保障，尽管希望永远无需动用这种能力。

Value assessment may identify gaps as well as opportunities for improving stakeholder value. Information from architectural analysis contributes to value assessment.

价值评定可识别差距以及提高利益相关方价值的机会。来自架构分析的信息有助于价值评定。

An AE approach specifies one or more value assessment objectives to be used in the value assessment effort. The use of particular value assessment methods for an AE effort can be influenced by the nature of the AE objectives, the available information sources, prior evaluations of this kind, available evaluation methods and tools, anticipated value assessment results and relevant architecture methodologies.

AE 途径规定价值评定工作中要使用的一个或多个价值评定目标。AE 工作对特定价值评定方法的使用能受以下因素影响：AE 目标的性质、可用的信息源、以往同类评估、可用的评估方法与工具、预期的价值评定结果以及相关的架构方法论。

> **EXAMPLE 2** Examples of Assessment methods are: multi-attribute utility analysis (MAUA), mission impact assessment, business case analysis, socio-economic analysis, strategy-to-task analysis, user focus group, analysis of alternatives, environmental impact assessment, etc.

> **示例 2**：评定方法的示例有：多属性效用分析（MAUA）、任务影响评定、商业论证分析、社会经济分析、战略到任务分析、用户焦点小组、备选方案分析、环境影响评定等。

> **EXAMPLE 3** Examples of assessment objectives are:

> **示例 3**：评定目标的示例有：

- Will the business solution provide adequate productivity improvement?

- 业务解决方案能否提供足够的生产率提升？

- Is the system usable by available personnel?

- 系统能否由现有人员使用？

- Will the service provide information in a timely manner?

- 服务能否及时提供信息？

- Will the product provide accurate and timely data?

- 产品能否提供准确且及时的数据？

Figure 4 depicts the elements that can be used in a value assessment effort in terms of the key concepts and the relations between them. Value assessment objectives are intended to satisfy the AE objectives and frame the relevant stakeholder concerns. Value assessment factors will frame the relevant AE factors.

图 4 按关键概念及其相互关系，描绘了可在价值评定工作中使用的要素。价值评定目标旨在满足 AE 目标，并框定相关的利益相关方关注点。价值评定因素将框定相关的 AE 因素。

> **EXAMPLE 4** Examples of value assessment factors are: development cost, operational cost, development time, training time, ease of use, maintainability, resilience, dependability.

> **示例 4**：价值评定因素的示例有：开发成本、运行成本、开发时间、训练时间、易用性、可维护性、韧性、可信性。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 4 — Key concepts with respect to value assessment effort**

**图 4 — 价值评定工作的关键概念**

The assessment method may prescribe how necessary information will be gathered and processed, and how value assessment criteria will be applied on the processed information to generate value assessment results for use by an AE approach. The assessment method can be decomposed into specific activities, tasks, roles and artifacts pertinent to that method.

评定方法可规定如何收集和处理所需信息，以及如何将价值评定准则施加于处理后的信息以生成价值评定结果，供 AE 途径使用。评定方法能分解为与该特定方法相关的活动、任务、角色和人工制品。

> **NOTE 1** Where available, one or more applicable value models can be referenced to assist in formulating the value assessment criteria. Value models are information structures that organize metrics for a set of value assessment factors such that they can serve as tools for assessing and managing value. These models are built over time based on best practices and lessons learned for a variety of value assessment factors. Value models can be developed by an industry, established within an organization or derived from the architecture requirements specification. See for example the Structured Metrics Meta-Model[67].

> **注 1**：在可获得的情况下，可引用一个或多个适用的价值模型来协助制定价值评定准则。价值模型是一种信息结构，它为给定的一组价值评定因素组织度量指标，从而能用作评定和管理价值的工具。这些模型是随着时间推移，基于各种价值评定因素的最佳实践与经验教训而构建的。价值模型能由行业开发、在组织内确立，或从架构需求规格导出。例如见结构化度量元模型[67]。

The assessment method will specify, if needed, objectives for one or more analysis methods to be employed and how the architectural analysis results will be used in the value assessment.

评定方法将在需要时规定所采用的一个或多个分析方法的目标，以及在价值评定中如何使用架构分析结果。

> **NOTE 2** If the information needed to perform a value assessment is already available from other sources (such as industry reports, design documentation, architecture descriptions, operational data, previous analyses, experiments, or demonstrations, etc.) then there can be no need to perform an architectural analysis.

> **注 2**：如果执行价值评定所需的信息已可从其他来源获得（如行业报告、设计文档、架构描述、运行数据、以往分析、试验或演示等），则可能无需执行架构分析。

##### 4.3.3 Architectural analysis 架构分析

Architectural analysis examines the key attributes of an architecture, e.g. its characteristics along particular dimensions such as security, cost, performance, and so on, or the relevant attributes of the architecture entity, as well as actual or potential impacts on stakeholders or on the environment. It also examines architecture vision, principles, concepts and properties, etc. that are relevant to achieving the architectural analysis objectives. Analysis may also look at other aspects of the architecture such as forms, patterns, structures, behaviors, functions, flows, and so on, as well as examining the assumptions that were made about technologies, operations, policies, constraints, etc.

架构分析考察架构的关键属性，例如其在安全性、成本、性能等特定维度上的特性，或架构实体的相关属性，以及对利益相关方或环境的实际影响或潜在影响。它还考察与实现架构分析目标相关的架构愿景、原则、概念与性质等。分析还可考察架构的其他方面，如形式、模式、结构、行为、功能、流等，并考察关于技术、运行、方针、约束等所作的假设。

> **NOTE 1** Architectural analysis is optional since the information needed to generate value assessment results could already be available from other sources, hence removing the need to do analysis. The AE plan will indicate if and to what extent that architectural analysis is needed for a particular AE effort.

> **注 1**：架构分析是可选的，因为生成价值评定结果所需的信息可能已可从其他来源获得，从而无需进行分析。AE 计划将指明特定 AE 工作是否需要架构分析以及所需程度。

An assessment method will employ, if needed, one or more analysis methods. The employment of particular analysis methods for a particular AE effort can be influenced by the nature of the assessment objectives, the available information sources, prior analyses of this kind, available analysis methods and tools, anticipated analysis results and relevant architecture methodologies.

评定方法将在需要时采用一个或多个分析方法。特定 AE 工作对特定分析方法的使用能受以下因素影响：评定目标的性质、可用的信息源、以往同类分析、可用的分析方法与工具、预期的分析结果以及相关的架构方法论。

> **EXAMPLE 1** Examples of Analysis methods are: functional analysis; object oriented analysis, performance analysis, behavioral analysis, cost and schedule analysis, risk and opportunity analysis, failure modes, effects and criticality analysis (FMECA), focus group surveys and Delphi method. (All of these methods can be used for architectural analysis, as well as for architecture development.)

> **示例 1**：分析方法的示例有：功能分析；面向对象分析、性能分析、行为分析、成本与进度分析、风险与机会分析、故障模式、影响及危害性分析（FMECA）、焦点小组调查和德尔菲法。（所有这些方法既能用于架构分析，也能用于架构开发。）

> **EXAMPLE 2** Examples of analysis objectives are:

> **示例 2**：分析目标的示例有：

- Will the business solution have a positive return on investment exceeding the hurdle rate?

- 业务解决方案的投资回报能否为正并超过最低可接受收益率？

- Is the system producible in large enough quantities to meet the target price?

- 系统能否以足够大的数量生产，以满足目标价格？

- Will the service provide enough bandwidth to meet expected user demand?

- 服务能否提供足够的带宽，以满足预期的用户需求？

- Will the product deliver data fast enough to meet its requirements?

- 产品能否足够快地交付数据，以满足其要求？

- Will the equipment be reliable enough to provide the expected level of availability?

- 设备能否足够可靠，以提供预期的可用性水平？

Figure 5 depicts the elements that can be used in an architectural analysis effort in terms of the key concepts and the relations between them. Analysis objectives are intended to satisfy the assessment objectives and frame the relevant stakeholder concerns. Analysis factors will frame the relevant assessment factors.

图 5 按关键概念及其相互关系，描绘了可在架构分析工作中使用的要素。分析目标旨在满足评定目标，并框定相关的利益相关方关注点。分析因素将框定相关的评定因素。

> **EXAMPLE 3** Examples of analysis factors are: operational latency, accuracy, resolution, mean time between failure, uptime.

> **示例 3**：分析因素的示例有：运行延迟、准确度、分辨率、平均故障间隔时间、正常运行时间。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 5 — Key concepts with respect to an architectural analysis effort**

**图 5 — 架构分析工作的关键概念**

The analysis method may prescribe how necessary information will be gathered and processed, and how analysis criteria will be applied on the processed information to generate analysis results for use by an assessment method. The analysis method can be decomposed into specific activities, tasks, roles and artifacts pertinent to that method.

分析方法可规定如何收集和处理所需信息，以及如何将分析准则施加于处理后的信息以生成分析结果，供评定方法使用。分析方法能分解为与该特定方法相关的活动、任务、角色和人工制品。

Analysis factors are identified based on the relevant architectural features, functions, quality characteristics, conceptual properties, and so on, related to the analysis objectives.

分析因素依据与分析目标相关的架构特征、功能、质量特性、概念属性等予以识别。

> **EXAMPLE 4** Examples of Analysis factors are: functionality, performance, number of interfaces, types of message elements transmitted and received, size, weight, power, cyber security, threat vulnerability, resilience, latency and response time.

> **示例 4**：分析因素的示例有：功能性、性能、接口数量、所传输和接收的消息元素类型、尺寸、重量、功耗、网络安全、威胁脆弱性、韧性、延迟和响应时间。

> **NOTE 2** A measures model can be used as a foundation for evaluating and assessing the quality of an architecture. The measures model can provide insights on how to achieve alignment back to functional, operational and performance measures for the organization. This can provide justification for investing in good architecture practices (part of the business case). See for example the Structured Metrics Meta-Model provided by OMG[67]. See Annex A for information about quality characteristics and value.

> **注 2**：度量模型可用作评估和评定架构质量的基础。度量模型能就如何回溯对齐到组织的功能度量、运营度量和性能度量提供洞见。这能为投资于良好架构实践（业务论证的一部分）提供理由。例如，见 OMG 提供的结构化度量元模型[67]。关于质量特性与价值的信息，见附录 A。

#### 4.4 Architecture evaluation conceptual model 架构评估概念模型

The overall conceptual model used in this document for architecture evaluation is illustrated in Figure 6.

本文件用于架构评估的总体概念模型如图 6 所示。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 6 — Conceptual model for architecture evaluation**

**图 6 — 架构评估概念模型**

#### 4.5 Comparison between assessment and analysis 评定与分析之比较

Assessment is used to determine the extent to which an architecture provides value to stakeholders, where value is associated with addressing stakeholder concerns or meeting architecture objectives. Value is also associated with the extent to which the architecture is aligned to its intended purpose. A number of examples are provided in Table 1 to show the distinctions between assessment and analysis.

评定用于确定架构向利益相关方提供价值的程度，其中价值与处理利益相关方关注点或满足架构目标相关联。价值还与架构与其预期目的相一致的程度相关联。表 1 给出了若干示例，以说明评定与分析之间的区别。

**Table 1 — Assessment vs analysis comparison**

**表 1 — 评定与分析比较**

| Characteristics ／ 特性 | Value assessment ／ 价值评定 | Architectural analysis ／ 架构分析 |
| --- | --- | --- |
| Goal orientation ／ 目标导向 | Ends Objectives (often multi-level) ／ 目的目标（常为多层级） | Means Objectives (often multi-level) ／ 手段目标（常为多层级） |
| Results ／ 结果 | Passes “judgment” ／ 作出“判断” | Matters of Fact ／ 事实问题 |
| Breadth ／ 广度 | Single, Unified Activity ／ 单一、统一的活动 | Multiple, Separate Activities ／ 多个、各自独立的活动 |
| Basis of work ／ 工作依据 | Synthesis of analysis results ／ 分析结果的综合 | Technical and other analyses ／ 技术分析及其他分析 |
| Scope ／ 范围 | Utility, Value, Worth, Priorities, Ranking, Trade-offs ／ 效用、价值、价值量、优先级、排序、权衡 | Ways & Means ／ 方式与手段 |
| Focus ／ 着眼点 | Effectiveness, Efficiencies, Equities ／ 有效性、效率、公平性 | Performance determination, Limits identification (bounds) ／ 性能确定、限值识别（边界） |
| Typical figures of merit ／ 典型品质因数 | Measure of Effectiveness (MOE’s), Return on Investment (ROI), Breakeven Point, Key Success Factors (KSF’s) ／ 效能度量（MOE）、投资回报率（ROI）、盈亏平衡点、关键成功因素（KSF） | Measures of Performance (MOP’s), Key Performance Parameters (KPP’s), Technical Performance Measures (TPM’s), Quality Metrics ／ 性能度量（MOP）、关键性能参数（KPP）、技术性能度量（TPM）、质量度量指标 |
| Key items of interest ／ 关键关注事项 | Competing Concerns, performing tradeoffs, achieving balance & robustness ／ 相互竞争的关注点、进行权衡、达成平衡与稳健性 | Individual Concerns, determining system properties & characteristics ／ 单项关注点、确定系统属性与特性 |
| Primary questions of interest ／ 主要关注问题 | So what? Who cares? What impacts? Why? Why not? ／ 那又如何？谁在乎？有何影响？为什么？为什么不？ | What, where, when, how, how much, how often? ／ 是什么、在哪里、何时、如何、多少、多久一次？ |

#### 4.6 Architecture evaluation factors 架构评估因素

A factor is a circumstance, fact or influence that contributes to a result or outcome. It is something that contributes causally to a result. Identification of factors can sometimes be driven by knowledge of desired effects. Factors should be consistent with the architectural principles that shaped the architecture; and these principles should influence selection of factors to use in the evaluation.

因素是有助于形成某一结果或结局的情况、事实或影响。它是因果性地促成某一结果的事物。因素的识别有时能由对期望效果的了解所驱动。因素宜与塑造该架构的架构原则相一致；这些原则宜影响评估中所用因素的选择。

The factors used in an architecture evaluation are central in helping to organize the evaluation effort and to achieve more transparent and understandable results.

架构评估中所用的因素，对于帮助组织评估工作并取得更透明、更易理解的结果具有核心作用。

> **EXAMPLE** Vitruvius, the Roman architect, is known for asserting in his book De architectura[38] that a structure must exhibit the three qualities of firmitas, utilitas, venustas – that is, it must be solid, useful, beautiful. These are sometimes called the Vitruvian virtues or the Vitruvian Triad. This is a good example of factors that can be used in an architecture evaluation.

> **示例**：罗马建筑师维特鲁威（Vitruvius）以其在《建筑十书》（De architectura）[38]中的论断而闻名：建筑物必须体现 firmitas、utilitas、venustas 三种品质——即坚固、实用、美观。这三者有时被称为维特鲁威美德或维特鲁威三要素。这是可用于架构评估的因素的一个良好示例。

> **NOTE** Examples of factors decomposition are provided in Annex A. Examples of value and quality factors are provided in Annex A.

> **注**：因素分解的示例见附录 A。价值因素和质量因素的示例见附录 A。

#### 4.7 Customized architecture evaluation frameworks 定制的架构评估框架

A generic AE framework is specified in this document that can be used in support of the Architecture Evaluation process defined in ISO/IEC/IEEE 42020. Specific frameworks can be derived from this generic framework. This clause describes the basic concepts regarding instantiation of specific AE frameworks while Clause 7 specifies provisions for instantiated specific AE frameworks.

本文件规定了一个通用 AE 框架，可用于支持 ISO/IEC/IEEE 42020 中定义的架构评估过程。特定框架能由该通用框架导出。本条描述有关特定 AE 框架实例化的基本概念，而第 7 章规定对已实例化的特定 AE 框架的各项条款。

The generic framework as illustrated by Figure 1 provides the elements and work products which could be instantiated or derived in specific frameworks. These specific frameworks may range from those targeting industry segments, like automotive or refinery operations, to those targeting common business processes, like portfolio management and program planning, and to those targeting common business architectures, like banking, retail, insurance, telecom, travel and hospitality, and so on. These frameworks allow the user to capture and reuse concepts common to many enterprises and thereby to increase the efficiency with which architectures can be evaluated.

图 1 所示的通用框架提供了可在特定框架中实例化或导出的元素和工作产品。这些特定框架的范围，可从面向行业细分领域（如汽车或炼油运营）的框架，到面向通用业务流程（如项目组合管理和项目规划）的框架，再到面向通用业务架构（如银行、零售、保险、电信、旅游与酒店等）的框架。这些框架使用户能捕获并复用众多企业共有的概念，从而提高架构评估的效率。

Instantiation of specific frameworks will need adaptation to the requirements of the specific situation where an AE effort will be performed. The specific framework is usually defined or developed with respect to the processes, methods and tools used in the local context.

特定框架的实例化需要适应将要开展 AE 工作的特定情况的要求。特定框架通常针对本地语境中所用的过程、方法和工具来定义或开发。

A specific AE framework provides a structure for reuse and evolution according to the evaluation needs. It may specify standardized practices for doing architecture evaluations. It can be used for:

特定 AE 框架提供了一种结构，用于按评估需求进行复用和演进。它可规定开展架构评估的标准化实践。它能用于：

- addressing specific evaluation objectives;

- 处理特定的评估目标；

- evaluating certain kinds of concerns of stakeholders;

- 评估利益相关方的某些类关注点；

- addressing specific value assessment objectives; or

- 处理特定的价值评定目标；或

- addressing specific architectural analysis objectives.

- 处理特定的架构分析目标。

A specific AE framework can instantiate or derive one or more tiers of the generic AE framework. In particular, it instantiates or derives one of the following:

特定 AE 框架能实例化或导出通用 AE 框架的一个或多个层级。具体而言，它实例化或导出下列之一：

- evaluation approach(es);

- 评估途径；

- assessment method(s); or

- 评定方法；或

- analysis method(s).

- 分析方法。

> **NOTE** The ATAM is an example of a specific AE framework that includes an evaluation approach based on the use of quality attribute workshops, and that specifies value assessment and analysis methods to be used. A summary description of ATAM is provided in Annex D.

> **注**：ATAM 是特定 AE 框架的一个示例，它包含一种基于质量属性研讨会运用的评估途径，并规定了所要使用的价值评定方法和分析方法。ATAM 的概述见附录 D。

A specific AE framework may include:

特定 AE 框架可包括：

- corresponding objectives and factors;

- 相应的目标与因素；

- expected roles and responsibilities of evaluators;

- 评估者的预期角色与职责；

- expected roles and responsibilities of stakeholders;

- 利益相关方的预期角色与职责；

- conditions of applicability and guidance on proper utilization; and

- 适用条件与恰当使用的指南；以及

- standardized format for evaluation results.

- 评估结果的标准化格式。

Communicating stakeholder perspectives requires clear semantics and terminology. The framework can include vocabulary, conventions, principles, practices, and applicable standards and regulatory requirements for evaluating architectures that can be generic in nature or specific to a domain of application, a collection of concerns to be examined or a particular methodology. The methods aggregated into a framework can share a common vocabulary, address similar concerns or be used together for other theoretical or practical considerations.

传达利益相关方角度需要清晰的语义和术语。框架可包括用于评估架构的词汇、约定、原则、实践以及适用的标准和监管要求，这些内容在性质上能是通用的，也能特定于某一应用领域、待审查的一组关注点或某一特定方法学。聚集到框架中的各种方法能共享共同词汇、处理相似的关注点，或出于其他理论或实践考虑而一起使用。

An AE approach can be developed afresh each time an evaluation is needed, or the constructs of the generic AE framework in this document can be used as the starting point and tailored for its particular use - either by way of specialization for a particular domain or with respect to concerns that are most relevant to the AE objectives.

每当需要开展评估时，AE 途径都能重新开发；也可将本文件中通用 AE 框架的各项构造用作起点，并针对其特定用途加以裁剪，其方式既可以是针对某一特定领域作专门化，也可以是就与 AE 目标最为相关的关注点作裁剪。

#### 4.8 Tailoring 裁剪

Tailoring may entail the addition, changing or removal of AE elements from the generic AE framework specified in this document. It may be performed for many reasons including the scale of the AE effort, the purpose of the evaluation, the intended uses of the AE results and the evaluation methodologies that will be employed. For example, if the purpose of the AE effort is to evaluate an architecture from an extant system or system design (i.e. to employ reverse architecting) then certain elements, such as architectural analysis, may not need to be performed.

裁剪可能涉及对本文件所规定通用 AE 框架中的 AE 要素加以增加、变更或删除。进行裁剪可能出于多种原因，包括 AE 工作的规模、评估的目的、AE 结果的预期用途以及将要采用的评估方法学。例如，若 AE 工作的目的是评估来自现有系统或系统设计的架构（即采用逆向架构工作），则某些要素（如架构分析）可能无需开展。

In all cases where such tailoring of AE elements is employed, the rationale behind the tailoring shall be recorded. Recording the rationale will assist stakeholders in determining the value arising from the AE effort and the confidence they should attribute to its outcomes.

在采用此类 AE 要素裁剪的所有情形下，均应记录裁剪背后的理由。记录理由将有助于利益相关方确定 AE 工作所产生的价值，以及他们宜赋予其结果的置信度。

Tailoring may diminish the perceived value of a claim of conformance to this document. This is because it is difficult for other organizations to understand the extent to which tailoring may have removed desirable provisions. An organization asserting a single-party claim of conformance to this document may find it advantageous to claim full conformance to a smaller set of AE elements rather than tailored conformance to a larger set of AE elements.

裁剪可能降低对本文件符合性声明的可感知价值。这是因为其他组织难以了解裁剪可能已在多大程度上删除所期望的条款。主张本文件单方符合性声明的组织可能发现，与对较大一组 AE 要素声称裁剪后符合相比，对较小一组 AE 要素声称完全符合更为有利。

The AE elements described in this document are not intended to preclude or discourage the use of additional AE elements that organizations find useful. In particular, governance and directives of the organization will be applied for tailoring of the AE elements.

本文件所述 AE 要素无意排除或阻碍组织使用其认为有用的其他 AE 要素。特别是，组织的治理与指令将适用于 AE 要素的裁剪。

### 5 Conformance 符合性

#### 5.1 General 总则

The requirements in this document are contained in Clauses 6 to 8. Situations in which claims of conformance with the provisions of this document can be made include those in 5.2 and 5.3.

本文件中的要求载于第 6 章至第 8 章。可作出对本文件条款符合性声明的情形，包括 5.2 和 5.3 中所述的情形。

> **NOTE** An organization can have its own set of requirements or directives with respect to following the provisions of this document. For example, compliance can be limited to a set of architecture evaluation elements (objectives, approaches, factors and/or results) or work products (plan and/or report). This allows the architecture evaluation effort to be aligned and consistent with other efforts within the organizations of either those requesting evaluation to be done or those doing the evaluation.

> **注**：一个组织能就遵循本文件条款一事拥有自己的一套要求或指令。例如，合规可限于一组架构评估要素（目标、途径、因素和／或结果）或工作产品（计划和／或报告）。这使架构评估工作得以与请求开展评估的组织或执行评估的组织内部的其他工作保持对齐与一致。

> **EXAMPLE** Specification of conformance for architecture evaluation objectives and results can be a way to establish contracts for the architecture evaluation efforts with freedom for the organization in charge of the architecture evaluation execution.

> **示例**：对架构评估目标与结果作出符合性规格，能成为为架构评估工作订立合同的一种方式，同时为负责架构评估实施的组织留出自由。

#### 5.2 Creating AE artifacts 创建 AE 人工制品

Claims of conformance with the provisions of this document can be made in the following situations:

在下列情形下可作出对本文件条款的符合性声明：

- When conformance is claimed for a customized architecture evaluation framework, the claim shall demonstrate that the architecture evaluation framework meets the requirements specified in Clause 7.

- 当对定制的架构评估框架声称符合性时，该声明应证明该架构评估框架满足第 7 章规定的要求。

- When conformance is claimed for an architecture evaluation plan, the claim shall demonstrate that the requirements specified in 8.1 and 8.2 are met.

- 当对架构评估计划声称符合性时，该声明应证明 8.1 和 8.2 中规定的要求得到满足。

- When conformance is claimed for an architecture evaluation report, the claim shall demonstrate that the requirements specified in 8.1 and 8.3 are met.

- 当对架构评估报告声称符合性时，该声明应证明 8.1 和 8.3 中规定的要求得到满足。

#### 5.3 Using generic AE framework to conduct AE efforts 使用通用 AE 框架开展 AE 工作

Claims of conformance with the provisions of this document can be made in the following situations:

在下列情形下可作出对本文件条款的符合性声明：

a) When conformance is claimed for an evaluation synthesis effort, the claim shall demonstrate that the evaluation approach used meets the requirements specified in 6.1.

a) 当对评估综合工作声称符合性时，该声明应证明所用的评估途径满足 6.1 中规定的要求。

> **NOTE 1** Evaluation synthesis is the effort conducted using the elements in the Evaluation Synthesis Tier of the generic AE framework specified in this document. It involves the combination of results from multiple value assessments to determine to what extent the evaluation objectives will be achieved. See 4.3.1 for more information on this concept.

> **注 1**：评估综合是使用本文件所规定通用 AE 框架中评估综合层级的要素所开展的工作。它涉及对多项价值评定的结果加以组合，以确定评估目标将在多大程度上得以实现。关于此概念的更多信息，见 4.3.1。

b) When conformance is claimed for a value assessment effort, the claim shall demonstrate that the assessment method used meets the requirements specified in 6.2.

b) 当对价值评定工作声称符合性时，该声明应证明所用的评定方法满足 6.2 中规定的要求。

> **NOTE 2** Value assessment is the effort conducted using the elements in the Value Assessment Tier of the generic AE framework specified in this document. It is concerned with a determination of the regard that something is held to deserve, or the importance, worth or usefulness of something to somebody. See 4.3.2 for more information on this concept. A comparison between the concepts of assessment and analysis is provided in 4.5.

> **注 2**：价值评定是使用本文件所规定通用 AE 框架中价值评定层级的要素所开展的工作。它关注的是确定某事物被认为应得的重视程度，或某事物对某人而言的重要性、价值或有用性。关于此概念的更多信息，见 4.3.2。评定与分析这两个概念之间的比较见 4.5。

c) When conformance is claimed for an architectural analysis effort, the claim shall demonstrate that the analysis method used meets the requirements specified in 6.3.

c) 当对架构分析工作声称符合性时，该声明应证明所用的分析方法满足 6.3 中规定的要求。

> **NOTE 3** Architectural analysis is the effort conducted using the elements in the Architectural Analysis Tier of the generic AE framework specified in this document. It is concerned with an examination of the key attributes of an architecture, e.g. its characteristics along particular dimensions such as security, cost, performance, and so on, or the relevant attributes of the architecture entity, as well as actual or potential impacts on stakeholders or on the environment. See 4.3.3 for more information on this concept. A comparison between the concepts of assessment and analysis is provided in 4.5.

> **注 3**：架构分析是使用本文件所规定通用 AE 框架中架构分析层级的要素所开展的工作。它关注的是对架构关键属性的考察，例如架构在信息安全、成本、性能等特定维度上的特性，或架构实体的相关属性，以及架构对利益相关方或环境造成的实际或潜在影响。关于此概念的更多信息，见 4.3.3。评定与分析这两个概念之间的比较见 4.5。

d) When conformance is claimed for an architecture evaluation effort, the claim shall demonstrate that the requirements specified in Clauses 7 and 8 are met.

d) 当对架构评估工作声称符合性时，该声明应证明第 7 章和第 8 章中规定的要求得到满足。

> **NOTE 4** Architectural evaluation is concerned with a judgment about one or more architectures with respect to the specified evaluation objectives. See 4.2 for more information on this concept.

> **注 4**：架构评估关注的是针对规定的评估目标，对一个或多个架构作出判断。关于此概念的更多信息，见 4.2。

#### 5.4 Verbal forms for the expression of provisions 表述条款的动词形式

Requirements of this document are marked by the use of the verb “shall”. Recommendations are marked by the use of the verb “should”. Permissions are marked by the use of the verb “may”. In the event of a conflict between normative figures and text, the text shall take precedence.

本文件的要求通过使用动词“shall”来标示。建议通过使用动词“should”来标示。许可通过使用动词“may”来标示。若规范性图与文本之间出现冲突，应以文本为准。

### 6 Architecture evaluation framework elements 架构评估框架要素

#### 6.1 Evaluation synthesis 评估综合

##### 6.1.1 General requirements 一般要求

> **NOTE 1** Figure 3 depicts AE elements that can be used in an evaluation synthesis effort in terms of the key concepts and the relations between them. Most of these concepts are also used in related standards described in Annex B.

> **注 1**：图 3 按关键概念及其相互关系，描绘了可在评估综合工作中使用的 AE 要素。这些概念大多也用于附录 B 所述的相关标准。

An architecture evaluation includes the following elements as specified in the subsequent subclauses:

架构评估按后续各分条的规定包括下列要素：

a) one or more AE objectives;

a) 一个或多个 AE 目标；

b) one or more AE approaches;

b) 一个或多个 AE 途径；

c) one or more AE factors; and d) one or more AE results.

c) 一个或多个 AE 因素；以及d) 一个或多个 AE 结果。

The AE effort shall:

AE 工作应：

- identify one or more AE approaches to address the AE objectives;

- 识别一个或多个 AE 途径以处理 AE 目标；

- address the relevant AE factors;

- 处理相关 AE 因素；

- produce the appropriate AE results;

- 产生适当的 AE 结果；

- determine the extent to which the AE objectives are met;

- 确定 AE 目标得以满足的程度；

- address relevant concerns;

- 处理相关关注点；

- address relevant business drivers and mission drivers;

- 处理相关业务驱动因素与使命驱动因素；

- determine the value of the architecture; and

- 确定架构的价值；以及

- produce one or more AE reports.

- 产出一份或多份 AE 报告。

The AE effort shall examine the AE results to determine the extent to which the AE objectives have been met. The AE effort may need to integrate and examine the AE results coming from multiple AE approaches used in the evaluation.

AE 工作应检查 AE 结果，以确定 AE 目标得以满足的程度。AE 工作可能需要综合并检查来自评估中所用多种 AE 途径的 AE 结果。

The AE effort may determine the value of architecture entities associated with the architecture under evaluation.

AE 工作可确定与所受评估的架构相关联的架构实体的价值。

The AE effort may specify the value assessment objectives that will satisfy the specified AE objectives. The AE effort may specify how to integrate AE results into the architecture description, when there is one.

AE 工作可规定将满足所规定的 AE 目标的价值评定目标。当存在架构描述时，AE 工作可规定如何将 AE 结果集成到架构描述中。

> **NOTE 2** While it is desirable to have a documented architecture description for use in the architecture evaluation, producing a description is sometimes not feasible with resources available, or it could be unnecessary if the architecture is based on widely accepted solutions in the domain. This document does not mandate the use of an explicit architecture description, but this document does encourage documentation of evidence collected in support of the architecture evaluation, including any understanding of the architecture obtained through various mechanisms, either generated during the evaluation or used in the evaluation.

> **注 2**：尽管为在架构评估中使用而具备一份形成文档的架构描述是可取的，但在可用资源条件下编制一份描述有时并不可行；若该架构以本领域中被广泛接受的解决方案为基础，则也可能并无必要。本文件不强制要求使用显式的架构描述，但本文件确实鼓励将所收集的、用以支持架构评估的证据形成文档，包括通过各种机制所获得的关于架构的任何理解，无论这些理解是评估期间生成的还是在评估中使用的。

Evaluation approaches, assessment methods and analysis methods may identify factors not previously associated with a stakeholder concern or architecture feature which are nonetheless determined to be a critical factor with respect to having the architecture entity be fit-for-purpose. When identified, the relevant reports should specify the newly identified factors with recommendations for the elaboration of value assessment factors, architecture evaluation factors, concern definition and stakeholder identification sufficient to address the newly identified criticality.

评估途径、评定方法和分析方法可识别出先前未与某一利益相关方关注点或架构特征相关联、但经判定对于使架构实体适于用途而言仍是关键因素的因素。一经识别，相关报告宜规定新识别出的因素，并随附建议，以细化价值评定因素、架构评估因素、关注点定义与利益相关方识别，使其足以处理新识别出的关键性。

##### 6.1.2 Architecture evaluation objectives 架构评估目标

Each AE objective shall:

每项 AE 目标应：

a) address one or more stakeholder concerns;

a) 处理一个或多个利益相关方关注点；

b) address relevant business drivers and mission drivers;

b) 处理相关的业务驱动因素与使命驱动因素；

c) be expressed in terms of AE factors; and d) be expressed in terms of expected or desired values or value range for the AE factors, when applicable.

c) 按 AE 因素予以表述；以及d) 在适用时，按 AE 因素的预期值或期望值或者值域予以表述。

> **EXAMPLE** Examples of AE objectives are:

> **示例**：AE 目标的示例包括：

- Will the business solution meet primary business needs?

- 业务解决方案能否满足主要业务需求？

- Is the system affordable?

- 系统是否可负担？

- Will the service be dependable?

- 服务是否可信赖？

- Will the product have sufficient market penetration?

- 产品能否具有充分的市场渗透率？

Each AE objective shall be a statement describing the extent to which the AE effort will address one or more of the relevant stakeholder concerns, such that they can form the basis for deriving value assessment objectives.

每项 AE 目标应是一份陈述，描述 AE 工作将处理一个或多个相关利益相关方关注点的程度，从而能构成推导价值评定目标的基础。

The AE objectives should be compatible with the established purpose and scope for the AE effort. The AE objectives may be expressed as questions to facilitate understanding of their intent.

AE 目标宜与为 AE 工作所确立的目的和范围相兼容。AE 目标可表述为问题，以便于理解其意图。

> **NOTE** The reason for expressing the questions in such a manner and with sufficient elaboration is to ensure better understanding of the objectives by the assessors and stakeholders..

> **注**：以此种方式并作充分阐述来表述这些问题，其原因在于确保评定者与利益相关方更好地理解各项目标。

##### 6.1.3 Architecture evaluation approaches 架构评估途径

Each AE approach shall provide the means to:

每种 AE 途径应提供以下手段：

a) identify AE objectives to be addressed;

a) 识别所要处理的 AE 目标；

b) specify AE factors to be used and AE criteria to be applied;

b) 规定所要使用的 AE 因素和所要施加的 AE 准则；

c) specify one or more value assessment objectives, aligning them to the AE objectives;

c) 规定一个或多个价值评定目标，并将其与 AE 目标对齐；

d) specify one or more assessment methods to address the value assessment objectives;

d) 规定一个或多个评定方法，以处理价值评定目标；

e) specify the value assessment factors to be used, aligning them to relevant stakeholder concerns; f) specify value assessment criteria to be applied;

e) 规定所要使用的价值评定因素，并将其与相关利益相关方关注点对齐；f) 规定所要施加的价值评定准则；

g) specify the type and form of value assessment results to be examined when executing the AE approach;

g) 规定在执行 AE 途径时所检查的价值评定结果的类型与形式；

h) specify how and when the identified assessment methods will be employed;

h) 规定所识别的评定方法将如何及何时被采用；

i) specify the mechanisms through which the AE criteria will be applied on AE factors; and j) generate the AE results.

i) 规定将 AE 准则施加于 AE 因素的机制；以及j) 生成 AE 结果。

Each AE approach should provide the means to:

每种 AE 途径宜提供以下手段：

k) examine the value assessment results to determine the extent to which the stakeholder concerns have been addressed;

k) 检查价值评定结果，以确定相关利益相关方关注点得到处理的程度；

l) examine the value assessment results to determine the extent to which the value assessment objectives have been met;

l) 检查价值评定结果，以确定价值评定目标得到满足的程度；

m) identify and characterize trade-offs between competing stakeholder concerns; and n) formulate findings and recommendations to be included in the AE results.

m) 识别并表征相互竞争的利益相关方关注点之间的权衡；以及n) 形成将纳入 AE 结果的发现与建议。

An AE approach may be specified as an AE framework for reuse in multiple architecture evaluations. The AE framework specification should be in accordance with Clause 7.

AE 途径可规定为 AE 框架，以供在多项架构评估中复用。AE 框架规格宜符合第 7 章。

> **EXAMPLE** The ATAM is an example of a published AE framework. ATAM is described in Annex D.

> **示例**：ATAM 是已发布的 AE 框架的一个示例。附录 D 描述了 ATAM。

##### 6.1.4 Architecture evaluation factors 架构评估因素

Each AE factor used in the AE approach shall:

AE 途径中所用的每个 AE 因素应：

a) be representative of one or more stakeholder concerns;

a) 代表一个或多个利益相关方关注点；

b) be in a normalized form suitable for comparison or integration with other factors;

b) 采取适合与其他因素比较或集成的规范化形式；

c) contribute to one or more AE objectives; and d) be usable by the AE approach to generate the AE results. EXAMPLE Examples of AE factors are: cost, schedule, performance, risk. Each AE factor should be specific and measurable.

c) 有助于实现一个或多个 AE 目标；以及d) 能由 AE 途径用于生成 AE 结果。AE 因素的示例包括：成本、进度、性能、风险。每个 AE 因素宜是特定的且可度量的。

Each AE factor should enable the AE effort to produce accurate, reliable and timely results.

每个 AE 因素宜使 AE 工作能够产生准确、可靠且及时的结果。

> **NOTE** The recommendations above are based on the general rule that good metrics are SMART – Specific, Measurable, Accurate, Reliable and Timely.

> **注**：以上建议基于良好度量指标是 SMART 这一通则——即特定（Specific）、可度量（Measurable）、准确（Accurate）、可靠（Reliable）且及时（Timely）。

##### 6.1.5 Architecture evaluation results 架构评估结果

Each AE result shall be traceable to inputs used, the AE criteria applied to derive it and the AE approach that applied the criteria.

每项 AE 结果应可追溯到所使用的输入、为推导该结果而施加的 AE 准则，以及施加该准则的 AE 途径。

Each AE result should:

每项 AE 结果宜：

a) be the outcome of an impartial and objective examination done as part of using the AE approach;

a) 是作为使用 AE 途径的一部分而进行的公正且客观的检查所得的结果；

b) document assumptions, risks and caveats to be taken into account while using the result; and c) include a statement of estimated uncertainty of the stated result.

b) 记录使用该结果时需考虑的假设、风险和限制性说明；以及c) 包括对所陈述结果之估计不确定度的说明。

Discrepancies between AE results from different AE approaches used should be explained.

不同 AE 途径所得 AE 结果之间的差异宜予以解释。

#### 6.2 Value assessment 价值评定

##### 6.2.1 General requirements 一般要求

> **NOTE 1** Figure 4 depicts the elements that can be used in a value assessment effort in terms of the key concepts and the relations between them. Value assessment objectives are intended to satisfy the AE objectives and frame the relevant stakeholder concerns. Value assessment factors will frame the relevant AE factors.

> **注 1**：图 4 按关键概念及概念之间的关系描绘了可用于价值评定工作的元素。价值评定目标旨在满足 AE 目标并框定相关利益相关方关注点。价值评定因素将框定相关 AE 因素。

> **NOTE 2** Information on the nature of value and how it relates to the concept of quality is provided in Annex A.

> **注 2**：关于价值的本质以及价值如何与质量概念相关联的信息，见附录 A。

Each value assessment includes the following elements as specified in the subsequent subclauses:

每项价值评定按后续各分条的规定包括下列要素：

a) one or more value assessment objectives;

a) 一个或多个价值评定目标；

b) one or more value assessment methods;

b) 一个或多个价值评定方法；

c) one or more value assessment factors, and d) one or more value assessment results.

c) 一个或多个价值评定因素；以及d) 一个或多个价值评定结果。

The value assessment effort shall examine the value assessment results to determine the extent to which the value assessment objectives have been met. The value assessment effort may need to integrate and examine the architectural analysis results coming from multiple architectural analysis methods used in the evaluation. The value assessment effort may need to explain discrepancies between architectural analysis results from different architectural analysis methods used.

价值评定工作应检查价值评定结果，以确定价值评定目标得到满足的程度。价值评定工作可能需要综合并检查来自评估中所用多种架构分析方法的架构分析结果。价值评定工作可能需要解释所用不同架构分析方法所得架构分析结果之间的差异。

Each value assessment effort shall:

每项价值评定工作应：

- specify value assessment objectives to address the relevant concerns;

- 规定价值评定目标，以处理相关关注点；

- identify one or more value assessment methods to address the value assessment objectives;

- 识别一个或多个价值评定方法，以处理价值评定目标；

- address the relevant value assessment factors;

- 处理相关的价值评定因素；

- address relevant concerns;

- 处理相关关注点；

- address relevant business drivers and mission drivers;

- 处理相关业务驱动因素和使命驱动因素；

- determine the extent to which the value assessment objectives are met; and

- 确定价值评定目标得到满足的程度；以及

- produce the appropriate value assessment results.

- 产生恰当的价值评定结果。

Each value assessment effort should be compatible with the established purpose and scope for the

每项价值评定工作宜与为 AE 工作确立的预期目的和范围相一致。

AE effort.

AE 工作。

Value assessment should determine the lineage from architecture artifacts to design, construction, and ultimately the products and services used to deliver value to stakeholders (note that there are no direct relationships between architecture and stakeholders).

价值评定宜确定从架构人工制品到设计、构建并最终到用于向利益相关方交付价值的产品和服务的谱系（注：架构与利益相关方之间没有直接关系）。

Each value assessment effort may specify the architectural analysis objectives that will satisfy the specified value assessment objectives.

每项价值评定工作可规定将满足所规定的价值评定目标的架构分析目标。

##### 6.2.2 Value assessment objectives 价值评定目标

Each value assessment objective shall be a statement describing the extent to which the value assessment effort will address one or more of the relevant stakeholder concerns, such that they can form the basis for deriving architectural analysis objectives.

每个价值评定目标应是一份陈述，描述该价值评定工作将处理一个或多个相关利益相关方关注点的程度，从而使其能够构成推导架构分析目标的基础。

The value assessment objectives may be expressed as questions to facilitate understanding of their intent.

价值评定目标可表述为问题，以便于理解其意图。

Each value assessment objective shall be expressible in terms of the kind of value a stakeholder expects to receive. Each value assessment objective shall include a qualitative description or quantitative extent of this expectation from use or operation of the architecture entity, or in its possession.

每个价值评定目标应能按利益相关方期望获得的价值种类予以表述。每个价值评定目标应包括对使用或运行该架构实体、或拥有该架构实体所产生此期望的定性描述或定量程度。

> **EXAMPLE 1** A qualitative description could state something like "profit should increase" while a quantitative extent could state something like "profit should increase by 50 % in 3 years”.

> **示例 1**：定性描述可表述为诸如“利润宜增长”，而定量的程度则可表述为诸如“利润宜在 3 年内增长 50 %”。

> **NOTE** Information on the nature of value and how it relates to the concept of quality is provided in Annex A.

> **注**：关于价值的本质以及价值如何与质量概念相关联的信息，见附录 A。

Each value assessment objective shall:

每个价值评定目标应：

a) satisfy one or more AE objectives;

a) 满足一个或多个 AE 目标；

b) be expressed in terms of value assessment factors; and c) be expressed in terms of expected or desired values or value range for the AE factors; and d) enable identification of the information necessary to assess achievement of the value assessment objective.

b) 按价值评定因素予以表述；以及c) 按 AE 因素的期望值或期望值域予以表述；以及d) 使识别评定该价值评定目标达成情况所需的信息成为可能。

> **EXAMPLE 2** Examples of value assessment objectives are:

> **示例 2**：价值评定目标的示例有：

- Will the business solution provide adequate productivity improvement?

- 业务方案能否提供足够的生产力提升？

- Does the system support level 5 trained personnel to control the factory process flow?

- 系统是否支持 5 级受训人员控制工厂流程？

- Will the service provide information in a timely manner?

- 服务能否以及时的方式提供信息？

- Will the product provide accurate and timely data?

- 产品能否提供准确而及时的数据？

##### 6.2.3 Value assessment methods 价值评定方法

Each value assessment method shall provide the means to:

每种价值评定方法应提供以下手段：

a) address assigned value assessment objectives;

a) 处理所分配的价值评定目标；

b) specify the value assessment factors to be used;

b) 规定所要使用的价值评定因素；

c) specify value assessment criteria to be applied;

c) 规定所要施加的价值评定准则；

d) specify the mechanisms through which the value assessment criteria will be applied on value assessment factors;

d) 规定将价值评定准则施加于价值评定因素的机制；

e) formulate findings and recommendations to be included in the value assessment results; and f) generate the value assessment results.

e) 形成将纳入价值评定结果的发现与建议；以及 f) 生成价值评定结果。

Each value assessment method should provide the means to:

每种价值评定方法宜提供以下手段：

— identify, if needed, one or more architectural analysis methods pertaining to the value assessment objectives it addresses;

— 在需要时，识别与其所处理的价值评定目标有关的一个或多个架构分析方法；

> **NOTE 1** Architectural analysis is optional since the information needed to generate value assessment results could already be available from other sources, hence removing the need to do analysis. The AE plan will indicate if and to what extent that architectural analysis is needed for a particular AE effort.

> **注 1**：架构分析是可选的，因为生成价值评定结果所需的信息可能已能从其他来源获得，从而无需进行分析。AE 计划将指明特定 AE 工作是否需要架构分析以及需要的程度。

- define architectural analysis objectives for the identified architectural analysis methods, derived from the value assessment objectives they address;

- 为所识别的架构分析方法定义架构分析目标，这些目标由其处理的价值评定目标推导而来；

- specify how and when the identified analysis methods will be employed;

- 规定所识别分析方法将如何及何时被采用；

> **NOTE 2** The mechanism for using the information produced by architectural analysis can include specific quantitative methods such as value-quality correlation mechanism, utility functions, statistical functions, constructed scale, objective functions, linear weighted sum, harmonic average or other integrative mechanisms. It can also include specific qualitative methods such as logical reasoning, grounded theory, matrix analysis, discourse analysis, characteristics typology, inductive reasoning or generalization.

> **注 2**：使用架构分析所产生信息的机制可包括特定的定量方法，如价值—质量关联机制、效用函数、统计函数、构造性标度、目标函数、线性加权和、调和平均或其他综合机制。它还可包括特定的定性方法，如逻辑推理、扎根理论、矩阵分析、话语分析、特征类型学、归纳推理或概括。

- determine the extent to which the architectural analysis objectives have been met;

- 确定架构分析目标得到满足的程度；

- determine completeness of coverage for the AE approach that employs it and the relevant value assessment objectives defined by that AE approach;

- 确定采用该方法的 AE 途径以及该 AE 途径所定义的相关价值评定目标的覆盖完整性；

- determine the extent to which relevant stakeholder concerns have been addressed; and

- 确定相关利益相关方关注点得到处理的程度；以及

- formulate findings and recommendations to be included in the value assessment results.

- 形成将纳入价值评定结果的发现与建议。

Value assessment methods may be specified as an AE framework for reuse in multiple architecture evaluations. The AE framework specification should be in accordance with Clause 7.

价值评定方法可规定为 AE 框架，以供在多项架构评估中复用。AE 框架规格宜符合第 7 章。

##### 6.2.4 Value assessment factors 价值评定因素

Each value assessment factor used in the value assessment method shall:

价值评定方法中所用的每个价值评定因素应：

a) be representative of one or more AE factors;

a) 代表一个或多个 AE 因素；

b) be in a normalized form suitable for comparison or integration with other factors;

b) 采取适合与其他因素比较或集成的规范化形式；

c) contribute to one or more value assessment objectives; and d) be usable by the value assessment method to generate the value assessment results. Each value assessment factor should be specific and measurable.

c) 有助于实现一个或多个价值评定目标；以及d) 能由价值评定方法用于生成价值评定结果。每个价值评定因素宜是特定的且可度量的。

Each value assessment factor should enable the value assessment effort to produce accurate, reliable and timely results.

每个价值评定因素宜使价值评定工作能够产生准确、可靠且及时的结果。

> **NOTE** The recommendations above are based on the general rule that good metrics are SMART – Specific, Measurable, Accurate, Reliable and Timely.

> **注**：以上建议基于良好度量指标是 SMART 这一通则——即特定（Specific）、可度量（Measurable）、准确（Accurate）、可靠（Reliable）且及时（Timely）。

##### 6.2.5 Value assessment results 价值评定结果

Each value assessment result shall be traceable to inputs used, the value assessment criteria applied to derive it and the assessment method that applied the criteria.

每项价值评定结果应可追溯到所使用的输入、为推导该结果而施加的价值评定准则，以及施加该准则的评定方法。

> **EXAMPLE** Examples of the kinds of value assessment results are things like customer satisfaction index, experience index, interaction quality index, communication experience index, quality of experience, safety index.

> **示例**：价值评定结果种类的示例有诸如客户满意度指数、体验指数、交互质量指数、沟通体验指数、体验质量、安全指数。

Each value assessment result should:

每项价值评定结果宜：

a) be the outcome of an impartial and objective assessment done as part of using a value assessment method;

a) 是作为使用价值评定方法的一部分而进行的公正且客观的评定所得的结果；

b) document assumptions, risks and caveats to be considered while using the result; and c) include a statement of estimated uncertainty of the stated result.

b) 记录使用该结果时需考虑的假设、风险和限制性说明；以及c) 包括对所陈述结果之估计不确定度的说明。

If there were any limitations of the method or in the scope considered while producing the value assessment results, this should be factored in while integrating the results into a holistic value assessment effort.

如果在产生价值评定结果时方法存在任何局限或所考虑的范围存在任何局限，则在将结果整合为整体价值评定工作时宜将这一点计入。

Discrepancies between architecture analysis results from different architectural analysis methods used should be explained.

不同架构分析方法所得架构分析结果之间的差异宜予以解释。

#### 6.3 Architectural analysis 架构分析

##### 6.3.1 General requirements 一般要求

> **NOTE 1** Figure 5 depicts the elements that can be used in an architectural analysis effort in terms of the key concepts and the relations between them. Analysis objectives are intended to satisfy the assessment objectives and frame the relevant stakeholder concerns. Analysis factors will frame the relevant assessment factors.

> **注 1**：图 5 按关键概念及概念之间的关系描绘了可用于架构分析工作的元素。分析目标旨在满足评定目标并框定相关利益相关方关注点。分析因素将框定相关评定因素。

> **NOTE 2** Architectural analysis is optional since the information needed to generate value assessment results could already be available from other sources, hence removing the need to do analysis. The AE plan will indicate if and to what extent that architectural analysis is needed for a particular AE effort.

> **注 2**：架构分析是可选的，因为生成价值评定结果所需的信息可能已能从其他来源获得，从而无需进行分析。AE 计划将指明特定 AE 工作是否需要架构分析以及需要的程度。

Each architectural analysis includes the following elements as specified in the subsequent sub clauses:

每项架构分析包括下列各元素，其规定见后续各分条款：

a) one or more architectural analysis objectives;

a) 一个或多个架构分析目标；

b) one or more architectural analysis methods;

b) 一个或多个架构分析方法；

c) one or more architectural analysis factors; and d) one or more architectural analysis results. Each architectural analysis effort shall:

c) 一个或多个架构分析因素；以及d) 一个或多个架构分析结果。每项架构分析工作应：

- specify architectural analysis objectives to address the relevant concerns;

- 规定架构分析目标，以处理相关关注点；

- identify one or more architectural analysis methods to address the architectural analysis objectives;

- 识别一个或多个架构分析方法，以处理这些架构分析目标；

- address the relevant architectural analysis factors;

- 处理相关架构分析因素；

- address relevant concerns;

- 处理相关关注点；

- address relevant business drivers and mission drivers;

- 处理相关业务驱动因素与使命驱动因素；

- determine the extent to which the architectural analysis objectives are met; and

- 确定架构分析目标得到满足的程度；以及

- produce the appropriate architectural analysis results.

- 产生恰当的架构分析结果。

Each architectural analysis effort should be compatible with the established purpose and scope for the

每项架构分析工作宜与既定的目的和范围相兼容，该目的和范围针对

AE effort.

AE 工作。

The architectural analysis effort shall examine the architectural analysis results to determine the extent to which the architectural analysis objectives have been met. The architectural analysis effort may need to integrate and examine the architectural analysis results coming from multiple architectural analysis methods used in the evaluation. The architectural analysis effort may need to explain discrepancies between architectural analysis results from different architectural analysis methods used.

架构分析工作应检查架构分析结果，以确定架构分析目标得到满足的程度。架构分析工作可能需要整合并检查来自评估中所用的多种架构分析方法的架构分析结果。架构分析工作可能需要解释所用不同架构分析方法所得架构分析结果之间的差异。

##### 6.3.2 Architectural analysis objectives 架构分析目标

Each architectural analysis objective shall be a statement describing the extent to which the architectural analysis effort will address one or more of the relevant stakeholder concerns, such that they can form the basis for performing the architectural analysis.

每个架构分析目标应是一份陈述，描述该架构分析工作将处理一个或多个相关利益相关方关注点的程度，从而使其能够构成执行架构分析的基础。

Each architectural analysis objective shall:

每个架构分析目标应：

a) satisfy one or more value assessment objectives;

a) 满足一个或多个价值评定目标；

b) be expressed in terms of expected or desired values or value range for the architectural analysis factors, when applicable; and c) enable identification of the information necessary to assess achievement of the architecture analysis objective.

b) 在适用时，按架构分析因素的期望值或期望值域予以表述；以及c) 使识别评定该架构分析目标达成情况所需的信息成为可能。

> **EXAMPLE** Examples of architectural analysis objectives are:

> **示例**：架构分析目标的示例有：

- Will the business solution have a positive return on investment exceeding the hurdle rate?

- 业务方案能否获得超过门槛收益率的正投资回报？

- Is the complexity of the system justified given its intended purpose?

- 鉴于系统的预期目的，系统的复杂性是否合理？

- Is the system producible in large enough quantities to meet the target price?

- 系统能否以足够大的产量生产，以满足目标价格？

- Is the system maintainable with the expected number of maintenance personnel and their skill levels?

- 在预期的维护人员数量及其技能水平下，系统是否可维护？

- Does the software application adequately handle cyber threats?

- 该软件应用能否充分应对网络威胁？

- Will the service provide enough bandwidth to meet expected user demand?

- 该服务能否提供足够的带宽以满足预期的用户需求？

- Will the product deliver data fast enough to meet its requirements?

- 该产品能否足够快地交付数据以满足其要求？

The architectural analysis objectives may be expressed as questions to facilitate understanding of their intent.

架构分析目标可表述为问题，以便于理解其意图。

##### 6.3.3 Architectural analysis methods 架构分析方法

Each architectural analysis method shall provide the means to:

每种架构分析方法应提供以下手段：

a) address assigned architectural analysis objectives;

a) 处理所分配的架构分析目标；

b) identify the relevant architecture attributes;

b) 识别相关架构属性；

c) specify architectural analysis factors to be used;

c) 规定所要使用的架构分析因素；

d) specify architectural analysis criteria to be applied; and e) generate the architectural analysis results.

d) 规定所要施加的架构分析准则；以及e) 生成架构分析结果。

Each architectural analysis method should provide the means to:

每种架构分析方法宜提供以下手段：

- specify the mechanisms through which the architectural analysis criteria will be applied on architectural analysis factors;

- 规定将架构分析准则施加于架构分析因素的机制；

- specify how and when particular analytical tools and techniques will be used;

- 规定特定分析工具与技术将如何及何时被使用；

- specify how and when particular measurement protocols will be used; and

- 规定特定测量协议将如何及何时被使用；以及

- determine quantitative or qualitative measurements or indicators for relevant architecture or architecture entity attributes;

- 确定相关架构属性或架构实体属性的定量或定性测量值或指标；

- examine architectural analysis factors to determine the extent to which the architectural analysis objectives have been met;

- 检查架构分析因素，以确定架构分析目标得到满足的程度；

- determine completeness of coverage for the value assessment method that employs it and the relevant architectural analysis objectives defined by that value assessment method;

- 确定采用该方法的评定方法以及该评定方法所定义的相关架构分析目标的覆盖完整性；

- determine the extent to which relevant stakeholder concerns have been addressed; and

- 确定相关利益相关方关注点得到处理的程度；以及

- formulate findings and recommendations to be included in the architectural analysis results.

- 形成将纳入架构分析结果的发现与建议。

Each architectural analysis method may provide the means to:

每种架构分析方法可提供以下手段：

- identify an architectural analysis factor not driven by a value assessment factor and thus lacking a related stakeholder concern, but which is nonetheless determined to be a critical factor with respect to having the architecture entity be fit-for-purpose; and

- 识别并非由价值评定因素驱动、因而不具有相关利益相关方关注点，但仍被确定为对于使架构实体切合用途而言属关键因素的架构分析因素；以及

- report the newly identified architectural analysis factor with recommendations for the elaboration of value assessment factors, architecture evaluation factors, concern definition and stakeholder identification sufficient to address the newly identified criticality.

- 报告新识别的架构分析因素，并随附对价值评定因素、架构评估因素、关注点定义和利益相关方识别加以细化的建议，这些建议足以处理新识别的关键性。

Architectural analysis methods may be specified as an AE framework for reuse in multiple architecture evaluations. The AE framework specification should be in accordance with Clause 7.

架构分析方法可规定为 AE 框架，以供在多项架构评估中复用。AE 框架规格宜符合第 7 章。

##### 6.3.4 Architectural analysis factors 架构分析因素

Each architectural analysis factor used in the analysis method shall:

分析方法中所用的每个架构分析因素应：

a) be representative of one or more value assessment factors;

a) 代表一个或多个价值评定因素；

b) be in a normalized form suitable for comparison or integration with other factors;

b) 采取适合与其他因素比较或集成的规范化形式；

c) contribute to one or more architectural analysis objectives; and d) be usable by the analysis method to generate the architectural analysis results. Each architectural analysis factor should be specific and measurable.

c) 有助于实现一个或多个架构分析目标；以及d) 能由分析方法用于生成架构分析结果。每个架构分析因素宜是特定的且可度量的。

Each architectural analysis factor should enable the architectural analysis effort to produce accurate, reliable and timely results.

每个架构分析因素宜使架构分析工作能够产生准确、可靠且及时的结果。

> **NOTE** The recommendations above are based on the general rule that good metrics are SMART – Specific, Measurable, Accurate, Reliable and Timely.

> **注**：以上建议基于良好度量指标是 SMART 这一通则——即特定（Specific）、可度量（Measurable）、准确（Accurate）、可靠（Reliable）且及时（Timely）。

##### 6.3.5 Architectural analysis results 架构分析结果

Each architectural analysis result shall be traceable to inputs used, architectural analysis factors and architectural analysis criteria used to derive it and the analysis method that applied the criteria.

每项架构分析结果应可追溯到所使用的输入、为推导该结果而使用的架构分析因素与架构分析准则，以及施加该准则的分析方法。

> **EXAMPLE** Examples of architectural analysis results are readiness level, availability level, response time, safety level, reliability level, foot print, resource utilization.

> **示例**：架构分析结果的示例有就绪等级、可用性等级、响应时间、安全等级、可靠性等级、占用空间、资源利用率。

Each architectural analysis result should:

每项架构分析结果宜：

a) be the outcome of an impartial and objective analysis done as part of using an analysis method;

a) 是作为使用分析方法的一部分而进行的公正且客观的分析所得的结果；

b) document assumptions, risks, and caveats to be considered while using the result;, and c) include a statement of estimated uncertainty of the stated result. Analysis results should be documented and retained for future reference.

b) 记录使用该结果时需考虑的假设、风险和限制性说明；以及c) 包括对所陈述结果之估计不确定度的说明。分析结果宜予以记录并保留，以供未来参考。

If there were any limitations of the method or in the scope considered while producing the architectural analysis results, this should be factored in while integrating the results into a holistic architectural analysis effort.

如果在产生架构分析结果时方法存在任何局限，或所考虑的范围存在任何局限，则在将结果整合为整体架构分析工作时宜将这一点计入。

Discrepancies between architecture analysis results from different architectural analysis methods used should be explained.

所用不同架构分析方法所得架构分析结果之间的差异宜予以解释。

### 7 Customized architecture evaluation frameworks 定制的架构评估框架

#### 7.1 General requirements 一般要求

> **NOTE 1** To reduce the work involved in generating the information required in an AE effort, and recognizing that the approaches and methods are typically knowledge elements that are reused across applicable contexts, this document defines the concept of a generic AE framework that can be used to derive specific frameworks relevant for AE objectives and sustaining the needed AE effort.

> **注 1**：为减少生成 AE 工作所需信息所涉及的工作，并考虑到各种途径与方法通常是在各适用语境中复用的知识元素，本文件定义了通用 AE 框架这一概念；该框架可用于推导与 AE 目标相关并能支撑所需 AE 工作的特定框架。

> **NOTE 2** Tailoring is not to be confused with the development of a customized AE framework. Tailoring (as described in 4.8) is taking some things from the standard and adopting it for conformance. On the other hand, customization is deriving a specific version of the AE framework that is applicable to a particular organization or situation.

> **注 2**：裁剪不应与定制 AE 框架的开发相混淆。裁剪（如 4.8 所述）是从本标准中选取某些内容并将之采纳用于符合性。而定制则是导出适用于特定组织或特定情况的特定版本 AE 框架。

A customized AE framework shall include:

定制 AE 框架应包括：

a) information identifying the framework (e.g. name, identification code, version number);

a) 标识该框架的信息（例如名称、标识代码、版本号）；

b) information identifying the intended uses and users;

b) 标识预期用途与使用者的信息；

c) information identifying the roles and responsibilities of stakeholders;

c) 标识利益相关方角色与职责的信息；

d) AE plan outline of required and optional content;

d) AE 计划中必需内容与可选内容的大纲；

e) AE report outline of required and optional content; and f) conditions of applicability.

e) AE 报告中必需内容与可选内容的大纲；以及 f) 适用条件。

> **EXAMPLE** The following are example conditions of applicability:

> **示例**：下列为适用条件的示例：

- The AE framework is applicable where an architecture entity involves planning safety for manned vs unmanned transportation activities.

- 当架构实体涉及有人与无人运输活动的安全规划时，该 AE 框架适用。

- The AE framework is applicable during the pre-concept phase of major acquisition programs.

- 该 AE 框架适用于重大获取项目的概念前阶段。

- The AE framework is applicable when the evaluation is for an architecture entity that is very small and can be implemented in less than a month.

- 当评估针对的架构实体规模很小、能在一个月内实现时，该 AE 框架适用。

A customized AE framework should provide a completed, populated customizable model of an AE effort or some aspect of it. The customized AE framework should state how an AE effort should be done and what information should be captured.

定制 AE 框架宜提供 AE 工作或其某些方面的完整、已填充的可定制模型。定制 AE 框架宜说明 AE 工作宜如何开展以及宜捕获哪些信息。

A customized AE framework should include:

定制 AE 框架宜包括：

- questions that can be answered using the specified approaches and methods;

- 能使用所规定的途径和方法予以回答的问题；

- identification of one or more stakeholder concerns framed by the framework;

- 对由该框架所框定的一个或多个利益相关方关注点的标识；

- correlation of concerns to specific stakeholders to express the context of each concern;

- 关注点与特定利益相关方的关联，以表达每个关注点的语境；

- assignment of a priority for each concern (e.g. High, Medium, Low);

- 为每个关注点指派优先级（例如高、中、低）；

- identification of associated compliance document(s) to help assess risk of non-compliance;

- 对相关符合性文件的标识，以帮助评定不符合的风险；

- specify the form and format of the informational inputs needed by the method;

- 规定该方法所需信息输入的形式与格式；

- include a mechanism for estimating time for:

- 包含用于估算下列事项所需时间的机制：

e.1) preparation and training of resources, e.2) conducting the evaluation, and e.3) post-evaluation analysis and documentation;

e.1) 资源的准备与培训，e.2) 评估的实施，以及e.3) 评估后的分析与文档编制；

- identify the form and/or format for expressing method outputs as the results; and

- 标识将方法输出表述为结果的形式和／或格式；以及

— provide a mechanism for correlating the inputs used and the criteria to be applied to each result produced.

— 提供一种机制，用于关联所使用的输入与即将施加到每个所产生的结果上的准则。

A customized AE framework should include adaptation guidelines if adaptation is allowed. The AE framework should enable specialization of the objectives, factors and criteria of its elements based on the objectives for which an architecture evaluation is sought.

若允许适配，定制 AE 框架宜包含适配指南。该 AE 框架宜使其各元素的目标、因素和准则能基于所寻求的架构评估目标而专门化。

A customized AE framework should enable adaptation for use with respect to the business and operational domain of the architecture entity of interest, evaluation purpose and scope, lifecycle stage of the architecture or architecture entity, and resources available for the evaluation effort.

定制 AE 框架宜使其能针对所关注架构实体的业务域与运行域、评估目的与范围、架构或架构实体的生存周期阶段，以及可用于该评估工作的资源进行适配。

A customized AE framework may include:

定制 AE 框架可包括：

- sample of an AE plan;

- AE 计划的样例；

- sample of an AE report;

- AE 报告的样例；

- sample of an implementation of an evaluation synthesis approach;

- 评估综合途径实现的样例；

- sample of an implementation of a value assessment method; and

- 价值评定方法实现的样例；以及

- sample of an implementation of an architectural analysis method.

- 架构分析方法实现的样例。

#### 7.2 Framework requirements for architecture evaluation 对架构评估的框架要求

The framework shall specify the characteristics of its evaluation elements in accordance with the requirements of 6.1. The framework may include specification of relevant assessment objectives in accordance with the requirements of 6.2. The framework may include specification of relevant analysis objectives in accordance with the requirements of 6.3.

框架应按照 6.1 的要求规定其评估元素的特性。框架可按照 6.2 的要求包含相关规定评定目标的内容。框架可按照 6.3 的要求包含相关规定分析目标的内容。

The framework may include AE objectives, factors and criteria.

框架可包括 AE 目标、因素和准则。

#### 7.3 Framework requirements for value assessment 对价值评定的框架要求

The framework shall specify the characteristics of its evaluation elements in accordance with the requirements of 6.2. The framework may include specification of relevant analysis objectives in accordance with the requirements of 6.3.

框架应按照 6.2 的要求规定其评估元素的特性。框架可按照 6.3 的要求包含相关规定分析目标的内容。

The framework may include value assessment objectives, factors and criteria.

框架可包括价值评定目标、因素和准则。

#### 7.4 Framework requirements for architectural analysis 对架构分析的框架要求

The framework shall specify the characteristics of its evaluation elements in accordance with the requirements of 6.3.

框架应按照 6.3 的要求规定其评估元素的特性。

The framework may include architectural analysis objectives, factors and criteria.

框架可包括架构分析目标、因素和准则。

#### 7.5 Framework requirements for architecture evaluation work products 对架构评估工作产品的框架要求

The framework shall specify the characteristics of AE work products in accordance with the requirements of Clause 8.

框架应按照第 8 章的要求规定 AE 工作产品的特性。

### 8 Architecture evaluation work products 架构评估工作产品

#### 8.1 General requirements 通用要求

The AE effort shall produce an AE plan (in accordance with the requirements in 6.2).

AE 工作应产生 AE 计划（按照 6.2 中的要求）。

A separate plan may be produced for each tier of the AE effort.

可为 AE 工作的每个层级分别产生一份计划。

> **NOTE** The activities in the Architecture Evaluation process specified in ISO/IEC/IEEE 42020 can be used as a guide when planning an AE effort. The planning activity specified in that AE process provides recommended tasks for planning an AE effort.

> **注**：ISO/IEC/IEEE 42020 中所规定的架构评估过程的活动，能在规划 AE 工作时用作指南。该 AE 过程中所规定的规划活动提供了用于规划 AE 工作的推荐任务。

The AE effort shall produce one or more AE reports (in accordance with the requirements in 6.3).

AE 工作应产生一份或多份 AE 报告（按照 6.3 中的要求）。

The AE report may include required items “by reference” by pointing to the AE plan, where appropriate. A separate report may be produced for each tier of the AE effort.

在适当情况下，AE 报告可通过指向 AE 计划而以“引用方式”包含所要求的项。可为 AE 工作的每个层级分别产生一份报告。

#### 8.2 Architecture evaluation plan 架构评估计划

##### 8.2.1 AE plan requirements AE 计划要求

The AE plan shall include:

AE 计划应包括：

a) purpose and scope of the AE effort;

a) AE 工作的目的与范围；

b) identification of previous related AE efforts;

b) 对以往相关 AE 工作的标识；

c) identification of architecture(s) to be evaluated;

c) 对拟评估架构的标识；

d) identification of architecture description(s) to be used, if applicable;

d) 对拟使用的架构描述的标识（如适用）；

e) identification of architectural principle(s) that were used to develop the architecture(s); f) identification of relevant stakeholders;

e) 对用于开发该架构的架构原则的标识；f) 对相关利益相关方的标识；

g) identification of driving stakeholder concerns to be addressed;

g) 对拟处理的驱动性利益相关方关注点的标识；

h) identification of relevant business drivers and mission drivers;

h) 对相关业务驱动因素和使命驱动因素的标识；

i) definition of AE objectives and their relative importance;

i) AE 目标及其相对重要性的定义；

j) identification of AE approaches to be employed;

j) 对拟采用的 AE 途径的标识；

k) identification of applicable constraints and conditions;

k) 对适用约束与条件的标识；

l) identification of resources required for the AE effort;

l) 对 AE 工作所需资源的标识；

m) identification of referenced data that needs to be archived and/or baselined;

m) 对需要归档和／或基线化的引用数据的标识；

n) identification of necessary information sources; and o) identification of relevant compliance documents, technical documentation, contract documentation, etc.

n) 对必要信息源的标识；以及o) 对相关符合性文件、技术文档、合同文档等的标识。

##### 8.2.2 AE plan recommendations AE 计划建议

The AE plan should include:

AE 计划宜包括：

a) definition of quality management procedures for the AE effort;

a) AE 工作的质量管理规程的定义；

b) definition of architecture governance procedures for the AE effort;

b) AE 工作的架构治理规程的定义；

c) specification of required precision and accuracy of the AE results;

c) AE 结果所要求的精密度与准确度的规定；

d) specification of the required form and content of needed inputs;

d) 所需输入所要求的形式与内容的规定；

e) specification of the required form and content of needed outputs; f) specification of the required form and content of the AE report;

e) 所需输出所要求的形式与内容的规定；f) AE 报告所要求的形式与内容的规定；

e.g) identification of risks and opportunities for the AE effort;

e.g) AE 工作的风险与机会的标识；

e.h) identification of opportunity pursuit plans for critical items among the identified opportunities; and e.i) identification of risk management plans for critical items among the identified risks.

e.h) 对所识别机会中的关键项的机遇追求计划的标识；以及e.i) 对所识别风险中的关键项的风险管理计划的标识。

The AE plan should provide the capability for the customer, requestor or sponsor, if applicable, to affix their approval.

AE 计划宜提供相应能力，使顾客、请求方或发起方（如适用）能签署其批准意见。

The AE plan should provide the capability for the approving authority, if applicable, to affix their approval.

AE 计划宜提供相应能力，使批准当局（如适用）能签署其批准意见。

The AE plan should include the recommended items from ISO/IEC/IEEE 15289:

AE 计划宜包括 ISO/IEC/IEEE 15289 中的推荐事项：

- date of issue and status;

- 发布日期和状态；

- issuing organization;

- 发布组织；

- references (applicable policies, laws, standards, contracts, requirements and other plans and procedures);

- 引用文件（适用的政策、法律、标准、合同、要求以及其他计划和规程）；

- approval authority;

- 批准机构；

- planned activities and tasks;

- 计划的活动与任务；

- identification of tools, methods and techniques;

- 工具、方法和技术的识别；

- schedules;

- 进度安排；

- budgets and cost estimates;

- 预算和成本估算；

- resources and their allocation, including human resources, technical resources (infrastructure) and tools;

- 资源及其分配，包括人力资源、技术资源（基础设施）和工具；

- responsibilities and authority, including the senior responsible owner and immediate process or service owner;

- 职责与权限，包括高级责任所有者和直接的过程或服务所有者；

- interfaces among parties involved;

- 各参与方之间的接口；

- risks and risk identification, assessment and mitigation activities;

- 风险以及风险识别、评定和缓解活动；

- quality assurance and performance measures;

- 质量保证和绩效测量；

- environment, infrastructure, security and safety;

- 环境、基础设施、信息安全和安全；

- training;

- 培训；

- approach for technical and management review and reporting;

- 技术和管理评审与报告的途径；

- other plans (plans or task descriptions that expand on the details of a plan);

- 其他计划（对某计划的细节予以展开的计划或任务描述）；

- glossary;

- 术语表；

- change procedures and history; and

- 更改规程和更改历史；以及

- termination process.

- 终止过程。

##### 8.2.3 AE plan permissions AE 计划许可事项

The AE plan may include:

AE 计划可包括：

a) identification of sponsor, if any;

a) 发起方的识别（如有）；

b) assumptions made in planning the AE effort;

b) 规划 AE 工作时所作的假设；

c) ground rules established in planning the AE effort;

c) 规划 AE 工作时所确立的基本规则；

d) work breakdown structure;

d) 工作分解结构；

e) definition of how the AE effort will be organized;

e) AE 工作组织方式的定义；

f) definition of timeframe for conducting the AE effort;

f) 开展 AE 工作的时间框架的定义；

g) identification of AE frameworks to be employed, if applicable;

g) 拟采用的 AE 框架的识别（如适用）；

h) identification of assessment methods to be employed;

h) 拟采用的评定方法的识别；

i) identification of the roles and responsibilities of stakeholders;

i) 利益相关方角色与职责的识别；

j) identification of the roles and responsibilities of evaluators;

j) 评估者角色与职责的识别；

k) identification of evaluator independence requirements, if applicable;

k) 评估者独立性要求的识别（如适用）；

l) identification of approval authority for the AE report;

l) AE 报告批准机构的识别；

m) definition of value assessment objectives, factors, metrics and criteria to be used;

m) 拟使用的价值评定目标、因素、度量和准则的定义；

n) identification of analysis methods to be employed, if applicable; and o) definition of architectural analysis objectives, factors and criteria to be used.

n) 拟采用的分析方法的识别（如适用）；以及o) 拟使用的架构分析目标、因素和准则的定义。

> **NOTE** The activities in the Architecture Evaluation process specified in ISO/IEC/IEEE 42020 can be used as a guide when planning an AE effort. The planning activity specified in that AE process provides recommended tasks for planning an AE effort.

> **注**：ISO/IEC/IEEE 42020 中规定的架构评估过程中的活动，能在规划 AE 工作时用作指南。该 AE 过程中所规定的规划活动，为规划 AE 工作提供了推荐任务。

#### 8.3 Architecture evaluation report 架构评估报告

##### 8.3.1 AE report requirements AE 报告要求

The AE report provides results of reviews and evaluations, such as a risk assessment, quality assurance evaluation or an evaluation of project portfolios, design constraints, candidate architectures, suppliers, customer satisfaction, effectiveness of security controls, analysis of change records or change requests, personnel needs, measurement needs or financial variances. It can include evaluation criteria. Evaluations can be based on criteria of traceability, consistency, testability, risk reduction, usability and customer satisfaction and feasibility.

AE 报告提供审查与评估的结果，例如风险评定、质量保证评估，或对项目组合、设计约束、候选架构、供应商、顾客满意程度、安全保密控制有效性、更改记录或更改请求的分析、人员需求、测量需求或财务偏差的评估。它能包括评估准则。评估能基于可追溯性、一致性、可测试性、风险降低、可用性和顾客满意程度以及可行性等准则。

The AE report provides information and recommendations to assist future decision-making, and it can indicate trends and recommendations for future comparable situations. For software configuration management evaluations, the report provides information about functional completeness of the software items against their requirements and the physical completeness of the software items (whether their design and code reflect an up-to-date technical description).

AE 报告提供信息和推荐，以辅助未来的决策，并能就未来类似情形指出趋势和推荐。对于软件配置管理评估，报告提供关于软件项相对于其需求的功能完备性以及软件项物理完备性（其设计和代码是否反映最新的技术描述）的信息。

Using the relevant AE plan contents where possible, each AE report shall include:

在可能的情况下利用 AE 计划的相关内容，每份 AE 报告应包括：

a) purpose and scope of the AE effort;

a) AE 工作的目的和范围；

b) identified issues, risks and opportunities;

b) 已识别的问题、风险和机会；

c) identified impacts on stakeholders;

c) 已识别的对利益相关方的影响；

d) definition of AE objectives addressed;

d) 所处理的 AE 目标的定义；

e) identification of stakeholder concerns addressed; f) identification of relevant stakeholders;

e) 所处理的利益相关方关注点的识别；f) 相关利益相关方的识别；

g) identification of architecture(s) that were evaluated;

g) 已评估的架构的识别；

h) identification of architecture description(s) that were used;

h) 已使用的架构描述的识别；

i) identification of resources used;

i) 已使用资源的识别；

j) definition of tailoring performed on the AE process for this AE effort;

j) 针对本次 AE 工作对 AE 过程所作裁剪的定义；

k) identification of AE frameworks employed, if any, with the rationale for their selection;

k) 已采用的 AE 框架（如有）的识别，及其选用理由；

l) identification of data used, collected or produced that needs to be archived or baselined;

l) 已使用、收集或产生的、需归档或基线化的数据的识别；

m) identification of information sources used in the AE effort; and n) identification of other resources used in the AE effort, including participating people and organizations;

m) AE 工作中所用信息源的识别；以及n) AE 工作中所用其他资源（包括参与人员和参与组织）的识别；

> **NOTE** The resources actually used during the architecture evaluation can differ from the planned resources.

> **注**：架构评估期间实际使用的资源能不同于计划的资源。

o) presentation of AE results;

o) AE 结果的呈现；

p) definition of evaluation synthesis objectives;

p) 评估综合目标的定义；

q) summary of overall results;

q) 总体结果的汇总；

r) recommended architecture(s), if multiple architecture were examined;

r) 所推荐的架构（若考察了多个架构）；

s) relevant observations and findings;

s) 相关观察结果和发现；

t) architecture trade-offs identified and examined;

t) 已识别并考察的架构权衡；

u) results from each of the AE approaches employed, mapped to the AE objectives they addressed; and v) traceability of the conclusions to the objectives of the evaluation.

u) 所采用的每种 AE 途径的结果，并映射到其所处理的 AE 目标；以及v) 结论对评估目标的可追溯性。

##### 8.3.2 AE report recommendations AE 报告建议

Each AE report should include:

每份 AE 报告宜包括：

a) proposed way forward, when applicable (e.g. recommended modifications to the architecture, additional evaluation or analysis needed, etc.);

a) 适用时拟议的前进路径（例如对架构的修改建议、所需的附加评估或分析等）；

b) derivation of final conclusions from the value assessment and architectural analysis results;

b) 由价值评定和架构分析结果得出最终结论的推导；

> **NOTE** In some domains such as safety critical systems it is often necessary to document the derivation of the conclusions all the way down to the analysis results.

> **注**：在某些领域（如安全关键系统）中，往往有必要将结论的推导过程一直记录到分析结果。

c) description of how each AE approach was implemented, along with sources of information used;

c) 对每种 AE 途径如何实施的描述，以及所用信息源；

d) sensitivity analysis on the results to help understand the impact of incomplete or inaccurate input data, etc.;

d) 对结果的敏感度分析，以帮助理解不完整或不准确的输入数据等的影响；

e) description of limitations of the AE effort;

e) AE 工作局限性的描述；

f) description of the extent to which the AE results are useful or valid;

f) AE 结果有用性或有效程度的描述；

g) recommendations on mitigating the identified issues and risks;

g) 关于缓解已识别问题和风险的建议；

h) traceability of concerns to specific stakeholders and to associated compliance documents;

h) 关注点对特定利益相关方及相关符合性文件的可追溯性；

i) assumptions made in execution of the AE effort;

i) 执行 AE 工作时所作的假设；

j) any significant deviations from the AE plan along with the reasons for those deviations;

j) 与 AE 计划的任何重大偏离及其原因；

k) identification of impacts due to planning assumptions found to be false;

k) 因发现规划假设不成立而产生的影响的识别；

l) archiving and repository requirements for the AE report; and m) lessons learned during the AE effort.

l) AE 报告的归档和存储库要求；以及m) AE 工作期间所汲取的教训。

The AE report should provide the capability for the customer, requestor or sponsor, if applicable, to affix their approval.

AE 报告宜提供使顾客、请求方或发起方（如适用）能够签署批准的能力。

The AE report should provide the capability for the approving authority, if applicable, to affix their approval.

AE 报告宜提供使批准机构（如适用）能够签署批准的能力。

If the evaluation identifies consequences of potential emergent properties of an architecture entity that are undesirable, then explicit actions to deal with them should be recommended. When these consequences are relatively obvious, evaluators should declare in the AE report any risks and potential unintended consequences, or incomplete consideration of potential emergent properties of an architecture entity, in order to provide the architects with an opportunity to mitigate those risks.

如果评估识别出架构实体的潜在涌现特性的非期望后果，则宜推荐应对这些后果的明确措施。当这些后果相对明显时，评估者宜在 AE 报告中声明任何风险以及潜在意外后果，或对架构实体潜在涌现特性考虑不周之处，以便为架构师提供缓解这些风险的机会。

In the course of the evaluation, if one or more assumptions made during planning or execution of the architecture evaluation have proven to be false, then evaluators delivering the AE results should use their knowledge and skills and make reasonable efforts to declare in the AE report any risks and potential unintended consequences of the false assumptions in order to provide the architects with an opportunity to mitigate those risks.

在评估过程中，如果在规划或执行架构评估期间所作的一项或多项假设被证明不成立，则交付 AE 结果的评估者宜运用其知识和技能，作出合理努力，在 AE 报告中声明这些不成立假设的任何风险和潜在意外后果，以便为架构师提供缓解这些风险的机会。

The AE report should document the provenance of all information items used in an AE. This facilitates answering of questions about the results, findings and recommendations of the evaluation.

AE 报告宜记录 AE 中所用全部信息部件的来源。这便于回答关于评估的结果、发现和建议的各种问题。

The AE report should include the recommended items from ISO/IEC/IEEE 15289:

AE 报告宜包括 ISO/IEC/IEEE 15289 中的推荐事项：

- date of issue and status,

- 发布日期和状态，

- issuing organization,

- 发布组织，

- contributors,

- 贡献者，

- summary,

- 摘要，

- context (assumptions),

- 语境（假设），

- body (including methods of obtaining results),

- 正文（包括获得结果的方法），

- conclusions and recommendations,

- 结论和建议，

- references,

- 引用文件，

- bibliography,

- 书目，

- glossary, and

- 术语表，以及

- change history.

- 更改历史。

##### 8.3.3 AE report permissions AE 报告许可事项

Each AE report may include:

每份 AE 报告可包括：

a) presentation of value assessment results;

a) 价值评定结果的呈现；

b) definition of value assessment objectives;

b) 价值评定目标的定义；

c) relevant observations and findings;

c) 相关观察结果和发现；

d) results from each of the assessment methods employed, mapped to the value assessment objectives they addressed;

d) 所采用的每种评定方法的结果，并映射到其所处理的价值评定目标；

e) description of how each value assessment was implemented, along with sources of information used;

e) 对每项价值评定如何实施的描述，以及所用信息源；

f) presentation of architectural analysis results;

f) 架构分析结果的呈现；

g) definition of architectural analysis objectives;

g) 架构分析目标的定义；

h) relevant observations and findings;

h) 相关观察结果和发现；

i) results from each of the analysis methods employed, mapped to the architectural analysis objectives they addressed; and j) description of how each architectural analysis was implemented, along with sources of information used.

i) 所采用的每种分析方法的结果，并映射到其所处理的架构分析目标；以及j) 对每项架构分析如何实施的描述，以及所用信息源。

k) implementation roadmap for the architecture;

k) 架构的实施路线图；

l) action plan for implementing the recommendations;

l) 实施各项建议的行动计划；

m) ground rules established in executing the AE effort;

m) 执行 AE 工作时所确立的基本规则；

n) responses from stakeholders, including architects, from their review of AE results;

n) 利益相关方（包括架构师）对 AE 结果进行评审后作出的回应；

o) comments received on preliminary drafts of observations and findings;

o) 就观察结果和发现的初稿所收到的意见；

p) recommendations with rationale based on findings of the AE effort; and q) additional findings and recommendations beyond the purpose and scope of the evaluation.

p) 基于 AE 工作的发现且附有理由的建议；以及q) 超出评估目的和范围的其他发现和建议。

Recommendations may be accompanied by implications, advantages and disadvantages, caveats or regrets associated with the recommendation.

建议可附有与该建议相关的影响、优点和缺点、限制性说明或遗憾。

Multiple reports may be generated for different target audiences.

可针对不同的目标受众生成多份报告。

> **NOTE** AE reports could be generated for different target audiences due to access limitations or other factors. Also, multiple reports could be needed to allow for interim reports during the life of the effort.

> **注**：AE 报告可能因访问限制或其他因素而针对不同的目标受众生成。此外，可能还需要多份报告，以便在该项工作期间提供中期报告。

It may be helpful to document in the report the level of rigor with which the AE effort was conducted, along with any known deficiencies such as incomplete or inaccurate data as inputs, key stakeholder inputs not received and use of models beyond their normal range of operation.

在报告中记录开展 AE 工作所达到的严谨程度可能是有益的，同时记录任何已知缺陷，例如作为输入的数据不完整或不准确、未收到关键利益相关方的输入，以及将模型用于超出其正常运行范围。

## Annex A (informative) — Value and quality concepts ｜ 附录 A（资料性）— 价值和质量概念

### A.1 General 总则

This annex complements Clauses 4 and 5 with additional information about value and quality concepts as used in this document.

本附录补充第 4 章和第 5 章，就本文件中所用的价值和质量概念提供附加信息。

Value and quality are two distinct attributes of an entity that ultimately determines its inferiority or superiority. It is often the case that quality of the entity is in the hands of the producer, while it is actually the consumer who determines the value of the entity, for which the consumer would willingly and knowingly pay. The value is a function of the quality that resides in the product or service, so this means that ultimately it is the consumer who determines what quality is acceptable. In other words, quality corresponds to the means, while value is subjective and is relative to the ends.

价值和质量是实体的两种不同属性，它们最终决定该实体的优劣。常见的情形是：实体的质量掌握在生产者手中，而实际上是由消费者决定实体的价值，消费者愿意并知情地为此付费。价值是产品或服务中所蕴含之质量的函数，因此这意味着最终是由消费者决定何种质量可以接受。换言之，质量对应于手段，而价值是主观的，并且是相对于目的而言的。

Carl Menger[52] wrote in 1871: "Value is nothing inherent in goods, no property of them, nor an independent thing existing by itself. It is a judgment economizing men make about the importance of goods at their disposal for the maintenance of their lives and well-being. Hence value does not exist outside the consciousness of men."

卡尔·门格尔[52]于 1871 年写道：“价值并非物品所固有之物，也不是物品的任何属性，更不是独立自在之物。它是从事经济的人就其所支配的物品对于维持其生命和福祉的重要性所作出的判断。因此，价值不存在于人的意识之外。”

Drucker[29] had this to say about quality: "Quality in a product or service is not what the supplier puts in. It is what the customer gets out and is willing to pay for. A product is not quality because it is hard to make and costs a lot of money, as manufacturers typically believe. That is incompetence. Customers pay only for what is of use to them and gives them value. Nothing else constitutes quality".

德鲁克[29]对质量有如下论述：“产品或服务的质量不在于供应商投入了什么，而在于顾客得到了什么并愿意为之付费。产品并不因为制造困难、耗资巨大就具有质量，尽管制造商通常这样认为。那是无能。顾客只为对他们有用、能给他们带来价值的东西付费。除此之外，任何其他东西都不构成质量。”

### A.2 Evaluation factors 评估因素

Value and quality are related to the factors used in the AE effort. These factors are used in each evaluation tier as illustrated in Figure A.1.

价值和质量与 AE 工作中所用的因素相关。如图 A.1 所示，这些因素用于每个评估层级。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.1 — Factors decomposition example (Simple case)**

**图 A.1 — 因素分解示例（简单情形）**

Often the factors decomposition can be performed in a strict hierarchical fashion as shown, but in more complex cases lower tier factors can impact more than one factor in a higher tier as illustrated in Figure A.2.

因素分解通常能按所示的严格层级方式进行，但在更复杂的情形中，较低层级的因素能影响较高层级的一个以上因素，如图 A.2 所示。

In similar fashion, the evaluation objectives in each tier can also be structured in a way where objectives in one tier will “satisfy” objectives in an upper tier. However, it is not always possible to have a simple and direct correlation between objectives in separate tiers.

类似地，各层级中的评估目标也能以如下方式构建：某一层级中的目标将“满足”上一层级中的目标。然而，并非总能在不同层级的目标之间建立简单而直接的关联。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.2 — Factors decomposition example (Complex case)**

**图 A.2 — 因素分解示例（复杂情形）**

Factors will be identified in each tier that best support the evaluation approach or methods used. But lower tier factors are not always needed, as illustrated in Figure A.3. In some cases, factors within a tier will need to be decomposed into lower level sub-factors to facilitate their use.

将在每个层级中识别最能支持所用评估途径或方法的因素。但并非总是需要较低层级的因素，如图 A.3 所示。在某些情形中，某一层级内的因素将需要分解为更低层级的子因素，以便于其使用。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.3 — Selective factors decomposition**

**图 A.3 — 选择性因素分解**

The AE factors defined in this document are similar to quality attributes in ATAM (see Annex D) and quality characteristics in the ISO/IEC 25000 family of standards on Systems and software Quality Requirements and Evaluation (SQuaRE). A summary of key concepts in SQuaRE are provided in A.4.5.

本文件所定义的 AE 因素类似于 ATAM 中的质量属性（见附录 D），以及关于系统与软件质量要求和评价（SQuaRE）的 ISO/IEC 25000 系列标准中的质量特性。SQuaRE 中关键概念的概述见 A.4.5。

### A.3 Value 价值

#### A.3.1 General 总则

This clause provides information on value, value-focused thinking, value models and value measures that could be useful in applying this document. The following items are covered:

本条提供关于价值、价值聚焦思维、价值模型和价值度量的信息，这些信息在应用本文件时可能有用。所涵盖的内容如下：

- what is “Value”;

- 什么是“价值”；

- Keeney’s value-focused thinking;

- Keeney 的价值聚焦思维；

- value assessment of system architectures;

- 系统架构的价值评定；

- Ring’s value model;

- Ring 的价值模型；

- stakeholder values, qualities and measures.

- 利益相关方价值、质量和度量。

The inclusion of these items does not imply endorsement of these particular ways of addressing value. Exclusion of other items is not intended to imply their shortfalls. The intention is to include those items that can be related to the conceptual elements in this document.

列入这些内容并不意味着认可这些处理价值的特定方式。未列入其他内容也无意暗示其存在不足。其意图是列入那些能与本文件中的概念元素相关联的内容。

#### A.3.2 What is “Value”? 什么是“价值”？

The importance of the concept of “Value” during architecting has been underscored in numerous articles, journal papers, case studies, books, and in practice. However, there is relatively little information about what value is, what its characteristics are or how stakeholders can best determine it. There are a wide variety of opinions on the nature of “Value”; some of these are summarized below:

在架构工作过程中“价值”概念的重要性已在众多文章、期刊论文、案例研究、书籍以及实践中得到强调。然而，关于价值是什么、其特性如何、或利益相关方如何能最好地确定价值，相关信息相对较少。对于“价值”的本质存在多种多样的观点；其中一些概述如下：

- Value as a higher order concept is misunderstood and sometimes mistaken with other concepts (e.g. cost, monetary return, importance, profit, advantage, return on investment).

- 价值作为一个高阶概念被误解，有时与其他概念混淆（例如成本、货币回报、重要性、利润、优势、投资回报）。

- Value and quality are often treated as synonyms, whereas quality is more properly treated as the means while value is the ends.

- 价值和质量常被当作同义词，而更恰当地说，质量应被视为手段，价值则是目的。

- Value is perceptual and subjective.

- 价值是感知性的和主观的。

- Value is determined based on a situation and is temporal in nature.

- 价值依据情境确定，并且本质上具有时间性。

- Stakeholders (and architects) make trade-offs when assessing value.

- 利益相关方（以及架构师）在评定价值时进行权衡。

- Value is created by consumption or utilization or possession.

- 价值通过消费、利用或占有而创造。

- Value of a product is what buyers are willing to pay[53].

- 产品的价值即购买者愿意支付的数额[53]。

- Value is the consumer’s overall assessment of the utility of a product based on perceptions of what is received and what is given[55]; and

- 价值是消费者基于对所获与所予的感知，对产品效用的总体评定[55]；以及

- Value reflects the customers desire to retain or obtain a system and depends on how much the system agrees with the value system of the customer[34].

- 价值反映客户保有或获取某一系统的意愿，并取决于该系统与客户价值体系的契合程度[34]。

#### A.3.3 Value-focused thinking 价值导向思维

Keeney[16] considers value as the fundamental construct in decision making and presents procedures and theoretical foundations for value-focused thinking. He considers value-focused thinking to be applicable in situations where a complex decision is necessary with no clear solution possible and the decision that is being made is critical to the stakeholders affected by the decision. The central role of thinking about values is expressed in Figure A.4.

Keeney[16] 将价值视为决策中的基本构念，并给出了价值导向思维的程序和理论基础。他认为，价值导向思维适用于下列情形：必须作出复杂决策，且不可能存在明确的解，而正在作出的决策对受该决策影响的利益相关方至关重要。关于价值思考的核心作用如图 A.4 所示。

Per Keeney, value-focused thinking essentially is comprised of two activities: a) deciding what the stakeholder wants or expects, and b) figuring out how to get it for them. According to Keeney, what the stakeholder wants or expects could be certain benefits that are intangible (like emotions, feelings, superiority etc.), or it can be tangible (like goods, services, money, capabilities, etc.). Value-focused thinking recognizes that design of any system or offering must uphold the expected value for its stakeholders without which stakeholders may not participate as anticipated or the system/offering may not be viable.

按照 Keeney 的观点，价值导向思维本质上由两项活动构成：a) 确定利益相关方想要或期望什么；b) 弄清如何为其获取。Keeney 认为，利益相关方想要或期望的，能是某些无形收益（如情绪、感受、优越感等），也能是有形收益（如货物、服务、金钱、能力等）。价值导向思维认识到，任何系统或供给物的设计都必须维护其利益相关方的预期价值；若无此价值，利益相关方可能不会如预期那样参与，或者系统／供给物可能无法存续。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.4 — Thinking about values[21]**

**图 A.4 — 关于价值的思考[21]**

#### A.3.4 Value assessment of system architectures 系统架构的价值评定

Selva & Crawley[54] espouse the line of thought that the key characteristics of system architecting is to maximize stakeholder value, rather than profit or performance. They propose quantification of stakeholders’ value using value functions that capture the needs and requirements of stakeholders. According to them, some common approaches to assess the value of an engineered system are:

Selva 与 Crawley[54] 主张这样一种思想：系统架构工作的关键特征在于使利益相关方价值最大化，而非使利润或性能最大化。他们提出，使用能捕获利益相关方需要和需求的价值函数来量化利益相关方的价值。他们认为，评定某一工程化系统价值的若干常见途径如下：

- using end-to-end simulation models to simulate every function and its interaction with the surrounding context to calculate the value of the system-of-interest;

- 使用端到端仿真模型仿真每一功能及其与周围语境的交互，以计算所关注系统的价值；

- observing system simulation experiments to quantify the value of a certain dataset (eg. numerical weather prediction);

- 开展观测系统模拟试验，以量化某一数据集的价值（如数值天气预报）；

- rating the importance of different customer attributes and their coupling to design features by means of House of Quality tools (sometimes known as Quality Function Deployment);

- 借助质量屋工具（有时称为质量功能展开）评定不同客户属性的重要程度及其与设计特征的耦合关系；

- computing the net present value of an architecture to determine its cardinal ranking amongst a collection;

- 计算某一架构的净现值，以确定其在某一集合中的基数排序；

- adopting the value of information approach to identify the probabilities of different scenarios and the availability of useful information in these scenarios to make a data-based decision;

- 采用信息价值途径，识别不同场景的概率以及这些场景中有用信息的可获得性，以作出基于数据的决策；

- comparing the capabilities of the system architecture with the stakeholder requirements and use rule-based expert systems to assess the value of the system architecture.

- 将系统架构的能力与利益相关方需求相比较，并使用基于规则的专家系统评定系统架构的价值。

#### A.3.5 Ring’s value model Ring 的价值模型

Ring[56] defines a ”value cycle” with three levels, as shown in Figure A.5, that is useful in delivering value to stakeholders and to continuously manage and upgrade long-life systems. These levels are organized to focus on the system to be created, the system’s purpose and the value of the system to its stakeholders.

Ring[56] 定义了一个具有三个层级的“价值循环”，如图 A.5 所示，该循环有助于向利益相关方交付价值，并有助于持续管理和升级长寿命系统。这些层级的组织方式，使其分别聚焦于将要创建的系统、系统的目的以及系统对其利益相关方的价值。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.5 — Ring’s system value cycle[56]**

**图 A.5 — Ring 的系统价值循环[56]**

The model promotes the thought process of discerning stakeholder’s value before the system is created rather than after the system becomes operational. The model takes into account the criteria that value is not stationary and changes over time and promotes a pursuit-type system rather than a requirements-based system so as to purposefully adapt the context to the solution system.

该模型倡导在系统创建之前而非在系统投入运行之后辨识利益相关方价值的思维过程。该模型计入价值并非静止不变、而是随时间变化这一准则，并倡导追求型系统而非基于需求的系统，以便有目的地使语境适应于解系统。

#### A.3.6 Stakeholder values, qualities and measures 利益相关方价值、质量与度量

Gilb[49] considers stakeholder values as those things that describe the improvements a stakeholder needs or wants from a specific solution and qualities (A.4.2) and as those things that describe the quality attributes of the specific solution. Gilb considers function as the purpose of the solution and qualities as the distinguishing elements between two solutions in the same solution space. It is normally intended that qualities will deliver improvement on the stakeholder values.

Gilb[49] 认为，利益相关方价值是描述利益相关方需要或希望从某一特定解中获得何种改进的那些事物，而质量（A.4.2）则是描述该特定解的质量属性的那些事物。Gilb 将功能视为解的目的，并将质量视为同一解空间中两个解之间的区分性要素。通常期望质量能带来利益相关方价值的改进。

Accordingly, different solutions exhibit different qualities depending on the corresponding stakeholder values. Gilb espouses the view that quality and value measures are quantifiable (like in the case of more user-friendly, less reliability, enhanced performance and so on) and this quantification helps address stakeholder needs appropriately.

相应地，不同的解依据相应的利益相关方价值而表现出不同的质量。Gilb 主张质量度量与价值度量是可量化的（例如更易用、可靠性更低、性能增强等情形），并且这种量化有助于恰当地处理利益相关方需要。

#### A.3.7 Value articulation framework 价值表述框架

Doji[48] considers value to reside in the perception of the stakeholder and proposes the value articulation framework as the method for tracing value from conception to realization in an assured manner. He considers 4 dimensions as essential ingredients in establishing this trace. Regarding the context of technology management, these dimensions are: Stakeholder and their perception of value, Quality characteristics of the Technology that is developed (which are the carriers of value and hence are of potential value), Technology management discipline (which aids in translating the potential value into actual value), and lastly the value that accrues to the given Stakeholder. Once the elements pertaining to the different dimensions are identified, he utilizes the generic X-matrix representation, as shown in Figure A.6, to establish the corresponding linkages and trace value creation, across the various dimensions.

Doji[48] 认为价值存在于利益相关方的感知之中，并提出价值表述框架，作为以有保证的方式从概念到实现追踪价值的方法。他认为有 4 个维度是建立这种追踪的关键要素。就技术管理的语境而言，这些维度是：利益相关方及其价值感知；所开发技术的质量特性（它们是价值的载体，因而具有潜在价值）；技术管理学科（它有助于将潜在价值转化为实际价值）；以及最后，归于给定利益相关方的价值。一旦识别出与各维度有关的要素，他便利用如图 A.6 所示的通用 X 矩阵表示法，来建立相应的联系，并跨各维度追踪价值的创造。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.6 — Doji’s value articulation framework[48]**

**图 A.6 — Doji 的价值表述框架[48]**

### A.4 Quality 质量

#### A.4.1 General 总则

This clause provides information on quality attributes, quality models and quality measures that could be useful in applying this document. The following items are covered in this clause:

本条给出关于质量属性、质量模型和质量度量的信息，这些信息在应用本文件时可能有用。本条涵盖下列各项：

- what is “Quality”;

- 什么是“质量”；

- architecture quality attributes;

- 架构质量属性；

- Boehm and Nupul’s quality models and ontology;

- Boehm 与 Nupul 的质量模型与本体；

- standards on System and Software Quality Requirements and Evaluation (SQuaRE) – the ISO/IEC 25000 family.

- 关于系统与软件质量要求和评价（SQuaRE）的标准——ISO/IEC 25000 系列。

The inclusion of these items does not imply endorsement of these particular ways of addressing quality. Exclusion of other items is not intended to imply their shortfalls. The intention is to include those items that can be related to the conceptual elements in this document.

列入这些条目并不意味着认可这些处理质量的特定方式。未列入其他条目也无意暗示它们存在缺陷。其意图是列入那些能与本文件中的概念元素相关联的条目。

#### A.4.2 What is “Quality”? 什么是“质量”？

The importance of the concept of “Quality” during architecting has been underscored in numerous articles, journal papers, case studies, books, and in practice. “Quality” is a subjective term for which each person or sector has its own definition. There are a wide variety of opinions on the nature of “Quality”; some of these are summarized below:

架构工作期间“质量”概念的重要性已在大量文章、期刊论文、案例研究、书籍以及实践中得到强调。“质量”是一个主观术语，每个人或每个部门都有自己的定义。关于“质量”的本质存在各种各样的观点；以下概述其中一些：

- Quality has a pragmatic interpretation as the non-inferiority or superiority of something.

- 质量在实用意义上可解释为某事物的非劣性或优越性。

- Quality is the characteristics of a product or service that bear on its ability to satisfy stated or

- 质量是产品或服务的特性，这些特性关系到其满足明确或

implied needs[26].

隐含需要[26]的能力。

- Quality is a product or service free of deficiencies[26].

- 质量是无缺陷的产品或服务[26]。

- Quality means “fitness for purpose”[30].

- 质量意味着“适合用途”[30]。

- Quality means “conformance to requirements”[28].

- 质量意味着“符合要求”[28]。

- Quality means “uniformity around a target”[32].

- 质量意味着“围绕目标的均匀性”[32]。

- Quality means “the loss a product imposes on society after it is shipped”[32].

- 质量意味着“产品出厂后给社会造成的损失”[32]。

- Quality in a product or service is not what the supplier puts in. It is what the customer gets out and is willing to pay for[29].

- 产品或服务的质量不是供应商投入的东西。它是客户得到并愿意为之付费的东西[29]。

- Degree to which a set of inherent characteristics fulfills requirements[2].

- 一组固有特性满足要求的程度[2]。

- Quality is “excellence of the system in a chosen dimension and is the basis for satisfying its stated purpose”[34].

- 质量是“系统在所选维度上的卓越性，并且是满足其规定目的的基础”[34]。

- Quality characteristics of a system are a set of essential and distinguishing attributes that have a pragmatic interpretation of the system’s inferiority or superiority[51].

- 系统的质量特性是一组本质性且具区分度的属性，对系统的劣与优具有实用主义的解释[51]。

In business, engineering and manufacturing, quality has a pragmatic interpretation as the non-inferiority or superiority of something; it is also defined as fitness for purpose. Quality is a perceptual, conditional and somewhat subjective attribute and may be understood differently by different people. Consumers may focus on the specification quality of a product/service or how it compares to competitors in the marketplace. Producers might measure the conformance quality or the degree to which the product/service was produced correctly[30].

在商业、工程和制造领域，质量被实用主义地解释为某事物的非劣性或优越性；它也被定义为适用性。质量是一种感知性的、有条件的且带有一定主观性的属性，不同的人可能有不同的理解。消费者可关注产品／服务的规格质量，或关注其在市场上与竞争者的比较情况。生产者则可能测量符合性质量，或产品／服务被正确生产的程度[30]。

Support personnel may measure quality in the degree that a product is reliable, maintainable or sustainable. A quality item (an item that has quality) can perform satisfactorily in service and is suitable for its intended purpose[31].

保障人员可按产品可靠、可维护或可持续的程度来测量质量。有质量的物品（即具有质量的物品）能在使用中令人满意地运行，并适宜于其预期目的[31]。

#### A.4.3 Architecture quality attributes 架构质量属性

Architecture quality attributes are the extent to which the architecture can deliver value to its stakeholders. It is a set of essential and distinguishing attributes that have a pragmatic interpretation of the architecture’s inferiority or superiority. It is a function of:

架构质量属性是架构能向其利益相关方交付价值的程度。它是一组本质性且具区分度的属性，对架构的劣与优具有实用主义的解释。它是下列各项的函数：

- architecture process outcomes,

- 架构过程的预期结果，

- impact of the architecture on various stakeholders,

- 架构对各类利益相关方的影响，

- measure of extent of achievement of stakeholder concerns, and

- 利益相关方关注点达成程度的度量，以及

- measure of capabilities of the architecture.

- 架构能力的度量。

While ATAM does deal with quality attributes, these are attributes of the architecture entity, not the architecture itself. See more on ATAM in Annex D.

ATAM 确实处理质量属性，但这些属性是架构实体的属性，而非架构本身的属性。关于 ATAM 的更多内容见附录 D。

Architecture quality attributes are the overall factors that affect behavior, structure, design and experience of architectures. They represent areas of concern that potentially impact the structure and behavior exhibited by the realized system. The extent to which the architecture handles a combination of quality attributes indicates the success of the architecting effort and overall quality of the realized system. The taxonomy for each architecture quality attribute would be:

架构质量属性是影响架构的行为、结构、设计和体验的总体因素。它们代表了一些关注领域，这些领域可能影响结构与已实现系统所呈现的行为。架构处理一组质量属性的程度，表明架构工作的成效以及已实现系统的总体质量。每个架构质量属性的分类法为：

a) Measures: The parameters by which the attributes are measured.

a) 度量：据以对属性进行度量的参数。

b) Factors: Policies and mechanisms of the system and its environment that impact the stakeholder concerns.

b) 因素：系统及其环境中影响利益相关方关注点的策略与机制。

c) Methods: Techniques for addressing concerns and processes for realizing the quality attributes during productions.

c) 方法：处理关注点的技术，以及在生产过程中实现质量属性的过程。

While conceptualizing architecture to address the architecture quality attributes, it is necessary to consider potential impact of each of the quality attributes on other stakeholder concerns. While tradeoff analysis techniques aid architects in prioritizing architecture quality attributes, architectural tactics describe how a specific quality attribute can be achieved. The importance of each architecture quality attribute depends on the context and the stakeholder’s concerns for which the specific architecture is conceptualized. Table A.1 provides an example list of architecture quality attributes.

在概念化架构以处理架构质量属性时，有必要考虑每个质量属性对其他利益相关方关注点的潜在影响。权衡分析技术帮助架构师排定架构质量属性的优先级，而架构战术则描述如何实现某一特定质量属性。每个架构质量属性的重要性取决于语境，以及该特定架构为之概念化的利益相关方关注点。表 A.1 给出了架构质量属性的示例清单。

**Table A.1 — Architecture quality attributes**

**表 A.1 — 架构质量属性**

| Quality attribute ／ 质量属性 | Description ／ 描述 |
| --- | --- |
| Coherence[35] ／ 连贯性[35] | Being logical and consistent ／ 具有逻辑性且保持一致 |
| Completeness[35] ／ 完整性[35] | Ability to form a whole ／ 形成整体的能力 |
| Elegance[39] ／ 优雅性[39] | Form and function are graceful and stylish ／ 形式与功能优雅且有格调 |
| Hierarchy[40] ／ 层次性[40] | Levels of abstractions ／ 抽象层级 |
| Modularity[37] ／ 模块化[37] | Separation of concerns ／ 关注点分离 |
| Variability[36] ／ 可变性[36] | Expandable in preplanned ways ／ 能按预先规划的方式扩展 |
| Subsetability[36] ／ 可子集性[36] | Support the production of a subset ／ 支持子集的生产 |
| Conceptual integrity[35] ／ 概念完整性[35] | Architecture unification ／ 架构统一 |
| Commonality[36] ／ 共性[36] | Sharing in preplanned ways ／ 按预先规划的方式共享 |
| Durability[38] ／ 耐久性[38] | Stand up robustly and remain in good condition ／ 稳健地经受住考验并保持良好状态 |
| Utility[38] ／ 实用性[38] | Useful and function well for people ／ 对人有用且运行良好 |
| Beauty[38] ／ 美观[38] | Delight people and raise their spirits ／ 令人愉悦并提振精神 |
| Robust[39] ／ 稳健[39] | Strong and not be vulnerable to changes ／ 强健且不易受变化影响 |
| Feasible[39] ／ 可行[39] | Should be able to implement ／ 宜能实施 |
| Flexible[39] ／ 灵活[39] | Adapt to changing conditions ／ 适应变化的条件 |
| Verifiable[39] ／ 可验证[39] | Perform as designed ／ 按设计运行 |
| Traceable[39] ／ 可追溯[39] | Architectural elements can be traced in any direction ／ 架构元素能沿任何方向追溯 |
| Cohesion[37] ／ 内聚性[37] | Forming a unified whole ／ 形成统一的整体 |

#### A.4.4 Boehm and Nupul’s quality model and ontology Boehm 与 Nupul 的质量模型与本体

Boehm and Nupul[41] attempts to qualitatively define quality by a set of attributes and metrics. They utilize a hierarchical quality model structured around high-level quality characteristics, intermediate level quality characteristics and primitive quality characteristics for this purpose. Each of these characteristics contributes to the overall quality level. They consider high level quality characteristics to represent the basic high-level requirements, intermediate level quality characteristics to represent the quality factors (portability, reliability, efficiency, usability, testability, understandability and flexibility), and primitive level quality characteristics to represent the quality metrics (device independence, accuracy, completeness, robustness, consistency, accountability and so on) that measure a given primary characteristic.

Boehm 与 Nupul[41] 试图通过一组属性和度量来定性地定义质量。为此，他们采用了一种层级式质量模型，其结构围绕高层质量特性、中间层质量特性和原始质量特性。这些特性中的每一个都对总体质量水平有所贡献。他们认为，高层质量特性代表基本的高层要求，中间层质量特性代表质量因素（可移植性、可靠性、效率、可用性、可测试性、可理解性和灵活性），原始层质量特性代表度量给定基本特性的质量度量（设备独立性、准确性、完整性、稳健性、一致性、可问责性等）。

Boehm and Nupul[27] present an ontology for reasoning about a system’s qualities. They espouse the view that functional requirements specifies what the system should do and hence it is additive in nature, while non-functional requirements (system qualities) specifies how well the system performs its functions and hence it is multiplicative and system-wide in nature. He utilizes a variation of the IDEF5[57] ontology structure comprising the elements Class, Individual, Referent, Relation, State and Process to express the ontology of system qualities. These class hierarchies are organized in terms of stakeholder value propositions, and child-class system qualities as means for achieving the parent class system quality end objectives. They also espouse the view that class hierarchies do not necessarily maintain one-to-many relationships and there are many cases where many-to-many relationships exist, especially when one or more system qualities impacts one or more top level system qualities. Table A.2 presents a typical upper level of system quality hierarchy.

Boehm 与 Nupul[27] 提出了一种用于推理系统质量的本体。他们主张这样一种观点：功能需求规定系统应做什么，因而在性质上是可加的；而非功能需求（系统质量）规定系统履行其功能的良好程度，因而在性质上是可乘的且遍及整个系统。他采用 IDEF5[57] 本体结构的一个变体来表达系统质量的本体，该结构由类、个体、指称物、关系、状态和过程这些元素组成。这些类层级按利益相关方价值主张来组织，并将子类系统质量作为实现父类系统质量目的目标的手段。他们还主张这样一种观点：类层级未必保持一对多关系，在许多情况下存在多对多关系，尤其当一个或多个系统质量影响一个或多个顶层系统质量时。表 A.2 给出了系统质量层级的典型上层。

**Table A.2 — Upper level of system quality hierarchy[27]**

**表 A.2 — 系统质量层级上层[27]**

| Stakeholder value-based system quality ends ／ 基于利益相关方价值的系统质量目的 | Contributing system quality means ／ 起贡献作用的系统质量手段 |
| --- | --- |
| Mission effectiveness ／ 任务效能 | Stakeholders-satisfactory balance of Physical Capability, Cyber Capability, Human Usability, Speed, Endurability, Maneuverability, Accuracy, Impact, Scalability, Versatility, Interoperability ／ 令利益相关方满意的物理能力、网络能力、人的可用性、速度、持久性、机动性、准确性、影响力、可扩展性、通用性、互操作性的平衡 |
| Resource utilization ／ 资源利用 | Cost, Duration, Key Personnel, Other Scarce Resources; Manufacturability, Sustainability ／ 成本、工期、关键人员、其他稀缺资源；可制造性、可持续性 |
| Dependability ／ 可信性 | Security, Safety, Reliability, Maintainability, Availability, Survivability, Robustness ／ 信息安全性、安全、可靠性、可维护性、可用性、生存性、稳健性 |
| Flexibility ／ 灵活性 | Modifiability, Tailorability, Adaptability ／ 可修改性、可裁剪性、适应性 |

#### A.4.5 The ISO/IEC 25000 family of standards on quality 关于质量的 ISO/IEC 25000 系列标准

##### A.4.5.1 General 概述

The ISO/IEC 25000 family of standards, also known as SQuaRE (System and Software Quality Requirements and Evaluation), has the goal of creating a framework for the evaluation of software product quality. Some of these are discussed in this annex:

ISO/IEC 25000 系列标准又称 SQuaRE（系统与软件质量要求和评价），其目标是建立用于评估软件产品质量的框架。本附录讨论其中一些标准：

- ISO/IEC 25000, SQuaRE — Quality model framework;

- ISO/IEC 25000，SQuaRE — 质量模型框架；

- ISO/IEC 25010, SQuaRE — System and Software Quality models;

- ISO/IEC 25010，SQuaRE — 系统和软件质量模型；

- ISO/IEC 25012, SQuaRE — Data Quality model;

- ISO/IEC 25012，SQuaRE — 数据质量模型；

- ISO/IEC 25020, SQuaRE — Measurement reference model and guide; and

- ISO/IEC 25020，SQuaRE — 测量参考模型与指南；以及

- ISO/IEC 25021, SQuaRE — Quality measure elements.

- ISO/IEC 25021，SQuaRE — 质量度量元素。

##### A.4.5.2 ISO/IEC 25000 Quality model framework ISO/IEC 25000 质量模型框架

This framework categorizes product quality into characteristics, which in some cases are further subdivided into sub-characteristics. A sub-characteristic in some cases can be divided into sub-sub-characteristics. This results in a quality breakdown structure as illustrated in Figure A.7.

该框架将产品质量划分为若干特性，其中一些特性又进一步细分为子特性。子特性在某些情况下能划分为子子特性。由此形成如图 A.7 所示的质量分解结构。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.7 — ISO/IEC 25000 Quality model framework**

**图 A.7 — ISO/IEC 25000 质量模型框架**

A.4.5.3) ISO/IEC 25010 System and software quality models

A.4.5.3) ISO/IEC 25010 系统和软件质量模型

A.4.5.3.1) Quality in use model

A.4.5.3.1) 使用质量模型

This quality in use model defines five characteristics related to outcomes of interaction with a system. It characterizes the impact that the product has on stakeholders. This model is presented in Figure A.8.

该使用质量模型定义了与同系统交互的结果有关的五项特性。它刻画了产品对利益相关方的影响。该模型如图 A.8 所示。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.8 — ISO/IEC 25010 Quality in use model**

**图 A.8 — ISO/IEC 25010 使用质量模型**

A.4.5.3.2) System/software product quality model

A.4.5.3.2) 系统／软件产品质量模型

This product quality model categorizes system/software product quality properties into eight characteristics that focuses on the target system. This model is presented in Figure A.9.

该产品质量模型将系统／软件产品的质量属性划分为八项聚焦于目标系统的特性。该模型如图 A.9 所示。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.9 — ISO/IEC 25010 System/software product quality model**

**图 A.9 — ISO/IEC 25010 系统／软件产品质量模型**

A.4.5.4) ISO/IEC 25012 Data quality model

A.4.5.4) ISO/IEC 25012 数据质量模型

This data quality model, as illustrated in Table A.3, categorizes data quality attributes into fifteen characteristics that are considered from two points of view: inherent and system dependent. While the inherent data quality refers to the degree to which the quality characteristics of data have the potential to satisfy needs when data is used in specified conditions, system dependent data quality refers to the degree to which data quality is reached and preserved within a system when data is used under specific conditions.

该数据质量模型如表 A.3 所示，将数据质量属性划分为十五项特性，这些特性从两个视角加以考虑：固有的和系统相关的。固有数据质量指在规定条件下使用数据时，数据的质量特性具有满足需要的潜力所达到的程度；而系统相关数据质量则指在特定条件下使用数据时，数据质量在某一系统内得以达到并得以保持的程度。

**Table A.3 — ISO/IEC 25012 Data quality model**

**表 A.3 — ISO/IEC 25012 数据质量模型**

| Characteristics ／ 特性 | Inherent ／ 固有的 | System dependent ／ 系统相关的 | Characteristics ／ 特性 | Inherent ／ 固有的 | System dependent ／ 系统相关的 |
| --- | --- | --- | --- | --- | --- |
| Accuracy ／ 准确性 | X |  | Efficiency ／ 效率 | X | X |
| Completeness ／ 完整性 | X |  | Precision ／ 精确性 | X | X |
| Consistency ／ 一致性 | X |  | Traceability ／ 可追溯性 | X | X |
| Credibility ／ 可信性 | X |  | Understandability ／ 可理解性 | X | X |
| Currentness ／ 现时性 | X |  | Availability ／ 可用性 |  | X |
| Accessibility ／ 可访问性 | X | X | Portability ／ 可移植性 |  | X |
| Compliance ／ 依从性 | X | X | Recoverability ／ 可恢复性 |  | X |
| Confidentiality ／ 保密性 | X | X |  |  |  |

A.4.5.5) ISO/IEC 25020 System and software product quality measurement reference model

A.4.5.5) ISO/IEC 25020 系统和软件产品质量测量参考模型

This product quality measurement reference model describes the relationship between a quality model, its associated quality characteristics (and sub-characteristics), and system and software product attributes with the corresponding software quality measures, measurement functions, quality measure elements and measurement methods. This model is presented in Figure A.10.

该产品质量测量参考模型描述了质量模型、其相关的质量特性（及子特性）以及系统和软件产品属性，与相应的软件质量度量、测量函数、质量度量元素和测量方法之间的关系。该模型如图 A.10 所示。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.10 — ISO/IEC 25020 System/software product quality measurement reference model**

**图 A.10 — ISO/IEC 25020 系统／软件产品质量测量参考模型**

An illustration of this model as given in ISO/IEC 25021 is presented in Table A.4.

ISO/IEC 25021 中给出的该模型示例见表 A.4。

**Table A.4 — ISO/IEC 25021 Product quality measurement reference model**

**表 A.4 — ISO/IEC 25021 产品质量测量参考模型**

| SNo ／ 序号 | Element ／ 元素 | Particulars ／ 详情 |
| --- | --- | --- |
| 1 | Quality measure element name ／ 质量度量元素名称 | Number of records ／ 记录数 |
| 2 | Objective ／ 目标 | To determine data quality of target data ／ 确定目标数据的数据质量 |
| 3 | Property to quantify ／ 待量化的属性 | Record is a set of related data items treated as a unit ／ 记录是被作为一个单元处理的一组相关数据项 |
| 4 | Relevant quality measures ／ 相关质量度量 | Measure of accuracy ／ 准确性度量 |
| 5 | Measurement method ／ 测量方法 | Review and analyze data records ／ 评审并分析数据记录 |
| 6 | List of sub-properties ／ 子属性清单 | Data item: lowest component of a group of data File: a set of related records ／ 数据项：一组数据的最低层组成部分；文件：一组相关记录 |
| 7 | Input for the quality measure element ／ 质量度量元素的输入 | Physical files of a database ／ 数据库的物理文件 |
| 8 | Numerical rules ／ 数值规则 | Adding total records ／ 累加记录总数 |
| 9 | Context of the quality measure element ／ 质量度量元素的语境 | Measure the accuracy and completeness to a group of data ／ 度量一组数据的准确性和完整性 |
| 10 | Measurement constraints ／ 测量约束 | Verify the impact of technology on the number of records generated for the same information ／ 验证技术对同一信息所生成记录数的影响 |

## Annex B (informative) — Relationship to other standards ｜ 附录 B（资料性）— 与其他标准的关系

### B.1 ISO/IEC standards in the domain of systems and software engineering 系统和软件工程领域的 ISO/IEC 标准

The following is a list of standards in ISO/IEC JTC1, SC7 that are most relevant and directly influence the conceptual model and requirements for architecture evaluation:

下列清单列出 ISO/IEC JTC1, SC7 中与架构评估的概念模型和要求最为相关且对其有直接影响的标准：

- ISO/IEC/IEEE 42020: This standard complements the architecture-related processes identified in ISO/IEC/IEEE 15288, ISO/IEC/IEEE 12207, and ISO 15704 with activities and tasks that enable architects and others to more effectively and efficiently implement architecture practices. Implementing these practices will help ensure that the architecture has greater influence on business and mission success. It specifies a coherent set of processes for governance, management, conceptualization, evaluation and elaboration of architectures, and activities that enable these processes. Users of this standard can apply these processes in the context of:

- ISO/IEC/IEEE 42020：本标准用一系列活动与任务补充了 ISO/IEC/IEEE 15288、ISO/IEC/IEEE 12207 和 ISO 15704 中识别的架构相关过程，这些活动与任务使架构师及其他人员能更有效且更高效地实施架构实践。实施这些实践将有助于确保架构对业务和任务的成功具有更大的影响力。本标准规定了一组协调一致的过程，用于架构的治理、管理、概念化、评估和细化，以及使这些过程得以开展的活动。本标准的使用者能在下列语境中应用这些过程：

B.1.1) understanding, development and evolution of entities through their life cycle stages such as conception, development, implementation, operation, sustainment, decommissioning, and disposal;

B.1.1) 通过实体的生存周期阶段（如构想、开发、实施、运行、维持、退役和处置）对实体进行的理解、开发和演进；

B.1.2) organization(s) acting as users, customers and providers of the solution specified by the architecture description; and

B.1.2) 作为架构描述所规定的解的使用者、客户和提供者的组织；以及

B.1.3) architecting of entities.

B.1.3) 实体的架构工作。

- ISO/IEC/IEEE 42010: This standard addresses the creation, analysis and sustainment of architectures of systems using architecture descriptions. A conceptual model of architecture description is established in this standard. The required contents of an architecture description are specified. Architecture viewpoints, architecture frameworks and architecture description languages are introduced for codifying conventions and common practices of architecture description. The required content of architecture viewpoints, architecture frameworks and architecture description languages is specified.

- ISO/IEC/IEEE 42010：本标准处理利用架构描述对系统架构的创建、分析和维持。本标准建立了架构描述的概念模型，规定了架构描述所要求的内容。本标准引入架构视角、架构框架和架构描述语言，以将架构描述的约定和常见实践编纂成文，并规定了架构视角、架构框架和架构描述语言所要求的内容。

- ISO/IEC/IEEE 15288: This standard establishes a common framework for system life cycle processes, with well-defined terminology. It applies to the acquisition of systems, which can be comprised of products, services or both, as well as to the supply, development, operation, maintenance and disposal of systems, whether performed internally or externally to an organization. ISO/IEC/IEEE 15288 is intended to be used either stand alone, or jointly with other documents such as ISO/IEC/IEEE 12207, and supplies a process reference model that supports process capability assessment in accordance with ISO/IEC 15504-2.

- ISO/IEC/IEEE 15288：本标准建立了系统生存周期过程的通用框架，并配有定义明确的术语。它适用于系统的获取（系统能由产品、服务或二者共同构成），也适用于系统的供应、开发、运行、维护和处置，无论这些活动是在组织内部还是外部进行。ISO/IEC/IEEE 15288 既宜单独使用，也宜与 ISO/IEC/IEEE 12207 等其他文件联合使用，并提供了一种过程参考模型，用以支持按照 ISO/IEC 15504-2 开展的过程能力评定。

### B.2 ISO standards in the domain of enterprise activities 企业活动领域的 ISO 标准

- ISO 15704: This standard defines the requirements for enterprise-reference architectures and methodologies, as well as the requirements that such architectures and methodologies shall satisfy to be considered a complete enterprise reference architecture and methodologies. The scope of these enterprise-reference architectures and methodologies covers those constituents deemed necessary to carry out all types of enterprise creation projects as well as any incremental change projects required by the enterprise throughout the whole life of the enterprise, including:

- ISO 15704：本标准定义了企业参考架构和方法论的要求，以及此类架构和方法论要被认定为完整的企业参考架构和方法论所应满足的要求。这些企业参考架构和方法论的范围涵盖那些被认为开展各类企业创建项目以及企业在整个企业生存期内所需的任何渐进式变更项目所必需的组成部分，包括：

- enterprise creation;

- 企业创建；

- major enterprise restructuring efforts; and

- 重大的企业重组工作；以及

— incremental changes affecting only parts of the enterprise-life cycle.

— 仅影响企业生存周期部分环节的渐进式变更。

### B.3 Relationship between architecture standards 架构标准之间的关系

Figure B.1 describes the main relationships between this document and other ISO standards related to architecture and related activities. This document does the following:

图 B.1 描述了本文件与架构及相关活动的其他 ISO 标准之间的主要关系。本文件开展下列工作：

- formalizes the evaluation act of:

- 将下列各项的评估活动形式化：

- architecture entities as defined by ISO/IEC/IEEE 42020;

- ISO/IEC/IEEE 42020 所定义的架构实体；

- enterprise architectures as defined by ISO 15704;

- ISO 15704 所定义的企业架构；

- system architectures as defined by ISO/IEC/IEEE 15288;

- ISO/IEC/IEEE 15288 所定义的系统架构；

- software architecture as defined by ISO/IEC/IEEE 12207;

- ISO/IEC/IEEE 12207 所定义的软件架构；

- Considers evaluation of architecture possibly based evidence (formalized viewpoints, views and models) from architecture description as defined by ISO/IEC/IEEE 42010; and

- 考虑可能基于 ISO/IEC/IEEE 42010 所定义的架构描述中的证据（形式化的架构视角、架构视图和模型）对架构进行的评估；以及

- Addresses concerns of the stakeholders acting in the context of enterprises and projects as defined by ISO 15704.

- 处理在 ISO 15704 所定义的企业和项目语境中行动的利益相关方的关注点。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure B.1 — Main relationships between ISO/IEC/IEEE 42030 and other ISO standards**

**图 B.1 — ISO/IEC/IEEE 42030 与其他 ISO 标准之间的主要关系**

## Annex C (informative) — Architecture evaluation examples ｜ 附录 C（资料性）— 架构评估示例

### C.1 General 总则

This annex provides examples using the architecture evaluation concepts outlined in this document for the following cases:

本附录针对下列情形，给出运用本文件所述架构评估概念的示例：

- business and information technology (IT) architecture;

- 业务和信息技术（IT）架构；

- software architecture;

- 软件架构；

- service architecture; and

- 服务架构；以及

- enterprise architecture

- 企业架构

The examples start off by identifying the relevant stakeholder concerns and using these to define the objectives for the evaluation. These objectives indicate the qualities that are expected from the architecture or its architecture entity. The qualities are tangibly expressed with the help of one or more factors. By implementing assessment and analysis methods with respect to these factors the evaluation results can be determined.

这些示例首先识别相关的利益相关方关注点，并据此定义评估的目标。这些目标指明对架构或其架构实体所期望的质量。这些质量借助一个或多个因素而得到有形表达。针对这些因素实施评定方法和分析方法，即能确定评估结果。

These factors are sometimes decomposed into subordinate factors to facilitate the examination. It is sometimes necessary to build a model to show how the factors contribute to the evaluation results. An example of this approach is described below:

为便于考察，这些因素有时被分解为从属因素。有时有必要构建模型，以表明这些因素如何促成评估结果。该途径的一个示例如下所述：

- Concern: FUNCTIONALITY. For this example, use specific case of “License Sharing.” This can be elaborated as follows:

- 关注点：功能性。本示例采用“许可共享”这一具体情形。它能如下展开：

System provides function X, defined in the use-case view. It would be evaluated by doing a walkthrough (potentially of several views) of that associated use-case. The use-case can be further elaborated by "time to execute", which would likewise be evaluated using walkthroughs perhaps coupled to an executable model.

系统提供功能 X，该功能在用况视图中定义。它将通过对相关用例进行走查（可能涉及若干视图）来评估。用例能进一步用“执行时间”加以展开，后者同样将采用走查来评估，或许还结合可执行模型。

- Concern: SECURITY. For this example, use specific case of “Unauthorized Access”. This can be elaborated as follows:

- 关注点：信息安全。本示例采用“未授权访问”这一具体情形。它能如下展开：

System is secure to use in a hostile environment, further defined by resisting various anti-use-cases (provided in a threat anti-use-case view). These can be further measured by Information Assurance Technical Framework ratings for strength of mechanism and/or assurance level. These would then be evaluated by walkthroughs and examination of the properties of both selected system and components and specified process elements (possibly another view) by which they are composed. A threat anti-use-case can be used to describe the abuse cases or what an attack might do to break the system security.

系统在敌对环境中使用是信息安全可靠的，这进一步由抵御各类反用例（在威胁反用例视图中给出）来定义。这些还能进一步用信息保障技术框架对机制强度和／或保障等级的评级来测量。随后将通过走查，并考察所选系统与构件的属性以及据以构成它们的规定的过程元素（可能是另一视图），来对这些加以评估。威胁反用例能用于描述滥用情形，或描述攻击为破坏系统信息安全可能采取的行动。

### C.2 Business and IT architecture evaluation 业务和 IT 架构评估

#### C.2.1 Situation 情境

A mail-order business (e.g. online clothing store) is trying to work out how to comply with new privacy regulations. One option is to update their current IT systems and business processes to fix gaps and achieve compliance. The alternative is to migrate to a SaaS software solution and associated business processes that comply with the regulations. They would like to evaluate their business and IT architectures to determine which option is better. The stakeholder concerns in Table C.1 are deemed to be relevant.

一家邮购企业（如在线服装商店）正在设法弄清如何遵守新的隐私法规。一种方案是更新其当前的 IT 系统和业务流程，以弥补差距并达到合规。另一种方案是迁移到符合该法规的 SaaS 软件解及相关的业务流程。他们希望评估其业务和 IT架构，以确定哪种方案更好。表 C.1 中的利益相关方关注点被认为具有相关性。

**Table C.1 — Business/IT architecture — Stakeholder concerns**

**表 C.1 — 业务／IT 架构 — 利益相关方关注点**

| Stakeholder ／ 利益相关方 | Concerns ／ 关注点 |
| --- | --- |
| Business ownership ／ 业务所有者 | Lifecycle costs, potential business value ／ 生存周期成本、潜在业务价值 |
| Business operations ／ 业务运营 | Cycle-time to compliance, disruptions due to change in business processes and IT infrastructure ／ 达到合规的周期时间，因业务流程和 IT 基础设施变更而造成的干扰 |
| IT operations ／ IT 运营 | Reliability, availability and ease of operations ／ 可靠性、可用性和运行便捷性 |

#### C.2.2 Business/IT architecture — Evaluation synthesis 业务／IT 架构 — 评估综合

**Table C.2 — Business/IT architecture — Evaluation synthesis**

**表 C.2 — 业务／IT 架构 — 评估综合**

| Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Evaluation synthesis approach ／ 评估综合途径 | Results ／ 结果 |
| --- | --- | --- | --- |
| Establish trade-offs among alternatives ／ 在各备选方案之间确立权衡 | Comparison of total life cycle cost of each option Including maintenance and business operations costs Comparison of business value impacts Transition comparison: cycle time, cost, disruptions, people impacts ／ 比较各方案的总生存周期成本，包括维护成本和业务运营成本；比较业务价值影响；比较转换：周期时间、成本、干扰、人员影响 | Combine all one-time costs, and all annual costs: IT, business operations Estimate business impacts in a median scenario, making necessary assumptions and projections ／ 合并全部一次性成本和全部年度成本：IT、业务运营；在中位情景下估计业务影响，作出必要的假设和预测 | Migration option has higher upfront cost ($6 M vs. $1,5 M), but lower annual cost ($2,2 M vs $2,7 M). Business capability impacts mostly balance out, no deal-breakers Likely positive long-term impact as SaaS solution evolves Substantial disruption impacts, both on brand image and people impacts: Medium ↓ ／ 迁移方案的前期成本更高（600 万美元对 150 万美元），但年度成本更低（220 万美元对 270 万美元）。业务能力影响大体相抵，无致命问题；随着 SaaS 解演进，很可能产生正向长期影响；干扰影响显著，既有品牌形象方面，也有人员影响方面：中 ↓ |
| Determine stakeholder priorities, current business situation ／ 确定利益相关方优先级和当前业务状况 | Understand what is important to stakeholders Understand current pressures on the business and its impact on the decision ／ 理解对利益相关方而言重要的事项；理解业务当前面临的压力及其对决策的影响 | Stakeholder interviews Business environment study, study of management reports ／ 利益相关方访谈；业务环境研究、管理报告研究 | Priority is no adverse impacts on capability, minimize cost Emphasis on short-term Considerable competitive pressure, struggle for survival ／ 优先事项是不对能力产生不利影响，并尽量降低成本；强调短期；竞争压力相当大，为生存而挣扎 |
| Develop overall recommendation ／ 形成总体建议 | — Propose strategy, rationale ／ — 提出策略、理由 | User symposium Weigh findings against business priorities Expand space of options if possible ／ 用户研讨会；将研究发现与业务优先事项相权衡；如有可能，扩展选项空间 | Go with updating option, defer SaaS adoption due to survival pressures Plan on future migration to SaaS, rework business processes where possible to ease future transition (avoid disruption impacts when transition required) ／ 采用更新方案，因生存压力而推迟采用 SaaS；计划未来迁移到 SaaS，尽可能重做业务流程，以减轻未来的转换（避免在需要转换时产生干扰影响） |

#### C.2.3 Business/IT architecture — Value assessment 业务／IT 架构 — 价值评定

**Table C.3 — Business/IT architecture — Value assessment**

**表 C.3 — 业务／IT 架构 — 价值评定**

| Value aspect being assessed ／ 被评定的价值方面 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Value assessment method ／ 价值评定方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Total cost of ownership for updating solution ／ 更新方案的总拥有成本 | — Determine one-time costs and annual costs of updating option ／ — 确定更新方案的一次性成本和年度成本 | Cost of IT systems update Cost of IT systems operation and maintenance Cost of business process changes ／ IT 系统更新成本；IT 系统运行和维护成本；业务流程变更成本 | Project planning for updating project Obtain historical data for maintenance and operations costs, estimate changes ／ 更新项目的项目规划；获取维护成本和运行成本的历史数据，估计其变化 | One-time cost of $1,5 M for updating Annual cost of $2,7 M ／ 更新的一次性成本为 150 万美元；年度成本为 270 万美元 |
|  | — Determine one-time costs and annual costs of updating option ／ — 确定更新方案的一次性成本和年度成本 | — Business operations cost ／ — 业务运营成本 |  |  |
| Total cost of ownership for SaaS approach ／ SaaS 途径的总拥有成本 | Determine annual costs with SaaS approach Determine cost of migration, including training and business structural changes ／ 确定采用 SaaS 途径的年度成本；确定迁移成本，包括培训和业务结构性变更 | SaaS solution procurement costs SaaS solution infrastructure costs SaaS business process operation costs Cost of migration ／ SaaS 解采购成本；SaaS 解基础设施成本；SaaS 业务流程运营成本；迁移成本 | Project planning for migration project, including SaaS infrastructure Interactions with SaaS vendor Estimated impacts on operations costs ／ 迁移项目的项目规划，包括 SaaS 基础设施；与 SaaS 供应商的交互；对运营成本的估计影响 | One-time cost of $6 M for migration Annual cost of $2,2 M ／ 迁移的一次性成本为 600 万美元；年度成本为 220 万美元 |
| Business impact of missing and added SaaS capabilities ／ SaaS 能力缺失和新增的业务影响 | Determine impact of missing capabilities Determine value of added capabilities and modified business processes ／ 确定能力缺失的影响；确定新增能力和经修改业务流程的价值 | Business impact of missing functionality No deal-breakers Business value of added capabilities and process improvements ／ 功能缺失的业务影响；无致命问题；新增能力和流程改进的业务价值 | Business impact analysis Market and order history analysis, to determine impact of new and missing features on market share and customer satisfaction ／ 业务影响分析；市场和订单历史分析，以确定新增特性和缺失特性对市场份额和客户满意度的影响 | Some process efficiency impacts due to missing management reports: Low ↓ Small expected increase in market opportunity from analytics capabilities and process flexibilities: Low ↑ ／ 因管理报告缺失而产生若干流程效率影响：低 ↓；分析能力和流程灵活性带来的市场机会预计小幅增加：低 ↑ |
| Business impact of dependability and other quality characteristics ／ 可信性及其他质量特性的业务影响 | — Determine business impacts of quality characteristics once steady state reached ／ — 确定达到稳态后质量特性的业务影响 | Estimated changes in dependability Expected changes in operability ／ 可信性的估计变化；运行性的预期变化 | — Financial assessment of risk impacts, effect of process changes on effort, rework ／ — 对风险影响、流程变更对工作量和返工的影响进行财务评定 | — Loss of reliability and increased cycle time to fix problems may result in slightly decreased satisfaction and revenue: Low ↓ ／ — 可靠性损失和修复问题周期时间增加可能导致满意度和收入略有下降：低 ↓ |

Table C.3 (continued)

表 C.3（续）

| Value aspect being assessed ／ 被评定的价值方面 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Value assessment method ／ 价值评定方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Business impact of transition ／ 转换的业务影响 | — What will be the business impacts during the transition period? ／ — 转换期内将有哪些业务影响？ | Impact of cycle time Cost of disruptions People impacts ／ 周期时间的影响；干扰成本；人员影响 | Analyze effects on order fulfilment and satisfaction Impact on brand image ／ 分析对订单履行和满意度的影响；对品牌形象的影响 | Longer cycle time for SaaS migration and more quality problems will lead to ~10 % higher loss of revenue, and around 2 % reduction in market share due to brand image: Medium ↓ IT operations team will need to be downsized with the SaaS option: Medium ↓ ／ SaaS 迁移的周期时间更长且质量问题更多，将导致收入损失增加约 10 %，并因品牌形象而使市场份额下降约 2 %：中 ↓；采用 SaaS 方案将需要缩减 IT 运营团队：中 ↓ |

#### C.2.4 Business/IT architecture — Architectural analysis 业务／IT 架构 — 架构分析

**Table C.4 — Business/IT architecture — Architectural analysis**

**表 C.4 — 业务／IT 架构 — 架构分析**

| Object being analyzed ／ 被分析的对象 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Architectural analysis method ／ 架构分析方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| IT architecture ／ IT 架构 | — Customer information collection and storage policies ／ — 客户信息收集与存储策略 | Customer personal information being collected and stored Storage locations ／ 正在收集和存储的客户个人信息；存储位置 | DB schema analysis tools Interview IT operations team Business process analysis ／ 数据库模式分析工具；访谈 IT 运营团队；业务流程分析 | — List of customer information being collected and stored, with locations ／ — 正在收集和存储的客户信息清单及其位置 |
| IT architecture and business process architecture ／ IT 架构和业务流程架构 | — Customer information access control policies ／ — 客户信息访问控制策略 | IT access controls Business process access controls Business process need-to-know ／ IT 访问控制；业务流程访问控制；业务流程的知需原则 | Business process analysis IT system reviews Interviews with operations team Observation of business process execution ／ 业务流程分析；IT 系统评审；与运营团队的访谈；对业务流程执行的观察 | Business process gaps in need-to-know List of controls on access to customer information ／ 业务流程中知需方面的差距；客户信息访问控制清单 |
| IT and business process architecture ／ IT 和业务流程架构 | — Gaps in privacy compliance ／ — 隐私合规方面的差距 | Non-compliances to storage location restrictions Non-compliance to access control restrictions ／ 不符合存储位置限制之处；不符合访问控制限制之处 | — Analysis of controls required by privacy regulation ／ — 对隐私法规所要求的控制的分析 | List of gaps in IT systems to be fixed List of gaps in business process to be fixed ／ 待修复的 IT 系统差距清单；待修复的业务流程差距清单 |

Table C.4 (continued)

表 C.4（续）

| Object being analyzed ／ 被分析的对象 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Architectural analysis method ／ 架构分析方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| SaaS solution ／ SaaS 解 | — Identify missing and added functionality ／ — 识别缺失的功能和新增的功能 | Missing features compared to existing system Added features ／ 与现有系统相比缺失的特性；新增的特性 | Compare information in SaaS product literature with current system features Interact with SaaS vendor ／ 将 SaaS 产品资料中的信息与当前系统特性相比较；与 SaaS 供应商交互 | Some management reports missing Some analytics features added ／ 缺少若干管理报告；新增若干分析特性 |
| SaaS business process ／ SaaS 业务流程 | — Identify changes required in business processes ／ — 识别业务流程中所需的变更 | Business process changes Required structural changes to accommodate process changes Effect on operability and outcomes ／ 业务流程变更；为适应流程变更所需的结构性变更；对运行性和结果的影响 | Business process analysis Operations impact analysis Risk analysis ／ 业务流程分析；运营影响分析；风险分析 | Redefinition of roles for warehouse and financial personnel so the roles align to processes. Rework of processes so both groups align to each other. Errors and delays likely during transition More flexibility in business process ／ 重新定义仓库人员和财务人员的角色，使角色与流程保持一致。重做流程，使两类人员相互对齐。转换期间可能出现错误和延迟；业务流程更具灵活性 |
| SaaS approach (solution + business process) ／ SaaS 途径（解＋业务流程） | — Determine SaaS impact on reliability, availability and ease of operations ／ — 确定 SaaS 对可靠性、可用性和运行便捷性的影响 | Experiences of current users of SaaS approach Reliability and availability of SaaS solution ／ SaaS 途径当前用户的经验；SaaS 解的可靠性和可用性 | Interview existing SaaS approach user base Failure modes and effects analysis ／ 访谈现有 SaaS 途径用户群；故障模式与影响分析 | Some glitches experienced by SaaS users Loss of control leads to reliability issues: delays in fixing problems ／ SaaS 用户遇到若干小故障；失去控制导致可靠性问题：修复问题出现延迟 |

### C.3 Software architecture evaluation 软件架构评估

#### C.3.1 Situation 情境

A leading IT services provider utilizes a proprietary, hand-crafted resume management system for handling and processing resumes of potential candidates. While the recruitment processes of this organization are encoded in their work-flow systems, the resume management system lies outside. The organization’s top management has decided to increase the number of associates by a factor of 10X over the next 5 years. In this situation, the infrastructure team is trying to work out how best to facilitate resume handling and processing so as to handle the increasing demands. It has been decided by the top management that the existing outdated resume management system should be replaced with a best- in-class solution as the architecture of the existing system does not exist. There are two suppliers for the new resume management system. One solution is a cloud based software service and the other is a packaged commercial software product. They would like to evaluate both these options to determine which option is better.

一家领先的 IT 服务提供商使用专有的、手工构建的简历管理系统来处理和加工潜在候选人的简历。该组织的招聘流程已编入其工作流系统，而简历管理系统则处于该系统之外。该组织的高层管理者已决定在未来 5 年内将员工人数增加 10 倍。在此情境下，基础设施团队正设法找到促进简历处理和加工的最佳方式，以应对不断增长的需求。高层管理者已决定，由于现有系统的架构并不存在，应将现有过时的简历管理系统替换为一流的解。新的简历管理系统有两家供应商。一种解是基于云的软件服务，另一种是打包的商业软件产品。他们希望评估这两种方案，以确定哪种方案更好。

The stakeholder concerns in Table C.5 are deemed to be relevant.

表 C.5 中的利益相关方关注点被认为具有相关性。

**Table C.5 — Software architecture — Stakeholder concerns**

**表 C.5 — 软件架构 — 利益相关方关注点**

| Stakeholder ／ 利益相关方 | Concerns ／ 关注点 |
| --- | --- |
| Human resources ／ 人力资源 | Latency in achieving the recruitment goals due to change in infrastructure; loss of historical data ／ 因基础设施变更而导致实现招聘目标的延迟；历史数据丢失 |
| Chief information officer ／ 首席信息官 | Technologies involved in the new systems; support and upgrade options; hardware and other infrastructure options; security and privacy options ／ 新系统所涉及的技术；支持和升级选项；硬件及其他基础设施选项；信息安全选项和隐私选项 |
| IT operations ／ IT 运营 | Backup and recovery options; reliability, configurability, performance and maintainability options ／ 备份和恢复选项；可靠性、可配置性、性能和可维护性选项 |

#### C.3.2 Software architecture — Evaluation synthesis 软件架构 — 评估综合

**Table C.6 — Software architecture — Evaluation synthesis**

**表 C.6 — 软件架构 — 评估综合**

| Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Evaluation synthesis approach ／ 评估综合途径 | Results ／ 结果 |
| --- | --- | --- | --- |
| Establish data migration costs ／ 确定数据迁移成本 | Comparison of data schema Including supporting file formats Comparison of migration capabilities Including ability to utilize existing classification Comparison of migration time Manual migration, batch migration ／ 比较数据模式，包括支持的文件格式；比较迁移能力，包括利用现有分类的能力；比较迁移时间；手工迁移、批量迁移 | Migration analysis Regression analysis ／ 迁移分析；回归分析 | Migration costs for the commercial product is $2 million. This is an additional feature in the system that needs to be procured. Migration costs for the cloud based service is $500 per 1 000 transactions. Migration effort is one time as data in old system is imported into the new instance for the commercial product. Migration effort is expended on demand basis for the cloud based service. ／ 商业产品的迁移成本为 200 万美元。这是系统中需要采购的一项附加特性。基于云的服务的迁移成本为每 1 000 笔事务 500 美元。对商业产品而言，由于旧系统中的数据被导入新实例，迁移工作量是一次性的。对基于云的服务而言，迁移工作量按需支出。 |
| Establish ownership of data and related costs ／ 确定数据的所有权及相关成本 | Comparison of data ownership Conditions for ownership transfer Access & security options Comparison of data criticality Data quality, meta-data schema ／ 比较数据所有权；所有权转移的条件；访问和信息安全选项；比较数据关键性；数据质量、元数据模式 | Customer data analytics KNIME tool ／ 客户数据分析；KNIME 工具 | All candidate data, relevant meta-data and relevant categorization are stored in the cloud by the service provider. Storage costs are fixed at $50 per month per GB of data. All candidate data, relevant meta-data are stored in organization’s infrastructure in-house. A RAID 1 TB storage costs $2 000. All data stored in the cloud are owned by the creators. Cloud software service only provides resources for managing the data. All data stored in the organization’s infrastructure are owned and managed by the organization. ／ 全部候选人数据、相关元数据和相关分类均由服务提供商存储在云中。存储成本固定为每月每 GB 数据 50 美元。全部候选人数据、相关元数据均存储在组织内部的基础设施中。一个 RAID 1 TB 存储的成本为 2 000 美元。存储在云中的所有数据均归其创建者所有。云软件服务仅提供用于管理数据的资源。存储在组织基础设施中的所有数据均由该组织拥有和管理。 |

Table C.6 (continued)

表 C.6（续）

| Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Evaluation synthesis approach ／ 评估综合途径 | Results ／ 结果 |
| --- | --- | --- | --- |
| Establish operating environment and related costs ／ 确定运行环境及相关成本 | Comparison of support effort 9x4 levels of availability L1, L2, L3 support options Comparison of maintenance effort Batch updates & patches Maintenance mode, time to recover ／ 比较支持工作量；9x4 可用性级别；L1、L2、L3 支持选项；比较维护工作量；批量更新与补丁；维护模式、恢复时间 | Operations Analysis Business Process Analysis ／ 运营分析；业务流程分析 | Enterprise infrastructure to facilitate internet based access of cloud based services. Integration with existing enterprise intranet infrastructure for commercial software product. Dedicated data and support center for managing the commercial software product in-house. ／ 用于支持对基于云的服务的互联网访问的企业基础设施。对商业软件产品而言，与现有企业内联网基础设施集成。用于在内部管理商业软件产品的专用数据与支持中心。 |

#### C.3.3 Software architecture — Value assessment 软件架构 — 价值评定

**Table C.7 — Software architecture — Value assessment**

**表 C.7 — 软件架构 — 价值评定**

| Value aspect being assessed ／ 被评定的价值方面 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Value assessment method ／ 价值评定方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Benefits in availing cloud services ／ 采用云服务的收益 | — Determine one-time benefits and recurrent benefits of cloud option ／ — 确定云选项的一次性收益与经常性收益 | Increasing infrastructure demands 10X in 5 years On demand availability Recruitment drives Pay as you go model Transaction based pricing ／ 基础设施需求在 5 年内增长 10 倍；按需可用性；招聘驱动因素；按使用付费模式；基于交易的定价 | — Multiple criteria decision analysis of eliciting value ／ — 引出价值的多准则决策分析 | High quality flexible services (24 x 7 availability) Increased resource availability and elasticity (scale up of 5X) Very competitive costs (nearest competitor is twice the price) Self-management ／ 高质量且灵活的服务（24×7 可用性）；资源可用性与弹性提升（可扩展 5 倍）；极具竞争力的成本（最接近的竞争者价格为其两倍）；自管理 |
| Benefits in availing commercial product ／ 采用商用产品所能获得的收益 | — Determine one-time benefits and recurring benefits of commercial product ／ — 确定商用产品的一次性收益与经常性收益 | User experience Aesthetic and minimalistic design Connectivity Anytime, anywhere Completeness No external licenses ／ 用户体验；美观而简约的设计；连接性；随时随地的可用性；完备性；无需外部许可 | — Utility and behavior assessment ／ — 效用与行为评定 | Industry standard in resume management Stable roadmap and planned upgrades Scalable across multiple geographies Multi-lingual ／ 简历管理领域的行业标准；稳定的路线图与有计划的升级；可跨多个地域扩展；多语言支持 |

Table C.7 (continued)

表 C.7（续）

| Value aspect being assessed ／ 被评定的价值方面 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Value assessment method ／ 价值评定方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Readiness levels of commercial product ／ 商用产品的就绪等级 | Determine technology landscape Determine software and supplier health indices Determine competitor landscape ／ 确定技术全景；确定软件与供应商健康指数；确定竞争者全景 | Software stability Minimal fixes Speed & performance Supplier stability Business continuity plans ／ 软件稳定性；最少的修复；速度与性能；供应商稳定性；业务连续性计划 | Technology and business readiness level assessment Customer life-line survey ／ 技术与业务就绪等级评定；客户生命线调查 | Software readiness level is 7 Software experience index is 5,7 Supplier readiness level is 6 Supplier customer satisfaction index is 92 % ／ 软件就绪等级为 7；软件体验指数为 5,7；供应商就绪等级为 6；供应商客户满意度指数为 92 % |
| Readiness levels of cloud service ／ 云服务的就绪等级 | Determine service landscape Determine technology landscape Determine s/w and service provider health indices ／ 确定服务全景；确定技术全景；确定软件与服务提供方健康指数 | Service stability Service quality levels Software stability Minimal fixes Service provider stability Service continuity plans ／ 服务稳定性；服务质量等级；软件稳定性；最少的修复；服务提供方稳定性；服务连续性计划 | Service scorecard assessment Service experience assessment Technology readiness level assessment ／ 服务记分卡评定；服务体验评定；技术就绪等级评定 | Service scorecard Slippage: 1/1 000 Down-time: 12 hours for 365 days Interaction score: 5,32 Service experience index: 4,7 Software service readiness level: 6 ／ 服务记分卡；滑移：1/1 000；停机时间：365 天中 12 小时；交互得分：5,32；服务体验指数：4,7；软件服务就绪等级：6 |

#### C.3.4 Software architecture — Architectural analysis 软件架构 — 架构分析

**Table C.8 — Software architecture — Architectural analysis**

**表 C.8 — 软件架构 — 架构分析**

| Object of interest ／ 所关注对象 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Architectural analysis method ／ 架构分析方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Quality attributes of cloud based software services ／ 基于云的软件服务的质量属性 | — Determine software and service quality levels ／ — 确定软件与服务的质量等级 | Under normal operating conditions Target: 1 000 transactions/ hour Under duress operating conditions Target: 100 transactions/ hour ／ 正常工作条件下：目标为 1 000 笔交易／小时；受压工作条件下：目标为 100 笔交易／小时 | Service quality attributes analysis Software quality attributes analysis Scenario based analysis ／ 服务质量属性分析；软件质量属性分析；基于场景的分析 | 9x2 levels of availability 9x4 levels of security 9x3 levels of privacy 256 bit encryption Sub 1 second response time ／ 9x2 级可用性；9x4 级信息安全；9x3 级隐私；256 位加密；低于 1 秒的响应时间 |

Table C.8 (continued)

表 C.8（续）

Table C.8 (continued)

表 C.8（续）

| Object of interest ／ 所关注对象 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Architectural analysis method ／ 架构分析方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Commercial product architecture ／ 商用产品架构 | — Interfacing and integration ／ — 接口与集成 | Back end integration Front end integration Data Synchronization Customization ／ 后端集成；前端集成；数据同步；定制 | — Analysis of interfaces, data schema, batch scripts, events, event data, triggers ／ — 对接口、数据模式、批处理脚本、事件、事件数据、触发器的分析 | Supports Linux and windows operating systems Database Clusters for storing and managing large amounts of data Accessible across multiple digital technologies Most functions accessible thru Command console availability APIs available for integration with enterprise applications ／ 支持 Linux 与 Windows 操作系统；用于存储和管理海量数据的数据库集群；可跨多种数字技术访问；大多数功能可通过命令控制台使用；可用性 API 可用于与企业应用集成 |

### C.4 Service architecture evaluation 服务架构评估

#### C.4.1 Situation 情形

A commercial airline services provider is trying to expand its services to cater to growing demand. Before expansion, the team would like to know whether the service architecture that it currently utilizes can be scaled-up, whether the current service quality levels can be retained, whether the cost of quality can be controlled and whether the difference that it brings to the passengers can be leveraged in some way.

一家商用航空服务提供方正力图扩展其服务，以满足不断增长的需求。在扩展之前，该团队希望了解：其当前所用的服务架构能否扩展；当前的服务质量等级能否保持；质量成本能否得到控制；以及其为乘客带来的差异能否以某种方式加以利用。

The stakeholder concerns in Table C.9 are deemed to be relevant.

表 C.9 中的利益相关方关注点被认为具有相关性。

**Table C.9 — Service architecture — Stakeholder concerns**

**表 C.9 — 服务架构 — 利益相关方关注点**

| Stakeholder ／ 利益相关方 | Concerns ／ 关注点 |
| --- | --- |
| Passengers ／ 乘客 | Hassle free travel experience; on-time performance; connectivity to other destina-tions; value for money ／ 无烦扰的旅行体验；准点性能；与其他目的地的连通性；物有所值 |
| Airlines’ top-management ／ 航空公司最高管理层 | Low-maintenance cost; average down-time below industry average; profitability; high level of safety; ／ 低维护成本；平均停机时间低于行业平均水平；盈利能力；高安全水平； |
| Investors ／ 投资者 | High return on investments; superior brand value; ／ 高投资回报；卓越的品牌价值； |

#### C.4.2 Service architecture — Evaluation synthesis 服务架构 — 评估综合

**Table C.10 — Service architecture — Evaluation synthesis**

**表 C.10 — 服务架构 — 评估综合**

| Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Evaluation synthesis approach ／ 评估综合途径 | Results ／ 结果 |
| --- | --- | --- | --- |
| Establish service quality levels ／ 确立服务质量等级 | Dependability of the service Average delays Missed connections Credibility of the service provider Successful claim resolution Efficiency of the service Baggage claims Oversales and overbooking Response times Dispute resolution timelines Service failure recovery timelines ／ 服务的可信性；平均延误；错过中转；服务提供方的可信度；索赔成功解决；服务的效率；行李索赔；超售与超额预订；响应时间；争议解决时限；服务失败恢复时限 | — Airline quality rating methodology ／ — 航空公司质量评级方法学 | On-time performance: 8,43 Denied boarding: 8,03/ month Mishandled baggage: 7,32 per 1 000 passengers Consumer complaints: 7,17 per 500 passengers Flight problems: 3 per day Customer service index: 4,32 Dispute resolution time: 60 days per complaint ／ 准点性能：8,43；拒绝登机：8,03／月；行李处理不当：每 1 000 名乘客 7,32；消费者投诉：每 500 名乘客 7,17；航班问题：每天 3 起；客户服务指数：4,32；争议解决时间：每起投诉 60 天 |
| Establish profes-sionalism levels ／ 确立专业水准等级 | Professional training of Personnel Average re-training in a year Service attitude & pro-activeness Accuracy of operations Information accuracy Low rates of breakdown and accidents Provision of committed services Customer satisfaction index Customer experience index Service failure recovery Time to recover Maintenance network ／ 人员的专业训练；年均再训练；服务态度与主动性；运行准确性；信息准确性；故障与事故的低发生率；承诺服务的提供；客户满意度指数；客户体验指数；服务失败恢复；恢复时间；维护网络 | — Multi-criteria decision making ／ — 多准则决策 | Days of re-training: 45 days in a year Failed connections: 15 per 1 000 passengers Customer service Complaints: 30 per 1 000 passengers Service failures: 2 per 300 trips Non-availability of staff: 1 per 2 000 services Maintenance down-time: 1 week per year Cancellations: 50 per 1 000 passengers Refunds: 50 per 500 passengers ／ 再训练天数：一年 45 天；中转失败：每 1 000 名乘客 15 起；客户服务投诉：每 1 000 名乘客 30 起；服务失败：每 300 次行程 2 起；人员不可用：每 2 000 次服务 1 起；维护停机时间：每年 1 周；取消：每 1 000 名乘客 50 起；退款：每 500 名乘客 50 起 |

Table C.10 (continued)

表 C.10（续）

| Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Evaluation synthesis approach ／ 评估综合途径 | Results ／ 结果 |
| --- | --- | --- | --- |
| Establish operating environment and related costs ／ 确立运行环境及相关成本 | Aircraft support 9x4 levels of availability L1, L2, L3 support options Aircraft operations 9x6 levels of safety 9x5 levels of recoverability Staff availability Cancelled Trips ／ 飞机保障；9x4 级可用性；L1、L2、L3 保障选项；飞机运行；9x6 级安全；9x5 级可恢复性；人员可用性；取消的行程 | — Evaluate Service SOP & operations SOP cost & effort ／ — 评估服务 SOP 与运行 SOP 的成本与工作量 | Price: $350 million per aircraft Maintenance: $35 million per aircraft per year Run-time: 6 000 hours per year Maintenance-time: 144 hours per 6 months Planned halt-time: 2 hour per trip — Fuel: 2,91 L/100 km ／ 价格：每架飞机 3.5 亿美元；维护：每架飞机每年 3 500 万美元；运行时间：每年 6 000 小时；维护时间：每 6 个月 144 小时；计划停机时间：每次行程 2 小时 — 燃油：2,91 L/100 km |

#### C.4.3 Service architecture — Value assessment 服务架构 — 价值评定

**Table C.11 — Service architecture — Value assessment**

**表 C.11 — 服务架构 — 价值评定**

| Value aspect being assessed ／ 被评定的价值方面 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Value assessment method ／ 价值评定方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Inflight service ／ 机上服务 | Determine the inflight experience index Determine the inflight service customer satisfaction index ／ 确定机上体验指数；确定机上服务客户满意度指数 | Inflight entertainment Technology and content Inflight communication Cellular and internet Inflight meals Quality of meals and drinks Seating Quality of seating Seating arrangements ／ 机上娱乐；技术与内容；机上通信；蜂窝网络与互联网；机上餐食；餐食与饮品质量；座椅；座椅质量；座位安排 | Airline service evaluation survey Analytic hierarchy process methodology ／ 航空公司服务评估调查；层次分析法方法学 | Passenger entertainment equipment conditions: 3,608 Seat and space comfortability: 3,585 Inflight entertainment programs and materials: 2,911 Interior cleanliness: 3,408 Meal variety and sufficiency: 3,123 Meal services: 3,362 Inflight service score: 0,214 ／ 乘客娱乐设备状况：3,608；座椅与空间舒适度：3,585；机上娱乐节目与材料：2,911；客舱内部清洁度：3,408；餐食种类与充足程度：3,123；餐食服务：3,362；机上服务得分：0,214 |

Table C.11 (continued)

表 C.11（续）

| Value aspect being assessed ／ 被评定的价值方面 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Value assessment method ／ 价值评定方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Customer service ／ 客户服务 | Determine the customer experience index Determine the customer service satisfaction index ／ 确定客户体验指数；确定客户服务满意度指数 | Ticketing Price and options Check-in Efficiency and interaction Communication Clear and precise Baggage No damage Timely information Customer care Quality of interaction Timely issue resolution ／ 售票；价格与选项；值机；效率与交互；沟通；清晰而准确；行李；无损坏；及时的信息；客户关怀；交互质量；及时的问题解决 | Customer experience satisfaction survey Stakeholder value assessment Quality of experience metrics and measures ／ 客户体验满意度调查；利益相关方价值评定；体验质量度量指标与措施 | Ticketing experience Index: 4,32 Check-in experience index: 5,32 Communication experience index: 5,32 Baggage experience index: 4,32 Customer care interaction index: 4,87 Issue resolution time: <1/2 hour Interaction quality index: 6,32 Safety index: 5,32 ／ 售票体验指数：4,32；值机体验指数：5,32；沟通体验指数：5,32；行李体验指数：4,32；客户关怀交互指数：4,87；问题解决时间：<1/2 小时；交互质量指数：6,32；安全指数：5,32 |

#### C.4.4 Service architecture — Architectural analysis 服务架构 — 架构分析

**Table C.12 — Service architecture — Architectural analysis**

**表 C.12 — 服务架构 — 架构分析**

| Object being analyzed ／ 被分析的对象 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Architectural analysis method ／ 架构分析方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Quality attributes of inflight services ／ 机上服务的质量属性 | — Determine service quality levels ／ — 确定服务质量等级 | Under normal operating conditions 8-hour International trip Under duress operating conditions Trip delayed by more than 8 hours ／ 正常工作条件下：8 小时国际航程；受压工作条件下：航程延误超过 8 小时 | Service quality attributes analysis Scenario based analysis ／ 服务质量属性分析；基于场景的分析 | Normal operations: 3 meals service 3 drinks service Soft-clean after every trip Toiletries refilled Air purged out Duress operations: 2 meals service 3 drinks service Poor cleaning Toiletries not refilled Pungent smell persists ／ 正常运行：3 次餐食服务；3 次饮品服务；每次航程后进行轻度清洁；洗漱用品补充；空气净化；受压运行：2 次餐食服务；3 次饮品服务；清洁不佳；洗漱用品未补充；刺激性气味持续存在 |

Table C.12 (continued)

表 C.12（续）

| Object being analyzed ／ 被分析的对象 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Architectural analysis method ／ 架构分析方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Quality attributes of baggage services ／ 行李服务的质量属性 | — Determine service quality levels ／ — 确定服务质量等级 | Under normal operating conditions 8-hour International trip Under duress operating conditions Trip delayed by more than 8 hours ／ 正常工作条件下：8 小时国际航程；受压工作条件下：航程延误超过 8 小时 | Service quality attributes analysis Scenario based analysis ／ 服务质量属性分析；基于场景的分析 | Normal operations: 1 in 5 000 bags misplaced 80 % claims honored 1 in 10 000 bags damaged Duress operations: 1 in 1 000 bags misplaced 1 in 2 000 bags damaged 60 % claims honored ／ 正常运行：每 5 000 件行李中有 1 件错运；80 % 的索赔得到受理；每 10 000 件行李中有 1 件损坏；受压运行：每 1 000 件行李中有 1 件错运；每 2 000 件行李中有 1 件损坏；60 % 的索赔得到受理 |

### C.5 Enterprise architecture evaluation 企业架构评估

#### C.5.1 Situation 情形

The enterprise has developed a new strategic plan. The enterprise architecture (EA) was revised to address the strategic goals and objectives in the plan and to align with the new strategic initiatives. The EA is now aligned with the strategic plan but its impact on existing programs needs to be assessed to determine necessary changes to program budgets and schedules. The corporate portfolio management process will be performed to realign the portfolio of programs, projects, technologies and systems. The architecture evaluation process is used to provide data for use during the portfolio realignment. The stakeholder concerns in Table C.13 are deemed to be relevant.

该企业制定了新的战略计划。为使企业架构（EA）处理该计划中的战略目的与目标，并与其新的战略举措保持一致，对企业架构作了修订。EA 现已与战略计划保持一致，但仍需评定其对现有项目群的影响，以确定项目群预算与进度所需作出的变更。将执行企业项目组合管理过程，以重新调整项目群、项目、技术与系统的项目组合。架构评估过程用于提供数据，供项目组合重新调整期间使用。表 C.13 中的利益相关方关注点被认为具有相关性。

**Table C.13 — Enterprise architecture — Stakeholder concerns**

**表 C.13 — 企业架构 — 利益相关方关注点**

| Stakeholder ／ 利益相关方 | Concerns ／ 关注点 |
| --- | --- |
| Chief executive officer ／ 首席执行官 | Programs are in alignment with the new strategic goals and objectives ／ 项目群与新的战略目的与目标保持一致 |
| Chief information officer ／ 首席信息官 | Impact of new EA on cyber threat posture and cyber initiatives ／ 新的 EA 对网络威胁态势与网络举措的影响 |
| Program manager ／ 项目群经理 | Cost and schedule impact on baselined program plans; increased risk of program execution ／ 对已基线化的项目群计划的成本与进度影响；项目群执行风险的增加 |
| Enterprise operations ／ 企业运营 | Improved customer satisfaction; improved profit margins ／ 客户满意度提升；利润率提升 |

#### C.5.2 Enterprise architecture — Evaluation synthesis 企业架构 — 评估综合

**Table C.14 — Enterprise architecture — Evaluation synthesis**

**表 C.14 — 企业架构 — 评估综合**

| Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Evaluation synthesis approach ／ 评估综合途径 | Results ／ 结果 |
| --- | --- | --- | --- |
| Align programs with strategic plan ／ 使项目群与战略计划保持一致 | Enterprise capability gaps Enterprise capability overlaps Synergy with business partners Marketplace coverage ／ 企业能力差距；企业能力重叠；与业务伙伴的协同；市场覆盖 | — Review panel consisting of program managers ／ — 由项目群经理组成的评审专家组 | Review panel report to architecture governance board Business impact summary to board & shareholders Customer impact summary to board ／ 评审专家组向架构治理委员会提交报告；向董事会与股东提交业务影响摘要；向董事会提交客户影响摘要 |
| Improve cyber threat resilience ／ 提升网络威胁韧性 | Threat identification Threat countermeasure effectiveness Threat damage recovery Overall operational uptime ／ 威胁识别；威胁对策有效性；威胁损害恢复；总体运行的正常运行时间 | — Model walkthrough by cyber domain experts ／ — 由网络域专家进行的模型走查 | — Cyber domain working group report to chief information officer and to architecture governance board ／ — 网络域工作组向首席信息官和架构治理委员会提交报告 |
| Improve customer satisfaction ／ 提升客户满意度 | Time to market Feature quality Ease of use Low cost operations ／ 上市时间；特性质量；易用性；低成本运营 | — System experiments to emulate new features in the revised EA ／ — 用以模拟修订后 EA 中新特性的系统实验 | Board visit to system lab to witness customer engagement and observe reactions Customer survey report to architecture governance board ／ 董事会走访系统实验室，以见证客户参与并观察反应；向架构治理委员会提交客户调查报告 |

#### C.5.3 Enterprise architecture — Value assessment 企业架构 — 价值评定

**Table C.15 — Enterprise architecture — Value assessment**

**表 C.15 — 企业架构 — 价值评定**

| Value aspect being assessed ／ 被评定的价值方面 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Value assessment method ／ 价值评定方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Enterprise viability ／ 企业存续能力 | Align programs with strategic plan ／ 使项目群与战略计划保持一致 | EA-program plan disconnects Business partner dependencies ／ EA 与项目群计划之间的脱节；业务伙伴依赖关系 | — Business impact assessment ／ — 业务影响评定 | — Business impact assessment report to review panel ／ — 向评审专家组提交业务影响评定报告 |
| Assured customer deliveries ／ 有保证的客户交付 | Improve cyber threat resilience ／ 提升网络威胁韧性 | Threat damage impacts Threat response impacts Overall operational uptime ／ 威胁损害影响；威胁响应影响；总体运行的正常运行时间 | — Mission impact assessment ／ — 使命影响评定 | — Mission impact assessment report to cyber working group ／ — 向网络工作组提交使命影响评定报告 |
| Meeting profit targets ／ 实现利润目标 | Improve customer satisfaction ／ 提升客户满意度 | Time to market Feature quality Ease of use Low cost operations ／ 上市时间；特性质量；易用性；低成本运营 | — Customer focus groups with follow-on surveys ／ — 客户焦点小组及后续调查 | — Customer reaction report to program managers and to architecture governance board ／ — 向项目群经理和架构治理委员会提交客户反应报告 |

#### C.5.4 Enterprise architecture — Architectural analysis 企业架构 — 架构分析

**Table C.16 — Enterprise architecture — Architectural analysis**

**表 C.16 — 企业架构 — 架构分析**

| Object being analyzed ／ 被分析的对象 | Objectives ／ 目标 | Factors & subfactors ／ 因素与子因素 | Architectural analysis method ／ 架构分析方法 | Results ／ 结果 |
| --- | --- | --- | --- | --- |
| Programs and projects ／ 项目群与项目 | Align programs with strategic plan ／ 使项目群与战略计划保持一致 | Development cost & schedule Field support costs Program risks and opportunities ／ 开发成本与进度；现场保障成本；项目群风险与机遇 | Cost analysis Schedule analysis Risk analysis ／ 成本分析；进度分析；风险分析 | Revised program budgets & schedules Revised risk list and risk mitigation plans ／ 修订后的项目群预算与进度；修订后的风险清单与风险缓解计划 |
| None. No analysis is needed since assessment method above generates its own information to complete the assessment ／ 无。由于上述评定方法自行生成完成评定所需的信息，因此无需进行分析 | Improve cyber threat resilience ／ 提升网络威胁韧性 | — N/A ／ — 不适用 | — N/A ／ — 不适用 | — N/A ／ — 不适用 |
| None. No analysis is needed since assessment method above generates its own information to complete the assessment ／ 无。由于上述评定方法自行生成完成评定所需的信息，因此无需进行分析 | Improve customer satisfaction ／ 提升客户满意度 | — N/A ／ — 不适用 | — N/A ／ — 不适用 | — N/A ／ — 不适用 |

## Annex D (informative) — Example architecture evaluation frameworks ｜ 附录 D（资料性）— 示例架构评估框架

### D.1 General 总则

Example architecture evaluation frameworks are provided to illustrate how this document can be applied. This does not imply endorsement of these particular examples. The following examples are provided:

提供示例架构评估框架是为了说明本文件可如何应用。这并不意味着对这些特定示例的认可。所提供示例如下：

- Architecture Tradeoff Analysis Method (ATAM);

- 架构权衡分析方法（ATAM）；

- Quality Assessment of System Architectures and their Requirements (QUASAR); and

- 系统架构及其需求的质量评定（QUASAR）；以及

- Analysis of Alternatives (AoA).

- 备选方案分析（AoA）。

### D.2 Architecture Tradeoff Analysis Method (ATAM) 架构权衡分析方法（ATAM）

#### D.2.1 Overview 概述

##### D.2.1.1 General 总则

Architecture Tradeoff Analysis Method® [ATAM®2)], as described in Reference [59] is a framework for software architecture and design trade-offs. However, ATAM is also used for evaluating architectures of software-reliant systems relative to business and quality goals and for analysis of how those goals trade off against each other.

如参考文献 [59] 所述，架构权衡分析方法® [ATAM®2)] 是用于软件架构与设计权衡的框架。然而，ATAM 也用于针对业务与质量目的，评估依赖软件的系统的架构，并用于分析这些目的彼此之间如何权衡。

In the ATAM framework, quality attributes such as performance, availability, security and modifiability are derived from business drivers in order to express how software and system properties can sustain business goals.

在 ATAM 框架中，性能、可用性、信息安全、可修改性等质量属性由业务驱动因素导出，以表达软件与系统特性如何支撑业务目的。

> **NOTE 1** As summarized in Table D.1, the main ATAM concepts map to architecture evaluation concepts as defined in this document.

> **注 1**：如表 D.1 所汇总，ATAM 的主要概念映射到本文件所定义的架构评估概念。

**Table D.1 — Mapping of the main ATAM concepts**

**表 D.1 — ATAM 主要概念的映射**

| ATAM concepts ／ ATAM 概念 | Concepts as defined in this document ／ 本文件所定义的概念 |
| --- | --- |
| Business goal ／ 业务目的 | Concern ／ 关注点 |
| Business objective ／ 业务目标 | Evaluation objective ／ 评估目标 |
| Business driver ／ 业务驱动因素 | Evaluation factor ／ 评估因素 |
| Architecture quality ／ 架构质量 | Assessment objective ／ 评定目标 |
| Risk and non-risk ／ 风险与非风险 | Assessment factors ／ 评定因素 |
| Sensitivity point Tradeoff point ／ 敏感点、权衡点 | Assessment factors ／ 评定因素 |
| Quality factor ／ 质量因素 | Analysis factors ／ 分析因素 |

2) ATAM and Architecture Tradeoff Analysis Method are registered trademarks of Carnegie Mellon University. This information is given for the convenience of users of this document and does not constitute an endorsement by ISO, IEC or IEEE of the method named.

2) ATAM 与 Architecture Tradeoff Analysis Method 是卡内基梅隆大学的注册商标。提供此信息是为便于本文件的用户使用，并不构成 ISO、IEC 或 IEEE 对所涉方法的认可。

##### D.2.1.2 Purpose 目的

The purpose of the ATAM is to evaluate architectures in light of quality attribute requirements through business drivers with regard to business goals. Sensitivity points and trade-off points are formalized by ATAM evaluations which expose architectural risks that potentially inhibit the achievement of business goals of an organization. These evaluations can be executed at different life-cycle stages of the architecture and the system of interest it targets.

ATAM 的目的是依据质量属性要求，经由业务驱动因素并针对业务目的来评估架构。ATAM 评估将敏感点与权衡点形式化，从而揭示可能妨碍组织实现其业务目的的架构风险。这些评估能在架构及其所针对的所关注系统的不同生存周期阶段执行。

##### D.2.1.3 Basic approach 基本途径

An ATAM evaluation examines an architecture in terms of quality attributes about the suitability of the architecture for the system for which it was designed to formulate one or more evaluation objectives. Suitability begins with an understanding of the business drivers: What business goals are most central to guarantee the system is fit for purpose and it motivates the system quality attributes? Examples of categories of objectives extracted from actual ATAM evaluations are described in Reference [60]: reduce total cost of ownership, improve capability/quality of system, improve market position, support improved business processes and improve confidence in and perception of the system. The evaluation factors include cost, schedule, quality and risk to achieving the objectives.

ATAM 评估从质量属性方面考察某一架构对于其所为之设计的系统的适合性，以形成一个或多个评估目标。适合性始于对业务驱动因素的理解：哪些业务目的对于保证系统切合用途最为核心，并驱动系统的质量属性？参考文献 [60] 描述了从实际 ATAM 评估中提取的目标类别示例：降低总拥有成本、提升系统能力／质量、改善市场地位、支持改进的业务过程，以及提升对系统的信心与认知。评估因素包括成本、进度、质量以及实现目标的风险。

##### D.2.1.4 Conceptual flow 概念流程

As illustrated in Figure D.1, business drivers and the architecture are elicited from project decision makers. These are refined into scenarios and the architectural decisions made in support of each one. Analysis of scenarios and decisions results in identification of risks, non-risks, sensitivity points and trade-off points in the architecture. Risks are synthesized into a set of risk themes, showing how each one threatens a business driver.

如图 D.1 所示，业务驱动因素与架构是从项目决策者那里引出的。这些内容被细化为场景，以及为支持每一场景而作出的架构决策。对场景与决策的分析导致识别出架构中的风险、非风险、敏感点与权衡点。风险被综合为一组风险主题，表明每一风险主题如何威胁某一业务驱动因素。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure D.1 — A conceptual flow of the ATAM**

**图 D.1 — ATAM 的概念流程**

##### D.2.1.5 Sequence of steps 步骤顺序

The project starts with preliminary steps:

项目从若干预备步骤开始：

- Present the ATAM. The evaluation leader describes the evaluation method to the participants, sets expectations and answers questions.

- 介绍 ATAM。评估负责人向参与者描述该评估方法，设定预期并回答问题。

- Present business drivers. A project spokesperson describes what business goals are motivating the development effort and hence what will be the architectural drivers.

- 介绍业务驱动因素。项目发言人描述哪些业务目的在驱动开发工作，从而说明什么将成为架构驱动因素。

- Present architecture. The architect describes the architecture, focusing on how it addresses the

- 介绍架构。架构师描述该架构，着眼于其如何处理

business drivers.

业务驱动因素。

- Identify architectural approaches. The architect identifies architectural approaches. The evaluation activities are conducted in a series of steps:

- 识别架构途径。架构师识别架构途径。评估活动按一系列步骤开展：

- Generate quality attribute utility tree. The evaluation team elicits quality factors that comprise system "utility" from the architecture team.

- 生成质量属性效用树。评估团队从架构团队那里引出构成系统“效用”的质量因素。

- Analyze architectural approaches. Architectural approaches that address the high-priority factors are analyzed. Architectural risks, non-risks, sensitivities and trade-offs are identified.

- 分析架构途径。对处理高优先级因素的架构途径进行分析。识别架构风险、非风险、敏感性与权衡。

- Brainstorm and prioritize scenarios. The evaluation team elicits a larger set of scenarios from the entire group of stakeholders.

- 头脑风暴并排定场景优先级。评估团队从全部利益相关方那里引出更大的一组场景。

- Analyze architectural approaches. Architectural approaches that address the highly-ranked scenarios are analyzed. These scenarios are test cases to confirm the analysis performed thus far.

- 分析架构途径。对处理高排序场景的架构途径进行分析。这些场景是用于确认迄今所作分析的测试用例。

- Present results. The evaluation team presents the findings to the stakeholders.

- 介绍结果。评估团队向利益相关方介绍各项发现。

##### D.2.1.6 Expected results 预期结果

The primary evaluation result is the collection of risk themes that group related risks and summarize their impact on the architecture and the business drivers. Other outputs include the artifacts created or refined to conduct the analysis (e.g., architectural approaches, utility tree, scenarios) and the detailed analysis results (e.g., risks, non-risks, sensitivity points and trade-offs points).

主要评估结果是风险主题的汇集，这些主题将相关风险归组，并汇总其对架构与业务驱动因素的影响。其他输出包括为开展分析而创建或细化的人工制品（例如架构途径、效用树、场景）以及详细的分析结果（例如风险、非风险、敏感点与权衡点）。

> **NOTE 2** Risk themes extracted from ATAM evaluations are described in Reference [61].

> **注 2**：参考文献 [61] 描述了从 ATAM 评估中提取的风险主题。

#### D.2.2 Evaluation synthesis 评估综合

ATAM is an architecture evaluation approach focusing on architecture quality. Considered evaluation objectives are business objectives derived from business goals. And business drivers are evaluation factors.

ATAM 是一种着眼于架构质量的架构评估途径。所考虑的评估目标是源自业务目的的业务目标。而业务驱动因素是评估因素。

An evaluation synthesis can involve the combination of results from one or several value assessments where ATAM is one of those value assessments performed to determine to what extent the evaluation objectives (for the entire AE effort) will be achieved. This could involve an examination of trade-offs between the results from the different value assessments.

评估综合可涉及将一项或多项价值评定的结果组合起来，其中 ATAM 即为这些价值评定之一，用以确定（整个 AE 工作的）评估目标将在多大程度上得以实现。这可能涉及考察不同价值评定结果之间的权衡。

#### D.2.3 Value assessment 价值评定

Value assessment in ATAM determines the extent to which architectural quality addresses the business goals from the system properties point of view: What are the quality attributes that motivate or influence the architecture? What are the desired results for these attributes to meet business and quality goals?

ATAM 中的价值评定从系统特性的角度确定架构质量处理业务目的的程度：哪些质量属性驱动或影响该架构？为满足业务目的与质量目的，这些属性应达到何种期望结果？

The assessment method is the scenario-based ATAM technique called “Analyze Architectural Approaches”. The method analyzes how well the architecture decisions meet the needs identified in prioritized scenarios that can occur during the lifecycle of the system. Given the high priority factors, the evaluation team elicits and analyzes the architectural approaches that address those factors. For example, an architectural approach aimed at meeting modifiability goals will be subjected to modifiability analysis. The evaluation team records the discussion surrounding the architectural decision, risks, non-risks, sensitivities, trade-offs and open issues.

评定方法是名为“分析架构途径”的基于场景的 ATAM 技术。该方法分析架构决策在多大程度上满足已排定优先级的场景中所识别的需要，这些场景能在系统的生存周期期间发生。给定高优先级因素，评估团队引出并分析处理这些因素的架构途径。例如，旨在满足可修改性目标的架构途径将接受可修改性分析。评估团队记录围绕架构决策、风险、非风险、敏感性、权衡与未决问题的讨论。

> **NOTE** Analyze Architectural Approaches is not quality-attribute specific with specific criteria in the form of questions “embedded” in the technique. Any quality attribute can be analyzed.

> **注**：“分析架构途径”并不特定于质量属性，该技术中并未“嵌入”以问题形式给出的特定准则。任何质量属性都能分析。

The primary assessment result is the collection of potentially problematic architectural decisions that put the stakeholder needs at risk and how they trade-off against each other.

主要评定结果是汇集那些可能存在问题、使利益相关方需要面临风险的架构决策，并说明它们彼此之间如何权衡。

For value assessment, risks, non-risks, sensitivity points and trade-off points can be considered as assessment factors.

对于价值评定，风险、非风险、敏感点与权衡点能被视作评定因素。

The focus is on the quality attributes of interest to a stakeholder and related quality attributes that are involved in trade-offs. The quality attributes are represented as a six-part scenario that is used to represent stakeholders’ interests, understand the requirements and provide the context and measure against which to analyze decisions. The six parts of a quality attribute scenario are: source, stimulus, artifact, environment, response and response measure.

着眼点在于利益相关方所关注的质量属性，以及参与权衡的相关质量属性。质量属性表示为六部分场景，用以表示利益相关方的利益、理解需求，并提供据以分析决策的语境与度量。质量属性场景的六个部分是：来源、刺激、人工制品、环境、响应与响应度量。

An example modifiability scenario is: A developer wishes to change the UI during design time; the change is made and unit tested in three hours. Another example, a performance scenario, is: Users initiate transactions during normal operation; the transactions are processed with an average latency of two seconds. The values obtained in these scenarios support the evaluation objectives such as the business goals to enter new markets and reduce time to market.

一个可修改性场景的示例是：开发者在设计时希望更改 UI；该更改在三小时内完成并通过单元测试。另一个示例是性能场景：用户在正常运行期间发起交易；这些交易以两秒的平均延迟得到处理。这些场景中获得的值支持诸如进入新市场与缩短上市时间等业务目的所对应的评估目标。

#### D.2.4 Architectural analysis 架构分析

Architectural analysis in ATAM examines the key attributes of the architecture along dimensions of quality such as availability, interoperability, modifiability, performance, security, testability and usability. The analysis factors are the response measure part of the six-part quality attribute scenario, such as latency, effort or time to repair in the case of performance, modifiability and availability.

ATAM 中的架构分析按可用性、互操作性、可修改性、性能、信息安全、可测试性和易用性等质量维度考察架构的关键属性。分析因素是六部分质量属性场景中的响应度量部分，例如在性能、可修改性和可用性的情形下为时延、工作量或修复时间。

ATAM doesn’t stipulate an analysis method. It brings together the necessary stakeholders to focus on a particular concern in a part of the system. The evaluation team may employ lightweight analysis techniques such as reflective questions, architectural tactics-based questionnaires, design-based checklists and quality attribute scenario-based analysis. Questions probe architectural decisions that bear on quality attribute requirements. For example, if the quality attribute of interest is performance then a question might be: How are priorities assigned to processes? If the quality attribute of interest is modifiability, then a question might be: Are there any places where layers are circumvented? The architect may have gathered the necessary information prior to the evaluation and present it as supporting evidence.

ATAM 并不规定分析方法。它汇集必要的利益相关方，聚焦于系统某一部分中的特定关注点。评估团队可采用轻量级分析技术，如反思性问题、基于架构策略的问卷、基于设计的检查表和基于质量属性场景的分析。所提问题探查那些影响质量属性要求的架构决策。例如，若所关注的质量属性是性能，则可提出这样的问题：如何为各进程分配优先级？若所关注的质量属性是可修改性，则可提出这样的问题：是否存在绕过层次的地方？架构师可在评估之前收集必要信息，并将其作为支撑证据呈现。

The responses will be evaluated in terms of how the decisions impact the execution of the scenario (e.g., two second latency, making changes within three hours) to inform the analysis result.

将依据这些决策对场景执行的影响（如 2 秒时延、在三小时内作出更改）来评估各项回应，从而为分析结果提供依据。

The analysis result is compared with the expected response to determine whether the stakeholder concerns associated with each quality attribute are satisfied or at risk. This assessment result in turn influences the evaluation result as risks are distilled into risk themes that impact the architecture and business drivers.

将分析结果与预期响应相比较，以确定与每个质量属性相关的利益相关方关注点是得到满足还是存在风险。该评定结果又会影响评估结果，因为风险被提炼为影响架构与业务驱动因素的风险主题。

> **NOTE** Quality attributes extracted for ATAM evaluations are described in Reference [62].

> **注**：为 ATAM 评估提取出的质量属性在参考文献 [62] 中描述。

#### D.2.5 Evaluation plan and report 评估计划与报告

The ATAM process contains the guidance and aids needed to produce an evaluation plan and carry out an actual evaluation. Before the analysis can begin, a setup phase is conducted in which the evaluation team is created and a partnership is formed between the evaluation team and the project whose architecture is being evaluated.

ATAM 过程包含编制评估计划并开展实际评估所需的指南与辅助手段。在分析能够开始之前，先实施筹备阶段；在该阶段组建评估团队，并在评估团队与架构正被评估的项目之间建立伙伴关系。

The ATAM process provides guidance for producing an architecture evaluation report in the form of a presentation and a document. The presentation is a required artifact and its presentation to all stakeholders is a required step in the evaluation. The presentation recapitulates the steps of the ATAM evaluation and presents the outputs, including: business drivers, architectural approaches, utility tree, scenarios, risks and non-risks, sensitivities and tradeoffs and risk themes. The final report includes the outputs documented in the presentation as well as: an executive summary, more detailed description of the analysis and next steps. The evaluation team also reflects on the quality of the evaluation and recommends improvements to the ATAM materials.

ATAM 过程提供以演示和文档两种形式编制架构评估报告的指南。演示是必需的人工制品，而向全体利益相关方作该演示是评估中的必需步骤。该演示概述 ATAM 评估的各个步骤，并呈现各项输出，包括：业务驱动因素、架构途径、效用树、场景、风险与非风险、敏感点与权衡以及风险主题。最终报告既包含演示中所记录的各项输出，还包含：执行摘要、对分析更详细的描述以及后续步骤。评估团队还反思评估的质量，并对 ATAM 材料提出改进建议。

> **NOTE** ATAM plan and report are documented in Reference [63].

> **注**：ATAM 计划与报告记录在参考文献 [63] 中。

### D.3 The Method Framework and QUASAR method 方法框架与 QUASAR 方法

#### D.3.1 Overview 概述

The Method Framework for Engineering System Architectures (MFESA)[64] is a framework that enables systems architects and engineers to create methods for systems architectures. The framework comprises:

系统工程架构方法框架（MFESA）[64] 是一个使系统架构师和工程师能够为系统架构创建方法的框架。该框架由以下部分构成：

- an ontology of concepts and terminology;

- 概念与术语的本体；

- a metamodel of the types of method elements (components);

- 方法元素（构件）类型的元模型；

- a repository containing reusable method components together with reusable methods constructed from such method components; and

- 一个储存库，其中包含可复用的方法构件，以及由这些方法构件构造出的可复用方法；以及

- a metamethod for creating project-specific methods for systems architecting.

- 一种用于为系统架构工作创建项目特定方法的元方法。

QUality Assessment of System Architectures and their Requirements (QUASAR) is a method that can be used in conjunction with MFESA.

系统架构及其要求的质量评定（QUASAR）是一种能与 MFESA 结合使用的方法。

#### D.3.2 Evaluation synthesis 评估综合

In fulfilment of part of one of the MFESA processes the QUASAR method[65][66] can be used to assess the quality of system architectures and their associated architecturally significant quality requirements. Whilst functional requirements satisfaction is handled by many requirements engineering (including requirements management) techniques, coverage of satisfaction of non-functional requirements (sometimes termed ‘ilities’) is generally not so well addressed, especially as they shift from external to internal and then a technical focus during system development.

为履行 MFESA 其中某一过程的部分内容，能使用 QUASAR 方法[65][66]评定系统架构及其相关的、具有架构意义的质量要求的质量。功能需求的满足由许多需求工程（包括需求管理）技术来处理，而对非功能需求（有时称为“ilities”）满足情况的覆盖通常处理得不够好，尤其是当这些需求在系统开发期间由外部关注转为内部关注、再转为技术关注时。

QUASAR is based on the:

QUASAR 基于以下各项：

- production of requirements and architecture quality cases as an intrinsic part of requirements engineering and systems architecting; and

- 编制要求与架构的质量情形，作为需求工程与系统架构工作的固有组成部分；以及

- independent assessment of these quality cases by assessment teams staffed by people who are trained and experienced in the requisite technical disciplines.

- 由评定团队对这些质量情形进行独立评定，评定团队配备的是在所需技术学科方面受过培训并有经验的人员。

#### D.3.3 Value assessment 价值评定

The quality of a system is based upon a quality model comprising quality characteristics, quality attributes and measurement scales and methods. QUASAR may be applied at different system tiers and can assess quality from both external and internal perspectives.

系统的质量以质量模型为基础，该模型由质量特性、质量属性和测量标度与方法构成。QUASAR 可应用于不同的系统层级，并能从外部与内部两种视角评定质量。

The characteristics which can be assessed include:

能够评定的特性包括：

- external quality characteristics such as compliance, configurability, dependability, efficiency, environmental compatibility, functionality, habitability, interoperability, operability, serviceability and usability;

- 外部质量特性，如合规性、可配置性、可信性、效率、环境兼容性、功能性、可居住性、互操作性、可操作性和易用性；

- internal quality characteristics such as feasibility, interoperability, portability, producibility, reusability, modifiability (including maintainability) and testability; and

- 内部质量特性，如可行性、互操作性、可移植性、可生产性、可复用性、可修改性（包括可维护性）和可测试性；以及

- performance (quality) attributes such as jitter, latency, response time, schedulability and throughput.

- 性能（质量）属性，如抖动、时延、响应时间、可调度性和吞吐量。

#### D.3.4 Architectural analysis 架构分析

In QUASAR[65][66] the achievement of quality is described in quality cases which are based on a generalization of safety/assurance cases and are formed from the recording of quality claims concerning the satisfaction of quality goals and non-functional requirements supported by clear and compelling arguments and sufficient and credible evidence. They are restricted to the level of detail appropriate for a system architecture description and the arguments may be simplified as compared with those used in safety/assurance cases.

在 QUASAR[65][66] 中，质量的达成在质量情形中描述；质量情形以安全／保障情形的推广为基础，由质量主张的记录构成，这些主张关乎质量目标与非功能需求的满足情况，并以清晰有力、令人信服的论证以及充分可信的证据为支撑。质量情形限于适合系统架构描述的详细程度；与安全／保障情形中所用的论证相比，其论证可以简化。

The quality characteristics and attributes which are to be assessed may be structured by tiering these quality factors (as requirements cases) or by relating them to specific system entities such as subsystems, with the former approach being preferred. This can be achieved through structuring of the corresponding claims. Each of the leaf node quality factors can then be assessed based on the formulation of a specific claim.

将要评定的质量特性与质量属性，可以通过将这些质量因素分层（作为要求情形）来结构化，也可以通过将之与子系统等特定系统实体相关联来结构化，其中前一种途径更可取。这可以通过对相应主张的结构化来实现。随后，每个叶节点质量因素都能基于特定主张的表述来评定。

Assessors probe the quality cases for their weaknesses and potential risk, and the structuring of the quality characteristics and attributes for their veracity. The assessors determine assessment results and provide corresponding reports.

评定人员探查质量情形的弱点与潜在风险，并探查质量特性与质量属性结构化方式的真实性。评定人员确定评定结果并提供相应报告。

Figure D.2 below shows how QUASAR and the associated structuring of quality characteristics and attributes conforms with the architecture evaluation framework tiers as defined in this document.

下面的图 D.2 示出 QUASAR 以及相关的质量特性与质量属性结构化方式如何与本文件所定义的架构评估框架层级相符合。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure D.2 — Correspondence of QUASAR concepts with those advocated in this document**

**图 D.2 — QUASAR 概念与本文件所主张概念的对应关系**

#### D.3.5 Evaluation plan and report 评估计划与报告

QUASAR[65][66] says nothing about the evaluation plan and report.

QUASAR[65][66] 未涉及评估计划与报告。

### D.4 Analysis of Alternatives (AoA) 备选方案分析（AoA）

#### D.4.1 Overview 概述

##### D.4.1.1 General 总则

Analysis of Alternatives (AoA) study is an approach applied in the United States as a requirement of military acquisition policy. The approach is documented in the AoA Handbook[58] published by the Office of Aerospace Studies at the Air Force Materiel Command. The AoA study ensures that at least three feasible alternatives are analyzed prior to making costly investment decisions. The AoA establishes and benchmarks metrics for Cost, Schedule, Performance (CSP) and Risk (CSPR) depending on military "needs" derived from the Joint Capabilities Integration Development System process. It moves away from employing a single acquisition source to the exploration of multiple alternatives so agencies have a basis for funding the best possible projects in a rational, defensible manner considering risk and uncertainty.

备选方案分析（AoA）研究是美国作为军事采办政策的一项要求而采用的一种途径。该途径记录在由空军装备司令部航空航天研究办公室发布的《AoA 手册》[58] 中。AoA 研究确保在作出代价高昂的投资决策之前，至少对三个可行备选方案进行分析。AoA 依据由联合能力集成与开发系统过程导出的军事“需要”，为成本、进度、性能（CSP）与风险（CSPR）确立度量指标并建立基准。它从采用单一采办来源转向探索多个备选方案，从而使各机构有依据以合理、可辩护的方式并考虑风险与不确定性，为尽可能最佳的项目提供经费。

##### D.4.1.2 Basic approach 基本途径

The AoA is designed to examine a broad spectrum of potential alternatives to the mission need described in a Mission Needs Statement. The key purpose of the AoA is to identify a "solution" that will fulfil the stated requirements as optimally as possible commensurate with established cost and schedule constraints, at the lowest practicable risk. The "solution" may be a specific design or configuration but it is more than likely to be a set of design parameter values the combination of which would provide the optimal and most desirable means of fulfilling the stated requirements. Thus, any specific design that complies with the optimal "solution" parameter values is deemed acceptable. Value is measured in terms of effectiveness (MOEs) and suitability (MOSs).

AoA 旨在考察任务需要说明书中所述任务需要的广泛潜在备选方案。AoA 的关键目的是识别出一种“解决方案”，使其在与既定成本与进度约束相称的条件下尽可能最优地满足所述要求，且风险为切实可行的最低。“解决方案”可以是一个具体的设计或配置，但更可能是一组设计参数值，其组合将提供满足所述要求的最优且最合意的手段。因此，任何符合最优“解决方案”参数值的具体设计都被认为可接受。价值以效能（MOEs）和适用性（MOSs）来度量。

##### D.4.1.3 Study objectives 研究目标

The objectives of the AoA are to:

AoA 的目标是：

1) refine alternatives;

1) 细化备选方案；

2) refine criteria;

2) 细化准则；

3) refine evaluation;

3) 细化评估；

4) work to gain consensus;

4) 努力达成共识；

5) reduce uncertainty; and

5) 减少不确定性；以及

6) choose an alternative.

6) 选定一个备选方案。

##### D.4.1.4 Maturity assessment 成熟度评定

The AoA assesses critical technology elements (CTEs) associated with each proposed materiel solution, identified in the Initial Capabilities Document (ICD), including: technology maturity, integration risk, manufacturing feasibility and, where necessary, technology maturation and demonstration needs.

AoA 评定与每个拟议物质解决方案相关的关键技术要素（CTE），这些要素在初始能力文件（ICD）中识别，包括：技术成熟度、集成风险、制造可行性，以及在必要时技术成熟与演示需要。

##### D.4.1.5 Risk assessment 风险评定

Risk is analyzed in many ways, such as technological maturity, manufacturing capacity, quality standards, manufacturing design, material and supply chain capacity, interoperability, operational survival, aggressiveness of the schedule, cost reasonableness, among many others. Each MOE and capability can carry an associated risk.

风险以多种方式分析，包括技术成熟度、制造能力、质量标准、制造设计、材料与供应链能力、互操作性、作战生存性、进度的激进程度、成本合理性等众多方面。每项 MOE 和每项能力都可带有相关的风险。

#### D.4.2 Evaluation synthesis 评估综合

AoA is an approach for performing the synthesis of possibly multiple value assessment methods that are conducted under the umbrella of the overall assessment of architectural alternatives. Various evaluation approaches could be used during an AoA:

AoA 是一种途径，用于综合可能在架构备选方案总体评定这一总体框架下开展的多种价值评定方法。在 AoA 期间能使用各种评估途径：

- expert review panel;

- 专家评审组；

- prototype demonstration;

- 原型演示；

- system experiment;

- 系统实验；

- modeling and simulation;

- 建模与仿真；

- model walkthrough;

- 模型走查；

- technical analysis;

- 技术分析；

- concept review; or

- 概念评审；或

- user symposium.

- 用户研讨会。

> **NOTE** Only modeling and simulation and technical analysis are described in the AoA Handbook, although these other approaches are often used.

> **注**：《AoA 手册》中只描述了建模与仿真和技术分析，尽管这些其他途径常被使用。

An evaluation synthesis involves the combination of results from multiple value assessments to determine to what extent the evaluation objectives (for the entire AoA effort) will be achieved. This could involve an examination of trade-offs between the results from the different value assessments.

评估综合涉及将多项价值评定的结果组合起来，以确定（对于整个 AoA 工作而言的）评估目标将在多大程度上得以实现。这可能涉及考察不同价值评定结果之间的权衡。

#### D.4.3 Value assessment 价值评定

Measures of Effectiveness (MOEs) and Measures of Suitability (MOSs) are associated with relevant mission tasks as exemplified in Table D.2.

效能度量（MOEs）与适用性度量（MOSs）与相关任务相关联，如表 D.2 所示例。

**Table D.2 — Example of mission tasks and associated measures**

**表 D.2 — 任务与相关度量的示例**

| Mission task ／ 任务 | Measures of Effectiveness ／ 效能度量 |
| --- | --- |
| Defeat target ／ 击败目标 | MOE 1.1: Probability of kill ／ MOE 1.1：杀伤概率 |
| Defeat target ／ 击败目标 | MOE 1.2: Number of weapons to defeat target ／ MOE 1.2：击败目标所需武器数量 |
| Defeat target ／ 击败目标 | MOE 1.3: Range ／ MOE 1.3：射程 |
| Defeat target ／ 击败目标 | MOE 1.4: Collateral damage ／ MOE 1.4：附带损伤 |
| Survive threat ／ 在威胁下生存 | MOE 2.1: Time to launch ／ MOE 2.1：发射时间 |
| Survive threat ／ 在威胁下生存 | MOE 2.2: Probability of survival ／ MOE 2.2：生存概率 |
| Survive threat ／ 在威胁下生存 | MOE 2.3: Counter threats ／ MOE 2.3：对抗威胁 |
| Support system ／ 保障系统 | MOS 3.1: Deployability ／ MOS 3.1：可部署性 |
| Support system ／ 保障系统 | MOS 3.2: Maintainability ／ MOS 3.2：可维护性 |
| Support system ／ 保障系统 | MOS 3.3: Mission reliability ／ MOS 3.3：任务可靠性 |

In AoA, value assessment is called effectiveness analysis and is focused on determination of MOEs and their respective values for alternative solutions with respect to the cost, schedule, risk and other factors for each alternative. However, usually the measures of suitability (MOSs) are also used in the value assessment. The general approach for effectiveness analysis is illustrated in Figure D.3.

在 AoA 中，价值评定称为效能分析，其重点在于针对每个备选方案的成本、进度、风险及其他因素，确定各备选方案的 MOE 及其相应取值。然而，适用性度量（MOSs）通常也用于价值评定。效能分析的一般途径如图 D.3 所示。

> **NOTE** ICD is Initial Capabilities Document, CDD is Capability Description Document.

> **注**：ICD 是初始能力文件，CDD 是能力描述文件。

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure D.3 — General approach for effectiveness analysis**

**图 D.3 — 效能分析的一般途径**

#### D.4.4 Architectural analysis 架构分析

The measures of value used during the effectiveness analysis are often reliant upon various performance analyses. Various Measures of Performance (MOPs) can be examined as the basis for the AoA’s architectural analysis, as illustrated in Table D.3.

效能分析期间所用的价值度量往往依赖于各种性能分析。能考察各种性能度量（MOPs）作为 AoA 架构分析的基础，如表 D.3 所示。

**Table D.3 — Measures of performance (MOP) framework example**

**表 D.3 — 性能度量（MOP）框架示例**

| Task ／ 任务 | Attribute ／ 属性 | Measure ／ 度量 | Metric ／ 度量指标 | Criteria ／ 准则 | Analysis method ／ 分析方法 |
| --- | --- | --- | --- | --- | --- |
| Enhance survivability ／ 增强生存性 | Survivability ／ 生存性 | Probability of survival ／ 生存概率 | Probability ／ 概率 | ≥0,85 | M&S (BRAWLER) ／ M&S（BRAWLER） |
| Enhance survivability ／ 增强生存性 | Conditions: ／ 条件： | Combat range (beyond and within threat detection range); engagement environment (contested, highly contested) ／ 交战距离（威胁探测距离之外与之内）；交战环境（争夺、激烈争夺） | Combat range (beyond and within threat detection range); engagement environment (contested, highly contested) ／ 交战距离（威胁探测距离之外与之内）；交战环境（争夺、激烈争夺） | Combat range (beyond and within threat detection range); engagement environment (contested, highly contested) ／ 交战距离（威胁探测距离之外与之内）；交战环境（争夺、激烈争夺） | Combat range (beyond and within threat detection range); engagement environment (contested, highly contested) ／ 交战距离（威胁探测距离之外与之内）；交战环境（争夺、激烈争夺） |
| Detect and identify threats ／ 探测与识别威胁 | Completeness ／ 完整性 | Number of threat detections ／ 威胁探测数量 | Percentage ／ 百分比 | ≥98 % of threats ／ ≥98 % 的威胁 | Parametric analysis ／ 参数分析 |
| Detect and identify threats ／ 探测与识别威胁 | Accuracy ／ 准确性 | Number of threat identifications ／ 威胁识别数量 | Percentage ／ 百分比 | ≥95 % unambigu-ous id of threats ／ ≥95 % 的威胁被无歧义识别 | Parametric analysis ／ 参数分析 |
| Detect and identify threats ／ 探测与识别威胁 | Conditions: ／ 条件： | Electronic signal density (high); emitter environment (red, blue, gray and white); threat classes (low to high priority) ／ 电子信号密度（高）；辐射源环境（红、蓝、灰、白）；威胁类别（低至高优先级） | Electronic signal density (high); emitter environment (red, blue, gray and white); threat classes (low to high priority) ／ 电子信号密度（高）；辐射源环境（红、蓝、灰、白）；威胁类别（低至高优先级） | Electronic signal density (high); emitter environment (red, blue, gray and white); threat classes (low to high priority) ／ 电子信号密度（高）；辐射源环境（红、蓝、灰、白）；威胁类别（低至高优先级） | Electronic signal density (high); emitter environment (red, blue, gray and white); threat classes (low to high priority) ／ 电子信号密度（高）；辐射源环境（红、蓝、灰、白）；威胁类别（低至高优先级） |
| Sustain and maintain ／ 维持与维护 | Availability ／ 可用性 | Operational availability (Ao) ／ 运行可用性（Ao） | Probability ／ 概率 | ≥0,98 | M&S (LCOM); expert elicitation ／ M&S（LCOM）；专家启发 |
| Sustain and maintain ／ 维持与维护 | Reliability ／ 可靠性 | Weapon system reliability ／ 武器系统可靠性 | Probability ／ 概率 | ≥0,98 | Comparative analysis; expert elicitation ／ 对比分析；专家启发 |
| Sustain and maintain ／ 维持与维护 | Conditions: ／ 条件： | Operations tempo (peacetime, wartime) ／ 作战节奏（平时、战时） | Operations tempo (peacetime, wartime) ／ 作战节奏（平时、战时） | Operations tempo (peacetime, wartime) ／ 作战节奏（平时、战时） | Operations tempo (peacetime, wartime) ／ 作战节奏（平时、战时） |

Table D.3 (continued)

表 D.3（续）

| Task ／ 任务 | Attribute ／ 属性 | Measure ／ 度量 | Metric ／ 度量指标 | Criteria ／ 准则 | Analysis method ／ 分析方法 |
| --- | --- | --- | --- | --- | --- |
| Deploy system ／ 部署系统 | Deployability ／ 可部署性 | Operator rating of ability to transport system ／ 操作人员对系统运输能力的评分 | Mode ／ 众数 | Operators can easily transport system ／ 操作人员能容易地运输系统 | Statistical analysis of operator responses to questionnaire items ／ 对操作人员问卷题项作答的统计分析 |
| Deploy system ／ 部署系统 | Conditions: ／ 条件： | Austere airfield environment; transport by C-130 aircraft ／ 简易机场环境；由 C-130 飞机运输 | Austere airfield environment; transport by C-130 aircraft ／ 简易机场环境；由 C-130 飞机运输 | Austere airfield environment; transport by C-130 aircraft ／ 简易机场环境；由 C-130 飞机运输 | Austere airfield environment; transport by C-130 aircraft ／ 简易机场环境；由 C-130 飞机运输 |

#### D.4.5 Evaluation plan and report 评估计划与报告

The AoA Handbook[58] provides a standardized template for the AoA plan and report.

《AoA 手册》[58] 为 AoA 计划与报告提供标准化模板。

## Bibliography 参考文献

1) ISO/IEC/IEEE 12207, Systems and software engineering — Software life cycle processes

1) ISO/IEC/IEEE 12207，系统与软件工程 — 软件生存周期过程

2) ISO/IEC 15026-1, Systems and software engineering — Systems and software assurance — Part 1:

2) ISO/IEC 15026-1，系统与软件工程 — 系统与软件保障 — 第 1 部分：

Concepts and vocabulary

概念与词汇

3) ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes

3) ISO/IEC/IEEE 15288，系统与软件工程 — 系统生存周期过程

4) ISO/IEC/IEEE 15289, Systems and software engineering — Content of life-cycle information items (documentation)

4) ISO/IEC/IEEE 15289，系统与软件工程 — 生存周期信息部件的内容（文档）

5) ISO 15704, Industrial automation systems — Requirements for enterprise-reference architectures and methodologies

5) ISO 15704，工业自动化系统 — 企业参考架构与方法论的要求

6) ISO/IEC 19501, Information technology — Open Distributed Processing — Unified Modeling Language (UML) Version 1.4.2

6) ISO/IEC 19501，信息技术 — 开放分布式处理 — 统一建模语言（UML）1.4.2 版

7) ISO/IEC 25000, Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Guide to SQuaRE

7) ISO/IEC 25000，系统与软件工程 — 系统与软件质量要求和评价（SQuaRE） — SQuaRE 指南

8) ISO/IEC 25010, Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models

8) ISO/IEC 25010，系统与软件工程 — 系统与软件质量要求和评价（SQuaRE） — 系统与软件质量模型

9) ISO/IEC 25012, Software engineering — Software product Quality Requirements and Evaluation (SQuaRE) — Data quality model

9) ISO/IEC 25012，软件工程 — 软件产品质量要求和评价（SQuaRE） — 数据质量模型

10) ISO/IEC 25020, Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Measurement reference model and guide

10) ISO/IEC 25020，系统与软件工程 — 系统与软件质量要求和评价（SQuaRE） — 测量参考模型与指南

11) ISO/IEC 25021, Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality measure elements

11) ISO/IEC 25021，系统与软件工程 — 系统与软件质量要求和评价（SQuaRE） — 质量度量元素

12) ISO/IEC 33001, Information technology — Process assessment — Concepts and terminology

12) ISO/IEC 33001，信息技术 — 过程评定 — 概念与术语

13) ISO/IEC/IEEE 42010:2011, Systems and software engineering — Architecture description

13) ISO/IEC/IEEE 42010:2011，系统与软件工程 — 架构描述

14) ISO/IEC/IEEE 42020:2019, Systems and software engineering — Architecture processes

14) ISO/IEC/IEEE 42020:2019，系统与软件工程 — 架构过程

15) Akao Yoji, 1990. Quality Function Deployment: Integrating Customer Requirements into

15) Akao Yoji, 1990. 质量功能展开：将顾客要求融入

Product Design, trans. by Glenn H. Mazur and Japan Business Consultants, Ltd., Productivity Press, Cambridge, MA, USA

产品设计, Glenn H. Mazur 与 Japan Business Consultants, Ltd. 译, Productivity Press, 美国马萨诸塞州剑桥

16) Clements Paul, Kazman Rick, Klein Mark, 2002. Evaluating Software Architectures: Methods and Case Studies, Addison-Wesley, Boston, MA, USA

16) Clements Paul, Kazman Rick, Klein Mark, 2002. 软件架构评估：方法与案例研究, Addison-Wesley, 美国马萨诸塞州波士顿

17) Greefhorst Danny, Proper Erik, Architecture Principles - The Cornerstones of Enterprise Architecture, 1st Edition, Springer, 2011

17) Greefhorst Danny, Proper Erik, 架构原则——企业架构的基石, 第 1 版, Springer, 2011

18) Greefhorst D., Proper E., “The Roles of Principles in Enterprise Architecture, http://archixl

18) Greefhorst D., Proper E., “原则在企业架构中的作用, http://archixl

.nl/files/tear2010_principles.pdf

.nl/files/tear2010_principles.pdf

19) Hilliard R., M. Kurland, S. Litvintchouk, T. Rice, and S. Schwarm. 1996. Architecture Quality Assessment Version 2.0. The MITRE Corp. http://web.mit.edu/richh/www/writings/aqa-v2.pdf.

19) Hilliard R., M. Kurland, S. Litvintchouk, T. Rice, 和 S. Schwarm. 1996. 架构质量评定 2.0 版. The MITRE Corp. http://web.mit.edu/richh/www/writings/aqa-v2.pdf.

20) Kazman R., Klein M., Mario R Barbacci, Tom Longstaff, Howard Lipson, and Jeromy Carriere. July 1998. The Architecture Tradeoff Analysis Method. Software Engineering Institute, CMU/SEI-98-TR-008, Software Engineering Institute, Pittsburgh, PA, USA. http://www

20) Kazman R., Klein M., Mario R Barbacci, Tom Longstaff, Howard Lipson, 和 Jeromy Carriere. 1998 年 7 月. 架构权衡分析方法. Software Engineering Institute, CMU/SEI-98-TR-008, Software Engineering Institute, 美国宾夕法尼亚州匹兹堡. http://www

.sei.cmu.edu/library/abstracts/reports/98tr008.cfm

.sei.cmu.edu/library/abstracts/reports/98tr008.cfm

21) Keeney R. L., 1996). Value-Focused Thinking: A Path to Creative Decisionmaking. Harvard University Press

21) Keeney R. L., 1996). 价值聚焦思维：通往创造性决策之路. Harvard University Press

22) NSA, Information Assurance Technical Framework, Unclassified, IATF Release 3.0-September 2000, A security guidance document developed by NSA’s ISSO organization with support from security advocates in government and industry

22) NSA, 信息保障技术框架, 非密, IATF 3.0 版—2000 年 9 月, 由 NSA 的 ISSO 组织在政府和行业信息安全倡导者的支持下编制的一份信息安全指南文件

23) Obbink Henk, Kruchten Philippe, Kozaczynski Wojtek, Postema Herman, Ran Alexander, Dominick Lutz, Kazman Rick, Hilliard Rich, Tracz Will, Kahane Ed, 2002. Software Architecture Review and Assessment (SARA) Report, Version 1.0

23) Obbink Henk, Kruchten Philippe, Kozaczynski Wojtek, Postema Herman, Ran Alexander, Dominick Lutz, Kazman Rick, Hilliard Rich, Tracz Will, Kahane Ed, 2002. 软件架构评审与评定（SARA）报告, 1.0 版

24) Parnell Gregory S., (editor). 2017. Trade-off Analytics: Creating and Exploring the System Tradespace Wiley Series in Systems Engineering and Management

24) Parnell Gregory S., (编). 2017. 权衡分析：创建并探索系统权衡空间 Wiley 系统工程与管理丛书

25) Vitruvius BC, De architectura, Marcus Vitruvius Pollio (1st century BC) (Transl. Morris Hicky Morgan, 1960), The Ten Books on Architecture. Courier Dover Publications. ISBN 0-486-20645-9

25) Vitruvius BC, De architectura, Marcus Vitruvius Pollio（公元前 1 世纪）（Morris Hicky Morgan 译，1960）, 《建筑十书》. Courier Dover Publications. ISBN 0-486-20645-9

26) American Society for Quality, Glossary – Entry: Quality, retrieved 2017-08-01

26) American Society for Quality, 术语表 – 条目：质量, 检索日期 2017-08-01

27) Boehm B., Kukreja N., (2015), An initial Ontology for System Qualities, Proceedings of 25th INCOSE Symposium, Seattle, USA

27) Boehm B., Kukreja N., (2015), 系统质量的初始本体, 第 25 届 INCOSE 研讨会论文集, 美国西雅图

28) Crosby Philip, (1979). Quality is Free. New York: McGraw-Hill. ISBN 0-07-014512-1

28) Crosby Philip, (1979). 质量免费. 纽约: McGraw-Hill. ISBN 0-07-014512-1

29) Drucker P. F., (1986). Innovation and entrepreneurship: Practice and principles. New York:

29) Drucker P. F., (1986). 创新与创业精神：实践与原则. 纽约:

Harper Row

Harper Row

30) Juran, Joseph M and Joseph A Defeo (2010), Quality Control Handbook, New York, McGraw-

30) Juran, Joseph M 和 Joseph A Defeo (2010), 质量控制手册, 纽约, McGraw-

Hill, 6th Edition

Hill, 第 6 版

31) Kiran D R, (2017), Total Quality Management: Key Concepts and Case Studies, Edition 1,

31) Kiran D R, (2017), 全面质量管理：关键概念与案例研究, 第 1 版,

Elsevier, Butterworth Heinemann publications

Elsevier, Butterworth Heinemann 出版社

32) Taguchi G., (1992). Taguchi on Robust Technology Development. ASME Press. ISBN 978- 99929-1-026-9

32) Taguchi G., (1992). 田口论稳健技术开发. ASME Press. ISBN 978- 99929-1-026-9

33) Kumar A., Doji S. L, Nikhil R Z, and Swaminathan N (2016), Value based System Architecting: Illustrated by Designing a Task Automation System, Proceedings of 26th INCOSE Symposium,

33) Kumar A., Doji S. L, Nikhil R Z, 和 Swaminathan N (2016), 基于价值的系统架构工作：以设计任务自动化系统为例, 第 26 届 INCOSE 研讨会论文集,

Edinburgh, UK

英国爱丁堡

34) Kumar A., Doji S. L, Nikhil R Z, and Jose K R (2017), Value based Architecture of Digital Product-

34) Kumar A., Doji S. L, Nikhil R Z, 和 Jose K R (2017), 基于价值的数字产品-

Service Systems, Proceedings of 27th INCOSE Symposium, Adelaide, Australia

服务系统架构, 第 27 届 INCOSE 研讨会论文集, 澳大利亚阿德莱德

35) Len Bass, Paul Clements, Rick Kazman, 2003, Software Architecture in Practice, 2nd Edition,

35) Len Bass, Paul Clements, Rick Kazman, 2003, 软件架构实践, 第 2 版,

Addison Wesley Publications, ISBN: 0-321-15495-9

Addison Wesley 出版社, ISBN: 0-321-15495-9

36) Paul Clements, Rick Kazman, Mark Klein, 2002, Evaluating Software Architectures: Methods and Case Studies, 1st Edition, Addison Wesley Publications, ISBN-10: 0-201-70482-X

36) Paul Clements, Rick Kazman, Mark Klein, 2002, 软件架构评估：方法与案例研究, 第 1 版, Addison Wesley 出版社, ISBN-10: 0-201-70482-X

37) The qualities of architecture, John Critchley, March 10th, 2008

37) 架构的质量, John Critchley, 2008 年 3 月 10 日

38) Vitruvius BC, De architectura, Marcus Vitruvius Pollio (1st century BC) (Transl. Morris 2106 Hicky Morgan, 1960), The Ten Books on Architecture. Courier Dover Publications. ISBN 0-2107 486-20645-9

38) Vitruvius BC, De architectura, Marcus Vitruvius Pollio（公元前 1 世纪）（Morris 2106 Hicky Morgan 译，1960）, 《建筑十书》. Courier Dover Publications. ISBN 0-2107 486-20645-9

39) Characteristics of Good Architecture, Enterprise Architect User Guide v13.0, Sparx Systems, 2018, url: http: /sparxsystems.com/enterprise_architect_user_guide/13.0/guidebooks/ea

39) 良好架构的特性, Enterprise Architect 用户指南 v13.0, Sparx Systems, 2018, url: http: /sparxsystems.com/enterprise_architect_user_guide/13.0/guidebooks/ea

_characteristics_of_good_architecture.html

_characteristics_of_good_architecture.html

40) Simon A, Herbert, 1962, The Architecture of Complexity, Proceedings of the American Philosophical Society, Vol. 106, No. 6. (Dec. 12, 1962), pp 467-482

40) Simon A, Herbert, 1962, 复杂性的架构, 美国哲学学会会刊, 第 106 卷, 第 6 期. （1962 年 12 月 12 日）, 第 467-482 页

41) Boehm B. W., Brown J. R., Kaspar H., Lipow M., McLeod G., Meritt M., Characteristics of

41) Boehm B. W., Brown J. R., Kaspar H., Lipow M., McLeod G., Meritt M., 软件质量的

Software Quality, Edition 2, North-Holland Pub. Co., 1978

特性, 第 2 版, North-Holland Pub. Co., 1978

42) [Broy, 2009] Automotive Architecture Framework: Towards a Holistic and Standardised System Architecture Description, An overview on description concepts, models and methods

42) [Broy, 2009] 汽车架构框架：走向整体化、标准化的系统架构描述, 关于描述概念、模型与方法的概述

43) Parnell Gregory S., (ed.) (2017). Trade-off Analytics: Creating and Exploring the System Tradespace (Wiley Series in Systems Engineering and Management, January 2017)

43) Parnell Gregory S., (编) (2017). 权衡分析：创建并探索系统权衡空间（Wiley 系统工程与管理丛书, 2017 年 1 月）

44) Parnell Gregory S., Bresnick Terry, Tani Steven N., Johnson Eric R., (2013). Handbook of

44) Parnell Gregory S., Bresnick Terry, Tani Steven N., Johnson Eric R., (2013). 决策分析

Decision Analysis (Wiley Handbooks in Operations Research and Management Science, April 2013)

手册（Wiley 运筹学与管理科学手册丛书, 2013 年 4 月）

45) Weill P., (2007), Innovating in Information Systems: What do the most agile firms in the world do? Sixth e-Business Conference, Barcelona Spain

45) Weill P., (2007), 信息系统中的创新：世界上最具敏捷性的企业在做什么？第六届电子商务会议, 西班牙巴塞罗那

46) Mark W., Maier (1996), Architecting Principles for Systems-of-Systems, DOI: 10.1002/j.2334- 5837.1996.tb02054.x

46) Mark W., Maier (1996), 系统的系统的架构原则, DOI: 10.1002/j.2334- 5837.1996.tb02054.x

47) Evans D., (2014), Styles of Architecting - A smarter approach to architecting the Defence Enterprise, Niteworks White Paper

47) Evans D., (2014), 架构工作的风格——架构国防企业的更明智途径, Niteworks 白皮书

48) Doji S., Lokku, Value distilled: A framework based approach to establish the trace of technology value in the context of engineering management, 2011 IEEE EUROCON - International Conference on Computer as a Tool, Lisbon, 2011, pp. 1-4

48) Doji S., Lokku，价值提炼：在工程管理语境下建立技术价值追溯的基于框架的途径，2011 IEEE EUROCON——作为工具的计算国际会议，里斯本，2011，第 1-4 页

49) Gilb T., Fundamental Principles of Evolutionary Project Management, Proceedings of 15th INCOSE Symposium, 2005, New York, USA

49) Gilb T.，演化式项目管理的基本原则，第 15 届 INCOSE 研讨会论文集，2005，美国纽约

50) Kumar A., Doji S. L, Nikhil R Z, and Jose K R, Value based Architecture of Digital Product-

50) Kumar A.，Doji S. L，Nikhil R Z 与 Jose K R，基于价值的数字产品-

Service Systems, Proceedings of 27th INCOSE Symposium, 2017, Adelaide, Australia

服务系统架构，第 27 届 INCOSE 研讨会论文集，2017，澳大利亚阿德莱德

51) Kumar A., Doji S. L, Nikhil R Z, and Swaminathan N, Value based System Architecting: Illustrated by Designing a Task Automation System, Proceedings of 26th INCOSE Symposium, 2016, Edinburgh, U

51) Kumar A.，Doji S. L，Nikhil R Z 与 Swaminathan N，基于价值的系统架构工作：以设计任务自动化系统为例，第 26 届 INCOSE 研讨会论文集，2016，爱丁堡，U

52) Menger C., (1976). Principles of economics. (Dingwall J., Hoselitz B. E., Trans.). New York: New York University Press. (Original work published 1871)

52) Menger C.，(1976)。经济学原理。(Dingwall J., Hoselitz B. E. 译)。New York: New York University Press。(原著出版于 1871 年)

53) Porter M.E., Competitive Advantage: Creating and Sustaining Superior Performance, ( Revised edition), The Free Press, 2004

53) Porter M.E.，竞争优势：创造与保持卓越绩效，（修订版），The Free Press，2004

54) Selva D., Crawley E.F., VASSAR: Value Assessment of System Architectures using Rules, in Proceedings of the 2013 IEEE Aerospace Conference, Big Sky, Montana, 2013

54) Selva D., Crawley E.F.，VASSAR：使用规则对系统架构进行价值评定，载于 2013 IEEE 航空航天会议论文集，蒙大拿州大天空，2013

55) Zeithaml Valarie (1998),, Consumer Perceptions of Price, Quality, and Value: A Means-End Model and Synthesis of Evidence, Journal of Marketing, Vol. 52 (July 1988), 2-22

55) Zeithaml Valarie (1998),，消费者对价格、质量和价值的感知：手段-目的模型与证据综合，Journal of Marketing，第 52 卷（1988 年 7 月），2-22

56) Ring J., 1998. A Value Seeking Approach to the Engineering of Systems. Proceedings of the IEEE

56) Ring J.，1998。系统工程的价值寻求途径。IEEE

Conference on Systems, Man, and Cybernetics. p. 2704-2708

系统、人与控制论会议论文集。第 2704-2708 页

57) Perakath C., Benjamin et al., 1994, IDEF5 Method Report, Knowledge Based Systems, Inc

57) Perakath C., Benjamin 等，1994，IDEF5 方法报告，Knowledge Based Systems, Inc

58) Office of Aerospace Studies, Air Force Material Command (AFMC) OAS/A9, Analysis of Alternatives, (AoA) Handbook, A Practical Guide to Analyzes of Alternatives" (PDF). Retrieved 24 August 2017

58) 航空航天研究办公室，空军装备司令部（AFMC）OAS/A9，备选方案分析（AoA）手册，备选方案分析实用指南"（PDF）。2017 年 8 月 24 日检索

59) CMU/SEI-2000-TR-004, “ATAM: Method for Architecture Evaluation”, Rick Kazman, Mark Klein and Paul Clements, technical report, Software Engineering Institute, Carnegie Mellon University,

59) CMU/SEI-2000-TR-004，“ATAM：架构评估方法”，Rick Kazman, Mark Klein and Paul Clements，技术报告，软件工程研究所，卡内基梅隆大学，

August 2000

2000 年 8 月

60) CMU/SEI-2005-TR-021: “Categorizing Business Goals for Software Architectures”. Rick Kazman and Len Bass. Software Engineering Institute, Carnegie Mellon University, 2005

60) CMU/SEI-2005-TR-021：“面向软件架构的业务目标分类”。Rick Kazman and Len Bass。软件工程研究所，卡内基梅隆大学，2005

61) CMU/SEI-2006-TR-012, “Risk Themes Discovered Through Architecture Evaluations”. Len Bass, Robert Nord, William Wood and David Zubrow. Pittsburgh, PA: Software Engineering Institute,

61) CMU/SEI-2006-TR-012，“通过架构评估发现的风险主题”。Len Bass, Robert Nord, William Wood and David Zubrow。匹兹堡，宾夕法尼亚州：软件工程研究所，

Carnegie Mellon University, 2006

卡内基梅隆大学，2006

62) “Insights from 15 Years of ATAM Data: Towards Agile Architecture”, Stephany Bellomo, Ian Gorton, and Rick Kazman, IEEE Software, September/October, 2015, 32:5, 38-45

62) “从 15 年 ATAM 数据中获得的洞见：走向敏捷架构”，Stephany Bellomo, Ian Gorton, and Rick Kazman，IEEE Software，2015 年 9／10 月，32:5，38-45

63) “Evaluating Software Architectures: Methods and Case Studies”, 2002 published by Addison- Wesley.

63) “评估软件架构：方法与案例研究”，2002 年由 Addison-Wesley 出版。

64) Firesmith Donald et al. , The Method Framework for Engineering System Architectures,

64) Firesmith Donald 等，系统工程架构的方法框架，

Auerbach/CRC Press 2009, ISBN 978-1-4200-8575-4

Auerbach/CRC Press 2009，ISBN 978-1-4200-8575-4

65) Firesmith D., QUality Assessment of System Architectures and their Requirements (QUASAR), presentation 2007, available online at http://www.sei.cmu.edu/library/assets/quality-assess.pdf

65) Firesmith D.，系统架构及其需求的质量评定（QUASAR），2007 年演示文稿，可在线获取：http://www.sei.cmu.edu/library/assets/quality-assess.pdf

66) Firesmith D., QUASAR: A Method for the QUality Assessment of Software-Intensive System

66) Firesmith D.，QUASAR：软件密集型系统

Architectures, CMU/SEI-2006-HB-001, SEI Handbook 2006, available online at http://resources

架构质量评定的方法，CMU/SEI-2006-HB-001，SEI 手册 2006，可在线获取：http://resources

.sei.cmu.edu/asset_files/Handbook/2006_002_001_14627.pdf

.sei.cmu.edu/asset_files/Handbook/2006_002_001_14627.pdf

67) Structured Metrics Metamodel Specification Version 1.1.1, Object Management Group, URL:

67) 结构化度量元模型规格 1.1.1 版，对象管理组，URL：

https://www.omg.org/spec/SMM/1.1.1/

https://www.omg.org/spec/SMM/1.1.1/

## IEEE notices and abstract IEEE 声明与摘要

### Important Notices and Disclaimers Concerning IEEE Standards Documents 关于 IEEE 标准文件的重要声明与免责声明

IEEE documents are made available for use subject to important notices and legal disclaimers. These notices and disclaimers, or a reference to this page, appear in all standards and may be found under the heading “Important Notices and Disclaimers Concerning IEEE Standards Documents.” They can also be obtained on request from IEEE or viewed at http: /standards.ieee.org/IPR/disclaimers.html.

IEEE 文件在重要声明与法律免责声明的前提下提供使用。这些声明与免责声明，或对本页的引用，出现在所有标准中，可在“关于 IEEE 标准文件的重要声明与免责声明”标题下查到。也可应请求向 IEEE 索取，或在 http: /standards.ieee.org/IPR/disclaimers.html 查看。

### Notice and Disclaimer of Liability Concerning the Use of IEEE Standards Documents 关于使用 IEEE 标准文件的声明与责任免责声明

IEEE Standards documents (standards, recommended practices, and guides), both full-use and trial-use, are developed within IEEE Societies and the Standards Coordinating Committees of the IEEE Standards Association (“IEEE-SA”) Standards Board. IEEE (“the Institute”) develops its standards through a consensus development process, approved by the American National Standards Institute (“ANSI”), which brings together volunteers representing varied viewpoints and interests to achieve the final product. IEEE Standards are documents developed through scientific, academic, and industry-based technical working groups. Volunteers in IEEE working groups are not necessarily members of the Institute and participate without compensation from IEEE. While IEEE administers the process and establishes rules to promote fairness in the consensus development process, IEEE does not independently evaluate, test, or verify the accuracy of any of the information or the soundness of any judgments contained in its standards.

IEEE 标准文件（标准、推荐实施规程与指南），无论完全使用版还是试用版，均由 IEEE 各专业协会以及 IEEE 标准协会（“IEEE-SA”）标准理事会的标准协调委员会制定。IEEE（“本学会”）通过共识制定过程制定其标准，该过程经美国国家标准学会（“ANSI”）批准，汇集代表各种观点与利益的志愿者以形成最终成果。IEEE 标准是由科学界、学术界与产业界技术工作组制定的文件。IEEE 工作组的志愿者不一定是本学会会员，且不从 IEEE 获取报酬。尽管 IEEE 管理该过程并制定规则以促进共识制定过程的公平性，但 IEEE 不独立评估、测试或核实其标准中所含任何信息的准确性或任何判断的可靠性。

IEEE Standards do not guarantee or ensure safety, security, health, or environmental protection, or ensure against interference with or from other devices or networks. Implementers and users of IEEE Standards documents are responsible for determining and complying with all appropriate safety, security, environmental, health, and interference protection practices and all applicable laws and regulations.

IEEE 标准不保证或确保安全、信息安全、健康或环境保护，也不确保免于同其他设备或网络之间的干扰。IEEE 标准文件的实施者和使用者有责任确定并遵守所有适当的安全、信息安全、环境、健康和干扰防护实践以及所有适用的法律和法规。

IEEE does not warrant or represent the accuracy or content of the material contained in its standards, and expressly disclaims all warranties (express, implied and statutory) not included in this or any other document relating to the standard, including, but not limited to, the warranties of: merchantability; fitness for a particular purpose; non-infringement; and quality, accuracy, effectiveness, currency, or completeness of material. In addition, IEEE disclaims any and all conditions relating to: results; and workmanlike effort. IEEE standards documents are supplied “AS IS” and “WITH ALL FAULTS.”

IEEE 不担保也不声明其标准所含材料的准确性或内容，并明确否认未包含在本文件或任何其他与该标准有关的文件中的所有担保（明示、默示和法定），包括但不限于以下担保：可销售性；特定用途适用性；不侵权；以及材料的质量、准确性、有效性、时效性或完整性。此外，IEEE 否认与下列各项有关的一切条件：结果；以及专业水准的努力。IEEE 标准文件按“AS IS”和“WITH ALL FAULTS”提供。

Use of an IEEE standard is wholly voluntary. The existence of an IEEE standard does not imply that there are no other ways to produce, test, measure, purchase, market, or provide other goods and services related to the scope of the IEEE standard. Furthermore, the viewpoint expressed at the time a standard is approved and issued is subject to change brought about through developments in the state of the art and comments received from users of the standard.

使用 IEEE 标准完全出于自愿。某项 IEEE 标准的存在并不意味着不存在其他方式来生产、测试、测量、采购、营销或提供与该 IEEE 标准范围有关的其他商品和服务。此外，标准批准和发布时所表达的观点可能因技术现状的发展和该标准使用者所提意见而改变。

In publishing and making its standards available, IEEE is not suggesting or rendering professional or other services for, or on behalf of, any person or entity nor is IEEE undertaking to perform any duty owed by any other person or entity to another. Any person utilizing any IEEE Standards document, should rely upon his or her own independent judgment in the exercise of reasonable care in any given circumstances or, as appropriate, seek the advice of a competent professional in determining the appropriateness of a given IEEE standard.

IEEE 出版并提供其标准，并非为任何人或实体、或代表任何人或实体建议或提供专业服务或其他服务，IEEE 也不承诺履行任何其他人或实体对他人所负的任何义务。任何人使用任何 IEEE 标准文件时，宜在任何特定情形下尽合理注意并依赖其自身的独立判断，或视情况在确定某项 IEEE 标准是否适当时寻求有资质的专业人员的意见。

IN NO EVENT SHALL IEEE BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO: PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE PUBLICATION, USE OF, OR RELIANCE UPON ANY STANDARD, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE AND REGARDLESS OF WHETHER SUCH DAMAGE WAS FORESEEABLE.

在任何情况下，IEEE 均不对任何直接的、间接的、附带的、特殊的、惩罚性的或后果性的损害（包括但不限于：替代商品或服务的采购；使用、数据或利润的损失；业务中断）承担任何责任，无论其因何引起，也无论基于何种责任理论，无论是合同责任、严格责任还是侵权责任（包括过失或其他情形），只要是以任何方式因出版、使用或依赖任何标准而引起的，即使已被告知发生此类损害的可能性，也无论此类损害是否可预见。

### Translations 翻译

The IEEE consensus development process involves the review of documents in English only. In the event that an IEEE standard is translated, only the English version published by IEEE should be considered the approved IEEE standard.

IEEE 的共识制定过程仅涉及以英文对文件进行审查。若某项 IEEE 标准被翻译，只有 IEEE 出版的英文版本宜被视为经批准的 IEEE 标准。

### Official statements 正式声明

A statement, written or oral, that is not processed in accordance with the IEEE-SA Standards Board Operations Manual shall not be considered or inferred to be the official position of IEEE or any of its committees and shall not be considered to be, or be relied upon as, a formal position of IEEE. At lectures, symposia, seminars, or educational courses, an individual presenting information on IEEE standards shall make it clear that his or her views should be considered the personal views of that individual rather than the formal position of IEEE.

未经按照 IEEE-SA 标准委员会操作手册处理的书面或口头声明，不应被视为或推断为 IEEE 或其任何委员会的正式立场，也不应被视为或作为 IEEE 的正式立场而加以依赖。在讲座、专题讨论会、研讨会或教育课程中，介绍 IEEE 标准相关信息的个人应明确说明，其观点宜被视为该个人的个人观点，而非 IEEE 的正式立场。

### Comments on standards 对标准的意见

Comments for revision of IEEE Standards documents are welcome from any interested party, regardless of membership affiliation with IEEE. However, IEEE does not provide consulting information or advice pertaining to IEEE Standards documents. Suggestions for changes in documents should be in the form of a proposed change of text, together with appropriate supporting comments. Since IEEE standards represent a consensus of concerned interests, it is important that any responses to comments and questions also receive the concurrence of a balance of interests. For this reason, IEEE and the members of its societies and Standards Coordinating Committees are not able to provide an instant response to comments or questions except in those cases where the matter has previously been addressed. For the same reason, IEEE does not respond to interpretation requests. Any person who would like to participate in revisions to an IEEE standard is welcome to join the relevant IEEE working group.

欢迎任何有关方面提出对 IEEE 标准文件进行修订的意见，而不论其是否为 IEEE 成员。但是，IEEE 不提供与 IEEE 标准文件有关的咨询信息或建议。对文件的修改建议宜以文本修改提案的形式提出，并附上适当的支持性意见。由于 IEEE 标准代表相关利益方的共识，因此对意见和问题的任何答复也宜取得利益平衡方的同意。为此，除有关事项此前已得到处理的情形外，IEEE 及其协会成员和标准协调委员会无法对意见或问题作出即时答复。出于同样的原因，IEEE 不对解释请求作出答复。任何希望参与 IEEE 标准修订的人士，均欢迎加入相关的 IEEE 工作组。

Comments on standards should be submitted to the following address: Secretary, IEEE-SA Standards Board

对标准的意见宜提交至以下地址：IEEE-SA 标准委员会秘书

445 Hoes Lane Piscataway, NJ 08854 USA

445 Hoes Lane Piscataway, NJ 08854 USA

### Laws and regulations 法律和法规

Users of IEEE Standards documents should consult all applicable laws and regulations. Compliance with the provisions of any IEEE Standards document does not imply compliance to any applicable regulatory requirements. Implementers of the standard are responsible for observing or referring to the applicable regulatory requirements. IEEE does not, by the publication of its standards, intend to urge action that is not in compliance with applicable laws, and these documents may not be construed as doing so.

IEEE 标准文件的使用者宜查阅所有适用的法律和法规。符合任何 IEEE 标准文件的规定并不意味着符合任何适用的监管要求。标准的实施者有责任遵守或参照适用的监管要求。IEEE 出版其标准，无意敦促采取不符合适用法律的行为，且这些文件不得被解释为如此。

### Copyrights 版权

IEEE draft and approved standards are copyrighted by IEEE under U.S. and international copyright laws. They are made available by IEEE and are adopted for a wide variety of both public and private uses. These include both use, by reference, in laws and regulations, and use in private self-regulation, standardization, and the promotion of engineering practices and methods. By making these documents available for use and adoption by public authorities and private users, IEEE does not waive any rights in copyright to the documents.

IEEE 草案标准和已批准标准依据美国和国际版权法由 IEEE 享有版权。这些标准由 IEEE 提供，并被广泛用于各种公共用途和私人用途。这些用途既包括在法律法规中以引用方式使用，也包括在私人自我规制、标准化以及推广工程实践和方法中使用。IEEE 使这些文件可供公共机构和私人使用者使用和采用，并不放弃对这些文件的任何版权权利。

### Photocopies 影印

Subject to payment of the appropriate fee, IEEE will grant users a limited, non-exclusive license to photocopy portions of any individual standard for company or organizational internal use or individual, non-commercial use only. To arrange for payment of licensing fees, please contact Copyright Clearance Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA; +1 978 750 8400. Permission to photocopy portions of any individual standard for educational classroom use can also be obtained through the Copyright Clearance Center.

在支付相应费用后，IEEE 将授予使用者有限的、非独占性的许可，允许仅为公司或组织内部使用或个人非商业使用而影印任何单项标准的部分内容。如需安排支付许可费，请联系 Copyright Clearance Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA；+1 978 750 8400。为教育课堂教学用途影印任何单项标准的部分内容，也可通过 Copyright Clearance Center 获得许可。

### Updating of IEEE Standards documents IEEE 标准文件的更新

7799

7799

Users of IEEE Standards documents should be aware that these documents may be superseded at any time by the issuance of new editions or may be amended from time to time through the issuance of amendments, corrigenda, or errata. An official IEEE document at any point in time consists of the current edition of the document together with any amendments, corrigenda, or errata then in effect.

IEEE 标准文件的使用者宜注意，这些文件可能随时因新版本的发布而被取代，也可能不时通过发布修正案、更正表或勘误表而得到修订。在任何时点，一份正式的 IEEE 文件由该文件的现行版本以及当时生效的任何修正案、更正表或勘误表组成。

Every IEEE standard is subjected to review at least every ten years. When a document is more than ten years old and has not undergone a revision process, it is reasonable to conclude that its contents, although still of some value, do not wholly reflect the present state of the art. Users are cautioned to check to determine that they have the latest edition of any IEEE standard.

每项 IEEE 标准至少每十年接受一次审查。当一份文件已超过十年且未经过修订过程时，有理由认为其内容虽仍具有一定价值，但并未完全反映当前的技术水平。提醒使用者进行核查，以确定其所持有的任何 IEEE 标准均为最新版本。

In order to determine whether a given document is the current edition and whether it has been amended through the issuance of amendments, corrigenda, or errata, visit the IEEE-SA Website at http: /ieeexplore.ieee.org/xpl/standards.jsp or contact IEEE at the address listed previously. For more information about the IEEE-SA or IEEE’s standards development process, visit the IEEE-SA Website at http: /standards.ieee.org.

为确定某份文件是否为现行版本，以及是否已通过发布修正案、更正表或勘误表而得到修订，请访问 IEEE-SA 网站 http: /ieeexplore.ieee.org/xpl/standards.jsp，或按上文所列地址联系 IEEE。有关 IEEE-SA 或 IEEE 标准制定过程的更多信息，请访问 IEEE-SA 网站 http: /standards.ieee.org。

### Errata 勘误

Errata, if any, for all IEEE standards can be accessed on the IEEE-SA Website: http: /standards.ieee

所有 IEEE 标准的勘误（如有）均可在 IEEE-SA 网站上访问：http: /standards.ieee

.org/findstds/errata/index.html. Users are encouraged to check this URL for errata periodically.

.org/findstds/errata/index.html。鼓励用户定期查看该 URL 以获取勘误。

### Patents 专利

Attention is called to the possibility that implementation of this standard may require use of subject matter covered by patent rights. By publication of this standard, no position is taken by the IEEE with respect to the existence or validity of any patent rights in connection therewith. If a patent holder or patent applicant has filed a statement of assurance via an Accepted Letter of Assurance, then the statement is listed on the IEEE-SA Website at http: /standards.ieee.org/about/sasb/patcom/patents

提请注意：本标准的实施可能需要使用受专利权保护的标的物。本标准的发布并不表示 IEEE 就与之相关的任何专利权的存在或有效性持有任何立场。如专利持有人或专利申请人已通过已接受的保证书提交声明，则该声明列于 IEEE-SA 网站 http: /standards.ieee.org/about/sasb/patcom/patents

.html. Letters of Assurance may indicate whether the Submitter is willing or unwilling to grant licenses under patent rights without compensation or under reasonable rates, with reasonable terms and conditions that are demonstrably free of any unfair discrimination to applicants desiring to obtain such licenses.

.html。保证书可表明提交方是否愿意在无偿条件下、或在合理费率并附有合理条款和条件下授予专利权项下的许可，且这些条款和条件对希望获得此类许可的申请方明显不构成任何不公平歧视。

Essential Patent Claims may exist for which a Letter of Assurance has not been received. The IEEE is not responsible for identifying Essential Patent Claims for which a license may be required, for conducting inquiries into the legal validity or scope of Patents Claims, or determining whether any licensing terms or conditions provided in connection with submission of a Letter of Assurance, if any, or in any licensing agreements are reasonable or non-discriminatory. Users of this standard are expressly advised that determination of the validity of any patent rights, and the risk of infringement of such rights, is entirely their own responsibility. Further information may be obtained from the IEEE Standards Association.

可能存在尚未收到保证书的必要专利权利要求。IEEE 不负责识别可能需要许可的必要专利权利要求，不负责调查专利权利要求的法律有效性或范围，也不负责确定与提交保证书（如有）相关而提供的任何许可条款或条件、或任何许可协议中的条款或条件是否合理或无歧视。明确告知本标准的使用者：任何专利权的有效性判定以及侵犯此类权利的风险，完全由其自行承担。更多信息可从 IEEE 标准协会获得。

### Abstract and keywords 摘要与关键词

ICS 35.080

ICS 35.080

© ISO/IEC 2019 – All rights reserved 82

© ISO/IEC 2019 – 版权所有 82

Copyright Notice

版权通告

The Canadian adoption of this International Standard as a National Standard of Canada contains information copyright protected by CSA Group. All rights reserved. No part of this National Standard of Canada may be reproduced in any form whatsoever without the prior permission of CSA Group. ISO/IEC material is reprinted with permission.

本国际标准被加拿大采用为加拿大国家标准，该采用版本含有受 CSA Group 版权保护的信息。版权所有。未经 CSA Group 事先许可，不得以任何形式复制本加拿大国家标准的任何部分。ISO/IEC 材料经许可重印。

Requests for permission to reproduce this National Standard of Canada or parts thereof should be addressed to:

复制本加拿大国家标准或其部分内容的许可申请，宜向以下地址提出：

Manager, Sales CSA Group

CSA Group 销售经理

178 Rexdale Boulevard Toronto, Ontario M9W 1R3

178 Rexdale Boulevard Toronto, Ontario M9W 1R3

Copyright violators will be prosecuted to the full extent of the law.

侵犯版权者将依法受到最大限度的追究。

ISBN 978-1-4883-3082-7

ISBN 978-1-4883-3082-7
