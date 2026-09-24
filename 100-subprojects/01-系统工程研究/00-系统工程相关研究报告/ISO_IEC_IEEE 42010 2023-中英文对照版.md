# ISO/IEC/IEEE 42010:2022《软件、系统与企业 — 架构描述》中英文对照版

> **本文件性质**：`ISO_IEC_IEEE 42010 2023.md` 的**逐段中英对照译本**。英文为源文（原文照录），中文为译文，置于对应英文段落之下。

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

**转换说明 / About this file**
本文件由 `ISO_IEC_IEEE 42010 2023.pdf` 自动转换生成，正文为**英文原文照录**，未作翻译或改写。
- **条款号**：一律保留印刷条款号（`1`、`5.2.6`、`A.1`、术语条目 `3.1`…），标题层级按原版字号还原。
- **插图**：原 PDF 的图为矢量轮廓，文字不在文本层，故按图区渲染为 PNG，存于同名 `.assets/` 目录，在原文位置以 `![Figure …](…)` 引用，共 11 幅（图 1~6、A.1~A.3、C.1~C.2）。
- **表格**：表 F.1／F.2 转为 Markdown 表；原表跨页处被版面切为三段，转换后仍分段呈现。
- **目录**：原印刷目录为点线制表符且页码不可靠，已替换为按标题层级生成的 Markdown 目录。
- **页眉页脚**（`ISO/IEC/IEEE 42010:2022(E)`、版权行、页码）为版面构件，未收入正文。
- **断行连字符**已还原（`identi- fying` → `identifying`），固有连字符保留（`non-functional`）。
- **封面与版权页**照录于正文之前，未作标题化处理。
**校验**：正文按 70 字符窗口全文比对，4281 个窗口 **0 未命中**；表格 57 个单元格 **0 缺失**。

---

## 目录（Contents）

  - [Cover and copyright pages (source lay-out, verbatim) 封面与版权页（按原版版面照录）](#cover-and-copyright-pages-source-lay-out-verbatim-封面与版权页按原版版面照录)
  - [Foreword 前言](#foreword-前言)
  - [Introduction 引言](#introduction-引言)
  - [Software, systems and enterprise — Architecture description 软件、系统与企业 — 架构描述](#software-systems-and-enterprise-architecture-description-软件系统与企业-架构描述)
    - [1 Scope 范围](#1-scope-范围)
    - [2 Normative references 规范性引用文件](#2-normative-references-规范性引用文件)
    - [3 Terms and definitions 术语和定义](#3-terms-and-definitions-术语和定义)
      - [3.1 architecting 架构工作](#31-architecting-架构工作)
      - [3.2 architecture 架构](#32-architecture-架构)
      - [3.3 architecture description / AD ｜ 架构描述 / AD](#33-architecture-description-ad-架构描述-ad)
      - [3.4 architecture description element / AD element ｜ 架构描述元素 / AD 元素](#34-architecture-description-element-ad-element-架构描述元素-ad-元素)
      - [3.5 architecture description framework / ADF ｜ 架构描述框架 / ADF](#35-architecture-description-framework-adf-架构描述框架-adf)
      - [3.6 architecture description language / ADL ｜ 架构描述语言 / ADL](#36-architecture-description-language-adl-架构描述语言-adl)
      - [3.7 architecture view 架构视图](#37-architecture-view-架构视图)
      - [3.8 architecture viewpoint 架构视角](#38-architecture-viewpoint-架构视角)
      - [3.9 aspect 方面体](#39-aspect-方面体)
      - [3.10 concern 关注点](#310-concern-关注点)
      - [3.11 correspondence 对应关系](#311-correspondence-对应关系)
      - [3.12 entity of interest / EoI ｜ 所关注实体 / EoI](#312-entity-of-interest-eoi-所关注实体-eoi)
      - [3.13 environment 环境](#313-environment-环境)
      - [3.14 information part 信息部件](#314-information-part-信息部件)
      - [3.15 model kind 模型种类](#315-model-kind-模型种类)
      - [3.16 specification 规格](#316-specification-规格)
      - [3.17 stakeholder 利益相关方](#317-stakeholder-利益相关方)
      - [3.18 stakeholder perspective 利益相关方角度](#318-stakeholder-perspective-利益相关方角度)
      - [3.19 view component / architecture view component ｜ 视图组件 / 架构视图组件](#319-view-component-architecture-view-component-视图组件-架构视图组件)
    - [4 Conformance 符合性](#4-conformance-符合性)
    - [5 Conceptual foundations 概念基础](#5-conceptual-foundations-概念基础)
      - [5.1 General **5.1 总则**](#51-general-51-总则)
      - [5.2 Conceptual models of an architecture description **5.2 架构描述的概念模型**](#52-conceptual-models-of-an-architecture-description-52-架构描述的概念模型)
        - [5.2.1 Context of architecture description 架构描述的语境](#521-context-of-architecture-description-架构描述的语境)
        - [5.2.2 Architectures and architecture descriptions 架构与架构描述](#522-architectures-and-architecture-descriptions-架构与架构描述)
        - [5.2.3 Stakeholders and concerns 利益相关方与关注点](#523-stakeholders-and-concerns-利益相关方与关注点)
        - [5.2.4 Stakeholder perspectives 利益相关方角度](#524-stakeholder-perspectives-利益相关方角度)
        - [5.2.5 Aspects 方面体](#525-aspects-方面体)
        - [5.2.6 Architecture considerations 架构考量因素](#526-architecture-considerations-架构考量因素)
        - [5.2.7 Architecture views and architecture viewpoints 架构视图与架构视角](#527-architecture-views-and-architecture-viewpoints-架构视图与架构视角)
        - [5.2.8 Model kinds, legends and architecture view components 模型种类、图例与架构视图组件](#528-model-kinds-legends-and-architecture-view-components-模型种类图例与架构视图组件)
        - [5.2.9 Architecture description (AD) elements 架构描述（AD）元素](#529-architecture-description-ad-elements-架构描述ad元素)
        - [5.2.10 View methods 视图方法](#5210-view-methods-视图方法)
        - [5.2.11 AD element correspondence AD 元素对应关系](#5211-ad-element-correspondence-ad-元素对应关系)
        - [5.2.12 Architecture decisions and rationale 架构决策与理由](#5212-architecture-decisions-and-rationale-架构决策与理由)
      - [5.3 Architecture description in the life cycle **5.3 生存周期中的架构描述**](#53-architecture-description-in-the-life-cycle-53-生存周期中的架构描述)
      - [5.4 Architecture description frameworks and languages **5.4 架构描述框架与语言**](#54-architecture-description-frameworks-and-languages-54-架构描述框架与语言)
        - [5.4.1 General 总则](#541-general-总则)
        - [5.4.2 Architecture description frameworks 架构描述框架](#542-architecture-description-frameworks-架构描述框架)
        - [5.4.3 ADF utilization ADF 的利用](#543-adf-utilization-adf-的利用)
        - [5.4.4 Architecture description languages 架构描述语言](#544-architecture-description-languages-架构描述语言)
    - [6 Specification of an architecture description 架构描述的规格](#6-specification-of-an-architecture-description-架构描述的规格)
      - [6.1 Architecture description identification and overview 架构描述的标识与概述](#61-architecture-description-identification-and-overview-架构描述的标识与概述)
      - [6.2 Identification of stakeholders 利益相关方的识别](#62-identification-of-stakeholders-利益相关方的识别)
      - [6.3 Identification of stakeholder perspectives 利益相关方角度的识别](#63-identification-of-stakeholder-perspectives-利益相关方角度的识别)
      - [6.4 Identification of concerns 关注点的识别](#64-identification-of-concerns-关注点的识别)
      - [6.5 Identification of aspects 方面体的识别](#65-identification-of-aspects-方面体的识别)
      - [6.6 Inclusion of architecture viewpoints 架构视角的纳入](#66-inclusion-of-architecture-viewpoints-架构视角的纳入)
      - [6.7 Inclusion of architecture views 架构视图的包含](#67-inclusion-of-architecture-views-架构视图的包含)
      - [6.8 Inclusion of view components 视图组件的包含](#68-inclusion-of-view-components-视图组件的包含)
      - [6.9 Recording of architecture correspondences 架构对应关系的记录](#69-recording-of-architecture-correspondences-架构对应关系的记录)
        - [6.9.1 Consistency within an architecture description 架构描述内的一致性](#691-consistency-within-an-architecture-description-架构描述内的一致性)
        - [6.9.2 Correspondences 对应关系](#692-correspondences-对应关系)
        - [6.9.3 Correspondence methods 对应方法](#693-correspondence-methods-对应方法)
      - [6.10 Recording of architecture decisions and rationale 架构决策与理由的记录](#610-recording-of-architecture-decisions-and-rationale-架构决策与理由的记录)
        - [6.10.1 Decision recording 决策记录](#6101-decision-recording-决策记录)
        - [6.10.2 Rationale recording 理由记录](#6102-rationale-recording-理由记录)
    - [7 Architecture description frameworks and architecture description languages 架构描述框架与架构描述语言](#7-architecture-description-frameworks-and-architecture-description-languages-架构描述框架与架构描述语言)
      - [7.1 Specification of an architecture description framework / 7.1.1 ｜ 架构描述框架的规格 / 7.1.1](#71-specification-of-an-architecture-description-framework-711-架构描述框架的规格-711)
      - [7.2 Specification of an architecture description language 架构描述语言的规格](#72-specification-of-an-architecture-description-language-架构描述语言的规格)
    - [8 Architecture viewpoints and model kinds 架构视角与模型种类](#8-architecture-viewpoints-and-model-kinds-架构视角与模型种类)
      - [8.1 Specification of an architecture viewpoint 架构视角的规格](#81-specification-of-an-architecture-viewpoint-架构视角的规格)
      - [8.2 Specification of a model kind 模型种类的规格](#82-specification-of-a-model-kind-模型种类的规格)
      - [8.3 View methods 视图方法](#83-view-methods-视图方法)
  - [Annex A (informative) — Notes on terms and concepts ｜ 附录 A（资料性）——术语与概念说明](#annex-a-informative-notes-on-terms-and-concepts-附录-a资料性术语与概念说明)
    - [A.1 General 总则](#a1-general-总则)
    - [A.2 Entities and their architectures 实体及其架构](#a2-entities-and-their-architectures-实体及其架构)
    - [A.3 Concerns 关注点](#a3-concerns-关注点)
    - [A.4 Aspects and perspectives 方面体与利益相关方角度](#a4-aspects-and-perspectives-方面体与利益相关方角度)
      - [A.4.1 General 总则](#a41-general-总则)
      - [A.4.2 Aspects 方面体](#a42-aspects-方面体)
      - [A.4.3 Stakeholder perspectives 利益相关方角度](#a43-stakeholder-perspectives-利益相关方角度)
      - [A.4.4 Structuring formalisms and structural categories 结构化形式体系与结构类别](#a44-structuring-formalisms-and-structural-categories-结构化形式体系与结构类别)
      - [A.4.5 Relationship between aspect and stakeholder perspective 方面体与利益相关方角度之间的关系](#a45-relationship-between-aspect-and-stakeholder-perspective-方面体与利益相关方角度之间的关系)
      - [A.4.6 Complementary ADF approaches 互补的 ADF 途径](#a46-complementary-adf-approaches-互补的-adf-途径)
    - [A.5 Architecture views and viewpoints 架构视图与架构视角](#a5-architecture-views-and-viewpoints-架构视图与架构视角)
    - [A.6 Correspondences 对应关系](#a6-correspondences-对应关系)
    - [A.7 Perspectives on architecture description languages 对架构描述语言的若干视角](#a7-perspectives-on-architecture-description-languages-对架构描述语言的若干视角)
  - [Annex B (informative) — Guidelines to specification of architecture viewpoints ｜ 附录 B（资料性）— 架构视角规格指南](#annex-b-informative-guidelines-to-specification-of-architecture-viewpoints-附录-b资料性-架构视角规格指南)
    - [B.1 General 总则](#b1-general-总则)
    - [B.2 Template for documenting specification of architecture viewpoints 用于记录架构视角规格的模板](#b2-template-for-documenting-specification-of-architecture-viewpoints-用于记录架构视角规格的模板)
      - [B.2.1 Template overview 模板概述](#b21-template-overview-模板概述)
      - [B.2.2 Architecture viewpoint name 架构视角名称](#b22-architecture-viewpoint-name-架构视角名称)
      - [B.2.3 Architecture viewpoint overview 架构视角概述](#b23-architecture-viewpoint-overview-架构视角概述)
      - [B.2.4 Concerns 关注点](#b24-concerns-关注点)
      - [B.2.5 Stakeholder perspectives 利益相关方角度](#b25-stakeholder-perspectives-利益相关方角度)
      - [B.2.6 Aspects 方面体](#b26-aspects-方面体)
      - [B.2.7 Typical stakeholders 典型利益相关方](#b27-typical-stakeholders-典型利益相关方)
      - [B.2.8 Correspondence methods 对应方法](#b28-correspondence-methods-对应方法)
      - [B.2.9 Specification of model kinds 模型种类规格](#b29-specification-of-model-kinds-模型种类规格)
        - [B.2.9.1 General 总则](#b291-general-总则)
        - [B.2.9.2 Metamodel related to the specification of a model kind 与模型种类规格相关的元模型](#b292-metamodel-related-to-the-specification-of-a-model-kind-与模型种类规格相关的元模型)
        - [B.2.9.3 Templates of specifications of model kinds 模型种类规格的模板](#b293-templates-of-specifications-of-model-kinds-模型种类规格的模板)
        - [B.2.9.4 Language related to the specification of a model kind 与模型种类规格相关的语言](#b294-language-related-to-the-specification-of-a-model-kind-与模型种类规格相关的语言)
      - [B.2.10 View methods 视图方法](#b210-view-methods-视图方法)
      - [B.2.11 Examples 示例](#b211-examples-示例)
      - [B.2.12 Notes 注](#b212-notes-注)
      - [B.2.13 Sources 来源](#b213-sources-来源)
    - [B.3 Resources for specifications of architecture viewpoints 架构视角规格的资源](#b3-resources-for-specifications-of-architecture-viewpoints-架构视角规格的资源)
  - [Annex C (informative) — Relationship to other standards ｜ 附录 C（资料性）— 与其他标准的关系](#annex-c-informative-relationship-to-other-standards-附录-c资料性-与其他标准的关系)
    - [C.1 General 总则](#c1-general-总则)
    - [C.2 Use with ISO/IEC/IEEE 42020 与 ISO/IEC/IEEE 42020 一起使用](#c2-use-with-isoiecieee-42020-与-isoiecieee-42020-一起使用)
    - [C.3 Use with ISO/IEC/IEEE 42030 与 ISO/IEC/IEEE 42030 一起使用](#c3-use-with-isoiecieee-42030-与-isoiecieee-42030-一起使用)
    - [C.4 Use with ISO 15704 与 ISO 15704 一起使用](#c4-use-with-iso-15704-与-iso-15704-一起使用)
    - [C.5 Use with ISO/IEC/IEEE 12207 与 ISO/IEC/IEEE 12207 一起使用](#c5-use-with-isoiecieee-12207-与-isoiecieee-12207-一起使用)
    - [C.6 Use with ISO/IEC/IEEE 15288 与 ISO/IEC/IEEE 15288 一起使用](#c6-use-with-isoiecieee-15288-与-isoiecieee-15288-一起使用)
    - [C.7 Use with open distributed processing standards 与开放分布式处理标准一起使用](#c7-use-with-open-distributed-processing-standards-与开放分布式处理标准一起使用)
      - [C.7.1 General 总则](#c71-general-总则)
      - [C.7.2 Enterprise viewpoint 企业视角](#c72-enterprise-viewpoint-企业视角)
      - [C.7.3 Information viewpoint 信息视角](#c73-information-viewpoint-信息视角)
      - [C.7.4 Computational viewpoint 计算视角](#c74-computational-viewpoint-计算视角)
      - [C.7.5 Engineering viewpoint 工程视角](#c75-engineering-viewpoint-工程视角)
      - [C.7.6 Technology viewpoint 技术视角](#c76-technology-viewpoint-技术视角)
  - [Annex D (informative) — Uses of architecture descriptions ｜ 附录 D（资料性）— 架构描述的用途](#annex-d-informative-uses-of-architecture-descriptions-附录-d资料性-架构描述的用途)
    - [D.1 General 总则](#d1-general-总则)
    - [D.2 Uses of architecture descriptions 架构描述的用途](#d2-uses-of-architecture-descriptions-架构描述的用途)
  - [Annex E (informative) — Architecture and architecture description life cycles ｜ 附录 E（资料性）— 架构与架构描述的生存周期](#annex-e-informative-architecture-and-architecture-description-life-cycles-附录-e资料性-架构与架构描述的生存周期)
    - [E.1 General 总则](#e1-general-总则)
    - [E.2 Architecting in the life cycle 生存周期中的架构工作](#e2-architecting-in-the-life-cycle-生存周期中的架构工作)
  - [Annex F (informative) — Architecture description frameworks ｜ 附录 F（资料性）— 架构描述框架](#annex-f-informative-architecture-description-frameworks-附录-f资料性-架构描述框架)
    - [F.1 General 总则](#f1-general-总则)
    - [F.2 Evolution of ADFs ADF 的演进](#f2-evolution-of-adfs-adf-的演进)
    - [F.3 ADF concepts ADF 概念](#f3-adf-concepts-adf-概念)
      - [F.3.1 ADF domains ADF 域](#f31-adf-domains-adf-域)
      - [F.3.2 Identification of stakeholders and definition of their perspectives 利益相关方的识别及其角度的定义](#f32-identification-of-stakeholders-and-definition-of-their-perspectives-利益相关方的识别及其角度的定义)
      - [F.3.3 Definition of aspects 方面体的定义](#f33-definition-of-aspects-方面体的定义)
      - [F.3.4 Specification of architecture viewpoint 架构视角规格](#f34-specification-of-architecture-viewpoint-架构视角规格)
      - [F.3.5 Specification of formalisms and languages 形式体系与语言的规格](#f35-specification-of-formalisms-and-languages-形式体系与语言的规格)
    - [F.4 Compliance with ADF requirements 对 ADF 要求的符合性](#f4-compliance-with-adf-requirements-对-adf-要求的符合性)
  - [Bibliography 参考文献](#bibliography-参考文献)
  - [IEEE Notices and Abstract IEEE 通告与摘要](#ieee-notices-and-abstract-ieee-通告与摘要)
      - [ICS 35.080 ISBN 978-1-5044-9155-6 STD25753 (PDF); 978-1-5044-9156-3 STDPD25753 (Print) ICS 35.080 ISBN 978-1-5044-9155-6 STD25753（PDF）；978-1-5044-9156-3 STDPD25753（印刷版）](#ics-35080-isbn-978-1-5044-9155-6-std25753-pdf-978-1-5044-9156-3-stdpd25753-print-ics-35080-isbn-978-1-5044-9155-6-std25753pdf978-1-5044-9156-3-stdpd25753印刷版)

---

---

## Cover and copyright pages (source lay-out, verbatim) 封面与版权页（按原版版面照录）

42010

42010

Second edition

第二版

2022-11

2022-11

Software, systems and enterprise — Architecture description

软件、系统与企业 — 架构描述

Logiciel, systèmes et entreprise — Description de l'architecture

软件、系统与企业 — 架构描述

Reference number ISO/IEC/IEEE 42010:2022(E)

参考编号 ISO/IEC/IEEE 42010:2022(E)

COPYRIGHT PROTECTED DOCUMENT

受版权保护的文件

© ISO/IEC 2022 © IEEE 2022 All rights reserved. Unless otherwise specified, or required in the context of its implementation, no part of this publication may be reproduced or utilized otherwise in any form or by any means, electronic or mechanical, including photocopying, or posting on the internet or an intranet, without prior written permission. Permission can be requested from either ISO or IEEE at the respective address below or ISO’s member body in the country of the requester.

© ISO/IEC 2022 © IEEE 2022 版权所有。除非另有规定，或在实施本文件的语境中有所要求，未经事先书面许可，不得以任何形式或任何手段（电子的或机械的，包括影印以及在国际互联网或内联网上发布）复制或以其他方式利用本出版物的任何部分。许可可向 ISO 或 IEEE（地址见下文各自地址）或向请求者所在国家的 ISO 成员机构申请。

ISO copyright office Institute of Electrical and Electronics Engineers, Inc CP 401 • Ch. de Blandonnet 8 3 Park Avenue, New York CH-1214 Vernier, Geneva NY 10016-5997, USA Phone: +41 22 749 01 11 Fax: +41 22 749 09 47 Email: copyright@iso.org Email: stds.ipr@ieee.org Website: www.iso.org Website: www.ieee.org Published in Switzerland

ISO 版权办公室 Institute of Electrical and Electronics Engineers, Inc CP 401 • Ch. de Blandonnet 8 3 Park Avenue, New York CH-1214 Vernier, Geneva NY 10016-5997, USA 电话：+41 22 749 01 11 传真：+41 22 749 09 47 电子邮件：copyright@iso.org 电子邮件：stds.ipr@ieee.org 网址：www.iso.org 网址：www.ieee.org 在瑞士出版

---

## Foreword 前言

ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) form the specialized system for worldwide standardization. National bodies that are members of ISO or IEC participate in the development of International Standards through technical committees established by the respective organization to deal with particular fields of technical activity. ISO and IEC technical committees collaborate in fields of mutual interest. Other international organizations, governmental and non-governmental, in liaison with ISO and IEC, also take part in the work.

ISO（国际标准化组织）和 IEC（国际电工委员会）构成世界范围标准化的专门体系。作为 ISO 或 IEC 成员的国家机构，通过各该组织为处理特定技术活动领域而设立的技术委员会，参与国际标准的制定。ISO 与 IEC 的技术委员会在共同感兴趣的领域开展合作。与 ISO 和 IEC 有联络的其他国际组织，政府的和非政府的，也参与此项工作。

The procedures used to develop this document and those intended for its further maintenance are described in the ISO/IEC Directives, Part 1. In particular, the different approval criteria needed for the different types of ISO/IEC documents should be noted. This document was drafted in accordance with the rules given in the ISO/IEC Directives, Part 2 (see www.iso.org/directives or www.iec.ch/members_experts/refdocs).

用于制定本文件的程序以及旨在对其进一步维护的程序，在《ISO/IEC 导则 第1部分》中描述。尤其宜注意，不同类型的 ISO/IEC 文件需要不同的批准准则。本文件依据《ISO/IEC 导则 第2部分》给出的规则起草（见 www.iso.org/directives 或 www.iec.ch/members_experts/refdocs）。

IEEE Standards documents are developed within the IEEE Societies and the Standards Coordinating Committees of the IEEE Standards Association (IEEE-SA) Standards Board. The IEEE develops its standards through a consensus development process, approved by the American National Standards Institute, which brings together volunteers representing varied viewpoints and interests to achieve the final product. Volunteers are not necessarily members of the Institute and serve without compensation. While the IEEE administers the process and establishes rules to promote fairness in the consensus development process, the IEEE does not independently evaluate, test, or verify the accuracy of any of the information contained in its standards.

IEEE 标准文件由 IEEE 各协会以及 IEEE 标准协会（IEEE-SA）标准委员会的标准协调委员会制定。IEEE 通过协商一致制定过程来制定其标准，该过程由美国国家标准学会批准，它汇集代表各种观点和利益的志愿者以形成最终产品。志愿者不一定是该学会的成员，且不取报酬。尽管 IEEE 管理该过程并制定规则以促进协商一致制定过程中的公平性，但 IEEE 并不独立评估、测试或验证其标准中所含任何信息的准确性。

Attention is drawn to the possibility that some of the elements of this document may be the subject of patent rights. ISO and IEC shall not be held responsible for identifying any or all such patent rights. Details of any patent rights identified during the development of the document will be in the Introduction and/or on the ISO list of patent declarations received (see www.iso.org/patents) or the IEC list of patent declarations received (see https://patents.iec.ch).

提请注意，本文件的某些内容可能涉及专利权。ISO 和 IEC 不应负责识别任何或所有此类专利权。在制定本文件过程中识别出的任何专利权的细节，将载于引言和／或 ISO 已收到的专利声明清单（见 www.iso.org/patents）或 IEC 已收到的专利声明清单（见 https://patents.iec.ch）中。

Any trade name used in this document is information given for the convenience of users and does not constitute an endorsement.

本文件中使用的任何商品名称均为方便使用者而提供的信息，不构成对其的认可。

For an explanation of the voluntary nature of standards, the meaning of ISO specific terms and expressions related to conformity assessment, as well as information about ISO's adherence to the World Trade Organization (WTO) principles in the Technical Barriers to Trade (TBT), see www.iso.org/iso/foreword.html. In the IEC, see www.iec.ch/understanding-standards.

关于标准的自愿性质、与合格评定有关的 ISO 特定术语和表述的含义，以及有关 ISO 遵守世界贸易组织（WTO）《技术性贸易壁垒（TBT）协定》原则的信息，见 www.iso.org/iso/foreword.html。在 IEC 中，见 www.iec.ch/understanding-standards。

ISO/IEC/IEEE 42010 was prepared by Joint Technical Committee ISO/IEC JTC 1, *Information technology*, Subcommittee SC 7, *Software and systems engineering*, in cooperation with the Software and Systems Engineering Standards Committee of the Computer Society of the IEEE, under the Partner Standards Development Organization cooperation agreement between ISO and IEEE.

ISO/IEC/IEEE 42010 由 ISO/IEC JTC 1*信息技术*技术委员会、SC 7*软件与系统工程*分委员会，与 IEEE 计算机学会软件与系统工程标准委员会合作，依据 ISO 与 IEEE 之间的伙伴标准制定组织合作协议制定。

This second edition cancels and replaces the first edition (ISO/IEC/IEEE 42010:2011), which has been technically revised.

本第二版取消并代替第一版（ISO/IEC/IEEE 42010:2011），后者已经过技术修订。

The main changes are as follows:

主要变化如下：

- The term used to refer to the subject of an architecture description is changed from “system of interest”

- 用于指称架构描述的主体的术语由“所关注系统”

to “entity of interest” (EoI) to be compatible with ISO/IEC/IEEE 42020 and ISO/IEC/IEEE 42030 standards and to allow for its application in non-system architecture situations. The term “entity” is also used in this document when entities are considered as surrounding things in an environment of an EoI.

改为“所关注实体”（EoI），以与 ISO/IEC/IEEE 42020 和 ISO/IEC/IEEE 42030 标准保持一致，并使本文件能适用于非系统的架构情形。本文件中，当诸实体被视为某个 EoI 的环境中的周围事物时，也使用“实体”这一术语。

- The term “architecture description framework” (ADF) replaces “architecture framework” in

- 术语“架构描述框架”（ADF）取代了

the previous edition. It is defined in order to differentiate ADFs from other kinds of architecting frameworks like architecture evaluation frameworks specified in ISO/IEC/IEEE 42030.

上一版中的“架构框架”。其定义旨在将 ADF 与 ISO/IEC/IEEE 42030 中规定的架构评估框架等其他各类架构工作框架区分开来。

- Architecture description element, introduced in the 2011 edition (see ISO/IEC/IEEE 42010:2011,

- 架构描述元素于 2011 版引入（见 ISO/IEC/IEEE 42010:2011 的

4.2.6, 5.7 and A.6) is now defined in Clause 3 as identified or named part of an architecture description allowing representing at least stakeholders, concerns, perspectives, and aspects identified in an AD, and views, view components, viewpoints, and model kinds included in an AD.

4.2.6、5.7 和 A.6），现于第 3 章定义为架构描述中经标识或命名的部分，其至少能表示 AD 中标识的诸利益相关方、关注点、角度和方面体，以及 AD 中所含的诸架构视图、视图组件、架构视角和模型种类。

- Aspect and stakeholder perspective concepts ―already introduced in the 2011 edition (See 3.5, note

- 方面体和利益相关方角度这两个概念——2011 版中已引入（见 3.5、5.6 的注

1 of 5.6, Annex A and B) are defined and described to accommodate current practice where these ideas are prevalent.

1、附录 A 和 B）——现予以定义和描述，以适应这些观念盛行的当前实践。

- A correspondence defines an identified or named relation between AD elements, as in Clause 4.2.6

- 对应关系定义了 AD 元素之间经标识或命名的关系，如 2011 版第 4.2.6 条中所述。但是，为澄清 AD 与对应关系之间的关系，

of the 2011 edition. But, to clarify the relationship between AD and correspondence, a note 1 to the definition is added to state that for the purpose of correspondences, an architecture description can be considered as an AD element in another architecture description. This correspondence between ADs is necessary because an architecture can be described by more than one AD and these alternatives of architectures have related for activities like trade-off analysis and decision making.

为该定义增补了注 1，说明：为对应关系之目的，一个架构描述可视为另一架构描述中的一个 AD 元素。AD 之间的这种对应关系是必要的，因为一个架构可由不止一个 AD 来描述，而这些架构备选方案与权衡分析和决策等活动相关。

- The term “architecture view component” is introduced as a separable portion of one or more

- 引入术语“架构视图组件”作为对一个或多个架构视图的可分部分的称谓，

architecture views, replacing “architecture model” in the 2011 edition. This change is to account for the fact that some parts of a view are model-based while others may not be. View components can be derived from an information source, which can sometimes be a model.

以取代 2011 版中的“架构模型”。此变化是为顾及如下事实：架构视图的某些部分是模型式的，而另一些部分可能不是。视图组件可派生自某一信息源，该信息源有时可以是一个模型。

- Model-based view components are governed by model kinds and documented by legends. Non-

- 基于模型的视图组件由模型种类所管控，并由图例加以记录。非

model-based view components are documented by legends.

基于模型的视图组件由图例加以记录。

- Model kinds are identified as a new conformance case to encourage model-based architecting.

- 模型种类被确定为新的符合性情形，以鼓励基于模型的架构工作。

- The concept of architecture viewpoint is updated to accommodate current practice where a

- 架构视角这一概念得到更新，以适应由一个

viewpoint governs one or more architecture views within an AD.

视角管控一个 AD 内一个或多个架构视图的当前实践。

- The definition of “model kind” given by the 2011 edition is extended to include categories of models

- 2011 版给出的“模型种类”定义得到扩展，以纳入诸模型类别，

as used by ADF like UAF.

2011 版给出的“模型种类”定义得到扩展，以纳入 ADF 如 UAF 所使用的诸模型类别。

- The figures use an informal entity-relationship diagram notation replacing UML class diagrams in

- 各图采用非正式的实体—关系图记法，取代 2011 版中的 UML 类图，

the 2011 edition, to facilitate comprehension by users of this document. The multiplicities of the relationships are explained in the text when necessary.

以便利本文件使用者的理解。必要时在正文中说明各关系的重数。

- Annex E illustrates a few concepts pertaining to architecture life cycles and architecture description

- 附录 E 举例说明若干与架构生存周期和架构描述

life cycles.

生存周期有关的概念。

- Annex F shows examples of how some architecture description frameworks can conform to

- 附录 F 给出若干架构描述框架如何能符合

requirements of this document.

本文件各项要求的示例。

Any feedback or questions on this document should be directed to the user’s national standards body. A complete listing of these bodies can be found at www.iso.org/members.html and www.iec.ch/national-committees.

对本文件的任何反馈或问题应提交给使用者的国家标准化机构。这些机构的完整名录见 www.iso.org/members.html 和 www.iec.ch/national-committees。

## Introduction 引言

The complexity of human-made entities has grown to an unprecedented level. This has led to new opportunities, and also increased challenges for organizations that create and use these entities. Architecting is increasingly applied by organizations, teams and individuals, to help manage the complexity faced by stakeholders of these entities.

人造实体的复杂性已增长到前所未有的水平。这为创建和使用这些实体的组织带来了新的机会，也带来了更大的挑战。组织、团队和个人越来越多地应用架构工作，以帮助管理这些实体的利益相关方所面对的复杂性。

Examples of entities include the following: Enterprise, organization, solution, system (including software systems), subsystem, process, business, data (as a data item or data structure), application, information technology (as a collection), mission, product, service, software item, hardware item, product line, family of systems, system of systems, collection of systems, collection of applications.

实体的示例包括：企业、组织、解决方案、系统（包括软件系统）、分系统、过程、业务、数据（作为数据项或数据结构）、应用、信息技术（作为集合）、使命、产品、服务、软件项、硬件项、产品线、系统族、系统的系统、系统集合、应用集合。

An architecture of an entity, expressed in one or more architecture descriptions (AD), assists in understanding the fundamental concepts or properties of the entity, pertaining to its structure, behaviour, design and evolution, such as feasibility, utility and maintainability and fundamental concepts for its development, operation, employment, external impacts, utilization and decommissioning.

实体的架构以一个或多个架构描述（AD）来表达，有助于理解该实体的基本概念或属性——涉及其结构、行为、设计和演化，诸如可行性、效用和可维护性，以及涉及其开发、运行、使用、外部影响、利用和退役的基本概念。

ADs are used by the parties that create, use and manage human-made entities to improve communication and cooperation, enabling all parties, organizations, teams and individuals to work together in an integrated and coherent fashion.

AD 由创建、使用和管理人造实体的各方使用，以改善沟通与合作，使所有各方、组织、团队和个人能以集成而连贯的方式协同工作。

> **NOTE** ISO/IEC/IEEE 42020 specifies a set of processes for architecting which can be employed in support of creating one or more ADs. The architecture elaboration process in ISO/IEC/IEEE 42020 is especially relevant for creation of ADs.

> **注**：ISO/IEC/IEEE 42020 规定了一组可用于支持创建一个或多个 AD 的架构工作过程。ISO/IEC/IEEE 42020 中的架构细化过程与 AD 的创建尤为相关。

Whereas an AD is a tangible work product, an architecture is intangible and abstract, understood through its concepts, properties and principles.

AD 是有形的工作产品，而架构是无形的、抽象的，需通过其概念、属性和原则来理解。

Architecture description frameworks (ADF) are used to codify the conventions and common practices of architecture description. Architecture description languages (ADL) are used to codify the description of architectures within different communities and domains of application.

架构描述框架（ADF）用于编集架构描述的惯例和通行实践。架构描述语言（ADL）用于编集不同群体和应用领域中架构的描述。

ADs have many uses, such as design, development, documentation, analysis, evaluation, maintenance, risk mitigation, downstream user specifications, tool specification, communication, planning, guidance, life cycle support, decision support, review, training, design validation, solution trade studies, cost comparison and analysis, by a variety of stakeholders throughout the life cycles of their entities of interest. Annex D describes more uses of an AD.

AD 有许多用途，诸如设计、开发、文档编制、分析、评估、维护、风险缓解、下游使用者规格、工具规格、沟通、策划、指导、生存周期支持、决策支持、评审、培训、设计确认、解决方案权衡研究、成本比较和分析，供各类利益相关方在其所关注实体的整个生存周期中使用。附录 D 描述了 AD 的更多用途。

This document provides terms, definitions and relationships for best practices in ADs. The provisions of this document serve to specify desired properties of ADs. This document also gives provisions that specify desired properties of ADFs and ADLs in order to usefully support the development and use of ADs. This document provides a basis for considering and comparing ADFs and ADLs by providing a common ontology for specifying their contents.

本文件提供 AD 最佳实践的术语、定义和关系。本文件的规定用于规定 AD 的期望属性。本文件还给出了规定 ADF 和 ADL 期望属性的规定，以有效支持 AD 的开发和使用。本文件通过提供用于规定其内容的公共本体论，为考察和比较架构描述框架（ADF）和架构描述语言（ADL）提供了基础。

This document can be used to establish a coherent architecting practice for developing ADs, ADFs and ADLs within an organization, in the context of an entity of interest (EoI) or its architecture. The provisions of this document can be used to assess conformance of specifications of ADs, ADFs, ADLs, viewpoints and model kinds.

本文件能用于在一个组织内，在所关注实体（EoI）或其架构的语境中，建立用于开发 AD、ADF 和 ADL 的连贯的架构工作实践。本文件的各项规定能用于评定 AD、ADF、ADL、视角和模型种类的规格的符合性。

The intent of this document is to enable a range of consistent and coherent approaches to describing an architecture including document-centric and model-based techniques.

本文件的意图在于使一系列一致的、连贯的途径能用于描述架构，包括以文档为中心的技术和基于模型的技术。

This document also provides motivations for use of architecture-related terms and concepts in other documents such as guides and standards.

本文件还为在其他文件（如指南和标准）中使用架构相关的术语和概念提供了动因。

Users of this document are advised to consult Clause 5 to gain appreciation of the conceptual foundations, along with the concepts and principles associated with an AD work product.

建议本文件的使用者查阅第 5 章，以领会其概念基础，以及与 AD 工作产品相关的概念和原则。

This document does not explicitly address completeness or correctness regarding the inclusion of particular elements in an AD. Nevertheless, completeness and correctness of an AD can be partially checked, for example, through the consistency of the AD elements established, whether relationships are transitive, and whether AD elements are shown in the views. Consistency rules can also be defined by showing whether the same particular AD element has correspondences with an AD. In addition, specifications that appear as elements within an AD are expected to be complete, precise and verifiable with respect to the subject of the specification.

本文件未明确述及 AD 中纳入特定元素的完备性或正确性。然而，AD 的完备性和正确性能部分地得到检查，例如通过所确立的 AD 元素的一致性、关系是否是可传递的、以及 AD 元素是否在诸架构视图中示出。一致性规则还能通过表明同一特定 AD 元素是否与 AD 具有对应关系来定义。此外，作为元素出现在 AD 中的规格，就其主体而言，预期是完备的、精确的和可验证的。

In this document, the following verbal forms are used:

本文件中使用下列动词形式：

- “shall” indicates a requirement;

- “shall”表示要求；

- “should” indicates a recommendation;

- “should”表示建议；

- “may” indicates a permission.

- “may”表示许可。

## Software, systems and enterprise — Architecture description 软件、系统与企业 — 架构描述

### 1 Scope 范围

This document specifies requirements for the structure and expression of an architecture description (AD) for various entities, including software, systems, enterprises, systems of systems, families of systems, products (goods or services), product lines, service lines, technologies and business domains.

本文件规定了针对各类实体的架构描述（AD）的结构与表达的要求，这些实体包括软件、系统、企业、系统的系统、系统族、产品（货物或服务）、产品线、服务线、技术和业务域。

This document distinguishes the architecture of an entity of interest from an AD expressing that architecture. Architectures are not the subject of this document.

本文件将所关注实体的架构与表达该架构的 AD 区分开来。架构不是本文件的主题。

This document specifies requirements for use of the architectural concepts and their relationships as captured in an AD. It does not specify requirements for any entity of interest or its environment.

本文件规定了使用 AD 中所记载的架构概念及其关系的要求。本文件不规定任何所关注实体或其环境的要求。

This document specifies requirements for an architecture description framework (ADF), an architecture description language (ADL), architecture viewpoints and model kinds in order to usefully support the development and use of an AD.

本文件规定了架构描述框架（ADF）、架构描述语言（ADL）、架构视角和模型种类的要求，以有效支撑 AD 的开发和使用。

This document specifies conformance to the requirements for an AD, ADF, ADL, architecture viewpoint and model kind.

本文件规定了针对 AD、ADF、ADL、架构视角和模型种类的各项要求的符合性。

This document does not specify the processes, architecting methods, models, notations, techniques or tools by which an AD is created, utilized or managed.

本文件不规定创建、使用或管理 AD 所借助的过程、架构工作方法、模型、记法、技术或工具。

This document does not specify any format or media for recording an AD.

本文件不规定记录 AD 的任何格式或介质。

### 2 Normative references 规范性引用文件

There are no normative references in this document.

本文件没有规范性引用文件。

### 3 Terms and definitions 术语和定义

For the purposes of this document, the following terms and definitions apply.

下列术语和定义适用于本文件。

ISO, IEC and IEEE maintain terminology databases for use in standardization at the following addresses:

ISO、IEC 和 IEEE 为供标准化使用而维护术语数据库，网址如下：

- ISO Online browsing platform: available at https:// www .iso .org/ obp/ ui

- ISO 在线浏览平台：可在 https:// www .iso .org/ obp/ ui 获取

- IEC Electropedia: available at https:// www .electropedia .org/

- IEC Electropedia：可在 https:// www .electropedia .org/ 获取

- IEEE Standards Dictionary Online: available at https:// dictionary .ieee .org/

- IEEE Standards Dictionary Online：可在 https:// dictionary .ieee .org/ 获取

> **NOTE** For additional terms and definitions in the field of systems and software engineering, see ISO/IEC/IEEE 24765, which is published periodically as a “snapshot” of the SEVOCAB (Systems and software Engineering Vocabulary) database and is publicly accessible at www .computer .org/ sevocab.

> **注**：关于系统和软件工程领域的附加术语和定义，见 ISO/IEC/IEEE 24765，该文件定期发布，作为 SEVOCAB（系统与软件工程词汇）数据库的“快照”，并可在 www .computer .org/ sevocab 公开访问。

#### 3.1 architecting 架构工作

conceiving, defining, expressing, documenting, communicating, certifying proper implementation of, maintaining and improving an *architecture* (3.2) throughout the life cycle of an *entity of interest* (3.12)

在*所关注实体*(3.12)的整个生存周期内，对*架构*(3.2)进行构想、定义、表达、编制文档、沟通、证实其正确实施、维护和改进

#### 3.2 architecture 架构

fundamental concepts or properties of an entity in its *environment* (3.13) and governing principles for the realization and evolution of this entity and its related life cycle processes

实体在其*环境*(3.13)中的基本概念或属性，以及为实现和演化该实体及其相关生存周期过程的管控原则

> [SOURCE: ISO/IEC/IEEE 42020:2019, 3.3, modified — The notes to entry have been removed.]

> **来源**：ISO/IEC/IEEE 42020:2019，3.3，修改——注文已删除。

#### 3.3 architecture description / AD ｜ 架构描述 / AD

work product used to express an *architecture* (3.2)

用于表达*架构*(3.2)的工作产品

> **Note 1 to entry:** A work product is an artifact produced by a process (see ISO/IEC 20246:2017, 3.18).

> **注 1**：工作产品是由过程产生的人工制品（见 ISO/IEC 20246:2017, 3.18）。

> **Note 2 to entry:** An AD is a tangible representation of information provided to the *stakeholders* (3.17). An AD is considered an *information part* (3.14).

> **注 2**：AD 是提供给*利益相关方*(3.17)的信息的有形表示。AD 被视为*信息部件*(3.14)。

#### 3.4 architecture description element / AD element ｜ 架构描述元素 / AD 元素

identified or named part of an *architecture description* (3.3)

*架构描述*(3.3)中经标识或命名的部分

> **Note 1 to entry:** AD elements include *stakeholders* (3.17), *concerns* (3.10), *stakeholder perspectives* (3.18), and *aspects* (3.9) identified in an *AD* (3.3), *ADLs* (3.6), *ADFs* (3.5) and *correspondences* (3.11) and correspondence methods used in an AD, and *architecture views* (3.7), *view components* (3.19), *architecture viewpoints* (3.8), and *model kinds* (3.15) included in an *AD* (3.3).

> **注 1**：AD 元素包括*AD*(3.3)、*ADL*(3.6)、*ADF*(3.5) 中所标识的*利益相关方*(3.17)、*关注点*(3.10)、*利益相关方角度*(3.18) 和 *方面体*(3.9)，AD 中所用的*对应关系*(3.11) 与对应方法，以及*AD*(3.3) 中所含的*架构视图*(3.7)、*视图组件*(3.19)、*架构视角*(3.8) 和 *模型种类*(3.15)。

> **Note 2 to entry:** For the purpose of *correspondences* (3.11), an *AD* (3.3) can be considered as an AD element in another *AD* (3.3).

> **注 2**：为*对应关系*(3.11)之目的，一个*AD*(3.3) 能视为另一个*AD*(3.3) 中的一个 AD 元素。

#### 3.5 architecture description framework / ADF ｜ 架构描述框架 / ADF

conventions, principles and practices for the description of *architectures* (3.2) established within a specific domain of application or community of *stakeholders* (3.17)

在特定应用领域或*利益相关方*(3.17)群体内确立的、用于描述*架构*(3.2)的惯例、原则和实践

> **EXAMPLE** Generalized Enterprise-Referencing Architectures Modelling Framework (GERAM) (ISO 15704:2019, Annex B), Reference Model of Open Distributed Processing (RM-ODP),[2] Unified Architecture Framework (UAF)[48], and NATO Architecture Framework (NAF)[44].

> **示例**：泛化企业参照架构建模框架（GERAM）（ISO 15704:2019，附录 B）、开放分布式处理参考模型（RM-ODP）[2]、统一架构框架（UAF）[48] 和 NATO 架构框架（NAF）[44]。

> **Note 1 to entry:** Architecture description frameworks promote structured organization, consistency of description, greater potential for reuse, and completeness of *architecture views* (3.7) and models.

> **注 1**：架构描述框架能促进结构化的组织、描述的一致性、更大的复用潜力，以及*架构视图*(3.7)和模型的完备性。

#### 3.6 architecture description language / ADL ｜ 架构描述语言 / ADL

means of expression, with syntax and semantics, consisting of a set of representations, conventions, and associated rules intended to be used to describe an *architecture* (3.2)

具有语法和语义的表达手段，由一组表示、惯例及相关规则构成，旨在用于描述*架构*(3.2)

> **EXAMPLE** Architecture Analysis and Design Language (AADL),[57] ArchiMate,[61] UML,[49] SysML,[47] UAF Profile[48].

> **示例**：架构分析与设计语言（AADL）[57]、ArchiMate[61]、UML[49]、SysML[47]、UAF Profile[48]。

#### 3.7 architecture view 架构视图

*information part* (3.14) comprising portion of an *architecture description* (3.3)

包含*架构描述*(3.3)的一部分的*信息部件*(3.14)

> **EXAMPLE** An Information or Data View addresses information-relevant concerns framed by an Information viewpoint. It contains as *view components* (3.19), a conceptual data model, a data management model and a data access model and correspondences linking those components together.

> **示例**：信息视图或数据视图应对由信息视角所框定的与信息相关的关注点。其作为*视图组件*(3.19)包含概念数据模型、数据管理模型和数据访问模型，以及将这些组件联系在一起的对应关系。

#### 3.8 architecture viewpoint 架构视角

set of conventions for the creation, interpretation and use of an *architecture view* (3.7) to frame one or more *concerns* (3.10)

用于创建、解释和使用*架构视图*(3.7)以框定一项或多项*关注点*(3.10)的一组惯例

> **Note 1 to entry:** In this document, “to frame” concerns means “to shape, compose, give expression to” those concerns. It is used to distinguish the stages of framing concerns by a viewpoint from addressing those concerns in a resulting view. This is analogous to the distinction between “framing a problem” and “solving that problem”.

> **注 1**：在本文件中，“框定”关注点意指“塑造、组织、表达”那些关注点。使用该表述是为了区分由视角框定关注点这一阶段与在所得架构视图中应对那些关注点这一阶段。这类似于“框定问题”与“解决该问题”之间的区分。

> **Note 2 to entry:** A viewpoint is a frame of reference for the concerns determined by the architect as relevant to the purpose of the *architecture description* (3.3).

> **注 2**：架构视角是架构师所确定的、被认为与*架构描述*(3.3)的目的相关的那些关注点的参考框架。

> **Note 3 to entry:** The conventions of an architecture viewpoint are documented in a *specification* (3.16) of that viewpoint. In some communities and architecture description frameworks, “view specification” and viewpoint are synonyms.

> **注 3**：架构视角的约定记录在该视角的*规格*(3.16)中。在某些团体和架构描述框架中，“视图规格”与视角是同义词。

> **Note 4 to entry:** The identification of a viewpoint is often the result of prior knowledge, experience and praxis in the domain(s) to which the viewpoint applies, indicating the information relevant to addressing the *concern* (3.10).

> **注 4**：视角的识别往往是该视角所适用的一个或多个领域中的先验知识、经验和实践的结果，其指示了与处理*关注点*(3.10)相关的信息。

#### 3.9 aspect 方面体

part of an entity’s character or nature EXAMPLE Functional, structural and informational aspects of an entity.

实体的特性或本质的组成部分示例：实体的功能方面体、结构方面体和信息方面体。

> **Note 1 to entry:** A particular aspect can be used for capturing the relevant features of the *entity of interest* (3.12) as a refinement of one or more *concerns* (3.10) under examination with respect to some part of its character, e.g. the structural character, functional character or informational character of the entity.

> **注 1**：特定方面体可用于捕获*所关注实体*(3.12)的相关特征，其方式是针对该实体特性的某个部分，例如该实体的结构特性、功能特性或信息特性，对所考察的一项或多项*关注点*(3.10)加以细化。

> **Note 2 to entry:** Aspects enable the architect to analyse, address and structure *concerns* (3.10). In general, there is a many-to-many relation between aspects and *concerns* (3.10).

> **注 2**：方面体使架构师能够分析、处理和构造*关注点*(3.10)。一般而言，方面体与*关注点*(3.10)之间是多对多关系。

> **Note 3 to entry:** See 5.2.5 for more discussion and examples.

> **注 3**：更多讨论和示例见 5.2.5。

#### 3.10 concern 关注点

matter of relevance or importance to a *stakeholder* (3.17)

对*利益相关方*(3.17)而言具有相关性或重要性的事项

> **Note 1 to entry:** concerns can be identified with regards to an *entity of interest* (3.12) or independently, such as with regards to environment, scenario, situation or use case of that entity.

> **注 1**：关注点可针对*所关注实体*(3.12)来识别，也可独立识别，例如针对该实体的环境、场景、情形或用例来识别。

> **Note 2 to entry:** In this document, interest in an entity is intended to encompass interest in that entity’s *environment* (3.13), life cycle, *architecture* (3.2), requirements, design, implementation and operation. Such interests are captured via *aspects* (3.9), concerns and *stakeholder perspectives* (3.18).

> **注 2**：在本文件中，对实体的关注旨在涵盖对该实体的*环境*(3.13)、生存周期、*架构*(3.2)、要求、设计、实施和运行的关注。此类关注经由*方面体*(3.9)、关注点和*利益相关方角度*(3.18)来捕获。

> **Note 3 to entry:** The identification of a concern is often the result of prior knowledge, experience and praxis in the domain to which the concern applies.

> **注 3**：关注点的识别往往是该关注点所适用领域中的先验知识、经验和实践的结果。

> **Note 4 to entry:** See 5.2.3 for more discussion and examples.

> **注 4**：更多讨论和示例见 5.2.3。

> [SOURCE: ISO/IEC/IEEE 42020:2019, 3.8, Notes have been modified]

> **来源**：ISO/IEC/IEEE 42020:2019，3.8，注已修改

#### 3.11 correspondence 对应关系

identified or named relationship between two or more *architecture description elements* (3.4)

两个或多个*架构描述元素*(3.4)之间经识别或命名的关系

> **EXAMPLE** Correspondences are used to express a wide range of relationships, such as equivalence, composition, refinement, consistency, traceability, dependency, constraint, satisfaction, and obligation.

> **示例**：对应关系用于表达各种关系，例如等价、组成、细化、一致性、可追溯性、依赖、约束、满足和义务。

> **Note 1 to entry:** For the purpose of correspondences, an *architecture description* (3.3) can be considered as an *AD* *element* (3.4) in another *architecture description* (3.3).

> **注 1**：就对应关系而言，一个*架构描述*(3.3)能被视为另一*架构描述*(3.3)中的一个*AD* *元素*(3.4)。

> **Note 2 to entry:** Correspondences can be identified or named relationship between *architecture description* *elements* (3.4) in different *architecture descriptions* (3.3) or between *architecture description elements* (3.4) stated in different notations.

> **注 2**：对应关系能是不同*架构描述*(3.3)中的*架构描述* *元素*(3.4)之间、或以不同表示法表述的*架构描述元素*(3.4)之间经识别或命名的关系。

#### 3.12 entity of interest / EoI ｜ 所关注实体 / EoI

subject of an *architecture description* (3.3)

*架构描述*(3.3)的主体

> **EXAMPLE** Enterprise, organization, solution, system (including software systems), subsystem, process, business, data (as a data item or data structure), application, information technology (as a collection), mission, product, service, software item, hardware item, product line, family of systems, system of systems, collection of systems, collection of applications.

> **示例**：企业、组织、解决方案、系统（包括软件系统）、子系统、过程、业务、数据（作为数据项或数据结构）、应用、信息技术（作为集合）、使命、产品、服务、软件项、硬件项、产品线、系统族、系统的系统、系统集合、应用集合。

> **Note 1 to entry:** In this document, the term entity of interest refers to the entity whose *architecture* (3.2) is under consideration in the preparation of an *architecture description* (3.3).

> **注 1**：在本文件中，术语“所关注实体”指在编制*架构描述*(3.3)时正考虑其*架构*(3.2)的那个实体。

> **Note 2 to entry:** This document distinguishes the entity of interest from other entities which are not the subject of the *architecture description* (3.3).

> **注 2**：本文件将所关注实体与并非该*架构描述*(3.3)主体的其他实体区分开。

> **Note 3 to entry:** In this document, interest in an entity is intended to encompass interest in that entity’s environment, life cycle, architecture, requirements, design, implementation and operation. Such interests are captured via aspects, concerns and stakeholder perspectives.

> **注 3**：在本文件中，对实体的关注旨在涵盖对该实体的环境、生存周期、架构、要求、设计、实施和运行的关注。此类关注经由方面体、关注点和利益相关方角度来捕获。

#### 3.13 environment 环境

context of surrounding things, conditions, or influences upon an entity

围绕实体的事物、条件或影响所构成的情境

> **Note 1 to entry:** The environment of an *entity of interest* (3.12) includes external entities that can have various influences upon an *entity*, such as developmental, technological, business, operational, organizational, political, economic, legal, regulatory, ecological and social influences as well as external physical effects such as electromagnetic radiation, charged particles, gravitational effects, and electric and magnetic fields.

> **注 1**：*所关注实体*(3.12)的环境包括能对*实体*产生各种影响的外部实体，例如开发、技术、业务、运行、组织、政治、经济、法律、监管、生态和社会影响，以及电磁辐射、带电粒子、引力效应和电场与磁场等外部物理效应。

> **Note 2 to entry:** A label attached as a qualifier to the term environment identifies a particular context within another context, such as development environment, test environment, and operational environment.

> **注 2**：附加于术语“环境”作为限定语的标签，用于标识另一情境中的特定情境，例如开发环境、测试环境和运行环境。

#### 3.14 information part 信息部件

separately identifiable body of information that is produced, stored, and delivered for human and machine use

为供人和机器使用而生成、存储和交付的、可单独识别的信息体

#### 3.15 model kind 模型种类

category of model distinguished by its key characteristics and modelling conventions EXAMPLE Functional models, activity models, structural models, use case models, geopolitical models, analytic models and economic models.

以其关键特性和建模约定相区分的模型类别示例：功能模型、活动模型、结构模型、用例模型、地缘政治模型、分析模型和经济模型。

#### 3.16 specification 规格

*information part* (3.14) that identifies, in a complete, precise and verifiable manner, the requirements, design, behaviour, or other expected characteristics of an entity

以完整、精确和可验证的方式标识实体的要求、设计、行为或其他预期特征的*信息部件*(3.14)

> [SOURCE: ISO/IEC/IEEE 15289:2019, 3.1.26 — “a system, service or process” replaced with “an entity”, “information item” replaced with “information part”]

> **来源**：ISO/IEC/IEEE 15289:2019，3.1.26 —— 以“实体”替换“系统、服务或过程”，以“信息部件”替换“信息项”

#### 3.17 stakeholder 利益相关方

role, position, individual, organization, or classes thereof, having an interest, right, share, or claim, in an *entity of interest* (3.12)

对*所关注实体*(3.12)享有利益、权利、份额或主张的角色、职位、个人、组织或其类别

> **EXAMPLE** End users, operators, acquirers, owners, suppliers, architects, developers, builders, maintainers, regulators, taxpayers, certifying agencies, and markets.

> **示例**：最终用户、操作者、采购方、所有者、供方、架构师、开发者、构建者、维护者、监管机构、纳税人、认证机构和市场。

#### 3.18 stakeholder perspective 利益相关方角度

way of thinking about an *entity of interest* (3.12), especially as it relates to *concerns* (3.10)

思考*所关注实体*(3.12)的方式，特别是就其与*关注点*(3.10)相关而言

> **EXAMPLE** The labels given to the middle three rows (i.e. owner, designer and builder) of the Zachman framework[67] correspond to stakeholder perspectives. The rows in the Unified Architecture Framework[48] and NATO Architecture Framework[44] grids correspond to stakeholder perspectives (although they are called ”domains” and “subjects of concerns,” respectively in those frameworks). See 5.2.4 for more examples.

> **示例**：Zachman 框架[67]中间三行（即所有者、设计者和构建者）的标签对应于利益相关方角度。统一架构框架[48]和 NATO 架构框架[44]网格中的各行对应于利益相关方角度（尽管在这些框架中它们分别被称为“域”和“关注主题”）。更多示例见 5.2.4。

> **Note 1 to entry:** The way one thinks about an entity can be influenced by one’s beliefs, training, experience, knowledge, personality, character traits, culture, peer pressure, role or stance, etc.

> **注 1**：一个人思考实体的方式可能受其信念、培训、经验、知识、个性、性格特质、文化、同伴压力、角色或立场等的影响。

#### 3.19 view component / architecture view component ｜ 视图组件 / 架构视图组件

separable portion of one or more *architecture views* (3.7) that is governed by the applicable *model kind* (3.15) or legend EXAMPLE An architecture view component describing access control mechanisms can be used in several views of an *architecture description* (3.3) to explain functional flows, behaviour and security features of an entity.

一个或多个*架构视图*(3.7)中受适用的*模型种类*(3.15)或图例所支配的可分离部分示例：描述访问控制机制的架构视图组件可用于*架构描述*(3.3)的若干视图中，以解释实体的功能流、行为和安全特性。

> **Note 1 to entry:** In the context of an *architecture description* (3.3), a legend is an informal documentation of conventions.

> **注 1**：在*架构描述*(3.3)的语境中，图例是对约定的非正式记录。

### 4 Conformance 符合性

The requirements in this document are contained in Clauses 6, 7 and 8. There are five situations in which claims of conformance with the provisions of this document can be made.

本文件中的要求包含在第 6 章、第 7 章和第 8 章中。在五种情形下能作出符合本文件各项规定的声明。

1) When conformance is claimed for an architecture description, the claim shall demonstrate that the specification of the architecture description meets the requirements listed in Clause 6.

1) 当针对一个架构描述主张符合性时，该主张应证明该架构描述的规格满足第 6 章所列的要求。

2) When conformance is claimed for an architecture description framework, the claim shall demonstrate that the specification of the architecture description framework meets the requirements listed in 7.1.

2) 当针对一个架构描述框架主张符合性时，该主张应证明该架构描述框架的规格满足 7.1 所列的要求。

3) When conformance is claimed for an architecture description language, the claim shall demonstrate that the specification of the architecture description language meets the requirements listed in 7.2.

3) 当针对一个架构描述语言主张符合性时，该主张应证明该架构描述语言的规格满足 7.2 所列的要求。

4) When conformance is claimed for an architecture viewpoint, the claim shall demonstrate that the specification of the architecture viewpoint meets the requirements listed in 8.1.

4) 当针对一个架构视角主张符合性时，该主张应证明该架构视角的规格满足 8.1 所列的要求。

5) When conformance is claimed for a model kind, the claim shall demonstrate that the specification of the model kind meets the requirements listed in 8.2.

5) 当针对一个模型种类主张符合性时，该主张应证明该模型种类的规格满足 8.2 所列的要求。

This document is designed such that “tailoring” is neither required nor permitted for its use when claims of conformance are made.

本文件的设计使得：在提出符合性主张时，其使用既不要求也不允许“裁剪”。

### 5 Conceptual foundations 概念基础

#### 5.1 General **5.1 总则**

This clause introduces the conceptual foundations of architecture description expressed in a set of conceptual models (see 5.2) and the application of those foundations to ADs (5.2), ADFs (see 5.4.2) and ADLs (see 5.4.3). The use of the architecture descriptions to support different architecture practices is outlined in Annex D. The concepts introduced in this clause are used in Clauses 6 to 8 to express requirements.

本章介绍架构描述的概念基础，其表达为一组概念模型（见 5.2），以及这些基础在 AD(5.2)、ADF（见 5.4.2）和 ADL（见 5.4.3）上的应用。架构描述用于支持不同架构实践的方式在附录 D 中概述。本章所介绍的概念在第 6 章至第 8 章中用于表达要求。

> **NOTE** Annex A provides further discussion of the terms and concepts used in this document and presents examples of their use in an historical context.

> **注**：附录 A 进一步讨论本文件所用的术语和概念，并在历史语境中给出其使用示例。

#### 5.2 Conceptual models of an architecture description **5.2 架构描述的概念模型**

##### 5.2.1 Context of architecture description 架构描述的语境

The term "entity of interest" is used in this document to refer to the subject of an architecture description. The term is intended to encompass, but is not limited to, entities within the following fields of application, reflecting the intended scope of this document as specified in Clause 1.

本文件使用术语“所关注实体”指称架构描述的主体。该术语旨在涵盖（但不限于）下列应用领域内的实体，以反映第 1 章所规定的本文件预期范围。

- software, including software products and services, per ISO/IEC/IEEE 12207;

- 软件，包括软件产品和服务，按 ISO/IEC/IEEE 12207；

- systems, including one-of-a-kind systems, mass-produced systems, customized, adaptive systems,

- 系统，包括单件系统、批量生产系统、定制系统、自适应系统，

stand-alone and embedded systems, per ISO/IEC/IEEE 15288;

独立系统和嵌入式系统，按 ISO/IEC/IEEE 15288；

- enterprises as described in ISO 15704, i.e. human undertakings or ventures that have mission, goals

- ISO 15704 所述的企业，即为提供产品或服务、或为实现预期项目成果或业务成果而具有使命、目标

and objectives to offer products or services, or to achieve a desired project outcome or business outcome.

和目的的人类事业或经营事业。

This document takes no position on what constitutes an entity within those or other fields of application or elsewhere. An entity can be a concrete entity or an abstract entity. An AD as specified in this document is suitable not only for entities in the fields of applications listed above, but also for entities in fields such as natural systems or conceptual systems.

对于上述或其他应用领域内以及别处何者构成实体，本文件不持立场。实体能是具体实体，也能是抽象实体。本文件所规定的 AD 不仅适用于上述应用领域内的实体，也适用于诸如自然系统或概念系统等领域内的实体。

Each entity of interest is situated in an environment which influences its characteristics and behaviours. The environment determines the totality of influences upon the entity of interest and the totality of influences of the entity of interest upon that environment, including its interactions with the environment and other entities, throughout the life cycle of that entity of interest.

每个所关注实体都处于某一环境之中，该环境影响其特性和行为。在该所关注实体的整个生存周期内，该环境决定了作用于该所关注实体的全部影响，以及该所关注实体作用于该环境的全部影响，包括与该环境及其他实体的交互。

Figure 1 depicts key concepts pertaining to an entity of interest and its architectures as a means of understanding ADs.

图 1 描绘了与所关注实体及其诸架构有关的关键概念，作为理解 AD 的一种手段。

> **NOTE 1** The figures and text in the remainder of Clause 5 constitute a set of conceptual models of architecture description. Figures 1 to 6 use an informal entity-relationship diagram notation to facilitate comprehension by users of this document. In the figures, rounded rectangles represent information objects, and arrows represent relationships between objects with the annotation read in the arrow direction. The figures illustrate the key concepts described throughout Clause 5. Annex A presents the full conceptual model.

> **注 1**：第 5 章其余部分的各图和正文构成一组架构描述的概念模型。图 1 至图 6 采用非正式的实体—关系图记法，以便利本文件使用者的理解。在各图中，圆角矩形表示信息对象，箭头表示对象之间的关系，其标注按箭头方向读取。各图举例说明贯穿第 5 章所述的诸关键概念。附录 A 给出完整的概念模型。

> **NOTE 2** Identification of the EoI can emerge from the analysis of the concerns of the stakeholders or can preexist before identification of some stakeholders and their concerns.

> **注 2**：EoI 的标识能产生于对利益相关方诸关注点的分析，也能先于某些利益相关方及其关注点的标识而预先存在。

> **EXAMPLE** The identification of an EoI generally results from the definition of the problem space. The problem description can be expressed with an architecture definition of a set of operational capabilities (often called “capability architecture”). At this capability definition stage, identified stakeholders are potentially concerned by the future EoI.

> **示例**：EoI 的标识一般源出于问题空间的定义。问题描述可用一组运行能力（常称为“能力架构”）的架构定义来表达。在此能力定义阶段，已标识的利益相关方潜在地关注未来的 EoI。

##### 5.2.2 Architectures and architecture descriptions 架构与架构描述

The architecture of an entity of interest comprises the fundamental concepts or properties of that entity considered in its environment. The architecture of an entity of interest can pertain to any or all of the entity’s:

所关注实体的架构包括该实体在其环境中加以考虑的诸基本概念或属性。所关注实体的架构能涉及其下列各项中的任一者或全部：

- constituent elements;

- 构成元素；

- interactions or interrelationships among its elements;

- 其各元素之间的交互或相互关系；

- interactions or interrelationships with its environment, including with other entities in that

- 与其环境的交互或相互关系，包括与该环境中其他

environment;

实体的交互或相互关系；

- behaviour and structure;

- 行为和结构；

- principles governing its design, use, operation and evolution.

- 管控其设计、使用、运行和演进的原则。

An AD is an expression of an architecture. ADs are work products resulting from architecting efforts. As a work product, an AD is devised for the specific purpose for which the architecting effort is undertaken, which is distinct from the purpose of the entity of interest. An AD comprises AD elements (see 5.2.10).

AD 是架构的一种表达。AD 是架构工作所产生的工作产品。作为工作产品，AD 是为开展该架构工作所针对的特定目的而设计的，该目的区别于所关注实体的目的。AD 包括诸 AD 元素（见 5.2.10）。

The architecture of an entity of interest can be understood through one or more distinct ADs, each created for a purpose relative to the architecture and stakeholder needs. Different ADs can, for example, be based on different stakeholders (see 5.2.3), stakeholder perspectives (see 5.2.4), time periods (sometimes termed epochs), or specific contexts or usage within the environment.

所关注实体的架构能通过一个或多个互不相同的 AD 来理解，每个 AD 都是为相对于该架构和利益相关方需要的一个目的而创建的。例如，不同的 AD 能基于不同的利益相关方（见 5.2.3）、利益相关方角度（见 5.2.4）、时间段（有时称为纪元），或该环境内的特定语境或用法。

> **NOTE** ISO/IEC/IEEE 42020 specifies a set of processes for architecting which can be employed in support of creating one or more ADs.

> **注**：ISO/IEC/IEEE 42020 规定了一组可用于支持创建一个或多个 AD 的架构工作过程。

##### 5.2.3 Stakeholders and concerns 利益相关方与关注点

Stakeholders are parties with direct or indirect interests in an entity. Among the stakeholders are those parties that have influence or control over and those who are impacted by an entity. A stakeholder’s interests are typically expressed as concerns about an entity of interest or the architecture of which they are aware. Concerns are often the result of the stakeholder's perspective gained from domain knowledge, experience, training, responsibility and authority.

利益相关方是对某一实体有直接或间接利益的诸当事方。利益相关方之中，既有对该实体具有影响力或控制力的当事方，也有受该实体影响的当事方。利益相关方的利益通常表达为对其所知晓的所关注实体或架构的关注点。关注点往往是利益相关方从领域知识、经验、培训、职责和权限中获得的角度的结果。

Concerns are matters of interest or importance to one or more stakeholders. A concern can be shared by one or more stakeholders and a stakeholder can hold more than one concern. The legitimacy and importance of a concern held by a stakeholder can be a consequence of the role of the stakeholder (e.g. owner, end user or participant, developer, architect, maintainer, disposer) or financial or social rights, shares, impact or claims (e.g. funding organization, governmental body, party receiving environmental impact from entity, stakeholder of an entity impacted by the entity of interest).

关注点是对一个或多个利益相关方具有利益或重要性的诸事项。一个关注点能由一个或多个利益相关方共享，一个利益相关方也能持有不止一个关注点。利益相关方所持关注点的正当性和重要性，能是下列情形的结果：该利益相关方的角色（例如所有者、最终用户或参与者、开发者、架构师、维护者、处置者），或财务或社会权利、份额、影响或主张（例如出资组织、政府机构、承受该实体环境影响的当事方、受该所关注实体影响的某一实体的利益相关方）。

Some stakeholders’ concerns are contrary to the success of the entity of interest. These stakeholders can have disagreements on the grounds of political or environmental considerations, can seek active disruption of the entity’s operations, or even outright destruction of the entity. Adversarial concerns can be taken into account when developing the architecture of the entity. For example, political objections can be resolved by incorporating a negotiated solution in the architecture of the entity, or threats can be mitigated by taking preventative measures.

某些利益相关方的关注点与该所关注实体的成功相悖。这些利益相关方能基于政治或环境方面的考虑而有异议，能谋求主动扰乱该实体的运行，甚至彻底摧毁该实体。在开展该实体的架构工作时，能把对抗性关注点纳入考虑。例如，政治上的反对能通过在实体的架构中纳入经协商的解决方案来化解，威胁也能通过采取预防措施来缓解。

During the entity of interest’s life cycle, concerns can arise at any time including (but not limited to) during conceptualization, when design choices are made, from construction or implementation, through deployment, operation, transfer of ownership, retirement and disposal.

在所关注实体的生存周期内，关注点能在任何时候产生，包括（但不限于）概念化期间、做出设计选择之时、源于建造或实施，直至部署、运行、所有权转移、退役和处置。

Concerns can manifest in various ways in relation to stakeholder's needs, architecture goals, expectations, responsibilities, requirements, design constraints and assumptions. Concerns can also manifest in recognition of dependencies, quality attributes, architecture decisions, risks or other issues.

关注点能就利益相关方的需要、架构目标、期望、职责、要求、设计约束和假设以各种方式显现。关注点也能在对依赖关系、质量属性、架构决策、风险或其他问题的识别中显现。

Concerns can pertain to influences exerted upon or by an entity of interest, including developmental, technological, business, operational, organizational, political, economic, legal, regulatory, ecological, social and physical influences. Concerns can also pertain to design influences such as internal structural features and component interoperability, particularly when architecting a system of systems or an enterprise.

关注点能涉及施加于所关注实体或由其所施加的影响，包括开发、技术、业务、运行、组织、政治、经济、法律、法规、生态、社会和物理影响。关注点也能涉及设计影响，如内部结构特征和组件互操作性，在开展系统的系统或企业的架构工作时尤为如此。

> **EXAMPLES**

- How is the system maintained?

- 系统如何维护？

- What system behaviours are safety-critical?

- 哪些系统行为属于安全关键？

- Can the entity of interest attain compliance with national regulations?

- 所关注实体能达到对国家法规的符合性吗？

- What is the cost to operate?

- 运行成本是多少？

- What are the risks, opportunities, satisfaction, resilience, coherence, affordability, complexity and trust

- 风险、机会、满意度、韧性、一致性、可负担性、复杂性和信任是什么，

offered by this architecture?

由本架构所提供的？

- In case of a flight navigation system of a commercial aircraft, what is GPS signal availability, tracking, degree

- 对于商用飞机的飞行导航系统，GPS 信号的可用性、跟踪、精度，

of accuracy, line of sight reception, altitude or elevations?

视线接收、高度或仰角如何？

- What are the data qualities (i.e. data qualities as described in ISO/IEC 25012:2008, Clause 4 or traditional

- 数据质量有哪些（即 ISO/IEC 25012:2008 第 4 章所述的数据质量，或传统的

system quality attributes as described in ISO/IEC 25010.)?

ISO/IEC 25010 所述的系统质量属性）？

- What is the system’s ability to maintain confidentiality, integrity, and availability for protecting operations?

- 系统为保护运行而维持保密性、完整性和可用性的能力如何？

- What is the ability to support a seamless transition from a legacy capability to a modernized operational

- 支持从遗留能力向现代化运行

capability?

能力无缝过渡的能力如何？

##### 5.2.4 Stakeholder perspectives 利益相关方角度

Stakeholders often form distinct groupings, or stakeholder perspectives, based on their common roles, experiences, beliefs or other characteristics. A perspective can reflect domain knowledge, professional experience, training or proximity to the entity of interest in its lifecycle (e.g. design, development, manufacturing, supply, operation and use). Importantly, a stakeholder perspective can also be influenced by personality, character traits, culture, peer pressure, constituency, etc.

利益相关方常常基于其共同的角色、经验、信念或其他特征，形成不同的分组，即利益相关方角度。一个角度能反映领域知识、专业经验、培训情况，或其在生存周期中（如设计、开发、制造、供应、运行和使用）与所关注实体的接近程度。重要的是，利益相关方角度还能受个性、性格特质、文化、同伴压力、所代表的群体等的影响。

Stakeholder perspectives are ways of thinking about the entity of interest in a context, especially as they relate to concerns. Typically, there are several ways of thinking about the architecture of the entity of interest.

利益相关方角度是在某一语境中思考所关注实体的方式，尤其就其与关注点的关系而言。通常，存在若干种思考所关注实体架构的方式。

The purpose of an AD (see 6.2) guides the identification of concerns that can reflect the perspectives of some stakeholders. There are often multiple stakeholder perspectives on any entity of interest.

架构描述的目的（见 6.2）指导对关注点的识别，这些关注点能反映部分利益相关方的角度。对任何所关注实体，往往存在多种利益相关方角度。

> **EXAMPLE 1** Operational and financial perspectives about an industrial production system.

> **示例 1**：关于工业生产系统的运行角度和财务角度。

> **EXAMPLE 2** Business, management, acquisition and supply perspectives about a banking system.

> **示例 2**：关于银行系统的业务、管理、采办和供应角度。

> **EXAMPLE 3** Development, deployment and customization perspectives about a mobile app.

> **示例 3**：关于移动应用的开发、部署和定制角度。

> **EXAMPLE 4** Provider and consumer perspectives about a hospitality service.

> **示例 4**：关于接待服务的提供方和消费方角度。

> **EXAMPLE 5** Data user and data provider perspectives about a content provider entity.

> **示例 5**：关于内容提供方实体的数据使用方和数据提供方角度。

Each perspective results in one or more concerns. Because concerns arise from stakeholder perspectives, architecture viewpoints framing those concerns are often grouped by stakeholder perspectives. Concerns are based on current interests and influences of the stakeholders and are often subjective in nature.

每个角度产生一个或多个关注点。由于关注点源自利益相关方角度，框定这些关注点的架构视角往往按利益相关方角度分组。关注点基于利益相关方当前的利益与影响，且往往本质上是主观的。

##### 5.2.5 Aspects 方面体

Aspects capture a set of characteristics or features of the entity of interest in its environment to address concerns within an AD.

方面体捕捉所关注实体在其环境中的一组特征或特性，以在架构描述内处理关注点。

An aspect can relate to one or more concerns of stakeholders. Usage of known aspects based upon prior experience within a field of application enables systematic coverage of the range of established concerns and also the identification of new concerns.

一个方面体能涉及利益相关方的一个或多个关注点。基于应用领域内的既有经验使用已知的方面体，能系统地覆盖已确立关注点的范围，并能识别新的关注点。

Aspects are based on experience in characterization of architectures and are more objective in nature as they arise from agreements among experts about practice in a domain and therefore are presumed to be best practice.

方面体基于对架构进行刻画的实践经验，且本质上较为客观，因为它们源自专家之间关于某领域实践的共识，因而被推定为最佳实践。

By examining aspects, relevant features or properties of the entity of interest can be discerned or predicted. Analysis of aspects can uncover one or more concerns.

通过考察方面体，能辨别或预测所关注实体的相关特征或性质。对方面体的分析能发现一个或多个关注点。

The definition of the relationships between aspects and concerns are based on the experience of the architects and are assessed by the stakeholders with their understanding and knowledge.

方面体与关注点之间关系的定义基于架构师的经验，并由利益相关方结合其理解与知识加以评判。

> **NOTE** A.4.2 contains more information about the utility of aspects.

> **注**：A.4.2 包含关于方面体效用的更多信息。

> **EXAMPLE 2** Behavioural, informational and structural aspects in a computer AD.

> **示例 2**：计算机架构描述中的行为方面体、信息方面体和结构方面体。

> **EXAMPLE 3** Connectivity aspects in a communications network AD (commonly shown as separate logical network and physical network depictions of a configuration of links and nodes in the network).

> **示例 3**：通信网络架构描述中的连接性方面体（通常表现为网络中链路与节点配置的独立逻辑网络描述和物理网络描述）。

Figure 1 depicts relationships between concerns, aspects, and stakeholder perspectives as utilized in an AD.

图 1 描绘了架构描述中所使用的关注点、方面体与利益相关方角度之间的关系。

![Figure 1 — Concerns, aspects, and stakeholder perspectives](ISO_IEC_IEEE 42010 2023.assets/fig-01.png)

**Figure 1 — Concerns, aspects, and stakeholder perspectives**

**图 1 — 关注点、方面体与利益相关方角度**

##### 5.2.6 Architecture considerations 架构考量因素

Architecture considerations are factors taken into account when architecting. Concerns (see 5.2.3), stakeholder perspectives (see 5.2.4) and aspects (see 5.2.5) are different considerations to consider while architecting. There are other considerations that can arise due to the architecture practices in use.

架构考量因素是开展架构工作时纳入考虑的因素。关注点（见 5.2.3）、利益相关方角度（见 5.2.4）和方面体（见 5.2.5）是架构工作期间需要考虑的不同考虑事项。由于所采用的架构实践，还会产生其他考虑事项。

Architecture considerations are useful when specifying architecture viewpoints and when constructing, interpreting, organizing or using architecture views (see 5.2.7). Architecture considerations can group specifications of architecture viewpoints, e.g. with respect to stakeholder perspectives.

在编制架构视角规格时，以及在构造、解释、组织或使用架构视图（见 5.2.7）时，架构考量因素很有用。架构考量因素能对架构视角规格进行分组，例如就利益相关方角度而言。

> **EXAMPLES** Considerations include: the ability of stakeholders to interpret the architecture description languages chosen to express stakeholder views, the degree of formality required for viewpoints and model kinds, the availability of supporting tools, standard practices used in the given industry domain, the availability of time and resources, the criticality of the depth of understanding that stakeholders need to achieve.

> **示例**：考虑事项包括：利益相关方解读为表达利益相关方视图而选用的架构描述语言的能力，架构视角和模型种类所要求的形式化程度，支撑工具的可用性，给定行业领域中使用的标准实践，时间和资源的可用性，利益相关方所需达到的理解深度的关键程度。

> **NOTE** Other considerations can relate to contexts, criteria, building blocks and domain vocabulary.

> **注**：其他考虑事项能涉及语境、准则、构建块和领域词汇。

##### 5.2.7 Architecture views and architecture viewpoints 架构视图与架构视角

An AD contains one or more architecture views. An architecture viewpoint governs one or more of these architecture views. A specification of an architecture viewpoint establishes the conventions for creating, interpreting, presenting and analysing a view to address the concerns framed by that viewpoint. Viewpoint specifications typically reflect the information elements required to facilitate the application of knowledge (including possibly informal or tacit experiential knowledge) to ascertain whether the architecture addresses the concerns satisfactorily.

一个架构描述包含一个或多个架构视图。一个架构视角管控这些架构视图中的一个或多个。架构视角规格确立创建、解释、呈现和分析视图的约定，以处理由该视角所框定的关注点。视角规格通常反映为便于应用知识（可包括非形式化的或隐性的经验知识）以确定架构是否令人满意地处理了关注点所需的信息元素。

> **NOTE 1** Architecture concerns, stakeholder perspectives and aspects can serve as an organizing basis for the viewpoints of an AD. Aspects are refinements of concerns and these aspects can be used to establish the viewpoint conventions. These aspects are evidenced in the resulting architecture view(s).

> **注 1**：架构关注点、利益相关方角度和方面体能作为架构描述各视角的组织基础。方面体是关注点的细化，这些方面体能用于确立视角约定。这些方面体在所得的架构视图中得到体现。

> **EXAMPLE 1** A telecommunications network (entity) is represented by a network connectivity deployment diagram that can be used to express the network model (as an architecture view) contained in a telecommunications architecture description. That view addresses communications parameters such as throughput and uptime (concerns) of operators and users (stakeholders).

> **示例 1**：电信网络（实体）由网络连通性部署图表示，该图能用于表达电信架构描述中所包含的网络模型（作为架构视图）。该视图处理运营商和用户（利益相关方）的吞吐量和正常运行时间等通信参数（关注点）。

> **EXAMPLE 2** A Parts and Variations View describing the content of a product line (entity) including common parts and individual products with their variants and options.

> **示例 2**：零部件与变型视图，描述产品线（实体）的内容，包括通用零部件以及带有其变型和选项的单个产品。

Figure 2 depicts the relationship between architecture views and architecture viewpoints in an AD.

图 2 描绘了 AD 中架构视图与架构视角之间的关系。

![Figure 2 — Architecture views and architecture viewpoints](ISO_IEC_IEEE 42010 2023.assets/fig-02.png)

**Figure 2 — Architecture views and architecture viewpoints**

**图 2 — 架构视图与架构视角**

An architecture viewpoint frames one or more concerns (see 5.2.3). A concern can be framed by more than one viewpoint. The architecture viewpoint identifies the specific aspects to be reflected in and concerns to be addressed by one or more architecture views. The specification of an architecture viewpoint provides conventions, e.g. AD elements, syntax and semantics, usage guidance and direction, to those who are creating, interpreting or using the architecture views.

架构视角框定一个或多个关注点（见 5.2.3）。一个关注点能由不止一个视角框定。架构视角标识一个或多个架构视图所要反映的特定方面体以及所要处理的关注点。架构视角的规格提供约定，例如 AD 元素、语法与语义、使用指南与方向，供创建、解释或使用架构视图的人员使用。

> **NOTE 2** Distinct from requirements for product acceptance, architecture views for the entity of interest that addresses concerns and reflects aspects can result in modified requirements.

> **注 2**：有别于产品验收要求，针对所关注实体、处理关注点并反映方面体的架构视图能导致要求被修改。

Using a metamodel or other conventions, the viewpoint specification establishes the manner in which AD elements (e.g. entities, relationships, attributes and constraints) are used, and possibly transformed by the viewpoint, when creating a view (see 5.2.9).

视角规格使用元模型或其他约定，确立在创建视图时 AD 元素（例如实体、关系、属性和约束）被使用以及可能被视角变换的方式（见 5.2.9）。

Architecture viewpoints are important analytical resources for development of architecture views because viewpoints reflect the architecting purpose, typical stakeholders and their perspectives, identified concerns, defined aspects of the entity of interest, and particular AD elements.

架构视角是开发架构视图的重要分析资源，因为视角反映了架构工作目的、典型利益相关方及其角度、已识别的关注点、所关注实体的已定义方面体以及特定的 AD 元素。

> **NOTE 3** Clause 8 specifies requirements on specification of architecture viewpoints. Annex B provides guidance on preparing architecture viewpoints.

> **注 3**：第 8 章规定关于架构视角规格的要求。附录 B 提供编制架构视角的指导。

##### 5.2.8 Model kinds, legends and architecture view components 模型种类、图例与架构视图组件

An architecture view is composed of one or more architecture view components. A view component that can be based on a model or not. Each view component is governed by a model kind or legend identified by its architecture viewpoint. A model kind determines the conventions for model-based view components. A legend documents the conventions for view components. These conventions include the intended uses, the terminology, the notations and their syntax and semantics and symbology of its governed models. A model kind or legend can be used by more than one viewpoint in an AD. Within an AD, an architecture view component can be part of more than one architecture view to enable sharing information when its content and presentation is relevant to more than one view.

架构视图由一个或多个架构视图组件构成。视图组件能基于模型，也能不基于模型。每个视图组件受其架构视角所标识的模型种类或图例管控。模型种类确定基于模型的视图组件的约定。图例记载视图组件的约定。这些约定包括预期用途、术语、记法及其所管控模型的语法、语义和符号体系。模型种类或图例能由 AD 中的不止一个视角使用。在一个 AD 内，当其内容和呈现与不止一个架构视图相关时，一个架构视图组件能作为不止一个架构视图的一部分，以实现信息共享。

> **EXAMPLE 1** Model kinds include use cases, activity models [such as structured analysis and design technique (SADT[53]) and ICAM1) Definition Language (IDEF0[60])], threat models, component models and connectivity models.

> **示例 1**：模型种类包括用例、活动模型[如结构化分析与设计技术（SADT[53]）和 ICAM1) 定义语言（IDEF0[60]）]、威胁模型、组件模型和连通性模型。

> **EXAMPLE 2** A data flow diagram can be a view component of a functional view. A separate control flow diagram can be a second view component in the same functional view. The functional view can also contain a narrative that explains how to interpret the flow diagrams in the view. The flow diagrams are model-based while the narrative is not. The data flow diagram can be part of an information security view.

> **示例 2**：数据流图能是功能视图的一个视图组件。单独的控制流图能是同一功能视图中的第二个视图组件。功能视图还能包含一段叙述，说明如何解释该视图中的流图。流图是基于模型的，而该叙述则不是。数据流图能是信息安全视图的一部分。

> **EXAMPLE 3** A symbology table can be a legend of an operational view.

> **示例 3**：符号体系表能是运行视图的图例。

Figure 3 depicts the composition of views from view components and the kinds of view components.

图 3 描绘了视图由视图组件构成的方式以及视图组件的种类。

![Figure 3 — Conceptual model for views and view components](ISO_IEC_IEEE 42010 2023.assets/fig-03.png)

**Figure 3 — Conceptual model for views and view components**

**图 3 — 视图与视图组件的概念模型**

##### 5.2.9 Architecture description (AD) elements 架构描述（AD）元素

An AD element is an occurrence of one or more architectural concepts in an AD. The AD elements include occurrences of the following architectural concepts: stakeholder, concern, aspect, stakeholder perspective, architecture viewpoint, architecture view, model kind, legend, architecture view component, architecture decision, architecture rationale and any correspondence and correspondence method specified on those constructs.

AD 元素是一个或多个架构概念在一个 AD 中的出现。AD 元素包括下列架构概念的出现：利益相关方、关注点、方面体、利益相关方角度、架构视角、架构视图、模型种类、图例、架构视图组件、架构决策、架构理由，以及在这些构造上规定的任何对应关系和对应方法。

Any one of these concepts can have multiple occurrences in one or more AD. An AD element occurrence specifies one or more architectural concepts.

这些概念中的任何一个能在一个或多个 AD 中有多次出现。一个 AD 元素出现规定一个或多个架构概念。

An AD element in an AD can be refined or elaborated by reference to another AD. An AD can utilize protocols introduced as AD elements of distinct ADs.

一个 AD 中的 AD 元素能通过引用另一个 AD 来细化或详细阐述。一个 AD 能利用作为不同 AD 的 AD 元素而引入的协议。

As viewpoints (see 5.2.7), model kinds (see 5.2.8) and legends (see 5.2.8) are specified and applied, additional AD elements are introduced. The governing viewpoint or model kind or legend determines the syntax and semantic conventions for these introduced AD elements.

随着视角（见 5.2.7）、模型种类（见 5.2.8）和图例（见 5.2.8）被规定和应用，附加的 AD 元素被引入。起管控作用的视角、模型种类或图例确定这些被引入的 AD 元素的语法与语义约定。

> **EXAMPLE** AD elements introduced by viewpoints or model kinds include use case constructs such as preconditions, actors, boundaries, systems; activity model constructs such as activities, inputs, outputs, controls, and mechanisms; architecture or design patterns to be employed.

> **示例**：由视角或模型种类引入的 AD 元素包括用例构造，如前置条件、参与者、边界、系统；活动模型构造，如活动、输入、输出、控制和机制；以及拟采用的架构或设计模式。

##### 5.2.10 View methods 视图方法

A specification of an architecture viewpoint includes one or more view methods. View methods provide guidance, heuristics, metrics, patterns, design rules or guidelines, best practices and examples to aid in view construction and use of associated views. View methods specify expression rules, modelling methods, analysis techniques and other operations on views. These methods specify the AD elements used when creating the view and methods to analyse, interrogate or query views to assess properties of interest. Requirements on view methods are specified in 8.3.

架构视角的规格包括一个或多个视图方法。视图方法提供指导、启发式方法、度量、模式、设计规则或指南、最佳实践和示例，以辅助视图构建以及关联架构视图的使用。视图方法规定表达规则、建模方法、分析技术以及对视图的其他操作。这些方法规定创建视图时使用的 AD 元素，以及为评定所关注的特性而对视图进行分析、询问或查询的方法。对视图方法的要求在 8.3 中规定。

View methods are divided into categories, including:

视图方法分为若干类别，包括：

- Construction methods are the means by which views are prepared using a viewpoint. These can be

- 构建方法是借助视角来制备视图的手段。这些方法能

in the form of process guidance (how to start, what to do next); or description guidance (templates for views of this type); or heuristics, styles, patterns, or other idioms to employ.

采取过程指导的形式（如何开始、下一步做什么）；或描述指导的形式（此类视图的模板）；或所采用的启发式方法、风格、模式或其他惯用法。

- Interpretive methods are the means by which views are to be understood by stakeholders and other

- 解释方法是利益相关方及其他

users.

使用者借以理解视图的手段。

- Analysis methods are used to check, reason about, transform, predict, apply and evaluate results

- 分析方法用于检查、推理、变换、预测、应用和评估

from this view.

来自此视图的结果。

> **NOTE** View methods are usually defined in a viewpoint and are referenced by or used by model kinds, architecture description frameworks, and architecture description languages.

> **注**：视图方法通常在视角中定义，并由模型种类、架构描述框架和架构描述语言引用或使用。

> **EXAMPLE** View methods pertaining to: chaining dependencies to assess the impact of a change; workshops to trade-off qualities or other concerns; boundary analyses to determine whether context and entity of interest are well defined; guidance on partitioning; analysis of architectural complexity; creation and enforcement of architecture styles (such as layered, aspect-oriented); pattern families to promote intended properties of the entity of interest; analyses against requirements for completeness and coverage; interpretation and integration of external models as information sources.

> **示例**：视图方法涉及：链接依赖关系以评估变更的影响；通过研讨会来权衡质量或其他关注点；边界分析以确定上下文和所关注实体是否定义良好；关于划分的指导；架构复杂性分析；架构风格（如分层、面向方面）的创建与强制执行；模式族以促进所关注实体的预期特性；针对完整性和覆盖性要求的分析；将外部模型作为信息源的解释与集成。

##### 5.2.11 AD element correspondence AD 元素对应关系

An AD element correspondence identifies an identified or named relation between two or more AD elements.

AD 元素对应关系标识两个或多个 AD 元素之间已识别或已命名的关系。

An AD element correspondence can relate:

架构描述元素对应关系能关联：

- one or more AD elements with one or more AD elements within an AD;

- 一个或多个架构描述元素与一个架构描述内的一个或多个架构描述元素；

- one or more AD elements with one or more AD elements occurring in multiple ADs;

- 一个或多个架构描述元素与出现在多个架构描述中的一个或多个架构描述元素；

- one or more AD elements with one or more AD elements within an ADF or across several ADFs;

- 一个或多个架构描述元素与一个架构描述框架内或跨若干架构描述框架的一个或多个架构描述元素；

- one or more AD elements with one or more AD elements using one or more ADLs

- 使用一个或多个架构描述语言的一个或多个架构描述元素与一个或多个架构描述元素

For the purposes of correspondences, an AD itself may be considered an AD element of a different AD.

为对应关系之目的，一个架构描述本身可视为另一个架构描述的一个架构描述元素。

AD element correspondences may be used to indicate consistency relationships within and among ADs; to facilitate correlations among ADs of related systems; or to enable coordinated interpretation and analysis of related descriptions.

架构描述元素对应关系可用于指示架构描述内及架构描述之间的一致性关系；便于相关系统的架构描述之间的相互关联；或使相关描述的协同解释与分析成为可能。

An AD element correspondence may be governed by a correspondence method which expresses rules, practices or models to specify the particular relation between the AD elements.

架构描述元素对应关系可由一种对应方法管控，该对应方法表达用于规定架构描述元素之间特定关系的规则、实践或模型。

AD element correspondences and correspondence methods can be used to express and enforce architecture relations such as composition, refinement, consistency, traceability, dependency, constraint, satisfaction and obligation [26] of AD elements.

架构描述元素对应关系与对应方法可用于表达并强制执行架构关系，如架构描述元素的组合、细化、一致性、可追溯性、依赖、约束、满足与义务 [26]。

> **EXAMPLE 1** A correspondence between an AD element within a view and the concern that it addresses; between an architecture view and the aspect that it implements; between an AD element and the function that it implements; between an interface on a component and the stack of standards to which the interface conforms; between a data object on a functional flow and the full data structure definition; between a system and the organizational structure that implements it.

> **示例 1**：一个架构视图内的架构描述元素与其所应对的关注点之间的对应关系；一个架构视图与其所实现的方面体之间的对应关系；一个架构描述元素与其所实现的功能之间的对应关系；一个组件上的接口与该接口所符合的标准栈之间的对应关系；功能流上的一个数据对象与完整数据结构定义之间的对应关系；一个系统与实现该系统的组织结构之间的对应关系。

> **EXAMPLE 2** “Self-referential” correspondences are an activity that is refined into two or more activities of the same kind, or an activity that can recursively invoke itself.

> **示例 2**：「自指」对应关系指一个活动被细化为同类的两个或更多活动，或一个活动能递归调用其自身。

Figure 4 depicts the nature of AD element correspondences.

图 4 描绘了架构描述元素对应关系的性质。

![Figure 4 — Conceptual model of AD element correspondences](ISO_IEC_IEEE 42010 2023.assets/fig-04.png)

**Figure 4 — Conceptual model of AD element correspondences**

**图 4 — 架构描述元素对应关系的概念模型**

> **EXAMPLE 3** A correspondence method can specify that all AD elements trace to a concern or requirement. Compliance to that method can be recorded in the form of a traceability matrix, with a rationale provided for each AD element that does not trace to a concern or requirement. The AD elements in a correspondence do not need to be distinct. A correspondence can be defined between an AD element and itself.

> **示例 3**：对应方法可规定所有架构描述元素都追溯到某个关注点或要求。对该方法的符合性可以追溯矩阵的形式记录，并为每个未追溯到关注点或要求的架构描述元素提供理由。一条对应关系中的架构描述元素不必互不相同。一条对应关系可定义在一个架构描述元素与其自身之间。

> **NOTE 1** Requirements for using correspondences and correspondence methods are specified in 6.9. Additional examples of their use are given in A.7.

> **注 1**：使用对应关系与对应关系的要求在 6.9 中规定。其使用的更多示例在 A.7 中给出。

> **NOTE 2** Correspondences in this document are similar to view correspondences in ISO/IEC 10746-2 (RM- ODP) and ISO/IEC 19793.

> **注 2**：本文档中的对应关系类似于 ISO/IEC 10746-2（RM-ODP）和 ISO/IEC 19793 中的视图对应关系。

> **NOTE 3** Usually correspondence methods are “cross model” or “cross view” or “cross AD” since correspondences within a view component are part of the conventions of the specification of the model kind.

> **注 3**：通常对应方法是「跨模型」或「跨视图」或「跨架构描述」的，因为视图组件内的对应关系是模型种类规格之约定的组成部分。

> **NOTE 4** Correspondences and correspondence methods can be applied to multiple AD elements to express architecture relations pertaining to multiple AD elements.

> **注 4**：对应关系与对应方法可应用于多个架构描述元素，以表达涉及多个架构描述元素的架构关系。

##### 5.2.12 Architecture decisions and rationale 架构决策与理由

An architecture decision is a collection of choices made in the overall context of an architecture. These choices usually pertain to various AD elements, entity requirements, or environmental influences on the architecture.

架构决策是在架构总体语境中所做选择的一个集合。这些选择通常涉及各类架构描述元素、实体要求或对架构的环境影响。

> **EXAMPLE 1** Selection of architecture concepts, choice of AD elements, selection of ADFs, choice of architecture layering scheme, choice of underlying technology, choice of business components, choice of tactics to use for achieving system qualities, choice of business processes, choice of applicable patterns, choice of style(s) to be applied, choice of range of implementation technologies or other realizations to be considered, and choice of option sets to be considered.

> **示例 1**：架构概念的选择、架构描述元素的选择、架构描述框架的选择、架构分层方案的选择、底层技术的选择、业务组件的选择、用于达成系统质量的策略的选择、业务流程的选择、适用模式的选择、拟应用风格的选择、拟考虑的实现技术或其他实现方式范围的选择，以及拟考虑选项集的选择。

Architecture rationale records explanation, justification or reasoning about architecture decisions. The rationale for a decision can include the following items: the basis for making a decision, impact on quality attributes, alternatives and trade-offs considered, potential consequences of the decision, architectural principles, and citations to sources of additional information.

架构理由记录关于架构决策的解释、论证或推理。一项决策的理由可包括以下内容：做出决策的依据、对质量属性的影响、所考虑的备选方案与权衡、决策的潜在后果、架构原则，以及附加信息来源的引用。

> **EXAMPLE 2** Meeting cost commitments, meeting time commitments, using proven technologies, minimizing rework, reducing capital investments, achieving interface compatibility, satisfying constraints imposed by the operational context.

> **示例 2**：满足成本承诺、满足时间承诺、使用成熟技术、尽量减少返工、减少资本投入、达成接口兼容性、满足运行语境施加的约束。

> **EXAMPLE 3** Modelling tool selections to align with related architectures (e.g. customer’s enterprise architecture) to ensure interoperability and traceability.

> **示例 3**：选择建模工具以与相关架构（例如客户的企业架构）保持一致，从而确保互操作性与可追溯性。

> **NOTE** Requirements for capturing decisions and rationale within an AD are specified in 6.10.

> **注**：在架构描述内捕获决策与理由的要求在 6.10 中规定。

#### 5.3 Architecture description in the life cycle **5.3 生存周期中的架构描述**

Architecting activities occur and ADs are produced for various reasons throughout the life of the entity of interest, from initial concept through the operation, refurbishment or final retirement from use, and eventual disposal of this entity.

在整个所关注实体生存期间，从初始概念到该实体的运行、翻修或最终停止使用，及其最终处置，架构工作活动出于各种原因而发生，架构描述也因各种原因而产生。

> **NOTE 1** Since an AD describes the concept of the entity of interest, in some cases, ADs continue to be produced even after retirement as long as there is interest in the concept, and can be parked or discarded as per the policies of the organization.

> **注 1**：由于架构描述描述的是所关注实体的概念，因此在某些情况下，只要对该概念仍有兴趣，即使实体退役后架构描述仍会继续产生，并可按组织的方针予以搁置或废弃。

ADs are the work products that result from architecting, which takes place within the context of a project and/or organization (company, network of companies, consortium and standardization body).

架构描述是架构工作所产生的工作产品，而架构工作发生在一个项目和／或组织（公司、公司网络、联合体和标准化机构）的语境中。

During the entity of interest life cycle, an AD can precede or follow architecture creation, updating or changing.

在所关注实体的生存周期内，架构描述可以先于或后于架构的建立、更新或变更。

> **NOTE 2** See Annex E for more details of the role of architecting in the life cycle.

> **注 2**：架构工作在生存周期中作用的更多细节见附录 E。

#### 5.4 Architecture description frameworks and languages **5.4 架构描述框架与语言**

##### 5.4.1 General 总则

ADFs and ADLs are now widely used in architecting to facilitate normalized expression of the architecture for those constructing and using ADs, and to ensure consistency of style and content coverage across ADs. ADFs and ADLs built on the concepts of architecture description presented in this document, can be utilized effectively for:

架构描述框架与架构描述语言如今在架构工作中被广泛使用，以便于为架构描述的构建者和使用者规范化地表达架构，并确保各架构描述在风格与内容覆盖上的一致性。基于本文档所提出的架构描述概念构建的架构描述框架与架构描述语言，可有效地用于：

a) generalized reference frameworks and languages intended to guide more specific ADFs;

a) 旨在指导更为具体的架构描述框架的通用参考框架与语言；

b) special purpose frameworks and languages intended to enable better analytical understanding and situational awareness;

b) 旨在促成更好的分析性理解与情境意识的专用框架与语言；

c) entity implementation frameworks and languages intended to facilitate entity engineering, operation and retirement.

c) 旨在促进实体的工程、运行与退役的实体实施框架与语言。

##### 5.4.2 Architecture description frameworks 架构描述框架

An ADF establishes a common practice for creating, interpreting, analysing and using ADs within a particular domain of interest, e.g. defense, aerospace and banking. An ADF can also guide or serve as a reference for one or more than one specialized ADF. For a generalized entity of interest within the context of a particular domain of practice, an ADF intended as a reference typically identifies architecture viewpoints for expected or known architecture considerations, often as stakeholder perspectives, concerns or aspects related to structure, function (both behaviour and fitness) and life cycle. For a reference use, the many different stakeholder perspectives can be generalized. Utilizing an architecture viewpoint, users of the reference have access to views appropriate for the generalized entity of interest that can satisfy the architecture considerations framed by that viewpoint.

架构描述框架为在某一特定关注领域（例如国防、航空航天和银行业）内创建、解释、分析和使用架构描述建立一种共同实践。架构描述框架还能指导一个或多个专门化架构描述框架，或作为其参考。对于某一特定实践领域语境中的泛化所关注实体，用作参考的架构描述框架通常为预期或已知的架构考量因素标识架构视角，这些考量因素往往表现为利益相关方角度、关注点或与结构、功能（行为与适合度二者）及生存周期有关的方面体。用于参考用途时，众多不同的利益相关方角度可予以泛化。借助一个架构视角，参考的使用者可获取适合该泛化所关注实体的架构视图，这些架构视图能满足由该视角所框定的架构考量因素。

An architecture viewpoint identified in an ADF, which intends to guide or serve as a reference for more specific ADF, identifies the typical concerns, aspects, model kinds and view methods, which constitute the conventions governing views associated with that viewpoint. Users of an ADF serving as a generalized reference can specialize the architecture considerations, the specifications of architecture viewpoints, and thus the resulting architecture views, as an ADF to use in implementing the architecture of a particular entity of interest.

在 ADF 中识别的架构视角，若意在指导更具体的 ADF 或充当其参考，则识别典型的关注点、方面体、模型种类和视图方法，它们构成管控与该视角相关联的架构视图的约定。将 ADF 用作通用参考的使用者，可以特化架构考量因素、架构视角规格，并因而特化所得的架构视图，以此作为用于实施某一特定所关注实体的架构的 ADF。

The architecture viewpoints identified in an ADF can result from experiences with architecture viewpoints specified or used by prior architecting efforts to determine satisfaction of concerns about an entity of interest to the extent of detail consistent with the purpose of the ADF.

ADF 中识别的架构视角，可以源自以往架构工作所规定或使用的架构视角的经验，用以在与 ADF 目的相一致的详细程度上判定对所关注实体的关注点的满意情况。

> **NOTE 1** Particular architecture decisions are made in ADFs: selection of stakeholders and related concerns, specific aspects and stakeholder perspectives. An ADF will structure ADs according to these decisions.

> **注 1**：特定的架构决策是在 ADF 中作出的：利益相关方及相关关注点的选择、特定方面体和利益相关方角度。ADF 将按照这些决策来构造架构描述。

An ADF provides a structuring formalism to organize AD elements that are usually associated with the architecture viewpoints used to generate associated views. The purpose of the structuring formalism is to provide ways of representing relationships among various elements of the architecture and enhancing opportunities for analysis of interactions among those elements.

ADF 提供一种结构化形式体系，用以组织通常与用于生成关联视图的架构视角相关联的架构描述元素。该结构化形式体系的目的在于：提供表示架构各元素之间关系的方式，并增加分析这些元素之间交互的机会。

> **NOTE 2** The most common structuring formalisms use architecture considerations, i.e. concerns, stakeholder perspectives and aspects, represented in a grid or matrix format.

> **注 2**：最常见的结构化形式体系使用架构考量因素，即关注点、利益相关方角度和方面体，以网格或矩阵形式表示。

> **EXAMPLE 1** Well known structuring formalisms include: GERAM cube in ISO 15704, Reference Architectural Model Industrie 4.0 (RAMI 4.0)[34], TOGAF phases (Business, Data, Application and Technology),[62] NAF grid,[44] UAF grid,[48] and Zachman Framework matrix[67].

> **示例 1**：众所周知的结构化形式体系包括：ISO 15704 中的 GERAM 立方体、工业 4.0 参考架构模型（RAMI 4.0）[34]、TOGAF 阶段（业务、数据、应用和技术）[62]、NAF 网格[44]、UAF 网格[48]以及 Zachman 框架矩阵[67]。

Figure 5 depicts the conceptual model of an ADF.

图 5 描绘了 ADF 的概念模型。

![Figure 5 — Conceptual model of an architecture description framework](ISO_IEC_IEEE 42010 2023.assets/fig-05.png)

**Figure 5 — Conceptual model of an architecture description framework**

**图 5 — 架构描述框架的概念模型**

An ADF defines structural categories used in the structuring formalism. These categories result from correspondence methods that group AD elements into meaningful configurations for presentation, analysis, and management of the AD for the entity of interest.

ADF 定义结构化形式体系中所用的结构类别。这些类别源自对应方法，后者将架构描述元素归组为有意义的配置，以便针对所关注实体对架构描述进行表示、分析和管理。

> **NOTE 3** Sometimes categories are represented by “dimensions” in a graphic portrayal, such as the rows and columns used in several frameworks. A structuring formalism in grid form usually has two framework dimensions but formalisms can have a single framework dimension, often segmented in a multi-layer hierarchy, or several framework dimensions where visual representation of framework dimensions above three is difficult.

> **注 3**：有时类别在图形描绘中由“维度”表示，例如若干框架中所用的行和列。网格形式的结构化形式体系通常有两个框架维度，但形式体系可以只有一个框架维度（常被分段为多层级的层次结构），也可以有多个框架维度（此时三个以上框架维度的可视化表示是困难的）。

> **EXAMPLE 2** A two-dimensional grid is used in the Zachman[67] and UAF[48] ADFs where stakeholder perspectives are depicted as rows and aspects of the generalized entity of interest are depicted as columns.

> **示例 2**：Zachman[67]和 UAF[48]的 ADF 使用二维网格，其中利益相关方角度被描绘为行，通用所关注实体的方面体被描绘为列。

> **NOTE 4** An ADF used as a reference can successfully rely on generalized architecture considerations and an agreed upon common vocabulary for the encompassed domain of interest. Specializations for implementation often necessitate careful customization to meet stakeholder expectations, particularly when adapting an ADF used as a reference for a particular purpose or for better comprehension by those stakeholders sponsoring the architecting effort. As a result of the introduction of specialized AD elements, a change in vocabulary and specifications of architecture viewpoints can be necessary.

> **注 4**：用作参考的 ADF 能够成功地依赖通用的架构考量因素以及就所涵盖的关注域达成共识的共用词汇。面向实施的特化往往需要经过仔细定制，以满足利益相关方的期望，尤其是在为使 ADF 适合某一特定目的、或为使发起架构工作的利益相关方更好地理解而将其用作参考时。由于引入了经特化的架构描述元素，可能有必要变更词汇以及架构视角规格。

Within an ADF, architecture viewpoints are important analytical resources for development of architecture views because viewpoints reflect the architecting purpose, typical stakeholders and their perspectives, identified concerns, defined aspects of the entity of interest, and particular AD elements.

在 ADF 内，架构视角是开发架构视图的重要分析资源，因为视角反映了架构工作目的、典型利益相关方及其角度、所识别的关注点、所关注实体的已定义方面体以及特定的架构描述元素。

Depending upon the intended application for a framework, the extent of detail resulting from a viewpoint can vary widely. A framework for reference can be expected to have more generalized stakeholder perspectives and architecture considerations, often partitioned into multiple functional clusters, e.g. product and life cycle.

取决于框架的预期应用，由某一视角所产生的详细程度可能差异很大。用作参考的框架可以预期具有更为通用的利益相关方角度和架构考量因素，且往往被划分为多个功能簇，例如产品和生存周期。

##### 5.4.3 ADF utilization ADF 的利用

When sharing typical AD elements in a common methodology, users can develop and maintain a less generalized domain specific ADF as a reference with architecture considerations and stakeholder viewpoints with appropriate model kinds and legends. Some ADFs used for references include explicit definitions of the AD elements associated with the model kinds and legends to use for each view of the entity of interest. Additional model kinds can address needed architecture considerations not covered by a particular framework.

在共同方法论中共享典型架构描述元素时，使用者能开发和维护通用性较低的领域特定 ADF，将其用作带有架构考量因素和利益相关方视角的参考，并配以适当的模型种类和图例。一些用作参考的 ADF 包含对与所关注实体的每个视图所要使用的模型种类和图例相关联的架构描述元素的明确定义。附加的模型种类能处理某一特定框架未涵盖的所需架构考量因素。

A specialized framework, or one intended for implementation rather than reference, uses more specific and possibly more detailed stakeholder concerns, specific aspects and often a narrow portion of, or no consideration of, the life cycle.

经特化的框架，或意在用于实施而非用作参考的框架，使用更具体且可能更详细的利益相关方关注点、特定方面体，并且往往只涉及生存周期的一小部分，或完全不考虑生存周期。

> **NOTE 1** Particular practice communities establish norms in areas where similar architecting is recurring: stakeholders with recurring concerns, conventions for addressing specific aspects, and architecting practices for establishing customary perspectives. An ADF will structure ADs according to these norms.

> **注 1**：特定的实践共同体在反复出现类似架构工作的领域确立规范：具有反复出现关注点的利益相关方、处理特定方面体的约定，以及建立惯用角度的架构工作实践。ADF 将按照这些规范构造架构描述。

Usage of ADFs in different situations is likely to identify new combinations of architecture considerations and useful viewpoints, model kinds, legends, views and correspondences. In different situations the following can occur:

在不同情形中使用 ADF，很可能识别出架构考量因素与有用视角、模型种类、图例、架构视图及对应关系的新组合。在不同情形中可能出现下列情况：

- omission of life cycle or part of life cycle;

- 省略生存周期或生存周期的一部分；

- inclusion of only some stakeholders or aspects;

- 仅包含部分利益相关方或方面体；

- inclusion of overlapping sets of aspects;

- 包含相互重叠的方面体集合；

- inclusion of only sub-domain or sub-groups of aspects;

- 仅包含方面体的子域或子组；

- inclusion of new or adapted viewpoints as new concerns emerge;

- 随着新关注点的出现而包含新的或经适配的视角；

- identification of previously unrealized correspondences.

- 识别出以前未认识到的对应关系。

Stakeholder concerns are often better understood when examined from different stakeholder perspectives across different aspects of the entity of interest, such as structure, behaviour and connectivity.

当从不同利益相关方角度、跨所关注实体的不同方面体（如结构、行为和连接性）加以考察时，利益相关方关注点往往能得到更好的理解。

Some stakeholders look at an architecture from a business perspective and can be interested in the functionality that is required or provided (what capability of the entity is being created or changed, or what new processes are necessary?) and some stakeholders look at an architecture from an economic perspective and can be interested in the financial consequences of the same functionality (what are the investment implications and what is the expected impact on the bottom line?).

一些利益相关方从业务角度审视架构，可能关注所需或所提供的功能（正在创建或变更该实体的什么能力，或者需要哪些新过程？）；另一些利益相关方从经济角度审视架构，可能关注同一功能的财务后果（有哪些投资影响，对最终收益的预期影响是什么？）。

> **NOTE 2** ADFs frequently encompass both provisions for AD and additional architecting practices.

> **注 2**：ADF 往往同时涵盖对架构描述的规定和附加的架构工作实践。

> **NOTE 3** Requirements for an ADF are specified in 7.1.

> **注 3**：对 ADF 的要求在 7.1 中规定。

> **NOTE 4** Annex F gives more information about ADFs and how they can be related to the concepts and requirements of the document.

> **注 4**：附录 F 给出关于 ADF 以及它们如何能与本文件的概念和要求相关联的更多信息。

> **NOTE 5** ADFs identify one or more AD elements which are instances of the architectural constructs: stakeholder, concern, stakeholder perspective, aspect, architecture viewpoint, model kind, legend, etc.

> **注 5**：ADF 识别一个或多个架构描述元素，这些元素是下列架构构造的实例：利益相关方、关注点、利益相关方角度、方面体、架构视角、模型种类、图例等。

One way to look at ADFs is to consider that an ADF is specifying the information model of an architecting effort (or project) that is tasked with the development of an architecture and its description. In other words, the ADF describes in an organized form the information elements that are to be produced.

看待 ADF 的一种方式是认为：ADF 规定的是受托开发某一架构及其描述的架构工作（或项目）的信息模型。换言之，ADF 以有组织的形式描述所要产生的信息元素。

If the ADF is expressed in a generic way, then it can only be used as a reference model (or partial model) of this information model, which then needs to be specialized by adding necessary detail for the purposes of the effort. Conversely, if the ADF is already specialized for the purposes of an application domain, then less tailoring is needed before utilization.

若 ADF 以通用方式表达，则它只能用作该信息模型的参考模型（或部分模型），之后还需针对本次工作的目的补充必要细节来加以特化。反之，若 ADF 已针对某个应用领域的目的作了特化，则在使用前所需的裁剪较少。

However, given the objective(s) of a particular architecting effort, domain specific ADFs can be further specialized. For example, some viewpoints, aspects, or perspectives may not be relevant from the point of view of these objective(s), or in turn there may exist concerns that are specific to the particular effort and shall therefore be addressed, which requires that additional viewpoints be specified and used.

然而，就某项架构工作的目标而言，领域特定的 ADF 还可以进一步特化。例如，某些视角、方面体或利益相关方角度从这些目标来看可能并不相关；反过来，也可能存在该项工作特有的关注点而应予以应对，这要求规定并使用额外的视角。

This continuum from generic to reference (or partial) and particular models is an application of the identical concepts expressed in ISO 15704 (for further details, see C.4).

从通用模型到参考（或部分）模型、再到特定模型的这一连续谱，是 ISO 15704 所述同一批概念的一种应用（更多细节见 C.4）。

##### 5.4.4 Architecture description languages 架构描述语言

An ADL is a specified syntax and semantics intended for use in describing the architecture of an entity of interest. An ADL is a language for stakeholders, including those involved in the architecting effort that allows the expression of architecture considerations by means of AD elements pertaining to the entity of interest, and the architecting context. An AD can use more than one ADL, even a different ADL for each viewpoint, or even distinct ADLs for each model kind specified by a single architecture viewpoint.

ADL 是为描述所关注实体的架构而规定的一套语法与语义。ADL 是面向利益相关方（包括参与架构工作的人员）的语言，它允许借助与所关注实体相关的 AD 元素以及架构工作语境来表达架构考量因素。一个 AD 可以使用多个 ADL，甚至每个视角各用一个不同的 ADL，或者对单个架构视角所规定的每种模型种类各用一个不同的 ADL。

> **EXAMPLE 1** UML profiles for architecture description are defined using stereotypes, tag definitions, and constraints applied to specific model elements (classes, attributes, operations, and activities) with a profile collection of such extensions collectively customized for a particular domain (e.g. aerospace, healthcare, financial) or platform (J2EE, .NET), and a modelling profile can define a particular model kind as part of its specification. Often general-purpose modelling languages, e.g. UML[49], SysML[47], OPM (ISO/PAS 19450), are embellished with profiles specifically intended for use in ADs.

> **示例 1**：UML 用于架构描述的概要（profile）是用构造型、标记定义以及施加于特定模型元素（类、属性、操作和活动）的约束来定义的，并配以一组此类扩展的概要集合，针对某个特定领域（如航空航天、医疗、金融）或平台（J2EE、.NET）统一定制；建模概要还可以在其规格中规定某种特定的模型种类。通用建模语言，如 UML[49]、SysML[47]、OPM（ISO/PAS 19450），常以专门用于 AD 的概要加以补充。

ADLs can be employed (or devised) to express specific architecture considerations which an architect needs to address.

可以采用（或设计）ADL 来表达架构师需要应对的特定架构考量因素。

> **NOTE 1** The use of more than one ADL in an AD requires great care to avoid confusion and misunderstanding.

> **注 1**：在一个 AD 中使用多个 ADL 时须格外谨慎，以免造成混淆与误解。

An ADL provides a way to create and understand the view components that compose into architecture views. Suitable ADL selection occurs by considering view methods that specify how information is selected, transformed and presented in an architecture view. View methods determine the information to capture when constructing ADs, to use for the analysis of captured descriptions, and the information needed for the description of architecture concepts and features.

ADL 提供了创建和理解组成架构视图的各视图组件的方式。恰当的 ADL 选择要通过考察视图方法来完成，视图方法规定信息在架构视图中如何选取、变换与呈现。视图方法决定了构造 AD 时需捕获哪些信息、分析所捕获的描述时使用哪些信息，以及描述架构概念与特征所需的信息。

ADLs can provide necessary rigor for the development of an AD. The semantics of an ADL can be specified in increasing extents of formality and expressive power by: a vocabulary or glossary using natural language, a taxonomy of terms and relationships, a meta-model expressing the uses of language constructs, and as an ontological theory using axioms in a formal logic or as an analytical theory using differential equations, tensor calculus, etc.

ADL 能为 AD 的开发提供必要的严谨性。ADL 的语义可按形式化程度与表达力的递增，依次用下列方式规定：以自然语言编写的词汇表或术语表；术语与关系的分类体系；表达语言构造物用法的元模型；以及用形式逻辑公理表述的本体论理论，或用微分方程、张量运算等表述的分析理论。

As transition occurs from a very generic reference ADF through a domain specific ADF and practice specific ADF to an implementation ADF, different ADLs are likely to be employed to meet more refined specifications of architecture viewpoints for architecture views.

在从非常通用的参考 ADF，经由领域特定 ADF 与实践特定 ADF，过渡到实现 ADF 的过程中，为满足对架构视图所用架构视角的更精细规格，很可能要采用不同的 ADL。

> **EXAMPLE 2** The transition from a generic Zachman Framework[67] to a UAF[48] involves a transition from general information and computing technology (ICT) ADL terminology to a precise terminology based on the UAF Domain Meta-Model.[48] This terminology can be implemented with the UAF Profile[48] using SysML[47] notation and semantics, which in turn is transitioned to implementation-specific ADL for a particular project modelling profile extension of UML[49].

> **示例 2**：从通用的 Zachman 框架[67] 过渡到 UAF[48]，涉及从一般的信息与计算技术（ICT）ADL 术语，过渡到基于 UAF 域元模型[48] 的精确术语。该术语可以用 UAF 概要[48] 配合 SysML[47] 的记法与语义来实现，进而再过渡为面向具体项目的、对 UML[49] 建模概要扩展的实现特定 ADL。

using correspondences (see 6.9.2) or a unified underlying ontology (see A.6 on projective and synthetic view creation approaches). The constructs of the actual ADLs used in practice are then subsets of this integrated ontology.

使用对应关系（见 6.9.2）或统一的基础本体论（见 A.6 关于投影式与合成式的架构视图创建途径）。于是，实践中使用的实际 ADL 的构造是这一集成本体论的子集。

> **EXAMPLE 3** AADL,[57] ArchiMate,[61] Systems Modelling Language (SysML),[47] ISO 19440, Business Process Model and Notation (BPMN),[46] Unified Modelling Language (UML),[49] Unified Architecture Framework (UAF) Profile[48] and the viewpoint languages of RM-ODP[3][4].

> **示例 3**：AADL[57]、ArchiMate[61]、系统建模语言（SysML）[47]、ISO 19440、业务流程模型与标记法（BPMN）[46]、统一建模语言（UML）[49]、统一架构框架（UAF）概要[48]以及 RM-ODP 的视角语言[3][4]。

> **NOTE 2** ADLs identify one or more AD elements which are instances of the architectural constructs: stakeholder, concern, architecture viewpoint, model kind, legend, etc.

> **注 2**：ADL 识别一个或多个架构描述元素，它们是下列架构构造的实例：利益相关方、关注点、架构视角、模型种类、图例等。

Figure 6 provides the conceptual model for an ADL.

图 6 给出 ADL 的概念模型。

> **NOTE 3** Requirements on ADLs are specified in 7.2.

> **注 3**：对 ADL 的要求在 7.2 中规定。

![Figure 6 — Conceptual model of an architecture description language](ISO_IEC_IEEE 42010 2023.assets/fig-06.png)

**Figure 6 — Conceptual model of an architecture description language**

**图 6 — 架构描述语言的概念模型**

### 6 Specification of an architecture description 架构描述的规格

#### 6.1 Architecture description identification and overview 架构描述的标识与概述

An AD shall identify the entity of interest and the expected environment of that entity of interest.

AD 应识别所关注实体以及该所关注实体的预期环境。

An AD shall include a statement of its intended purpose.

AD 应包含对其预期目的的陈述。

An AD shall include identifying information and supplementary information as determined by the project and/or organization.

AD 应包含由项目和／或组织确定的标识信息和补充信息。

> **EXAMPLE** Date of issue and status; authors, reviewers, approving authority, issuing organization; change history; summary; scope; context; glossary; version control information; configuration management information and references. See ISO/IEC/IEEE 15289 or ISO/IEC TS 33060 for additional examples.

> **示例**：发布日期和状态；作者、评审者、批准机构、发布组织；更改历史；摘要；范围；语境；术语表；版本控制信息；配置管理信息和引用文件。更多示例见 ISO/IEC/IEEE 15289 或 ISO/IEC TS 33060。

> **NOTE 1** For an AD intended to serve as a reference for another AD, the entity of interest is abstract, or a generalization of entities of interest, and the purpose of the AD is to express a reference architecture which could provide a basis for further ADs.

> **注 1**：对于意在充当另一 AD 参考的 AD，其所关注实体是抽象的，或者是对若干所关注实体的泛化，而该 AD 的目的是表达一种参考架构，可为后续 AD 提供基础。

> **NOTE 2** This document does not specify a format for ADs.

> **注 2**：本文件不规定 AD 的格式。

> **NOTE 3** This document does not prescribe how ADs are created. For example, they can be individually constructed, generated with automated tools, derived from or based upon other information sources and models.

> **注 3**：本文件不规定 AD 如何创建。例如，AD 可以单独构造、用自动化工具生成、从其他信息源和模型导出或以它们为基础。

> **NOTE 4** This document does not prescribe the extent or expectation regarding the use of formal modelling methods in an AD. While informal methods can be used effectively, formal modelling methods are often less ambiguous.

> **注 4**：本文件不规定在 AD 中使用形式化建模方法的程度或期望。虽然非形式化方法能有效使用，但形式化建模方法往往歧义更少。

#### 6.2 Identification of stakeholders 利益相关方的识别

An AD shall identify the stakeholders having concerns that are considered fundamental to the architecture of the entity of interest and consistent with the purpose of the AD.

AD 应识别具有下列关注点的利益相关方：这些关注点被认为对于所关注实体的架构是基本的，并且与该 AD 的目的相一致。

> **EXAMPLE** Stakeholders include users, operators, acquirers, owners, suppliers and vendors, architects, designers and developers, implementers, maintainers, regulators (including government), testers, public-at-large, adversaries and competitors.

> **示例**：利益相关方包括用户、操作者、获取方、所有者、供应方与厂商、架构师、设计师与开发者、实施者、维护者、监管者（包括政府）、测试者、公众、对手和竞争者。

An AD should identify the possible impacts of the architecture on the current and future stakeholders.

AD 宜识别架构对当前和未来利益相关方的可能影响。

Consideration shall be given to recommendations made in previous evaluations of the architecture or of related architectures.

应考虑以往对该架构或相关架构的评估中所提出的建议。

An AD shall include a statement of known resource limitations or other constraints that prevented the AD from addressing identified stakeholders and architecture considerations, i.e. concerns, perspectives, and aspects.

AD 应包含对已知资源限制或其他约束的陈述，这些限制或约束使该 AD 未能处理已识别的利益相关方和架构考量因素，即关注点、利益相关方角度和方面体。

Non-conformances shall be identified and explained with rationales.

应识别不符合项，并给出理由予以说明。

#### 6.3 Identification of stakeholder perspectives 利益相关方角度的识别

An AD shall identify stakeholder perspectives considered relevant to the architecture of the entity of interest and consistent with the purpose of the AD.

AD 应识别被认为与所关注实体的架构相关且与该 AD 的目的相一致的利益相关方角度。

An AD shall associate each identified perspective with the identified stakeholders holding that perspective.

AD 应使每个已识别的角度与持有该角度的已识别利益相关方相关联。

Within the scope of the intended purpose of the AD, the architecting effort should identify present or future stakeholder perspectives which may be relevant to the entity of interest.

在该 AD 预期目的的范围内，架构工作宜识别可能与该所关注实体相关的当前或未来的利益相关方角度。

For each identified perspective, an AD shall enumerate its resulting concerns from among identified concerns (per 6.4).

对于每个已识别的角度，AD 应依据 6.4 在已识别的关注点中列举出由该角度产生的关注点。

> **EXAMPLE** Stakeholder perspectives include: strategic, organizational, operational, logical, physical and technological perspectives.

> **示例**：利益相关方角度包括：战略角度、组织角度、运行角度、逻辑角度、物理角度和技术角度。

> **NOTE 1** This document does not prescribe: the granularity of concerns; the granularity and dependencies of stakeholder perspectives; how stakeholder perspectives relate to each other; or how stakeholder perspectives relate to other statements about an entity such as stakeholder needs, entity goals, or entity requirements. These issues are subjects for specific AD, ADFs, architecting methods, or other practices.

> **注 1**：本文件不规定：关注点的粒度；利益相关方角度的粒度与依赖关系；利益相关方角度彼此如何关联；或者利益相关方角度如何与关于实体的其他陈述（如利益相关方需要、实体目标或实体要求）相关联。这些问题属于特定 AD、ADF、架构工作方法或其他实践的议题。

> **NOTE 2** See Annex F for examples of stakeholder perspectives as used in ADFs.

> **注 2**：利益相关方角度在 ADF 中的用法示例见附录 F。

#### 6.4 Identification of concerns 关注点的识别

An AD shall identify the concerns considered relevant to the architecture of the entity of interest and consistent with the purpose of the AD.

AD 应识别被认为与所关注实体的架构相关且与该 AD 的目的相一致的关注点。

> **EXAMPLE** Concerns include the following: suitability of the architecture for achieving the objectives for the entity of interest, enterprise capability and capacity to implement the entity of interest, the feasibility of realizing and operating the entity of interest, the potential risks and impacts of the entity of interest to its stakeholders throughout its life cycle, added value to the stakeholder(s), reuse of known architectures, resilience, extensibility, adaptability, latency, resource utilization, effectiveness, operability, usefulness, usability, interoperability, complexity, sustainability and evolvability of the entity of interest, environmental impacts of the development, use, and disposal of the entity of interest.

> **示例**：关注点包括下列各项：架构对于实现所关注实体目标的适宜性；企业实施所关注实体的能力与容量；实现和运行所关注实体的可行性；所关注实体在其整个生存周期内对其利益相关方的潜在风险与影响；对利益相关方的增值；已知架构的复用；所关注实体的韧性、可扩展性、适应性、时延、资源利用、有效性、可操作性、有用性、易用性、互操作性、复杂性、可持续性和可演化性；所关注实体的开发、使用和处置的环境影响。

An AD shall associate each identified concern with the identified stakeholders holding that concern.

AD 应使每个已识别的关注点与持有该关注点的已识别利益相关方相关联。

> **NOTE 1** In general, the association of concerns with stakeholders is many-to-many.

> **注 1**：一般而言，关注点与利益相关方的关联是多对多的。

> **NOTE 2** Consideration of past, present or future concerns can be relevant to the entity of interest.

> **注 2**：对过去、现在或未来关注点的考虑能与所关注实体相关。

> **NOTE 3** Concerns expressed as interrogative questions and with appropriate detail to the purpose of the AD enable more efficient and effective communication.

> **注 3**：以疑问句形式表达、且详细程度适合该 AD 目的的关注点，能带来更高效、更有效的沟通。

#### 6.5 Identification of aspects 方面体的识别

An AD shall identify aspects considered relevant to the architecture of the entity of interest and consistent with the purpose of the AD.

AD 应识别被认为与所关注实体的架构相关且与该 AD 的目的相一致的方面体。

Each identified aspect shall be associated with the concerns that apply.

每个已识别的方面体应与适用的关注点相关联。

> **EXAMPLE** Aspects include, among others, structural, behavioural, functional, programmatic aspects.

> **示例**：方面体包括（但不限于）结构方面体、行为方面体、功能方面体和计划方面体。

> **NOTE** This document does not prescribe: the granularity and dependencies of aspects; how aspects relate to each other; or how aspects relate to other statements about an entity such as stakeholder needs, entity goals, or entity requirements. These issues are subjects for specific ADs, ADFs, ADLs, architecting methods, or other practices. See Annex F for examples of ADFs that use particular aspects and stakeholder perspectives.

> **注**：本文件不规定：方面体的粒度与依赖关系；方面体彼此如何关联；或者方面体如何与关于实体的其他陈述（如利益相关方需要、实体目标或实体要求）相关联。这些问题属于特定 AD、ADF、ADL、架构工作方法或其他实践的议题。使用特定方面体和利益相关方角度的 ADF 示例见附录 F。

#### 6.6 Inclusion of architecture viewpoints 架构视角的纳入

An AD shall include or reference each architecture viewpoint used therein.

AD 应包含或引用其中所使用的每个架构视角。

Each architecture viewpoint shall include version identification as specified by the organization and/ or project.

每个架构视角应包含由组织和／或项目规定的版本标识。

The specification of each included architecture viewpoint shall be in accordance with the provisions of Clause 8.

所包含的每个架构视角的规格应符合第 8 章的规定。

Each concern identified in accordance with 6.4 shall be framed by at least one architecture viewpoint.

依据 6.4 识别的每个关注点应由至少一个架构视角来框定。

Each stakeholder perspective identified in accordance with 6.3 shall be associated with the architecture viewpoints which cover that perspective.

依据 6.3 识别的每个利益相关方角度应与覆盖该角度的架构视角相关联。

> **EXAMPLE** Function, Information, Resource, and Organization.

> **示例**：功能、信息、资源和组织。

> **NOTE 1** This document does not require the use of any particular architecture viewpoints.

> **注 1**：本文件不要求使用任何特定的架构视角。

> **NOTE 2** Annex B and Annex C provide additional information pertaining to specification of architecture viewpoints.

> **注 2**：附录 B 和附录 C 提供与架构视角规格有关的附加信息。

> **NOTE 3** An architecture viewpoint can serve as a contract between architect and other stakeholders. For the concerns framed by the viewpoint, architect and stakeholders can agree on what notations and representational conventions will be used to address those concerns. This contract agreement can be made before any detailed architecting is undertaken to reduce or avoid surprises.

> **注 3**：架构视角能充当架构师与其他利益相关方之间的契约。对于由该视角所框定的关注点，架构师与利益相关方能就用以应对这些关注点的记法和表示约定达成一致。此项契约约定能在开展任何详细架构工作之前达成，以减少或避免意外。

#### 6.7 Inclusion of architecture views 架构视图的包含

An AD shall include one or more architecture views for each architecture viewpoint used.

对于所使用的每个架构视角，AD 应包含一个或多个架构视图。

> **NOTE 1** When a viewpoint governs more than one view in a particular AD, they are describing one architecture.

> **注 1**：当某一视角在特定 AD 中管控一个以上架构视图时，这些视图描述的是同一个架构。

> **EXAMPLE 1** Several kinds of views can be described for a functional viewpoint: for example, functional chains express the behaviour and function trees express decomposition.

> **示例 1**：对于功能视角，能描述若干种视图：例如，功能链表达行为，功能树表达分解。

Each architecture view shall include version identification as specified by the organization and/or project.

每个架构视图应包含由组织和／或项目所规定的版本标识。

Each stakeholder perspective identified by the AD in accordance with 6.3 shall be addressed by at least one view in accordance with the view’s governing viewpoint.

AD 按照 6.3 所识别的每个利益相关方角度，应由至少一个架构视图按照该视图的管控视角予以应对。

Each concern identified by the AD in accordance with 6.4 shall be addressed by at least one view in accordance with the view's governing viewpoint.

AD 按照 6.4 所识别的每个关注点，应由至少一个架构视图按照该视图的管控视角予以应对。

Each architecture aspect identified by the AD in accordance with 6.5 shall be addressed by at least one view in accordance with the view’s governing viewpoint.

AD 按照 6.5 所识别的每个方面体，应由至少一个架构视图按照该视图的管控视角予以应对。

Each architecture view shall adhere to the conventions of its governing architecture viewpoint. Each architecture view may address more than one concern.

每个架构视图应遵循其管控架构视角的约定。每个架构视图可应对一个以上关注点。

Each architecture view shall include or provide a reference for:

每个架构视图应包含下列内容，或为其提供引用：

a) identifying and supplementary information as specified by the organization and/or project;

a) 由组织和／或项目所规定的标识信息和补充信息；

b) identification of its governing architecture viewpoint;

b) 其管控架构视角的标识；

c) one or more view components that address all of the concerns (per 6.4) framed by its governing architecture viewpoint (per 6.6) and that cover some or all of the entity of interest with respect to that viewpoint; and d) the recording of any known issues within a view with respect to its governing architecture viewpoint.

c) 一个或多个视图组件，它们应对其管控架构视角（按 6.6）所框定的全部关注点（按 6.4），并就该视角而言覆盖所关注实体的部分或全部；以及d) 就视图的管控架构记载该视图内任何已知问题视角。

> **NOTE 2** “Known issues” per d) include unresolved issues, risks, exceptions and deviations from the governing model kinds or legends. Open issues can lead to decisions to be made. Exceptions and deviations can be documented as decision outcomes and rationale (per 6.10).

> **注 2**：d) 中的“已知问题”包括未解决的问题、风险、例外情况，以及对管控模型种类或图例的偏离。未决问题能引致需要作出的决策。例外情况和偏离能记载为决策结果和理由（按 6.10）。

> **NOTE 3** Per c), it is not necessary to require that each view covers the entire entity of interest with regard to the purpose and scope of the AD. It can, for example, be scoped to purposely be limited to one particular portion of the entity, sometimes by direction, sometimes by limited time or resources, or sometimes based on the narrow scope of the architecting effort

> **注 3**：按 c)，并非必须要求每个视图都就 AD 的目的和范围覆盖整个所关注实体。例如，视图的范围可以有意识地限定于该实体的某一特定部分——有时是依据指令，有时是由于时间或资源有限，有时是基于架构工作的狭窄范围

An AD may include other information which is not part of any architecture view.

AD 可包含不属于任何架构视图的其他信息。

> **EXAMPLE 2** Information parts not within any view could include overviews of the entity of interest, architecture principles, architecture patterns and architecture styles whose application spans more than one view; referenced bases for the architecture, such as domain or reference architectures; correspondences between views; and architecture rationale. This information can assist stakeholders and other users of the AD responsible for its maintenance and development.

> **示例 2**：不属于任何视图的信息部分可包括：所关注实体的概览；架构原则、架构模式以及适用跨越一个以上视图的架构风格；所引用的架构依据，如领域架构或参考架构；视图之间的对应关系；以及架构理由。此类信息能帮助利益相关方以及负责 AD 维护和开发的其他 AD 使用者。

#### 6.8 Inclusion of view components 视图组件的包含

An architecture view shall be composed of one or more view components in accordance with its governing architecture viewpoint.

架构视图应按照其管控架构视角由一个或多个视图组件组成。

Each view component shall include version identification as specified by the organization and/or project.

每个视图组件应包含由组织和／或项目所规定的版本标识。

Each view component shall identify its governing model kind, if any, and adhere to the conventions of its governing architecture viewpoint (see 6.6).

每个视图组件应标识其管控模型种类（如有），并遵循其管控架构视角的约定（见 6.6）。

Within a view, one or more view components can be used to selectively present some or all of the informational content required by the architecture viewpoint to highlight points of interest.

在一个视图内，能使用一个或多个视图组件来有选择地呈现架构视角所要求的部分或全部信息内容，以突显值得关注的要点。

A view component may be a part of more than one architecture view. Correspondences can express the relationships among components shared across views.

一个视图组件可以是多个架构视图的一部分。对应关系能表达跨视图共享的组件之间的关系。

When a view component does not have a governing model kind, i.e. for an information part not described with a model, a view component legend shall be included to specify the conventions used in that view component.

当视图组件没有管控模型种类时，即对于未用模型描述的信息部分，应包含视图组件图例，以规定该视图组件中所用的约定。

> **EXAMPLE** A view component that is a record of expert opinion, rather than a model that one can analyse using calculations, simulation, or any other suitable analysis method.

> **示例**：一种记录专家意见的视图组件，而非能用计算、仿真或任何其他适宜分析方法加以分析的模型。

> **NOTE 1** Sharing view components between architecture views permits an AD to capture distinct but related concerns without redundancy or repetition of the same information in multiple views and reduces possibilities for inconsistency. Sharing of view components also permits an aspect-oriented style of AD[52]: view components shared across architecture views can be used to express architectural perspectives; view components shared within an architecture view can be used to express architectural textures. View components can be used as “containers” for applying architecture patterns[27] or architecture styles to express fundamental schemes (such as layers, three-tier, peer-to-peer and model-view-controller) within architecture views.

> **注 1**：在架构视图之间共享视图组件，使 AD 能够捕获不同但相关的关注点，而无需在多个视图中冗余或重复相同信息，并减少出现不一致的可能性。共享视图组件还允许面向方面体式的 AD[52]：跨架构视图共享的视图组件能用于表达架构透视；在一个架构视图内共享的视图组件能用于表达架构纹理。视图组件能用作“容器”，以在架构视图内应用架构模式[27]或架构风格来表达基本方案（如分层、三层、对等和模型—视图—控制器）。

> **NOTE 2** This document does not prescribe the level of formality of view components to be used in an AD. While model-based view components that have a formal specification of semantics and syntax can be less ambiguous, non-model-based view components can also be used effectively.

> **注 2**：本文件不规定 AD 中拟使用的视图组件的形式化程度。虽然具有形式化语义和语法规格的基于模型的视图组件能较少歧义，但非基于模型的视图组件也能有效使用。

#### 6.9 Recording of architecture correspondences 架构对应关系的记录

##### 6.9.1 Consistency within an architecture description 架构描述内的一致性

An AD shall record any known inconsistencies.

AD 应记载任何已知的不一致。

An AD should include or reference an analysis of consistency of its architecture views, its view components and other AD elements.

AD 宜包含或引用对其架构视图、视图组件及其他 AD 元素一致性的分析。

Correspondences and correspondence methods, as specified in 6.9.2 and 6.9.3, may be used to express, record, enforce and analyse consistency between views, their view components and other AD elements within and among ADs.

6.9.2 和 6.9.3 所规定的对应关系和对应方法，可用于表达、记载、强制实施和分析各视图、其视图组件及其他 AD 元素在 AD 之内和 AD 之间的一致性。

##### 6.9.2 Correspondences 对应关系

An AD shall include or reference a list of AD element correspondences.

AD 应包含或引用一份架构描述元素对应关系清单。

An AD element correspondence shall identify one or more participating AD elements.

一条架构描述元素对应关系应标识一个或多个参与的架构描述元素。

> **EXAMPLE** An AD element satisfies a Requirement as demonstrated by an Evaluation Method: TracesToDemo (an AD Element, a Requirement, an Evaluation Method).

> **示例**：一个架构描述元素满足一项要求，如由一种评估方法所证明：TracesToDemo（一个架构描述元素、一项要求、一种评估方法）。

An AD element correspondence may involve elements within an AD or across several ADs.

一条架构描述元素对应关系可涉及一个 AD 内的元素，也可涉及若干 AD 之间的元素。

An AD element correspondence shall identify any governing correspondence methods (see 6.9.3).

一条架构描述元素对应关系应标识任何管控对应方法（见 6.9.3）。

Each AD element correspondence shall identify the participating ADs.

每条架构描述元素对应关系应标识参与的 AD。

> **NOTE** AD element Correspondences can be used to express relations among ADs, ADFs, and ADLs. See Zachman Framework [56] example in Annex F.

> **注**：架构描述元素对应关系能用于表达 AD、ADF 和 ADL 之间的关系。参见附录 F 中的 Zachman 框架[56]示例。

##### 6.9.3 Correspondence methods 对应方法

An AD shall include or reference a list of correspondence methods applying to itself or its AD elements.

AD 应包含或引用一份适用于其自身或其架构描述元素的对应方法清单。

A correspondence method applying to one or more AD elements can originate in the AD elements, in the AD itself; in the specification of a model kind or an architecture viewpoint used for the AD (see 8); or in the specification of an ADF or ADL used therein (see 7).

适用于一个或多个架构描述元素的对应方法，能源自这些架构描述元素、源自 AD 本身；源自用于该 AD 的模型种类或架构视角的规格（见 8）；或源自其中所用的 ADF 或 ADL 的规格（见 7）。

> **NOTE 1** For each applied correspondence method, an AD shall record whether the method holds (is satisfied) or otherwise record all known violations. A correspondence method holds if an associated correspondence can be shown to be satisfied. A correspondence method is violated if an associated correspondence cannot be shown to be satisfied or when no associated correspondence exists.

> **注 1**：对于每个所应用的对应方法，AD 应记录该方法是否成立（得到满足），否则应记录所有已知违例。若某一关联的对应关系能被证明得到满足，则该对应方法成立。若某一关联的对应关系不能被证明得到满足，或不存在关联的对应关系，则该对应方法被违反。

An AD shall include or reference each correspondence method applying to it.

AD 应包含或引用适用于它的每个对应方法。

> **NOTE 2** A correspondence method applying to an AD could originate in the AD; in the specification of a viewpoint or a model kind (see Clause 8); or in the specification of an ADF or ADL selected for use in that AD (see Clause 7).

> **注 2**：适用于某一 AD 的对应方法能源自该 AD；源自某一视角或模型种类的规格（见第 8 章）；或源自为该 AD 中使用而选择的 ADF 或 ADL 的规格（见第 7 章）。

#### 6.10 Recording of architecture decisions and rationale 架构决策与理由的记录

##### 6.10.1 Decision recording 决策记录

An AD shall record architecture decisions considered essential to the architecture of the entity of interest within the scope and intended purpose of the AD.

AD 应记录在 AD 的范围和预期目的内被认为对所关注实体的架构必不可少的架构决策。

> **NOTE 1** An AD expresses decisions about an architecture. Architecture rationale expresses why decisions have been chosen.

> **注 1**：AD 表述关于某一架构的决策。架构理由表述决策为何被选定。

The AD should record alternative decisions considered and rejected and the rationale for those choices.

AD 宜记录已考虑并否决的备选决策以及作出这些选择的理由。

The organization and/or project should establish a decision recording and sharing strategy and criteria for selecting important decisions to record and support with rationale in the AD.

组织和／或项目宜建立决策记录与共享策略，以及用于选择在 AD 中记录并以理由支持的重要决策的准则。

Decisions, among others, to consider for selection criteria are those:

拟作为选择准则考虑的决定（除其他外）为下列各项：

- regarding architecturally significant requirements;

- 涉及架构上重要的要求的；

- needing a major investment of effort or time to make, implement or enforce;

- 作出、实施或强制执行需要投入大量精力或时间的；

- affecting key stakeholders or a number of stakeholders;

- 影响关键利益相关方或若干利益相关方的；

- addressing fundamental concerns (such as performance, evolvability, safety);

- 应对基本关注点（如性能、可演化性、安全性）的；

- necessitating intricate or non-obvious reasoning;

- 需要复杂或非显而易见的推理的；

- that are highly sensitive to changes;

- 对变更高度敏感的；

- that are likely to be costly to change;

- 变更代价可能高昂的；

- that form a base for project planning and management (such as work breakdown structure creation,

- 构成项目策划与管理基础（如创建工作分解结构、

critical chain identification and management quality gate tracking);

关键链识别和管理质量门禁跟踪）的；

- that result in the replacement of assumptions with known information;

- 导致以已知信息替换假设的；

- that result in significant capital expenditures or indirect costs;

- 导致重大资本支出或间接成本的；

- linked to requirement compliance;

- 与需求符合性相关联的；

- linked to technical standard selection;

- 与技术标准选择相关联的；

- linked to system vulnerability mitigation.

- 与系统脆弱性缓解相关联的。

When recording decisions, the inclusion of the following information should be considered:

记录决策时，宜考虑包含下列信息：

- unique decision identification;

- 决策的唯一标识；

- clear statement of decision;

- 对决策的清晰陈述；

- identification of decision authority or owner;

- 决策权属方或决策责任人的标识；

- identification of constraints and assumptions that influence the decision;

- 影响该决策的约束和假设的标识；

- link decision to the concerns or aspects of an entity to which it pertains;

- 将该决策链接到其所涉实体的关注点或方面体；

- link decision to AD elements affected by the decision;

- 将该决策链接到受该决策影响的 AD 元素；

- link to decision rationale;

- 链接到决策理由；

- relationships to other decisions;

- 与其他决策的关系；

- consequences of the decision (relating to other decisions) are recorded;

- 该决策的后果（与其他决策相关）得到记录；

- timestamps for when the decision occurred, when approved and when modified;

- 决策作出、获批和修改的时间戳；

- source citations for additional information.

- 附加信息的来源引用。

> **NOTE 2** The lists of decisions are not intended to be exhaustive.

> **注 2**：决策清单并非意在穷尽。

> **NOTE 3** Sometimes recording rejected alternatives and their rationale for rejection is useful, e.g. when in the future the rationale no longer applies and the decisions are necessary.

> **注 3**：有时记录被否决的备选方案及其否决理由是有用的，例如当该理由在将来不再适用而相关决策成为必要时。

> **EXAMPLE** Examples of types of relationships are: constrains, influences, enables, triggers, forces, subsumes, refines, conflicts with, exposes, and is compatible with (See Reference [39] and Reference [60]).

> **示例**：关系类型的示例包括：约束、影响、使能、触发、强制、包含、细化、与…冲突、暴露以及与…兼容（见参考文献 [39] 和参考文献 [60]）。

Relations among decisions can be captured via correspondences or by applying correspondence methods.

决策之间的关系能通过对应关系或通过应用对应方法加以捕获。

##### 6.10.2 Rationale recording 理由记录

An AD should include or reference a rationale for each architecture viewpoint selected for use (per 6.6).

AD 宜包含或引用为其使用而选择的每个架构视角的理由（按 6.6）。

An AD should include or reference a rationale for each ADF and each ADL selected for use.

AD 宜包含或引用为其使用而选择的每个 ADF 和每个 ADL 的理由。

An AD shall include or reference rationale for each essential architecture decision (per 6.10.1).

AD 应包含或引用每项必不可少的架构决策的理由（按 6.10.1）。

An AD should include or reference evidence of consideration and rationale for selection of alternatives.

AD 宜包含或引用考虑的证据以及选择备选方案的理由。

An AD should include a rationale for an AD limitation (e.g. resource problem, timing problem, and effort avoided for well-known description already covered by other ADs).

AD 宜包含 AD 局限性的理由（如资源问题、时间问题，以及因其他 AD 已涵盖的众所周知的描述而省去的投入）。

### 7 Architecture description frameworks and architecture description languages 架构描述框架与架构描述语言

#### 7.1 Specification of an architecture description framework / 7.1.1 ｜ 架构描述框架的规格 / 7.1.1

An ADF (3.5) shall include or reference:

ADF(3.5)应包含或引用：

a) information identifying the ADF and its intended scope of applicability;

a) 标识该 ADF 及其预期适用范围的信息；

b) version identification of the ADF as specified by the organization and/or project;

b) 由组织和／或项目规定的 ADF 版本标识；

c) one or more typical stakeholders (per 6.2);

c) 一个或多个典型利益相关方（按 6.2）；

d) one or more typical concerns held by typical stakeholders (per 6.4);

d) 典型利益相关方持有的一个或多个典型关注点（按 6.4）；

e) one or more architecture viewpoints that frame those typical concerns (per 8.1);

e) 框定这些典型关注点的一个或多个架构视角（按 8.1）；

**7.1.2** When expected in a conforming AD, an ADF should specify:

**7.1.2** 当符合性 AD 中有此预期时，ADF 宜规定：

a) one or more stakeholder perspectives (per 6.3);

a) 一个或多个利益相关方角度（按 6.3）；

b) one or more aspects (per 6.5);

b) 一个或多个方面体（按 6.5）；

c) definition of one or more structuring formalisms to organize viewpoints (per 5.4.2);

c) 用以组织架构视角的一个或多个结构化形式体系的定义（按 5.4.2）；

d) one or more model kinds that apply to specified architecture viewpoints (per 8.2);

d) 适用于所规定架构视角的一个或多个模型种类（按 8.2）；

e) definition of one or more legends that apply to specified architecture viewpoints;

e) 适用于所规定架构视角的一个或多个图例的定义；

f) identification of ADLs that can be used to create views with regards to the viewpoint specification (per 7.2);

f) 可用于参照视角规格创建架构视图的 ADL 的标识（按 7.2）；

g) correspondence methods (per 6.9.3);

g) 对应方法（按 6.9.3）；

h) view methods (per 8.3);

h) 视图方法（按 8.3）；

i) version identification as specified by the organization and/or project.

i) 由组织和／或项目规定的版本标识。

The intended scope of use can range on a scale between the very generic (all industries and application domains and all kinds of entities of interest (EoI), and the use of the ADF for multiple purposes) through to the very special or particular (such as intended to cover a given industry, application domain, or kind of EoI, a particular EoI, or a particular EoI in a given stage of its life, or for a particular purpose). This classification is similar to the genericity dimension defined as a structuring formalism in ISO 15704 (see A.4.4).

预期使用范围能在一个尺度上变化：从非常通用的一端（所有行业和应用域、所有种类的所关注实体（EoI），以及将 ADF 用于多种目的），直到非常专门或特定的一端（如意在涵盖某一给定行业、应用域或某类 EoI，某一特定 EoI，或处于其生存周期某一给定阶段的某一特定 EoI，或用于某一特定目的）。该分类类似于 ISO 15704 中作为结构化形式体系定义的通用性维度（见 A.4.4）。

> **NOTE 1** The word typical in the list above is intended to mean ‘typical in the intended scope of applicability’.

> **注 1**：上文列表中的 typical 一词意在表示“在预期适用范围内典型的”。

The specification of an ADF should include conditions on applicability.

ADF 的规格宜包含适用性条件。

> **EXAMPLE 1** The following are conditions on applicability:

> **示例 1**：下列各项是适用性条件：

- An ADF can require an AD to identify stakeholders when the entity of interest operates within a jurisdiction

- ADF 可以要求 AD 在下列情况下识别利益相关方：所关注实体在某管辖区域内运行，

impacting their business model.

而该管辖区域影响其业务模式。

- An ADF can permit an AD to omit a real-time viewpoint when none of its concerns have been identified for the

- ADF 可以允许 AD 在下列情况下省略实时视角：其关注点均未针对

entity of interest.

所关注实体得到识别。

- An ADF can allow an AD to omit use of a particular model kind when no selected viewpoint uses that model

- ADF 可以允许 AD 在下列情况下省略对某一特定模型种类的使用：所选择的视角均不使用该模型

kind.

种类。

The specification of an ADF should indicate its consistency with the concepts in 5.2.

ADF 的规格宜指明其与 5.2 中诸概念的一致性。

> **NOTE 2** The above requirement can be met through a metamodel, a mapping of framework constructs to the requirements in Clause 5, a text narrative, or in some other manner.

> **注 2**：上述要求能通过元模型、将框架构造映射到第 5 章各项要求、文字叙述或某种其他方式予以满足。

An AD that conforms to the requirements of Clause 6 adheres to a specification of an ADF when the AD identifies and considers the applicability of each:

符合第 6 章要求的 AD，当该 AD 标识并考虑下列各项各自的适用性时，即遵循某一 ADF 的规格：

- stakeholder (per 6.2) identified by the ADF;

- 由该 ADF 标识的利益相关方（按 6.2）；

- stakeholder perspective (per 6.3) identified by the ADF;

- 由该 ADF 标识的利益相关方角度（按 6.3）；

- concern (per 6.4) identified by the ADF;

- 由该 ADF 标识的关注点（按 6.4）；

- aspect (per 6.5) identified by the ADF;

- 由该 ADF 标识的方面体（按 6.5）；

- architecture viewpoint (per 8.1) specified by the ADF;

- 由该 ADF 规定的架构视角（按 8.1）；

- correspondence method (per 6.9.3) specified by the ADF.

- 由该 ADF 规定的对应方法（按 6.9.3）。

A specification of an ADF may establish additional rules for adherence.

ADF 的规格可确立附加的遵循规则。

An AD can adhere to one or more specifications of ADFs, or to no framework specifications.

一个 AD 能遵循一个或多个 ADF 的规格，或不遵循任何框架规格。

> **NOTE 3** For an AD to adhere to more than one framework specification entails a reconciliation between each framework specification’s identified stakeholders, concerns, aspects, stakeholder perspectives, architecture viewpoints, model kinds, and correspondence methods within the AD.

> **注 3**：一个 AD 遵循多个框架规格，意味着要在该 AD 内对每个框架规格所标识的利益相关方、关注点、方面体、利益相关方角度、架构视角、模型种类和对应方法进行协调。

An ADF may have a structuring formalism with one or more structural categories to provide ways of representing relationships among various elements of the architecture and enhancing opportunities for analysis of interactions among those elements.

ADF 可具有一种结构化形式体系，其中含一个或多个结构类别，以提供表示架构各元素之间关系的方式，并增强对这些元素之间交互进行分析的机会。

> **EXAMPLE 2** Structural categories include architectural constructs such as: domains, model kinds, perspectives, aspects, interrogatives, levels of abstraction, subjects of concern, aspects of concern, phases, layers and architectural tiers.

> **示例 2**：结构类别包括诸如下列的架构构造物：域、模型种类、角度、方面体、疑问类、抽象层级、关注主题、关注方面体、阶段、层和架构层级。

> **NOTE 4** See Annex F for examples of architecture frameworks using aspects, stakeholder perspectives and other structural categories.

> **注 4**：使用方面体、利益相关方角度及其他结构类别的架构框架示例见附录 F。

#### 7.2 Specification of an architecture description language 架构描述语言的规格

The specification of an ADL shall include or reference:

ADL 的规格应包含或引用：

a) identification of typical concerns (6.4) or aspects (6.5) covered by the ADL;

a) 对 ADL 所覆盖的典型关注点(6.4)或方面体(6.5)的标识；

b) the identification of one or more view methods to be selected from the ADL (per 8.3);

b) 对拟从 ADL 中选用的一个或多个视图方法（按 8.3）的标识；

c) one or more model kinds (per 8.2) implemented by the ADL for use in framing the relevant concerns or reflect the relevant aspects;

c) 由 ADL 实现、用于框定相关关注点或反映相关方面体的一个或多个模型种类（按 8.2）；

d) any architecture viewpoints (per 8.1) implemented by the ADL;

d) 由 ADL 实现的任何架构视角（按 8.1）；

e) any correspondence methods (per 6.9.3);

e) 任何对应方法（按 6.9.3）；

f) version identification as specified by the organization and/or project.

f) 由组织和／或项目规定的版本标识。

### 8 Architecture viewpoints and model kinds 架构视角与模型种类

#### 8.1 Specification of an architecture viewpoint 架构视角的规格

The specification of an architecture viewpoint shall include or reference:

架构视角的规格应包含或引用：

a) any stakeholder perspectives associated with this viewpoint (per 6.3);

a) 与本视角相关的任何利益相关方角度（按 6.3）；

b) one or more concerns (per 6.4) framed by this architecture viewpoint;

b) 由本架构视角框定的一个或多个关注点（按 6.4）；

c) one or more aspects related to those concerns (per 6.5);

c) 与那些关注点相关的一个或多个方面体（按 6.5）；

d) known typical stakeholders (per 6.2) holding those concerns which are framed by this architecture viewpoint (per item b));

d) 持有由本架构视角（按 b) 项）所框定的那些关注点的已知典型利益相关方（按 6.2）；

e) model kinds (per 8.2) and legends for use when constructing views (per 8.2);

e) 构造架构视图时使用的模型种类（按 8.2）和图例（按 8.2）；

f) correspondence methods capturing relations within resulting views and their view components (per 6.8);

f) 捕获所生成架构视图内及其视图组件之间关系的对应方法（按 6.8）；

g) references to any sources of information about this viewpoint.

g) 对本视角任何信息来源的引用。

A specification of an architecture viewpoint should identify view methods (per 8.3) used to create, interpret or analyse views governed by the associated architecture viewpoint; and one or more model kind (per 8.2).

架构视角的规格宜标识用于创建、解释或分析受该相关架构视角管控的架构视图的视图方法（按 8.3），以及一个或多个模型种类（按 8.2）。

Each legend shall provide guidance to users in interpreting the view components which it documents.

每个图例应就其所记载的视图组件的解释向用户提供指南。

The specification of an architecture viewpoint can use correspondence methods.

架构视角的规格能使用对应方法。

The specification of an architecture viewpoint can be included as part of an AD (Clause 6), as a part of the specification of an ADF or ADL (Clause 7) or individually using the requirements of this clause.

架构视角的规格能作为 AD 的一部分（第 6 章）、作为 ADF 或 ADL 的规格的一部分（第 7 章）纳入，或按本章的要求单独使用。

> **NOTE 1** When a specification of an architecture viewpoint is included and applied in an AD, the typical stakeholders of item e) are replaced by the known stakeholders identified in the AD.

> **注 1**：当架构视角的规格纳入 AD 并加以应用时，e) 项中的典型利益相关方由该 AD 中标识的已知利益相关方取代。

> **NOTE 2** This document does not require any particular specifications of architecture viewpoints to be used.

> **注 2**：本文件不要求使用任何特定的架构视角规格。

> **NOTE 3** Annex B provides guidance to specification of architecture viewpoints.

> **注 3**：附录 B 给出了架构视角规格的指南。

#### 8.2 Specification of a model kind 模型种类的规格

The specification of a model kind shall include or reference:

模型种类的规格应包含或引用：

a) conventions such as definition of a language, notation or modelling technique comprising the model kind;

a) 约定，例如构成该模型种类的语言、记法或建模技术的定义；

b) any view methods (per 8.3) and correspondence methods associated with the model kind;

b) 与该模型种类相关的任何视图方法（按 8.3）和对应方法；

c) any version identification as specified by the organization and/or project;

c) 由组织和／或项目规定的任何版本标识；

d) any sources of information about this model kind.

d) 关于本模型种类的任何信息来源。

> **NOTE** Item a) can be met in a number of ways such as with a metamodel, grammar or template for the specification of a model kind that defines the structure and interpretation of its models (see B.2.9).

> **注**：a) 项能以若干方式得到满足，例如借助用于模型种类规格的元模型、文法或模板，该规格定义其模型的结构与解释（见 B.2.9）。

#### 8.3 View methods 视图方法

A specification of an architecture viewpoint may include one or more view methods.

架构视角的规格可包含一个或多个视图方法。

View methods shall be defined in the specifications of model kinds (see 8.2), viewpoints (see 8.1), ADLs (see 7.2), and ADFs (see 7.1) when it is necessary to provide guidance on how views are constructed or used.

当需要就架构视图如何构造或使用提供指南时，应在模型种类（见 8.2）、视角（见 8.1）、ADL（见 7.2）和 ADF（见 7.1）的规格中定义视图方法。

If a model is used as an information source when creating a view, a view method should define how AD elements will be portrayed in the view component, how model data are transformed or translated for use in the view component and how relationships between information from different sources are portrayed in the view component.

若在创建架构视图时把模型用作信息来源，视图方法宜定义 AD 元素将如何在视图组件中呈现、模型数据如何转换或翻译以供视图组件使用，以及来自不同来源的信息之间的关系如何在视图组件中呈现。

If a “non-model” is used as an information source when creating a view, a view method should define how its contents are portrayed in the view component as AD elements, how the non-model-related data are transformed or translated for use in the view component, and how relationships between information from different sources are portrayed in the view component.

若在创建架构视图时把“非模型”用作信息来源，视图方法宜定义其内容如何作为 AD 元素在视图组件中呈现、与非模型相关的数据如何转换或翻译以供视图组件使用，以及来自不同来源的信息之间的关系如何在视图组件中呈现。

## Annex A (informative) — Notes on terms and concepts ｜ 附录 A（资料性）——术语与概念说明

### A.1 General 总则

This annex discusses the principles, concepts and terms on which this document is based. Figure A.1 depicts the main concepts of AD.

本附录讨论本文件所依据的原则、概念和术语。图 A.1 描绘了 AD 的主要概念。

![Figure A.1 — Conceptual model of an architecture description](ISO_IEC_IEEE 42010 2023.assets/fig-07.png)

**Figure A.1 — Conceptual model of an architecture description**

**图 A.1——架构描述的概念模型**

This document makes use of several terms (architecture, concern, aspect, stakeholder perspective, architecture view, architecture viewpoint, view component, model kind) which are in wide usage with several different meanings across the community. This Annex discusses these terms, the motivations for their definitions in this document, and contrasts these definitions with other usages.

本文件使用了若干术语（架构、关注点、方面体、利益相关方角度、架构视图、架构视角、视图组件、模型种类），这些术语在业界被广泛使用且具有多种不同含义。本附录讨论这些术语、本文件对其下定义的理由，并将这些定义与其他用法加以对照。

This document defines minimal requirements on ADs to support the scope established in Clause 1. The approach is to allow organizations maximum flexibility in applying the standard while demonstrating conformance with the requirements in Clauses 6, 7 and 8. Given the multi-disciplinary nature of architecting, the intent is to meet the needs of multiple stakeholders and allow different ways to describe the architecture of an entity of interest. The organization of ADs into architecture views governed by architecture viewpoints provides a mechanism for the separation of concerns based on the stakeholders, while providing an integrated view of the whole entity that is fundamental to the notion of architecture.

本文件对 AD 规定最低要求，以支撑第 1 章所确立的范围。其做法是允许组织在应用本标准时具有最大灵活性，同时证明符合第 6、7、8 章的要求。鉴于架构工作具有多学科性质，其意图是满足多个利益相关方的需要，并允许以不同方式描述所关注实体的架构。将 AD 组织为受架构视角管控的架构视图，提供了一种基于利益相关方分离关注点的机制，同时提供对整个实体的整体视图，而这对架构概念而言是基本的。

Establishing the quality of an architecture being described by a conforming AD (Is this a good architecture?) or the quality of an AD itself (Is this AD complete and consistent?) are factors for the evaluation of the AD. This document does not presume to impose conditions that are required for quality considerations. It does recommend that results of such evaluations be recorded (per 6.2).

确定符合性 AD 所描述的架构的质量（这是一个好的架构吗？）或 AD 本身的质量（此 AD 是否完整且一致？），是评估该 AD 的因素。本文件并不擅自规定质量考虑所必需的条件。它确实建议记录此类评估的结果（按 6.2）。

> **NOTE** Evaluation of architectures is the subject of ISO/IEC/IEEE 42030.

> **注**：架构的评估是 ISO/IEC/IEEE 42030 的主题。

### A.2 Entities and their architectures 实体及其架构

In this document, the term architecture is intended to convey the essence or fundamentals of an entity of interest. There are several key aspects to the definition of architecture (3.2) in this document. This definition is chosen to encompass a variety of previous uses of the term “architecture” by recognizing their underlying common themes. Principal among these is the need to understand and control those elements of an entity of interest that contribute to its utility, cost, time and risk within its environment. In some cases, the fundamental elements are physical or structural components of the entity and their relationships. Sometimes, the fundamental elements are functional or logical elements. In other cases, what is fundamental or essential to the understanding of an entity are its overarching principles or patterns. Properties can also be the fundamental characteristics of an entity, its elements and their relationships. The definition of architecture in this document is intended to encompass these distinct, but related uses, while encouraging a more rigorous delineation of what constitutes the architecture of an entity.

在本文件中，术语架构旨在表达所关注实体的精髓或基本要素。本文件中架构的定义(3.2)有若干关键方面。选择这一定义，是为了通过识别以往各种用法背后共同的主题，涵盖术语“架构”的多种既往用法。其中首要的是，需要理解并控制所关注实体中那些在其环境内影响其实用性、成本、时间和风险的要素。在某些情况下，基本要素是实体的物理或结构组成部分及其关系。有时，基本要素是功能或逻辑要素。在另一些情况下，对理解某个实体而言属于基本或本质的东西，是其总体原则或模式。属性也能是实体、其要素及其关系的基本特征。本文件中架构的定义旨在涵盖这些彼此不同但相互关联的用法，同时鼓励对何为实体的架构作出更严格的界定。

The phrase “concepts or properties” is used in the definition of architecture (3.2) to allow two differing philosophies to use this document without prejudice. These two philosophies are:

架构(3.2)的定义中使用“概念或属性”这一表述，是为了让两种不同的哲学观点都能不抱偏见地使用本文件。这两种哲学观点是：

- Architecture as concept: wherein architecture is a conception of an entity in one’s mind;

- 作为概念的架构：其中架构是人心中对某一实体的一种构想；

- Architecture as property: wherein architecture is a property or attribute of an entity of interest.

- 作为属性的架构：其中架构是所关注实体的一种属性或特性。

Empirical studies have discovered four metaphors for architecture found in organizations[59]:

实证研究发现，组织中存在四种关于架构的隐喻[59]：

- architecture as blueprint;

- 作为蓝图的架构；

- architecture as literature;

- 作为文献的架构；

- architecture as language;

- 作为语言的架构；

- architecture as decision.

- 作为决策的架构。

The conceptual foundation of this document does not presume any one of these metaphors; rather it works equally well with any of them. The existence of these multiple metaphors supports a central design tenet of this document: that architecture is inherently based upon multiple stakeholders with multiple concerns and using multiple viewpoints and aspects.

本文件的概念基础并不预设其中任何一种隐喻；相反，它与其中任何一种隐喻都同样契合。这些多重隐喻的存在，支持本文件的一项核心设计信条：架构在本质上以持有多种关注点、使用多种架构视角和方面体的多个利益相关方为基础。

### A.3 Concerns 关注点

This document uses the term concern to mean any topic of interest pertaining to the entity being architected or to the architecture itself. Stakeholders, including the architect, of that subject entity hold these concerns. Some concerns drive or relate to the architecture and therefore this document requires their identification as a part of the AD. Concerns range over a wide spectrum of interests (including technical, personal, developmental, technological, business, operational, organizational, political, economic, legal, regulatory, ecological, social influences).

本文件使用术语关注点，意指与正在被架构的实体或与架构本身有关的任何所关注的论题。该主体实体的利益相关方（包括架构师）持有这些关注点。有些关注点驱动架构或与架构相关，因此本文件要求将其识别为 AD 的一部分。关注点涵盖广泛的利益范围（包括技术、个人、开发、工艺技术、业务、运行、组织、政治、经济、法律、法规、生态、社会等方面的影响）。

The motivation for using this term comes from the phrase “separation of concerns” in software and systems engineering, coined by Edsger W. Dijkstra.

使用这一术语的动因来自软件工程和系统工程中的短语“关注点分离”，该短语由 Edsger W. Dijkstra 首创。

Let me try to explain to you, what to my taste is characteristic for all intelligent thinking. It is, that one is willing to study in depth an aspect of one’s subject matter in isolation for the sake of its own consistency, all the time knowing that one is occupying oneself only with one of the aspects. We know that a program must be correct and we can study it from that viewpoint only; we also know that it should be efficient and we can study its efficiency on another day, so to speak. In another mood we may ask ourselves whether, and if so: why, the program is desirable. But nothing is gained—on the contrary!—by tackling these various aspects simultaneously. It is what I sometimes have called “the separation of concerns”, which, even if not perfectly possible, is yet the only available technique for effective ordering of one's thoughts, that I know of. This is what I mean by “focusing one’s attention upon some aspect”: it does not mean ignoring the other aspects, it is just doing justice to the fact that from this aspect’s point of view, the other is irrelevant. It is being one- and multiple-track minded simultaneously[30].

让我试着向诸位说明，依我之见，一切明智的思考所具有的特征是什么。那就是：人们愿意为着某一主题自身的融贯性，孤立地深入研究该主题的某一个方面，同时始终知道自己所涉足的只是其中一个方面。我们知道一个程序必须是正确的，于是可以只从这一视角研究它；我们也知道它应当是高效的，于是可以说，可以改日再研究其效率。换一种心境，我们还可以自问该程序是否可取，若可取，又为何可取。但同时处理这些不同的方面并不能有所收获——恰恰相反！这就是我有时所称的“关注点分离”，即使它并非完全可行，据我所知，它仍是有效梳理思想的唯一可用技术。这就是我所说的“把注意力集中于某个方面”之意：它并不意味着忽略其他方面，而只是承认这样一个事实——从这一方面的观点看，其他方面是无关的。这就是同时做到单轨思维与多轨思维[30]。

As specified in this document, each architecture viewpoint frames one or more concerns (see 6.6) so that a view resulting from the application of that architecture viewpoint addresses identified concerns for the entity of interest. Separating the treatment of concerns by views allows stakeholders to focus on what is of special interest to them and offers a means of organizing and managing complexity of the AD (see 6.7). The literature of enterprise, systems and software engineering records a large inventory of such concerns. Examples are given in 5.2.3.

如本文件所规定，每个架构视角都框定一个或多个关注点（见 6.6），从而使应用该架构视角所得的架构视图能够应对所关注实体的已识别关注点。按架构视图分离对关注点的处理，使利益相关方能够聚焦于其特别关注的内容，并提供了一种组织和管控 AD 复杂性的手段（见 6.7）。企业、系统和软件工程领域的文献记载了大量此类关注点。5.2.3 给出了示例。

### A.4 Aspects and perspectives 方面体与利益相关方角度

#### A.4.1 General 总则

Historically architecting efforts were driven by the concerns of stakeholders. However, the advent of ADFs (and to a much lesser extent ADLs) established practices that drew upon prior architecting experience which resulted in the organizing of architecting efforts which are not necessarily driven by concerns specific to the architecting effort in question but significantly driven by this prior experience. This approach to architecting enabled specific concerns to be identified at a later point in time after first building architecture views using the ADF-driven approach.

历史上，架构工作是由利益相关方的关注点驱动的。然而，ADF（以及程度小得多的 ADL）的出现确立了借鉴以往架构工作经验的实践，由此形成的架构工作组织方式未必由该架构工作特有的关注点驱动，而在很大程度上由此前经验驱动。这种架构工作途径使得：在先用 ADF 驱动的方式构建架构视图之后，能在稍后的时点识别出特定的关注点。

This prior experience is typically encapsulated in grid-based ADFs, typically of two dimensions, but sometimes of three or more dimensions. While there is no uniformity in the established practice as to what the respective rows and columns comprise, it appears there are at least two orthogonal sets which are prevalent.

这种以往经验通常被封装在基于网格的 ADF 中，此类 ADF 通常为二维，但有时为三维或更多维。对于各行和各列分别由什么构成，既有实践并不统一，但看来至少有两个正交的集合是普遍采用的。

One such dimension is the “aspect.” Architects do not necessarily address all aspects simultaneously nor even all possible aspects but tend to address them in a specific order (with iteration as appropriate) dependent upon the architecting objectives, prior experience and any method being applied. Some aspects may not be important for particular architecting efforts (e.g. because they are not relevant to the architecture of interest, or its kind of architecture, or because they are not a driver for that specific architecture).

其中一个维度是“方面体”。架构师未必同时处理所有方面体，甚至未必处理所有可能的方面体，而是倾向于依据架构工作目标、以往经验和所采用的任何方法，按特定顺序处理它们（酌情迭代）。对于特定的架构工作，某些方面体可能并不重要（例如，因为它们与所关注的架构或其架构种类无关，或者因为它们不是该特定架构的驱动因素）。

The other dimension “stakeholder perspective,” is also fundamental and captures what an architect does, namely employing different ways of thinking about an entity or its architecture driven e.g. by concerns, prior experience or method.

另一个维度“利益相关方角度”也是基本的，它体现了架构师所做的工作，即采用由关注点、以往经验或方法等驱动的、关于某一实体或其架构的不同思维方式。

Stakeholder perspective is driven more by architecting thinking and approach. Aspect is driven more by what is or may be needed to be covered in an AD. Concerns form (and are amenable to being addressed through and mapped onto) some combination of one or more aspects and one or more stakeholder perspectives.

利益相关方角度更多地由架构工作的思维和途径驱动。方面体更多地由 AD 中需要或可能需要涵盖的内容驱动。关注点构成一个或多个方面体与一个或多个利益相关方角度的某种组合（并且适宜于通过该组合加以应对并映射到该组合之上）。

The use of aspects and stakeholder perspectives is compatible with a more organized and disciplined (and standardized) approach to both architecting and AD. It is noted that some architectural issues can be direct stakeholder concerns in particular domains or circumstances. In such cases, they are usually addressed through the mechanism of stakeholder perspectives. In other cases, they are not, but instead can be addressed through the mechanism of aspects. This gives rise to variation in the organizing of material employed in commonly used ADFs.

使用方面体和利益相关方角度，与对架构工作和 AD 两者采用更有组织、更有纪律（且标准化）的途径是相容的。已注意到，在特定领域或情形下，某些架构问题可能直接就是利益相关方的关注点。在此类情况下，它们通常通过利益相关方角度的机制加以应对。在其他情况下则并非如此，而是能通过方面体的机制加以应对。这就导致常用 ADF 中所用材料的组织方式出现差异。

#### A.4.2 Aspects 方面体

Aspects provide a way to partition the architecture to enable a more systematic examination of the architecture’s fundamental concepts such as structure and properties, and the evaluation of architecture alternatives. This document uses the term aspect as an organizing basis for views in an architecture description (see 6.5). Aspects, concerns and stakeholder perspectives focus views on cohesive sets of interests within an architecture description. Aspects, concerns and perspectives can provide a basis for capturing many of the relevant architecture considerations with respect to the architecture.

方面体提供了一种划分架构的方式，以便更系统地考察架构的基本概念（如结构和属性），并评估各架构备选方案。本文件使用术语方面体，作为架构描述中各架构视图的组织基础（见 6.5）。方面体、关注点和利益相关方角度将架构视图聚焦于架构描述内内聚的利益集合。方面体、关注点和角度能为记录与架构有关的许多相关架构考量因素提供基础。

The aspects align with technical architecting specialities which access relevant architectural information to be able to analyse, synthesize, assess, elaborate their particular aspect(s) and in turn add to (i.e. develop, embellish, elaborate on, increase confidence in, etc.) the architectural information. Examples of roles with specialities include information architects and analysts, security architects, reliability engineers, human factors specialists, human organization experts, and cost forecasters.

方面体与技术性的架构工作专业领域相一致；这些专业领域获取相关的架构信息，以便能够分析、综合、评定、细化其特定的方面体，进而充实（即开发、润色、细化、增强对……的信心等）架构信息。具备专业领域的角色示例包括信息架构师与分析师、安全架构师、可靠性工程师、人因专家、人力组织专家以及成本预测人员。

> **EXAMPLE 1** Spatial, structural, functional, connectivity, taxonomic, informational and roadmap aspects in an aircraft AD.

> **示例 1**：空间、结构、功能、连通性、分类、信息及路线图方面体在飞机 AD 中的示例。

> **EXAMPLE 2** Behavioural, informational and structural aspects in a computer AD.

> **示例 2**：行为、信息及结构方面体在计算机 AD 中的示例。

> **EXAMPLE 3** Logical connectivity and physical connectivity aspects in a communications network AD (corresponding to the so-called logical network and physical network depictions of a configuration of links and nodes in the network).

> **示例 3**：逻辑连通性与物理连通性方面体在通信网络 AD 中的示例（对应于对网络中链路与节点配置的所谓逻辑网络和物理网络描绘）。

Aspects are neutral with respect to any particular concern although these concerns can be mapped to many relevant aspects. By examining the aspects of an architecture description, certain relevant features or properties of the entity can be discerned or predicted.

方面体对任何特定关注点均保持中性，尽管这些关注点能映射到许多相关的方面体。通过考察架构描述的各个方面体，能辨识或预测该实体的某些相关特征或特性。

Aspects often reflect domain knowledge and come from the experience of engineers and architects. They also come from the ADFs that have found certain aspects to be useful for architecting for the scoped domain for that framework. These aspects are also embedded in methods that are taught to architects and encapsulated in some modelling tools.

方面体往往反映领域知识，来自工程师与架构师的经验。它们也来自各类 ADF，这些 ADF 已发现某些方面体对其所界定领域的架构工作是有用的。这些方面体还嵌入在传授给架构师的方法之中，并封装在某些建模工具之内。

Concerns will apply directly to what is relevant or important with regard to an entity of interest or an architecture whereas an aspect is a part of the character or nature of the architecture entity itself.

关注点直接适用于与所关注实体或架构相关或重要的内容，而方面体则是架构实体自身性质或本性的一部分。

Treating a “stakeholder concern” as the starting point for creating architecture views assumes that one already knows a priori who the stakeholders are and what their concerns may be. In many complex entities, this is not feasible. Some stakeholders are often not known until creation of some architecture views for the aspects considered to be relevant and customary for the domain. When these views are shown to potential stakeholders, then they can likely reveal to us the concerns they may have (if any) for the implied architecture solution.

把“利益相关方关注点”当作创建架构视图的起点，预设了人们已经先验地知道利益相关方是谁、其关注点可能是什么。在许多复杂实体中，这并不可行。有些利益相关方往往要等到针对该领域认为相关且惯用的方面体创建出某些架构视图之后才为人所知。当这些视图展示给潜在利益相关方时，他们便很可能向我们揭示其对所隐含的架构解决方案可能持有的关注点（若有）。

Concerns of the architect as a stakeholder will typically differ from aspects in being not as extensive in scope and less structured in form. Over time and following review and consolidation these concerns can become codified into aspects, usually as they apply to a specific domain of application.

架构师作为利益相关方的关注点，通常与方面体不同：其范围没有那么广，形式上也没有那么结构化。随着时间推移，并经过评审与整合，这些关注点能被编纂为方面体，通常是在它们适用于某一特定应用领域之时。

Aspects can be used to examine the entity to get a more complete understanding of how the architecture addresses that concern. Aspects can likewise aid understanding to what extent the architecture is not addressing that concern.

能使用方面体考察实体，以更完整地理解架构如何应对该关注点。方面体同样能帮助理解架构在多大程度上未应对该关注点。

The relationship between concerns and aspects can be illustrated with these examples: one can analyse, for example, the entity’s behaviour (as an aspect) against several concerns, like: portability, performance; or one can assess a concern such as security through analysis of, for example, behavioural, structural and organizational aspects.

关注点与方面体之间的关系可用以下示例说明：例如，人们能针对若干关注点分析实体的行为（作为一个方面体），如：可移植性，性能；或者，人们能通过分析例如行为、结构及组织方面体来评定诸如安全性这样的关注点。

Aspects are also useful during evaluation of alternative architectures (see ISO/IEC/IEEE 42030).

方面体在评估备选架构时同样有用（见 ISO/IEC/IEEE 42030）。

The concept of aspects has been used in software development to deal with “cross-cutting concerns.” An aspect is a feature of a program shared across by many parts of the program and unrelated to its primary function (Kiczales et al [39]).

方面体的概念已在软件开发中用于处理“横切关注点”。方面体是程序的这样一种特征：它由程序的许多部分共享，且与程序的主要功能无关（Kiczales 等 [39]）。

Non-functional properties such as performance, cost, and quality factors (like reliability, confidentiality and resilience) are concerns that are structured using the notion of aspects (5.2.5). These non-functional properties are often termed “-ilities” or “non-functional requirements (NFRs)”.

诸如性能、成本及质量因素（如可靠性、保密性和韧性）这类非功能特性，是用方面体的概念来结构化的关注点(5.2.5)。这些非功能特性常被称为“-ilities”或“非功能需求（NFR）”。

#### A.4.3 Stakeholder perspectives 利益相关方角度

This document uses the term stakeholder perspective to mean a particular way of thinking about an entity, especially one that is influenced by one’s beliefs or experiences. The way one thinks about an entity (i.e. one’s perspective) can be influenced by organizational role, training, experience, knowledge, personality, character traits, culture, peer pressure, etc. Different ways of thinking about an architecture are often employed when architecting. (See examples in 5.2.4.)

本文件使用术语利益相关方角度，指思考某一实体的特定方式，尤其是受个人信念或经历影响的方式。人们思考实体的方式（即其角度）能受组织角色、培训、经历、知识、个性、性格特质、文化、同伴压力等影响。做架构工作时，往往采用不同的方式思考架构。（见 5.2.4 中的示例。）

> **EXAMPLE** From UAF[48]: strategic, operational, services, personnel, resources, security, projects, standards, actual resources. From ArchiMate[61]: strategy, business, application, technology, physical, implementation, migration. From NAF[44]: concepts, service specifications, logical specifications, resource specifications, architecture metadata. From DODAF[31]: capability, operational, services, systems, standards, data, and information, projects. From ISO 15704 (GERAM): identity, concept, requirements, preliminary design, detailed design, implementation, operation, decommissioning.

> **示例**：来自 UAF[48]：战略、运营、服务、人员、资源、安全、项目、标准、实际资源。来自 ArchiMate[61]：战略、业务、应用、技术、物理、实施、迁移。来自 NAF[44]：概念、服务规格、逻辑规格、资源规格、架构元数据。来自 DODAF[31]：能力、运营、服务、系统、标准、数据与信息、项目。来自 ISO 15704（GERAM）：标识、概念、需求、初步设计、详细设计、实施、运行、退役。

The determination of relevant stakeholder perspectives is dependent upon the interests of, and stances adopted by, the various stakeholders that are relevant to the architecture. For a given stakeholder perspective there are usually multiple concerns and aspects to be considered.

相关利益相关方角度的确定，取决于与架构相关的各利益相关方的利益及其采取的立场。对于给定的利益相关方角度，通常有多个关注点和方面体需要考虑。

#### A.4.4 Structuring formalisms and structural categories 结构化形式体系与结构类别

An ADF can provide a structuring formalism, i.e. a set of rules for using architecture considerations and correspondences between them, to organize the architecture viewpoints used to generate associated views, e.g. a grid framework formalism. The purpose of the structuring formalism is to provide ways of representing relationships among various elements of the architecture and enhancing opportunities for analysis of interactions among those elements.

ADF 能提供一种结构化形式体系，即一组使用架构考量因素及其相互间对应关系的规则，用以组织用于生成关联视图的架构视角，例如网格框架形式体系。结构化形式体系的目的是提供表示架构各元素之间关系的方式，并增强分析这些元素之间交互的机会。

> **EXAMPLE 1** Well known structuring formalisms include: GERAM cube in ISO 15704, Reference Architectural Model Industrie 4.0 (RAMI 4.0)[34], TOGAF stack (business, information systems, technology)[62], NAF grid,[44] UAF grid,[48] and Zachman Framework matrix[67].

> **示例 1**：众所周知的结构化形式体系包括：ISO 15704 中的 GERAM 立方体、工业 4.0 参考架构模型（RAMI 4.0）[34]、TOGAF 栈（业务、信息系统、技术）[62]、NAF 网格[44]、UAF 网格[48] 以及 Zachman 框架矩阵[67]。

In this document, this concept of framework dimensions is called “structural categories” since the way these categories are used in various ADFs is not always aligned with the concept of “dimensions.” So, the structural categories term is used herein since it is a broader and more inclusive concept.

在本文件中，这一框架维度的概念被称为“结构类别”，因为这些类别在各 ADF 中的使用方式并不总是与“维度”的概念一致。因此，本文使用结构类别一词，因为它是一个更宽泛、更具包容性的概念。

An ADF can define structural categories used in the structuring formalism. Sometimes these categories are represented by “dimensions” in a graphic portrayal, such as the rows and columns used in several frameworks. A structuring formalism in grid form usually has two framework dimensions but formalisms can have a single framework dimension, often segmented in a multi-layer hierarchy, or many framework dimensions where visual representation of framework dimensions above three is difficult.

ADF 能定义结构化形式体系中所使用的结构类别。有时这些类别在图形描绘中由“维度”表示，如若干框架中所用的行与列。网格形式的结构化形式体系通常有两个框架维度，但形式体系也能只有一个框架维度（常被分段为多层级的层次结构），或有多个框架维度（此时三个以上的框架维度难以可视化表示）。

> **EXAMPLE 2** A two-dimensional grid is used as a structuring formalism by some ADFs where stakeholder perspectives correspond to rows and aspects correspond to columns.

> **示例 2**：某些 ADF 使用二维网格作为结构化形式体系，其中利益相关方角度对应行，方面体对应列。

The structural categories (i.e. dimensions) of the formalism can include things such as domains, model kinds, perspectives, aspects, interrogatives, levels of abstraction, subjects of concern, aspects of concern, phases, layers, architectural tiers.

该形式体系的结构类别（即维度）能包括诸如下列的内容：领域、模型种类、角度、方面体、疑问词、抽象层级、关注主题、关注方面体、阶段、层、架构层级。

Some commonly used ADFs have a two-dimensional grid or matrix to organize their specifications of architecture viewpoints. The two-dimensional grid originated with Zachman.[67] (Today, many other forms can be found such as cubes, stars, pentagons and ellipses.) These are examples of structuring formalisms used on those frameworks.

一些常用的 ADF 采用二维网格或矩阵来组织其架构视角规格。二维网格发端于 Zachman。[67]（如今还能见到许多其他形式，如立方体、星形、五边形和椭圆形。）这些就是那些框架上所使用的结构化形式体系的示例。

The rows in these grids are the perspectives referred to in this document, although the names of these rows in the frameworks will vary: UAF[48] calls them domains, ArchiMate[61] calls them layers, NAF[44] calls them “subjects of concern”, GERAM in ISO 15704 has two of its three primary dimensions representing extent of abstraction (genericity) and life cycle modelling phase. The underlying idea is the same across these frameworks and this concept has been adopted by this document. The concept also makes explicit that a viewpoint provides a perspective.

这些网格中的行即本文件所称的角度，尽管各框架中这些行的名称各不相同：UAF[48] 称之为领域，ArchiMate[61] 称之为层，NAF[44] 称之为“关注主题”，ISO 15704 中的 GERAM 则以其三个主要维度中的两个分别表示抽象程度（通用性）和生存周期建模阶段。其基本思想在这些框架中是一致的，本文件采纳了这一概念。该概念还明示了架构视角提供角度。

‘Genericity’ is a key conceptual approach from ISO 15704 that applies to an enterprise when modelling the expression of increasingly specific concepts. ISO 15704 defines three levels of genericity: generic, partial and particular. This genericity concept is applicable to other kinds of entities and to the notion of ADFs as well. A progression of increasingly specific (i.e., less generic) ADFs can be used to provide more specificity as one approaches the level of implementation of entities in the real world.

“通用性”是 ISO 15704 中的一个关键概念方法，在对日益具体的概念的表述进行建模时适用于企业。ISO 15704 定义了三个通用性层级：通用的、部分的、特定的。这一通用性概念同样适用于其他种类的实体，也适用于 ADF 的概念。随着逐步接近现实世界中实体的实现层级，可以运用一组日益具体（即通用性更低）的 ADF 来提供更多的具体性。

> **EXAMPLE 3** One possibility is to begin with the generic ICT terminology ADF, such as concepts used in the Zachman Framework, and transition to an ADF with more prototypical domain detail, such as UAF (with a UAF Profile and accompanying SysML notation and semantics), which in turn can transition to an implementation-specific ADF for a particular project using a further modelling profile extension with detail sufficient for the particular domain specific context.

> **示例 3**：一种可能是从通用的 ICT 术语 ADF 入手，如 Zachman 框架中使用的概念，再过渡到具有更多原型性领域细节的 ADF，如 UAF（带有 UAF 概要文件以及随附的 SysML 记法和语义），后者又可过渡到针对特定项目的实现专用 ADF，做法是使用进一步的建模概要扩展，其细节足以应对特定的领域特定语境。

The transitions from generic through partial to particular that provide more domain-specific detail in an ADF are useful due to reasons of quality and efficiency, since any particular project prefers to use an ADF tailored to the application area (such as having predefined perspectives and aspects that are common and reusable in similar projects), has previously been tested (prior success provides expertise and knowledge), and utilizes a terminology shared among experts of the given domain.

为使 ADF 提供更多领域特定的细节，从通用的经部分的到特定的这些过渡出于质量和效率的原因是有用的，因为任何特定项目都倾向于采用针对应用领域裁剪的 ADF（例如具有在类似项目中常见且可复用的预定义视角和方面体）、已被先前检验的 ADF（先前的成功提供专业能力和知识），并使用特定领域专家之间共享的术语。

#### A.4.5 Relationship between aspect and stakeholder perspective 方面体与利益相关方角度之间的关系

Stakeholder perspective and aspect are closely related and often confused. While perspective is the way one thinks about something, aspect can be used for capturing the relevant features of the *entity of* *interest*. An aspect of properties or concepts associated with the entity is perceived when viewing it and thinking about it from a particular perspective. When the perspective is shifted, often the properties or concepts are different. Likewise, when the viewing aspect is changed then different properties or concepts about the entity can be discerned.

利益相关方角度与方面体密切相关，且常常被混淆。角度是人思考某事物的方式，而方面体可用于捕获*所关注* *实体*的相关特征。从特定角度观察并思考实体时，所感知到的是与该实体相关联的属性或概念的一个方面体。当角度发生转移时，属性或概念往往不同。同样，当观察的方面体改变时，能够辨识出该实体不同的属性或概念。

Aspects and stakeholders perspectives are commonly used in the ADF as a way to organize architecture viewpoints as illustrated by the examples described in Annex F (see References [38] [63]). An architecture view can be constructed for a particular aspect and a particular perspective. The perspective can represent an aggregation of concerns held by one or more stakeholders. When an architecture framework matrix or grid uses these concepts, the columns usually represent aspect-related items and the rows usually represent perspective-related items.

在 ADF 中，方面体和利益相关方角度通常用作组织架构视角的一种方式，如附录 F 中描述的示例所示（见参考文献 [38] [63]）。可以为特定方面体和特定角度构造一个架构视图。角度能表示由一个或多个利益相关方持有的关注点的聚合。当架构框架矩阵或网格使用这些概念时，列通常表示与方面体相关的项，行通常表示与角度相关的项。

#### A.4.6 Complementary ADF approaches 互补的 ADF 途径

The combination of stakeholder perspectives and aspects to conduct architecting in a manner informed by prior experience can serve as a different and complementary approach to architecting driven by identified stakeholders and their specific concerns (see 5.2.3). For example, using prior experience in conducting the architecting of a similar entity situated in a similar environment, potential issues can be identified which when raised with stakeholders give rise to real concerns.

将利益相关方角度与方面体结合起来，以借鉴先前经验的方式开展架构工作，可作为由已识别的利益相关方及其特定关注点驱动的架构工作的一种不同的、互补的途径（见 5.2.3）。例如，利用在类似环境中对类似实体开展架构工作的先前经验，能够识别出潜在问题，这些问题在向利益相关方提出时会产生真实的关注点。

Using established aspects from known stakeholder perspectives can be enormously helpful in reducing architecting effort to arrive at suitable architecture viewpoints. However, architects need to exercise care not to let these aspects and stakeholder perspectives of prior architecting effort overshadow concerns not previously expressed nor to discount emerging concerns as the architecting project unfolds.

使用由已知利益相关方角度确立的方面体，对于减少获得合适架构视角所需的架构工作量极为有益。然而，架构师需要谨慎，不要让先前架构工作的这些方面体和利益相关方角度遮蔽了先前未表达的关注点，也不要在架构项目展开过程中忽视新出现的关注点。

The roles fulfilled by aspects and stakeholder perspectives are different. For a given perspective there are usually multiple aspects to be considered. When the stakeholder perspective is changed, then the properties or concepts that are perceived are different.

方面体与利益相关方角度所承担的角色是不同的。对于给定的角度，通常有多个方面体需要考虑。当利益相关方角度改变时，所感知到的属性或概念也随之不同。

### A.5 Architecture views and viewpoints 架构视图与架构视角

The terms architecture view and architecture viewpoint are central to this document. Although sometimes used synonymously, in this document they refer to separate and distinct concepts.

术语架构视图和架构视角是本文件的核心。尽管有时被同义使用，但在本文件中它们指相互独立且不同的概念。

It is a goal of this document to encompass existing AD practices by providing common terminology and concepts. Many existing practices express architectures through collections of models. Typically, these models are further organized into cohesive groups, called views. The cohesion of a group of models or other information is determined by the perspective taken and the concerns and aspects addressed by that group of models and other information sources. In this document, a specification of an architecture viewpoint refers to the conventions for expressing an architecture with respect to a given perspective, set of concerns and aspects:

本文件的目标之一是通过提供通用的术语和概念来涵盖现有的 AD 实践。许多现有实践通过模型集合来表达架构。通常，这些模型被进一步组织成内聚的分组，称为架构视图。一组模型或其他信息的内聚性，取决于所采取的角度以及该组模型和其他信息源所处理的关注点和方面体。在本文件中，架构视角规格指针对给定角度、关注点集和方面体表达架构的约定：

*A view is a* way *of expressing the architecture of an entity of interest from a particular viewpoint.\*

*架构视图是*一种*从特定架构视角表达所关注实体架构的*方式。\*

The use of multiple views to express an architecture is a fundamental premise of this document. The need for multiple views in ADs is widely recognized. While the use of multiple views is widespread, authors differ on what views are needed, based on audience, and on appropriate methods for expressing each view. Because of the wide range of opinion, this document does not require a predefined set of architecture viewpoints and their specifications; it encourages the practice of defining or selecting architecture viewpoints appropriate to the entity of interest.

使用多个架构视图来表达架构是本文件的一项基本前提。AD 中对多个架构视图的需求已得到广泛认可。尽管多个架构视图的使用十分普遍，但作者们在需要哪些架构视图（取决于受众）以及表达每个架构视图的适宜方法上存在分歧。由于意见差异很大，本文件不要求一组预定义的架构视角及其规格；它鼓励定义或选择适合于所关注实体的架构视角这一做法。

A consequence of making architecture viewpoints first-class entities is that they are among the constructs considered as AD elements.

将架构视角作为一等实体的一个结果是，它们属于被视为 AD 元素的构造。

The remainder of this subclause provides brief historical notes on the use and evolution of the term “viewpoint” in systems and software.

本子条款的其余部分简要介绍术语“视角”在系统与软件中的使用和演变的历史。

The earliest use of first-class viewpoints appears in Ross’ Structured Analysis (SADT) in 1977.[53] In requirements engineering, Nuseibeh, Kramer and Finkelstein treat viewpoints as first-class entities, with associated attributes and operations[43]. These works inspired the formulation of architecture viewpoints as specified in Clause 8. The term is chosen to align with the ISO Reference Model of Open Distributed Processing (RM-ODP),[2] which uses the term in these ways:

一等视角的最早使用出现在 1977 年 Ross 的结构化分析（SADT）中。[53] 在需求工程中，Nuseibeh、Kramer 和 Finkelstein 将视角视为一等实体，并带有相关联的属性和操作[43]。这些工作启发了第 8 章所规定的架构视角的制定。选择该术语是为了与 ISO 开放分布式处理参考模型（RM-ODP）[2]保持一致，该模型以下列方式使用该术语：

A viewpoint (on a system) is an abstraction that yields a specification of the whole system related to a particular set of concerns. (see ISO/IEC 10746-1:1998, 6.2.2.)

（关于系统的）视角是一种抽象，它产生与特定关注点集相关的整个系统的规格。（见 ISO/IEC 10746-1:1998, 6.2.2.）

A viewpoint (on a system) is a form of abstraction achieved using a selected set of architectural constructs and structuring rules, in order to focus on particular concerns within a system. (see ISO/IEC 10746-2:2009, 3.2.7.)

（关于系统的）视角是一种抽象形式，它通过使用一组选定的架构构造和结构化规则来实现，以便聚焦于系统内的特定关注点。（见 ISO/IEC 10746-2:2009, 3.2.7.）

However, where this document uses “architecture view” to refer to the application of a viewpoint to a particular entity, RM-ODP[2] uses the term “viewpoint specification”.

然而，本文件使用“架构视图”指将视角应用于特定实体，而 RM-ODP[2]使用术语“视角规格”。

A specification of an architecture viewpoint contains the conventions (such as notations, languages and types of models) for constructing a certain kind of view. An architecture viewpoint offers a way of looking at an entity’s architecture and provides the architect with resources for modelling an entity with respect to the concerns framed by that viewpoint. That viewpoint can be applied to many entities. Each view is one such application.

架构视角规格包含用于构造某一类视图的约定（如记法、语言和模型种类）。架构视角提供一种审视实体架构的方式，并为架构师提供资源，以便针对该视角所框定的关注点对实体建模。该视角可应用于许多实体。每个架构视图就是这样的一种应用。

Every architecture view must have a specification of an architecture viewpoint specifying the conventions for interpreting the contents of the view. In this document, legends are introduced to document the conventions of view components.

每个架构视图都必须有一份架构视角规格，规定用于解释该架构视图内容的约定。本文件中引入图例，以记录视图组件的约定。

Within an individual AD, this document requires that each view needs to be governed by an architecture viewpoint. This means that each view conforms to one set of conventions (possibly including one or more specifications of model kinds, possibly presented in more than one way for diverse stakeholders). In situations where there is a need to use two or more viewpoints to produce a view, a single viewpoint can be developed by composing the two or more viewpoints which can then be used to produce the view. Alternatively, usage of multiple viewpoints can be simply documented in the view.

在单个架构描述内，本文件要求每个架构视图都需受一个架构视角管控。这意味着每个架构视图符合一组约定（可能包括一个或多个模型种类规格，可能为不同的利益相关方以不止一种方式呈现）。在需要使用两个或更多架构视角来生成一个架构视图的情形下，可通过组合这两个或更多架构视角来开发单个架构视角，然后再用该架构视角生成该架构视图。或者，也可直接在架构视图中记录对多个架构视角的使用。

In situations where there is a need to consider the whole entity of interest for the development of a view; but the boundary of the entity is not known then, parts of the entity can become the focus from the perspective of the concerns framed and aspects revealed by the governing architecture viewpoint. For example, to develop a performance view of a networked entity, both network transmission delays and processing times can be considered to produce a complete end-to-end view of the performance of the entire entity of interest, but somethings like size, weight, power consumption, bandwidth and throughput need not be considered.

在需要考虑整个所关注实体以开发一个架构视图、但该实体的边界尚不已知的情形下，从管控架构视角所框定的关注点和所揭示的方面体这一角度来看，该实体的各部分能成为焦点。例如，为开发一个网络化实体的性能视图，能同时考虑网络传输时延和处理时间，以生成整个所关注实体性能的完整端到端视图，而尺寸、重量、功耗、带宽和吞吐量之类则无需考虑。

An AD can focus on the entity of interest at a specific point of time (for example, when it is delivered to a customer), or consider the evolution of the architecture over several time scales. Any view can be constructed from a series of view components, each representing the entity of interest at a given point of time, stage or phase. The composition of such view components within a view would describe how that entity evolves over time, while still allowing the view to deal with the whole entity of interest.

架构描述能聚焦于特定时间点（例如交付给客户时）的所关注实体，或考虑架构在若干时间尺度上的演化。任何架构视图都能由一系列视图组件构造而成，每个视图组件表示给定时间点、阶段或时期的所关注实体。此类视图组件在一个架构视图内的组合将描述该实体如何随时间演化，同时仍允许该架构视图处理整个所关注实体。

There are two common approaches to the construction of views: the synthetic approach[55] and the projective approach.[25] In the synthetic approach, the architect constructs views of the entity of interest and integrates these views within an AD, using correspondences. In the projective approach, an architect derives each view through some routine, possibly mechanical, procedure of extraction from an underlying information source or set of models. This document is designed to be usable with either of these approaches to views.

架构视图的构建有两种常见途径：综合途径[55]和投影途径[25]。在综合途径中，架构师构造所关注实体的架构视图，并使用对应关系将这些架构视图集成在一个架构描述内。在投影途径中，架构师通过某种例行的、可能是机械化的过程，从底层信息源或模型集中提取出每个架构视图。本文件设计为能用于这两种架构视图途径中的任一种。

Annex B and Annex C provide further information and references pertaining to specification of architecture viewpoints.

附录B和附录C提供了与架构视角规格有关的进一步信息和引用文件。

### A.6 Correspondences 对应关系

Correspondences are used to identify or express named relations within and between AD elements.

对应关系用于标识或表达架构描述元素内部及之间的命名关系。

Although many model kinds and ADLs include constructs to capture relations (such as relationships in entity-relation-attribute diagrams, associations in UML), when an AD utilizes multiple viewpoints and model kinds, there may not be any available way to identify and express named relations between these diverse representations. In such cases, correspondences can be used to identify and express these named relations.

尽管许多模型种类和架构描述语言都包含捕获关系的构造（例如实体-关系-属性图中的关系、UML中的关联），但当一份架构描述使用多个架构视角和模型种类时，可能没有任何可用的方式来标识和表达这些不同表示之间的命名关系。在此类情形下，能使用对应关系来标识和表达这些命名关系。

The 2011 edition of this document introduced correspondences and correspondence rules to express and enforce relations between AD elements. In this document, AD element is an identified or named part of an architecture description. AD elements include stakeholders, concerns, stakeholder perspectives, and aspects identified in an AD, and views, view components, viewpoints, and model kinds included in an AD.

本文件2011版引入了对应关系和对应规则，以表达和实施架构描述元素之间的关系。在本文件中，架构描述元素是架构描述中已标识或已命名的部分。架构描述元素包括架构描述中标识的利益相关方、关注点、利益相关方角度和方面体，以及架构描述中包含的架构视图、视图组件、架构视角和模型种类。

In addition, AD elements include ADs themselves and instances of the constructs introduced by viewpoints and model kinds. Any of these AD elements can participate in relations expressed by correspondences. Correspondences have a number of uses. They can be used to express consistency, traceability, composition, refinement and model transformation, and dependences of any type within and between ADs.

此外，架构描述元素还包括架构描述本身，以及由架构视角和模型种类引入的构造的实例。这些架构描述元素中的任何一个都能参与由对应关系表达的关系。对应关系有多种用途。它们能用于表达架构描述内部及之间的一致性、可追溯性、组合、细化和模型变换，以及任何类型的依赖关系。

A survey of uses of model relations together with a taxonomy and classification of relation mechanisms is found in Reference [26]. Correspondences can be used to meet the requirements of 6.9.1 for recording view consistencies and inconsistencies.

参考文献[26]中给出了模型关系用途的调查以及关系机制的分类法和类别划分。对应关系能用于满足6.9.1中关于记录架构视图一致性和不一致性的要求。

In this edition, correspondence rules are generalized to correspondence methods. Correspondence methods capture intended relationships that are to be enforced on correspondences within and between AD elements.

在本版中，对应规则被推广为对应方法。对应方法捕获要在架构描述元素内部及之间的对应关系上强制实施的预期关系。

The remainder of this subclause presents examples of correspondences and correspondence methods. The features of the correspondence mechanism, in relation to similar mechanisms in the literature, are discussed.

本子条款的其余部分给出对应关系和对应方法的示例。还讨论了对应机制的特征与文献中类似机制的关系。

> **EXAMPLE 1** Consider two view components in an automotive system’s AD: a software application view component and an electronic control unit (ECU) view component. The software application view component includes these elements: Autopilot, Dashboard (consisting of Controls, Instrument panel cluster, Center stack), Braking, GPS, LIDAR and Sensor Fusion. The ECU view component identifies a number of ECUs, numbered 1 through 4. A correspondence, depicting the assignment of applications to ECUs, is shown in Figure A.2 as a matrix. The form of a correspondence is not specified by this document.

> **示例 1**：考虑汽车系统的架构描述中的两个视图组件：一个软件应用视图组件和一个电子控制单元（ECU）视图组件。软件应用视图组件包括下列元素：Autopilot、Dashboard（由Controls、Instrument panel cluster、Center stack组成）、Braking、GPS、LIDAR和Sensor Fusion。ECU视图组件标识了若干ECU，编号为1到4。图A.2以矩阵形式示出描绘应用到ECU分配的一个对应关系。对应关系的形式不由本文件规定。

![Figure A.2 — Example of a correspondence](ISO_IEC_IEEE 42010 2023.assets/fig-08.png)

**Figure A.2 — Example of a correspondence**

**图A.2 — 对应关系示例**

The example meets the requirement of 6.9.2: it has a unique name (“bundled on”), identifies participating elements (the applications and ECU), and identifies an optional correspondence method (M1).

该示例满足6.9.2的要求：它具有唯一的名称（“bundled on”）、标识参与元素（各应用和ECU），并标识一个可选的对应方法（M1）。

A correspondence method expresses a constraint to be enforced on correspondences. EXAMPLE 2 presents a simple correspondence method.

对应方法表达要在对应关系上强制实施的约束。示例2给出一个简单的对应方法。

> **EXAMPLE 2** M1: every application must be bundled onto at least one ECU.

> **示例 2**：M1：每个应用都必须捆绑到至少一个ECU上。

The correspondence named “bundled on” in EXAMPLE 1 satisfies M1 because all applications are assigned to at least one ECU.

示例1中名为“bundled on”的对应关系满足M1，因为所有应用都分配到至少一个ECU。

Most correspondences will be expressed in terms of elements of views or view components, but this is not required. EXAMPLES 3 and 4 show other forms of correspondences.

大多数对应关系将按架构视图或视图组件的元素来表达，但并非必须如此。示例3和示例4示出其他形式的对应关系。

> **EXAMPLE 3** Tasks Interactions: For every instance of the model kind, Tasks needs to have a refinement to an instance of model kind Interactions.

> **示例 3**：Tasks Interactions：对于该模型种类的每个实例，Tasks都需要有一个到Interactions模型种类实例的细化。

This correspondence method can be satisfied by the correspondence shown in Figure A.3 where there are Users, Operators and Auditors. Each task instance (view component depicted as a triangle) is refined into an interaction instance (view component depicted with a pentagon). Alternatively, this can be recorded as a matrix, as in EXAMPLE 1.

该对应方法能由图A.3所示的对应关系满足，其中有Users、Operators和Auditors。每个任务实例（以三角形描绘的视图组件）都细化为一个交互实例（以五边形描绘的视图组件）。或者，也可如示例1那样将其记录为矩阵。

In EXAMPLE 3 the participants in the correspondence are not elements within view components, but view components themselves. A correspondence can relate any AD elements (see 5.2.11 and 6.9.2); users of this document are free to introduce other types of AD elements suited to their purposes.

在示例3中，对应关系的参与者不是视图组件内的元素，而是视图组件本身。对应关系能关联任何架构描述元素（见5.2.11和6.9.2）；本文件的使用者可自由引入适合其目的的其他类型的架构描述元素。

Many correspondences will be binary, but this is not required. A correspondence can relate an arbitrary number of AD elements. EXAMPLE 4 illustrates an *n*-ary correspondence method.

许多对应关系将是二元的，但并非必须如此。一个对应关系能关联任意数量的架构描述元素。示例4说明一个*n*元对应方法。

> **EXAMPLE 4** View Versioning: The version identifier of each view needs to be greater than 1.5 prior to publication of this AD.

> **示例 4**：View Versioning：在本架构描述发布之前，每个架构视图的版本标识符都需要大于1.5。

![Figure A.3 — Example of a correspondence satisfying the Task-Interactions method](ISO_IEC_IEEE 42010 2023.assets/fig-09.png)

**Figure A.3 — Example of a correspondence satisfying the Task-Interactions method**

**图 A.3 — 满足 Task-Interactions 方法的对应关系示例**

The term “correspondence” is chosen to align with RM-ODP. The correspondence mechanism is designed to be compatible with view correspondences in RM-ODP[2] however, there are some differences. Notable differences are:

选用“对应关系”这一术语，是为了与 RM-ODP 保持一致。对应关系机制的设计与 RM-ODP[2] 中的视图对应关系兼容，但存在一些差异。显著的差异如下：

a) The term “correspondence” is used in this document rather than “view correspondence”. In RM-

a) 本文件使用“对应关系”而非“视图对应关系”。在 RM-

ODP, each view is homogeneous—a single viewpoint language is used per viewpoint specification. In RM-ODP a viewpoint specification is what is referred to in this document as an architecture view (see A.5).

ODP 中，每个视图都是同质的——每个视角规格使用单一视角语言。在 RM-ODP 中，视角规格即本文件所称的架构视图（见 A.5）。

b) This document permits heterogeneous views: each view consists of one or more view components wherein each can utilize a different modelling convention (see 6.8). It is useful to be able to state a correspondence between view components in different modelling languages, not just between views. Therefore, “view correspondence” is a special case of what is needed in this document, and that term is somewhat misleading in this more general case;

b) 本文件允许异质视图：每个视图由一个或多个视图组件构成，其中每个视图组件能采用不同的建模约定（见 6.8）。能够陈述不同建模语言中的视图组件之间的对应关系，而不仅是视图之间的对应关系，是有用的。因此，“视图对应关系”只是本文件所需内容的一个特例，在这一更一般的情形下，该术语有些误导；

c) RM-ODP view correspondences express binary relations where correspondences in this document express *n*-ary relations;

c) RM-ODP 视图对应关系表达二元关系，而本文件中的对应关系表达 *n* 元关系；

d) RM-ODP view correspondences are defined on elements of view specifications whereas correspondences in this document do not need to refer to individual elements of models, but arbitrary AD elements;

d) RM-ODP 视图对应关系定义在视角规格的元素上，而本文件中的对应关系无需引用模型的单个元素，而可引用任意的 AD 元素；

e) Correspondences and correspondence methods can be used to identify and express named relations across ADs.

e) 对应关系和对应方法能用于识别和表达具名关系，且可跨 AD。

Mathematically, a correspondence is an *n*-ary relation. A correspondence method is an intentional definition of an *n*-ary relation. Relations include 1-1 mappings (isomorphisms) and functions as special cases, both of which are too restrictive for many applications of correspondences. Relations have useful properties which permit composition, reasoning and allow efficient representation and manipulation (see Reference [42] and references therein).

在数学上，对应关系是一种 *n* 元关系。对应方法是 *n* 元关系的一种意向性定义。关系将 1-1 映射（同构）和函数作为特例包含在内，而二者对对应关系的许多应用而言都过于受限。关系具有有用的性质，能支持复合与推理，并允许高效的表示和操作（见参考文献 [42] 及其中的参考文献）。

### A.7 Perspectives on architecture description languages 对架构描述语言的若干视角

The term architecture description language (ADL) has been in use since the 1990s in the software, systems and enterprise architecture communities. Within the conceptual model of this document, an ADL is any language for use in describing an architecture.

架构描述语言（ADL）这一术语自 20 世纪 90 年代以来一直在软件、系统和企业架构界使用。在本文件的概念模型中，ADL 是用于描述架构的任何语言。

Early ADLs included Rapide (Stanford),[41] Wright (CMU)[65], and Darwin[37] (Imperial College) . ADLs focused on structural concerns: large-scale system organization expressed in terms of components, connectors and configurations with varying support for framing behavioural concerns. More recently, “wide-spectrum” ADLs have been developed which support a wider range of concerns. These include Architecture Analysis and Description Language (AADL)[57], SysML,[47] and ArchiMate.[61] EXAMPLEs 1 to 3 describe some contemporary ADLs with reference to their relationship to the conceptual model defined in this document.

早期 ADL 包括 Rapide（斯坦福大学）[41]、Wright（CMU）[65] 和 Darwin[37]（帝国理工学院）。ADL 聚焦于结构类关注点：以组件、连接件和配置表达的大规模系统组织，对框定行为类关注点的支撑程度不一。较晚近以来，已开发出支持更广泛关注点的“宽谱”ADL，包括架构分析与描述语言（AADL）[57]、SysML[47] 和 ArchiMate[61]。示例 1 至 3 结合本文件所定义的概念模型，描述了若干当代 ADL 及其与该模型的关系。

Within the conceptual model of this document, an ADL is any language for use in describing an architecture. An ADL can be used for a single model kind (e.g. Darwin[37]), multiple model kinds (e.g. UML, Rapide, AADL), a single viewpoint (e.g. ACME[33]), or multiple viewpoints (e.g. ArchiMate, SysML). Therefore, an ADL can be used by one or more specifications of architecture viewpoints to frame identified concerns within an AD.

在本文件的概念模型中，ADL 是用于描述架构的任何语言。一个 ADL 能用于单一模型种类（如 Darwin[37]）、多个模型种类（如 UML、Rapide、AADL）、单一视角（如 ACME[33]）或多个视角（如 ArchiMate、SysML）。因此，一个 ADL 能由一个或多个架构视角规格使用，以在 AD 中框定已识别的关注点。

> **EXAMPLE 1** ArchiMate[61] organizes ADs into several layers of concerns: Business, Application and Technology (or Infrastructure), specifies several aspects of concerns within each of those layers: Structural, Behavioural and Informational aspects, and defines a number of basic architecture viewpoints for these. Each architecture viewpoint is defined via its own metamodel, relating that architecture viewpoint to others, and specifying the stakeholders, concerns, purpose, layers and aspects.

> **示例 1**：ArchiMate[61] 将 AD 组织为若干关注点层：业务、应用和技术（或基础设施），规定每一层内关注点的若干方面体：结构方面体、行为方面体和信息方面体，并为这些层定义若干基本架构视角。每个架构视角通过其自身的元模型定义，将该架构视角与其他架构视角相关联，并规定利益相关方、关注点、目的、层和方面体。

> **EXAMPLE 2** The Systems Modelling Language (SysML[47]) is built upon UML. SysML defines several types of diagrams: Activity, Sequence, State Machine, Use Case, Block Definition, Internal Block, Package, Parametric, and Requirement diagrams. In the terms of this document, each SysML diagram type provides a different type of view. SysML provides first-class constructs for Stakeholders, Concerns, Views and Architecture Viewpoint so that users can create new model kind in accordance with this document.

> **示例 2**：系统建模语言（SysML[47]）构建在 UML 之上。SysML 定义若干类图：活动图、序列图、状态机图、用例图、块定义图、内部块图、包图、参数图和需求图。按本文件的术语，每一类 SysML 图提供一种不同类型的视图。SysML 为利益相关方、关注点、视图和架构视角提供一等构造，使用户能按照本文件创建新的模型种类。

> **EXAMPLE 3** The Unified Architecture Framework Profile (UAFP[48]) is a modelling language focused on representation of the enterprise and includes language extensions to UML/SysML that allow the extraction of specified and custom models from an integrated AD. The models describe the enterprise (and associated “resources”) from a set of stakeholders’ concerns through a set of predefined architecture viewpoints, specifications of views and associated views Given that in architecture practice multiple models would be created separately from a number of specifications of architecture viewpoints and in multiple versions, to be able to maintain cross-model consistency the UAFP allows the definition of constraints to express this. UAFP is defined as a UML 2 / SysML v1.6 profile, corresponding to the actual domain concepts (UAF concepts and relationships) separately defined in the UAF Domain Meta Model (DMM).[48] This separation allows UAF to be used in conjunction with more than one ADF (such as DoDAF[31] or NAF,[44] for example).

> **示例 3**：统一架构框架概要（UAFP[48]）是一种专注于企业表示的建模语言，包含对 UML/SysML 的语言扩展，允许从集成的 AD 中提取规定模型和定制模型。这些模型通过一组预定义的架构视角、视图规格和相关视图，从一组利益相关方关注点出发描述企业（及关联的“资源”）。鉴于在架构实践中，会依据若干架构视角规格以多个版本分别创建多个模型，为能保持跨模型一致性，UAFP 允许定义约束来表达这一点。UAFP 定义为 UML 2 / SysML v1.6 概要，与在 UAF 领域元模型（DMM）中单独定义的实际领域概念（UAF 概念与关系）相对应。[48] 这种分离使 UAF 能与不止一个 ADF（例如 DoDAF[31] 或 NAF[44]）结合使用。

An ADL frames a particular set of concerns for an audience of stakeholders, by defining one or more model kinds together with any other methods or tools. Similar to an ADF or an architecture viewpoint, an ADL is a reusable resource—it is not limited in use to an individual entity or AD.

ADL 通过定义一个或多个模型种类以及任何其他方法或工具，为一类利益相关方受众框定一组特定的关注点。与 ADF 或架构视角类似，ADL 是一种可复用的资源——其使用不限于单个实体或 AD。

## Annex B (informative) — Guidelines to specification of architecture viewpoints ｜ 附录 B（资料性）— 架构视角规格指南

### B.1 General 总则

This annex provides a template for preparing specifications of architecture viewpoints and annotated guidelines to a sample of currently available specifications of architecture viewpoints.

本附录提供用于编制架构视角规格的模板，以及针对现行若干架构视角规格样例的带注释指南。

### B.2 Template for documenting specification of architecture viewpoints 用于记录架构视角规格的模板

#### B.2.1 Template overview 模板概述

A template for the specification of architecture viewpoints is presented. An architecture viewpoint that is documented in this form meets the requirements of 8.1.

给出了架构视角规格的模板。以这种形式记录的架构视角满足 8.1 的要求。

The template identifies the contents of a specification of an architecture viewpoint. Each element of the content includes its name (B.2.X), and a brief description of its intended content, and guidance for developing that content. In some cases, additional contents are nested within top-level description contents of the specification.

该模板标识架构视角规格的内容。每一内容元素包括其名称（B.2.X）、对其预期内容的简要说明，以及编制该内容的指南。在某些情况下，附加内容嵌套在该规格的顶层描述内容之中。

#### B.2.2 Architecture viewpoint name 架构视角名称

The name for the architecture viewpoint. If there are synonyms or other common names by which the architecture viewpoint is known, in addition to the name of the architecture viewpoint, other common names can be identified.

架构视角的名称。如果除架构视角的名称外，该架构视角还有同义词或其他常用名称，则可标识这些其他常用名称。

#### B.2.3 Architecture viewpoint overview 架构视角概述

An abstract or brief overview of the architecture viewpoint and the related architecture viewpoint features.

架构视角及相关架构视角特性的摘要或简要概述。

#### B.2.4 Concerns 关注点

A listing of the architecture-related concerns to be framed by this architecture viewpoint per 8.1 item b). This helps decide whether the related architecture viewpoint will be useful for modelling a particular entity of interest.

按 8.1 中 b) 项，列出将由该架构视角框定的架构相关关注点。这有助于判定相关架构视角对于建模特定的所关注实体是否有用。

A listing of the kinds of issues an architecture viewpoint is not appropriate for to avoid misuse. This can be a good antidote for certain overly used viewpoints and model kinds.

列出该架构视角不适用的问题种类，以避免误用。对于某些被过度使用的架构视角和模型种类，这可能是一剂良方。

#### B.2.5 Stakeholder perspectives 利益相关方角度

A listing of any stakeholder perspectives associated with this architecture viewpoint [per 8.1 item b)].

列出与该架构视角相关联的任何利益相关方角度[按 8.1 中 b) 项]。

#### B.2.6 Aspects 方面体

A listing of the aspects refining the above concerns [per 8.1 item c)] or encompassing potential concerns.

列出细化上述关注点或涵盖潜在关注点的方面体[按 8.1 中 c) 项]。

> **NOTE** The identification of concerns, stakeholder perspectives and aspects are intended to assist architects and other stakeholders in determining the utility of this viewpoint for their entity of interest.

> **注**：识别关注点、利益相关方角度和方面体，旨在帮助架构师和其他利益相关方判定该视角对其所关注实体是否有用。

#### B.2.7 Typical stakeholders 典型利益相关方

A listing of the stakeholders expected to be users or audiences for views prepared using this architecture viewpoint [per 8.1 item d)].

列出预期成为使用该架构视角所编制架构视图的用户或受众的利益相关方[按 8.1 中 d) 项]。

> **NOTE** When an architecture viewpoint is selected for use and applied in an AD, it is useful to document the association of actual stakeholders with concerns framed by this viewpoint and related specification (per 6.4).

> **注**：当选用某一架构视角并在 AD 中应用时，记录实际利益相关方与该视角及相关规格所框定的关注点之间的关联是有用的（按 6.4）。

#### B.2.8 Correspondence methods 对应方法

A listing of any correspondence methods defined by this viewpoint or its model kinds (per 8.1, 8.2 and 6.9.3).

列出由该视角或其模型种类所定义的任何对应方法（按 8.1、8.2 和 6.9.3）。

These methods can be applied across view components, across views within an AD or across ADs.

这些方法能跨视图组件、跨一个 AD 内的各架构视图或跨各 AD 应用。

#### B.2.9 Specification of model kinds 模型种类规格

##### B.2.9.1 General 总则

The architecture viewpoint identifies each model kind [per 8.1 item e)].

该架构视角标识每一模型种类[按 8.1 中 e) 项]。

For each model kind used, describe its conventions, language or modelling techniques. These are key modelling resources which the specification of the architecture viewpoint makes available that establish the vocabularies for constructing the architecture views.

对所采用的每一模型种类，描述其约定、语言或建模技术。这些是架构视角规格所提供的关键建模资源，确立了构建各架构视图所用的词汇。

This document does not require one style for documenting specifications of model kinds. A specification of a model kind can be documented in various ways, including:

本文件不要求以单一风格记录模型种类规格。模型种类规格能以多种方式记录，包括：

a) by specifying a metamodel that defines its core constructs and relationships;

a) 规定一个元模型，以定义其核心构造和关系；

b) by providing a template to be filled in by users;

b) 提供由用户填写的模板；

c) via a language definition, modelling profile or by reference to an existing modelling language;

c) 通过语言定义、建模概要，或援引现有的建模语言；

d) by some combination of these, or other means.

d) 通过上述方式的某种组合，或其他手段。

Guidance on methods a) to c) is provided in B.2.9.2 to B.2.9.4.

关于 a) 至 c) 各方法的指南见 B.2.9.2 至 B.2.9.4。

##### B.2.9.2 Metamodel related to the specification of a model kind 与模型种类规格相关的元模型

A metamodel presents one or more constructs which are the AD elements that comprise the vocabulary of the model kind and its specification. There are various ways of representing metamodels. The metamodel will present:

元模型给出一个或多个构造，这些构造是构成该模型种类及其规格词汇表的 AD 元素。元模型有多种表示方式。元模型将给出：

- entities: What are the major sorts of elements that are present in models of this kind?

- 实体：本类模型中存在哪些主要种类的元素？

- attributes: What properties do entities possess in models of this kind?

- 属性：在本类模型中，实体具有哪些性质？

- relationships: What relations are defined among entities in models of this kind?

- 关系：在本类模型中，实体之间定义了哪些关系？

- constraints: What kinds of constraints are there on entities, attributes and/or relationships in

- 约束：对本类模型中的实体、属性和／或关系存在哪些种类的

models of this kind?

约束？

Within an AD, instances of entities, attributes, relationships and constraints are AD elements in the sense of 5.2.9.

在一个 AD 内，实体、属性、关系和约束的实例都是 5.2.9 意义上的 AD 元素。

> **NOTE** When specification of an architecture viewpoint specifies multiple model kinds it can be useful to specify a single architecture viewpoint related metamodel unifying the definition of the model kinds. Furthermore, it is often helpful to use a unified metamodel to express a set of related architecture viewpoints (such as when defining an ADF or ADL).

> **注**：当架构视角规格规定多个模型种类时，规定一个统一的、与架构视角相关的元模型来统一各模型种类的定义，可能是有用的。此外，使用统一的元模型来表达一组相关架构视角（例如定义 ADF 或 ADL 时）往往也是有帮助的。

##### B.2.9.3 Templates of specifications of model kinds 模型种类规格的模板

Provide a template or form specifying the format or expected content of view components governed by this model kind specification.

提供规定受该模型种类规格管控的视图组件的格式或预期内容的模板或表单。

Each such template, form, or their parts, can have a legend to be used when this model kind is used within an AD.

每一这样的模板、表单或其各部分，都能带有在该模型种类用于 AD 内时所使用的图例。

##### B.2.9.4 Language related to the specification of a model kind 与模型种类规格相关的语言

Identify an existing notation or modelling language or define one that can be used when applying this model kind in an AD. Describe its syntax, semantics, and tool support, as needed.

标识现有的记法或建模语言，或定义一种在 AD 中应用该模型种类时能使用的记法或建模语言。按需描述其语法、语义和工具支持。

#### B.2.10 View methods 视图方法

Define methods available on views. (see 5.2.10 and 8.3).

定义可用于架构视图的方法（见 5.2.10 和 8.3）。

#### B.2.11 Examples 示例

This subclause provides examples for users.

本条为用户提供示例。

#### B.2.12 Notes 注

Any additional information that users of this specification may need or find helpful.

该规格的使用者可能需要或认为有帮助的任何附加信息。

#### B.2.13 Sources 来源

Identify the sources for this specification, if any, including author, history, literature references and prior art [per 8.1 item g)].

标识该规格的来源（如有），包括作者、沿革、文献引用和现有技术[按 8.1 中 g) 项]。

### B.3 Resources for specifications of architecture viewpoints 架构视角规格的资源

The following represent some resources for well-documented specifications of architecture viewpoints. Not all of these are documented in accordance with the requirements of this document but can be used in an AD or included in an ADF specification in a conforming manner.

以下列举若干可作为文档完备的架构视角规格的资源。这些资源并非全部按本文件的要求记录，但能以符合本文件的方式用于 AD，或纳入 ADF 规格。

- Callo-Arias, America, and Avgeriou, “Defining execution viewpoints for a large and complex

- Callo-Arias、America 和 Avgeriou，“为大型复杂

software-intensive system”[27].

软件密集型系统定义执行视角”[27]。

The source above documents an “execution viewpoint catalog” for understanding the execution of complex software-intensive systems. The four architecture viewpoints are specified: Execution Profile, Execution Deployment, Resource Usage and Execution Concurrency. Correspondence methods between the architecture viewpoints are also included.

上述来源记录了一个“执行视角目录”，用于理解复杂软件密集型系统的执行。其中规定了四个架构视角：执行概貌、执行部署、资源使用和执行并发。还包括各架构视角之间的对应方法。

- Clements, et al., “Documenting Software Architectures: views and beyond”[28].

- Clements 等，“记录软件架构：视图与超越”[28]。

The source above provides extensive resources for defining 3 categories of specifications of architecture viewpoints. These categories, called viewtypes, are Module, Component and Connector and Allocation viewtypes. Within each viewtype, a number of styles are defined.

上述来源为定义 3 类架构视角规格提供了大量资源。这些类别称为视图类型，即模块视图类型、组件与连接件视图类型和分配视图类型。每一视图类型内都定义了若干风格。

- Eeles and Cripps, “The Process of Software Architecting”[32].

- Eeles 和 Cripps，“软件架构工作过程”[32]。

The source above defines a process for software architects, using the IEEE 1471-2000[1] model as a foundation. Provides a template for specifications of architecture viewpoints and architecture viewpoint catalogues including: Requirements, Functional, Deployment, Validation, Application, Infrastructure, Systems Management, Availability, Performance, Security; and the “work products” (i.e. model kind specifications) for each.

上述来源以 IEEE 1471-2000[1] 模型为基础，为软件架构师定义了一个过程。它提供了架构视角规格和架构视角目录的模板，包括：需求、功能、部署、验证、应用、基础设施、系统管理、可用性、性能、安全性；以及其中每一项的“工作产品”（即模型种类规格）。

- Architecture viewpoint Repository[64]

- 架构视角库[64]

The website is a repository for architecture viewpoints specified by the community.

该网站是一个汇集社区所规定架构视角的库。

- Kruchten, “The ‘4+1’ view model of software architecture”[40]

- Kruchten，“软件架构的‘4+1’视图模型”[40]

The source above specifies architecture viewpoints for Logical, Development, Process and Physical views. The resulting views are integrated via Scenarios.

上述来源为逻辑视图、开发视图、过程视图和物理视图规定了架构视角。所得到的各架构视图通过场景加以集成。

- Rozanski and Woods, “Software Systems Architecture: Working with Stakeholders Using Viewpoints

- Rozanski 和 Woods，“软件系统架构：使用视角与角度

and Perspectives”[54]

同利益相关方协同工作”[54]。

The source above defines a catalogue of architecture viewpoints: Functional, Information, Concurrency, Development, Deployment and Operational viewpoints and perspectives (see 5.2.4): Security, Performance and Scalability, Availability and Resilience, and Evolution perspectives for software-intensive systems.

上述来源定义了一个架构视角目录：功能、信息、并发、开发、部署和运行视角，以及角度（见 5.2.4）：针对软件密集型系统的安全性、性能和可伸缩性、可用性和韧性，以及演进角度。

> **NOTE** Rozanski and Woods’ perspectives do not fit the definition in this document.

> **注**：Rozanski 和 Woods 所说的角度不符合本文件中的定义。

## Annex C (informative) — Relationship to other standards ｜ 附录 C（资料性）— 与其他标准的关系

### C.1 General 总则

This annex illustrates how ADs created in accordance with this document can meet the requirements of other standards. This document specifies the core terminology and the concepts usable for AD. Other standards can use this document as a normative reference in order to define one or more architecture viewpoints, concerns, aspects and perspectives to be used in ADs within projects and enterprises.

本附录说明按本文件创建的 AD 如何能满足其他标准的要求。本文件规定了可用于 AD 的核心术语和概念。其他标准能将本文件作为规范性引用文件，以定义项目和企业的 AD 中所要使用的一个或多个架构视角、关注点、方面体和角度。

### C.2 Use with ISO/IEC/IEEE 42020 与 ISO/IEC/IEEE 42020 一起使用

ISO/IEC/IEEE 42020 specifies requirements, recommendations and permissions for architecture processes suitable for the enterprise, organization or project. In this reference document, AD is mainly addressed by a process called “architecture elaboration”, explaining how to describe or document an architecture in a sufficiently complete and correct manner for the intended uses of the architecture. Nevertheless, another ISO/IEC/IEEE 42020 process, called “architecture conceptualization”, can be undertaken to serve as the basis for an AD in order to characterize the problem space and determine suitable solutions that address stakeholder concerns, achieve architecture objectives and meet relevant requirements. Both architecture conceptualization and architecture elaboration are specified in ISO/IEC/IEEE 42020 through an extensive set of activities, tasks, outcomes and work products. Recognizing that particular projects or organizations do not need to use all of the processes specified by this document, full conformance and tailored conformance are defined to accommodate a flexible implementation approach to claim conformance to ISO/IEC/IEEE 42020.

ISO/IEC/IEEE 42020 规定了适用于企业、组织或项目的架构过程的要求、建议和许可。在本引用文件中，架构描述主要由称为“架构细化”的过程处理，该过程说明如何以足够完整和正确的方式描述或记录架构，以满足架构的预期用途。然而，也能开展 ISO/IEC/IEEE 42020 的另一过程，即“架构概念化”，作为架构描述的基础，以刻画问题空间并确定适当的解决方案，从而应对利益相关方关注点、实现架构目标并满足相关要求。架构概念化和架构细化在 ISO/IEC/IEEE 42020 中均通过一整套广泛的活动、任务、预期结果和工作产品加以规定。考虑到特定项目或组织并不需要使用本文件规定的全部过程，定义了完全符合性和裁剪符合性，以支持灵活的实施途径来声称对 ISO/IEC/IEEE 42020 的符合性。

### C.3 Use with ISO/IEC/IEEE 42030 与 ISO/IEC/IEEE 42030 一起使用

ISO/IEC/IEEE 42030 provides a conceptual foundation for examining architecture related information that can help determine facts about the architecture. It provides a generic, conceptual guiding framework that can be used for the planning, execution, and documentation of architecture evaluations. The elements presented can be used to determine architecture value, determine architectural characteristics, validate whether an architecture can address evaluation criteria, validate whether the architecture addresses current and future stakeholder needs, and also provide inputs to decisions made at the operational and tactical levels. ISO/IEC/IEEE 42030 proposes three tiers for architecture evaluation. The evaluation synthesis tier aids in combining results from multiple value assessments to determine to what extent the evaluation objectives will be achieved. The value assessment tier aids in determining the amount and kind of value a stakeholder can expect from the architecture. The architectural analysis tier aids in examining the key attributes of an architecture, or the relevant attributes of the architecture entity, as well as actual or potential impacts on stakeholders or on the environment. In ISO/IEC/IEEE 42030, AD is considered to help determine the different architecture concepts and architecture related information necessary for the purposes of architecture evaluation. Nevertheless, AD is considered in order to determine the value due to an architecture and quality characteristics exhibited by the entity and its architecture.

ISO/IEC/IEEE 42030 为审查架构相关信息提供了概念基础，这些信息能帮助确定关于架构的事实。它提供了一个通用的概念性指导框架，能用于架构评估的策划、执行和文档编制。所给出的要素能用于确定架构价值、确定架构特性、验证架构是否能应对评估准则、验证架构是否应对当前和未来的利益相关方需要，并为在运行层和战术层做出的决策提供输入。ISO/IEC/IEEE 42030 提出了架构评估的三个层级。评估综合层级有助于组合多项价值评定的结果，以确定评估目标将在何种程度上得以实现。价值评定层级有助于确定利益相关方能从架构中预期得到的价值的数量和种类。架构分析层级有助于审查架构的关键属性或者架构实体的相关属性，以及对利益相关方或环境的实际影响或潜在影响。在 ISO/IEC/IEEE 42030 中，架构描述被认为有助于确定为架构评估目的所需的不同架构概念和架构相关信息。然而，考虑架构描述，是为了确定归于架构的价值以及实体及其架构所展现的质量特性。

### C.4 Use with ISO 15704 与 ISO 15704 一起使用

ISO 15704 specifies a reference base of concepts and principles for enterprise architectures that enable enterprise development, enterprise integration, enterprise interoperability, human understanding and computer processing and further specifies requirements for models and languages created for expressing such enterprise architectures.

ISO 15704 规定了企业架构的概念与原则的参考基础，使能企业发展、企业集成、企业互操作、人的理解和计算机处理，并进一步规定了为表达此类企业架构而创建的模型和语言的要求。

ISO 15704 specifies those terms, concepts and principles considered necessary to address stakeholder concerns and to carry out enterprise creation programs as well as any incremental change projects required by the enterprise throughout the whole life of the enterprise and forms the basis by which enterprise architecture and modelling standards can be developed or aligned.

ISO 15704 规定了为应对利益相关方关注点、实施企业创建计划以及开展企业在整个企业生存期内所需的任何增量变更项目而被认为必要的术语、概念和原则，并构成据以制定或协调企业架构与建模标准的基础。

ISO 15704 does not present or adopt specific methodologies for creating or using enterprise architectures or models but does utilize this document as a source of some terminology and overall characterization of an architecture description. However, the focus is on establishing a reference base capable of supporting specific enterprise programs, rather than a design intended to fulfil the stated requirements.

ISO 15704 不提出也不采用用于创建或使用企业架构或模型的具体方法论，但确实将本文件用作某些术语以及架构描述总体刻画的来源。然而，其重点在于建立能够支持特定企业计划的参考基础，而不是意在满足所陈述要求的设计。

ISO 15704 identifies an extensive collection of potential artefacts for expressing an enterprise-referencing architecture and its associated methodologies. Not all of these artefacts will be applicable, necessary or even desirable for all architecting efforts. The identification of these artefacts assures that this document meets the needs of the widest possible number of enterprise-referencing architecture and methodology situations. Users of this document need to assess not only the value of generating an identified artefact but also the value of maintaining that artefact under the changing circumstances of the referenced enterprise.

ISO 15704 识别出一大批潜在的人工制品，用于表达引用企业的架构及其相关联的方法论。并非所有这些人工制品都适用于、有必要用于、甚至宜用于所有的架构工作。识别这些人工制品可确保本文件满足尽可能多的引用企业的架构与方法论情形的需要。本文件的使用者不仅需要评定生成某个已识别人工制品的价值，还需要评定在所引用企业的情况不断变化之下维护该人工制品的价值。

The approach taken in ISO 15704 is the use of systems thinking and systems theory in enterprise architecture and about how it is possible to reconcile and understand, based on a single overarching framework, the interplay of two major enterprise change endeavours: enterprise engineering (i.e. deliberate change) and evolutionary, organic change. This approach has stood the test of time in diverse applications [51].

ISO 15704 所采取的方法是在企业架构中运用系统思维和系统理论，并说明如何基于单一总体框架来协调和理解两项重大企业变革努力的相互作用：企业工程（即有意的变革）与演化的、有机的变革。该方法已在多种应用中经受住了时间的检验 [51]。

ISO 15704 is concerned with the complete life cycle architecture of entities in an enterprise context and advocates model-based architecting and a framework to be used for organizing models of these entities.

ISO 15704 关注企业语境下实体的全生存周期架构，并倡导基于模型的架构工作以及用于组织这些实体的模型的框架。

Accordingly, a modelling framework is to provide the means (dimensions) to organize models according to:

据此，建模框架要提供按照以下方面组织模型的手段（维度）：

- The extent of abstraction used by the model, such as covering identity, concept, requirements,

- 模型所采用的抽象程度，例如涵盖标识、概念、要求、

preliminary (architectural) design, detailed design, build/implementation, operation and decommissioning. (Note that the scope of ISO 15704 is therefore broader than architectural design.)

初步（架构）设计、详细设计、构建／实施、运行和退役。（注意，ISO 15704 的范围因此比架构设计更宽泛。）

- The type of information (or aspect) about the entity as conveyed by the model (function, information,

- 模型所传达的关于实体的信息类型（或方面体）（功能、信息、

resource, and organization), which characterizes viewpoints across extents of abstraction.

资源和组织），它刻画了跨各抽象程度的架构视角。

- The scope of information covered (models describing mission fulfilment and mission control)

- 所覆盖的信息范围（描述使命履行和使命控制的模型）

- The scope according to the means of implementation (models describing human-implemented and

- 按照实施手段划分的范围（描述由人实施的和

technology-implemented parts of the entity)

由技术实施的实体部分的模型）

In addition, ISO 15704 provides a categorization of models according to a genericity-to-specificity axis. Accordingly, in a modelling framework there is a continuum, covering

此外，ISO 15704 按照从通用性到专用性的轴提供了模型的分类。据此，在建模框架中存在一个连续谱，涵盖

- Generic models that capture the semantics of concepts used across all of the dimensions of enterprise

- 通用模型，它们捕获在相关领域内企业

modelling in the domain of interest. Typical representations of generic models (in increasing level of formality) include taxonomies, meta-models, and ontological theories. The level of detail of metamodels would vary depending on the domain (examples include ISO 19440, UAF domain metamodel, etc.)

建模的所有维度上所使用的概念的语义。通用模型的典型表示（按形式化程度递增）包括分类体系、元模型和本体论理论。元模型的详细程度会随领域而异（示例包括 ISO 19440、UAF 领域元模型等）

- Partial models, which are reusable, paradigmatic, typical models (or model fragments, or model

- 部分模型，即可复用的、范例式的、典型的模型（或模型片段，或模型

building blocks) that capture characteristics common to many enterprises within or across one or more industrial sectors. Combined with the extent of abstraction axis this provides for the organization of models.

构建块），它们捕获在一个或多个工业部门之内或跨部门的许多企业所共有的特性。与抽象程度轴相结合，这为组织模型提供了依据。

An important kind of partial model is a reference model, which captures the common characteristics of a set of particular entities, such as the model of a product line, or a collection of models covering the architecture of a product line.

一种重要的部分模型是参考模型，它捕获一组特定实体的共有特性，例如产品线的模型，或涵盖产品线架构的模型集合。

> **NOTE** Most ISO standards can be represented as partial models or reference models.

> **注**：大多数 ISO 标准都能表示为局部模型或参考模型。

- Particular models, each describing an individual entity of interest.

- 各个具体模型，每个模型描述一个单独的所关注实体。

An example of a modelling framework is provided in ISO 15704:2019 Annex B (GERAM) and ISO 19439, which latter is an elaboration of GERAM’s GERA Modelling Framework (see Figure C.1).

建模框架的一个示例见 ISO 15704:2019 附录 B（GERAM）和 ISO 19439，后者是 GERAM 的 GERA 建模框架的细化（见图 C.1）。

![Figure C.1 — Depiction of GERA modelling framework](ISO_IEC_IEEE 42010 2023.assets/fig-10.png)

**Figure C.1 — Depiction of GERA modelling framework**

**图 C.1 — GERA 建模框架图示**

Practitioners may use a tool-supported architecture modelling framework (AMF) to organize models as above, because in this way various views of these models can be produced and packaged for stakeholder consumption as proposed by architecture description frameworks (ADFs).

从业者可使用工具支持的架构建模框架（AMF）按上述方式组织模型，因为这样就能生成这些模型的各种视图，并按架构描述框架（ADF）所提出的方式打包供利益相关方使用。

This approach is more economical than updating views and propagating the effects of such updates across multiple views, because often the same model can be used to extract from it a multitude of views (both in form and level of detail, according to stakeholder viewpoints); this will eliminate many correspondence problems across views that otherwise may arise if using purely description-based architecture views.

这种方法比更新视图并在多个视图之间传播此类更新的影响更为经济，因为同一个模型往往可用于从中提取大量视图（在形式和详细程度上均依利益相关方视角而定）；这将消除视图之间的许多对应问题，而若使用纯粹基于描述的架构视图，这些问题本可能出现。

Another distinguishing feature of the GERAM approach is the use of recursion and iteration to manage the complicated relationships within an enterprise and its supply chain (see Figure C.2).

GERAM 方法的另一个显著特征是使用递归与迭代来管理企业及其供应链内部的复杂关系（见图 C.2）。

![Figure C.2 — Recursive use of ADs that iterate life cycle modelling phases](ISO_IEC_IEEE 42010 2023.assets/fig-11.png)

**Figure C.2 — Recursive use of ADs that iterate life cycle modelling phases**

**图 C.2 — 迭代生存周期建模阶段的架构描述的递归使用**

### C.5 Use with ISO/IEC/IEEE 12207 与 ISO/IEC/IEEE 12207 一起使用

ISO/IEC/IEEE 12207 defines one process specifically pertaining to software architecture: architecture definition (see ISO/IEC/IEEE 12207). The concept of architecture in this document is consistent with the architectural design processes of ISO/IEC/IEEE 12207. However, ISO/IEC/IEEE 12207 places requirements on an AD in addition to those of this document. Specifically, an architecture definition needs to include an identification of the architecture entities included in the software and an allocation of key stakeholder concerns and critical software requirements to those items.

ISO/IEC/IEEE 12207 定义了一个专门与软件架构有关的过程：架构定义（见 ISO/IEC/IEEE 12207）。本文件中架构的概念与 ISO/IEC/IEEE 12207 的架构设计过程一致。但 ISO/IEC/IEEE 12207 对本文件之外的架构描述另提要求。具体而言，架构定义需要包含对软件中所含架构实体的标识，以及将关键利益相关方关注点和关键软件需求分配给这些项。

As observed in the NOTE accompanying ISO/IEC/IEEE 12207:2017, 6.4.4.3 c) 2), architecture is not necessarily concerned with all requirements, but rather only with those that drive the architecture, hence the focus of the architecture definition process on the critical software requirements.

正如 ISO/IEC/IEEE 12207:2017, 6.4.4.3 c) 2) 所附注中指出的，架构并不一定涉及所有需求，而只涉及驱动架构的那些需求，因此架构定义过程聚焦于关键软件需求。

The expected use of an AD can include other ISO/IEC/IEEE 12207 processes. In particular, an AD is used to communicate the architecture to the Design Definition process and can be used to facilitate the communications between the acquirer and the developer roles in other software life cycle processes.

架构描述的预期用途可包括其他 ISO/IEC/IEEE 12207 过程。特别是，架构描述用于向设计定义过程传达架构，并可用于促进其他软件生存周期过程中采购方与开发方角色之间的沟通。

An AD can conform to this document and to ISO/IEC/IEEE 12207.

架构描述能符合本文件，也能符合 ISO/IEC/IEEE 12207。

### C.6 Use with ISO/IEC/IEEE 15288 与 ISO/IEC/IEEE 15288 一起使用

ISO/IEC/IEEE 15288 defines one process specifically pertaining to system architecture: architecture definition. The concept of architecture in this document is consistent with the architecture definition process of ISO/IEC/IEEE 15288. However, ISO/IEC/IEEE 15288 places requirements on an AD in addition to those herein. Specifically, an architecture definition needs to include an identification of the architecture entities included in the system and an allocation of key stakeholder concerns and critical system requirements to those items. These can be achieved in various ways, such as by creating decomposition and allocation architecture viewpoints, or through use of correspondences.

ISO/IEC/IEEE 15288 定义了一个专门与系统架构有关的过程：架构定义。本文件中架构的概念与 ISO/IEC/IEEE 15288 的架构定义过程一致。但 ISO/IEC/IEEE 15288 对架构描述另提要求，超出本文所提要求。具体而言，架构定义需要包含对系统中所含架构实体的标识，以及将关键利益相关方关注点和关键系统需求分配给这些项。这些可通过多种方式实现，如创建分解与分配架构视角，或使用对应关系。

As observed in the NOTE accompanying ISO/IEC/IEEE 15288:2015, 6.4.4.3 c) 2), architecture is not necessarily concerned with all requirements, but rather only with those that drive the architecture, hence the focus of the architecture definition process on the critical system requirements.

正如 ISO/IEC/IEEE 15288:2015, 6.4.4.3 c) 2) 所附注中指出的，架构并不一定涉及所有需求，而只涉及驱动架构的那些需求，因此架构定义过程聚焦于关键系统需求。

The expected uses of an AD can include other ISO/IEC/IEEE 15288 processes. In particular, an AD is used to communicate the system architecture to the design definition process and can be used to facilitate the communications between the acquirer and the developer roles in other system life cycle processes.

架构描述的预期用途可包括其他 ISO/IEC/IEEE 15288 过程。特别是，架构描述用于向设计定义过程传达系统架构，并可用于促进其他系统生存周期过程中采购方与开发方角色之间的沟通。

An AD can conform to this document and to ISO/IEC/IEEE 15288.

架构描述能符合本文件，也能符合 ISO/IEC/IEEE 15288。

### C.7 Use with open distributed processing standards 与开放分布式处理标准一起使用

#### C.7.1 General 总则

The reference model of open distributed processing (RM-ODP)[2] defines an ADF for distributed processing systems; systems “in which discrete components may be located in different places, or where communication between components may suffer delay or may fail.” (see ISO/IEC 10746-2).

开放分布式处理的参考模型（RM-ODP）[2]为分布式处理系统定义了一种架构描述框架；此类系统是“其中离散组件可位于不同地点，或组件之间的通信可能遭受延迟或可能失败”的系统（见 ISO/IEC 10746-2）。

The RM-ODP framework defines five viewpoints for specifying ODP systems and a set of correspondences between them.

RM-ODP 框架定义了用于规定 ODP 系统的五个视角，以及它们之间的一组对应关系。

For each viewpoint, there is an associated viewpoint language which defines “the concepts and rules for specifying ODP systems from the corresponding viewpoint”.

对于每个视角，都有一个相关联的视角语言，它定义了“从相应视角规定 ODP 系统的概念和规则”。

An AD conforming to this document and using ISO/IEC 10746-3 would include the viewpoints defined by ISO/IEC 10746-3 and views to implement these viewpoints. A conforming AD does not need to be limited to the five predefined viewpoints of ISO/IEC 10746-3; the AD can include additional viewpoints and views, as needed.

符合本文件并使用 ISO/IEC 10746-3 的架构描述将包含由 ISO/IEC 10746-3 定义的视角和实现这些视角的视图。符合的架构描述不必局限于 ISO/IEC 10746-3 的五个预定义视角；架构描述可按需包含附加的视角和视图。

Elements of that specification specific to ADs (such as stakeholders) are omitted here since they are particular to individual systems. Unless noted, all contents are direct quotes or close paraphrases from ISO/IEC 10746-3.

该规格中特定于架构描述的元素（如利益相关方）在此省略，因为它们因各个系统而异。除另有说明外，所有内容均直接引自或近似转述自 ISO/IEC 10746-3。

> **NOTE** ISO/IEC 19793 defines a UML profile for the specification of open distributed processing systems using these viewpoints.

> **注**：ISO/IEC 19793 定义了使用这些视角规定开放分布式处理系统的 UML 概要。

#### C.7.2 Enterprise viewpoint 企业视角

The enterprise viewpoint frames these concerns:

企业视角框定以下关注点：

- the purpose, scope and policies for an ODP system;

- ODP 系统的目的、范围和策略；

- activities undertaken by the system;

- 系统所开展的活动；

- policy statements about the system.

- 关于系统的策略陈述。

In the enterprise language, an ODP system and its environment are represented as a community of objects. The community is defined in terms of:

在企业语言中，ODP 系统及其环境被表示为对象的社区。该社区按以下各项定义：

- enterprise objects comprising the community;

- 构成该社区的企业对象；

- roles fulfilled by each of those objects;

- 由这些对象中每个对象履行的角色；

- policies governing interactions between enterprise objects fulfilling roles;

- 管控履行角色的企业对象之间交互的策略；

- policies governing the creation, usage and deletion of resources by enterprise objects fulfilling

- 管控履行角色的企业对象对资源的创建、使用和删除的策略

roles;

角色的；

- policies governing the configuration of enterprise objects and assignment of roles to enterprise

- 管控企业对象的配置和角色向企业对象分配的策略

objects;

对象的；

- policies relating to environment contracts governing the system.

- 与环境契约有关的、管控系统的策略。

> **NOTE 1** Roles constrain the behaviour of the objects that fulfil them.

> **注 1**：角色约束履行这些角色的对象的行为。

> **NOTE 2** Policies are defined in terms of permissions, obligations, and prohibitions.

> **注 2**：策略用许可、义务和禁止来定义。

> **NOTE 3** The enterprise language is defined in ISO/IEC 15414.

> **注 3**：企业语言在 ISO/IEC 15414 中定义。

#### C.7.3 Information viewpoint 信息视角

The information viewpoint frames these concerns: the semantics of information and information processing in an ODP system.

信息视角框定以下关注点：ODP 系统中信息与信息处理的语义。

The information language is defined in terms of three schemata:

信息语言按三个模式定义：

- invariant schema: predicates on objects which always need to be true;

- 不变模式：对象上始终需要为真的谓词；

- static schema: state of one or more objects at some point in time;

- 静态模式：某一时间点上的一或多个对象的状态；

- dynamic schema: allowable state changes of one or more objects.

- 动态模式：一或多个对象允许的状态变化。

#### C.7.4 Computational viewpoint 计算视角

The computational viewpoint frames these concerns: a functional decomposition of the system into objects which interact at interfaces.

计算视角框定以下关注点：系统按在接口处交互的对象所作的功能分解。

The computational language covers concepts for specifying:

计算语言涵盖用于规定以下内容的概念：

- computational objects;

- 计算对象；

- interfaces to objects and interface definitions;

- 对象的接口及接口定义；

- interactions at interfaces, as either operations or continuous streams;

- 接口处的交互，其形式为操作或连续流；

- implicit and explicit bindings and compound binding objects.

- 隐式与显式绑定以及复合绑定对象。

#### C.7.5 Engineering viewpoint 工程视角

The engineering viewpoint frames these concerns: the mechanisms and functions required to support distributed interaction between objects in the system.

工程视角框定以下关注点：支持系统中各对象之间分布式交互所需的机制与功能。

The engineering language includes concepts for specifying:

工程语言涵盖用于规定以下内容的概念：

- the structure of communication channels that connect engineering objects, in terms of stubs,

- 连接工程对象的通信通道的结构，以桩、

binders, protocols and interceptors;

绑定件、协议和拦截器来表达；

- templates for providing required transparencies, such as migration, relocation, replication and

- 用于提供所需透明性的模板，例如迁移透明性、重定位透明性、复制透明性和

failure transparencies.

故障透明性。

#### C.7.6 Technology viewpoint 技术视角

The technology viewpoint frames these concerns: the selection of implementable standards for the system, their implementation and testing.

技术视角框定以下关注点：为系统选择可实现的标准，以及这些标准的实施与测试。

The technology language includes concepts to:

技术语言涵盖用于以下各项的概念：

- capture the choice of technology to be used, in terms of the selection of existing standards or

- 捕获所选用技术的选择，即选择现有标准或

domain-specific specifications for these technologies;

针对这些技术的领域特定规格；

- express how the specifications for an ODP system are implemented;

- 表达 ODP 系统的规格如何得到实现；

- provide support for testing.

- 为测试提供支持。

## Annex D (informative) — Uses of architecture descriptions ｜ 附录 D（资料性）— 架构描述的用途

### D.1 General 总则

ADs can be used in a variety of settings and life cycle models. This annex illustrates a few uses of ADs throughout the life cycle of their entities of interest.

AD 能用于各种情境和生存周期模型。本附录举例说明在其所关注实体的整个生存周期中 AD 的若干用途。

### D.2 Uses of architecture descriptions 架构描述的用途

Uses for ADs include, but are not limited to:

AD 的用途包括但不限于：

a) as basis for entity design and development activities;

a) 作为实体设计与开发活动的依据；

b) as basis to analyse and evaluate alternative implementations of an architecture;

b) 作为分析和评估架构的备选实现的依据；

c) as development and maintenance documentation;

c) 作为开发与维护文档；

d) to support informed technical, investment or other strategic decisions, to reduce or mitigate attendant risk;

d) 支持知情的技术、投资或其他战略决策，以降低或缓解伴随风险；

e) documenting essential features of an entity of interest, such as:

e) 记录所关注实体的本质特征，例如：

1) intended use and environment;

1) 预期用途与环境；

2) principles, assumptions and constraints to guide future change;

2) 指导未来变更的原则、假设与约束；

3) points of flexibility or limitations of the entity with respect to future changes;

3) 实体在未来变更方面的灵活性之处或局限；

4) architecture decisions, their rationales and implications;

4) 架构决策及其理由与影响；

5) recording its architecture styles;

5) 记录其架构风格；

f) as input to automated tools for simulation, system generation and analysis;

f) 作为用于仿真、系统生成和分析的自动化工具的输入；

g) specifying a group or family of entities sharing common features (such as can be codified as a reference architecture, reference model or product line architecture);

g) 规定共享共同特征的实体组或实体族（例如可编纂为参考架构、参考模型或产品线架构者）；

h) communicating among parties involved in the development, production, deployment, operation and maintenance of an entity of interest streamlining the flow from architecture and system engineering to development;

h) 在参与所关注实体的开发、生产、部署、运行与维护的各方之间沟通，从而理顺从架构与系统工程到开发的流程；

i) as basis for preparation of acquisition documents (such as requests for proposal and statements of work);

i) 作为编制采办文件（如建议征询书和工作说明书）的依据；

j) communicating among clients, acquirers, suppliers and developers as a part of contract negotiations;

j) 在客户、采购方、供方和开发方之间沟通，作为合同谈判的一部分；

k) documenting the characteristics, features and design of an entity for potential clients, acquirers, owners, operators and integrators;

k) 为潜在客户、采购方、所有者、运行方和集成方记录实体的特性、特征与设计；

l) planning for transition from a legacy architecture to a new architecture;

l) 策划从遗留架构向新架构的过渡；

m) as guide to operational and infrastructure support and configuration management;

m) 作为运行与基础设施支持以及配置管理的指南；

o) establishing criteria for certifying implementations for compliance with an architecture;

o) 确立对实现进行符合某一架构的认证的准则；

p) as compliance mechanism to external, program-, project- or organization-specific policies (for example legislation, or overarching architecture principles adopted by governance);

p) 作为对外部、项目群、项目或组织特定方针（例如法律法规，或治理所采用的总体架构原则）的符合性机制；

q) as basis for review, analysis, and evaluation of the entity throughout its life cycle;

q) 作为在实体整个生存周期中对其进行评审、分析和评估的依据；

r) as basis to analyse and evaluate alternative architectures;

r) 作为分析和评估备选架构的依据；

s) sharing lessons learned and reusing architectural knowledge through definition of architecture viewpoints, architecture patterns and architecture styles;

s) 通过定义架构视角、架构模式和架构风格，分享经验教训并复用架构知识；

t) training and education of stakeholders and other parties on best practices in architecting and evolution;

t) 就架构工作与演进方面的最佳实践对利益相关方和其他各方开展培训与教育；

u) as evidence for entity functional and non-functional properties;

u) 作为实体功能与非功能性质的证据；

v) scenario-based simulation.

v) 基于场景的仿真。

> **NOTE** Annex C discusses the use of ADs in the context of other standards.

> **注**：附录 C 讨论在其他标准的语境中 AD 的用途。

## Annex E (informative) — Architecture and architecture description life cycles ｜ 附录 E（资料性）— 架构与架构描述的生存周期

### E.1 General 总则

ADs can be used in a variety of settings and life cycle models. This annex illustrates a few concepts pertaining to architecture life cycles and AD life cycles.

AD 能用于各种情境和生存周期模型。本附录举例说明若干与架构生存周期和 AD 生存周期有关的概念。

### E.2 Architecting in the life cycle 生存周期中的架构工作

Architecting contributes to the conceptualization, development, operation and maintenance of an entity from its initial conception through its operation, refurbishment or final retirement from use, and eventual disposal.

架构工作有助于实体的概念化、开发、运行和维护，即从实体最初的构想，经其运行、翻新或最终退役停用，直至最终处置。

Architecting can take place throughout the life cycle of the entity, not necessarily only within the early stage of its life. Therefore, an entity’s architecture potentially influences processes throughout the entity’s life cycle. While it is expected that the architecture of an entity remains stable over a longer period, from time to time the architecture of the entity (or a part of the entity) can incrementally evolve. Less frequently an entity can go through a significant transformation, with necessary re-architecting being performed.

架构工作能贯穿实体的整个生存周期进行，不一定仅限于其生存周期的早期阶段。因此，实体的架构可能影响实体整个生存周期中的各个过程。虽然预期实体的架构在较长时期内保持稳定，但实体的架构（或实体的一部分）能不时增量演进。实体较少经历重大转变，此时则开展必要的重新架构工作。

ADs are the work products resulting from the execution of architecting efforts to transmit, share and record the architecture of the entity and associated decisions across the life cycle. The original and subsequent (incremental or extensive) architecting efforts communicate and document the outcome from using ADs. The status and history of solution alternatives and versions are expressed as architecture descriptions.

AD 是执行架构工作所产生的工作产品，用于在整个生存周期中传递、共享和记录实体的架构及相关决策。最初的架构工作和后续的（增量的或大范围的）架构工作，均借助 AD 来沟通和记录其成果。解决方案备选方案与版本的状态和历史表达为架构描述。

> **NOTE 1** ISO/IEC/IEEE 15288 and ISO/IEC/IEEE 12207 describes the architecture definition process. ISO/IEC/IEEE 42020 complements this definition toward a complete set of architecture processes in support of architecting efforts.

> **注 1**：ISO/IEC/IEEE 15288 和 ISO/IEC/IEEE 12207 描述架构定义过程。ISO/IEC/IEEE 42020 补充这一定义，以形成支持架构工作的一整套架构过程。

The developed models and other information parts, as well as the ADs themselves, each have their own life cycle. During architecture development the need for the architecture is identified, the architecture concepts are defined, its details are elaborated, trade-offs and possible realizations are analysed, evaluated and approved, and released for use, then utilized. Later the AD can be updated, and new versions released. Ideally the stages of utilization are long and stable, because of the efficiencies achieved by using a shared architecture in the life cycle of multiple entities. Therefore, the architecture of the entity(ies) of interest has its own life cycle.

所开发的模型和其他信息部件以及 AD 本身，各自都有其生存周期。在架构开发期间，识别对架构的需要，定义架构概念，细化其细节，对权衡与可能的实现进行分析、评估和批准，并发布以供使用，随后加以利用。之后，AD 可予以更新，并发布新版本。理想情况下，利用阶段漫长而稳定，因为在多个实体的生存周期中使用共享的架构能获得效率。因此，所关注实体的架构有其自身的生存周期。

Conversely, the life cycle of any entity is fundamentally influenced by the life cycle of its architecture. For example, investment decisions to create a project to develop a system of systems based upon the existing systems in a service ecosystem heavily depend on the existence of a stable, trusted, shared and agreed-upon architecture of its integrating infrastructure. When planning the life cycle stages of an entity, the plan will take into account the predicted life cycle stages of the chosen architecture.

反之，任何实体的生存周期都从根本上受其架构生存周期的影响。例如，为基于服务生态系统中的现有系统开发系统的系统而立项的投资决策，很大程度上取决于其集成基础设施是否具有稳定、可信、共享且经协商一致的架构。在策划实体的生存周期阶段时，该策划将考虑所选架构的预测生存周期阶段。

The process of architecting involves thinking about the entity of interest from multiple perspectives, and these perspectives correspond to life cycle phase activities. For example, the architect will consider the entity from the business perspective, including the entity’s identity, as well as the concept of the entity (such as its role in the market, the capabilities, the relationships to the business context, and the policies and principles that need to govern the solution). The architect will also consider the high-level requirements that the entity needs to satisfy (functional and non-functional requirements), and from the business analyst’s perspective translate this to a specification. The architect will also translate these requirements to an architectural solution, which is a preliminary design of the entity of interest and prepare the solution for evaluation.

架构工作的过程涉及从多个角度思考所关注实体，而这些角度与生存周期阶段的活动相对应。例如，架构师将从业务角度考虑实体，包括实体的标识以及实体的概念（例如其在市场中的角色、能力、与业务语境的关系，以及需要管控解决方案的方针与原则）。架构师还将考虑实体需要满足的高层级要求（功能要求与非功能要求），并从业务分析师的角度将其转化为规格。架构师还将转化这些要求转化为架构解决方案，该方案是所关注实体的初步设计，并为评估准备该解决方案。

The phases (identity definition, concept development, requirements definition, preliminary design, as defined in ISO 15704) are activity types that are normally iterated within the architecture development stage (as defined in ISO/IEC/IEEE 15288 and ISO/IEC/IEEE 12207) until the relevant stakeholder questions can all be addressed in a satisfactory manner. The concept of phase is therefore referring to a type of activity, whereupon instances of that activity are repeated as necessary during a stage and typically across multiple future stages of the entity’s life.

各阶段（标识定义、概念开发、要求定义、初步设计，如 ISO 15704 所定义）是活动类型，通常在架构开发阶段（如 ISO/IEC/IEEE 15288 和 ISO/IEC/IEEE 12207 所定义）内迭代，直至相关的利益相关方问题都能以令人满意的方式得到处理。因此，阶段这一概念指的是一种活动类型，该活动的实例在某一阶段内按需重复，并且通常跨越实体生存周期的多个后续阶段。

The need for iterations depends on multiple factors, such as the innovation content of the architecture development, skills and maturity of the organization, the availability of reference architectures or patterns that can be reused, and the methodology used.

迭代的必要性取决于多种因素，例如架构开发的创新含量、组织的技能与成熟度、可复用的参考架构或模式的可用性，以及所使用的方法论。

It is typical for architecture development to be performed in the organizational setting of a project or program, in which case the program and its projects need to be architected as well, as entities in their own right. The same is true in the setting of systems of systems and of supporting systems (as defined in ISO/IEC/IEEE 15288 and ISO/IEC/IEEE 24748-1), each of these systems are implemented as entities that would need to be architected if not pre-existing.

架构开发通常是在项目或项目群的组织环境中进行的，此时项目群及其项目本身也作为实体而需要被架构。在系统的系统以及支持系统（如 ISO/IEC/IEEE 15288 和 ISO/IEC/IEEE 24748-1 所定义）的环境中同样如此：这些系统中的每一个都作为实体来实现，若不预先存在，这些实体就需要被架构。

In the process of architecture development architects must engage in two-way communication with stakeholders – both for getting informed and to inform. Work products incorporate various information parts (more and more often various models), which then form the basis of creating ADs that are in a form that stakeholders and architects mutually understand and that satisfy the goal of architecting as defined by architecture governance and management.

在架构开发过程中，架构师必须与利益相关方进行双向沟通——既为获取信息，也为传递信息。工作产品纳入各种信息部分（越来越多地是各种模型），这些信息部分随后构成创建 AD 的基础，而 AD 的形式是利益相关方与架构师双方都理解的，并满足由架构治理与管理所定义的架构工作目标。

This document does not depend upon, assume or prescribe any particular life cycle.

本文件不依赖、不假定也不规定任何特定的生存周期。

> **NOTE 2** Annex C demonstrates how this document can be used when applying the life cycle processes of ISO/IEC/IEEE 12207 and ISO/IEC/IEEE 15288. ISO/IEC/IEEE 42020 specifies a set of processes for architecting, and for architecture governance, management, and enablement within the context of a life cycle.

> **注 2**：附录 C 演示了在应用 ISO/IEC/IEEE 12207 和 ISO/IEC/IEEE 15288 的生存周期过程时如何使用本文件。ISO/IEC/IEEE 42020 规定了在生存周期语境中用于架构工作以及用于架构治理、架构管理和架构使能的一组过程。

## Annex F (informative) — Architecture description frameworks ｜ 附录 F（资料性）— 架构描述框架

### F.1 General 总则

This annex provides examples of ADFs and the way they use the concepts defined in 5.4.2 (see Figure 6). Each of them conforms to applicable requirements of 7.1.

本附录给出 ADF 的示例以及它们使用 5.4.2 中所定义概念的方式（见图 6）。其中每一个都符合 7.1 的适用要求。

### F.2 Evolution of ADFs ADF 的演进

In systems and software engineering, the notion of ADF dates back to the 1970s.[31][67][29] The motivation for definition of the term (3.5) and its specification (see 7.1) in this document is to provide a means of evolving existing and future ADFs in a uniform manner to promote sharing of information about entities, architectures and techniques for AD, better uniformity to enable improved understanding of the architectures being described, and interoperability between architecture communities who use different conceptual foundations. The uniform definition of architecture viewpoints and coordinated collections of associated specifications can promote reuse of tools and techniques by the communities using these frameworks.

在系统与软件工程中，ADF 的概念可追溯至 20 世纪 70 年代。[31][67][29] 本文件定义该术语(3.5)并规定其规格（见 7.1），其动因在于：提供一种以统一方式演进既有和未来 ADF 的手段，以促进关于实体、架构和 AD 技术的信息共享、促成更好的一致性以便更好地理解所描述的架构，并促进使用不同概念基础的各架构团体之间的互操作。架构视角的统一定义以及相关规格的协调集合，能促进使用这些框架的团体对工具和技术的复用。

The specification of ADF is intended to establish the relationships between an ADF and other concepts in this document (illustrated in Figure 2 and Figure 6). ADFs often include additional content, prescriptions and relationships, such as process guidance, life cycle connections, and documentation formats, not defined by this document. These are potential future areas of standardization.

ADF 的规格旨在确立 ADF 与本文件中其他概念之间的关系（见图 2 和图 6）。ADF 常包含本文件未规定的其他内容、规定和关系，例如过程指南、生存周期关联和文档格式。这些是未来可能的标准化领域。

### F.3 ADF concepts ADF 概念

#### F.3.1 ADF domains ADF 域

Various architecture frameworks have been in existence over a few decades.

各种架构框架已存在数十年。

> **EXAMPLE** GERA Framework provided by ISO 15704, Industrial Internet Architecture Framework,[36] Kruchten’s “4+1” view model,[40] NATO Architecture Framework (NAF),[44] US Department of Defence Architecture Framework (DoDAF),[31] OASIS - Reference Architecture Foundation for Service Oriented Architecture,[45] Reference Model for Open Distributed Processing (RM-ODP),[2][3][4] The Open Group’s Architecture Framework(TOGAF),[62] OMG’s Unified Architecture Framework,[48] and Zachman’s information systems architecture framework[67].

> **示例**：ISO 15704 提供的 GERA 框架、工业互联网架构框架、[36] Kruchten 的“4+1”视图模型、[40] NATO 架构框架（NAF）、[44] 美国国防部架构框架（DoDAF）、[31] OASIS 面向服务的架构参考架构基础、[45] 开放分布式处理参考模型（RM-ODP）、[2][3][4] The Open Group 的架构框架（TOGAF）、[62] OMG 的统一架构框架、[48] 以及 Zachman 的信息系统架构框架[67]。

> **NOTE** GERAM provides an ADF for an enterprise architecture modelling activity and is therefore a modelling framework covering the whole of life for an entity of interest.

> **注**：GERAM 为企业架构建模活动提供了一种 ADF，因此是一种覆盖所关注实体整个生存周期的建模框架。

Most of them are dedicated to creating ADs in different domains like:

其中大多数专用于在不同领域创建 AD，例如：

- Zachman[67] and TOGAF[62] for information systems;

- Zachman[67] 和 TOGAF[62] 用于信息系统；

- Kruchten’s “4+1” view model[40] for software;

- Kruchten 的“4+1”视图模型[40] 用于软件；

- NAF,[44] DoDAF[31] and UAF[48] for enterprises and systems of systems;

- NAF，[44] DoDAF[31] 与 UAF[48] 用于企业和系统的系统；

- GERA (ISO 15704) for enterprise modelling of socio-technical systems of systems, e.g. industrial

- GERA（ISO 15704）用于社会技术系统的系统的企业建模，例如工业

automation, transformation, critical infrastructure.

自动化、转型、关键基础设施。

#### F.3.2 Identification of stakeholders and definition of their perspectives 利益相关方的识别及其角度的定义

Some ADFs like Zachman[67] clearly identify typical stakeholders like: Planner, Owner, Designer, Builder, Implementer and User.

某些 ADF（如 Zachman[67]）明确识别典型的利益相关方，例如：策划者、所有者、设计者、建造者、实施者和用户。

Others identify stages in the AD related to a class of typical stakeholders like: The Open Group’s Architecture Framework (TOGAF),[62] with Business Architecture, Information System Architecture and Technology Architecture.

另一些识别 AD 中与某一类典型利益相关方相关的阶段，例如：The Open Group 的架构框架（TOGAF），[62] 以及业务架构、信息系统架构和技术架构。

Others identify stakeholder perspectives like:

还有一些识别利益相关方角度，例如：

- UAF[48] with “domains”: Architecture Management, Strategic, Operational, Services, Personnel,

- UAF[48] 的“域”：架构管理、战略、运营、服务、人员、

Resources, Security, Projects, Standards, and Actual Resources;

资源、安全、项目、标准以及实际资源；

- ArchiMate[61] with “layers”: Strategy, Business, Application, Technology, Physical, Implementation,

- ArchiMate[61] 的“层”：战略、业务、应用、技术、物理、实施、

and Migration;

以及迁移；

- NAF[44] with “subjects of concerns”: concept specification, service specification, logical specification,

- NAF[44] 的“关注主题”：概念规格、服务规格、逻辑规格、

physical resource specification, and architecture meta-data;

物理资源规格以及架构元数据；

- DoDAF[31] with “viewpoints”: Capability, Operational, Services, Systems, Standards, and Data and

- DoDAF[31] 的“视角”：能力、运营、服务、系统、标准以及数据与

Information;

信息；

- GERA (ISO 15704) with “levels of abstraction” or “life cycle phases”: Identity, concept, requirements,

- GERA（ISO 15704）的“抽象层级”或“生存周期阶段”：标识、概念、要求、

preliminary design, detailed design, implementation, operation and decommissioning.

初步设计、详细设计、实施、运行和退役。

#### F.3.3 Definition of aspects 方面体的定义

ADFs organize the properties and features of architecture models and views in various ways, such as:

ADF 以各种方式组织架构模型和架构视图的属性与特征，例如：

- Zachman[67] with “interrogatives”: What, How, Where, Who, Where, Why;

- Zachman[67] 的“疑问词”：什么、如何、何处、谁、何处、为何；

- NAF[44] with “aspects of concerns”: Taxonomy, Structure, Connectivity, Processes, States, Sequences,

- NAF[44] 的“关注方面体”：分类、结构、连通性、过程、状态、序列、

Information, Constraints and Roadmap;

信息、约束和路线图；

- UAF[48] with “model kinds”: Motivation, Taxonomy, Structure, Connectivity, Processes, States,

- UAF[48] 的“模型种类”：动机、分类、结构、连通性、过程、状态、

Sequences, Information, Parameters, Constraints, Roadmap and Traceability.

序列、信息、参数、约束、路线图和追溯。

ADFs attempt to generalize or harmonize multiple particular ADs to offer guidance for creation of new particular cases by specifying generic stakeholder perspectives and generic aspects (see Zachman[67] [66] and others).

ADF 试图对多个特定的 AD 加以泛化或协调，通过规定通用的利益相关方角度和通用方面体，为创建新的特定情形提供指南（见 Zachman[67] [66] 等）。

#### F.3.4 Specification of architecture viewpoint 架构视角规格

An ADF generally specifies architecture viewpoints providing specifications of model kinds to frame typical concerns and to govern the architecture views and ease understanding of the legends.

ADF 通常规定架构视角，给出模型种类的规格，以框定典型关注点、管控架构视图并便于理解图例。

> **EXAMPLE** Reference Model for Open distributed (RM-ODP)[3] defines the following concepts: enterprise, information, computational, engineering and technology viewpoint specifications.

> **示例**：开放分布式处理参考模型（RM-ODP）[3] 定义了下列概念：企业、信息、计算、工程和技术视角规格。

ADFs often utilize one or more structural categories to represent distribution of architecture viewpoints in a two-dimensional grid or matrix. See References [38][63] for example. There are some ADFs, such as GERA (ISO 15704) and SABSA[56], which use three or more categories to convey the complexity of describing architectures.

ADF 常常采用一个或多个结构类别，以二维网格或矩阵的形式表示架构视角的分布。示例参见参考文献 [38][63]。有些 ADF 使用三个或更多类别来传达描述架构的复杂性，如 GERA（ISO 15704）和 SABSA[56]。

#### F.3.5 Specification of formalisms and languages 形式体系与语言的规格

Generally the ADFs define their formalism for constructing models with a metamodel: like DoDAF’s[31] DoDAF Metamodel (DM2), UAF’s[48][48] Domain Metamodel (DMM), and NAF’s[44] metamodel (MM).

一般而言，ADF 用元模型来定义其构建模型的形式体系：如 DoDAF[31] 的 DoDAF 元模型（DM2）、UAF[48][48] 的域元模型（DMM）以及 NAF[44] 的元模型（MM）。

Some of them also provide languages, which can be used to implement the formalism, like:

其中一些还提供可用于实现该形式体系的语言，如：

- UAF[48][48] with its Profile;

- UAF[48][48] 及其概要；

- ArchiMate modelling language[61];

- ArchiMate 建模语言[61]；

- Constructs for enterprise modelling (ISO 19440).

- 企业建模的构造（ISO 19440）。

### F.4 Compliance with ADF requirements 对 ADF 要求的符合性

Currently none of the ADF fully comply with all the requirements itemized in 7.1. Nevertheless, each of the items is addressed by several of the ADF and all these items are considered as necessary in an AD. Consequently, the provisions in 7.1 provide areas for improvement for these frameworks.

目前尚无任何 ADF 完全符合 7.1 中逐条列出的全部要求。然而，这些条目中的每一项都为若干 ADF 所处理，且所有这些条目在 AD 中均被视为必要的。因此，7.1 中的规定为这些框架提供了改进空间。

Table F.1 and Table F.2 show an interpretation of how some of the published ADFs comply with 7.1 requirements.

表 F.1 和表 F.2 给出了对若干已发布 ADF 如何符合 7.1 要求的一种解释。

> **NOTE** In Table F.1 and Table F.2 “Partial” means that the requirement is fulfilled to some degree but is not expressed with explicit wording. “Yes” is used when the requirement is met. “No” states that the requirement is not addressed.

> **注**：在表 F.1 和表 F.2 中，“部分”表示该要求得到一定程度的满足，但未以明确措辞表述。“是”用于表示要求得到满足。“否”表示该要求未被处理。

**Table F.1 — ADF requirements compliance (1/2)**

**表 F.1 — ADF 要求符合性（1/2）**

|  | GERA (ISO 15704) | RM-ODP[2] | Zachman[67] | TOGAF[62] |
| --- | --- | --- | --- | --- |
| Information identifying the ADF ／ 标识 ADF 的信息 | Implementation dependent ／ 依实现而定 | Implementation dependent ／ 依实现而定 | Yes ／ 是 | Yes ／ 是 |
| Stakeholder identification ／ 利益相关方识别 | Organization viewpoint ／ 组织视角 | No ／ 否 | Yes ／ 是 | No ／ 否 |
| Concern identification ／ 关注点识别 | Covered by identification, concept and requirements life cycle phases ／ 由识别、概念和需求生存周期阶段覆盖 | Yes (in Viewpoints) ／ 是（在视角中） | Partial ／ 部分 | Partial ／ 部分 |
| Aspects ／ 方面体 | Aspect-oriented views ／ 面向方面体的架构视图 | No ／ 否 | Called “interrogatives” ／ 称为“疑问词” | No ／ 否 |
| Stakeholder perspectives ／ 利益相关方角度 | Covered by identification, concept and requirements life cycle phases ／ 由识别、概念和需求生存周期阶段覆盖 | No ／ 否 | Yes ／ 是 | Called “phases” ／ 称为“阶段” |
| Formalism ／ 形式体系 | GERAM Metamodel ／ GERAM 元模型 | UML Profile ／ UML 概要 | No ／ 否 | No ／ 否 |
| Architecture Viewpoint ／ 架构视角 | Aspect-oriented viewpoints ／ 面向方面体的视角 | Viewpoint specification or viewpoint language ／ 视角规格或视角语言 | Partial ／ 部分 | No ／ 否 |
| Model kinds ／ 模型种类 | Criteria explained ／ 说明了准则 | One per viewpoint ／ 每个视角一个 | Partial ／ 部分 | Partial ／ 部分 |
| Legends and correspondence methods ／ 图例与对应方法 | Partial ／ 部分 | Formalized ／ 形式化 | Partial ／ 部分 | Partial ／ 部分 |
| Framework methods ／ 框架方法 | GERAM | No ／ 否 | Partial ／ 部分 | TOGAF/ADM |

**Table F.2 — ADF requirements compliance (2/2)**

**表 F.2 — ADF 要求符合性（2/2）**

|  | UAF[48] | NAF[44] | DoDAF[31] | ArchiMate[61] |
| --- | --- | --- | --- | --- |
| Information identifying the ADF ／ 标识 ADF 的信息 | Yes ／ 是 | Yes ／ 是 | Yes ／ 是 | Yes ／ 是 |
| Stakeholder identification ／ 利益相关方识别 | Yes (in view specifications) ／ 是（在视图规格中） | No ／ 否 | No ／ 否 | Yes (as part of the "Motivation Elements") ／ 是（作为 "Motivation Elements" 的一部分） |
| Concern identification ／ 关注点识别 | Yes (in view specifications) ／ 是（在视图规格中） | Partial ／ 部分 | Partial ／ 部分 | Yes (in Viewpoints) ／ 是（在视角中） |

**Table F.2** *(continued)***Table F.2** *(continued)*

**表 F.2** *(续)***表 F.2** *(续)*

|  | UAF[48] | NAF[44] | DoDAF[31] | ArchiMate[61] |
| --- | --- | --- | --- | --- |
| Aspects ／ 方面体 | Called “Model kinds” ／ 称为“模型种类” | Called “Aspects of concerns” ／ 称为“关注点的方面体” | No ／ 否 | Called “Aspects” ／ 称为“方面体” |
| Stakeholder perspectives ／ 利益相关方角度 | Called “domains” ／ 称为“域” | Called “subjects of concerns” ／ 称为“关注点主体” | Called “viewpoints” ／ 称为“视角” | Called “Layers” ／ 称为“层” |
| Formalism ／ 形式体系 | Domain metamodel (DMM) and a Profile ／ 域元模型（DMM）和一个概要 | NAF metamodels ／ NAF 元模型 | DM2 metamodel ／ DM2 元模型 | ArchiMate Specification ／ ArchiMate 规格 |
| Architecture Viewpoint ／ 架构视角 | Called “view specifications” within a Grid ／ 在网格中称为“视图规格” | Called “viewpoints” within a Grid ／ 在网格中称为“视角” | Called “Models” ／ 称为“模型” | Called “viewpoint mechanism” ／ 称为“视角机制” |
| Model kinds ／ 模型种类 | Recommended implementations in UAF Profile’s view specifications ／ UAF 概要的视图规格中推荐的实现 | Partial ／ 部分 | Partial ／ 部分 | ArchiMate Specification ／ ArchiMate 规格 |
| Legends and correspondence methods ／ 图例与对应方法 | Partial ／ 部分 | Partial ／ 部分 | Partial ／ 部分 | Partial ／ 部分 |
| Framework methods ／ 框架方法 | No ／ 否 | NAF Chapter 2 ／ NAF 第 2 章 | 6 Step Approach ／ 6 步方法 | No ／ 否 |

## Bibliography 参考文献

[1] IEEE 1471:2000, *IEEE Recommended Practice for Architectural Description for Software-Intensive* *Systems*

[1] IEEE 1471:2000, *IEEE 软件密集型系统的* *架构描述推荐实践*

[2] ISO/IEC 10746-1, *Information technology — Open Distributed Processing — Reference model:* *Overview — Part 1:*

[2] ISO/IEC 10746-1, *信息技术 — 开放分布式处理 — 参考模型：* *概述 — 第 1 部分：*

[3] ISO/IEC 10746-2, *Information technology — Open distributed processing — Reference model:* *Foundations — Part 2:*

[3] ISO/IEC 10746-2, *信息技术 — 开放分布式处理 — 参考模型：* *基础 — 第 2 部分：*

[4] ISO/IEC 10746-3, *Information technology — Open distributed processing — Reference model:* *Architecture — Part 3:*

[4] ISO/IEC 10746-3, *信息技术 — 开放分布式处理 — 参考模型：* *架构 — 第 3 部分：*

[5] ISO/IEC/IEEE 12207:2017, *Systems and software engineering — Software life cycle processes*

[5] ISO/IEC/IEEE 12207:2017, *系统与软件工程 — 软件生存周期过程*

[6] ISO/IEC/IEEE 15288:2015, *Systems and software engineering — System life cycle processes*

[6] ISO/IEC/IEEE 15288:2015, *系统与软件工程 — 系统生存周期过程*

[7] ISO/IEC/IEEE 15289:2019, *Systems and software engineering — Content of life-cycle information* *items (documentation)*

[7] ISO/IEC/IEEE 15289:2019, *系统与软件工程 — 生存周期信息* *部件（文档）的内容*

[8] ISO/IEC 15414, *Information technology — Open distributed processing — Reference model —* *Enterprise language*

[8] ISO/IEC 15414, *信息技术 — 开放分布式处理 — 参考模型 —* *企业语言*

[9] ISO 15704:2019, *Enterprise modelling and architecture — Requirements for enterprise-referencing* *architectures and methodologies*

[9] ISO 15704:2019, *企业建模与架构 — 对企业参照架构* *与方法论的要求*

[10] ISO 19439:2006, *Enterprise integration — Framework for enterprise modelling*

[10] ISO 19439:2006, *企业集成 — 企业建模框架*

[11] ISO 19440:2020, *Enterprise modelling and architecture — Constructs for enterprise modelling*

[11] ISO 19440:2020, *企业建模与架构 — 企业建模的构造*

[12] ISO/PAS 19450:2015, *Automation systems and integration — Object-Process Methodology*

[12] ISO/PAS 19450:2015, *自动化系统与集成 — 对象-过程方法论*

[13] ISO/IEC 19793:2015, *Information technology — Open Distributed Processing — Use of UML for* *ODP system specifications*

[13] ISO/IEC 19793:2015, *信息技术 — 开放分布式处理 — UML 用于* *ODP 系统规格*

[14] ISO/IEC 20246:2017, *Software and systems engineering — Work product reviews*

[14] ISO/IEC 20246:2017, *软件与系统工程 — 工作产品评审*

[15] ISO/IEC/IEEE 24748-1:2018, *Systems and software engineering — Life cycle management — Part* *1: Guidelines for life cycle management*

[15] ISO/IEC/IEEE 24748-1:2018, *系统与软件工程 — 生存周期管理 —* *第 1 部分：生存周期管理指南*

[16] ISO/IEC/IEEE 24765:2017, *Systems and software engineering — Vocabulary*

[16] ISO/IEC/IEEE 24765:2017, *系统与软件工程 — 词汇*

[17] ISO/IEC 25010:2011, *Systems and software engineering — Systems and software Quality* *Requirements and Evaluation (SQuaRE) — System and software quality models*

[17] ISO/IEC 25010:2011, *系统与软件工程 — 系统与软件质量* *要求和评价（SQuaRE） — 系统与软件质量模型*

[18] ISO/IEC 25012:2008, *Software engineering — Software product Quality Requirements and* *Evaluation (SQuaRE) — Data quality model*

[18] ISO/IEC 25012:2008, *软件工程 — 软件产品质量要求和* *评价（SQuaRE） — 数据质量模型*

[19] ISO/IEC 25024:2015, *Systems and software engineering — Systems and software Quality* *Requirements and Evaluation (SQuaRE) — Measurement of data quality*

[19] ISO/IEC 25024:2015, *系统与软件工程 — 系统与软件质量* *要求和评价（SQuaRE） — 数据质量的测量*

[20] ISO/IEC 33001:2015, *Information technology — Process assessment — Concepts and terminology*

[20] ISO/IEC 33001:2015, *信息技术 — 过程评定 — 概念和术语*

[21] ISO/IEC TS 33060:2020, *Information technology — Process assessment — Process assessment* *model for system life cycle processes*

[21] ISO/IEC TS 33060:2020, *信息技术 — 过程评定 —* *系统生存周期过程的过程评定模型*

[22] ISO/IEC/IEEE 42010:2011, *Systems and software engineering — Architecture description*

[22] ISO/IEC/IEEE 42010:2011, *系统与软件工程 — 架构描述*

[23] ISO/IEC/IEEE 42020:2019, *Software, systems and enterprise — Architecture processes*

[23] ISO/IEC/IEEE 42020:2019, *软件、系统与企业 — 架构过程*

[24] ISO/IEC/IEEE 42030:2019, *Software, systems and enterprise — Architecture evaluation framework*

[24] ISO/IEC/IEEE 42030:2019, *软件、系统与企业 — 架构评估框架*

[25] Atkinson C., Gerbig R., Tunjic C., “A multi-level modelling environment for SUM-based software engineering”, Proceedings of the 1st Workshop on View-Based, Aspect-Oriented and Orthographic Software Modelling (VAO '13), ACM Press, 2013

[25] Atkinson C., Gerbig R., Tunjic C., “基于 SUM 的软件工程的多级建模环境”，《第一届基于视图、面向方面与正交软件建模研讨会（VAO '13）论文集》，ACM Press，2013

[26] Boucké N., Composition and relations of architectural models supported by an architectural description language. Doctoral dissertation, Katholieke Universiteit Leuven, October 2009

[26] Boucké N.，由架构描述语言支持的架构模型的组合与关系。博士论文，鲁汶天主教大学，2009 年 10 月

[27] Callo-Arias T.B., America P., Avgeriou P., “Defining execution viewpoints for a large and complex software-intensive system”, Proceedings of WICSA/ECSA 2009

[27] Callo-Arias T.B., America P., Avgeriou P., “为大型复杂软件密集型系统定义执行视角”，WICSA/ECSA 2009 论文集

[28] Clements P., Bachmann F., Bass L., Garlan D., Ivers J., Little R. et al., Documenting Software Architectures: Views and Beyond. Addison-Wesley, Boston, 2002

[28] Clements P., Bachmann F., Bass L., Garlan D., Ivers J., Little R. 等，软件架构编档：视图与超越。Addison-Wesley，Boston，2002

[29] Darnton G., Giacoletto S., Information in the Enterprise. Digital Press, Burlington, MA, 1992

[29] Darnton G., Giacoletto S.，企业中的信息。Digital Press，Burlington, MA，1992

[30] Dijkstra E.W., On the role of scientific thought. 1974. https:// www .cs .utexas .edu/ users/ EWD/ transcriptions/ EWD04xx/ EWD447 .html

[30] Dijkstra E.W.，论科学思想的作用。1974. https:// www .cs .utexas .edu/ users/ EWD/ transcriptions/ EWD04xx/ EWD447 .html

[31] DoD Architecture Framework, version 2.02, https:// dodcio .defense .gov/ library/ dod -architecture -framework/

[31] DoD 架构框架，版本 2.02，https:// dodcio .defense .gov/ library/ dod -architecture -framework/

[32] Eeles P., Cripps P., The Process of Software Architecting. Addison Wesley, 2010

[32] Eeles P., Cripps P.，软件架构工作过程. Addison Wesley, 2010

[33] Garlan D., Monroe R.T., Wile D., ACME: An Architecture Description Interchange, Proceedings of the 1997 conference of the Centre for Advanced Studies on Collaborative research, 7-22.

[33] Garlan D., Monroe R.T., Wile D.，ACME：一种架构描述交换，1997 年协作研究高级研究中心会议论文集，7-22.

[34] Heidel R., The Reference Architecture Model RAMI 4.0 and the Industrie 4.0 component, 2019

[34] Heidel R.，参考架构模型 RAMI 4.0 与工业 4.0 组件，2019

[35] Hilliard R., “Viewpoint modelling”, First ICSE Workshop on Describing Software Architecture with UML, May 2001

[35] Hilliard R.，“视角建模”，第一届 ICSE 用 UML 描述软件架构研讨会，2001 年 5 月

[36] Industrial Internet Architecture Framework https:// www .iiconsortium .org/

[36] 工业互联网架构框架 https:// www .iiconsortium .org/

[37] Magee J., Kramer J., Dynamic structure in software architectures, ACM SIGSOFT Foundations of Software Engineering (FSE), pages 3-14, 1996, Conference Sa Francisco CA October 16-18, 1996

[37] Magee J., Kramer J.，软件架构中的动态结构，ACM SIGSOFT 软件工程基础会议（FSE），第 3-14 页，1996，会议于 1996 年 10 月 16-18 日在加州旧金山举行

[38] Josey A, Lankhorst M, Band I, Jonkers H, Quartel D., “An Introduction to the ArchiMate® 3.0 Specification”, June 2016

[38] Josey A, Lankhorst M, Band I, Jonkers H, Quartel D.，“ArchiMate® 3.0 规格介绍”，2016 年 6 月

[39] Kiczales G., Lamping J., Menhdhekar A., Maeda C., Lopes C., Loingtier J.M. et al., Aspect-oriented programming. In Akșit, M., Matsuoka, S., eds.: Proceedings European Conference on Object-Oriented Programming. Volume 1241. Springer-Verlag, Berlin, Heidelberg, and New York (1997) 220–242

[39] Kiczales G., Lamping J., Menhdhekar A., Maeda C., Lopes C., Loingtier J.M. 等，面向方面编程。载于 Akșit, M., Matsuoka, S. 编：欧洲面向对象编程会议论文集。第 1241 卷。Springer-Verlag，柏林、海德堡和纽约(1997)220–242

[40] Kruchten P.B., The ‘4+1’ View Model of Architecture. IEEE Softw. 1995, **12** (6) pp. 45–50

[40] Kruchten P.B.，架构的“4+1”视图模型。IEEE Softw. 1995，**12** (6) 第 45–50 页

[41] Luckham D.C., Kenney J.J., Augustin L.M., Vera J., Bryan D., Mann W., Specification and analysis of system architecture using Rapide. IEEE Trans. Softw. Eng. 1995 April, **21** (4) pp. 336– 355

[41] Luckham D.C., Kenney J.J., Augustin L.M., Vera J., Bryan D., Mann W.，使用 Rapide 的系统架构规格与分析。IEEE Trans. Softw. Eng. 1995 年 4 月，**21** (4) 第 336–355 页

[42] Muskens J., Bril R.J., Chaudron M.R.V., “Generalizing consistency checking between software views”, Proceedings of the 5th Working IEEE/IFIP Conference on Software Architecture (WICSA’05), 169–180, Washington, DC: IEEE Computer Society, 2005

[42] Muskens J., Bril R.J., Chaudron M.R.V.，“推广软件视图之间的一致性检查”，第 5 届 IEEE/IFIP 软件架构工作会议论文集（WICSA’05），169–180，华盛顿特区：IEEE Computer Society，2005

[43] Nuseibeh B., Kramer J., Finkelstein A., A framework for expressing the relationships between multiple views in requirements specification. IEEE Trans. Softw. Eng. 1994, **20** (10) pp. 760–773

[43] Nuseibeh B., Kramer J., Finkelstein A.，用于表达需求规格中多个视图之间关系的框架。IEEE Trans. Softw. Eng. 1994，**20** (10) 第 760–773 页

[44] NATO. Architecture Framework version 4, https:// www .nato .int/ cps/ en/ natohq/ topics _157575 .htm

[44] NATO。架构框架第 4 版，https:// www .nato .int/ cps/ en/ natohq/ topics _157575 .htm

[45] OASIS, Reference Architecture Foundation for Service Oriented Architecture Version 1.0

[45] OASIS，面向服务的架构参考架构基础 1.0 版

[46] OMG Business Process Model and Notation (BPMN™), https:// www .omg .org/ spec/ BPMN/ About -BPMN/

[46] OMG 业务流程模型与记号（BPMN™），https:// www .omg .org/ spec/ BPMN/ About -BPMN/

[47] Systems Modelling Language Object Management Group https:// www .omg .org/ spec/ SysML/ About -SysML/

[47] 系统建模语言，对象管理组 https:// www .omg .org/ spec/ SysML/ About -SysML/

[48] Unified Architecture Framework Object Management Group https:// www .omg .org/ spec/ UAF/ About -UAF/

[48] 统一架构框架，对象管理组 https:// www .omg .org/ spec/ UAF/ About -UAF/

[49] Unified Modelling Language Object Management Group , (UML®), https:// www .omg .org/ spec/ UML/ About -UML/

[49] 统一建模语言，对象管理组，（UML®），https:// www .omg .org/ spec/ UML/ About -UML/

[50] OMG UML Profile for DoDAF/MODAF https:// www .omg .org/ updm/

[50] OMG 用于 DoDAF/MODAF 的 UML 概要 https:// www .omg .org/ updm/

[51] Bernus Peter, *Richard Martin, Ovidiu Noran, and Arturo Molina. IFIP WG5.12 Architectures for* *Enterprise Integration: Twenty-Five Years of the GERAM Framework*, in Goedicke M. et al., (Eds.): Advancing Research in Information and Communication Technology, IFIP AICT 600, pp. 1–24, 2021. https:// doi .org/ 10 .1007/ 978 -3 -030 -81701 -5 _10

[51] Bernus Peter, *Richard Martin, Ovidiu Noran, and Arturo Molina. IFIP WG5.12 面向* *企业集成的架构：GERAM 框架二十五年*，载于 Goedicke M. 等编：推进信息与通信技术研究，IFIP AICT 600，第 1–24 页，2021。https:// doi .org/ 10 .1007/ 978 -3 -030 -81701 -5 _10

[52] Ran A., “*ARES Conceptual Framework for Software Architecture*”, M. Jazayeri, A. Ran, and F. van der Linden (eds.), Software Architecture for Product Families Principles and Practice, Boston: Addison-Wesley, 1–29, 2000

[52] Ran A.，“*软件架构的 ARES 概念框架*”，M. Jazayeri, A. Ran, and F. van der Linden 编，产品族的软件架构：原理与实践，Boston: Addison-Wesley，1–29，2000

[53] Ross D.T., Structured Analysis (SA): a language for communicating ideas. IEEE Trans. Softw. Eng. 1977, **SE-3** (1) pp. 16–34

[53] Ross D.T.，结构化分析（SA）：一种用于交流思想的语言。IEEE Trans. Softw. Eng. 1977，**SE-3** (1) 第 16–34 页

[54] Rozanski N., Woods E., Software Systems Architecture: Working with Stakeholders Using Viewpoints and Perspectives. Addison-Wesley, 2005

[54] Rozanski N., Woods E.，软件系统架构：运用视角与透视同利益相关方协作。Addison-Wesley，2005

[55] Sabetzadeh M., Finkelstein A., Goedicke M., “Viewpoints”, P. Laplante (ed.), Encyclopedia of Software Engineering, Taylor and Francis, 2010

[55] Sabetzadeh M., Finkelstein A., Goedicke M.，“视角”，P. Laplante 编，软件工程百科全书，Taylor and Francis，2010

[56] SABSA Institute Resource, The SABSA White Paper, W100, Published 2009

[56] SABSA 研究院资源，SABSA 白皮书，W100，2009 年出版

[57] Society of Automotive Engineers, Architecture Analysis & Design Language, http:// www .aadl .info/

[57] 汽车工程师学会，架构分析与设计语言，http:// www .aadl .info/

[58] Shaw M., Prospects for an engineering discipline of software. IEEE Softw. 1990 November

[58] Shaw M.，软件工程学科的前景。IEEE Softw. 1990 年 11 月

[59] Smolander K., “Four Metaphors of Architecture in Software Organizations: Finding out The Meaning of Architecture in Practice”, Proceedings of the 2002 International Symposium on Empirical Software Engineering (ISESE’02)

[59] Smolander K.，“软件组织中架构的四种隐喻：在实践中探究架构的含义”，2002 年国际经验软件工程研讨会论文集（ISESE’02）

[60] ISO/IEC/IEEE 31320-1:2012, *Information technology — Modeling Languages — Part 1: Syntax and* *Semantics for IDEF0*

[60] ISO/IEC/IEEE 31320-1:2012，*信息技术 — 建模语言 — 第 1 部分：IDEF0 的语法与* *语义*

[61] The Open Group, ArchiMate Specification, https:// www .opengroup .org/ archimate -forum/ archimate -overview

[61] The Open Group，ArchiMate 规格，https:// www .opengroup .org/ archimate -forum/ archimate -overview

[62] The Open Group Architecture Framework (TOGAF) https:// www .opengroup .org/ togaf/

[62] The Open Group 架构框架（TOGAF） https:// www .opengroup .org/ togaf/

[63] Unified Architecture Method (UAM) https:// www .unified -am .com/ UAM/ index .htm

[63] 统一架构方法（UAM） https:// www .unified -am .com/ UAM/ index .htm

[64] Viewpoints Repository for ISO/IEC/IEEE 42010, http:// www .iso -architecture .org/ viewpoints/

[64] ISO/IEC/IEEE 42010 视角库，http:// www .iso -architecture .org/ viewpoints/

[65] Wright ADL website, http:// www .cs .cmu .edu/ ~able/ wright/

[65] Wright ADL 网站，http:// www .cs .cmu .edu/ ~able/ wright/

[66] XP Z67-140 Information Technology –ARCADIA– Method for Systems Engineering supported by its conceptual modelling language –General Description– Specification of the engineering definition method and the modelling language, AFNOR

[66] XP Z67-140 信息技术 –ARCADIA– 由其概念建模语言支撑的系统工程方法 –总述– 工程定义方法与建模语言的规格，AFNOR

[67] Zachman J.A., A Framework for Information Systems Architecture. IBM Syst. J. 1987, **26** (3)

[67] Zachman J.A.，信息系统架构框架。IBM Syst. J. 1987，**26** (3)

## IEEE Notices and Abstract IEEE 通告与摘要

**Important Notices and Disclaimers Concerning IEEE Standards Documents**

**关于 IEEE 标准文件的重要通告与免责声明**

IEEE Standards documents are made available for use subject to important notices and legal disclaimers. These notices and disclaimers, or a reference to this page (https:// standards .ieee .org/ ipr/ disclaimers .html), appear in all standards and may be found under the heading “Important Notices and Disclaimers Concerning IEEE Standards Documents.”

IEEE 标准文件在提供使用时，须遵守重要通告与法律免责声明。这些通告与免责声明，或对本页（https:// standards .ieee .org/ ipr/ disclaimers .html）的引用，出现在所有标准中，并可在“关于 IEEE 标准文件的重要通告与免责声明”这一标题下查到。

**Notice and Disclaimer of Liability Concerning the Use of IEEE Standards Documents**

**关于使用 IEEE 标准文件的责任通告与免责声明**

IEEE Standards documents are developed within the IEEE Societies and the Standards Coordinating Committees of the IEEE Standards Association (IEEE SA) Standards Board. IEEE develops its standards through an accredited consensus development process, which brings together volunteers representing varied viewpoints and interests to achieve the final product. IEEE Standards are documents developed by volunteers with scientific, academic, and industry-based expertise in technical working groups. Volunteers are not necessarily members of IEEE or IEEE SA, and participate without compensation from IEEE. While IEEE administers the process and establishes rules to promote fairness in the consensus development process, IEEE does not independently evaluate, test, or verify the accuracy of any of the information or the soundness of any judgments contained in its standards.

IEEE 标准文件由 IEEE 各学会以及 IEEE 标准协会（IEEE SA）标准委员会的各标准协调委员会制定。IEEE 通过经认可的共识制定过程制定其标准，该过程汇聚代表不同观点与利益的志愿者，以形成最终成果。IEEE 标准是由具备科学、学术和产业专长的志愿者在技术工作组中制定的文件。志愿者不一定是 IEEE 或 IEEE SA 的成员，且不因参与而从 IEEE 获得报酬。尽管 IEEE 管理该过程并制定规则以促进共识制定过程的公正性，但 IEEE 不独立评估、测试或验证其标准中所含任何信息的准确性，也不验证其中任何判断的可靠性。

IEEE does not warrant or represent the accuracy or completeness of the material contained in its standards, and expressly disclaims all warranties (express, implied and statutory) not included in this or any other document relating to the standard, including, but not limited to, the warranties of: merchantability; fitness for a particular purpose; non-infringement; and quality, accuracy, effectiveness, currency, or completeness of material. In addition, IEEE disclaims any and all conditions relating to results and workmanlike effort. In addition, IEEE does not warrant or represent that the use of the material contained in its standards is free from patent infringement. IEEE Standards documents are supplied “AS IS” and “WITH ALL FAULTS.”

IEEE 不担保也不声明其标准中所含材料的准确性或完整性，并明确否认本文件或与标准有关的任何其他文件中未包含的一切担保（明示、默示和法定担保），包括但不限于以下担保：可销售性；特定用途适用性；不侵权；以及材料的质量、准确性、有效性、时效性或完整性。此外，IEEE 否认与结果和专业水准努力有关的一切条件。此外，IEEE 不担保也不声明使用其标准中所含材料不会侵犯专利权。IEEE 标准文件按“现状”与“含全部瑕疵”提供。

Use of an IEEE standard is wholly voluntary. The existence of an IEEE Standard does not imply that there are no other ways to produce, test, measure, purchase, market, or provide other goods and services related to the scope of the IEEE standard. Furthermore, the viewpoint expressed at the time a standard is approved and issued is subject to change brought about through developments in the state of the art and comments received from users of the standard.

使用 IEEE 标准完全出于自愿。IEEE 标准的存在，并不意味着不存在其他方式来生产、试验、测量、采购、营销或提供与该 IEEE 标准范围有关的其他货物和服务。此外，标准在批准和发布之时所表达的观点，会随技术发展水平的进展以及标准用户提出的意见而变化。

In publishing and making its standards available, IEEE is not suggesting or rendering professional or other services for, or on behalf of, any person or entity, nor is IEEE undertaking to perform any duty owed by any other person or entity to another. Any person utilizing any IEEE Standards document, should rely upon his or her own independent judgment in the exercise of reasonable care in any given circumstances or, as appropriate, seek the advice of a competent professional in determining the appropriateness of a given IEEE standard.

IEEE 在出版并提供其标准时，并非为任何人或实体、亦非代表任何人或实体提议或提供专业服务或其他服务，IEEE 也不承诺履行任何其他人或实体对他人所负的任何义务。任何使用任何 IEEE 标准文件的人，均应在任何特定情形下尽到合理注意，依靠其自身的独立判断；或在适当情况下，就某一给定 IEEE 标准是否适当征询有能力的专业人员的意见。

IN NO EVENT SHALL IEEE BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO: THE NEED TO PROCURE SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE PUBLICATION, USE OF, OR RELIANCE UPON ANY STANDARD, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE AND REGARDLESS OF WHETHER SUCH DAMAGE WAS FORESEEABLE.

在任何情况下，IEEE 均不对任何直接、间接、偶发、特殊、惩戒性或后果性损害（包括但不限于：为获取替代货物或服务之需要；使用、数据或利润的损失；业务中断）承担任何责任，无论损害因何引起，也无论基于何种责任理论，无论是以合同、严格责任还是侵权（包括过失或其他）为由，只要是以任何方式产生于任何标准的出版、使用或依赖，即使已被告知发生此类损害的可能性，且无论此类损害是否可预见。

**Translations**

**翻译**

The IEEE consensus development process involves the review of documents in English only. In the event that an IEEE standard is translated, only the English version published by IEEE is the approved IEEE standard.

IEEE 的共识制定过程仅涉及对英文文件的审查。若 IEEE 标准被翻译，则只有 IEEE 出版的英文版本是经批准的 IEEE 标准。

**Official statements**

**正式声明**

A statement, written or oral, that is not processed in accordance with the IEEE SA Standards Board Operations Manual shall not be considered or inferred to be the official position of IEEE or any of its committees and shall not be considered to be, nor be relied upon as, a formal position of IEEE. At lectures, symposia, seminars, or educational courses, an individual presenting information on IEEE standards shall make it clear that the presenter’s views should be considered the personal views of that individual rather than the formal position of IEEE, IEEE SA, the Standards Committee, or the Working Group.

未按照 IEEE SA 标准委员会操作手册处理的书面或口头声明，不应被视为或推断为 IEEE 或其任何委员会的官方立场，也不应被视为或被作为 IEEE 的正式立场而加以依赖。在讲座、专题研讨会、研讨会或教育课程中，介绍 IEEE 标准相关信息的个人应明确说明：演讲人的观点应视为该个人的个人观点，而非 IEEE、IEEE SA、标准委员会或工作组的正式立场。

**Comments on standards**

**对标准的评论**

**IEEE does not provide interpretations, consulting information, or advice pertaining to IEEE** **Standards documents**

**IEEE 不提供与 IEEE** **标准文件有关的解释、咨询信息或建议**

Suggestions for changes in documents should be in the form of a proposed change of text, together with appropriate supporting comments. Since IEEE standards represent a consensus of concerned interests, it is important that any responses to comments and questions also receive the concurrence of a balance of interests. For this reason, IEEE and the members of its Societies and Standards Coordinating Committees are not able to provide an instant response to comments, or questions except in those cases where the matter has previously been addressed. For the same reason, IEEE does not respond to interpretation requests. Any person who would like to participate in evaluating comments or in revisions to an IEEE standard is welcome to join the relevant IEEE working group. You can indicate interest in a working group using the Interests tab in the Manage Profile & Interests area of the IEEE SA myProject system. An IEEE Account is needed to access the application.

对文件的修改建议宜以拟议的文本修改形式提出，并附上适当的支持性意见。由于 IEEE 标准代表有关利益方的共识，因此对评论和问题的任何答复也须获得各利益方均衡的认同，这一点很重要。为此，对于评论或问题，IEEE 及其协会和标准协调委员会的成员无法即时作出答复，除非该事项此前已经处理过。基于同样理由，IEEE 不答复解释请求。任何希望参与评论评审或参与 IEEE 标准修订的人士，均欢迎加入相关的 IEEE 工作组。您可使用 IEEE SA myProject 系统的“管理简档与兴趣”区域中的“兴趣”选项卡，表明对某一工作组的兴趣。访问该应用程序需要一个 IEEE 账户。

Comments on standards should be submitted using the Contact Us form.

对标准的评论宜使用“联系我们”表单提交。

**Laws and regulations**

**法律和法规**

Users of IEEE Standards documents should consult all applicable laws and regulations. Compliance with the provisions of any IEEE Standards document does not constitute compliance to any applicable regulatory requirements. Implementers of the standard are responsible for observing or referring to the applicable regulatory requirements. IEEE does not, by the publication of its standards, intend to urge action that is not in compliance with applicable laws, and these documents may not be construed as doing so.

IEEE 标准文件的使用者宜查阅所有适用的法律和法规。符合任何 IEEE 标准文件的条款，并不构成符合任何适用的法规要求。标准的实施者有责任遵守或援引适用的法规要求。IEEE 出版其标准，无意鼓动不符合适用法律的行动，且这些文件不得被解释为鼓动此类行动。

**Data privacy**

**数据隐私**

Users of IEEE Standards documents should evaluate the standards for considerations of data privacy and data ownership in the context of assessing and using the standards in compliance with applicable laws and regulations.

IEEE 标准文件的使用者在依照适用法律和法规评定和使用这些标准时，宜从数据隐私和数据所有权的考量出发对这些标准进行评估。

**Copyrights**

**版权**

IEEE draft and approved standards are copyrighted by IEEE under US and international copyright laws. They are made available by IEEE and are adopted for a wide variety of both public and private uses. These include both use, by reference, in laws and regulations, and use in private self-regulation, standardization, and the promotion of engineering practices and methods. By making these documents available for use and adoption by public authorities and private users, IEEE does not waive any rights in copyright to the documents.

IEEE 草案标准和已批准标准由 IEEE 依据美国和国际版权法享有版权。它们由 IEEE 提供，并被公共和私人领域的各种用途所采用。这些用途既包括在法律法规中通过引用而使用，也包括在私人自我规制、标准化以及工程实践与方法的推广中使用。IEEE 使这些文件可供公共机构和私人用户使用和采用，并不因此放弃对这些文件的任何版权权利。

**Photocopies**

**影印**

Subject to payment of the appropriate licensing fees, IEEE will grant users a limited, non-exclusive license to photocopy portions of any individual standard for company or organizational internal use or individual, non-commercial use only. To arrange for payment of licensing fees, please contact Copyright Clearance Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA; +1 978 750 8400; https:// www .copyright .com/ . Permission to photocopy portions of any individual standard for educational classroom use can also be obtained through the Copyright Clearance Center.

在支付相应许可费的前提下，IEEE 将授予使用者一项有限的、非排他的许可，仅为公司或组织内部使用或个人非商业使用而影印任何单项标准的部分内容。为安排支付许可费，请联系 Copyright Clearance Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA；+1 978 750 8400；https:// www .copyright .com/ 。为教育课堂教学使用而影印任何单项标准部分内容的许可，也可通过 Copyright Clearance Center 获得。

**Updating of IEEE Standards documents**

**IEEE 标准文件的更新**

Users of IEEE Standards documents should be aware that these documents may be superseded at any time by the issuance of new editions or may be amended from time to time through the issuance of amendments, corrigenda, or errata. An official IEEE document at any point in time consists of the current edition of the document together with any amendments, corrigenda, or errata then in effect.

IEEE 标准文件的使用者宜注意，这些文件可随时因新版标准的发布而被取代，也可不时通过发布修改件、勘误表或正误表而得到修订。在任何时点，一份正式的 IEEE 文件由该文件的现行版本连同届时有效的任何修改件、勘误表或正误表构成。

Every IEEE standard is subjected to review at least every 10 years. When a document is more than 10 years old and has not undergone a revision process, it is reasonable to conclude that its contents, although still of some value, do not wholly reflect the present state of the art. Users are cautioned to check to determine that they have the latest edition of any IEEE standard.

每项 IEEE 标准至少每 10 年接受一次审查。当一份文件已超过 10 年且未经历修订过程时，可以合理认定：其内容虽仍有一定价值，但并未完全反映当前的技术发展水平。提请使用者注意核查，以确定其持有任何 IEEE 标准的最新版本。

In order to determine whether a given document is the current edition and whether it has been amended through the issuance of amendments, corrigenda, or errata, visit IEEE Xplore or contact IEEE. For more information about the IEEE SA or IEEE’s standards development process, visit the IEEE SA Website.

为确定某一给定文件是否为现行版本，以及是否已通过发布修改件、勘误表或正误表而得到修订，请访问 IEEE Xplore 或联系 IEEE。有关 IEEE SA 或 IEEE 标准制定过程的更多信息，请访问 IEEE SA 网站。

**Errata**

**正误表**

Errata, if any, for all IEEE standards can be accessed on the IEEE SA Website. Search for standard number and year of approval to access the web page of the published standard. Errata links are located under the Additional Resources Details section. Errata are also available in IEEE Xplore. Users are encouraged to periodically check for errata.

所有 IEEE 标准的正误表（如有）均可在 IEEE SA 网站上查阅。搜索标准编号和批准年份即可访问已发布标准的网页。正误表链接位于“附加资源详细信息”部分之下。正误表也可在 IEEE Xplore 中获取。鼓励使用者定期核查正误表。

**Patents**

**专利**

IEEE Standards are developed in compliance with the IEEE SA Patent Policy.

IEEE 标准依据 IEEE SA 专利政策制定。

**IMPORTANT NOTICE**

**重要通告**

IEEE Standards do not guarantee or ensure safety, security, health, or environmental protection, or ensure against interference with or from other devices or networks. IEEE Standards development activities consider research and information presented to the standards development group in developing any safety recommendations. Other information about safety practices, changes in technology or technology implementation, or impact by peripheral systems also may be pertinent to safety considerations during implementation of the standard. Implementers and users of IEEE Standards documents are responsible for determining and complying with all appropriate safety, security, environmental, health, and interference protection practices and all applicable laws and regulations.

IEEE 标准不担保也不确保安全、信息安全、健康或环境保护，也不确保免于与其他设备或网络相互干扰。IEEE 标准的制定活动在形成任何安全建议时，会考虑提交给标准制定工作组的研究与信息。关于安全实践、技术或技术实现的变化、或外围系统影响的其他信息，也可能与本标准实施期间的安全考虑相关。IEEE 标准文件的实施者和使用者负责确定并遵守所有适当的安全、信息安全、环境、健康和干扰防护实践，以及所有适用的法律和法规。

**Abstract** ISO/IEC/IEEE 42010:2022 addresses the creation, analysis and sustainment of architectures of entities through the use of architecture description work products. A conceptual model for architecture description is established. Architecture viewpoint, stakeholder perspectives, architecture aspects, model kinds, architecture description frameworks and architecture description languages are introduced for codifying conventions and common practices of architecture description. The required content is specified for architecture descriptions, architecture viewpoints, architecture description frameworks, architecture description languages, and model kinds. Annexes provide the motivation and background for key concepts and terminology and examples of applying ISO/IEC/IEEE 42010:2022.

**摘要**ISO/IEC/IEEE 42010:2022 论述如何通过使用架构描述工作产品来创建、分析和维持各实体的架构。确立了架构描述的概念模型。引入架构视角、利益相关方角度、架构方面体、模型种类、架构描述框架和架构描述语言，用以将架构描述的约定和通行做法成文。规定了架构描述、架构视角、架构描述框架、架构描述语言和模型种类的所要求内容。各附录给出关键概念和术语的动因与背景，以及应用 ISO/IEC/IEEE 42010:2022 的示例。

**Keywords**: architecture description, architecture view, architecture viewpoint, architecture view component, architecture description framework, architecture description language, architecture decision, architecture rationale, architecture consideration, concern, architecture aspect, stakeholder perspective, model kind, correspondence, correspondence method.

**关键词**: 架构描述、架构视图、架构视角、架构视图组件、架构描述框架、架构描述语言、架构决策、架构理由、架构考量因素、关注点、架构方面体、利益相关方角度、模型种类、对应关系、对应方法。

#### ICS 35.080 ISBN 978-1-5044-9155-6 STD25753 (PDF); 978-1-5044-9156-3 STDPD25753 (Print) ICS 35.080 ISBN 978-1-5044-9155-6 STD25753（PDF）；978-1-5044-9156-3 STDPD25753（印刷版）
