# ISO/IEC/IEEE 15288:2023《系统与软件工程 — 系统生存周期过程》中英文对照版

> **本文件性质**：`ISO IEC IEEE 15288 2023.md` 的**逐段中英对照译本**。英文为源文（原文照录），中文为译文，置于对应英文段落之下。

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
本文件由 `ISO IEC IEEE 15288 2023.pdf` 自动转换生成，正文为**英文原文照录**，未作翻译或改写。
- **条款号**：一律保留印刷条款号（`1`、`6.4.1`、`A.1`、`D.5`…）；标题层级**按条款号的级数还原**（1→三级、6.1→四级、6.4.1→五级；附录 A.1→三级、A.2.1→四级），不按字号——同一层级的字号在源件里并不统一。
- **插图**：源 PDF 的图为矢量轮廓（文字不在文本层），故按图区渲染为 PNG，存于同名 `.assets/` 目录，在原文位置以 `![Figure …](…)` 引用。
- **表格**：按 `find_tables` 检出结果转 Markdown 表；跨页表在源件中被版面切段，转换后仍分段呈现。
- **目录**：原印刷目录为点线制表符且页码不可靠，已替换为按标题层级生成的 Markdown 目录。
- **页眉页脚**（`ISO/IEC/IEEE 15288:2023(E)`、版权行、页码）为版面构件，未收入正文。
- **断行连字符**已还原，固有连字符保留。
- **段落切分**：源 PDF 在部分页/栏交界处把**一句话切成两段**（转为 Markdown 后仍分段呈现，与另两份标准的英文 MD 同一处理）；文字未增删，覆盖面校验可证。
- **封面与版权页**照录于正文之前，未作标题化处理。

---

## 目录（Contents）

  - [Cover and copyright pages (source lay-out, verbatim) 封面与版权页（源版式，逐字照录）](#cover-and-copyright-pages-source-lay-out-verbatim-封面与版权页源版式逐字照录)
  - [Foreword 前言](#foreword-前言)
  - [Introduction 引言](#introduction-引言)
  - [Systems and software engineering — System life cycle processes 系统与软件工程——系统生存周期过程](#systems-and-software-engineering-system-life-cycle-processes-系统与软件工程系统生存周期过程)
    - [1 Scope 范围](#1-scope-范围)
    - [2 Normative references 规范性引用文件](#2-normative-references-规范性引用文件)
    - [3 Terms, definitions, and abbreviated terms 术语、定义和缩略语](#3-terms-definitions-and-abbreviated-terms-术语定义和缩略语)
      - [3.1 acquirer 获取方](#31-acquirer-获取方)
      - [3.2 acquisition 获取](#32-acquisition-获取)
      - [3.3 activity 活动](#33-activity-活动)
      - [3.4 agreement 协议](#34-agreement-协议)
      - [3.5 architecture 架构](#35-architecture-架构)
      - [3.6 artefact 人工制品](#36-artefact-人工制品)
      - [3.7 audit 审核](#37-audit-审核)
      - [3.8 baseline 基线](#38-baseline-基线)
      - [3.9 concept of operations 运行构想](#39-concept-of-operations-运行构想)
      - [3.10 concern 关注点](#310-concern-关注点)
      - [3.11 configuration item 配置项](#311-configuration-item-配置项)
      - [3.12 customer 顾客](#312-customer-顾客)
      - [3.13 design, noun 设计，名词](#313-design-noun-设计名词)
      - [3.14 design characteristics 设计特征](#314-design-characteristics-设计特征)
      - [3.15 enabling system 使能系统](#315-enabling-system-使能系统)
      - [3.16 environment 环境](#316-environment-环境)
      - [3.17 incident 事件](#317-incident-事件)
      - [3.18 information item 信息部件](#318-information-item-信息部件)
      - [3.19 interface 接口](#319-interface-接口)
      - [3.20 interoperating system 互操作系统](#320-interoperating-system-互操作系统)
      - [3.21 life cycle 生存周期](#321-life-cycle-生存周期)
      - [3.22 life cycle model 生存周期模型](#322-life-cycle-model-生存周期模型)
      - [3.23 operational concept 运行概念](#323-operational-concept-运行概念)
      - [3.24 operator 操作者](#324-operator-操作者)
      - [3.25 organization 组织](#325-organization-组织)
      - [3.26 problem 问题](#326-problem-问题)
      - [3.27 process 过程](#327-process-过程)
      - [3.28 iteration 迭代](#328-iteration-迭代)
      - [3.29 process purpose 过程目的](#329-process-purpose-过程目的)
      - [3.30 process outcome 过程结果](#330-process-outcome-过程结果)
      - [3.31 recursion 递归](#331-recursion-递归)
      - [3.32 product 产品](#332-product-产品)
      - [3.33 project 项目](#333-project-项目)
      - [3.34 quality assurance / QA ｜ 质量保证 / QA](#334-quality-assurance-qa-质量保证-qa)
      - [3.35 quality characteristic 质量特性](#335-quality-characteristic-质量特性)
      - [3.36 requirement 要求](#336-requirement-要求)
      - [3.37 resource 资源](#337-resource-资源)
      - [3.38 retirement 退役](#338-retirement-退役)
      - [3.39 risk 风险](#339-risk-风险)
      - [3.40 safety 安全性](#340-safety-安全性)
      - [3.41 security 安全](#341-security-安全)
      - [3.42 service 服务](#342-service-服务)
      - [3.43 stage 阶段](#343-stage-阶段)
      - [3.44 stakeholder 利益相关方](#344-stakeholder-利益相关方)
      - [3.45 supplier 供应方](#345-supplier-供应方)
      - [3.46 system 系统](#346-system-系统)
      - [3.47 system element 系统元素](#347-system-element-系统元素)
      - [3.48 system-of-interest / SoI ｜ 系统关注 / SoI](#348-system-of-interest-soi-系统关注-soi)
      - [3.49 system of systems / SoS ｜ 系统的系统 / SoS](#349-system-of-systems-sos-系统的系统-sos)
      - [3.50 systems engineering 系统工程](#350-systems-engineering-系统工程)
      - [3.51 task 任务](#351-task-任务)
      - [3.52 traceability 可追溯性](#352-traceability-可追溯性)
      - [3.53 user 用户](#353-user-用户)
      - [3.54 validation 确认](#354-validation-确认)
      - [3.55 verification 验证](#355-verification-验证)
      - [3.56 view 视图](#356-view-视图)
      - [3.57 viewpoint 视角](#357-viewpoint-视角)
    - [4 Conformance 符合性](#4-conformance-符合性)
      - [4.1 Intended usage 预期用途](#41-intended-usage-预期用途)
      - [4.2 Full conformance 完全符合性](#42-full-conformance-完全符合性)
        - [4.2.1 Full conformance to outcomes 预期结果完全符合性](#421-full-conformance-to-outcomes-预期结果完全符合性)
        - [4.2.2 Full conformance to tasks 任务完全符合性](#422-full-conformance-to-tasks-任务完全符合性)
      - [4.3 Tailored conformance 裁剪符合性](#43-tailored-conformance-裁剪符合性)
    - [5 Key concepts and their application 关键概念及其应用](#5-key-concepts-and-their-application-关键概念及其应用)
      - [5.1 General 总则](#51-general-总则)
      - [5.2 System concepts 系统概念](#52-system-concepts-系统概念)
        - [5.2.1 Systems 系统](#521-systems-系统)
        - [5.2.2 System structure 系统结构](#522-system-structure-系统结构)
        - [5.2.3 Interfacing, enabling, and interoperating systems 接口系统、使能系统和互操作系统](#523-interfacing-enabling-and-interoperating-systems-接口系统使能系统和互操作系统)
        - [5.2.4 Concepts related to the system solution context 与系统解决方案语境相关的概念](#524-concepts-related-to-the-system-solution-context-与系统解决方案语境相关的概念)
        - [5.2.5 Product line engineering (PLE) 产品线工程（PLE）](#525-product-line-engineering-ple-产品线工程ple)
      - [5.3 Organizational concepts 组织概念](#53-organizational-concepts-组织概念)
        - [5.3.1 Organizations 组织](#531-organizations-组织)
        - [5.3.2 Organization and project-level adoption 组织层面与项目层面的采用](#532-organization-and-project-level-adoption-组织层面与项目层面的采用)
        - [5.3.3 Organization and collaborative activities 组织与协作活动](#533-organization-and-collaborative-activities-组织与协作活动)
      - [5.4 System of systems concepts 系统的系统概念](#54-system-of-systems-concepts-系统的系统概念)
        - [5.4.1 Differences between systems and SoS 系统与 SoS 之间的差异](#541-differences-between-systems-and-sos-系统与-sos-之间的差异)
        - [5.4.2 Managerial and operational independence 管理独立性与运行独立性](#542-managerial-and-operational-independence-管理独立性与运行独立性)
        - [5.4.3 Taxonomy of SoS SoS 的分类法](#543-taxonomy-of-sos-sos-的分类法)
        - [5.4.4 SoS considerations in life cycle stages of a system 系统生存周期阶段中的 SoS 考虑事项](#544-sos-considerations-in-life-cycle-stages-of-a-system-系统生存周期阶段中的-sos-考虑事项)
        - [5.4.5 Application of this document to SoS 本文件对 SoS 的应用](#545-application-of-this-document-to-sos-本文件对-sos-的应用)
      - [5.5 Life cycle concepts 生存周期概念](#55-life-cycle-concepts-生存周期概念)
        - [5.5.1 System life cycle model 系统生存周期模型](#551-system-life-cycle-model-系统生存周期模型)
        - [5.5.2 System life cycle stages 系统生存周期阶段](#552-system-life-cycle-stages-系统生存周期阶段)
      - [5.6 Process concepts 过程概念](#56-process-concepts-过程概念)
        - [5.6.1 Criteria for processes 过程的准则](#561-criteria-for-processes-过程的准则)
        - [5.6.2 Description of processes 过程的描述](#562-description-of-processes-过程的描述)
        - [5.6.3 General characteristics of processes 过程的一般特征](#563-general-characteristics-of-processes-过程的一般特征)
      - [5.7 Processes in this document 本文件中的过程](#57-processes-in-this-document-本文件中的过程)
        - [5.7.1 General 总则](#571-general-总则)
        - [5.7.2 Agreement processes 协议过程](#572-agreement-processes-协议过程)
        - [5.7.3 Organizational project-enabling processes 组织项目使能过程](#573-organizational-project-enabling-processes-组织项目使能过程)
        - [5.7.4 Technical management processes 技术管理过程](#574-technical-management-processes-技术管理过程)
        - [5.7.5 Technical processes 技术过程](#575-technical-processes-技术过程)
      - [5.8 Process application 过程应用](#58-process-application-过程应用)
        - [5.8.1 Overview 概述](#581-overview-概述)
        - [5.8.2 Process iteration, recursion, and concurrency 过程迭代、递归与并发](#582-process-iteration-recursion-and-concurrency-过程迭代递归与并发)
        - [5.8.3 Process views 过程视图](#583-process-views-过程视图)
      - [5.9 Concept and system definition 概念与系统定义](#59-concept-and-system-definition-概念与系统定义)
      - [5.10 Assurance and quality characteristics 保证与质量特性](#510-assurance-and-quality-characteristics-保证与质量特性)
      - [5.11 Process reference model 过程参考模型](#511-process-reference-model-过程参考模型)
    - [6 System life cycle processes 系统生存周期过程](#6-system-life-cycle-processes-系统生存周期过程)
      - [6.1 Agreement processes 协议过程](#61-agreement-processes-协议过程)
        - [6.1.1 Acquisition process 获取过程](#611-acquisition-process-获取过程)
        - [6.1.2 Supply process 供应过程](#612-supply-process-供应过程)
      - [6.2 Organizational project-enabling processes 组织项目使能过程](#62-organizational-project-enabling-processes-组织项目使能过程)
        - [6.2.1 Life cycle model management process 生存周期模型管理过程](#621-life-cycle-model-management-process-生存周期模型管理过程)
        - [6.2.2 Infrastructure management process 基础设施管理过程](#622-infrastructure-management-process-基础设施管理过程)
        - [6.2.3 Portfolio management process 项目组合管理过程](#623-portfolio-management-process-项目组合管理过程)
        - [6.2.4 Human resource management process 人力资源管理过程](#624-human-resource-management-process-人力资源管理过程)
        - [6.2.5 Quality management process 质量管理过程](#625-quality-management-process-质量管理过程)
        - [6.2.6 Knowledge management process 知识管理过程](#626-knowledge-management-process-知识管理过程)
      - [6.3 Technical management processes 技术管理过程](#63-technical-management-processes-技术管理过程)
        - [6.3.1 Project planning process 项目规划过程](#631-project-planning-process-项目规划过程)
        - [6.3.2 Project assessment and control process 项目评定与控制过程](#632-project-assessment-and-control-process-项目评定与控制过程)
        - [6.3.3 Decision management process 决策管理过程](#633-decision-management-process-决策管理过程)
        - [6.3.4 Risk management process 风险管理过程](#634-risk-management-process-风险管理过程)
        - [6.3.5 Configuration management process 配置管理过程](#635-configuration-management-process-配置管理过程)
        - [6.3.6 Information management process 信息管理过程](#636-information-management-process-信息管理过程)
        - [6.3.7 Measurement process 测量过程](#637-measurement-process-测量过程)
        - [6.3.8 Quality assurance process 质量保证过程](#638-quality-assurance-process-质量保证过程)
      - [6.4 Technical processes 技术过程](#64-technical-processes-技术过程)
        - [6.4.1 Business or mission analysis process 业务或任务分析过程](#641-business-or-mission-analysis-process-业务或任务分析过程)
        - [6.4.2 Stakeholder needs and requirements definition process 利益相关方需要与需求定义过程](#642-stakeholder-needs-and-requirements-definition-process-利益相关方需要与需求定义过程)
        - [6.4.3 System requirements definition process 系统需求定义过程](#643-system-requirements-definition-process-系统需求定义过程)
        - [6.4.4 System architecture definition process 系统架构定义过程](#644-system-architecture-definition-process-系统架构定义过程)
        - [6.4.5 Design definition process 设计定义过程](#645-design-definition-process-设计定义过程)
        - [6.4.6 System analysis process 系统分析过程](#646-system-analysis-process-系统分析过程)
        - [6.4.7 Implementation process 实现过程](#647-implementation-process-实现过程)
        - [6.4.8 Integration process 集成过程](#648-integration-process-集成过程)
        - [6.4.9 Verification process 验证过程](#649-verification-process-验证过程)
        - [6.4.10 Transition process 转换过程](#6410-transition-process-转换过程)
        - [6.4.11 Validation process 确认过程](#6411-validation-process-确认过程)
        - [6.4.12 Operation process 运行过程](#6412-operation-process-运行过程)
        - [6.4.13 Maintenance process 维护过程](#6413-maintenance-process-维护过程)
        - [6.4.14 Disposal process 处置过程](#6414-disposal-process-处置过程)
  - [Annex A (normative) — Tailoring process ｜ 附录 A（规范性）——裁剪过程](#annex-a-normative-tailoring-process-附录-a规范性裁剪过程)
    - [A.1 General 总则](#a1-general-总则)
    - [A.2 Tailoring process 裁剪过程](#a2-tailoring-process-裁剪过程)
      - [A.2.1 Purpose 目的](#a21-purpose-目的)
      - [A.2.2 Outcomes 预期结果](#a22-outcomes-预期结果)
      - [A.2.3 Activities and tasks 活动与任务](#a23-activities-and-tasks-活动与任务)
  - [Annex B (informative) — Example process artefacts and information items ｜ 附录 B（资料性）——过程人工制品与信息部件示例](#annex-b-informative-example-process-artefacts-and-information-items-附录-b资料性过程人工制品与信息部件示例)
  - [Annex C (informative) — Process reference model for assessment purposes ｜ 附录 C（资料性）——用于评定目的的过程参考模型](#annex-c-informative-process-reference-model-for-assessment-purposes-附录-c资料性用于评定目的的过程参考模型)
    - [C.1 General 总则](#c1-general-总则)
    - [C.2 Conformance with ISO/IEC 33004 与 ISO/IEC 33004 的符合性](#c2-conformance-with-isoiec-33004-与-isoiec-33004-的符合性)
      - [C.2.1 General 总则](#c21-general-总则)
      - [C.2.2 Requirements for process reference models 对过程参考模型的要求](#c22-requirements-for-process-reference-models-对过程参考模型的要求)
      - [C.2.3 Process descriptions 过程描述](#c23-process-descriptions-过程描述)
    - [C.3 The process reference model 过程参考模型](#c3-the-process-reference-model-过程参考模型)
  - [Annex D (informative) — Model-based systems and software engineering (MBSSE) ｜ 附录 D（资料性）— 基于模型的系统与软件工程（MBSSE）](#annex-d-informative-model-based-systems-and-software-engineering-mbsse-附录-d资料性-基于模型的系统与软件工程mbsse)
    - [D.1 MBSE description MBSE 描述](#d1-mbse-description-mbse-描述)
    - [D.2 Implementation of system life cycle processes in an MBSE approach 以 MBSE 途径实施系统生存周期过程](#d2-implementation-of-system-life-cycle-processes-in-an-mbse-approach-以-mbse-途径实施系统生存周期过程)
    - [D.3 MBSE as a practice 作为实践的 MBSE](#d3-mbse-as-a-practice-作为实践的-mbse)
    - [D.4 Benefits of executing system life cycle processes in an MBSE environment 在 MBSE 环境中执行系统生存周期过程的效益](#d4-benefits-of-executing-system-life-cycle-processes-in-an-mbse-environment-在-mbse-环境中执行系统生存周期过程的效益)
    - [D.5 Model types useful in MBSE MBSE 中有用的模型类型](#d5-model-types-useful-in-mbse-mbse-中有用的模型类型)
  - [Bibliography 参考文献](#bibliography-参考文献)
  - [IEEE notices and abstract IEEE 通告与摘要](#ieee-notices-and-abstract-ieee-通告与摘要)

---

---

## Cover and copyright pages (source lay-out, verbatim) 封面与版权页（源版式，逐字照录）

15288

15288

Second edition

第二版

2023-05

2023-05

Systems and software engineering — System life cycle processes

系统与软件工程 — 系统生存周期过程

Ingénierie des systèmes et du logiciel — Processus du cycle de vie du système

系统与软件工程 — 系统生存周期过程

Reference number ISO/IEC/IEEE 15288:2023(E)

参考编号 ISO/IEC/IEEE 15288:2023(E)

COPYRIGHT PROTECTED DOCUMENT

版权保护文件

© ISO/IEC 2023 © IEEE 2023 All rights reserved. Unless otherwise specified, or required in the context of its implementation, no part of this publication may be reproduced or utilized otherwise in any form or by any means, electronic or mechanical, including photocopying, or posting on the internet or an intranet, without prior written permission. Permission can be requested from either ISO or IEEE at the respective address below or ISO’s member body in the country of the requester.

© ISO/IEC 2023 © IEEE 2023 保留所有权利。除非另有规定，或在实施本文件时有所要求，未经事先书面许可，不得以任何形式或任何手段（电子的或机械的，包括影印，或在互联网或内联网上发布）复制或以其他方式利用本出版物的任何部分。许可可向 ISO 或 IEEE 索取，地址见下文各自地址，或向索取者所在国的 ISO 成员机构索取。

ISO copyright office Institute of Electrical and Electronics Engineers, Inc CP 401 • Ch. de Blandonnet 8 3 Park Avenue, New York CH-1214 Vernier, Geneva NY 10016-5997, USA Phone: +41 22 749 01 11 Fax: +41 22 749 09 47 Email: copyright@iso.org Email: stds.ipr@ieee.org Website: www.iso.orgWebsite: www.ieee.org Published in Switzerland

ISO 版权办公室 电气电子工程师学会（IEEE）公司 CP 401 • Ch. de Blandonnet 8 3 Park Avenue, New York CH-1214 Vernier, Geneva NY 10016-5997, USA 电话：+41 22 749 01 11 传真：+41 22 749 09 47 电子邮件：copyright@iso.org 电子邮件：stds.ipr@ieee.org 网址：www.iso.org网址：www.ieee.org 发布于瑞士

---

## Foreword 前言

ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) form the specialised system for worldwide standardization. National bodies that are members of ISO or IEC participate in the development of International Standards through technical committees established by the respective organization to deal with particular fields of technical activity. ISO and IEC technical committees collaborate in fields of mutual interest. Other international organizations, governmental and non-governmental, in liaison with ISO and IEC, also take part in the work.

ISO（国际标准化组织）和 IEC（国际电工委员会）构成世界范围标准化的专门体系。属 ISO 或 IEC 成员的国家机构，通过各自组织为处理特定技术活动领域而设立的技术委员会，参与国际标准的制定。ISO 和 IEC 的技术委员会在相互感兴趣的领域开展合作。与 ISO 和 IEC 保持联络的其他国际组织，无论政府的还是非政府的，也参与此项工作。

The procedures used to develop this document and those intended for its further maintenance are described in the ISO/IEC Directives, Part 1. In particular, the different approval criteria needed for the different types of ISO/IEC documents should be noted. This document was drafted in accordance with the editorial rules of the ISO/IEC Directives, Part 2 (see www.iso.org/directives or www.iec.ch/members_experts/refdocs).

用于制定本文件以及旨在对其进行进一步维护的程序，在 ISO/IEC 导则第 1 部分中描述。特别宜注意，不同类型的 ISO/IEC 文件所需的批准准则各不相同。本文件依据 ISO/IEC 导则第 2 部分的编辑规则起草（见 www.iso.org/directives 或 www.iec.ch/members_experts/refdocs）。

IEEE Standards documents are developed within the IEEE Societies and the Standards Coordinating Committees of the IEEE Standards Association (IEEE-SA) Standards Board. The IEEE develops its standards through a consensus development process, approved by the American National Standards Institute, which brings together volunteers representing varied viewpoints and interests to achieve the final product. Volunteers are not necessarily members of the Institute and serve without compensation. While the IEEE administers the process and establishes rules to promote fairness in the consensus development process, the IEEE does not independently evaluate, test, or verify the accuracy of any of the information contained in its standards.

IEEE 标准文件由 IEEE 各学会以及 IEEE 标准协会（IEEE-SA）标准委员会的标准协调委员会制定。IEEE 通过协商一致制定过程制定其标准，该过程由美国国家标准学会批准，汇聚代表不同观点和利益的志愿者以形成最终产品。志愿者不一定是本学会的成员，且无偿服务。IEEE 虽管理该过程并制定规则以促进协商一致制定过程的公平性，但 IEEE 并不独立评估、测试或验证其标准中所含任何信息的准确性。

Attention is drawn to the possibility that some of the elements of this document may be the subject of patent rights. ISO shall not be held responsible for identifying any or all such patent rights. Details of any patent rights identified during the development of the document will be in the Introduction and/ or on the ISO list of patent declarations received (see www.iso.org/patents) or the IEC list of patent declarations received (see https://patents.iec.ch).

提请注意，本文件的某些要素可能涉及专利权。ISO 不承担识别任何或所有此类专利权的责任。在制定本文件过程中识别出的任何专利权的详细信息，将载于引言中和／或 ISO 已收到的专利声明清单（见 www.iso.org/patents）或 IEC 已收到的专利声明清单（见 https://patents.iec.ch）。

Any trade name used in this document is information given for the convenience of users and does not constitute an endorsement.

本文件中使用的任何商品名，均为方便使用者而提供的信息，不构成认可。

For an explanation of the voluntary nature of standards, the meaning of ISO specific terms and expressions related to conformity assessment, as well as information about ISO's adherence to the World Trade Organization (WTO) principles in the Technical Barriers to Trade (TBT), see www.iso.org/iso/foreword.html. In the IEC, see www.iec.ch/understanding-standards.

关于标准的自愿性质的说明、与符合性评定有关的 ISO 特定术语和表述的含义，以及有关 ISO 遵守世界贸易组织（WTO）技术性贸易壁垒（TBT）原则的信息，见 www.iso.org/iso/foreword.html。在 IEC 中，见 www.iec.ch/understanding-standards。

This document was prepared by Joint Technical Committee ISO/JTC 1, *Information technology,* Subcommittee SC 7, *Software and systems engineering,* in cooperation with the Systems and Software Engineering Standards Committee of the IEEE Computer Society, under the Partner Standards Development Organization cooperation agreement between ISO and IEEE.

本文件由联合技术委员会 ISO/JTC 1（*信息技术*）和分技术委员会 SC 7（*软件与系统工程*）与 IEEE 计算机学会的系统与软件工程标准委员会合作制定，依据 ISO 与 IEEE 之间的伙伴标准制定组织合作协议。

This second edition cancels and replaces the first edition (ISO/IEC/IEEE 15288:2015), which has been technically revised.

本第二版取消并代替第一版（ISO/IEC/IEEE 15288:2015），第一版已作技术修订。

The main changes are as follows:

主要变化如下：

- improvements to selected technical processes including business or mission analysis, system

- 对选定技术过程的改进，包括业务或任务分析、系统

architecture definition, system analysis, implementation, integration, operations, and maintenance;

架构定义、系统分析、实现、集成、运行和维护；

- improvements to selected technical management processes including risk management and

- 对选定技术管理过程的改进，包括风险管理和

configuration management;

配置管理；

- updates to Clause 5, key concepts, including a better description of iteration, recursion, system-of-

- 对第 5 章关键概念的更新，包括对迭代、递归、系统的

systems, quality characteristics, etc.;

系统、质量特性等的更好描述；

- new content in Clause 5 on concept and system definition, and expanded content on process

- 第 5 章中关于概念和系统定义的新内容，以及关于过程

application and system concepts;

应用和系统概念的扩展内容；

- updates to the terms and definitions;

- 对术语和定义的更新；

- a new annex addressing model-based systems engineering (MBSE).

- 新增一个论述基于模型的系统工程（MBSE）的附录。

Any feedback or questions on this document should be directed to the user’s national standards body. A complete listing of these bodies can be found at www.iso.org/members.html and www.iec.ch/national-committees.

对本文件的任何反馈或问题，宜向使用者的国家标准化机构提出。这些机构的完整清单见 www.iso.org/members.html 和 www.iec.ch/national-committees。

## Introduction 引言

The complexity of systems continues to increase to unprecedented levels. This has led to new opportunities, but also to increased challenges for the organizations that create and utilise systems. These challenges exist throughout the life cycle of a system and at all levels of architectural detail. This document provides a common process framework for describing the life cycle of systems, adopting a systems engineering approach. This document concerns systems that can be configured with one or more of the following system elements: hardware elements, software elements, data, humans, processes, services, procedures, facilities, materials, and naturally occurring entities.

系统的复杂性持续增长，达到前所未有的水平。这既带来了新的机遇，也给创建和利用系统的组织带来了更大的挑战。这些挑战存在于系统的整个生存周期中，也存在于架构细节的各个层级上。本文件采用系统工程方法，为描述系统的生存周期提供通用的过程框架。本文件所涉及的系统，能由一个或多个下列系统元素配置而成：硬件元素、软件元素、数据、人员、过程、服务、规程、设施、材料和自然存在的实体。

This document focuses on defining stakeholder needs, concerns, priorities, and constraints for the required functionality early in the development cycle, establishing requirements, then proceeding with design synthesis and system validation while considering the complete problem. It integrates all the disciplines and specialty groups into a team effort forming a structured development process that proceeds from conception through production to operation. It considers the needs of all stakeholders with the goal of providing a quality product that meets the needs of users and other applicable stakeholders. It provides the processes for acquiring and supplying systems. It helps to improve communication and cooperation among the parties that create, utilise, and manage modern systems in order that they can work in an integrated, coherent fashion. Finally, this document provides the framework for assessment and improvement of the life cycle processes.

本文件关注在开发周期早期定义所需功能的利益相关方需要、关注点、优先事项和约束，建立需求，随后在考虑完整问题的同时进行设计综合和系统确认。它将所有专业和专门小组整合为团队工作，形成从构想经生产到运行的结构化开发过程。它考虑所有利益相关方的需要，目标是提供满足用户及其他适用利益相关方需要的优质产品。它提供用于获取和供应系统的过程。它有助于改进创建、利用和管理现代系统的各方之间的沟通与合作，使其能以集成、协调的方式工作。最后，本文件为生存周期过程的评定和改进提供了框架。

There is a wide variety of systems in terms of their purpose, domain of application, complexity, size, novelty, adaptability, quantity, location, life span, and evolution. The processes in this document form a comprehensive set from which an organization can construct system life cycle models appropriate to its products and services. An organization, depending on its purpose, can select and apply an appropriate subset to fulfil that purpose.

系统在目的、应用领域、复杂性、规模、新颖性、适应性、数量、位置、寿命和演化方面千差万别。本文件中的过程构成一个全面的集合，组织能据此构建适合其产品和服务的系统生存周期模型。组织能根据其目的，选择并应用适当的子集来实现该目的。

This document can be used in one or more of the following modes:

本文件能以下列一种或多种方式使用：

- By an organization — to help establish an environment of desired processes. These processes can be

- 由组织使用——以帮助建立由所期望过程构成的环境。这些过程能

supported by an infrastructure of methods, procedures, techniques, tools, and trained personnel. The organization may then employ this environment to perform and manage its projects and progress systems through their life cycle stages. In this mode this document is used to assess conformance of a declared, established environment to its provisions. It can be used by a single organization in a self-imposed mode or in a multi-party situation. Parties can be from the same organization or from different organizations and the situation can range from an informal agreement to a formal contract.

由方法、程序、技术和工具以及经过培训的人员构成的基础设施予以支持。组织随后可运用这一环境来执行和管理其项目，并推进系统历经其生存周期各阶段。在这一方式下，本文件用于评定所声明的、已建立的环境与本文件各项规定之间的符合性。它既能由单一组织以自我施加的方式使用，也能在多参与方情形下使用。各参与方可来自同一组织或不同组织，其情形可从非正式协议到正式合同不等。

- By a project — to help select, structure, and employ the elements of an established environment to

- 由项目使用——以帮助选择、构造和运用已建立环境的各要素，以

provide products and services. In this mode this document is used in the assessment of conformance of the project to the declared and established environment.

提供产品和服务。在这一方式下，本文件用于评定项目与所声明的、已建立的环境之间的符合性。

- By an acquirer and a supplier — to help develop an agreement concerning processes and activities.

- 由获取方和供应方使用——以帮助制定关于过程和活动的协议。

Via the agreement, the processes and activities in this document are selected, negotiated, agreed to, and performed. In this mode this document is used for guidance in developing the agreement.

通过该协议，本文件中的过程和活动得以选择、协商、达成一致并予以执行。在这一方式下，本文件用于为制定该协议提供指南。

- By process assessors — to serve as a process reference model for use in the performance of process

- 由过程评定员使用——用作过程参考模型，以用于执行过程

assessments that can be used to support organizational process improvement.

评定，这些评定能用于支持组织的过程改进。

In the context of this document and ISO/IEC/IEEE 12207, there is a continuum of human‐made systems from those that use little or no software to those in which software is the primary interest. When software is the predominant system or element of interest, ISO/IEC/IEEE 12207 should be used. Both documents have the same process model, share most activities and tasks, and differ primarily in descriptive notes.

在本文件与 ISO/IEC/IEEE 12207 的语境中，人造系统构成一个连续谱：从很少使用或完全不使用软件的系统，到以软件为主要关注对象的系统。当所关注的主要系统或元素是软件时，宜使用 ISO/IEC/IEEE 12207。两份文件具有相同的过程模型，共有多数活动和任务，主要区别在于描述性注。

Although this document does not establish a management system, it is intended to be compatible with the quality management system provided by ISO 9001, the service management system provided by ISO/IEC 20000 series, the IT asset management system provided by the ISO/IEC 19770 series, and the information security management system provided by ISO/IEC 27000.

尽管本文件不建立管理体系，但旨在与 ISO 9001 提供的质量管理体系、ISO/IEC 20000 系列提供的服务管理体系、ISO/IEC 19770 系列提供的 IT 资产管理体系以及 ISO/IEC 27000 提供的安全管理体系相兼容。

## Systems and software engineering — System life cycle processes 系统与软件工程——系统生存周期过程

### 1 Scope 范围

This document establishes a common framework of process descriptions for describing the life cycle of systems created by humans, defining a set of processes and associated terminology from an engineering viewpoint. These processes can be applied to systems of interest, their system elements, and to systems of systems. Selected sets of these processes can be applied throughout the stages of a system's life cycle. This is accomplished through the involvement of stakeholders, with the ultimate goal of achieving customer satisfaction.

本文件建立了过程描述的通用框架，用以描述人造系统的生存周期，并从工程视角定义了一组过程及相关术语。这些过程能应用于所关注系统、其系统元素以及系统的系统。这些过程的选定集合能应用于系统生存周期的各个阶段。这是通过利益相关方的参与来实现的，最终目标是实现顾客满意。

This document defines a set of processes to facilitate system development and information exchange among acquirers, suppliers, and other stakeholders in the life cycle of a system.

本文件定义了一组过程，以促进系统开发以及系统生存周期中获取方、供应方和其他利益相关方之间的信息交换。

This document specifies processes that support the definition, control, and improvement of the system life cycle processes used within an organization or a project. Organizations and projects can use these processes when acquiring and supplying systems.

本文件规定了用以支持组织或项目内所用系统生存周期过程的定义、控制和改进的各项过程。组织和项目在获取和供应系统时能使用这些过程。

This document applies to organizations in their roles as both acquirers and suppliers.

本文件适用于同时承担获取方和供应方角色的组织。

This document applies to the full life cycle of systems, including conception, development, production, utilization, support and retirement of systems, and to the acquisition and supply of systems, whether performed internally or externally to an organization. The life cycle processes of this document can be applied iteratively and concurrently to a system and recursively to the system elements.

本文件适用于系统的全生存周期，包括系统的构想、开发、生产、使用、保障和退役，也适用于系统的获取与供应，无论这些工作是在组织内部还是组织外部执行的。本文件中的生存周期过程能对系统迭代地、并发地应用，并能对系统元素递归地应用。

This document applies to one-of-a-kind systems, mass-produced systems, and customised, adaptable systems. It also applies to a complete stand-alone system and to systems that are embedded and integrated into larger more complex and complete systems.

本文件适用于单件系统、批量生产系统以及定制的、可适配的系统。它也适用于完整的独立系统，以及嵌入并集成到更大、更复杂、更完整的系统中的系统。

This document does not prescribe a specific system life cycle model, development methodology, method, modelling approach or technique.

本文件不规定特定的系统生存周期模型、开发方法学、方法、建模途径或技术。

This document does not detail information items in terms of name, format, explicit content, and recording media. ISO/IEC/IEEE 15289 addresses the content for life cycle process information items (documentation).

本文件不按名称、格式、明示内容和记录介质来详细规定信息部件。ISO/IEC/IEEE 15289 涉及生存周期过程信息部件（文档）的内容。

### 2 Normative references 规范性引用文件

There are no normative references in this document.

本文件没有规范性引用文件。

### 3 Terms, definitions, and abbreviated terms 术语、定义和缩略语

For the purposes of this document, the following terms and definitions apply.

下列术语和定义适用于本文件。

ISO, IEC, and IEEE maintain terminology databases for use in standardization at the following addresses:

ISO、IEC 和 IEEE 维护供标准化使用的术语数据库，网址如下：

- ISO Online browsing platform: available at https://​www​.iso​.org/​obp

- ISO 在线浏览平台：可访问 https://​www​.iso​.org/​obp

- IEC Electropedia: available at https://​www​.electropedia​.org/​

- IEC Electropedia：可访问 https://​www​.electropedia​.org/​

- IEEE Standards Dictionary Online: available at: https://​dictionary​.ieee​.org/​

- IEEE Standards Dictionary Online：可访问 https://​dictionary​.ieee​.org/​

> **NOTE** Definitions for other system and software engineering terms can be found in ISO/IEC/IEEE 24765, available at www​.computer​.org/​sevocab.

> **注**：其他系统和软件工程术语的定义可参见 ISO/IEC/IEEE 24765，网址为 www​.computer​.org/​sevocab。

#### 3.1 acquirer 获取方

*stakeholder* (3.44) that acquires or procures a *system* (3.46), *product* (3.32) or *service* (3.42) from a *supplier* (3.45)

从*供应方*(3.45)获取或采购*系统*(3.46)、*产品*(3.32)或*服务*(3.42)的*利益相关方*(3.44)

> **Note 1 to entry:** Other terms commonly used for an acquirer are buyer, *customer* (3.12), owner, purchaser, or internal/organizational sponsor.

> **注 1**：获取方常用的其他术语有买方、*顾客*(3.12)、所有者、获取方或内部／组织发起人。

#### 3.2 acquisition 获取

*process* (3.27) of obtaining a *system* (3.46), *product* (3.32) or *service* (3.42)

获得*系统*(3.46)、*产品*(3.32)或*服务*(3.42)的*过程*(3.27)

#### 3.3 activity 活动

set of cohesive *tasks* (3.51) of a *process* (3.27)

*过程*(3.27)的一组内聚的*任务*(3.51)

#### 3.4 agreement 协议

mutual acknowledgement of terms and conditions under which a working relationship is conducted EXAMPLE Contract, memorandum of agreement.

对据以开展工作关系的条款和条件的相互认可合同、协议备忘录。

#### 3.5 architecture 架构

fundamental concepts or properties of a *system* (3.46) in its *environment* (3.16) and governing principles for the realization and evolution of this system and its related *life cycle* (3.21) *processes* (3.27)

*系统*(3.46)在其*环境*(3.16)中的基本概念或属性，以及对该系统及其相关*生存周期*(3.21)*过程*(3.27)的实现与演化的管控原则

> [SOURCE: ISO/IEC/IEEE 42020:2019, 3.3, modified — ‘entity’ has been replaced with ‘system’; notes to entry have been removed.]

> **来源**：ISO/IEC/IEEE 42020:2019，3.3，修改——已将‘entity’替换为‘system’；删除了条目注。

#### 3.6 artefact 人工制品

work *product* (3.32) that is produced and used during a project to capture and convey information EXAMPLE Models, stakeholder requirements, system/software requirements, architecture descriptions, design descriptions, source code, implemented system elements, verified or validated system.

在项目期间产生并用于捕获和传递信息的*工作产品*(3.32)模型、利益相关方需求、系统／软件需求、架构描述、设计描述、源代码、已实现的系统元素、经验证或确认的系统。

> [SOURCE: ISO 19014-4:2020, 3.9, modified — EXAMPLE has been added.]

> **来源**：ISO 19014-4:2020，3.9，修改——增加了示例。

#### 3.7 audit 审核

independent examination of a work *product* (3.32) or set of work products to assess compliance with specifications, standards, contractual *agreements* (3.4), or other criteria

为评定对规格、标准、合同*协议*(3.4)或其他准则的符合性，对*工作产品*(3.32)或工作产品集合所作的独立检查

#### 3.8 baseline 基线

formally approved version of a *configuration item* (3.11)*,* regardless of media, formally designated and fixed at a specific time during the configuration item's *life cycle* (3.21)

*配置项*(3.11)*，*不论介质如何，在配置项*生存周期*(3.21)内的特定时刻被正式指定并固定的、经正式批准的版本

> [SOURCE: IEEE Std 828-2012]

> **来源**：IEEE Std 828-2012

#### 3.9 concept of operations 运行构想

verbal and graphic statement, in broad outline, of an *organization’s* (3.25) assumptions or intent in regard to an operation or series of operations of new, modified, or existing organizational *systems* (3.46)

关于新的、经修改的或现有组织*系统*(3.46)的一次运行或一系列运行，对*组织*(3.25)的假设或意图所作的概括性的文字和图形陈述

> **Note 1 to entry:** The concept of operations frequently is embodied in long-range strategic plans and annual operational plans. In the latter case, the concept of operations in the plan covers a series of connected operations to be carried out simultaneously or in succession to achieve an organizational performance objective. See also *operational concept* (3.23).

> **注 1**：运行构想常常体现在长期战略计划和年度运行计划中。在后一种情况下，计划中的运行构想涵盖为实现组织的绩效目标而同时或相继开展的一系列相互关联的运行。另见*运行概念*(3.23)。

> **Note 2 to entry:** The concept of operations provides the basis for bounding the operating space, system capabilities, *interfaces* (3.19), and operating *environment* (3.16).

> **注 2**：运行构想为界定运行空间、系统能力、*接口*(3.19)和运行*环境*(3.16)提供依据。

> [SOURCE: ANSI/AIAA G-043B-2018, 5.2, modified — The second definition has been used; the last two sentences of Note 1 to entry have been removed; Note 2 to entry has been added.]

> **来源**：ANSI/AIAA G-043B-2018，5.2，修改——采用了第二种定义；删去了注 1 的最后两句；增加了注 2。

#### 3.10 concern 关注点

matter of interest or importance to a *stakeholder* (3.44)

对*利益相关方*(3.44)而言具有利益或重要性的问题

> **Note 1 to entry:** A concern pertains to any influence on a *system* (3.46) in its *environment* (3.16), including developmental, technological, business, operational, organizational, political, economic, legal, regulatory, ethical, ecological, and social influences.

> **注 1**：关注点关乎*环境*(3.16)中对*系统*(3.46)的一切影响，包括开发、技术、业务、运行、组织、政治、经济、法律、监管、伦理、生态与社会等方面的影响。

> [SOURCE: ISO/IEC/IEEE 42020:2019, 3.8, modified — EXAMPLE has been removed; Note 1 to entry has been added.]

> **来源**：ISO/IEC/IEEE 42020:2019，3.8，修改——删去了示例；增加了注 1。

#### 3.11 configuration item 配置项

item or aggregation of hardware, software, or both, that is designated for configuration management and treated as a single entity in the configuration management *process* (3.27)

被指定进行配置管理、并在配置管理*过程*(3.27)中作为单一实体对待的硬件、软件或二者的条目或集合

#### 3.12 customer 顾客

*organization* (3.25) or person that receives a *product* (3.32) or *service* (3.42)

接收*产品*(3.32)或*服务*(3.42)的*组织*(3.25)或个人

> **EXAMPLE** Consumer, client, *user* (3.53), *acquirer* (3.1), buyer, or purchaser.

> **示例**：消费者、委托方、*用户*(3.53)、*获取方*(3.1)、买方或获取方。

> **Note 1 to entry:** A customer can be internal or external to the organization.

> **注 1**：顾客能是组织内部的或外部的。

#### 3.13 design, noun 设计，名词

specification of *system elements* (3.47) and their relationships, that is sufficiently complete to support a compliant implementation of the *architecture* (3.5)

*系统元素*(3.47)及其关系的规定，其完整程度足以支撑*架构*(3.5)的合规实现

> **Note 1 to entry:** Design provides the detailed implementation-level physical structure, behaviour, temporal relationships, and other attributes of system elements.

> **注 1**：设计给出系统元素在实现层面的详细物理结构、行为、时间关系和其他属性。

#### 3.14 design characteristics 设计特征

design attributes or distinguishing features that pertain to a measurable description of a *product* (3.32) or *service* (3.42)

与*产品*(3.32)或*服务*(3.42)的可测量描述相关的设计属性或区别性特征

#### 3.15 enabling system 使能系统

*system* (3.46) that supports a *system-of-interest* (3.48) during its *life cycle* (3.21) *stages* (3.43) but does not necessarily contribute directly to its function during operation EXAMPLE Production-enabling system, which is required when a system-of-interest enters the production stage.

在*系统关注*(3.48)的*生存周期*(3.21)*阶段*(3.43)中为其提供支持、但在运行期间未必直接对其功能作出贡献的*系统*(3.46)生产使能系统，当系统关注进入生产阶段时需要该系统。

> **Note 1 to entry:** Each enabling system has a life cycle of its own. This document is applicable to each enabling system when, in its own right, it is treated as a system-of-interest.

> **注 1**：每个使能系统各有其自身的生存周期。当某一使能系统本身被作为系统关注对待时，本文件适用于该系统。

#### 3.16 environment 环境

<system> context determining the setting and circumstances of all influences upon a *system* (3.46)

〈系统〉确定对*系统*(3.46)的一切影响之背景与境况的语境

#### 3.17 incident 事件

anomalous or unexpected event, set of events, condition, or situation at any time during the *life cycle* (3.21) of a *project* (3.33)*,* *product* (3.32)*, service* (3.42)*,* or *system* (3.46)

在*项目*(3.33)*、产品*(3.32)、*服务*(3.42)或*系统*(3.46)的*生存周期*(3.21)中任何时候出现的异常或非预期的事件、事件集合、状况或情形

> **Note 1 to entry:** An incident is elevated and treated as a *problem* (3.26) when the cause of the incident needs to be analysed and corrected to prevent reoccurrence to avoid or minimise loss of life, or damage of property or natural *resources* (3.37).

> **注 1**：当事件的原因需要分析和纠正以防止再次发生，从而避免或尽量减少生命损失或财产或自然*资源*(3.37)损害时，事件被升级并作为*问题*(3.26)处理。

#### 3.18 information item 信息部件

separately identifiable body of information that is produced, stored, and delivered for human use

为供人使用而生成、存储和交付的、可单独识别的信息体

> [SOURCE: ISO/IEC/IEEE 15289:2019, 3.1.12, modified — The preferred term "information product" has been removed; notes to entry have been removed.]

> **来源**：ISO/IEC/IEEE 15289:2019，3.1.12，修改——删去了首选术语“information product”；删去了注。

#### 3.19 interface 接口

point at which two or more logical, physical, or both, *system elements* (3.47) or software system elements meet and act on or communicate with each other

两个或更多逻辑、物理或二者兼有的*系统元素*(3.47)或软件系统元素相遇并相互作用或相互通信的点

> [SOURCE: ISO/IEC/IEEE 24748-6: —, 3.1.3]

> **来源**：ISO/IEC/IEEE 24748-6:—，3.1.3

#### 3.20 interoperating system 互操作系统

*system* (3.46) that exchanges information with the *system-of-interest* (3.48) and uses the information that has been exchanged

与*系统关注*(3.48)交换信息并使用所交换信息的*系统*(3.46)

#### 3.21 life cycle 生存周期

evolution of a *system* (3.46), *product* (3.32), *service* (3.42), *project* (3.33) or other human-made entity from conception through *retirement* (3.38)

*系统*(3.46)、*产品*(3.32)、*服务*(3.42)、*项目*(3.33)或其他人工实体从构想到*退役*(3.38)的演化

#### 3.22 life cycle model 生存周期模型

framework of *processes* (3.27) and *activities* (3.3) concerned with the *life cycle* (3.21) which can be organized into *stages* (3.43)*,* acting as a common reference for communication and understanding

与*生存周期*(3.21)有关的*过程*(3.27)和*活动*(3.3)的框架，能组织为*阶段*(3.43)，作为交流和理解的共同参照

#### 3.23 operational concept 运行概念

verbal and graphic statement of an *organization’s* (3.25) assumptions or intent in regard to an operation or series of operations of a specific *system* (3.46) or a related set of specific new, existing or modified systems

关于某一特定*系统*(3.46)或一组相关的新系统、现有系统或修改后系统的一次或一系列运行，对*组织*(3.25)的假设或意图所作的文字与图示陈述

> **Note 1 to entry:** The operational concept is designed to give an overall picture of the operations using one or more specific systems, or set of related systems, in the organization’s operational *environment* (3.16) from the *users’* (3.53) and *operators’* (3.24) perspectives. See also *concept of operations* (3.9).

> **注 1**：运行概念旨在从*用户*(3.53)和*操作者*(3.24)的角度，给出在组织的运行*环境*(3.16)中使用一个或多个特定系统或一组相关系统的运行全貌。另见*运行构想*(3.9)。

> **Note 2 to entry:** The operational concept is about systems, while a *concept of operations* (3.9) typically refers to organizations.

> **注 2**：运行概念针对的是系统，而*运行构想*(3.9)通常指组织。

> [SOURCE: ANSI/AIAA G-043B-2018, 5.2, modified — The third definition has been used; the first sentence in Note 1 to entry has been removed; Note 2 to entry has been added.]

> **来源**：ANSI/AIAA G-043B-2018，5.2，修改——采用了第三种定义；删去了注 1 的第一句；增加了注 2。

#### 3.24 operator 操作者

individual or *organization* (3.25) that performs the operations of a *system* (3.46)

对*系统*(3.46)执行操作的个体或*组织*(3.25)

> **Note 1 to entry:** The role of operator and the role of *user* (3.53) can be vested, simultaneously or sequentially, in the same individual or organization.

> **注 1**：操作者的角色和*用户*(3.53)的角色能同时地或先后地授予同一个体或组织。

> **Note 2 to entry:** An individual operator combined with knowledge, skills, and procedures can be considered as an element of the system.

> **注 2**：具备知识、技能和规程的个体操作者能被看作系统的一个元素。

> **Note 3 to entry:** An operator may perform operations on a system that is operated, or of a system that is operated, depending on whether or not operating instructions are placed within the system boundary.

> **注 3**：操作者能对被操作的系统执行操作，或对某一系统的运行执行操作，取决于操作说明是否置于系统边界之内。

#### 3.25 organization 组织

person or group of people that has its own functions with responsibilities, authorities, and relationships to achieve its objectives EXAMPLE Company, corporation, firm, enterprise, manufacturer, institution, charity, sole trader, association, or parts or combination thereof.

拥有自身职能、职责、权限和关系以实现其目标的个人或群体公司、企业、商行、事业单位、制造商、机构、慈善团体、个体经营者、协会，或其部分或组合。

> [SOURCE: ISO 9000:2015, 3.2.1, modified — Notes to entry have been removed; EXAMPLE has been added.]

> **来源**：ISO 9000:2015，3.2.1，修改——删去了注；增加了示例。

#### 3.26 problem 问题

difficulty, uncertainty, or otherwise realised and undesirable event, set of events, condition, or situation that requires investigation and corrective action

需要调查和纠正措施的困难、不确定性或其他已显现且不期望的事件、事件集合、状况或情形

#### 3.27 process 过程

set of interrelated or interacting *activities* (3.3) that transform inputs into outputs

将输入转换为输出的相互关联或相互作用的一组*活动*(3.3)

#### 3.28 iteration 迭代

<process> repeating the application of the same *process* (3.27) or set of processes on the same level of the *system* (3.46) structure

〈过程〉在*系统*(3.46)结构的同一层级上重复应用同一*过程*(3.27)或过程集

#### 3.29 process purpose 过程目的

high level objective of performing the *process* (3.27) and the likely outcomes of effective implementation of the process

执行*过程*(3.27)的高层级目标以及该过程有效实施的预期结果

> **Note 1 to entry:** The purpose of implementing the process is to provide benefits to the *stakeholders* (3.44).

> **注 1**：实施该过程的目的是为*利益相关方*(3.44)提供益处。

#### 3.30 process outcome 过程结果

observable result of the successful achievement of the *process purpose* (3.29)

*过程目的*(3.29)成功实现的可观察结果

#### 3.31 recursion 递归

<process> repeating the application of the same *process* (3.27) or set of processes to successive levels of *system elements* (3.47) in the system structure

〈过程〉将同一*过程*(3.27)或过程集重复应用于系统结构中相继层级的*系统元素*(3.47)

#### 3.32 product 产品

output of an *organization* (3.25) that can be produced without any transaction taking place between the organization and the *customer* (3.12)

*组织*(3.25)的输出，能在该组织与*顾客*(3.12)之间不发生任何交易的情况下产生

> **Note 1 to entry:** The dominant element of a product is that it is generally tangible.

> **注 1**：产品的主要特点在于它通常是有形的。

> [SOURCE: ISO 9000:2015, 3.7.6, modified — Notes 1 and 3 to entry have been removed.]

> **来源**：ISO 9000:2015，3.7.6，修改——删去了注 1 和注 3。

#### 3.33 project 项目

endeavour with defined start and finish criteria undertaken to create a *product* (3.32) or *service* (3.42) in accordance with specified *resources* (3.37) and *requirements* (3.36)

为按照规定的*资源*(3.37)和*需求*(3.36)创建*产品*(3.32)或*服务*(3.42)而开展的、具有确定起止准则的努力

> **Note 1 to entry:** A project is sometimes viewed as a unique *process* (3.27) comprising coordinated and controlled *activities* (3.3) and composed of activities from the Technical Management and Technical Processes defined in this document.

> **注 1**：项目有时被视为一个独特的*过程*(3.27)，该过程包含经过协调与控制的*活动*(3.3)，并由本文件所定义的技术管理过程与技术过程中的活动组成。

> **Note 2 to entry:** Continuous development approaches such as agile and DevOps can use different terminology for the creation of product and services.

> **注 2**：敏捷和 DevOps 等持续开发方法能对产品与服务的创建使用不同的术语。

#### 3.34 quality assurance / QA ｜ 质量保证 / QA

part of quality management focused on providing confidence that quality *requirements* (3.36) will be fulfilled

质量管理的一部分，致力于提供质量*要求*(3.36)将得到满足的信任

> [SOURCE: ISO 9000:2015, 3.3.6, modified — The abbreviated term has been added.]

> **来源**：ISO 9000:2015，3.3.6，修改——增加了缩略语。

#### 3.35 quality characteristic 质量特性

inherent characteristic of a *product* (3.32), *service* (3.42), *process* (3.27), or *system* (3.46) related to a *requirement* (3.36)

与*要求*(3.36)有关的*产品*(3.32)、*服务*(3.42)、*过程*(3.27)或*系统*(3.46)的固有特性

> [SOURCE: ISO 9000:2015, 3.10.2, modified — ‘object’ has been replaced with ‘product, service, process, or system’; notes to entry have been removed.]

> **来源**：ISO 9000:2015，3.10.2，修改——“object”已替换为“product, service, process, or system”；删去了注。

#### 3.36 requirement 要求

statement which translates or expresses a need and its associated constraints and conditions

转化或表达需要及其相关约束和条件的陈述

> [SOURCE: ISO/IEC/IEEE 29148:2018, 3.1.19, modified — Notes to entry have been removed.]

> **来源**：ISO/IEC/IEEE 29148:2018，3.1.19，修改——删去了注。

#### 3.37 resource 资源

asset that is utilised or consumed during the execution of a *process* (3.27)

在*过程*(3.27)的执行期间被利用或消耗的资产

> **Note 1 to entry:** Resource includes diverse entities such as funding, personnel, facilities, capital equipment, tools and utilities such as power, water, fuel, and communication infrastructures.

> **注 1**：资源包括各类实体，如资金、人员、设施、资本设备、工具，以及电力、水、燃料和通信基础设施等公用设施。

> **Note 2 to entry:** Resources include those that are reusable, renewable or consumable.

> **注 2**：资源包括可复用、可再生或可消耗的资源。

#### 3.38 retirement 退役

<system> withdrawal of active support by the operation and maintenance *organization* (3.25), partial or total replacement by a new *system* (3.46)*,* or installation of an upgraded system, or final decommissioning and disposal

〈系统〉运行与维护*组织*(3.25)撤出主动支持，由新*系统*(3.46)部分或全部替换*，*或安装经升级的系统，或最终退役和处置

#### 3.39 risk 风险

effect of uncertainty on objectives

不确定性对目标的影响

> **Note 1 to entry:** An effect is a deviation from the expected — positive or negative. A positive effect is also known as an opportunity.

> **注 1**：影响是对预期的偏离——正面的或负面的。正面影响也称为机会。

> **Note 2 to entry:** Objectives can have different aspects [such as financial, health and *safety* (3.40), and environmental goals] and can apply at different levels [such as strategic, organization-wide, project, *product* (3.32) and *process* (3.27)].

> **注 2**：目标能具有不同的方面[如财务、健康与*安全性*(3.40)以及环境目标]，并能适用于不同的层次[如战略、组织范围、项目、*产品*(3.32)和*过程*(3.27)]。

> **Note 3 to entry:** Risk is often characterized by reference to potential events and consequences, or a combination of these.

> **注 3**：风险通常以潜在事件和后果、或二者的组合来表征。

> **Note 4 to entry:** Risk is often expressed in terms of a combination of the consequences of an event (including changes in circumstances) and the associated likelihood of occurrence.

> **注 4**：风险通常以事件后果（包括情形的变化）和相关发生可能性的组合来表示。

> **Note 5 to entry:** Uncertainty is the state, even partial, of deficiency of information related to understanding or knowledge of an event, its consequence, or likelihood.

> **注 5**：不确定性是与对事件及其后果或可能性的理解或认识有关的信息存在欠缺（哪怕是部分欠缺）的状态。

> [SOURCE: ISO Guide 73:2009, 1.1, modified — The last sentence in Note 1 to entry has been added.]

> **来源**：ISO Guide 73:2009，1.1，修改——增加了注 1 的最后一句。

#### 3.40 safety 安全性

expectation that a *system* (3.46) does not, under defined conditions, lead to a state in which human life, health, property, or the *environment* (3.16) is endangered

在规定的条件下，*系统*(3.46)不会导致人的生命、健康、财产或*环境*(3.16)受到危害的状态的期望

> **Note 1 to entry:** The term is alternatively defined as freedom from *risk* (3.39) which is not tolerable.

> **注 1**：该术语也定义为免于不可容忍的*风险*(3.39)。

> [SOURCE: ISO/IEC/IEEE 12207:2017, 3.1.48, modified — Note 1 to entry has been added.]

> **来源**：ISO/IEC/IEEE 12207:2017，3.1.48，修改——增加了注 1。

#### 3.41 security 安全

protection against intentional subversion or forced failure

针对蓄意破坏或强制失效的防护

> **Note 1 to entry:** Security includes authenticity, accountability, confidentiality, integrity, availability, non-repudiation, and reliability, all of which have the related issue of their assurance.

> **注 1**：安全包括真实性、可问责性、保密性、完整性、可用性、不可否认性和可靠性，它们都有与之相关的保证问题。

> [SOURCE: NATO AEP-67, modified — Note 1 to entry has been updated.]

> **来源**：NATO AEP-67，修改——更新了注 1。

#### 3.42 service 服务

output of an *organization* (3.25) with at least one *activity* (3.3) necessarily performed between the organization and the *customer* (3.12)

*组织*(3.25)的输出，其中至少有一项*活动*(3.3)必需在该组织与*顾客*(3.12)之间进行

> **Note 1 to entry:** The dominant elements of a service are generally intangible.

> **注 1**：服务的主要构成要素通常是无形的。

> **Note 2 to entry:** A service is coherent, discrete, and can be composed of other services.

> **注 2**：服务是连贯的、离散的，并可由其他服务组成。

> [SOURCE: ISO 9000:2015, 3.7.7, modified — Notes 2, 3, and 4 to entry have been replaced by a new Note 2 to entry.]

> **来源**：ISO 9000:2015，3.7.7，修改——注 2、注 3 和注 4 已由新的注 2 替代。

#### 3.43 stage 阶段

period within the *life cycle* (3.21) of an entity that relates to the state of its description or realization

实体*生存周期*(3.21)内与其描述或实现的状态相关的时期

> **Note 1 to entry:** As used in this document, stages relate to major progress and achievement milestones of the entity through its life cycle.

> **注 1**：在本文件中，阶段与实体在其生存周期中的重大进展和成就里程碑相关。

> **Note 2 to entry:** Stages often overlap.

> **注 2**：阶段常常重叠。

#### 3.44 stakeholder 利益相关方

individual or *organization* (3.25) having a right, share, claim, or interest in a *system* (3.46) or in its possession of characteristics that meet their needs and expectations EXAMPLE End *users* (3.53), end user organizations, supporters, developers, *customers* (3.12), producers, trainers, maintainers, disposers, *acquirers* (3.1), *suppliers* (3.45), regulatory bodies, and people influenced positively or negatively by a system.

对*系统*(3.46)或对其具备满足自身需要和期望的特性享有权利、份额、主张或利益的个人或*组织*(3.25)最终*用户*(3.53)、最终用户组织、支持者、开发者、*顾客*(3.12)、生产者、培训者、维护者、处置者、*获取方*(3.1)、*供应方*(3.45)、监管机构以及受系统正面或负面影响的个人。

> **Note 1 to entry:** Some stakeholders can have interests that oppose each other or oppose the system.

> **注 1**：某些利益相关方能具有彼此对立或与系统对立的利益。

#### 3.45 supplier 供应方

*organization* (3.25) or an individual that enters into an *agreement* (3.4) with the *acquirer* (3.1) for the supply of a *product* (3.32) or *service* (3.42)

与*获取方*(3.1)订立*协议*(3.4)以供应*产品*(3.32)或*服务*(3.42)的*组织*(3.25)或个人

> **Note 1 to entry:** Other terms commonly used for supplier are contractor, producer, seller or vendor.

> **注 1**：供应方的其他常用术语有承包商、生产者、卖方或供应方。

> **Note 2 to entry:** The acquirer and the supplier sometimes are part of the same organization.

> **注 2**：获取方和供应方有时是同一组织的组成部分。

#### 3.46 system 系统

arrangement of parts or elements that together exhibit a stated behaviour or meaning that the individual constituents do not

各部分或各元素的安排，它们合在一起呈现出单个构成部分所不具备的既定行为或意义

> **Note 1 to entry:** A system is sometimes considered as a *product* (3.32) or as the *services* (3.42) it provides.

> **注 1**：系统有时被视为*产品*(3.32)，或被视为它所提供的*服务*(3.42)。

> **Note 2 to entry:** In practice, the interpretation of its meaning is frequently clarified by the use of an associative noun, e.g. aircraft system. Alternatively, the word “system” is substituted simply by a context-dependent synonym (e.g. aircraft), though this potentially obscures a system principles perspective.

> **注 2**：在实践中，其含义的解释常常借助关联名词的使用来澄清，例如飞机系统。或者，“system”一词仅以依语境而定的同义词替代（例如 aircraft），不过这有可能掩盖系统原理这一视角。

> **Note 3 to entry:** A complete system includes all of the associated equipment, facilities, material, computer programs, firmware, technical documentation, *services* (3.42), and personnel required for operations and support to the degree necessary for self-sufficient use in its intended *environment* (3.16).

> **注 3**：一个完整的系统包括所有相关设备、设施、材料、计算机程序、固件、技术文件、*服务*(3.42)以及人员，其配备程度以在其预期*环境*(3.16)中自给自足地使用所需的运行与保障为限。

#### 3.47 system element 系统元素

discrete part of a *system* (3.46) that can be implemented to fulfil specified *requirements* (3.36)

*系统*(3.46)的离散部分，能加以实现以满足规定的*要求*(3.36)

> **EXAMPLE** Hardware, software, data, humans, *processes* (3.27) [e.g. processes for providing *service* (3.42) to *users* (3.53)], procedures [e.g., *operator* (3.24) instructions], facilities, materials, and naturally occurring entities or any combination.

> **示例**：硬件、软件、数据、人员、*过程*(3.27)[例如向*用户*(3.53)提供*服务*(3.42)的过程]、规程[例如*操作者*(3.24)说明]、设施、材料以及自然存在的实体，或上述各项的任意组合。

#### 3.48 system-of-interest / SoI ｜ 系统关注 / SoI

*system* (3.46) whose *life cycle* (3.21) is under consideration

其*生存周期*(3.21)正处于考虑之中的*系统*(3.46)

#### 3.49 system of systems / SoS ｜ 系统的系统 / SoS

set of *systems* (3.46) or *system elements* (3.47) that interact to provide a unique capability that none of the constituent systems can accomplish on its own

相互作用以提供任何单个构成系统自身都无法实现的独特能力的*系统*(3.46)或*系统元素*(3.47)的集合

> [SOURCE: ISO/IEC/IEEE 21839:2019, 3.1.4]

> **来源**：ISO/IEC/IEEE 21839:2019，3.1.4

#### 3.50 systems engineering 系统工程

transdisciplinary and integrative approach to enable the successful realization, use, and *retirement* (3.38) of engineered *systems* (3.46) using systems principles and concepts and scientific, technological and management methods

一种跨学科、综合性的途径，运用系统原理与概念以及科学、技术和管理方法，使工程化*系统*(3.46)得以成功实现、使用和*退役*(3.38)

> [SOURCE: INCOSE-TP-2020-002-06]

> **来源**：INCOSE-TP-2020-002-06

#### 3.51 task 任务

required, recommended, or permissible action, intended to contribute to the achievement of one or more outcomes of a *process* (3.27)

所要求的、所推荐的或所允许的行动，旨在促成*过程*(3.27)的一项或多项预期结果的实现

#### 3.52 traceability 可追溯性

discernible association among two or more logical entities, such as *requirements* (3.36)*,* *system elements* (3.47), *verifications* (3.55), or *tasks* (3.51)

两个或多个逻辑实体之间可辨别的关联，如*要求*(3.36)*、* *系统元素*(3.47)、*验证*(3.55)或*任务*(3.51)

> [SOURCE: ISO/IEC TR 29110-1:2016, 3.71, modified — "discernible" has been added; EXAMPLE has been removed.]

> **来源**：ISO/IEC TR 29110-1:2016，3.71，已修改——“discernible”已添加；EXAMPLE 已删除。

#### 3.53 user 用户

individual or group that interacts with a *system* (3.46) or benefits from a system during its utilization

与*系统*(3.46)交互、或在系统使用期间从系统获益的个人或群体

> **Note 1 to entry:** The role of user and the role of *operator* (3.24) are sometimes vested, simultaneously or sequentially, in the same individual or *organization* (3.25).

> **注 1**：用户角色与*操作员*(3.24)角色有时同时或先后赋予同一个个人或*组织*(3.25)。

> [SOURCE: ISO/IEC 25010:2011, 4.3.16, modified — The original Note 1 to entry has been replaced by a new one.]

> **来源**：ISO/IEC 25010:2011，4.3.16，已修改——原注 1 已由新注取代。

#### 3.54 validation 确认

confirmation, through the provision of objective evidence, that the *requirements* (3.36) for a specific intended use or application have been fulfilled

通过提供客观证据，对为特定预期用途或应用而提出的*要求*(3.36)已得到满足的认定

> **Note 1 to entry:** In a *life cycle* (3.21) context, validation involves the set of *activities* (3.3) for gaining confidence that a *system* (3.46) is able to accomplish its intended use, goals, and objectives in an *environment* (3.16) like the operational environment. The right system was built.

> **注 1**：在*生存周期*(3.21)语境中，确认涉及一组*活动*(3.3)，用以获得信心，确信*系统*(3.46)能在类似于运行环境的*环境*(3.16)中实现其预期用途、目标和目的。所构建的是正确的系统。

> [SOURCE: ISO 9000:2015, 3.8.13, modified — Notes 1 to 3 to entry have been removed; a new Note 1 to entry has been added.]

> **来源**：ISO 9000:2015，3.8.13，已修改——原注 1 至注 3 已删除；已增加新的注 1。

#### 3.55 verification 验证

confirmation, through the provision of objective evidence, that specified *requirements* (3.36) have been fulfilled

通过提供客观证据，对规定*要求*(3.36)已得到满足的认定

> **Note 1 to entry:** Verification is a set of *activities* (3.3) that compares a *system* (3.46) or *system element* (3.47) against the required characteristics. This includes, but is not limited to, specified requirements, *design* (3.13) description, and the system itself. The system was built right.

> **注 1**：验证是一组*活动*(3.3)，用于将*系统*(3.46)或*系统元素*(3.47)与所要求的特性进行比对。这包括但不限于规定要求、*设计*(3.13)描述以及系统本身。系统构建得正确。

> [SOURCE: ISO 9000:2015, 3.8.12, modified — Notes 1 to 3 to entry have been removed; a new Note 1 to entry has been added.]

> **来源**：ISO 9000:2015，3.8.12，已修改——原注 1 至注 3 已删除；已增加新的注 1。

#### 3.56 view 视图

representation of a *system* (3.46) from the perspective of a related set of *concerns* (3.10)

从一组相关*关注点*(3.10)的角度对*系统*(3.46)的表示

> **Note 1 to entry:** A view can be an operational, functional, or architectural representation of a system.

> **注 1**：视图能是系统的运行表示、功能表示或架构表示。

> [SOURCE: ISO/IEC/IEEE 24774:2021, 3.21, modified — removed ‘whole’ from the definition and the original Note 1 to entry has been replaced by a new one.]

> **来源**：ISO/IEC/IEEE 24774:2021，3.21，已修改——从定义中删除了“whole”，原注 1 已由新注取代。

#### 3.57 viewpoint 视角

specification of the conventions for constructing and using a *view* (3.56)

用于构造和使用*视图*(3.56)的约定的规格

> [SOURCE: ISO/IEC/IEEE 24774:2021, 3.22, modified — Notes 1 to 3 to entry have been removed.]

> **来源**：ISO/IEC/IEEE 24774:2021，3.22，已修改——原注 1 至注 3 已删除。

### 4 Conformance 符合性

#### 4.1 Intended usage 预期用途

The requirements in this document are contained in Clause 6 and Annex A. This document provides requirements for a number of processes suitable for usage during the life cycle of a system. It is possible that particular projects or organizations need only some of the processes provided by this document. Therefore, implementation of this document typically involves selecting and declaring a set of processes suitable to the organization or project. There are two ways that an implementation can be claimed to conform to the provisions of this document – full conformance and tailored conformance.

本文件的要求载于第 6 章和附录 A。本文件为若干适合在系统生存周期内使用的过程提出了要求。特定项目或组织可能只需要本文件所提供的部分过程。因此，本文件的实施通常涉及选择并声明一组适合该组织或项目的过程。某项实施据以主张符合本文件规定的方式有两种——完全符合性和裁剪符合性。

There are two criteria for claiming full conformance. Achieving either criterion suffices for conformance, although the chosen criterion (or criteria) shall be stated in the claim. Claiming “full conformance to tasks” asserts that all of the requirements of the activities and tasks of the declared set of processes are achieved. Alternatively, claiming “full conformance to outcomes” asserts that all of the required outcomes of the declared set of processes are achieved. Full conformance to outcomes permits greater freedom in the implementation of conforming processes and can be useful for implementing processes to be used in the context of an innovative life cycle model.

声称完全符合性有两项准则。达成任一项准则即足以构成符合性，但所选准则（或多项准则）应在主张中予以说明。声明“任务完全符合性”即主张所声明过程集合的活动与任务的全部要求均已达成。或者，声明“预期结果完全符合性”即主张所声明过程集合的全部所需预期结果均已达成。预期结果完全符合性为符合性过程的实施提供了更大的自由度，并且能用于实施拟在创新性生存周期模型情境中使用的过程。

> **NOTE 1** Options for conformance are provided for needed flexibility in the application of this document. Each process has a set of objectives (phrased as “outcomes”) and a set of activities and tasks that represent one way to achieve the objectives.

> **注 1**：提供符合性方面的多种选择，是为了在本文件的应用中获得所需的灵活性。每个过程都有一组目标（以“预期结果”的形式表述）以及一组活动与任务，这些活动与任务代表达成这些目标的一种方式。

> **NOTE 2** Users who implement the activities and tasks of the declared set of processes can assert full conformance to tasks of the selected processes. Some users, however, can have innovative process variants that achieve the objectives (i.e. the outcomes) of the declared set of processes without implementing all of the activities and tasks. These users can assert full conformance to the outcomes of the declared set of processes. The two criteria – conformance to task and conformance to outcome – are necessarily not equivalent since specific performance of activities and tasks can require, in some cases, a higher level of capability than just the achievement of outcomes.

> **注 2**：实施所声明过程集合的活动与任务的使用者，能就所选过程主张任务完全符合性。然而，某些使用者可能拥有创新的过程变体，它们无需实施全部活动与任务即达成所声明过程集合的目标（即预期结果）。这些使用者能就所声明过程集合的预期结果主张完全符合性。这两项准则——任务符合性与预期结果符合性——必然不等价，因为在某些情形下，具体执行活动与任务所需的能力水平可能高于仅达成预期结果。

> **NOTE 3** An organization (e.g. national, industrial association, company) imposing this document as a condition of trade can specify and make public the minimum set of required processes, outcomes, activities, and tasks, which constitute suppliers' compliance with the conditions of trade.

> **注 3**：将本文件作为贸易条件加以施加的组织（如国家机构、行业协会、公司），能规定并公布所需的过程、预期结果、活动和任务的最小集合，供应方对该贸易条件的符合即由该集合构成。

> **NOTE 4** Requirements of this document are marked by the use of the verb "shall". Recommendations are marked by the use of the verb "should". Permissions are marked by the use of the verb "may". However, despite the verb that is used, the requirements for conformance are selected as described previously.

> **注 4**：本文件的要求以动词“应”标示。推荐以动词“宜”标示。许可以动词“可”标示。然而，无论使用何种动词，符合性要求均按前述方式选定。

#### 4.2 Full conformance 完全符合性

##### 4.2.1 Full conformance to outcomes 预期结果完全符合性

A claim of full conformance declares the set of processes for which conformance is claimed. Full conformance to outcomes is achieved by demonstrating that all of the outcomes of the declared set of processes have been achieved. In this situation, the provisions for activities and tasks of the declared set of processes are guidance rather than requirements, regardless of the verb form that is used in the provision.

完全符合性的主张声明其所主张符合的过程集合。预期结果完全符合性通过证明所声明过程集合的全部预期结果均已达成而实现。在此情形下，无论条款中使用何种动词形式，所声明过程集合中关于活动与任务的条款均为指南而非要求。

> **NOTE** One intended use of this document is to facilitate process assessment and improvement. For this purpose, the objectives of each process are written in the form of 'outcomes' compatible with the provisions of the ISO/IEC 33000 family of standards. Those standards provide for the assessment of the processes of this document, providing a basis for improvement. Users intending process assessment and improvement can use the process outcomes written in this document as the "process reference model" required by ISO/IEC 33002.

> **注**：本文件的一项预期用途是促进过程评估与改进。为此，每个过程的目标均以“预期结果”的形式编写，与 ISO/IEC 33000 族标准的规定相兼容。这些标准为评估本文件中的各过程作出了规定，从而为改进提供依据。拟进行过程评估与改进的使用者，能把本文件所编写的过程预期结果用作 ISO/IEC 33002 所要求的“过程参考模型”。

##### 4.2.2 Full conformance to tasks 任务完全符合性

A claim of full conformance declares the set of processes for which conformance is claimed. Full conformance to tasks is achieved by demonstrating that all of the requirements of the activities and tasks of the declared set of processes have been achieved. In this situation, the provisions for the outcomes of the declared set of processes are guidance rather than requirements, regardless of the verb form that is used in the provision.

完全符合性的主张声明其所主张符合的过程集合。任务完全符合性通过证明所声明过程集合的活动与任务的全部要求均已达成而实现。在此情形下，无论条款中使用何种动词形式，所声明过程集合中关于预期结果的条款均为指南而非要求。

> **NOTE** A claim of full conformance to tasks can be appropriate in contractual situations where an acquirer or a regulator requires detailed understanding of the suppliers’ processes.

> **注**：在获取方或监管方要求详细了解供应方过程的合同情境下，任务完全符合性的主张可能是适宜的。

#### 4.3 Tailored conformance 裁剪符合性

When this document is used as a basis for establishing a set of processes that do not qualify for full conformance, the processes in Clause 6 of this document shall be selected or modified in accordance with the tailoring process prescribed in Annex A. The tailored set of processes, for which tailored conformance is claimed, are declared. Tailored conformance is achieved by demonstrating that the outcomes, activities, and tasks, as tailored, have been achieved.

当以本文件为基础建立一组不符合完全符合性条件的过程时，应按附录 A 规定的裁剪过程，选择或修改本文件第 6 章中的过程。为其声明裁剪符合性的那组经裁剪的过程，应予声明。裁剪符合性通过证明经裁剪的预期结果、活动与任务均已达成而实现。

> **NOTE 1** Tailoring can diminish the perceived value of a claim of conformance to this document because it is difficult for other organizations to understand the extent to which tailoring can have deleted desirable provisions.

> **注 1**：裁减可能削弱对本文件符合性声明的可感知价值，因为其他组织难以了解裁减在多大程度上删改了所期望的规定。

> **NOTE 2** An organization asserting a claim of conformance to this document can find it advantageous to claim full conformance to a smaller list of processes rather than tailored conformance to a larger list of processes.

> **注 2**：主张对本文件符合性的组织能发现，声明对较少一组过程的完全符合，比声明对较多一组过程的裁减符合更为有利。

> **NOTE 3** An organization can also choose to claim full conformance to a selected set of processes as well as tailored conformance to other processes.

> **注 3**：组织还能选择既对选定的一组过程声明完全符合，又对其他过程声明裁减符合。

### 5 Key concepts and their application 关键概念及其应用

#### 5.1 General 总则

This clause highlights and explains essential concepts on which this document is based. Further elaboration of these concepts can be found in the ISO/IEC/IEEE 24748-1 and ISO/IEC/IEEE 24748-2, which provide guidelines on the application of life cycle management.

本条强调并解释本文件所依据的基本概念。对这些概念的进一步阐述见 ISO/IEC/IEEE 24748-1 和 ISO/IEC/IEEE 24748-2，它们就生存周期管理的应用提供了指南。

#### 5.2 System concepts 系统概念

##### 5.2.1 Systems 系统

A system is an arrangement of parts or elements that together exhibit behaviour or meaning that the individual constituents do not. Systems can be either physical or conceptual, or a combination of both. Systems in the physical universe are composed of matter and energy, may embody information encoded in matter-energy carriers, and exhibit observable behaviour. Conceptual systems are abstract systems of pure information, and do not directly exhibit behaviour, but exhibit “meaning”. In both cases, the system’s properties (as a whole) result or emerge from the parts or elements and their individual properties and the relationships and interactions between and among the parts, the system and its environment.

系统是部件或元素的安排，这些部件或元素共同表现出各单个组成部分所不具备的行为或含义。系统能是物理的或概念的，或二者的组合。物理世界中的系统由物质和能量组成，可承载以物质—能量载体编码的信息，并表现出可观察的行为。概念系统是纯信息的抽象系统，不直接表现出行为，但表现出“含义”。在这两种情况下，系统的属性（作为整体）都源自或涌现于部件或元素及其各自的属性，以及各部件之间、系统与其环境之间的关系和相互作用。

The perception and definition of a particular system, its architecture and its system elements depend on a stakeholder's interests and responsibilities. One stakeholder's system-of-interest (SoI) can be viewed as a system element in another stakeholder's SoI. Furthermore, an SoI can be viewed as being part of the environment for another stakeholder's SoI. Also, an SoI can be viewed as a constituent system in an SoS.

对某一特定系统、其架构及其系统元素的感知和定义，取决于利益相关方的利益与职责。一个利益相关方的所关注系统（SoI）能被看作另一个利益相关方的 SoI 中的一个系统元素。此外，一个 SoI 能被看作另一个利益相关方的 SoI 的环境的一部分。一个 SoI 还能被看作 SoS 中的一个构成系统。

The following are key points regarding the characteristics of the SoI (also see Figure 1 and Figure 2):

以下是关于 SoI 特征的关键要点（另见图 1 和图 2）：

a) defined boundaries encapsulate meaningful needs and practical solutions;

a) 所定义的边界封装了有意义的需要和切实可行的解决方案；

b) there is a hierarchical or other relationship between system elements;

b) 系统元素之间存在层级关系或其他关系；

c) an entity at any level in the SoI can be viewed as a system;

c) SoI 中任何层级上的实体都能被看作一个系统；

d) a system comprises an integrated, defined set of subordinate system elements;

d) 系统由一组集成的、已定义的下级系统元素构成；

e) humans can be viewed as both users external to a system (e.g. users) and as system elements (e.g.

e) 人既能被看作系统外部的用户（例如用户），也能被看作系统内部的系统元素（例如

operators) within a system;

操作者）；

f) a system can be viewed in isolation as an entity, i.e. a product; or as a collection of functions capable of interacting with its surrounding environment, i.e. a set of services.

f) 系统能被孤立地看作一个实体，即一个产品；或被看作一组能够与其周围环境相互作用的功能，即一组服务。

> **NOTE** Services, hardware elements, and software elements can be products or services if they are either individual SoIs or constituents in an SoS. Consideration of services and products integrated within a system is sometimes called a product-service system[65]. Product-service systems provide a means for organizations to offer services related to their products.

> **注**：服务、硬件元素和软件元素，若其本身是单个 SoI 或是 SoS 中的组成部分，则能是产品或服务。对集成在某一系统中的服务和产品的考虑，有时称为产品—服务系统[65]。产品—服务系统为组织提供了一种途径，用以提供与其产品相关的服务。

Whatever the boundaries chosen to define the system, the concepts in this document are generic and permit a practitioner to correlate or adapt individual instances of life cycles to its system principles.

无论为定义系统选择何种边界，本文件中的概念都是通用的，并允许从业者将各个生存周期实例与其系统原则相关联或相适应。

##### 5.2.2 System structure 系统结构

The system life cycle processes in this document are described in relation to a system (see Figure 1) which is composed of a set of interacting system elements, each of which can be implemented to fulfil its respective specified requirements. System elements may include software elements, hardware elements, services, and utilization and support resources. Responsibility for the implementation of any system element may be delegated to another party through an agreement.

本文件中的系统生存周期过程是相对于一个系统来描述的（见图 1），该系统由一组相互作用的系统元素组成，其中每个系统元素都能以实现其各自的规定需求的方式实现。系统元素可包括软件元素、硬件元素、服务以及使用与保障资源。任何系统元素的实现职责都能通过协议委托给另一方。

![Figure 1 — System and system element relationship](ISO IEC IEEE 15288 2023.assets/fig-01.png)

**Figure 1 — System and system element relationship**

**图 1 — 系统与系统元素的关系**

The relationship between system elements can be expressed in many forms, including hierarchies or networks. For more complex SoIs, a prospective system element may itself need to be considered as a system (that in turn is comprised of system elements) before a complete set of system elements can be defined with confidence (see Figure 2). In this manner, the appropriate system life cycle processes are applied recursively to an SoI to resolve its structure to the point where understandable and manageable system elements can be implemented (made, bought, or reused). While Figures 1 and 2 imply a hierarchical relationship, in reality there are an increasing number of systems that, from one or more aspects, are not hierarchical, such as networks and other distributed systems. 5.4 discusses the concept of a system of systems (SoS).

系统元素之间的关系能以多种形式表达，包括层级或网络。对于更复杂的 SoI，在能有把握地定义完整的系统元素集之前，某个预期的系统元素本身可能就需要被看作一个系统（该系统又由系统元素构成）（见图 2）。以此方式，将适宜的系统生存周期过程递归地应用于一个 SoI，以将其结构分解到能够实现（制造、购买或复用）可理解且可管理的系统元素的程度。虽然图 1 和图 2 暗示了层级关系，但在现实中，越来越多的系统从一个或多个方面看并非层级结构，例如网络和其他分布式系统。5.4 讨论了系统的系统（SoS）的概念。

![Figure 2 — System-of-interest structure](ISO IEC IEEE 15288 2023.assets/fig-02.png)

**Figure 2 — System-of-interest structure**

**图 2 — 所关注系统的结构**

##### 5.2.3 Interfacing, enabling, and interoperating systems 接口系统、使能系统和互操作系统

Any system sharing an interface (data or information, energy, resource, physical) with the SoI during any stage of the SoI’s life cycle is an interfacing system and needs to be considered in the system development. Humans can be system elements of the SoI (e.g. an operator) or can be interfacing externally to the SoI (e.g. a user requesting information) throughout the SoI’s life cycle stages.

在 SoI 生存周期的任何阶段与 SoI 共享接口（数据或信息、能量、资源、物理）的任何系统都是接口系统，需要在系统开发中予以考虑。在 SoI 的各个生存周期阶段中，人既可以是 SoI 的系统元素（例如操作者），也可以在 SoI 外部与之接口（例如请求信息的用户）。

Throughout the life cycle of an SoI, essential services are required from enabling systems, e.g. mass-production system, training system, maintenance system. Each of these systems supports one or more lifecycle processes of the SoI to be conducted. SoIs often have interfaces with other systems that are used during life cycle stages other than operations. Some of these interfaces can be exclusive to that stage and not used during operation.

在 SoI 的整个生存周期中，需要使能系统提供基本服务，例如批量生产系统、训练系统、维护系统。这些系统各自支持 SoI 的一个或多个生存周期过程得以开展。SoI 常常与其他系统存在接口，这些接口在运行以外的生存周期阶段中使用。其中有些接口能为该阶段所独有，而在运行期间不使用。

Systems that interact to perform a function are called interoperating systems, which are an important aspect in the context of systems of systems (see 5.4). Interoperating systems are a subset of the interfacing systems. While interoperability can involve the exchange and use of information, physical and other types of interoperability can be important. For example, many kinds of electronic devices now have power adapters appropriate for the user’s location.

相互作用以执行某一功能的系统称为互操作系统，这在系统的系统的语境中是一个重要方面（见 5.4）。互操作系统是接口系统的一个子集。互操作性可涉及信息的交换与使用，但物理的及其他类型的互操作性也能是重要的。例如，许多种类的电子设备现在都配有适合用户所在地的电源适配器。

> **NOTE** Interoperating systems can exchange information to enable an SoI to operate reliably, securely, usefully or efficiently, or to improve accessibility or usability. An interoperating system can also receive information from the SoI for use by other systems or SoS.

> **注**：互操作系统能交换信息，以使 SoI 可靠、安全、有用或高效地运行，或改善可访问性或易用性。互操作系统还能从 SoI 接收信息，以供其他系统或 SoS 使用。

The interrelationships between the SoI and the interfacing, enabling, and interoperating systems can be bi-directional or one-way. Requirements for the interrelationships need to be included in the requirements for the SoI.

SoI 与接口系统、使能系统和互操作系统之间的相互关系能是双向的或单向的。这些相互关系的要求需要纳入 SoI 的要求之中。

Further elaboration of these concepts can be found in the ISO/IEC/IEEE 24748-1 and ISO/IEC/IEEE 24748-2, which provide guidelines on the application of life cycle processes.

对这些概念的进一步阐述见 ISO/IEC/IEEE 24748-1 和 ISO/IEC/IEEE 24748-2，它们就生存周期过程的应用提供了指南。

##### 5.2.4 Concepts related to the system solution context 与系统解决方案语境相关的概念

An SoI and its enabling systems are normally thought of as a solution addressing stakeholder concerns. The concerns of stakeholders are related to their business models. In particular, the concerns of an SoI supplier, an acquirer, and a user are different; this drives the need for them to consider different enabling systems to make the SoI viable in their own system solution context. Thus, the solution needs to consider the different stakeholder needs and business models.

一个 SoI 及其使能系统通常被视为应对利益相关方关注点的解决方案。利益相关方的关注点与其业务模式相关。特别是，SoI 的供应方、获取方和用户的关注点各不相同；这促使他们需要考虑不同的使能系统在其各自的系统解决方案语境中使 SoI 可行。因此，解决方案需要考虑利益相关方不同的需要和业务模式。

> **EXAMPLE** A manufacturing system is necessary for the supplier and is usually not considered by users and acquirers.

> **示例**：制造系统对供应方而言是必需的，通常不为用户和获取方所考虑。

In this perspective, for a given SoI, the business or mission analysis process is intended to address the set of solution contexts (see Figure 3).

在这一视角下，对于给定的 SoI，业务或任务分析过程旨在处理解决方案语境的集合（见图 3）。

![Figure 3 — System solution contexts](ISO IEC IEEE 15288 2023.assets/fig-03.png)

**Figure 3 — System solution contexts**

**图 3 — 系统解决方案语境**

> **NOTE** Several operational concepts, acquisition contexts and deployments can be associated with a given SoI. This multi-dimensional life description is provided in ISO 15704.

> **注**：若干运行概念、获取语境和部署都能与给定的 SoI 相关联。这种多维度的生存描述在 ISO 15704 中给出。

Variants and options shall be specified for the SoI to address the set of solution contexts. Products and services are often considered in system families and product lines with identification of elements common to different projects, and variants and options per project (see ISO/IEC 26550 for more details). Development of systems, products, and services often benefit from the identification of reuse opportunities between projects, including the establishment of product lines, families of products, systems, and systems of systems. These assets available for the projects are managed through the application of the knowledge management process.

应为 SoI 规定变体和选项，以应对解决方案语境的集合。产品和服务常常在系统族和产品线中加以考虑，并识别不同项目共有的元素以及各项目的变体和选项（详见 ISO/IEC 26550）。系统、产品和服务的开发常常得益于识别项目之间的复用机会，包括建立产品线、产品族、系统族和系统的系统。这些可供项目使用的资产，通过应用知识管理过程来管理。

##### 5.2.5 Product line engineering (PLE) 产品线工程（PLE）

When an organization develops a product line, engineering the product line holistically is much more effective and efficient than engineering each of the individual systems. This requires engineering the product line as a single SoI, with variations defined to support the individual system instances, for much of the life cycle. However, at the point in the life cycle where a specific system instance is developed, validated, and deployed into operation – an individual member of the product line – that system becomes an SoI itself that can continue with its own post-development life cycle, which can include production, support, utilization, retirement, and more. Variation management models are applied to manage the definition and production of the system instances. Whereas PLE generally focuses on the benefits of using a common platform with reusable assets for a product family, feature-based PLE addresses PLE in a holistic and automated manner (see ISO/IEC 26580).

当一个组织开发一条产品线时，对产品线进行整体工程化，其效果和效率都远高于对各个单独系统逐一进行工程化。这要求在生存周期的大部分时间里，将产品线作为单一的 SoI 来工程化，并定义变体以支持各个系统实例。然而，在生存周期中开发、确认并部署某个特定系统实例——产品线的单个成员——之时，该系统本身即成为 SoI，能继续其自身的开发后生存周期，其中可包括生产、保障、使用、退役等。应用变化管理模型来管理系统实例的定义和生产。PLE 通常关注产品族使用带有可复用资产的通用平台所带来的收益，而基于特征的 PLE 则以整体化、自动化的方式处理产品线工程（见 ISO/IEC 26580）。

In this approach, all of the system life cycle processes apply both when the product line is viewed as the SoI and when each instance of the product line with its variations is considered the SoI. From the holistic product line SoI perspective, many of the artefacts developed through the life cycle processes are shared across multiple members of the product line, which adds to the efficiency.

在这种方法中，无论将产品线视为 SoI，还是将产品线的每个实例连同其变化视为 SoI，所有系统生存周期过程都同样适用。从整体产品线 SoI 的视角看，通过生存周期过程开发的许多人工制品在产品线的多个成员之间共享，从而提高了效率。

The following are key tenets of feature-based PLE:

以下为基于特征的产品线工程的关键原则：

- A collective set of features for the system instances in the product line (called the feature catalogue in

- 产品线中各系统实例的一组集合性特征（在

ISO/IEC 26580) captures the distinguishing characteristics of how the members of the product line differ from each other and provides a common language of variation throughout the organization. The feature catalogue is a special type of MBSE (model-based systems engineering) model that helps to analyse and address the variations in the product line (see Annex D).

ISO/IEC 26580 中称为特征目录）捕获产品线各成员彼此区别的显著特性，并在整个组织内提供一种关于变化的通用语言。特征目录是一种特殊类型的 MBSE（基于模型的系统工程）模型，有助于分析和处理产品线中的变化（见附录 D）。

- The features selected for a system instance in a product line portfolio are specified in a collection of

- 为产品线项目组合中某个系统实例所选择的特征，规定在一组

features applicable to that instance (called the bill of features in ISO/IEC 26580).

适用于该实例的特征之中（在 ISO/IEC 26580 中称为特征清单）。

- All engineering artefacts that support the creation, design, implementation, deployment, and

- 支持产品的创建、设计、实现、部署和

operation of products are identified and maintained as a single copy of all content used in any system in the product line – i.e. no duplication (called shared asset supersets in ISO/IEC 26580). Content used in all products is common content, which is managed collectively for the product line. Content that varies in one or more system instances is encapsulated with its variations (called the variation points in ISO/IEC 26580), which can be included, omitted, generated, or transformed for a given system instance, based on selected features.

运行的所有工程人工制品，都作为产品线中任何系统所用全部内容的单一副本加以识别和维护——即不重复（在 ISO/IEC 26580 中称为共享资产超集）。所有产品都使用的内容为公共内容，对产品线统一管理。在一个或多个系统实例中发生变化的内容连同其变化一起封装（在 ISO/IEC 26580 中称为变化点），这些内容能基于所选特征，针对给定的系统实例被包含、省略、生成或变换。

- A system instance is comprised of the variation points, automatically derived according to the

- 系统实例由变化点（根据

selected features for the instance, plus all common content.

为该实例所选择的特征自动导出）加上全部公共内容构成。

#### 5.3 Organizational concepts 组织概念

##### 5.3.1 Organizations 组织

When an organization, as a whole or a part, enters into an agreement, it is sometimes called a “party” to the agreement. Parties can be from the same organization or from separate organizations. An organization can be as small as a single individual, if the individual is assigned responsibilities and authorities.

当一个组织整体或其中一部分订立协议时，有时被称为协议的“当事方”。当事方能来自同一组织，也能来自不同的组织。一个组织能小到仅为一个人，只要为该人分配了职责和权限。

In informal terms, the organization that is responsible for executing a process is sometimes referred to by the name of that process. For example, the organization executing the acquisition process is sometimes called the “acquirer”. Other examples include supplier, implementer, maintainer, and operator.

用非正式的表述来说，负责执行某个过程的组织，有时以该过程的名称来指称。例如，执行获取过程的组织有时被称为“获取方”。其他例子包括供应方、实现方、维护方和运行方。

A few other terms are applied to organizations in this document: "user" can be the organization that benefits from the utilization of the product or service; "customer" refers to the user and acquirer collectively; and "stakeholder" refers to an individual or organization with an interest in the system.

本文档对组织还使用了另外几个术语：“用户”能是从产品或服务的使用中获益的组织；“顾客”统指用户和获取方；“利益相关方”则指对系统存有利益的个人或组织。

The processes and organizations are only related functionally. This document does not dictate or imply a structure for an organization, nor does it specify that particular processes are to be executed by particular parts of the organization. It is the responsibility of the organization that implements this document to define a suitable structure for the organization and assign appropriate roles and responsibilities for the execution of processes.

过程与组织仅在功能上相关。本文档不规定也不暗示组织的结构，亦不规定特定过程须由组织的特定部分执行。实施本文档的组织有责任为该组织定义适宜的结构，并为过程的执行分配适当的角色和职责。

The processes in this document form a comprehensive set to serve various organizations. An organization, small or large, depending on its purpose or its acquisition strategy, can select an appropriate set of the processes (and associated activities and tasks) to fulfil that purpose. An organization may perform one process or more than one process.

本文档中的过程构成一套完备的集合，以服务于各类组织。一个组织，无论规模大小，都能根据其目的或获取策略选择一组适当的过程（以及相关的活动和任务）来实现该目的。一个组织可执行一个过程，也可执行多个过程。

This document is intended to be applied by an organization internally or by two or more organizations. When applied internally, the two agreeing parties typically act under the terms of an agreement that may vary in formality under different circumstances. When applied externally, the two agreeing parties typically act under the terms of a contract. This document uses the term “agreement” to apply to either situation.

本文档拟由一个组织内部应用，或由两个或多个组织应用。在内部应用时，两个达成一致的当事方通常依据一项协议的条款行事，该协议的形式程度在不同情形下可有所不同。在外部应用时，两个达成一致的当事方通常依据一份合同的条款行事。本文档用“协议”这一术语涵盖这两种情形。

For the purpose of this document, any project is assumed to be conducted within the context of an organization. This is important because a project is dependent upon various outcomes produced by the processes of the organization, e.g. employees to staff the project and facilities to house the project. For this purpose, this document provides a set of “organizational project-enabling” processes. These processes are not assumed to be adequate to operate an organization; instead, the processes, considered as a collection, are intended to state the minimum set of dependencies that the project places upon the organization.

就本文档而言，假定任何项目都是在某个组织的语境中实施的。这一点很重要，因为项目依赖于该组织各过程所产生的各种预期结果，例如为项目配备的人员和容纳项目的设施。为此，本文档提供了一组“组织项目使能”过程。这些过程并不被认为足以运行一个组织；相反，这些过程作为一个集合，旨在陈述项目对组织所提出的最低限度的依赖集合。

##### 5.3.2 Organization and project-level adoption 组织层面与项目层面的采用

Modern organizations strive to develop a robust set of life cycle processes that are applied repeatedly to the projects of the organization. Therefore, this document is intended to be useful for adoption at either the organization level or at the project level. An organization would adopt this document and supplement it with appropriate procedures, practices, tools, and policies. A project of the organization would typically conform to the organization's processes rather than conform directly to this document.

现代组织力求建立一套健全的生存周期过程，并反复应用于本组织的各个项目。因此，本文件旨在可供组织层面或项目层面采用。组织会采纳本文件，并以适宜的程序、实践、工具和方针予以补充。组织的项目通常符合本组织的过程，而不是直接符合本文件。

In some cases, projects may be executed by an organization that does not have an appropriate set of processes adopted at the organizational level. Such a project may directly adopt the provisions of this document.

在某些情况下，项目可能由尚未在组织层面采纳适宜过程集的组织来执行。此类项目可直接采纳本文件的规定。

##### 5.3.3 Organization and collaborative activities 组织与协作活动

Due to the increasing complexities of system solutions, it is often useful to employ collaborative and concurrent engineering approaches across the system life cycle. The following are some considerations:

由于系统解决方案日益复杂，在整个系统生存周期中采用协作式与并行式工程途径往往是有益的。以下是一些考虑事项：

- System life cycle activities are performed in a collaborative manner by involving stakeholders and

- 系统生存周期活动以协作方式开展，让利益相关方与

subject matter experts concurrently, as practical.

领域专家在实际可行时同时参与。

- A collaborative framework can be defined within an organization or between organizations to

- 可在组织内部或组织之间定义协作框架，以

facilitate the involvement of the range of stakeholders and experts. A collaborative framework includes shared methods, tools, and other resources, and establishes an environment for better communication and shared vision and values.

便于各类利益相关方与专家参与。协作框架包括共享的方法、工具及其他资源，并营造有利于更好沟通以及共享愿景与价值观的环境。

- Collaborative engineering is an essential element of iterative or incremental development approaches

- 协作工程是迭代式或增量式开发途径的基本要素，

to help ensure timely feedback and communication across the stakeholders.

有助于确保各利益相关方之间及时反馈与沟通。

#### 5.4 System of systems concepts 系统的系统概念

##### 5.4.1 Differences between systems and SoS 系统与 SoS 之间的差异

An SoS is a set of systems that interact to provide a unique capability that none of the constituent systems can accomplish on its own. In the context of SoS, the relevant pieces of the SoI are, by definition, systems themselves. An SoS consists of some number of constituent systems, plus any inter-system infrastructure, facilities, and processes necessary to enable the constituent systems to integrate or interoperate.

SoS 是一组相互作用的系统，用以提供任何单个构成系统都无法自行实现的独特能力。在 SoS 语境中，按定义，SoI 的相关组成部分本身就是系统。SoS 由若干构成系统，以及为使这些构成系统能够集成或互操作所必需的系统间基础设施、设施和过程组成。

Within an SoS, each constituent system is an independent system that forms part of an SoS. Constituent systems can be part of one or more SoS. Each constituent system is a useful system by itself, having its own development, management, utilization, goals, and resources, but interacts within the SoS to provide the unique capability of the SoS. These additional attributes are what distinguish SoS from a collection of systems.

在 SoS 中，每个构成系统都是构成 SoS 一部分的独立系统。构成系统能属于一个或多个 SoS。每个构成系统本身即是有用的系统，有其自身的开发、管理、使用、目标和资源，但在 SoS 内相互作用以提供 SoS 的独特能力。正是这些附加属性将 SoS 与系统的集合区分开来。

A system may interact as part of one or more SoS in support of multiple capabilities. In this document, when the interaction of an SoI with an SoS is discussed, this may include one or more SoS in support of one or more capabilities.

系统能作为一个或多个 SoS 的一部分相互作用，以支持多种能力。在本文件中，当讨论 SoI 与 SoS 的相互作用时，可包括支持一种或多种能力的一个或多个 SoS。

The differences between systems and SoS are not in the structure or arrangement of the individual elements, but rather in the behavioural and managerial characteristics of those elements.

系统与 SoS 之间的差异不在于各单个元素的结构或排列，而在于这些元素的行为特征与管理特征。

##### 5.4.2 Managerial and operational independence 管理独立性与运行独立性

Systems operate within a context of managerial control subject to governance. Organizations govern a portfolio of programmes through goals and objectives, subject to laws, regulations, and external agreements such as contracts. Programmes manage some number of projects to achieve those goals and objectives. Relationships between constituent systems affect the SoS. Systems that do not have any interactions with the constituent systems of a subject SoS are not part of that SoS.

系统在受治理约束的管理控制语境中运行。组织通过目标和目的治理由若干项目群构成的组合，并受法律、法规以及合同等外部协议的约束。项目群管理若干项目以实现这些目标和目的。构成系统之间的关系影响 SoS。与所关注 SoS 的构成系统没有任何相互作用的系统，不属于该 SoS。

An essential characteristic of the SoS is that constituent systems within the SoS are operationally independent. That is, the constituent systems can (and do) operate independently to fulfil some number of purposes on their own, separate from the SoS. While constituent systems operate independently from each other for their own purposes, they also operate interdependently with each other and other elements to produce the SoS outputs. Constituent systems are never totally independent, yet they are also never totally subservient to the SoS.

SoS 的一项基本特征是其构成系统在运行上相互独立。也就是说，构成系统能（并且确实）脱离 SoS 独立运行，以自行实现若干目的。构成系统为自身目的彼此独立运行，同时又彼此以及与其他元素相互依赖地运行，以产生 SoS 的输出。构成系统从不是完全独立的，但也从不是完全从属于 SoS 的。

Another essential characteristic is that constituent systems within the SoS are both managerially independent and interdependent. Managerial independence suggests that the constituent systems can be managed by organizations that retain some degree of independence even though they are interdependent while participating in SoS. The implication is that these organizations can have goals and objectives for the constituent systems that differ from those of the SoS and the other constituent systems. If so, there is likely some degree of independence and interdependence of governance, as well as some degree of independence and interdependence of management.

另一项基本特征是，SoS 内的构成系统既在管理上独立，又相互依赖。管理独立性意味着，构成系统能由在参与 SoS 时虽相互依赖但仍保持某种程度独立的组织来管理。其含义是，这些组织可为构成系统设定不同于 SoS 及其他构成系统的目标和目的。若如此，治理可能存在某种程度的独立性与相互依赖，管理也可能存在某种程度的独立性与相互依赖。

Regardless of the means of managing the organizations, alignment (or lack thereof) in the goals and objectives affects the SoS. While some constituent systems are directed or influenced to belong to SoS, some constituent systems can be unaware of the SoS. Some constituent systems choose to belong on a cost/benefits basis, also to cause greater fulfilment of their own purposes, and because of their belief in the overarching SoS purpose.

无论以何种方式管理这些组织，目标和目的上的一致（或不一致）都会影响 SoS。有些构成系统是被指示或受影响而属于 SoS 的，也有些构成系统可能并不知晓该 SoS。有些构成系统基于成本／效益选择加入，同时也是为了更大程度地实现自身目的，并出于对 SoS 总体目的的信念。

##### 5.4.3 Taxonomy of SoS SoS 的分类法

Using essential characteristics to partition the various types of SoS provides an abbreviated nomenclature for thinking about SoS. ISO/IEC/IEEE 21841 defines a normalised taxonomy for systems of systems (SoS) to facilitate communications among stakeholders. It also briefly explains what a taxonomy is and how it applies to the SoS to aid in understanding and communication. There are many characteristics such as scale and scope, around which taxonomies can be derived.

利用基本特征划分各类 SoS，可提供一套简明的命名体系以思考 SoS。ISO/IEC/IEEE 21841 定义了系统的系统（SoS）的规范化分类法，以便于利益相关方之间的沟通。它还简要说明了什么是分类法以及分类法如何应用于 SoS，以帮助理解与沟通。诸如规模与范围等许多特征都可作为推导分类法的依据。

The SoS taxonomy in ISO/IEC/IEEE 21841 organizes the relevant aspects or essential characteristics of SoS, providing specific viewpoints that align with stakeholder concerns. This organization facilitates communications between the various stakeholders that are involved with activities like governance, engineering, operation, and management of these SoS, and provides a reference for other related standards.

ISO/IEC/IEEE 21841 中的 SoS 分类法组织了 SoS 的相关方面或基本特征，提供了与利益相关方关注点相一致的具体视角。这种组织方式便于参与这些 SoS 的治理、工程、运行和管理等活动的各类利益相关方之间沟通，并为其他相关标准提供参考。

ISO/IEC/IEEE 21841 can be useful when describing an SoS or comparing SoS.

在描述 SoS 或对 SoS 进行比较时，ISO/IEC/IEEE 21841 能提供帮助。

##### 5.4.4 SoS considerations in life cycle stages of a system 系统生存周期阶段中的 SoS 考虑事项

ISO/IEC/IEEE 21839 provides a set of SoS considerations to be addressed at key points in the life cycle of the SoI. The considerations and key points align with those which are introduced in this document. Selected subsets of these considerations can be applied throughout the life of systems through the involvement of stakeholders. The ultimate goal is to achieve stakeholder satisfaction, so that when delivered, the SoI operates effectively in the operational environment which is typically characterized as one or more systems of systems.

ISO/IEC/IEEE 21839 提供了一组在 SoI 生存周期关键点上应予考虑的 SoS 考虑事项。这些考虑事项和关键点与本文件中引入的相一致。通过利益相关方的参与，可选择其中若干子集应用于系统的整个生存期。最终目标是实现利益相关方满意，从而使 SoI 在交付后能在通常表现为一个或多个系统的系统的运行环境中有效运行。

A constituent system can be an entity in more than one SoS. An SoS is often comprised of existing constituent systems along with new constituent systems which are developed and integrated into the SoS. The focus of ISO/IEC/IEEE 21839 is a constituent system as the SoI. The considerations provided in ISO/IEC/IEEE 21839 are with respect to what is necessary to account for the life cycle of the constituent system to enable it to interact in the anticipated SoS configurations.

一个构成系统能是多个 SoS 中的实体。SoS 通常由既有构成系统，以及新开发并集成到该 SoS 中的新构成系统组成。ISO/IEC/IEEE 21839 的关注点是以构成系统作为 SoI。ISO/IEC/IEEE 21839 中提供的考虑事项所针对的是：为使构成系统能在预期的 SoS 配置中相互作用，对其生存周期需要纳入考虑的内容。

ISO/IEC/IEEE 21839 can be useful as an augmentation to this document when the SoI is a constituent system within an SoS, which is the typical situation for current systems.

当 SoI 是 SoS 中的构成系统（当前系统通常即属此情形）时，ISO/IEC/IEEE 21839 能作为对本文件的补充而发挥作用。

##### 5.4.5 Application of this document to SoS 本文件对 SoS 的应用

ISO/IEC/IEEE 21840 provides guidance for the utilization of this document in the context of SoS. While this document applies to systems in general (including constituent systems), ISO/IEC/IEEE 21840 provides guidance on the application of these processes to the special case of SoS. However, ISO/IEC/IEEE 21840 is not a self-contained SoS replacement for this document. ISO/IEC/IEEE 21840 is intended to be used in conjunction with this document, ISO/IEC/IEEE 21839, and ISO/IEC/IEEE 21841 and is not intended to be used as standalone guidance.

ISO/IEC/IEEE 21840 为在 SoS 语境下使用本文件提供指南。本文件适用于一般意义上的系统（包括构成系统），而 ISO/IEC/IEEE 21840 则为将这些过程应用于 SoS 这一特殊情形提供指南。然而，ISO/IEC/IEEE 21840 并不是本文件在 SoS 情形下的自包含替代文件。ISO/IEC/IEEE 21840 旨在与本文件、ISO/IEC/IEEE 21839 和 ISO/IEC/IEEE 21841 结合使用，其本意并非用作独立指南。

When the SoI is part of an SoS, the application of the processes in this document is dependent on the type of SoS life cycle and impact of the SoS interactions on the SoI. In some cases, there can be “waves” of SoS revision. In other cases, SoS changes occur continually, with many processes operating on a continuous basis to implement evolutionary change.

当 SoI 是 SoS 的一部分时，本文件中各过程的应用取决于 SoS 生存周期的类型以及 SoS 交互对 SoI 的影响。在某些情形下，可能存在 SoS 修订的“波次”；在另一些情形下，SoS 变更不断发生，许多过程持续运行以实现演进式变更。

#### 5.5 Life cycle concepts 生存周期概念

##### 5.5.1 System life cycle model 系统生存周期模型

Every system has a life cycle. A life cycle can be described using an abstract functional model that represents the conceptualization of a need for the system, its realization, utilization, evolution, and disposal.

每个系统都有生存周期。生存周期能用抽象的功能模型来描述，该模型表征对系统需要的概念化以及系统的实现、利用、演进和处置。

A system progresses through its life cycle as the result of actions, performed and managed by people in organizations, using processes for execution of these actions. The detail in the life cycle model is expressed in terms of these processes, their outcomes, relationships, and sequence. This document does not prescribe any particular life cycle model. Instead, it defines a set of processes, termed life cycle processes, that can be used in the definition of the system's life cycle. The processes described in this document support sequential as well as iterative and incremental development models. Also, this document does not prescribe any particular sequence of processes within the life cycle model. The sequence of the processes is determined by project objectives and by selection of the system life cycle model.

系统在其生存周期中推进，是组织中的人员执行和管理的行动的结果，这些行动借助过程来实施。生存周期模型中的细节以这些过程及其预期结果、关系和顺序来表述。本文件不规定任何特定的生存周期模型，而是定义了一组称为生存周期过程的过程，它们能用于定义系统的生存周期。本文件所述过程既支持顺序式开发模型，也支持迭代式和增量式开发模型。此外，本文件不规定生存周期模型内过程的任何特定顺序。过程的顺序由项目目标和系统生存周期模型的选择决定。

##### 5.5.2 System life cycle stages 系统生存周期阶段

Life cycles vary according to the nature, purpose, use, and prevailing circumstances of the system. Each stage has a distinct purpose and contribution to the whole life cycle and is considered when planning and executing the system life cycle. The life cycle model comprises one or more stages, as needed. It is assembled as a sequence of stages that can be iterative, concurrent, or overlapping, as appropriate for the SoI's scope, magnitude, complexity, changing needs, and opportunities.

生存周期随系统的性质、目的、用途和所处境况而变化。每个阶段都有其独特的目的，并对整个生存周期有所贡献，在策划和执行系统生存周期时予以考虑。生存周期模型按需要包含一个或多个阶段，它由一系列阶段组合而成；这些阶段能是迭代的、并发的或重叠的，以适应 SoI 的范围、规模、复杂性、变化中的需要和机遇。

The stages represent the major life cycle periods associated with a system and they relate to the state of the system description or the system itself. The stages describe the major progress and achievement milestones of the system through its life cycle. They give rise to the primary decision gates of the life cycle. These decision gates apply specific decision criteria and are used by organizations to understand and manage the inherent uncertainties and risks associated with business case, costs, schedule, performance, or functionality of a system. The stages thus provide a framework within which organization management has high-level visibility and control of technical management and technical processes. ISO/IEC/IEEE 24748-1 describes the application of these processes in any stage, provides more details on decision gates, and defines typical system life cycle stages, including

阶段代表与系统相关的主要生存周期时期，并与系统描述或系统本身的状态有关。阶段描述系统在其生存周期中的主要进展和成就里程碑。它们引出生存周期的主要决策门。这些决策门应用特定的决策准则，被组织用来理解和管理与系统的商业论证、成本、进度、性能或功能相关的固有不确定性和风险。因此，阶段提供了一个框架，组织管理层据此对技术管理过程和技术过程拥有高层级的可见性和控制。ISO/IEC/IEEE 24748-1 描述了这些过程在任何阶段中的应用，给出了关于决策门的更多细节，并定义了典型的系统生存周期阶段，包括

- concept;

- 概念；

- development;

- 开发；

- production;

- 生产；

- utilization;

- 利用；

- support;

- 保障；

- retirement.

- 退役。

Note that there are significant differences between life cycle stages (e.g. utilization, support, retirement) and processes (e.g. operation, maintenance, disposal).

注意，生存周期阶段（例如利用、保障、退役）与过程（例如运行、维护、处置）之间存在显著差异。

Organizations employ stages differently to satisfy contrasting strategies. The life cycle stages often occur concurrently, especially in continuous, incremental, or evolutionary approaches. Using stages concurrently and in different orders can lead to life cycle forms with distinctly different characteristics.

各组织以不同方式运用阶段，以满足取向各异的策略。生存周期阶段常常同时出现，在连续式、增量式或演进式途径中尤为如此。并发地并以不同顺序使用阶段，能导致特征明显不同的生存周期形态。

Further elaboration of these concepts can be found in ISO/IEC/IEEE 24748-1 and ISO/IEC/IEEE 24748-2, which provide guidelines on the application of life cycle management.

关于这些概念的进一步阐述见 ISO/IEC/IEEE 24748-1 和 ISO/IEC/IEEE 24748-2，它们就生存周期管理的应用提供了指南。

> **NOTE** The set of events, occurrences, and evolution across the life cycle is sometimes referred to as the system life history. Per ISO 15704, the life history is the actual, recorded and configuration managed sequence of steps the system has gone through during its lifetime.

> **注**：贯穿生存周期的事件、发生情况和演进的集合，有时称为系统生存史。按照 ISO 15704，生存史是系统在其寿命期内所经历的实际的、有记录且经配置管理的步骤序列。

#### 5.6 Process concepts 过程概念

##### 5.6.1 Criteria for processes 过程的准则

The determination of the life cycle processes in this document is based upon three basic principles:

本文件对生存周期过程的确定基于三项基本原则：

- Each life cycle process has strong relationships among its outcomes, activities, and tasks.

- 每个生存周期过程在其预期结果、活动和任务之间具有紧密的关系。

- The dependencies among the processes are reduced to the greatest feasible extent.

- 各过程之间的依赖关系被降到可行的最大程度。

- A process is capable of execution by a single organization in the life cycle.

- 一个过程能由生存周期中的单个组织来执行。

##### 5.6.2 Description of processes 过程的描述

Each process of this document is described in terms of the following attributes:

本文件的每个过程按以下属性加以描述：

- The title conveys the scope of the process as a whole.

- 标题传达过程作为整体的范围。

- The purpose describes the goals of performing the process.

- 目的描述执行该过程的目标。

- The outcomes express the observable results expected from the successful performance of the

- 预期结果表达成功执行该过程所期望的

process.

可观察结果。

- The activities are sets of cohesive tasks of a process.

- 活动是过程的内聚任务集。

- The tasks are requirements intended to support the achievement of the outcomes.

- 任务是旨在支持达成预期结果的要求。

Additional detail regarding this form of process description can be found in ISO/IEC/IEEE 24774. Outputs are an optional attribute for a process description. They are artefacts or information items. Annex B includes examples of outputs from the processes.

关于这种过程描述形式的更多细节见 ISO/IEC/IEEE 24774。输出是过程描述的可选属性，它们是人工制品或信息部件。附录 B 给出了各过程输出的示例。

##### 5.6.3 General characteristics of processes 过程的一般特征

In addition to the basic attributes described in 5.6.2, processes may be characterized by other attributes common to all processes. The ISO/IEC 33000 family of standards identifies common process attributes that characterize six levels of achievement within a measurement framework for process capability.

除 5.6.2 所述的基本属性外，过程还可具有所有过程共有的其他属性。ISO/IEC 33000 系列标准识别出若干通用过程属性，它们在过程能力的测量框架内刻画六个达成等级。

#### 5.7 Processes in this document 本文件中的过程

##### 5.7.1 General 总则

This document groups the activities that can be performed during the life cycle of a system into four process groups:

本文件把能在系统的生存周期中执行的活动归入四个过程组：

a) agreement processes;

a) 协议过程；

b) organizational project-enabling processes;

b) 组织项目使能过程；

c) technical management processes;

c) 技术管理过程；

d) technical processes.

d) 技术过程。

The groups and the processes included in each group are depicted in Figure 4. Each of the life cycle processes is described in terms of its purpose and desired outcomes with a set of related activities and tasks that can be performed to achieve those outcomes.

各过程组及每组所包含的过程如图 4 所示。每个生存周期过程都按其目的和所期望的预期结果来描述，并配有一组为达成这些预期结果而可执行的相关活动和任务。

The processes described in this document are not intended to preclude or discourage the use of additional processes that organizations find useful. The order of the subclauses in which the processes are defined in this document does not determine the order in which the processes are performed during the system life cycle or any of its stages (i.e. there is no prescriptive order or sequence). A description of each process group is provided in 5.7.2 to 5.7.5.

本文件所述过程无意排除或阻止组织使用其认为有用的其他过程。本文件中定义各过程的子条款的顺序，并不决定各过程在系统生存周期或其任何阶段中执行的顺序（即不存在规定性的顺序或序列）。5.7.2 至 5.7.5 给出了各过程组的描述。

![Figure 4 — System life cycle processes](ISO IEC IEEE 15288 2023.assets/fig-04.png)

**Figure 4 — System life cycle processes**

**图 4 — 系统生存周期过程**

##### 5.7.2 Agreement processes 协议过程

Organizations are producers and users of systems. One organization (acting as an acquirer) can task another (acting as a supplier) for products or services. This is achieved using agreements. Agreements allow both acquirers and suppliers to realise value and support strategies for their organizations.

组织是系统的生产者和使用者。一个组织（作为获取方）能就产品或服务向另一个组织（作为供应方）下达任务。这通过协议来实现。协议使获取方和供应方均能实现价值，并支持各自组织的战略。

Generally, organizations act simultaneously or successively as both acquirers and suppliers of systems. The agreement processes can be used with less formality when the acquirer and the supplier are in the same organization. Similarly, they can be used within the organization to agree on the respective responsibilities of organization, project, and technical functions.

一般而言，组织同时或先后充当系统的获取方和供应方。当获取方与供应方处于同一组织内时，协议过程能以正式程度较低的方式使用。同样，协议过程也能在组织内部使用，以就组织、项目和技术职能各自的职责达成一致。

The agreement processes consist of the following (also see Figure 4):

协议过程由下列各项组成（另见图 4）：

a) acquisition process – used by organizations for acquiring products or services;

a) 获取过程 – 供组织用于获取产品或服务；

b) supply process – used by organizations for supplying products or services.

b) 供应过程 – 供组织用于供应产品或服务。

These processes define the activities necessary to establish an agreement between two organizations. If the acquisition process is invoked, it provides the means for interacting with a supplier. This may include products that are supplied for use as an operational system, services in support of operational activities, or elements of a system being provided by a supplier. If the supply process is invoked, it provides the means for an agreement for a product or service that is provided to the acquirer.

这些过程定义了在两个组织之间建立协议所必需的活动。若调用获取过程，该过程提供了与供应方相互作用的手段。这可包括为用作运行系统而供应的产品、支持运行活动的服务，或由供应方提供的系统元素。若调用供应过程，该过程提供了就向获取方提供的产品或服务订立协议的手段。

> **NOTE 1** Security is an increasing concern in systems engineering. See the ISO/IEC 27036 series for requirements and guidance for suppliers and acquirers on how to secure information in supplier relationships. Specific aspects of information security supplier relationships are addressed in ISO/IEC 27036-3 and ISO/IEC 27036-4.

> **注 1**：安全在系统工程中日益受到关注。关于供应方和获取方如何在供应方关系中保护信息，其要求与指南见 ISO/IEC 27036 系列。安全中供应方关系的具体方面在 ISO/IEC 27036-3 和 ISO/IEC 27036-4 中述及。

When an SoI participates as part of an SoS, it is often necessary to consider the resource and capability dependencies in the performance of the agreement processes. As needed, the agreements would include clauses for the SoS interactions and dependencies or additional agreements generated. The processes apply for the agreements between the stakeholders of the SoI and interoperating systems. If there is an external entity with some type of responsibility that spans an SoS in which the SoI is a constituent system, then management and support arrangements can be required with that external entity. The agreements establish the responsibilities and modes of support and control across the life cycle stages among the stakeholder organizations from the context of the SoI participation in the SoS. This is of greater importance if the organization holds primary objectives for their constituent system that may not be directly aligned with those of the SoS.

当 SoI 作为 SoS 的一部分参与时，在实施协议过程时往往需要考虑资源与能力方面的依赖关系。视需要，协议会载入针对 SoS 相互作用与依赖的条款，或生成附加协议。这些过程适用于 SoI 的利益相关方与互操作系统之间的协议。若存在某一外部实体，其某类职责跨越以 SoI 为构成系统的某个 SoS，则可能需要与该外部实体作出管理与支持安排。协议从 SoI 参与 SoS 的语境出发，确立各利益相关方组织在生存周期各阶段中的职责以及支持与控制方式。若组织为其构成系统设定的主要目标可能与 SoS 的目标并不直接一致，这一点就更为重要。

> **NOTE 2** More information about process application for the SoS is provided in ISO/IEC/IEEE 21839 and ISO/IEC/IEEE 21840.

> **注 2**：关于 SoS 的过程应用的更多信息见 ISO/IEC/IEEE 21839 和 ISO/IEC/IEEE 21840。

##### 5.7.3 Organizational project-enabling processes 组织项目使能过程

The organizational project-enabling processes are concerned with providing the resources needed to enable the project to meet the needs and expectations of the organization’s stakeholders. The organizational project-enabling processes are typically concerned at a strategic level with the management and improvement of the organization’s undertaking, with the provision and deployment of resources and assets, and with its management of risks in competitive or uncertain situations.

组织项目使能过程涉及提供必要的资源，以使项目能够满足组织利益相关方的需要与期望。组织项目使能过程通常在战略层面关注对组织所开展事业的管理与改进、资源与资产的提供与部署，以及在竞争性或不确定性情形下的风险管理。

The organizational project-enabling processes establish the environment in which projects are conducted. The organization establishes the processes and life cycle models to be used by projects; establishes, redirects, or cancels projects; provides resources required, including human and financial; and sets and monitors the quality measures for systems and other deliverables that are developed by projects to satisfy internal and external customers.

组织项目使能过程确立项目得以开展的环境。组织确立供项目使用的过程和生存周期模型；设立、重新定向或取消项目；提供所需的资源，包括人力和财力资源；并为项目为满足内部和外部顾客而开发的系统及其他交付物设定并监视质量测量。

The organizational project-enabling processes do not necessarily imply commercial or profit-making motives. Organizational project-enabling processes are equally relevant to non-profit organizations, since they are also accountable to stakeholders, are responsible for resources and encounter risk in their undertakings. This document can be applied to non-profit organizations as well as to profit- making organizations. In addition, organizational project-enabling processes are not intended to be a comprehensive set of organizational processes that enable strategic management of the organization.

组织项目使能过程并不必然意味着商业或营利动机。组织项目使能过程对非营利组织同样适用，因为非营利组织也要对利益相关方负责，也对资源负有责任，并在其事业中面临风险。本文件既能适用于非营利组织，也适用于营利性组织。此外，组织项目使能过程并非旨在成为使能组织战略管理的全套组织过程。

The organizational project-enabling processes consist of the following (also see Figure 4):

组织项目使能过程由下列各项组成（另见图 4）：

a) life cycle model management process;

a) 生存周期模型管理过程；

b) infrastructure management process;

b) 基础设施管理过程；

c) portfolio management process;

c) 项目组合管理过程；

d) human resource management process;

d) 人力资源管理过程；

e) quality management process;

e) 质量管理过程；

f) knowledge management process.

f) 知识管理过程。

In a typical SoI, organizational project-enabling processes establish the environment and provide the necessary resources for the conduct of projects to address system solutions. The organization establishes the processes and life cycle models to be used by projects; establishes, redirects, or cancels projects; provides resources required, including human, material and financial; and sets and monitors the quality measures for systems and other deliverables that are developed by projects for internal and external customers. These processes also provide the environment and resources for the SoI to be able to support capabilities provided by an SoS in which the SoI participates. The organizations responsible for the constituent systems implement these processes for their SoI independent of the SoS. These processes can be influenced by regulations, interface standards, or agreements for those parts of the SoI that contribute to the overall SoS capabilities.

在典型的 SoI 中，组织项目使能过程确立环境并提供必要的资源，以开展旨在形成系统解决方案的项目。组织确立供项目使用的过程和生存周期模型；设立、重新定向或取消项目；提供所需的资源，包括人力、物力和财力资源；并为项目为内部和外部顾客开发的系统及其他交付物设定并监视质量测量。这些过程还为 SoI 提供环境和资源，使 SoI 能够支持其参与的 SoS 所提供的能力。负责各构成系统的组织为其 SoI 实施这些过程，而不依赖于该 SoS。对于 SoI 中有助于实现 SoS 总体能力的那些部分，这些过程可受到法规、接口标准或协议的影响。

> **NOTE** More information about process application for the SoS is provided in ISO/IEC/IEEE 21839 and ISO/IEC/IEEE 21840.

> **注**：关于 SoS 的过程应用的更多信息见 ISO/IEC/IEEE 21839 和 ISO/IEC/IEEE 21840。

##### 5.7.4 Technical management processes 技术管理过程

The technical management processes are concerned with managing the resources and assets allocated by organization management and with applying them to fulfil the agreements into which the organization or organizations enter. The technical management processes relate to the technical effort of projects, in particular to planning in terms of cost, timescales, and achievements; to the checking of actions to help ensure that they comply with plans and performance criteria; and to the identification and selection of corrective actions that recover shortfalls in progress and achievement. These processes are used to establish and perform technical plans for the project, manage information across the technical team, assess technical progress against the plans for the system products or services, control technical tasks through to completion, and to aid in the decision-making process. Individual technical management processes may be invoked at any time in the life cycle and at any level in a hierarchy of projects, as required by plans or unforeseen events. The technical management processes are applied with a level of rigor and formality that depends on the agreements as well as risk and complexity of the project.

技术管理过程涉及对组织管理层所分配的资源与资产进行管理，并将这些资源与资产用于履行组织所订立的协议。技术管理过程关乎项目的技术工作，特别是关乎在成本、时间进度和成果方面的策划；关乎对各项行动进行检查以帮助确保其符合计划和绩效准则；也关乎识别和选择能够弥补进展与成果不足的纠正措施。这些过程用于为项目建立并执行技术计划、在技术团队内管理信息、对照系统产品或服务的计划评定技术进展、控制技术任务直至完成，并协助决策过程。单个技术管理过程可在生存周期中的任何时候、在项目层次结构中的任何层级调用，视计划或未预见事件的需要而定。技术管理过程的实施所达到的严谨程度与正式程度，取决于协议以及项目的风险与复杂性。

> **NOTE 1** Technical management is ‘the application of technical and administrative resources to plan, organize, and control engineering functions’ (ISO/IEC/IEEE 24765).

> **注 1**：技术管理是‘为规划、组织和控制工程职能而应用技术资源与行政资源’（ISO/IEC/IEEE 24765）。

Typically, several projects co-exist in any one organization. The technical management processes can be employed at a corporate level to meet internal needs.

通常，任何一个组织中都会并存若干项目。技术管理过程能在企业层面采用，以满足内部需要。

> **NOTE 2** Technical management processes are applied during the performance of each technical process.

> **注 2**：技术管理过程在每个技术过程的执行期间应用。

The technical management processes can be applied to manage the technical activities through the life cycles of systems, including products or services.

技术管理过程能用于管理贯穿系统（包括产品或服务）生存周期的技术活动。

> **NOTE 3** This set of technical management processes are performed so that system-specific technical processes can be conducted effectively. They do not comprise a management system or a comprehensive set of processes for project management, as that is not within the scope of this document.

> **注 3**：执行这组技术管理过程，是为了使针对具体系统的技术过程能有效开展。它们并不构成管理体系，也不构成用于项目管理的一套完整过程，因为那不在本文件的范围内。

The technical management processes consist of the following (also see Figure 4):

技术管理过程包括下列各项（另见图 4）：

a) project planning process;

a) 项目规划过程；

b) project assessment and control process;

b) 项目评定与控制过程；

c) decision management process;

c) 决策管理过程；

d) risk management process;

d) 风险管理过程；

e) configuration management process;

e) 配置管理过程；

f) information management process;

f) 信息管理过程；

g) measurement process;

g) 测量过程；

h) quality assurance process.

h) 质量保证过程。

Project planning and project assessment and control are key to all management practices. These processes establish the general approach for managing a project or a process. The other processes in this group provide a specific focused set of tasks for performing to a specialised management objective. They are all evident in the management of any undertaking, ranging from a complete organization down to a single life cycle process and its tasks. In this document, the project is chosen as the context for describing processes. The same processes can also be applied in the performance of services.

项目规划以及项目评定与控制，是一切管理实践的关键。这两个过程确立管理一个项目或一个过程的一般途径。本组中的其他过程为达成某一专门的管理目标提供一组具体而有侧重的任务。从整个组织直到单个生存周期过程及其任务，在任何事业的管理中都能见到这些过程。在本文件中，选择项目作为描述过程的语境。这些过程也能应用于服务的执行。

Technical management processes are concerned with managing the resources and assets allocated by organization management and with applying them to fulfil the agreements into which the organization or organizations enter. The technical management processes need to include the considerations of the expected SoS interactions. The considerations span the planning, assessment, and management of resources, risks, and other factors associated with dependencies from other interacting systems. For example, the planning, assessment, and control activities need to include SoS-related cost and schedule considerations for the SoI. This includes monitoring the progress in the areas of cross-system dependencies. The agreement processes are executed to negotiate the required resources across stakeholders.

技术管理过程关注的是管理由组织管理层分配的资源与资产，并将它们用于履行该组织或多个组织所订立的协议。技术管理过程需要纳入对预期 SoS 相互作用的考虑事项。这些考虑事项涵盖与来自其他互操作系统的依赖关系相关联的资源、风险及其他因素的规划、评定和管理。例如，规划、评定与控制活动需要纳入针对 SoI 的与 SoS 相关的成本和进度考虑事项。这包括监视跨系统依赖关系领域的进展。执行协议过程，以在各利益相关方之间协商所需的资源。

> **NOTE 4** More information about process application for the SoS is provided in ISO/IEC/IEEE 21839 and ISO/IEC/IEEE 21840.

> **注 4**：关于 SoS 的过程应用的更多信息，见 ISO/IEC/IEEE 21839 和 ISO/IEC/IEEE 21840。

##### 5.7.5 Technical processes 技术过程

The technical processes are concerned with technical actions throughout the life cycle. Technical processes transform the needs of stakeholders into products or services. By applying that product or operating that service, technical processes provide sustainable performance, when and where needed, to meet the stakeholder requirements and achieve customer satisfaction. The technical processes are applied to create and use a system, whether it is in the form of a model or is a finished product.

技术过程关注的是贯穿生存周期的技术行动。技术过程将利益相关方的需要转换为产品或服务。通过应用该产品或运行该服务，技术过程在需要的时间和地点提供可持续的性能，以满足利益相关方需求并实现顾客满意。技术过程用于创建和使用系统，无论该系统是模型形式还是成品形式。

The technical processes are used to define the requirements for a system, to transform the requirements into an effective product, to permit consistent reproduction of the product where necessary, to use the product, to provide the required services, to sustain the provision of those services and to dispose of the product when it is retired from service.

技术过程用于：规定系统的需求；将需求转换为有效的产品；在必要时支持产品的一致复现；使用产品；提供所需的服务；维持这些服务的持续提供；并在产品退役时对其进行处置。

The technical processes define the activities that enable organization and project functions to optimise the benefits and reduce the risks that arise from technical decisions and actions. These activities enable products and services to possess the timeliness and availability, the cost effectiveness, and the functionality, reliability, maintainability, producibility, usability and other quality characteristics required by acquiring and supplying organizations. They also enable products and services to conform to the expectations, ethical perspectives, or legislated requirements of society.

技术过程所定义的活动，使组织职能与项目职能能够优化收益并降低由技术决策和技术行动产生的风险。这些活动使产品和服务具备获取组织和供应组织所要求的及时性与可用性、成本效益，以及功能、可靠性、维修性、可生产性、易用性和其他质量特性。这些活动还使产品和服务符合社会的期望、伦理观点或法律规定的要求。

The technical processes consist of the following (also see Figure 4):

技术过程包括下列各项（另见图 4）：

a) business or mission analysis process;

a) 业务或任务分析过程；

b) stakeholder needs and requirements definition process;

b) 利益相关方需要与需求定义过程；

c) system requirements definition process;

c) 系统需求定义过程；

d) system architecture definition process;

d) 系统架构定义过程；

e) design definition process;

e) 设计定义过程；

f) system analysis process;

f) 系统分析过程；

g) implementation process;

g) 实现过程；

h) integration process;

h) 集成过程；

i) verification process;

i) 验证过程；

j) transition process;

j) 转换过程；

k) validation process;

k) 确认过程；

l) operation process;

l) 运行过程；

m) maintenance process;

m) 维护过程；

n) disposal process.

n) 处置过程。

> **NOTE 1** For software and hardware system elements, these processes are applied at recursively lower levels for system definition and recursively higher levels for system realization.

> **注 1**：对于软件和硬件系统元素，这些过程在系统定义时应用于递归的更低层级，在系统实现时应用于递归的更高层级。

> **NOTE 2** These processes are often performed concurrently, iterating between one another to establish a solution that is balanced with respect to requirements, critical performance measures, critical quality characteristics, and SoS considerations. At any level of abstraction, system requirements and models are made consistent via iterations of applicable technical processes. When requirements and models are not directly capable of being implemented, the same processes are repeated recursively throughout the system structure.

> **注 2**：这些过程常常并行执行，彼此迭代，以确立在需求、关键性能度量、关键质量特性以及 SoS 考虑事项等方面平衡的解决方案。在任何抽象层级上，都通过适用技术过程的迭代使系统需求与模型保持一致。当需求与模型不能直接实现时，在系统结构中递归地重复同样的过程。

> **NOTE 3** Interface management is a set of activities that cut across the systems engineering processes. These are cross-cutting activities of the technical and technical management processes that apply and track as a specific view of the processes and system. See ISO/IEC/IEEE 24748-1 for an example interface management process view and INCOSE-TP-2003-002-5, Part III, section 3.2.4 for more information.

> **注 3**：接口管理是一组贯穿系统工程各过程的活动。这些活动是技术过程与技术管理过程的横切活动，以过程和系统的一种特定视图加以应用和追踪。接口管理过程视图的示例见 ISO/IEC/IEEE 24748-1，更多信息见 INCOSE-TP-2003-002-5 第 III 部分第 3.2.4 节。

Technical processes are concerned with technical actions throughout the life cycle of the SoI. As the technical processes are performed for the provision and support of technical solutions across the life cycle stages, SoS considerations for the SoI include the technical impact on interacting systems and their stakeholders and infrastructure. ISO/IEC/IEEE 21839 states that “this includes both systems/ services on which the SoI depends and systems/services that depend on the SoI”. This can impose new requirements or constraints on the SoI by the SoS configurations in which the SoI participated in support of required or desired business or mission capabilities. The SoS technical considerations apply to all the technical processes across the life cycle stages and play an especially important role in the business or mission analysis, stakeholder needs and requirements definition, system requirements definition, system architecture definition, and design definition processes.

技术过程关注的是贯穿 SoI 生存周期的技术行动。由于技术过程是为在生存周期各阶段提供和支持技术解决方案而执行的，因此针对 SoI 的 SoS 考虑事项包括对互操作系统及其利益相关方和基础设施的技术影响。ISO/IEC/IEEE 21839 指出，“这既包括 SoI 所依赖的系统／服务，也包括依赖 SoI 的系统／服务”。SoI 为支持所需或期望的业务或任务能力而参与其中的 SoS 配置，可能据此对 SoI 施加新的需求或约束。SoS 技术考虑事项适用于贯穿各生存周期阶段的所有技术过程，并在业务或任务分析、利益相关方需要与需求定义、系统需求定义、系统架构定义和设计定义过程中发挥特别重要的作用。

> **NOTE 4** ISO/IEC/IEEE 21839 and ISO/IEC/IEEE 21840 provide more information on process application for the SoS.

> **注 4**：ISO/IEC/IEEE 21839 和 ISO/IEC/IEEE 21840 提供了关于 SoS 过程应用的更多信息。

#### 5.8 Process application 过程应用

##### 5.8.1 Overview 概述

The life cycle processes defined in this document can be used by any organization when acquiring, using, creating, modifying or supplying a system. They can be applied at any point in a system’s structure and at any stage in the life cycle.

本文件所定义的生存周期过程，能由任何组织在获取、使用、创建、修改或供应系统时使用。它们能应用于系统结构中的任何位置，以及生存周期中的任何阶段。

The functions these processes perform are defined in terms of specific purposes, outcomes, and the set of activities and tasks that constitute the process.

这些过程所执行的功能，按特定的目的、预期结果以及构成该过程的活动与任务集来界定。

Each life cycle process in Figure 4 can be invoked, as required, at any time throughout the life cycle. The application of these processes is influenced by many factors throughout the life cycle of the system, which may require the processes to be applied in an iterative, recursive, or concurrent manner.

图 4 中的每个生存周期过程，均可视需要在整个生存周期内的任何时候加以调用。这些过程的应用受到系统整个生存周期中诸多因素的影响，这可能要求以迭代、递归或并发的方式应用这些过程。

Figure 5 illustrates the interrelationships among processes defined in this document. The technical management processes are continually applied to manage and control all of the processes and life cycle stages. The system analysis process provides data and information that are essential for each iteration of the systems life cycle processes, which are performed to support any of the technical management processes (6.3) and the technical processes (6.4).

图 5 示出了本文件所定义各过程之间的相互关系。技术管理过程被持续应用，以管理和控制所有过程及生存周期阶段。系统分析过程提供的数据和信息，对于系统生存周期过程的每一次迭代都必不可少，而这些迭代的实施用以支持任何技术管理过程(6.3)和技术过程(6.4)。

> **NOTE** The arrows in Figure 5 are intended to show general relationships that include iterative, recursive, and concurrent application. All possible relationships are not included. The actual flows or interactions between the processes for a project are determined by the project tailoring and needs. Also, the arrows are not intended to indicate any specific temporal relationships, sequences, or scheduling. The arrows between process groups or aggregations of processes within process groups are intended to indicate that the project can apply the processes in any order, can iterate between processes, and can implement them concurrently.

> **注**：图 5 中的箭头用以表示一般性关系，其中包括迭代、递归和并发的应用。并非所有可能的关系都已包含在内。项目各过程之间的实际流或相互作用，由项目的裁剪和需要确定。此外，这些箭头并非用以指示任何具体的时间关系、顺序或进度安排。过程组之间、或过程组内各过程聚合之间的箭头，用以指示项目能按任意顺序应用这些过程、能在过程之间迭代，并能并发实施这些过程。

The changing nature of the influences on the system (e.g. operational environment changes, new opportunities for system element implementation, modified structure, and responsibilities in organizations) requires continual review of the selection and timing of process use. Process use in the life cycle can be dynamic, responding to the many external influences on the system or internal influences from a more continuous development approach. The life cycle approach also allows for incorporating the changes in the next stage. The life cycle stages assist the planning, execution, and management of life cycle processes in the face of this complexity in life cycles by providing comprehensible and recognizable high-level purpose and structure. The set of processes within a life cycle stage are applied with the common goal of satisfying the exit criteria for that stage or the entry criteria of the formal progress reviews within that stage. This applies regardless of the type of life cycle model or development approach.

对系统之影响的不断变化（例如运行环境变化、系统元素实现的新机遇、结构变更以及组织中职责的变更），要求持续评审过程使用的选择与时机。生存周期中的过程使用能是动态的，以响应来自系统的诸多外部影响，或来自更连续式开发途径的内部影响。生存周期途径还允许在下一阶段纳入这些变更。面对生存周期中的这种复杂性，生存周期阶段通过提供可理解且可识别的高层目的与结构，有助于生存周期过程的规划、执行和管理。生存周期阶段内的过程集，以满足该阶段的退出准则、或该阶段内正式进展评审的进入准则为共同目标加以应用。无论生存周期模型或开发途径属何种类型，这一点都适用。

Where justified by quality risks, detailed descriptions of process instances in the context of the specific product or service may also be created. Instantiation of processes involves identifying specific success criteria for a process instance, derived from the requirements, and identifying the specific activities and tasks needed to achieve the success criteria, derived from the activities and tasks identified in this document. Creating detailed descriptions of process instances enables better management of quality risks by establishing the link between the process and the specific requirements.

在质量风险证明有必要时，还可创建特定产品或服务语境下过程实例的详细描述。过程的实例化包括：确定某一过程实例的特定成功准则（由需求导出），并确定实现这些成功准则所需的特定活动与任务（由本文件所确定的活动与任务导出）。创建过程实例的详细描述，能通过建立过程与特定需求之间的联系，更好地管理质量风险。

![Figure 5 — Interrelationships between processes](ISO IEC IEEE 15288 2023.assets/fig-05.png)

**Figure 5 — Interrelationships between processes**

**图 5 — 过程之间的相互关系**

The processes in this document are often applied using an MBSE approach, which uses a set of models to implement the processes and achieve the expected outcomes. See Annex D for information regarding MBSE.

本文件中的过程常常采用 MBSE 途径来应用，该途径使用一组模型来实施这些过程并实现预期结果。关于 MBSE 的信息见附录 D。

##### 5.8.2 Process iteration, recursion, and concurrency 过程迭代、递归与并发

When the application of the same process or set of processes is repeated on the same level of the system structure, the application is referred to as iterative. The iterative use of processes is important for the progressive refinement of process outputs, for example, the interaction between successive verification actions and integration actions can incrementally build confidence in the conformance of the product or service. Iteration is not only appropriate but also expected. New information is created by the application of a process or set of processes. Typically, this information takes the form of questions with respect to requirements, analysed risks, or opportunities. Iterative application of a process or set of processes should continue until such questions are resolved.

当同一过程或过程集在系统结构的同一层级上重复应用时，该应用称为迭代式。过程的迭代使用对于过程输出的逐步细化很重要；例如，相继的验证行动与集成行动之间的交互，能逐步建立对产品或服务符合性的信心。迭代不仅适宜，而且也是所预期的。过程或过程集的应用会生成新的信息。这类信息通常表现为关于需求、已分析的风险或机遇的问题。过程或过程集的迭代应用宜持续到此类问题得到解决为止。

Iteration between business or mission analysis, stakeholder needs and requirements definition, system requirements definition, system architecture definition, and design definition processes often occurs to help achieve a common understanding of the problem to be solved and the identification of a satisfactory solution. These are heavily supported by the system analysis and decision management processes (see Figure 5). Information produced by the processes should be shared and used by all other system life cycle processes.

业务或任务分析、利益相关方需要与需求定义、系统需求定义、系统架构定义和设计定义诸过程之间的迭代常常发生，以帮助就所要解决的问题达成共识，并确定令人满意的解决方案。这些过程得到系统分析过程和决策管理过程的大力支持（见图 5）。这些过程所产生的信息宜由所有其他系统生存周期过程共享和使用。

The recursive use of processes, i.e. the repeated application of the same process or set of processes applied to successive levels of system elements in a system’s structure, is a key aspect of the application of this document. From a view of relations between a system and its system elements, the outputs of processes applied for a system or system element, whether information, artefacts, or services, are inputs to other processes or other system elements for additional analysis or more generalised synthesis of its system elements, to arrive at a more detailed or mature set of outcomes. Such an approach adds value to systems at successive levels in the system structure.

过程的递归使用，即在系统结构中的相继各层级系统元素上重复应用同一过程或过程集，是本文件应用的一个关键方面。从系统与其系统元素之间关系的角度看，对某一系统或系统元素所应用过程的输出，无论是信息、人工制品还是服务，都是其他过程或其他系统元素的输入，用于对其系统元素作进一步分析或更概括的综合，以得到更详细或更成熟的预期结果集。这种途径为系统结构中相继各层级的系统增加价值。

The discussion in this subclause on iterative and recursive use of the system life cycle processes is not meant to imply any specific hierarchical, vertical, or horizontal structure for the SoI, enabling system, organization, or project.

本条款中关于系统生存周期过程迭代使用与递归使用的讨论，无意暗示 SoI、使能系统、组织或项目的任何特定层级结构、纵向结构或横向结构。

Concurrent use of processes can exist within a project (e.g. when design actions and preparatory actions for building a system are performed at the same time), and between projects (e.g. when system elements are designed at the same time under different project responsibilities). All processes can be used in parallel with other processes. As an example, the operation and maintenance processes need to provide input to the system requirements definition, system architecture definition, design definition, and implementation processes.

过程的并发使用能存在于一个项目内部（例如当构建系统的设计行动与准备行动同时执行时），也能存在于项目之间（例如当系统元素在不同项目职责下同时设计时）。所有过程都能与其他过程并行使用。举例来说，运行过程和维护过程需要向系统需求定义、系统架构定义、设计定义和实现诸过程提供输入。

##### 5.8.3 Process views 过程视图

There are cases where a unified focus is needed for activities and tasks that are selected from disparate processes to provide visibility to a significant concept or thread that cuts across the processes employed across the life cycle. For this purpose, the concept of a process view has been formulated. Like a process, the description of a process view includes a statement of purpose and outcomes. Unlike a process, the description of a process view does not include unique activities and tasks. Instead, the description includes guidance explaining how the outcomes can be achieved by employing the activities and tasks of the various life cycle processes. The detailed information about process views is available in ISO/IEC/IEEE 24748-1 and ISO/IEC/IEEE 24774. The following International Standards provide details on some of the technical viewpoints:

有些情况下，需要对从不同过程中选出的活动与任务作统一聚焦，以使贯穿整个生存周期所用各过程的重要概念或线索可见。为此，提出了过程视图这一概念。与过程一样，过程视图的描述包括目的和预期结果的陈述。与过程不同的是，过程视图的描述不包含独有的活动与任务。相反，该描述包含指南，说明如何通过采用各生存周期过程的活动与任务来实现这些预期结果。关于过程视图的详细信息见 ISO/IEC/IEEE 24748-1 和 ISO/IEC/IEEE 24774。下列国际标准给出了一些技术视角的详细信息：

- ISO/IEC/IEEE 24748-1

- ISO/IEC/IEEE 24748-1

- specialty engineering;

- 专业工程；

- interface management;

- 接口管理；

- security.

- 安全。

- ISO/IEC/IEEE 15026-4

- ISO/IEC/IEEE 15026-4

- system assurance;

- 系统保证；

- software assurance.

- 软件保证。

#### 5.9 Concept and system definition 概念与系统定义

Concepts, needs, and requirements evolve at various levels resulting from the establishment of or changes to the organizational concept of operations, strategy, or environment. The concept of operations addresses the leadership’s intended way of operating the organization. This evolution is accomplished through the application of the business or mission analysis, stakeholder needs and requirement definition, system requirements definition, system architecture definition, and design definition processes with the support of other processes as needed. Through the iterative and concurrent use of all these processes, stakeholders are identified and insights are gained into the relationships between the concepts, needs, and requirements of the organization, stakeholders, and systems, as well as the emergent properties and behaviours of the system that arise from the interactions and relations among the system elements and environment.

由于组织运行概念、战略或环境的建立或变更，概念、需要与需求在各个层级上不断演进。运行概念涉及领导层运行组织的预期方式。这一演进通过应用业务或任务分析过程、利益相关方需要与需求定义过程、系统需求定义过程、系统架构定义过程以及设计定义过程来实现，并视需要由其他过程提供支持。通过迭代且并行地使用所有这些过程，识别出各利益相关方，并洞察组织、利益相关方与系统的概念、需要与需求之间的关系，以及由系统元素与环境之间的交互和关系所产生的系统涌现属性与行为。

The business or mission analysis process analyses changes in the organizational concept of operations, environment, and other strategic inputs to identify and define key problems or opportunities that should be addressed to achieve the organization’s mission(s), vision, goals, or objectives. The business or mission analysis process also identifies, characterizes, and prioritises alternative solution classes (or general approaches) that are candidates to address the problem or opportunity. Using the stakeholder needs and requirements definition process, stakeholders define their concepts, needs, and requirements in the context of the defined problem or opportunity, the associated capabilities required, and the preferred solution class(es). This includes defining the operational context of the solution. The operational concept addresses what the system will do and why. Using the system requirements definition process, the engineering team tasked with providing a solution transform the stakeholder requirements into system requirements. In the application of the three processes discussed in this document, a range of analysis techniques and trade-offs are applied iteratively and recursively to transform concepts into needs and needs into requirements (e.g. mission analysis, business analysis, operational analysis, requirements analysis).

业务或任务分析过程分析组织运行概念、环境及其他战略输入的变化，以识别并定义为实现组织的任务、愿景、目标或目的而宜予处理的关键问题或机会。业务或任务分析过程还识别、表征并按优先次序排列备选解类（或一般途径），这些解类是处理该问题或机会的候选方案。利用利益相关方需要与需求定义过程，利益相关方在所定义的问题或机会、所需的关联能力以及优选的解类的语境下，定义其概念、需要与需求。这包括定义解的运行语境。运行概念涉及系统将做什么以及为何做。利用系统需求定义过程，承担提供解之任务的工程团队将利益相关方需求转换为系统需求。在应用本文件所讨论的这三个过程时，迭代且递归地应用一系列分析技术与权衡，以将概念转换为需要、将需要转换为需求（例如任务分析、业务分析、运行分析、需求分析）。

> **NOTE 1** ISO/IEC/IEEE 29148 provides further details on the development of concepts, needs, and requirements. It includes lower-level elaboration for the processes discussed in this document, as well as annotated outlines for documenting operational concepts, stakeholder needs and requirements, and system requirements.

> **注 1**：ISO/IEC/IEEE 29148 对概念、需要与需求的开发给出了进一步细节。它包含本文件所讨论过程的更低层级细化，以及用于记录运行概念、利益相关方需要与需求以及系统需求的带注释大纲。

The system architecture definition process focuses on defining an architecture that addresses the stakeholder concerns and is applied iteratively and concurrently with the business or mission analysis, stakeholder needs and requirements definition, and system requirements definition processes to determine the best solution to address stakeholder concerns. The design definition process, on the other hand, is driven by requirements that have been vetted through evaluation with the architecture and more detailed analyses of feasibility. Architecture focuses on suitability, viability, and desirability, whereas design focuses on compatibility with technologies and other design elements and on feasibility of construction and integration. An effective architecture is as design-agnostic as possible to allow for maximum flexibility in the design trade space.

系统架构定义过程聚焦于定义一种能够应对利益相关方关注点的架构，并与业务或任务分析过程、利益相关方需要与需求定义过程以及系统需求定义过程迭代且并行地应用，以确定应对利益相关方关注点的最佳解。另一方面，设计定义过程由以下需求驱动：这些需求已通过结合架构的评估以及更详细的可行性分析得到审查。架构聚焦于适宜性、可行性与合意性，而设计聚焦于与技术及其他设计元素的兼容性，以及构建与集成的可行性。有效的架构尽可能与设计无关，以便在设计权衡空间中获得最大灵活性。

The design definition process provides feedback to the system architecture definition process to consolidate or confirm the allocation, partitioning and alignment of architectural entities (e.g. strategic goals, capabilities and effects, operational activities, resource functions) to system elements that comprise the system. Note that an architecture entity (an entity being architected or one subject to the system architecture definition process) and a system element (a discrete part of a system that fulfils specified requirements) represent two different notions.

设计定义过程向系统架构定义过程提供反馈，以整合或确认将架构实体（例如战略目标、能力与效果、运行活动、资源功能）分配、划分并对齐到构成系统的系统元素。注意，架构实体（被架构的实体，或经受系统架构定义过程的实体）与系统元素（系统中满足规定需求的离散部分）代表两种不同的概念。

> **NOTE 2** Practices, conventions, principles, and concepts for system architecture definition are specified by the ISO/IEC/IEEE 420x0 family of standards. ISO/IEC/IEEE 42020 provides architecture processes for the governance, management, conceptualization, evaluation, and elaboration of architectures; ISO/IEC/IEEE 42030 provides an architecture evaluation framework for performing architectural analysis, value assessment, and evaluation synthesis; and ISO/IEC/IEEE 42010 provides key principles and concepts for describing an architecture.

> **注 2**：系统架构定义的实践、惯例、原则与概念由 ISO/IEC/IEEE 420x0 系列标准规定。ISO/IEC/IEEE 42020 提供用于架构的治理、管理、概念化、评估与细化的架构过程；ISO/IEC/IEEE 42030 提供架构评估框架，用于执行架构分析、价值评定与评估综合；而 ISO/IEC/IEEE 42010 提供用于描述架构的关键原则与概念。

The enterprise architecture(s) or relevant reference architectures, when available, can provide useful insights for the system architecture through the life cycle of the SoI. Additionally, when the organization or enterprise is treated as the SoI, the enterprise architecture becomes a relevant part of the system definition, since it is then the top-level system architecture.

企业架构或相关参考架构（若有）能在 SoI 的整个生存周期内为系统架构提供有用的洞察。此外，当组织或企业被视为 SoI 时，企业架构即成为系统定义的相关部分，因为此时它便是顶层系统架构。

The processes discussed in this clause interact with other technical and technical management processes to provide necessary inputs and information. For example, the system analysis process provides analysis results to support trade-offs that are managed by the decision management process. Additionally, the establishment of the concepts, requirements, architecture, and design are informed by the other technical processes, such as the operations and maintenance processes.

本条所讨论的过程与其他技术过程和技术管理过程交互，以提供必要的输入与信息。例如，系统分析过程提供分析结果，以支持由决策管理过程管理的权衡。此外，概念、需求、架构与设计的确立还得到其他技术过程（如运行过程与维护过程）的输入。

#### 5.10 Assurance and quality characteristics 保证与质量特性

Assurance is defined as grounds for justified confidence that a claim has been or will be achieved. This confidence is achieved by applying applicable system life cycle activities, which include a planned, systematic approach with acceptable measures of system assurance and risk management of exploitable vulnerabilities. Stakeholders need assurance prior to depending on a system, especially a system involving complexity, novelty, or technology with a history of problems. The greater the degree of dependence, the greater the need for strong assurance. System assurance claims frequently concern the functions or capabilities of the system.

保证的定义是：对某项主张已经达成或将要达成抱持正当信任的依据。这种信任通过应用适用的系统生存周期活动而获得，这些活动包括有计划、系统化的途径，并配以可接受的系统保证度量以及对可利用脆弱性的风险管理。利益相关方在依赖某一系统之前需要保证，尤其是涉及复杂性、新颖性或具有问题历史的技术之系统。依赖程度越高，对强保证的需要就越大。系统保证主张常常涉及系统的功能或能力。

Assurance, as for a variety of attributes such as safety, security, and dependability, is often required. Stakeholder concerns include achieving justified confidence that the system, while achieving its intent, does not also provide unintended behaviour or produce unintended outcomes. A claims-oriented approach to assurance serves to address the concerns that are not typically captured within the requirements that focus on intended behaviour. An assurance case can identify gaps in requirements coverage and inform the development of derived requirements to address those gaps.

对于安全性、安全与可信性等多种属性，往往都需要保证。利益相关方关注点包括：有正当理由地信任系统在达成其意图的同时，不会产生非预期的行为或产生非预期的结果。以主张为导向的保证途径用于处理那些通常未被聚焦预期行为的需求所涵盖的关注点。保证案例能识别需求覆盖方面的缺口，并为制定解决这些缺口的派生需求提供依据。

Assurance is often provided through activities to construct an assurance case. An assurance case is an auditable artefact that provides a convincing and valid argument for a claim on the basis of tangible evidence under a given context. Subtle and complex arguments are necessary to organize a wide variety and huge amount of evidence and link them to the claim. Pieces of evidence can be pass/fail results of test, quantitative measurements, or qualitative evaluations. These pieces require careful review on their validity, certainty, fairness, etc., when they are integrated into a cohesive argument. Often there is not a simple direct connection between the evidence provided and the overall claim, so there has to be a structure to describe the subclaims and the reasoning that links this overall claim and the evidence.

保证往往通过构建保证案例的活动来提供。保证案例是一种可审计的人工制品，它在给定语境下基于确凿证据为某项主张提供令人信服且有效的论证。需要精细而复杂的论证来组织种类繁多、数量巨大的证据，并将其与主张关联起来。证据可以是试验的合格／不合格结果、定量测量值或定性评估。当这些证据被整合为一个有机统一的论证时，需要对其有效性、确定性、公正性等进行仔细审查。所提供的证据与总体主张之间往往不存在简单的直接联系，因此必须有某种结构来描述子主张以及将这一总体主张与证据联系起来的推理。

Assurance cases focusing on specific characteristics include safety case, composed assurance package (for security), and dependability case.

聚焦特定特性的保证案例包括安全性案例、组合保证包（用于安全）和可信性案例。

Assurance activities should be integrated into life cycle processes throughout the system life cycle. Construction of assurance cases require detailed knowledge about both the SoI and the characteristics under consideration. Integration of the specific analyses in the SoI development and involving experts in the SoI development are key success factors to achieve a compliant and balanced system solution.

保证活动宜在整个系统生存周期中融入各生存周期过程。构建保证案例需要同时掌握关于 SoI 和所考虑特性的详细知识。将特定分析融入 SoI 的开发，并让专家参与 SoI 的开发，是获得合规且平衡的系统解决方案的关键成功因素。

> **NOTE** The ISO/IEC/IEEE 15026 series provides more information on systems and software assurance and assurance cases.

> **注**：ISO/IEC/IEEE 15026 系列就系统与软件保证以及保证案例提供了更多信息。

Considerations for requirements on specific characteristics are provided by other documents including the IEC 61508 series (safety); ISO/IEC 27000 and ISO/IEC 15408-3 (information security); IEC 60300-1 and IEC 62741 (dependability); and ISO/IEC 25000 (systems and software quality requirements and evaluation).

对特定特性的需求，其考虑事项由其他文件提供，包括 IEC 61508 系列（安全性）；ISO/IEC 27000 和 ISO/IEC 15408-3（安全）；IEC 60300-1 和 IEC 62741（可信性）；以及 ISO/IEC 25000（系统与软件质量要求和评价）。

#### 5.11 Process reference model 过程参考模型

Annex C defines a process reference model for processes contained in Clause 6. The process reference model is applicable to an organization that is assessing its processes to determine the capability of these processes. The purpose and outcomes are a statement of the goals of the performance of each process. This statement of goals permits assessment of the effectiveness of the processes in ways other than simple conformity assessment.

附录 C 为第 6 章所含的各过程定义了过程参考模型。该过程参考模型适用于正在评定其过程以确定这些过程能力的组织。目的和预期结果是对每个过程执行目标的陈述。这种目标陈述使得能以简单符合性评定以外的方式评定各过程的有效性。

### 6 System life cycle processes 系统生存周期过程

#### 6.1 Agreement processes 协议过程

##### 6.1.1 Acquisition process 获取过程

###### 6.1.1.1 Purpose 目的

The purpose of the acquisition process is to obtain a product or service in accordance with the acquirer's requirements.

获取过程的目的是按照获取方的需求获得产品或服务。

> **NOTE** As part of this process, the agreement is modified when a change request is agreed to by both the acquirer and supplier.

> **注**：作为本过程的一部分，当变更请求经获取方和供应方双方同意时，对协议进行修改。

###### 6.1.1.2 Outcomes 预期结果

As a result of the successful performance of the acquisition process:

作为成功实施获取过程的结果：

a) a request for supply is prepared;

a) 编制供应请求；

b) one or more suppliers are selected;

b) 选出一个或多个供应方；

c) an agreement is established between the acquirer and supplier;

c) 在获取方与供应方之间建立协议；

d) a product or service complying with the agreement is accepted;

d) 接收符合协议的产品或服务；

e) acquirer obligations defined in the agreement are satisfied;

e) 协议中规定的获取方义务得到履行；

f) responsibility for the acquired product or service is transferred, as directed by the agreement.

f) 按照协议的指示，转移对所获取产品或服务的责任。

###### 6.1.1.3 Activities and tasks 活动与任务

The acquirer shall implement the following activities and tasks in accordance with applicable organization policies and procedures with respect to the acquisition process.

获取方应按照适用的组织方针和规程，针对获取过程实施下列活动与任务。

> **NOTE 1** The activities and resulting agreement from this process often apply to suppliers in the supply chain, including subcontracted suppliers.

> **注 1**：本过程的活动及由此产生的协议往往适用于供应链中的供应方，包括分包供应方。

a) Prepare for the acquisition. This activity consists of the following tasks.

a) 为获取做准备。本活动由以下任务组成。

1) Define a strategy for how the acquisition will be conducted.

1) 确定获取将如何开展的策略。

> **NOTE 2** This strategy describes or references the life cycle model, risks and issues mitigation, a schedule of milestones and decision gates, and selection criteria if the supplier is external to the acquiring organization. It also includes key drivers and characteristics of the acquisition, such as responsibilities and liabilities; specific models, methods, or processes; level of criticality; formality; and priority of relevant trade-off factors.

> **注 2**：本策略描述或引用生存周期模型、风险与问题的缓解措施、里程碑与决策门的时间安排，以及在供应方处于获取组织之外时的选择准则。它还包括获取的关键驱动因素和特性，如职责与责任；特定的模型、方法或过程；关键性程度；正式程度；以及相关权衡因素的优先级。

2) Prepare a request for the supply of a product or service that includes the requirements.

2) 编制包含各项需求的、产品或服务的供应请求。

> **NOTE 3** If a supplier is external to the organization, then the request typically includes the practices with which a supplier is expected to comply and the criteria for selecting a supplier.

> **注 3**：若供应方处于本组织之外，则供应请求通常包括期望供应方遵守的实践以及选择供应方的准则。

> **NOTE 4** A definition of requirements is provided to one or more suppliers. The requirements are the stakeholder or the system requirements, depending on the type of acquisition approach, through the associated requirements definition process.

> **注 4**：向一个或多个供应方提供需求定义。视获取途径的类型而定，这些需求是利益相关方需求或系统需求，经由相应的需求定义过程得出。

b) Advertise the acquisition and select the supplier. This activity consists of the following tasks.

b) 发布获取通告并选择供应方。本活动由以下任务组成。

1) Communicate the request for the supply of a product or service to potential suppliers.

1) 将产品或服务的供应请求传达给潜在供应方。

2) Select one or more suppliers.

2) 选择一个或多个供应方。

> **NOTE 5** To obtain competitive solicitations, proposals to supply are evaluated and compared against the selection criteria and ranked. The justification for rating each proposal is declared and suppliers are informed why they were or were not selected.

> **注 5**：为获得竞争性征集，按选择准则对供应建议书进行评价、比较并排序。宣布每份建议书评级的理由，并告知供应方其被选中或未被选中的原因。

c) Establish and maintain an agreement. This activity consists of the following tasks.

c) 建立并保持协议。本活动由以下任务组成。

> **NOTE 6** Project cost, schedule, and performance are monitored through the project assessment and control process. Any identified issues that require agreement modifications are referred to this activity. Any proposals for changes to system elements or information are controlled through the change management activity of the configuration management process.

> **注 6**：项目成本、进度和绩效通过项目评定与控制过程进行监视。任何需要修改协议的已识别问题均提交至本活动。对系统元素或信息提出变更的任何建议，均通过配置管理过程的变更管理活动加以控制。

> **NOTE 7** For an SoS, if a multi-lateral agreement exists, responsibilities and modes of support and control are established across the life cycle stages among the stakeholder organizations participating in the SoS. Agreements are flexible to adapt to changing requirements of an SoS for which the SoI is a constituent system.

> **注 7**：对于 SoS，若存在多边协议，则在参与该 SoS 的各利益相关方组织之间，跨各生存周期阶段确立职责以及支持与控制的方式。协议具有灵活性，以适应 SoI 作为其构成系统的 SoS 不断变化的需求。

1) Develop and approve an agreement with the supplier that includes acceptance criteria.

1) 制定并批准与供应方之间的协议，其中包含验收准则。

> **NOTE 8** This agreement ranges in formality from a written contract to a verbal agreement. Appropriate to the level of formality, the agreement establishes requirements, development and delivery milestones, verification, validation and acceptance conditions, process requirements (e.g. configuration management, risk management, measurement), exception-handling procedures, agreement change management procedures, payment schedules, accountability of each party in case of non-fulfilment, and handling of data rights and intellectual property so that both parties of the agreement understand the basis for executing the agreement. For a written contract, this occurs when the contract is signed.

> **注 8**：本协议在正式程度上从书面合同到口头协议不等。协议按与其正式程度相称的方式，规定需求、开发与交付里程碑、验证、确认和验收条件、过程要求（例如配置管理、风险管理、测量）、异常处理规程、协议变更管理规程、付款计划、各方在不履行情况下的责任，以及数据权利和知识产权的处理，以使协议双方理解执行协议的依据。对于书面合同，这在合同签署时发生。

> **NOTE 9** The agreement identifies any requirements to be imposed on participating subcontractors.

> **注 9**：协议标识出拟施加于参与分包的各分包方的任何要求。

2) Identify necessary changes to the agreement.

2) 识别对协议的必要变更。

> **NOTE 10** In requesting a change to the agreement, the acquirer or the supplier details its specifications, rationale, and background.

> **注 10**：在请求变更协议时，获取方或供应方详述其规格、理由和背景。

3) Evaluate impact of changes on the agreement.

3) 评估变更对协议的影响。

> **NOTE 11** Any change is investigated for impacts to project plans, schedule, cost, technical capability, and quality. A change can be handled within the existing agreement, can require a modification to the agreement, or can require a new agreement.

> **注 11**：对任何变更均调查其对项目计划、进度、成本、技术能力和质量的影响。变更能在现有协议内处理，能要求对协议进行修改，或能要求订立新的协议。

4) Update the agreement with the supplier, as necessary.

4) 必要时更新与供应方之间的协议。

> **NOTE 12** The result of the agreement modification is incorporated into the project plans and communicated to all affected parties.

> **注 12**：协议修改的结果纳入项目计划，并传达至所有受影响的各方。

d) Monitor the agreement. This activity consists of the following tasks.

d) 监视协议。本活动由以下任务组成。

1) Assess the execution of the agreement.

1) 评定协议的执行情况。

> **NOTE 13** This includes confirmation that all parties are meeting their responsibilities in accordance with the agreement. The project assessment and control process is used to evaluate projected cost, schedule, performance, and the impact of undesirable outcomes on the organization. This information is combined with other assessments of the execution of the terms of the agreement.

> **注 13**：这包括确认各方均按照协议履行其职责。使用项目评定与控制过程来评估预计成本、进度、绩效，以及不期望结果对组织的影响。该信息与对协议条款执行情况的其他评定相结合。

2) Provide data needed by the supplier and resolve issues in a timely manner.

2) 提供供应方所需的数据，并及时解决问题。

e) Accept the product or service. This activity consists of the following tasks.

e) 接收产品或服务。本活动由以下任务组成。

1) Confirm that the delivered product or service complies with the agreement.

1) 确认所交付的产品或服务符合协议。

> **NOTE 14** Exceptions that arise during the conduct of the agreement or with the delivered product or service are resolved in accordance with the procedures established in the agreement.

> **注 14**：在协议履行期间出现的例外情况，或在所交付产品或服务方面出现的例外情况，按协议中确立的程序予以解决。

> **NOTE 15** Acceptance can be performed using the validation process.

> **注 15**：验收能运用确认过程来执行。

2) Provide payment or other agreed consideration.

2) 支付款项或提供其他约定的对价。

3) Accept the product or service from the supplier, or other party, as directed by the agreement.

3) 按协议的指示，从供应方或其他方接收产品或服务。

4) Close the agreement.

4) 结束协议。

> **NOTE 16** The project is closed by the portfolio management process.

> **注 16**：项目由项目组合管理过程结束。

##### 6.1.2 Supply process 供应过程

###### 6.1.2.1 Purpose 目的

The purpose of the supply process is to provide an acquirer with a product or service that meets agreed requirements.

供应过程的目的是向获取方提供满足约定要求的产品或服务。

> **NOTE** As part of this process, the agreement is modified when a change request is agreed to by both the acquirer and supplier.

> **注**：作为本过程的一部分，当获取方与供应方双方就变更请求达成一致时，即对协议进行修改。

###### 6.1.2.2 Outcomes 预期结果

As a result of the successful performance of the supply process:

作为成功执行供应过程的结果：

a) an acquirer for a product or service is identified;

a) 识别出产品或服务的获取方；

b) a response to the acquirer's request is produced;

b) 生成对获取方请求的响应；

c) an agreement is established between the acquirer and supplier;

c) 在获取方与供应方之间建立协议；

d) a product or service is provided;

d) 提供产品或服务；

e) supplier obligations defined in the agreement are satisfied;

e) 协议中规定的供应方义务得到满足；

f) responsibility for the acquired product or service is transferred, as directed by the agreement.

f) 按协议的指示，转移对所获取产品或服务的责任。

###### 6.1.2.3 Activities and tasks 活动与任务

The supplier shall implement the following activities and tasks in accordance with applicable organization policies and procedures with respect to the Supply process.

供应方应针对供应过程，按照适用的组织方针和程序实施以下活动与任务。

a) Prepare for the supply. This activity consists of the following tasks.

a) 为供应做准备。本活动由以下任务组成。

1) Determine the existence and identity of an acquirer who has a need for a product or service.

1) 确定存在对产品或服务有需要的获取方，并确定其身份。

> **NOTE 1** Potential acquirers are often identified through the business or mission analysis process. For a product or service developed for consumers, an agent, for example, a marketing function within the supplier organization, often represents the acquirer.

> **注 1**：潜在的获取方往往通过业务或任务分析过程予以识别。对于为消费者开发的产品或服务，通常由代理人（例如供应方组织内的营销职能部门）代表获取方。

2) Define a supply strategy.

2) 定义供应策略。

> **NOTE 2** This strategy describes or references the life cycle model, risks and issues mitigation, and a schedule of milestones. It also includes key drivers and characteristics of the acquisition such as responsibilities and liabilities; specific models; methods or processes; level of criticality; formality; and priority of relevant trade-off factors.

> **注 2**：该策略描述或引用生存周期模型、风险与问题缓解措施以及里程碑进度安排。它还包括获取的关键驱动因素和特征，如职责与责任；特定模型；方法或过程；关键性程度；正式程度；以及相关权衡因素的优先次序。

b) Respond to a request for supply of products or services. This activity consists of the following tasks.

b) 响应产品或服务的供应请求。本活动由以下任务组成。

1) Evaluate a request for the supply of a product or service to determine feasibility and how to respond.

1) 评估产品或服务的供应请求，以确定可行性及响应方式。

2) Prepare a response that satisfies the solicitation.

2) 编制满足招标要求的响应。

c) Establish and maintain an agreement. This activity consists of the following tasks.

c) 建立并保持协议。本活动由以下任务组成。

1) Negotiate and approve an agreement with the acquirer that includes acceptance criteria.

1) 与获取方协商并批准包含验收准则的协议。

> **NOTE 3** This agreement ranges in formality from a written contract to a verbal agreement. Appropriate to the level of formality, the agreement establishes requirements, development and delivery milestones, verification, validation and acceptance conditions, process requirements (e.g. configuration management, risk management, measurement), exception-handling procedures, agreement change management procedures, payment schedules, accountability of each party in case of non-fulfilment, and handling of data rights and intellectual property so that both parties of the agreement understand the basis for executing the agreement. For a written contract, this occurs when the contract is signed.

> **注 3**：本协议的正式程度从书面合同到口头约定不等。按照正式程度，协议确立要求、开发与交付里程碑、验证、确认与验收条件、过程要求（例如配置管理、风险管理、测量）、例外处理程序、协议变更管理程序、付款进度安排、各方在未履行情况下的责任归属，以及数据权利和知识产权的处理，从而使协议双方理解执行协议的依据。对于书面合同，这在合同签署时即已完成。

> **NOTE 4** For an SoS, if a multi-lateral agreement exists, responsibilities and modes of support and control are established across the life cycle stages among the stakeholder organizations participating in the SoS. Agreements are flexible to adapt to changing requirements of an SoS for which the SoI is a constituent system.

> **注 4**：对于 SoS，如果存在多边协议，则在参与该 SoS 的各利益相关方组织之间，跨生存周期各阶段确立职责以及支持与控制模式。协议具有灵活性，以适应 SoI 作为其构成系统的 SoS 不断变化的要求。

2) Identify necessary changes to the agreement.

2) 识别对协议的必要变更。

> **NOTE 5** In requesting a change to the agreement, the acquirer or the supplier details its specifications, rationale, and background.

> **注 5**：在请求变更协议时，获取方或供应方详述其规格、理由和背景。

3) Evaluate impact of changes on the agreement.

3) 评估变更对协议的影响。

> **NOTE 6** Any change is investigated for impacts to project plans, schedule, cost, technical capability, or quality. A change can be handled within the existing agreement, can require a modification to the agreement, or can require a new agreement.

> **注 6**：对任何变更都要调查其对项目计划、进度、成本、技术能力或质量的影响。变更能在现有协议范围内处理，能要求对协议进行修改，也能要求订立新协议。

4) Update the agreement with the acquirer, as necessary.

4) 视需要更新与获取方的协议。

> **NOTE 7** The result of the agreement modification is incorporated into the project plans and communicated to all affected parties.

> **注 7**：协议修改的结果纳入项目计划，并传达给所有受影响的各方。

d) Execute the agreement. This activity consists of the following tasks.

d) 执行协议。本活动由以下任务组成。

1) Execute the agreement in accordance with the established project plans.

1) 按照已确立的项目计划执行协议。

> **NOTE 8** A supplier sometimes adopts or agrees to use acquirer processes.

> **注 8**：供应方有时采纳或同意使用获取方的过程。

2) Assess the execution of the agreement.

2) 评定协议的执行情况。

> **NOTE 9** This includes confirmation that all parties are meeting their responsibilities in accordance with the agreement. The project assessment and control process is used to evaluate projected cost, schedule, performance, and the impact of undesirable outcomes on the organization. The change management activity of the configuration management process is used to control changes to the system elements. This information is combined with other assessments of the execution of the terms of the agreement.

> **注 9**：这包括确认各方均按协议履行其职责。运用项目评定与控制过程来评估预计成本、进度、绩效以及不良结果对组织的影响。运用配置管理过程的变更管理活动来控制对系统元素的变更。这一信息与对协议条款执行情况的其他评定相结合。

e) Deliver and support the product or service. This activity consists of the following tasks.

e) 交付并支持产品或服务。本活动由以下任务组成。

1) Deliver the product or service in accordance with the agreement criteria.

1) 按照协议准则交付产品或服务。

2) Provide assistance to the acquirer in support of the delivered product or service, per the agreement.

2) 按协议向获取方提供协助，以支持所交付的产品或服务。

3) Accept and acknowledge payment or other agreed consideration.

3) 接收并确认款项或其他约定的对价。

4) Transfer the product or service to the acquirer, or other party, as directed by the agreement.

4) 按协议的指示，将产品或服务转移给获取方或其他方。

5) Close the agreement.

5) 结束协议。

> **NOTE 10** The project is closed by the portfolio management process.

> **注 10**：项目由项目组合管理过程结束。

#### 6.2 Organizational project-enabling processes 组织项目使能过程

##### 6.2.1 Life cycle model management process 生存周期模型管理过程

###### 6.2.1.1 Purpose 目的

The purpose of the life cycle model management process is to define, maintain, and help ensure availability of policies, life cycle processes, life cycle models, and procedures for use by the organization with respect to the scope of this document.

生存周期模型管理过程的目的是，针对本文件的范围，定义、维护并帮助确保供组织使用的方针、生存周期过程、生存周期模型和程序可供使用。

This process provides policies, life cycle processes, life cycle models, and procedures that are consistent with the organization's objectives. These life cycle assets are defined, adapted, improved, and maintained to support individual project needs in a way that they are capable of being applied using effective, proven methods and tools.

本过程提供与组织目标相一致的方针、生存周期过程、生存周期模型和程序。这些生存周期资产经过定义、适配、改进和维护，以支持各个项目的需要，使其能够运用有效的、经证实的方法和工具加以应用。

> **NOTE** Regulated domains sometimes require specific life cycle management process standards, e.g. ANSI/ AAMI/IEC 62304.

> **注**：受监管的业务域有时要求特定的生存周期管理过程标准，例如 ANSI/AAMI/IEC 62304。

###### 6.2.1.2 Outcomes 预期结果

As a result of the successful performance of the life cycle model management process:

作为成功执行生存周期模型管理过程的结果：

a) organizational policies and procedures for the management and deployment of life cycle models and processes are established;

a) 用于管理和部署生存周期模型和过程的组织方针和程序得以建立；

b) roles, responsibility, accountability, and authority within life cycle policies, processes, models, and procedures are defined;

b) 生存周期方针、过程、模型和程序中的角色、职责、责任归属和权限得以界定；

c) policies, life cycle processes, life cycle models, and procedures for use by the organization are selected;

c) 选出供组织使用的方针、生存周期过程、生存周期模型和程序；

d) policies, life cycle processes, life cycle models, and procedures for use by the organization are assessed;

d) 供组织使用的方针、生存周期过程、生存周期模型和程序得到评定；

e) prioritised process, model, and procedure improvements are implemented.

e) 已排定优先次序的过程、模型和规程改进得到实施。

###### 6.2.1.3 Activities and tasks 活动与任务

The organization shall implement the following activities and tasks in accordance with applicable organization policies and procedures with respect to the life cycle model management process.

组织应按照适用的组织方针和规程，针对生存周期模型管理过程实施下列活动与任务。

a) Establish the life cycle processes. This activity consists of the following tasks.

a) 建立生存周期过程。本活动由下列任务组成。

> **NOTE 1** The detail of the life cycle implementation within a project is dependent upon the complexity of the work, the methods used, and the skills and training of personnel involved in performing the work. A project tailors policies, processes, models, and procedures in accordance with its requirements and needs, while maintaining alignment with regulations and organizational policies.

> **注 1**：项目内生存周期实施的详细程度取决于工作的复杂性、所采用的方法以及参与执行该工作的人员的技能和培训。项目按照自身的要求和需要裁剪方针、过程、模型和规程，同时保持与法规和组织方针的一致。

1) Establish policies and life cycle procedures for process management and deployment that are consistent with organizational strategies.

1) 建立与组织战略一致的过程管理和部署的方针及生存周期规程。

2) Establish the life cycle processes that implement the requirements of this document and that are consistent with organizational strategies.

2) 建立实现本文件要求且与组织战略一致的生存周期过程。

3) Define the roles, responsibilities, accountabilities, and authorities to facilitate implementation of life cycle processes and the strategic management of life cycles.

3) 规定角色、职责、问责和职权，以促进生存周期过程的实施以及生存周期的战略管理。

4) Define criteria that control progression through the life cycle.

4) 规定控制生存周期推进的准则。

> **NOTE 2** The decision-making criteria regarding entering and exiting each life cycle stage and key milestones and decision gates are established.

> **注 2**：就进入和退出每个生存周期阶段以及关键里程碑和决策门建立决策准则。

5) Establish standard life cycle models for the organization that are comprised of stages and define the purpose and outcomes for each stage.

5) 为组织建立由阶段构成的标准化生存周期模型，并规定每个阶段的目的和预期结果。

> **NOTE 3** The life cycle model comprises one or more stages, as needed. It is assembled as a sequence of stages that overlap or iterate, as appropriate for the SoI's scope, magnitude, complexity, changing needs and opportunities. Stages are illustrated in ISO/IEC/IEEE 24748-1 using a commonly encountered example of life cycle stages. The life cycle processes and activities are selected, tailored as appropriate and employed in a stage to fulfil the purpose and outcomes of that stage.

> **注 3**：生存周期模型按需由一个或多个阶段构成。它组装为阶段序列，这些阶段视 SoI 的范围、规模、复杂性以及不断变化的需要和机遇而重叠或迭代。ISO/IEC/IEEE 24748-1 使用一个常见的生存周期阶段示例来说明阶段。生存周期过程和活动经选择、适当裁剪后运用于某一阶段，以实现该阶段的目的和预期结果。

b) Assess the life cycle processes. This activity consists of the following tasks.

b) 评定生存周期过程。本活动由下列任务组成。

> **NOTE 4** The ISO/IEC 33000 family of standards provides a more detailed set of process assessment activities and tasks that are aligned with the tasks shown below.

> **注 4**：ISO/IEC 33000 族标准给出了一组更详细的过程评定活动与任务，与下列任务保持一致。

1) Monitor process execution across the organization.

1) 监视整个组织内的过程执行情况。

> **NOTE 5** This includes the analysis of process measures and review of trends with respect to strategic criteria, feedback from the projects regarding the effectiveness and efficiency of the processes, and monitoring execution in accordance with regulations and organizational policies.

> **注 5**：这包括分析过程测量值并对照战略准则审查趋势，审查各项目就过程有效性和效率给出的反馈，以及监视是否按照法规和组织方针执行。

2) Conduct periodic reviews of the life cycle models used by the projects.

2) 对各项目所使用的生存周期模型进行定期审查。

> **NOTE 6** This includes confirming the continuing suitability, adequacy, and effectiveness of the life cycle models used by the projects and making improvements as appropriate. This includes the stages, processes, and achievement criteria that control progression through the life cycle.

> **注 6**：这包括确认各项目所使用的生存周期模型持续适宜、充分和有效，并在适当时作出改进。这涉及控制生存周期推进的各阶段、过程和成就准则。

3) Identify improvement opportunities from assessment results.

3) 从评定结果中识别改进机会。

c) Improve the process. This activity consists of the following tasks.

c) 改进过程。本活动由下列任务组成。

1) Prioritise and plan improvement opportunities.

1) 对改进机会排定优先次序并作出规划。

2) Implement improvement opportunities and inform relevant stakeholders.

2) 实施改进机会并告知相关利益相关方。

> **NOTE 7** Process improvement includes improvements to any of the processes in the organization. Lessons learned are captured and available.

> **注 7**：过程改进包括对组织中任何过程的改进。经验教训得到捕获并可供使用。

##### 6.2.2 Infrastructure management process 基础设施管理过程

###### 6.2.2.1 Purpose 目的

The purpose of the infrastructure management process is to provide the infrastructure and services to projects to support organization and project objectives throughout the life cycle.

基础设施管理过程的目的是为项目提供基础设施和服务，以在生存周期内支持组织和项目的目标。

This process defines, provides and maintains the facilities, tools, and communications and information technology assets needed for the organization with respect to the scope of this document.

本过程就本文件的范围规定、提供并维护组织所需的设施、工具以及通信和信息技术资产。

###### 6.2.2.2 Outcomes 预期结果

As a result of the successful performance of the infrastructure management process:

作为基础设施管理过程成功执行的结果：

a) the needs for infrastructure are defined;

a) 基础设施的需要得到规定；

b) the infrastructure elements are specified;

b) 基础设施元素得到规定；

c) infrastructure elements are obtained;

c) 基础设施元素得到获取；

d) the infrastructure is available;

d) 基础设施可供使用；

e) prioritised infrastructure improvements are implemented.

e) 已排定优先次序的基础设施改进得到实施。

###### 6.2.2.3 Activities and tasks 活动与任务

The organization shall implement the following activities and tasks in accordance with applicable organization policies and procedures with respect to the infrastructure management process.

组织应按照适用的组织方针和规程，针对基础设施管理过程实施下列活动与任务。

a) Establish the infrastructure. This activity consists of the following tasks.

a) 建立基础设施。本活动由下列任务组成。

1) Define project infrastructure needs.

1) 规定项目的基础设施需要。

> **NOTE 1** Infrastructure element examples are facilities, tools, hardware, software, services, and standards.

> **注 1**：基础设施元素的示例有设施、工具、硬件、软件、服务和标准。

> **NOTE 2** The infrastructure resource needs for the project are considered in context with other projects and resources within the organization, as well as within the policies and strategic plans of the organization. Constraints and timelines that influence and control provision of infrastructure resources and services for the project are also evaluated. Project plans and future strategy needs contribute to the understanding of the resource infrastructure that is required. Physical factors (e.g. facilities), logistics needs, and human factors (including health and safety aspects) are also considered.

> **注 2**：项目的基础设施资源需要，结合组织内的其他项目和资源以及组织的方针和战略计划加以考虑。还会评定影响和控制项目基础设施资源与服务提供的约束和时间线。项目计划和未来战略需要有助于理解所需的资源基础设施。还要考虑物理因素（例如设施）、后勤需要以及人的因素（包括健康和安全方面）。

> **NOTE 3** The ISO/IEC 27036 series provides guidance for addressing security of outsourced infrastructure.

> **注 3**：ISO/IEC 27036 系列为处理外包基础设施的安全提供指南。

2) Identify, obtain, and provide infrastructure resources and services that are needed to implement and support projects.

2) 识别、获取并提供实施和支持项目所需的基础设施资源和服务。

> **NOTE 4** An inventory asset registry is often established to track infrastructure elements and support reuse.

> **注 4**：通常建立库存资产登记册，以跟踪基础设施元素并支持复用。

b) Maintain the infrastructure. This activity consists of the following tasks.

b) 维护基础设施。本活动由下列任务组成。

1) Evaluate the degree to which delivered infrastructure resources satisfy project needs.

1) 评估所交付的基础设施资源满足项目需要的程度。

2) Identify and provide improvements or changes to the infrastructure resources as needed.

2) 按需要识别并提供对基础设施资源的改进或更改。

##### 6.2.3 Portfolio management process 项目组合管理过程

###### 6.2.3.1 Purpose 目的

The purpose of the portfolio management process is to initiate and sustain necessary, sufficient, and suitable projects to meet the strategic objectives of the organization.

项目组合管理过程的目的是发起并维持必要、充分且适宜的项目，以实现组织的战略目标。

This process commits the investment of adequate organization funding and resources, and sanctions the authorities needed to establish selected projects. It performs continued assessment of projects to confirm they justify, or can be redirected to justify, continued investment.

本过程承诺投入充分的组织资金和资源，并批准设立所选项目所需的职权。它对项目持续进行评定，以确认这些项目值得继续投资，或能通过调整方向而值得继续投资。

###### 6.2.3.2 Outcomes 预期结果

As a result of the successful performance of the portfolio management process:

作为项目组合管理过程成功执行的结果：

a) strategic venture opportunities, investments, or necessities are prioritised;

a) 战略性事业机会、投资或必需事项已排定优先次序；

b) projects are identified;

b) 项目得到识别；

c) resources and budgets for each project are allocated;

c) 每个项目的资源和预算得到分配；

d) project management responsibilities, accountability, and authorities are defined;

d) 项目管理的职责、问责和职权得到规定；

e) projects meeting agreements and stakeholder requirements are sustained;

e) 满足协议和利益相关方要求的项目得到维持；

f) projects not meeting agreements or satisfying stakeholder requirements are redirected or terminated;

f) 未满足协议或未满足利益相关方要求的项目得到调整方向或终止；

g) projects that have completed agreements and satisfied stakeholder requirements are closed.

g) 已完成协议并满足利益相关方要求的项目得到关闭。

###### 6.2.3.3 Activities and tasks 活动与任务

The organization shall implement the following activities and tasks in accordance with applicable organization policies and procedures with respect to the portfolio management process.

组织应按照适用的组织方针和规程，针对项目组合管理过程实施下列活动与任务。

a)Define and authorise projects. This activity consists of the following tasks.

a)定义并授权项目。本活动由以下任务组成。

1)Identify potential new or modified capabilities or missions.

1)识别潜在的新能力或经修改的能力，或者新使命或经修改的使命。

> **NOTE 1** The organization strategy, concept of operations, or gap or opportunity analysis is reviewed for current gaps, problems, or opportunities. A new capability or strategic need is usually determined in the business or mission analysis process, further defined in the stakeholder needs and requirements definition process, and managed through this process.

> **注 1**：评审组织战略、运行构想或差距或机会分析，以查明当前的差距、问题或机会。新的能力或战略需要通常由业务或任务分析过程确定，由利益相关方需要与需求定义过程进一步定义，并通过本过程加以管理。

2)Prioritise, select, and establish new strategic opportunities, ventures, or undertakings.

2)对新的战略机会、事业或事项排定优先次序，加以选择并确立。

> **NOTE 2** These are usually consistent with the strategy and action plans of the organization. The potential projects are prioritised and thresholds established to determine which projects will be executed. The characteristics of identified projects are often determined, including stakeholder value, risks and barriers to success, dependencies and inter-relationships, constraints, resource needs, and mutual contention for resources. Each potential project is then assessed with respect to likelihood of success and cost-benefit. The decision management and system analysis processes provide details on performing an analysis of alternatives.

> **注 2**：这些通常与组织的战略和行动计划相一致。对潜在项目排定优先次序并确定阈值，以决定将执行哪些项目。往往会确定所识别项目的特征，包括利益相关方价值、风险与成功障碍、依赖关系与相互关系、约束、资源需要以及对资源的相互争用。随后，针对成功可能性与成本效益对每个潜在项目进行评定。决策管理过程和系统分析过程给出了实施备选方案分析的细节。

3)Define projects, accountabilities, and authorities.

3)定义项目、责任与权限。

4)Identify the expected goals, objectives, and outcomes of each project.

4)识别每个项目的预期目标、目的和结果。

5)Identify and allocate resources for the achievement of project goals and objectives.

5)识别并分配资源，以实现项目目标和目的。

6)Identify any multi-project interfaces and dependencies to be managed or supported by each project.

6)识别需由各项目管理或支持的任何多项目接口和依赖关系。

> **NOTE 3** This includes the use or reuse of enabling systems used by more than one project and the use or reuse of common system elements by more than one project.

> **注 3**：这包括对多个项目所使用的使能系统的使用或重用，以及多个项目对共用系统元素的使用或重用。

> **NOTE 4** Understanding each project in the context of the overall (strategic or enterprise) architecture or SoS environment helps to ensure interfaces and constraints are identified.

> **注 4**：在总体（战略或企业）架构或 SoS 环境的语境中理解每个项目，有助于确保识别出接口和约束。

7)Specify the project reporting requirements and review milestones that govern the execution of each project.

7)规定管控每个项目执行的项目报告要求与评审里程碑。

8)Authorise each project to commence execution of project plans.

8)授权每个项目开始执行项目计划。

> **NOTE 5** Additional information on developing project plans is provided in the project planning process. Project plans are most useful when developed and approved early in the project life cycle.

> **注 5**：关于制定项目计划的附加信息由项目规划过程提供。项目计划在项目生存周期早期制定并获批准时最为有用。

b)Evaluate the portfolio of projects. This activity consists of the following tasks.

b)评估项目组合。本活动由以下任务组成。

1)Evaluate projects to confirm ongoing viability.

1)评估项目，以确认其持续可行性。

> **NOTE 6** Viability includes the following.

> **注 6**：可行性包括以下方面。

a) The project is making progress towards achieving established goals and objectives.

a) 项目正朝着实现既定目标和目的取得进展。

b) The project is complying with project directives.

b) 项目正遵守项目指令。

c) The project is being conducted in accordance with project life cycle policies, processes, and procedures.

c) 项目正按照项目生存周期方针、过程和程序开展。

d) The project remains viable, as indicated by, for example, continuing need for the service, practicable product implementation, and acceptable investment benefits.

d) 项目仍然可行，例如由对服务的持续需要、可行的产品实现和可接受的投资收益所表明。

2)Act to continue projects that are satisfactorily progressing.

2)对进展令人满意的项目，采取措施使其继续实施。

3)Act to redirect projects that can be expected to progress satisfactorily with appropriate redirection.

3)对在适当调整方向后预期能令人满意地进展的项目，采取措施予以重新定向。

c)Terminate projects**.\** This activity consists of the following tasks.

c)终止项目**。\** 本活动由以下任务组成。

1)Where agreements permit, act to cancel or suspend projects whose disadvantages or risks to the organization outweigh the benefits of continued investments.

1)在协议允许的情况下，对给组织带来的不利影响或风险超过继续投资效益的项目，采取措施予以取消或暂停。

2)After completion of the agreement for products and services, act to close the projects.

2)在产品和服务协议完成后，采取措施关闭项目。

> **NOTE 7** Closure is accomplished in accordance with organizational policies and procedures, and the agreement.

> **注 7**：关闭按照组织方针、程序以及协议来完成。

##### 6.2.4 Human resource management process 人力资源管理过程

###### 6.2.4.1 Purpose 目的

The purpose of the human resource management process is to provide the organization with necessary human resources and to maintain their competencies, consistent with strategic needs.

人力资源管理过程的目的是为组织提供必要的人力资源，并按照战略需要保持其能力。

This process provides a supply of skilled and experienced personnel qualified to perform life cycle processes to achieve organization, project, and stakeholder objectives.

本过程提供一批技能娴熟、经验丰富且具备执行生存周期过程资格的人员，以实现组织、项目和利益相关方的目的。

###### 6.2.4.2 Outcomes 预期结果

As a result of the successful performance of the human resource management process:

作为成功实施人力资源管理过程的结果：

a) skills required by projects are identified;

a) 识别出项目所需的技能；

b) necessary human resources are provided to projects;

b) 向项目提供必要的人力资源；

c) skills of personnel are developed, maintained, or enhanced;

c) 人员的技能得到开发、保持或提升；

d) personnel conflicts are resolved.

d) 人员冲突得到解决。

###### 6.2.4.3 Activities and tasks 活动与任务

The organization shall implement the following activities and tasks in accordance with applicable organization policies and procedures with respect to the Human Resource management process.

对于人力资源管理过程，组织应按照适用的组织方针和程序实施以下活动与任务。

a) Identify skills. This activity consists of the following tasks.

a) 识别技能。本活动由以下任务组成。

1) Identify skill needs based on current and expected projects.

1) 根据当前项目和预期项目识别技能需要。

2) Identify and record skills of personnel.

2) 识别并记录人员的技能。

b) Develop skills. This activity consists of the following tasks.

b) 开发技能。本活动由以下任务组成。

1) Establish skills development strategy.

1) 制定技能开发战略。

> **NOTE 1** This strategy includes types and levels of training, categories of personnel, schedules, personnel resource requirements, and training needs.

> **注 1**：该战略包括培训的类型与层级、人员类别、进度安排、人力资源需要以及培训需要。

2) Obtain or develop training, education, or mentoring resources.

2) 获取或开发培训、教育或指导资源。

> **NOTE 2** These resources include training materials that are developed by the organization or external parties, training courses that are available from external suppliers, or computer-based instruction.

> **注 2**：这些资源包括由组织或外部各方开发的培训材料、可从外部供应方获得的培训课程，或基于计算机的教学。

3) Provide planned skill development.

3) 提供有计划的技能开发。

4) Maintain records of skill development.

4) 保持技能开发的记录。

c) Acquire and provide skills. This activity consists of the following tasks.

c) 获取并提供技能。本活动由以下任务组成。

> **NOTE 3** This includes the recruitment and retention of personnel with experience levels and skills necessary to properly staff projects; staff assessment and review, e.g. their proficiency, motivation, ability to work in a team environment, as well as the need to be retrained, reassigned, or reallocated.

> **注 3**：这包括招聘和留用具备为项目恰当配备人员所需的经验水平和技能的人员；人员的评定与审查，例如其熟练程度、积极性、在团队环境中工作的能力，以及接受再培训、重新分配任务或重新调配的需要。

1) Obtain qualified personnel when skill deficits are identified.

1) 在识别出技能不足时获取合格人员。

> **NOTE 4** This includes using outsourced resources.

> **注 4**：这包括使用外包资源。

2) Maintain and manage the pool of skilled personnel necessary to staff ongoing projects.

2) 保持并管理为在办项目配备人员所需的技能人员队伍。

3) Make project assignments based on project and staff-development needs.

3) 根据项目和人员发展需要作出项目任务分配。

4) Motivate personnel, e.g. through career development and reward mechanisms.

4) 激励人员，例如通过职业发展和奖励机制。

5) Resolve personnel conflicts across or within projects.

5) 解决项目之间或项目内部的人员冲突。

> **NOTE 5** This includes conflicts of capacity in organizational infrastructure and supporting services and personnel resources among ongoing projects; or from project personnel being over-committed.

> **注 5**：这包括各在办项目之间在组织基础设施、支持服务和人力资源方面的能力冲突，或源于项目人员承担任务过多而产生的冲突。

##### 6.2.5 Quality management process 质量管理过程

###### 6.2.5.1 Purpose 目的

The purpose of the quality management process is to assure that products, services, and implementations of the quality management process meet organizational and project quality objectives, and achieve customer satisfaction.

质量管理过程的目的是确保产品、服务以及质量管理过程的实施满足组织和项目的质量目标，并实现顾客满意。

###### 6.2.5.2 Outcomes 预期结果

As a result of the successful performance of the quality management process:

作为成功实施质量管理过程的结果：

a) organizational quality management policies, objectives, and procedures are implemented;

a) 组织的质量管理方针、目标和程序得以实施；

b) quality evaluation criteria and methods are established;

b) 建立质量评估准则和方法；

c) resources and information are provided to projects to support the operation and monitoring of project QA activities;

c) 向项目提供资源和信息，以支持项目 QA 活动的运行与监视；

d) QA evaluation results are analysed;

d) 对 QA 评估结果进行分析；

e) quality management policies and procedures are improved based upon project and organizational results.

e) 质量管理方针和程序根据项目和组织的结果得到改进。

> **NOTE** These outcomes have been written to align with ISO 9001:2015, 4.4.1. See ISO 9001 for information regarding how to establish a complete quality management system.

> **注**：这些预期结果在表述上与 ISO 9001:2015，4.4.1 保持一致。关于如何建立完整的质量管理体系的信息，见 ISO 9001。

###### 6.2.5.3 Activities and tasks 活动与任务

The organization shall implement the following activities and tasks in accordance with applicable organization policies and procedures with respect to the quality management process.

对于质量管理过程，组织应按照适用的组织方针和程序实施以下活动与任务。

a) Plan quality management. This activity consists of the following tasks**.\**

a) 规划质量管理。本活动由以下任务组成**。\**

1) Establish quality management policies, objectives, and procedures.

1) 制定质量管理方针、目标和程序。

> **NOTE 1** ISO 9001 is a process model for quality management systems. ISO 9004 contains guidelines for performance improvements. Regulated domains sometimes require specific quality management process standards, e.g. ISO 13485.

> **注 1**：ISO 9001 是质量管理体系的过程模型。ISO 9004 包含绩效改进指南。受监管领域有时要求特定的质量管理过程标准，例如 ISO 13485。

> **NOTE 2** The policies, objectives, and procedures are based on the organization’s strategy for customer satisfaction.

> **注 2**：方针、目标和程序基于组织为实现顾客满意而制定的战略。

2) Define responsibilities and authority for implementation of quality management.

2) 定义实施质量管理的责任与权限。

> **NOTE 3** Resources for quality management are often assigned from distinct organizations for independence from project management.

> **注 3**：为使质量管理独立于项目管理，质量管理的资源往往由不同的组织分派。

3) Define quality evaluation criteria and methods.

3) 定义质量评估准则和方法。

4) Provide resources and information for quality management.

4) 为质量管理提供资源和信息。

b) Assess quality management. This activity consists of the following tasks.

b) 评定质量管理。本活动由以下任务组成。

1) Gather and analyse QA evaluation results, in accordance with the defined criteria.

1) 按所规定的准则收集并分析 QA 评估结果。

2) Assess customer satisfaction.

2) 评定顾客满意。

> **NOTE 4** ISO 10004 contains guidelines for monitoring and measuring customer satisfaction.

> **注 4**：ISO 10004 包含监视和测量顾客满意的指南。

3) Conduct periodic reviews of project QA activities for compliance with the quality management policies, objectives, and procedures.

3) 为符合质量管理方针、目标和程序，对项目 QA 活动进行定期评审。

4) Monitor the status of quality improvements on processes, products, and services.

4) 监视过程、产品和服务的质量改进状况。

c) Perform quality management corrective and preventive action. This activity consists of the following tasks.

c) 实施质量管理纠正措施和预防措施。本活动由以下任务组成。

1) Plan corrective actions when quality management objectives are not achieved.

1) 当质量管理目标未实现时，规划纠正措施。

2) Plan preventive actions when there is a sufficient risk that quality management objectives will not be achieved.

2) 当存在质量管理目标无法实现的足够风险时，规划预防措施。

3) Monitor corrective and preventive actions to completion and inform relevant stakeholders.

3) 监视纠正措施和预防措施直至完成，并告知相关利益相关方。

> **NOTE 5** Implementation of corrective and preventive action is performed in other relevant processes, such as life cycle model management or project assessment and control.

> **注 5**：纠正措施和预防措施的实施在其他相关过程中进行，如生存周期模型管理过程或项目评定与控制过程。

##### 6.2.6 Knowledge management process 知识管理过程

###### 6.2.6.1 Purpose 目的

The purpose of the knowledge management process is to create the capability and assets that enable the organization to exploit opportunities to re-apply existing knowledge.

知识管理过程的目的是建立能力和资产，使组织能利用机会复用既有知识。

This encompasses knowledge, skills, and knowledge assets, including system elements.

这涵盖知识、技能和知识资产，包括系统元素。

###### 6.2.6.2 Outcomes 预期结果

As a result of the successful performance of the knowledge management process:

作为成功实施知识管理过程的结果：

a) a taxonomy for the application of knowledge assets is identified;

a) 识别出知识资产应用的分类法；

b) the organizational knowledge, skills, and knowledge assets are organized;

b) 组织知识、技能和知识资产得到整理；

c) the organizational knowledge, skills, and knowledge assets are available;

c) 组织知识、技能和知识资产可供使用；

d) the organizational knowledge, skills, and knowledge assets are communicated across the organization;

d) 组织知识、技能和知识资产在整个组织内得到传达；

e) knowledge management usage data is analysed.

e) 对知识管理使用数据进行分析。

###### 6.2.6.3 Activities and tasks 活动与任务

The organization shall implement the following activities and tasks in accordance with applicable organization policies and procedures with respect to the knowledge management process.

对于知识管理过程，组织应按照适用的组织方针和程序实施以下活动与任务。

a)Plan knowledge management. This activity consists of the following tasks.

a)规划知识管理。本活动由以下任务组成。

1)Define the knowledge management strategy.

1)定义知识管理战略。

> **NOTE 1** The knowledge management strategy generally includes:

> **注 1**：知识管理战略通常包括：

a) identifying domains and their potential for the reapplication of knowledge;

a) 识别各领域及其复用知识的潜力；

b) plans for obtaining and maintaining knowledge, skills, and knowledge assets for their useful life;

b) 在其使用寿命期内获取和保持知识、技能和知识资产的计划；

c) characterization of the types of knowledge, skills, and knowledge assets to be collected and maintained;

c) 对拟收集和保持的知识、技能和知识资产类型进行特征描述；

d) criteria for accepting, qualifying, and retiring knowledge, skills, and knowledge assets;

d) 知识、技能和知识资产的接收、合格认定和退役准则；

e) procedures for controlling changes to the knowledge, skills, and knowledge assets;

e) 控制知识、技能和知识资产变更的程序；

f) plans, mechanisms, and procedures for protection, control, and access to classified or sensitive data and information;

f) 保护、控制和访问涉密或敏感数据与信息的计划、机制和程序；

g) mechanisms for storage and retrieval.

g) 存储和检索机制。

> **NOTE 2** Knowledge management includes knowledge shared internally within the organization and knowledge that is shared outside the organization with stakeholders, acquirers, and partners, subject to intellectual property and non-disclosure agreements.

> **注 2**：知识管理包括在组织内部共享的知识，以及在遵守知识产权和保密协议的前提下，在组织外部与利益相关方、获取方和合作伙伴共享的知识。

2)Identify the knowledge, skills, and knowledge assets to be managed.

2)识别拟管理的知识、技能和知识资产。

3)Identify projects that can benefit from the application of the knowledge, skills, and knowledge assets.

3)识别能受益于知识、技能和知识资产应用的各项目。

b)Share knowledge and skills throughout the organization. This activity consists of the following tasks.

b)在整个组织内分享知识和技能。本活动由以下任务组成。

1)Establish and maintain a classification for capturing and sharing knowledge and skills across the organization.

1)建立并保持一套分类，用于在整个组织内捕获和分享知识和技能。

> **NOTE 3** This classification includes expert, common, and domain knowledge and skills, as well as lessons learned.

> **注 3**：该分类包括专家知识、通用知识和领域知识及技能，以及经验教训。

2)Capture or acquire knowledge and skills.

2)捕获或获取知识和技能。

3)Make knowledge and skills accessible to the organization.

3)使知识和技能可供组织使用。

c)Share knowledge assets throughout the organization. This activity consists of the following tasks.

c)在整个组织内分享知识资产。本活动由以下任务组成。

1)Establish a taxonomy to organize knowledge assets.

1)建立一套分类法，用以整理知识资产。

> **NOTE 4** The taxonomy includes the following:

> **注 4**：分类法包括以下内容：

a) definition of the boundaries of domains and their relationships to others;

a) 领域边界的定义及其与其他领域的关系；

b) domain models capturing essential common and different features, capabilities, concepts, functions;

b) 体现必要的共性特征与差异特征、能力、概念和功能的领域模型；

c) an architecture for a family of systems within the domain, including their common and different features.

c) 领域内系统族的架构，包括其共性特征与差异特征。

> **NOTE 5** See ISO/IEC 26550 for more information on product line knowledge assets and ISO/IEC/IEEE 42010 for knowledge assets on architecture frameworks, viewpoints, model kinds, views, and models.

> **注 5**：关于产品线知识资产的更多信息，见 ISO/IEC 26550；关于架构框架、架构视角、模型种类、架构视图和模型方面的知识资产，见 ISO/IEC/IEEE 42010。

2)Develop or acquire knowledge assets.

2)开发或获取知识资产。

> **NOTE 6** Knowledge assets include system elements or their representations (e.g. reusable code libraries, reference architectures) architecture or design elements (e.g. architecture or design patterns), processes, criteria, or other technical information (e.g. training materials) related to domain knowledge, and lessons learned.

> **注 6**：知识资产包括系统元素或其表示（如可复用代码库、参考架构）、架构元素或设计元素（如架构模式或设计模式）、过程、准则，或与领域知识有关的其他技术信息（如培训材料），以及经验教训。

3)Make knowledge assets accessible to the organization.

3)使知识资产可供组织使用。

d)Manage knowledge, skills, and knowledge assets. This activity consists of the following tasks.

d)管理知识、技能和知识资产。本活动由以下任务组成。

1)Maintain knowledge, skills, and knowledge assets.

1)保持知识、技能和知识资产。

2)Monitor and record the use of knowledge, skills, and knowledge assets.

2)监视并记录知识、技能和知识资产的使用情况。

3)Periodically reassess the currency of technology and market needs of the knowledge assets.

3)定期重新评定知识资产在技术和市场需求方面的时效性。

#### 6.3 Technical management processes 技术管理过程

##### 6.3.1 Project planning process 项目规划过程

###### 6.3.1.1 Purpose 目的

The purpose of the project planning process is to produce and coordinate effective and workable plans.

项目规划过程的目的是制定并协调有效且可行的计划。

This process determines the scope of the project management and technical activities, identifies process outputs, tasks and deliverables, establishes schedules for task conduct, including achievement criteria, and required resources to accomplish tasks. This is an on-going process that continues throughout a project, with regular revisions to plans. ISO/IEC/IEEE 16326 provides additional information on project planning.

本过程确定项目管理活动与技术活动的范围，识别过程输出、任务和交付物，规定执行任务的进度安排（包括成就准则），以及完成任务所需的资源。这是一个在项目全程持续进行的过程，计划会定期修订。ISO/IEC/IEEE 16326 提供了关于项目规划的附加信息。

> **NOTE** The strategies defined in each of the other processes provide inputs and are integrated in the project planning process. The project assessment and control process is used to assess whether the plans are integrated, aligned, and feasible. Any revision to plans requires approval by the authority defined in the project management plan.

> **注**：其他各过程中界定的战略提供输入，并在项目规划过程中得到整合。项目评定与控制过程用于评定各项计划是否整合、协调一致且可行。计划的任何修订均需由项目管理计划中规定的权限批准。

###### 6.3.1.2 Outcomes 预期结果

As a result of the successful performance of the project planning process:

作为项目规划过程成功执行的结果：

a) objectives and plans are defined;

a) 目标与计划得到规定；

b) roles, responsibilities, accountabilities, and authorities within the project are defined;

b) 项目内的角色、职责、问责和职权得到规定；

c) performance and achievement criteria are defined;

c) 绩效与成就准则得到规定；

d) resources and services necessary to achieve the objectives are committed;

d) 实现目标所必需的资源与服务得到承诺投入；

e) plans for the execution of the project are activated.

e) 项目执行计划得到激活。

###### 6.3.1.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the project planning process.

组织应按照适用的组织方针和规程，针对项目规划过程实施下列活动与任务。

a) Define the project. This activity consists of the following tasks.

a) 定义项目。本活动由以下任务组成。

1) Identify the project objectives, assumptions, and constraints.

1) 识别项目目标、假设和约束。

> **NOTE 1** Objectives and constraints include strategic goals, performance and other quality aspects, cost, schedule, and customer satisfaction. Each objective is identified with a level of detail that permits selection, tailoring, and implementation of the appropriate processes and activities.

> **注 1**：目标与约束包括战略目标、绩效及其他质量方面、成本、进度和顾客满意度。每个目标都以允许选择、裁剪和实施适当过程与活动的详细程度加以识别。

2) Define the project scope as established in the agreement.

2) 规定协议中所确立的项目范围。

> **NOTE 2** This includes all the relevant activities required to satisfy decision criteria and complete the project successfully. A project can have responsibility for one or more stages in the complete system life cycle. Planning includes defining appropriate actions for maintaining project plans, performing assessments and controlling the project.

> **注 2**：这包括为满足决策准则并成功完成项目所需的全部相关活动。一个项目可负责完整系统生存周期中的一个或多个阶段。规划包括规定用于维护项目计划、实施评定和控制项目的适当措施。

3) Define and maintain a life cycle model that is comprised of stages using the defined life cycle models of the organization.

3) 利用组织已定义的生存周期模型，规定并维护由阶段构成的生存周期模型。

> **NOTE 3** ISO/IEC/IEEE 24748-1 provides detailed information regarding life cycle stages and the definition of a representative life cycle model. See 5.5.2 and ISO/IEC/IEEE 24748-1 for information on life cycle models and stages.

> **注 3**：ISO/IEC/IEEE 24748-1 给出了关于生存周期阶段以及代表性生存周期模型定义的详细信息。关于生存周期模型和阶段的信息，见 5.5.2 和 ISO/IEC/IEEE 24748-1。

4) Establish appropriate breakdown structures.

4) 建立适当的分解结构。

> **NOTE 4** Each element is described with a level of detail that is consistent with identified risks and required visibility. Typical breakdown structures include work breakdown structure, functional breakdown structure, system breakdown structure, and organizational breakdown structure. Related tasks in the work breakdown structure are grouped into project tasks. PMI®1) Practice Standard for Work Breakdown Structures[68] contains additional details.

> **注 4**：每个元素都以与已识别风险和所需可见性相一致的详细程度加以描述。典型的分解结构包括工作分解结构、功能分解结构、系统分解结构和组织分解结构。工作分解结构中相关的任务归组为项目任务。PMI®1) 的《工作分解结构实践标准》[68] 载有更多细节。

5) Define and maintain the life cycle processes that will be applied on the project.

5) 规定并维护将应用于项目的生存周期过程。

> **NOTE 5** These processes are based on the defined processes of the organization (see life cycle model management process). The definition of the processes can include the entry criteria; exit criteria; inputs; outputs; process sequence constraints (predecessor/successor relationships); process concurrency requirements (what processes and tasks are worked concurrently with other process area tasks or activities); and scope and cost parameters (for critically important cost estimation).

> **注 5**：这些过程以组织已定义的过程为基础（见生存周期模型管理过程）。过程的定义可包括：进入准则；退出准则；输入；输出；过程顺序约束（前驱／后继关系）；过程并发要求（哪些过程与任务同其他过程领域的任务或活动并发开展）；以及范围和成本参数（用于至关重要的成本估算）。

b) Plan project and technical management. This activity consists of the following tasks.

b) 规划项目与技术管理。本活动由以下任务组成。

1) Define and maintain a schedule based on project objectives and work estimates.

1) 基于项目目标和工作估算，规定并维护进度安排。

> **NOTE 6** This includes definition of the duration, relationship, dependencies, and sequence of activities; achievement milestones; resources employed; the reviews; and schedule reserves for risk management necessary to achieve timely completion of the project.

> **注 6**：这包括规定活动的持续时间、关系、依赖关系和顺序；成就里程碑；所投入的资源；评审；以及为实现项目按期完成所必需的风险管理进度储备。

2) Define achievement criteria for the life cycle stage decision gates, delivery dates, and major dependencies on external inputs or outputs.

2) 为生存周期阶段决策门、交付日期以及对外部输入或输出的主要依赖关系规定成就准则。

3) Define project performance criteria.

3) 规定项目绩效准则。

4) Define the costs and plan a budget.

4) 规定成本并规划预算。

> **NOTE 7** Costs are based on the schedule, labour estimates, infrastructure costs, procurement items, acquired service and enabling system estimates, and budget reserves for risk management.

> **注 7**：成本以进度安排、人工估算、基础设施成本、采购事项、所获取的服务和使能系统估算，以及用于风险管理的预算储备为基础。

5) Define roles, responsibilities, accountabilities, and authorities.

5) 规定角色、职责、问责和职权。

> **NOTE 8** This includes defining the project organization, staff acquisitions, and the development of staff skills. Authorities include, as appropriate, the legally responsible roles and individuals, e.g. design authorization, safety authorization, and award of certification or accreditation.

> **注 8**：这包括规定项目组织、人员招募以及员工技能的培养。职权视情况包括法律上负责的角色和个人，例如设计授权、安全授权以及认证或认可的授予。

6) Define the infrastructure and services required.

6) 规定所需的基础设施和服务。

> **NOTE 9** This includes defining the capacity needed, its availability and its allocation to project tasks. Infrastructure includes facilities, tools, communications, and information technology assets. The requirements for enabling systems for each life cycle stage are also specified.

> **注 9**：这包括规定所需的能力、其可用性及其对项目任务的分配。基础设施包括设施、工具、通信和信息技术资产。还要规定每个生存周期阶段对使能系统的要求。

7) Plan the acquisition of materials and enabling system services supplied from outside the project.

7) 规划从项目外部供应的材料和使能系统服务的获取。

1) PMI® is a trademark of Project Management Institute. This information is given for the convenience of users of this document and does not constitute an endorsement by ISO of the product named.

1) PMI® 是 Project Management Institute 的商标。给出这一信息是为方便本文件的使用者，并不构成 ISO 对所述产品的认可。

> **NOTE 10** This includes, as necessary, plans for solicitation, supplier selection, acceptance, contract administration, and contract closure. The agreement processes are used for the planned acquisitions.

> **注 10**：这视需要包括招标、供应方选择、验收、合同管理和合同收尾的计划。协议过程用于所规划的获取。

> **NOTE 11** The ISO/IEC 27036 series provides guidance for acquisition of infrastructure and services.

> **注 11**：ISO/IEC 27036 系列为基础设施和服务的获取提供指南。

8) Generate and communicate a plan for project and technical management and execution, including reviews.

8) 生成并沟通项目与技术管理及执行的计划，包括评审。

> **NOTE 12** Technical planning for the system is often captured in a systems engineering management plan (SEMP), see ISO/IEC/IEEE 24748-4, or a software engineering management plan. Plans for developing a software system are often captured in a software development plan, see ISO/ IEC/IEEE 24748-5.

> **注 12**：系统的技术规划通常记录在系统工程管理计划（SEMP）中，见 ISO/IEC/IEEE 24748-4；或记录在软件工程管理计划中。开发软件系统的计划通常记录在软件开发计划中，见 ISO/IEC/IEEE 24748-5。

> **NOTE 13** The strategy activities and tasks from each of the other processes provide inputs and are integrated in the project planning process. The project assessment and control process is used to help ensure that the plans are integrated, aligned, and feasible.

> **注 13**：其他各过程中的策略活动与任务提供输入，并在项目规划过程中得到整合。项目评定与控制过程用于帮助确保各项计划得到整合、协调一致且可行。

c) Activate the project. This activity consists of the following tasks.

c) 激活项目。本活动由以下任务组成。

1) Obtain authorization for the project.

1) 获得项目的授权。

> **NOTE 14** The portfolio management process provides the authorization.

> **注 14**：项目组合管理过程提供该授权。

2) Submit requests and obtain commitments for necessary resources to perform the project.

2) 提交请求并获得执行项目所需资源的承诺。

3) Implement project plans.

3) 实施项目计划。

##### 6.3.2 Project assessment and control process 项目评定与控制过程

###### 6.3.2.1 Purpose 目的

The purpose of the project assessment and control process is to assess if the plans are aligned and feasible; determine the status of the project, technical and process performance; and direct execution to help ensure that the performance is according to plans and schedules, within projected budgets, to satisfy project objectives.

项目评定与控制过程的目的是评定各项计划是否协调一致且可行；确定项目、技术与过程绩效的状态；并指导执行，以帮助确保绩效符合计划和进度安排、处于预计预算之内，从而满足项目目标。

This process evaluates, periodically and at major events, the progress and achievements against requirements, plans, and overall strategic objectives. Information is provided for management action when significant variances are detected. This process also includes redirecting the project activities and tasks, as appropriate, to correct identified deviations and variations from other technical management or technical processes. Redirection may include re-planning as appropriate.

本过程定期并在重大事件发生时，对照需求、计划和总体战略目标评估进展与成就。当检测到重大偏差时，提供信息供管理措施使用。本过程还包括视情况重新定向项目的活动与任务，以纠正来自其他技术管理过程或技术过程的已识别偏离和差异。重新定向可包括视情况进行重新规划。

###### 6.3.2.2 Outcomes 预期结果

As a result of the successful performance of the project assessment and control process:

作为项目评定与控制过程成功执行的结果：

a) performance measures or assessment results are available;

a) 绩效测量值或评定结果可供使用；

b) adequacy of roles, responsibilities, accountabilities, authorities, and resources is assessed;

b) 角色、职责、问责、职权和资源的充分性得到评定；

c) technical progress reviews are performed;

c) 实施技术进展评审；

d) deviations in project performance from plans are analysed;

d) 项目绩效相对于计划的偏离得到分析；

e) affected stakeholders are informed of project status;

e) 受影响的利益相关方获知项目状态；

f) corrective action is directed when project performance or achievement is not meeting targets;

f) 当项目绩效或成就未达到目标时，指导采取纠正措施；

g) project replanning is initiated, as necessary;

g) 视需要启动项目重新规划；

h) project action to progress (or not) from one scheduled milestone, decision gate or event to the next is authorised.

h) 项目从一个已排定的里程碑、决策门或事件推进（或不推进）至下一项的行动得到授权。

###### 6.3.2.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the project assessment and control process.

组织应按照适用的组织方针和规程，针对项目评定与控制过程实施下列活动与任务。

a) Plan for project assessment and control. This activity consists of the following task:

a) 规划项目评定与控制。本活动由以下任务组成：

1) Define the project assessment and control strategy.

1) 规定项目评定与控制策略。

> **NOTE 1** The strategy identifies the expected project assessment and control activities, including planned assessment methods and timeframes as well as necessary management and technical reviews.

> **注 1**：该策略识别预期的项目评定与控制活动，包括所规划的评定方法和时间范围，以及必要的管理与技术评审。

b) Assess the project. This activity consists of the following tasks.

b) 评定项目。本活动由以下任务组成。

1) Assess alignment of project objectives and plans with the project context.

1) 评定项目目标和计划与项目语境的一致程度。

2) Assess management and technical plans against objectives to determine adequacy and feasibility.

2) 对照目标评定管理与技术计划，以确定其充分性和可行性。

3) Assess project and technical status against appropriate plans to determine actual and projected cost, schedule, and performance variances.

3) 对照适当的计划评定项目与技术状态，以确定实际的和预计的成本、进度和绩效差异。

4) Assess the adequacy of roles, responsibilities, accountabilities, and authorities.

4) 评定角色、职责、问责和职权的充分性。

> **NOTE 2** This includes assessment of the adequacy of personnel competencies to perform project roles and accomplish project tasks. Objective measures are used wherever possible, e.g. efficiency of resource use, project achievement.

> **注 2**：这包括评定人员能力对履行项目角色和完成项目任务的充分性。尽可能使用客观测量值，例如资源利用效率、项目成就。

5) Assess the adequacy and availability of resources.

5) 评定资源的充分性和可用性。

> **NOTE 3** Resources include infrastructure, personnel, funding, time, or other pertinent items. This task includes evaluating the reuse of existing processes and infrastructure resources, and confirming that intra-organizational commitments are satisfied.

> **注 3**：资源包括基础设施、人员、资金、时间或其他相关事项。本任务包括评估对现有过程和基础设施资源的复用，并确认组织内部的承诺得到满足。

6) Assess progress using measured achievement and milestone completion.

6) 利用所测量的成就和里程碑完成情况评定进展。

> **NOTE 4** This includes collecting and evaluating data for labour, material, service costs, and technical performance, as well as other technical data about objectives, such as affordability. These are compared against measures of achievement. This includes conducting effectiveness assessments to determine the adequacy of the evolving system against requirements. It also includes assessing the readiness of enabling systems to deliver their services when needed.

> **注 4**：这包括收集并评估人工、材料、服务成本以及技术绩效的数据，以及关于目标（如可负担性）的其他技术数据。将这些数据与成就测量值进行比较。这包括实施有效性评定，以确定不断演进的系统相对于需求的充分性。它还包括评定使能系统在需要时交付其服务的就绪程度。

7) Conduct required management and technical reviews, audits, and inspections.

7) 实施所需的管理与技术评审、审核和检查。

> **NOTE 5** These are formal or informal, and are conducted to determine readiness to proceed to the next stage of the life cycle or project milestone, to help ensure that project and technical objectives are being met, or to obtain feedback from stakeholders. These reviews, audits, and inspections are closely coordinated with the quality assurance process. For more information on technical reviews see ISO/IEC/IEEE 24748-8.

> **注 5**：这些评审、审核和检查可以是正式的或非正式的，其目的是确定是否已就绪可进入生存周期的下一阶段或项目里程碑，帮助确保项目与技术目标正在得到满足，或获得利益相关方的反馈。这些评审、审核和检查与质量保证过程密切协调。关于技术评审的更多信息，见 ISO/IEC/IEEE 24748-8。

8) Monitor critical processes and new technologies.

8) 监视关键过程与新技术。

> **NOTE 6** This includes identifying and evaluating technology maturity and feasibility of technology insertion.

> **注 6**：这包括识别并评估技术成熟度以及技术引入的可行性。

9) Make recommendations based on measurement results and other project information.

9) 基于测量结果和其他项目信息提出建议。

> **NOTE 7** Measurement results are analysed to identify deviations, variations, or undesirable trends from planned values that include potential concerns, and to make appropriate recommendations for corrective, preventive, adaptive, additive, or perfective actions. This includes, where appropriate, statistical analysis of measures that indicates trends, e.g. fault density to indicate quality of outputs, distribution of measured parameters that indicate process repeatability.

> **注 7**：分析测量结果，以识别相对于计划值的偏离、差异或不良趋势（包括潜在关注点），并针对纠正性、预防性、适应性、补充性或完善性措施提出适当建议。这视情况包括表明趋势的测量值统计分析，例如以故障密度表明输出的质量、以所测量参数的分布表明过程可重复性。

10) Record and provide status and findings from assessment tasks.

10) 记录并提供评定任务的状态和结果。

11) Monitor process execution within the project.

11) 监视项目内的过程执行情况。

> **NOTE 8** This includes the analysis of process measures and review of trends with respect to project objectives. Any improvement actions identified would be handled through the quality assurance process or the life cycle model management process.

> **注 8**：这包括分析过程测量值并对照项目目标审查趋势。所识别的任何改进措施均通过质量保证过程或生存周期模型管理过程处理。

c) Control the project. This activity consists of the following tasks.

c) 控制项目。本活动由以下任务组成。

1) Initiate necessary actions needed to address identified issues.

1) 启动处理已识别问题所需的必要措施。

> **NOTE 9** This occurs when project or technical achievement is not meeting planned targets. This includes corrective, preventive, and problem resolution actions. Actions generally require replanning or reassignment of personnel, tools, and infrastructure assets and often impact the cost, schedule, or technical scope or definition. Actions sometimes require changes to the implementation and execution of the life cycle processes.

> **注 9**：这发生在项目或技术成就未达到计划目标之时。这包括纠正性、预防性和问题解决措施。措施通常需要重新规划或重新分派人员、工具和基础设施资产，并且常常影响成本、进度或技术范围或定义。措施有时需要更改生存周期过程的实施与执行。

> **NOTE 10** Actions are recorded and reviewed to confirm their adequacy and timeliness.

> **注 10**：记录并审查各项措施，以确认其充分性和及时性。

2) Initiate necessary project replanning.

2) 启动必要的项目重新规划。

> **NOTE 11** The project planning process is invoked for replanning when project objectives or constraints have changed, or when planning assumptions are shown to be invalid.

> **注 11**：当项目目标或约束发生变化，或规划假设被证明无效时，调用项目规划过程进行重新规划。

> **NOTE 12** Any change that requires a change to the agreement between acquirer and supplier invokes the acquisition and supply processes.

> **注 12**：任何需要更改获取方与供应方之间协议的变更，均调用获取过程和供应过程。

3) Initiate necessary change actions when there is a contractual change to cost, time, or quality due to the impact of an acquirer or supplier request.

3) 当因获取方或供应方请求的影响而发生成本、时间或质量的合同变更时，启动必要的变更措施。

> **NOTE 13** This includes consideration of modified terms and conditions for supply or initiating new supplier selection, which invokes the acquisition and supply processes.

> **注 13**：这包括考虑修改供应条款和条件，或启动新的供应方选择，后者调用获取过程和供应过程。

4) Authorise the project to proceed toward the next milestone, decision gate, or event, if justified.

4) 在有正当理由时，授权项目推进至下一里程碑、决策门或事件。

> **NOTE 14** The decision management process is used to reach agreement on milestone or decision gate completion.

> **注 14**：使用决策管理过程就里程碑或决策门的完成达成一致。

##### 6.3.3 Decision management process 决策管理过程

###### 6.3.3.1 Purpose 目的

The purpose of the decision management process is to provide a structured, analytical framework for objectively identifying, characterizing, and evaluating a set of alternatives for a decision at any point in the life cycle and select the most beneficial course of action.

决策管理过程的目的是提供一个结构化、分析性的框架，以便在生存周期中的任何时点客观地识别、表征和评估一组决策备选方案，并选择最有益的行动方案。

> **NOTE 1** This process is used to resolve technical or project issues and to respond to requests for decisions encountered during the system life cycle. Typical approaches include identification of the alternative(s) that provides the preferred outcomes for the situation. The methods most frequently used for decision management are the trade-off study, cost-benefit analysis, engineering analysis, and problem-solving analysis (e.g., TRIZ and Kepner-Tregoe). Each of the alternatives is assessed against the decision criteria (e.g., cost impact, schedule impact, programmatic constraints, regulatory implications, technical performance characteristics, critical quality characteristics, SoS considerations, and risk). Results of these comparisons are ranked, via a suitable selection model, and are then used to decide on an optimal solution. Key study data (e.g. assumptions and decision rationale) are typically managed to inform decision-makers, re-justify the decision in the future, and support future decision-making.

> **注 1**：本过程用于解决技术或项目问题，并响应系统生存周期中遇到的决策请求。典型途径包括识别能为该情况提供优选结果的备选方案。决策管理最常用的方法是权衡研究、成本效益分析、工程分析和问题解决分析（例如 TRIZ 和 Kepner-Tregoe）。每个备选方案都对照决策准则（例如成本影响、进度影响、项目性约束、法规影响、技术绩效特性、关键质量特性、SoS 考虑事项和风险）进行评定。这些比较的结果通过适当的选择模型排序，随后用于决定最优解。关键研究数据（例如假设和决策理由）通常受到管理，以告知决策者、将来重新论证该决策并支持未来的决策。

> **NOTE 2** When it is necessary to perform a detailed assessment of a parameter for one of the criteria, the system analysis process is employed to perform the assessment.

> **注 2**：当需要对某一准则的参数进行详细评估时，采用系统分析过程来实施该评估。

###### 6.3.3.2 Outcomes 预期结果

As a result of the successful performance of the decision management process:

作为决策管理过程成功执行的结果：

a) decisions requiring alternative analysis are identified;

a) 需要备选方案分析的决策得到识别；

b) alternative courses of action are evaluated;

b) 备选行动方案得到评估；

c) a preferred course of action is selected;

c) 选出一个优选的行动方案；

d) the resolution, decision rationale, and assumptions are recorded.

d) 解决方案、决策理由和假设得到记录。

###### 6.3.3.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the decision management process.

组织应按照适用的组织方针和规程，针对决策管理过程实施下列活动与任务。

a) Prepare for decisions. This activity consists of the following tasks.

a) 为决策作准备。本活动由以下任务组成。

1) Define a decision management strategy.

1) 规定决策管理策略。

> **NOTE 1** A decision management strategy includes the identification of roles, responsibilities, accountabilities, and authorities. It includes the identification of decision categories and a prioritization scheme. Decisions often arise as a result of an effectiveness assessment, a technical trade-off, a problem needing to be solved, an action needed as a response to risk exceeding the acceptable threshold, or a new opportunity or approval for project progression to the next life cycle stage. Organization or project guidelines determine the level of rigor and formality to apply to the decision analysis.

> **注 1**：决策管理策略包括识别角色、职责、问责和职权。它包括识别决策类别和一个优先次序方案。决策往往因以下情况而产生：有效性评定、技术权衡、需要解决的问题、为应对超出可接受阈值的风险而需采取的措施，或新机会或者批准项目推进至下一生存周期阶段。组织或项目指南确定适用于决策分析的严格程度和正式程度。

2) Identify the circumstances and need for a decision.

2) 识别需要作出决策的情形和需要。

> **NOTE 2** Problems or opportunities and the alternative courses of action that will resolve their outcome are recorded, categorised, and reported.

> **注 2**：记录、分类并报告问题或机会以及将解决其结果的备选行动方案。

3) Involve relevant stakeholders in the decision-making to draw on experience and knowledge.

3) 让有关利益相关方参与决策，以借鉴经验和知识。

b) Analyse the decision information. This activity consists of the following tasks.

b) 分析决策信息。本活动由以下任务组成。

1) Select and declare the decision management strategy for each decision.

1) 为每项决策选择并声明决策管理策略。

> **NOTE 3** The level of rigor required to resolve these problems or opportunities is determined, as well as the data and system analysis needed for evaluating the alternatives.

> **注 3**：确定解决这些问题或机会所需的严格程度，以及评估备选方案所需的数据和系统分析。

2) Determine desired outcomes and measurable selection criteria.

2) 确定期望结果和可测量的选择准则。

> **NOTE 4** The desired value for all quantifiable criteria and the threshold value(s) beyond which the attribute will be unsatisfactory are determined. Typically, weighting factors for all criteria are determined.

> **注 4**：确定所有可量化准则的期望值，以及超过后该属性将不可接受的阈值。通常确定所有准则的权重系数。

3) Identify the trade space and alternatives.

3) 识别权衡空间和备选方案。

> **NOTE 5** If a large number of alternatives exist, they are qualitatively screened to reduce alternatives to a manageable number for further detailed system analysis. This screening is often based on qualitative assessments of such factors as risk, cost, schedule, and regulatory impacts. This includes new design parameters, different architecture characteristics, SoS considerations, range of values for critical quality characteristics as well as risks and opportunities.

> **注 5**：如果存在大量备选方案，则对其进行定性筛选，将备选方案减少到可管理的数量，以便进一步开展详细的系统分析。这种筛选通常基于对风险、成本、进度和法规影响等因素的定性评定。这包括新的设计参数、不同的架构特性、SoS 考虑事项、关键质量特性的取值区间以及风险与机会。

4) Evaluate each alternative against the criteria.

4) 对照准则评估每个备选方案。

> **NOTE 6** The system analysis process is used, as necessary, to quantify specific criteria for each trade-off alternative to be evaluated. This includes new design parameters, different architecture characteristics, SoS considerations, and range of values for critical quality characteristics. The system analysis process assesses the range of parameter variations to obtain a sensitivity analysis for each of the trade-off alternatives evaluated. These results are used to establish the feasibility of the various trade-off alternatives.

> **注 6**：视需要使用系统分析过程，为待评估的每个权衡备选方案量化特定准则。这包括新的设计参数、不同的架构特性、SoS 考虑事项以及关键质量特性的取值区间。系统分析过程评定参数变化的范围，以获得对每个所评估权衡备选方案的敏感性分析。这些结果用于确立各种权衡备选方案的可行性。

c) Make and manage decisions. This activity consists of the following tasks.

c) 作出并管理决策。本活动由以下任务组成。

1) Determine preferred alternative for each decision.

1) 为每项决策确定优选备选方案。

> **NOTE 7** Alternatives are evaluated quantitatively, using the selection criteria. The selected alternative generally provides an optimization of, or improvement in an identified decision.

> **注 7**：使用选择准则对备选方案进行定量评估。所选备选方案通常针对已识别的决策提供优化或改进。

2) Record the resolution, decision rationale, and assumptions.

2) 记录解决方案、决策理由和假设。

3) Record, track, evaluate, and report decisions.

3) 记录、跟踪、评估并报告决策。

> **NOTE 8** This includes records of problems and opportunities, accountability for the decision, and disposition, as stipulated in agreements or organizational procedures and in a manner that permits auditing and learning from experience.

> **注 8**：这包括记录问题与机会、决策的问责以及处置，按协议或组织规程的规定，并以允许审核和从经验中学习的方式进行。

> **NOTE 9** This allows the organization to confirm that problems have been effectively resolved, adverse trends have been reversed, unanticipated risks and consequences have been addressed, and opportunities have been exploited.

> **注 9**：这使组织能够确认问题已得到有效解决、不良趋势已得到扭转、未预料的风险与后果已得到处理，并且机会已得到利用。

##### 6.3.4 Risk management process 风险管理过程

###### 6.3.4.1 Purpose 目的

The purpose of the risk management process is to identify, analyse, treat, and monitor the risks continually.

风险管理过程的目的是持续地识别、分析、处理和监视风险。

The risk management process systematically addresses uncertainty throughout the life cycle of a system product or service towards achieving objectives.

风险管理过程在系统产品或服务的整个生存周期内，为实现目标而系统地处理不确定性。

> **NOTE** In Clause 3, risk is defined as the “effect of uncertainty on objectives”. Consequently, risks can be either positive or negative. However, in common usage, risk generally means a negative effect. This document uses common interpretation of risk where there is a negative effect. When the effect is positive, it is often considered an opportunity. The risk management activities defined below can easily be adapted to also cover opportunities; additional guidance is provided in notes in the risk management process activities and tasks.

> **注**：在第 3 章中，风险被定义为“不确定性对目标的影响”。因此，风险既可以是正面的，也可以是负面的。但在通常用法中，风险一般指负面影响。本文件采用风险具有负面影响的通常解释。当影响为正面时，往往将其视为机会。下文所定义的风险管理活动能容易地加以调整，从而同样涵盖机会；风险管理过程的活动与任务中的注给出了附加指南。

###### 6.3.4.2 Outcomes 预期结果

As a result of the successful performance of the risk management process:

作为风险管理过程成功执行的结果：

a) risks are identified;

a) 风险得到识别；

b) risks are analysed;

b) 风险得到分析；

c) risk treatments are selected;

c) 风险处理方案得到选择；

d) appropriate treatments are implemented;

d) 适当的处理方案得到实施；

e) risks are evaluated to assess changes in status and progress in treatment;

e) 对风险进行评估，以评定其状态变化和处理进展；

f) risk profile is maintained.

f) 风险概况得到维护。

###### 6.3.4.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the risk management process.

组织应按照适用的组织方针和规程，针对风险管理过程实施下列活动与任务。

> **NOTE 1** ISO/IEC/IEEE 16085 provides a more detailed set of risk management activities and tasks and is aligned with ISO 31000 and ISO Guide 73*.\* ISO 9001:2015, Clause A.4 provides additional risk-based thinking to address preventive action with respect to quality management.

> **注 1**：ISO/IEC/IEEE 16085 给出了更详细的一组风险管理活动与任务，并与 ISO 31000 和 ISO Guide 73* 保持一致。\* ISO 9001:2015 的 A.4 给出附加的基于风险的思维，以处理与质量管理有关的预防措施。

a)Plan risk management. This activity consists of the following tasks.

a) 规划风险管理。本活动由以下任务组成。

1)Define the risk management strategy.

1) 规定风险管理策略。

> **NOTE 2** The strategy typically defines the scope of the risk management process, risk management approach, and risk criteria, measures, parameters, rating scale, and treatment alternatives. This includes a description of the risk management process at all levels of the supply chain and describes how risks from all suppliers will be raised to the next level(s) for incorporation in the project risk management process.

> **注 2**：该策略通常规定风险管理过程的范围、风险管理途径以及风险准则、测量值、参数、评级量表和处理备选方案。这包括描述供应链各层级的风险管理过程，并描述来自所有供应方的风险如何上报至上一层级，以纳入项目风险管理过程。

> **NOTE 3** To additionally cover the management of opportunities, the strategy can include opportunities in the scope and approach, as well as define the opportunity criteria, measures, parameters, rating scale, and treatment alternatives.

> **注 3**：为额外涵盖机会管理，该策略可将机会纳入范围与途径，并规定机会准则、测量值、参数、评级量表和处理备选方案。

2)Define and record the context of the risk management process.

2) 规定并记录风险管理过程的语境。

> **NOTE 4** This includes the identification of the stakeholders and description of their perspectives, risk categories, and a description (perhaps by reference) of the technical and managerial objectives, assumptions, and constraints. The risk categories include the relevant technical areas of the system and facilitate identification of risks across the life cycle of the system.

> **注 4**：这包括识别利益相关方并描述其视角、风险类别，以及对技术与管理目标、假设和约束的描述（可通过引用）。风险类别包括系统的相关技术领域，并有助于识别系统整个生存周期内的风险。

> **NOTE 5** Opportunities provide potential benefits for the system or project. Each of the opportunities pursued have associated risks that detract from the expected benefit. This includes the risks associated with not pursuing an opportunity, as well as the risk of not achieving the effects of the opportunity.

> **注 5**：机会为系统或项目提供潜在收益。所追求的每个机会都伴有关联风险，这些风险会减损预期收益。这包括与不追求某一机会相关联的风险，以及未能实现该机会效果的风险。

b)Maintain the risk profile. This activity consists of the following tasks.

b)维护风险概况。本活动由下列任务组成。

1)Define and record the risk thresholds and conditions.

1)定义并记录风险阈值与条件。

> **NOTE 6** Risk (and opportunity) thresholds define the levels at which the appropriate treatment strategies are considered.

> **注 6**：风险（与机会）阈值定义考虑适当处理策略所处的层级。

2)Establish and maintain a risk profile.

2)建立并维护风险概况。

> **NOTE 7** A risk profile includes:

> **注 7**：风险概况包括：

- description of the risk;

- 风险的描述；

- the risk's likely causes and events;

- 风险的可能原因与事件；

- possible consequences of the risk;

- 风险的可能后果；

- the risk's severity of consequences;

- 风险后果的严重程度；

- the risk's likelihood of occurrence;

- 风险的发生可能性；

- the risk's likelihood of detection in the case the risk become an issue;

- 在风险成为问题的情况下检测到该风险的可能性；

- the risk's thresholds and conditions;

- 风险的阈值与条件；

- the risk's current state;

- 风险的当前状态；

- the risk's current treatment, or contingency strategy or plan;

- 风险的当前处理，或应急策略或计划；

- the risk's history.

- 风险的历史。

The risk profile is updated and baselined periodically. Updates are typically made when there are changes in:

风险概况定期更新并基线化。通常在下列方面发生变化时进行更新：

- the risk management context;

- 风险管理语境；

- a new risk is identified;

- 识别出新风险；

- any change in an existing risk’s information.

- 既有风险的信息发生任何变化。

> **NOTE 8** When addressing opportunities, typically one profile is used for both risks and opportunities to gain a better understanding of the overall contingencies.

> **注 8**：在处置机会时，通常对风险与机会使用同一份概况，以更好地理解总体应急安排。

3)Periodically provide the relevant risk profile to stakeholders.

3)定期向利益相关方提供相关的风险概况。

c)Analyse risks. This activity consists of the following tasks.

c)分析风险。本活动由下列任务组成。

1)Identify risks in the categories described in the risk management context.

1)按风险管理语境中描述的类别识别风险。

> **NOTE 9** Risks are commonly identified through various analyses, such as safety, reliability, assurance, producibility, and performance analyses; technology, architecture, integration, and readiness assessments; measurement reports; and trade-off studies. Sometimes, these risks are identified early in the life cycle and continue into the utilization, support, and retirement of the system. Additionally, risks are often identified through the analysis of measures associated with system goals, e.g. measures of effectiveness or measures of performance. See IEC 31010 which includes several methods for identifying risks.

> **注 9**：风险通常通过各种分析来识别，例如安全性、可靠性、保证、可生产性与性能分析；技术、架构、集成与就绪性评定；测量报告；以及权衡研究。有时，这些风险在生存周期早期即被识别出来，并延续到系统的使用、保障与退役阶段。此外，风险常常通过分析与系统目标相关联的度量来识别，例如有效性度量或性能度量。见 IEC 31010，其中包含若干识别风险的方法。

2)Estimate the likelihood of occurrence and consequences of each identified risk.

2)估计每一已识别风险的发生可能性与后果。

3)Evaluate each risk against its risk thresholds.

3)对照风险阈值评估每一风险。

4)Define and record recommended treatment strategies and measures for each risk that exceeds its risk threshold.

4)对每一超出其风险阈值的风险，定义并记录建议的处理策略与度量。

> **NOTE 10** Risk treatment strategies include, but are not limited to, eliminating the risk, reducing its likelihood of occurrence or severity of consequence, or accepting the risk. Opportunity treatment strategies include pursuing or exploiting the opportunity, deferring, or monitoring. Treatment strategies can also include taking or increasing risk to pursue an opportunity. Measures provide information about the effectiveness of the treatment alternatives.

> **注 10**：风险处理策略包括但不限于：消除风险，降低其发生可能性或后果严重程度，或接受风险。机会处理策略包括：追求或利用机会、推迟或监视。处理策略还可包括为追求机会而承担或增加风险。度量提供有关各处理备选方案有效性的信息。

d)Treat risks that exceed their risk threshold. This activity consists of the following tasks.

d)处理超出其风险阈值的风险。本活动由下列任务组成。

1)Identify recommended alternatives for risk treatment.

1)识别建议的风险处理备选方案。

2)Define measures for determining the effectiveness of risk treatments.

2)定义用于确定风险处理有效性的度量。

3)Implement selected risk treatments.

3)实施选定的风险处理。

> **NOTE 11** Typically, the implemented alternative can be the one for which the stakeholders determine the actions taken will make a risk acceptable. If there is more than one alternative with acceptable risk levels, decision criteria are established and applied to choose the best alternative.

> **注 11**：通常，所实施的备选方案可以是经利益相关方判定、所采取的措施将使风险变为可接受的那一个。若存在多个风险水平均可接受的备选方案，则建立并应用决策准则以选出最佳备选方案。

4)Coordinate management action for selected risk treatments.

4)为选定的风险处理协调管理措施。

> **NOTE 12** Further information can be found in 6.3.2.

> **注 12**：进一步信息见 6.3.2。

e)Monitor risks. This activity consists of the following tasks.

e)监视风险。本活动由下列任务组成。

1)Continually monitor all risks and the risk management context.

1)持续监视所有风险及风险管理语境。

> **NOTE 13** When risks change their state, the changes are captured and the risks are re-evaluated. Risks that exceed thresholds are considered as high priority and are continually monitored to determine if any future risk treatment actions are necessary.

> **注 13**：当风险的状态发生变化时，捕获这些变化并重新评估风险。超出阈值的风险被视为高优先级，并持续加以监视，以确定未来是否需要采取风险处理措施。

2)Implement and monitor measures to evaluate the effectiveness of risk treatments.

2)实施并监视用于评估风险处理有效性的度量。

3)Continually monitor for the emergence of new risks and sources throughout the life cycle.

3)在整个生存周期内持续监视新风险与新风险源的出现。

##### 6.3.5 Configuration management process 配置管理过程

###### 6.3.5.1 Purpose 目的

The purpose of the configuration management process is to manage system and system element configurations over their life cycle.

配置管理过程的目的是在系统与系统元素的生存周期内管理其配置。

Managing includes establishing and maintaining consistency, integrity, traceability, and control. Configurations include products and their product configuration information.

管理包括建立并保持一致性、完整性、可追溯性与控制。配置包括产品及其产品配置信息。

###### 6.3.5.2 Outcomes 预期结果

As a result of the successful performance of the configuration management process:

配置管理过程成功执行的结果是：

a) system and system element configurations are managed;

a) 系统与系统元素的配置得到管理；

b) configuration baselines, including approved configurations, are maintained;

b) 配置基线（包括已批准的配置）得到维护；

c) changes to items under configuration management are controlled;

c) 纳入配置管理的项的更改得到控制；

d) configuration status information is available;

d) 配置状态信息可获取；

e) required configuration audits are completed;

e) 所需的配置审核得以完成；

f) system releases are approved.

f) 系统发布得到批准。

###### 6.3.5.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the configuration management process.

就配置管理过程而言，下列活动与任务应按照适用的组织方针与规程实施。

a)Prepare for configuration management. This activity consists of the following tasks.

a)准备配置管理。本活动由下列任务组成。

1)Define a configuration management strategy.

1)定义配置管理策略。

> **NOTE 1** This includes details covering:

> **注 1**：这包括涵盖下列方面的细节：

a) roles, responsibilities, accountabilities, and authorities;

a) 角色、职责、问责与职权；

b) management of changes to items under configuration management, including dispositions, access, release, and control;

b) 纳入配置管理的项的更改管理，包括处置、访问、发布与控制；

c) the necessary baselines to be established;

c) 需建立的必要基线；

d) the locations and conditions of storage, the storage media and their environment, in accordance with designated levels of integrity, security, and safety;

d) 按照指定的完整性、安全与安全性级别确定的存储位置与条件、存储介质及其环境；

e) the criteria or events for commencing configuration control and maintaining baselines of evolving configurations;

e) 启动配置控制并维护不断演进的配置基线的准则或事件；

f) the audit strategy and the responsibilities for assessing continual integrity and security of the configuration definition information;

f) 审核策略，以及评定配置定义信息持续完整性与安全的职责；

g) change management, including any planned configuration control boards, regular and emergency change requests, and procedures for change management;

g) 更改管理，包括任何已计划的配置控制委员会、常规与紧急更改请求，以及更改管理规程；

h) coordination across the applicable stakeholders, including the set of acquirer, supplier, and supply chain organizations, as well as interacting organizations in an SoS environment.

h) 适用的利益相关方之间的协调，包括获取方、供应方与供应链组织这一集合，以及 SoS 环境中相互交互的组织。

> **NOTE 2** The strategy covers the life of the system, or the extent of the contract, as appropriate.

> **注 2**：该策略视情况涵盖系统的寿命，或合同的范围。

> **NOTE 3** Additional guidance regarding configuration management activities can be found in ISO 10007, IEEE Std 828, SAE EIA-649, STANAG 4427, and SAE ARP4754A.

> **注 3**：有关配置管理活动的附加指南见 ISO 10007、IEEE Std 828、SAE EIA-649、STANAG 4427 和 SAE ARP4754A。

2)Define the archive and retrieval approach for items under configuration management, as well as configuration management artefacts and data.

2)为纳入配置管理的项以及配置管理人工制品与数据定义存档和检索途径。

> **NOTE 4** This includes data retention procedures that need to be aligned with the information management process.

> **注 4**：这包括需要与信息管理过程保持一致的数据留存规程。

b)Perform configuration identification. This activity consists of the following tasks.

b)执行配置标识。本活动由下列任务组成。

1)Identify the system elements and artefacts that need to be under configuration management.

1)识别需要纳入配置管理的系统元素与人工制品。

> **NOTE 5** Items under configuration management are often called configuration items. They receive special attention. They are often the subject of reviews and configuration audits. Items subject to configuration management usually include requirements, models, product and system elements, services, and baselines.

> **注 5**：纳入配置管理的项常称为配置项。它们受到特别关注。它们常常是评审与配置审核的对象。受配置管理约束的项通常包括需求、模型、产品与系统元素、服务以及基线。

2)Identify the configuration data to be managed.

2)识别待管理的配置数据。

> **NOTE 6** This includes the relationships between system elements as well as the associated data.

> **注 6**：这包括系统元素之间的关系以及相关联的数据。

3)Establish unique identifiers for the items under configuration management.

3)为纳入配置管理的项建立唯一标识符。

> **NOTE 7** Items are distinguished by unique identifiers or markings. The identifiers are in accordance with relevant standards and product sector conventions, such that the items under configuration control are unambiguously traceable to their specifications or equivalent, recorded descriptions. The ISO/IEC 19770 series includes requirements for unique identification of IT assets that are configuration items.

> **注 7**：项通过唯一标识符或标记加以区分。这些标识符符合相关标准与产品行业惯例，从而使受配置控制的项能够明确无误地追溯到其规格或等效的已记录描述。ISO/IEC 19770 系列标准包含对作为配置项的 IT 资产进行唯一标识的要求。

4)Define baselines through the life cycle.

4)定义贯穿生存周期的基线。

> **NOTE 8** Baselines capture the evolving configuration states of system elements at designated times or under defined circumstances. The content for the baselines is developed through the technical processes, but is formalised at a point in time through the configuration management process. Baselines form the basis for the next change.

> **注 8**：基线在指定时刻或规定情况下捕获系统元素不断演进的配置状态。基线的内容通过技术过程形成，但通过配置管理过程在某一时点予以正式化。基线构成下一次更改的基础。

5)Obtain applicable stakeholder agreement to establish a baseline.

5)取得适用利益相关方的同意以建立基线。

> **NOTE 9** The project assessment and control process is used to reach agreement.

> **注 9**：使用项目评定与控制过程达成一致。

6)Approve and track system or system element releases.

6)批准并跟踪系统或系统元素的发布。

> **NOTE 10** The purpose of a release is to authorise the use of a system or system element for a specific purpose, with or without restrictions. Examples are releases for tests or for operational use.

> **注 10**：发布的目的是授权将系统或系统元素用于特定目的，可带限制或不带限制。例如，用于试验或运行使用的发布。

> **NOTE 11** Releases generally include a set of changes. These changes are made through the technical processes and then verified or validated through the verification and validation processes. Approval of a release generally includes acceptance of the verified and validated changes.

> **注 11**：发布通常包含一组更改。这些更改通过技术过程作出，然后通过验证过程和确认过程加以验证或确认。发布的批准通常包括接收经验证和确认的更改。

c)Perform configuration change management. This activity consists of the following tasks.

c)执行配置更改管理。本活动由下列任务组成。

> **NOTE 12** Configuration change management establishes procedures and methods for managing change to a baseline once it is established. This is sometimes referred to as configuration control.

> **注 12**：配置更改管理建立用于在基线建立后管理基线更改的规程与方法。这有时称为配置控制。

1)Identify and record requests for change and requests for variance.

1)识别并记录更改请求与偏离请求。

> **NOTE 13** A request for variance is sometimes referred to as a deviation, waiver, or concession.

> **注 13**：偏离请求有时称为偏差、豁免或让步。

2)Coordinate, evaluate, and disposition requests for change and requests for variance.

2)协调、评估并处置更改请求与偏离请求。

> **NOTE 14** This includes an impact assessment of proposed changes, including impact on project plans, costs, benefits, risks, quality, and schedule. A decision is made on whether to implement or close the change request.

> **注 14**：这包括对拟议更改的影响评定，涉及对项目计划、成本、效益、风险、质量与进度的影响。就是否实施或关闭更改请求作出决策。

3)Submit requests for review and approval.

3)提交请求以供评审和批准。

> **NOTE 15** Requests for change and requests for variance are often under the formal control of a configuration control board (CCB). Evaluation includes analysis of need versus impact.

> **注 15**：更改请求与偏离请求常常处于配置控制委员会（CCB）的正式控制之下。评估包括对需要与影响的分析。

4)Track and manage approved changes to the baseline, requests for change, and requests for variance.

4)跟踪并管理对基线的已批准更改、更改请求与偏离请求。

> **NOTE 16** This task involves prioritization, tracking, scheduling, and closing changes. Changes are then made through the technical processes. These changes are verified or validated through the verification and validation processes, to help ensure that the approved changes have been made.

> **注 16**：本任务涉及更改的排定优先次序、跟踪、安排进度与关闭。随后通过技术过程作出更改。这些更改通过验证过程和确认过程加以验证或确认，以帮助确保已批准的更改已经作出。

> **NOTE 17** It is good practice to record the rationale for changes.

> **注 17**：记录更改的理由是一种良好实践。

d)Perform configuration status accounting. This activity consists of the following tasks.

d)执行配置状态记帐。本活动由下列任务组成。

1)Develop and maintain the configuration management status information, for system elements, baselines, and releases.

1)为系统元素、基线与发布建立并维护配置管理状态信息。

> **NOTE 18** Configuration status accounting provides the data on the status of controlled products or services needed to make decisions regarding system elements throughout the product life cycle. This includes taking into account the nature of the items under configuration control. Configuration descriptions conform, where possible, to product or technology standards. Configuration information permits forward and backward traceability to other configuration states. The rationale for the baselines and releases and associated authorizations in configuration data are generally recorded. Configuration records are maintained through the system life cycle and then archived taking into account agreements, relevant legislation, or best industry practice.

> **注 18**：配置状态记帐提供有关受控产品或服务状态的数据，这些数据是在整个产品生存周期内就系统元素作出决策所需的。这包括考虑受配置控制的项的性质。配置描述尽可能符合产品或技术标准。配置信息允许向前和向后追溯到其他配置状态。基线、发布以及配置数据中相关授权的理由通常予以记录。配置记录在系统生存周期内予以维护，然后考虑协议、相关法规或最佳行业实践予以存档。

> **NOTE 19** The recording, retrieval, and consolidation of the current configuration status and the status of all preceding configurations to confirm information correctness, timeliness, integrity, and security is managed. Audits are performed to verify conformance of a baseline to drawings, interface control documents, and other agreement requirements.

> **注 19**：对当前配置状态及所有先前配置状态的记录、检索与合并加以管理，以确认信息的正确性、及时性、完整性与安全。执行审核以验证基线符合图样、接口控制文件及其他协议要求。

2)Capture, store, and report configuration management data.

2)捕获、存储并报告配置管理数据。

e)Perform configuration verification and audit. This activity consists of the following tasks.

e)执行配置验证与审核。本活动由下列任务组成。

1)Identify the need for configuration and configuration management verification activities and audits.

1)识别对配置及配置管理验证活动与审核的需要。

> **NOTE 20** The configuration management process works in conjunction with the verification process to identify and perform the verification activities.

> **注 20**：配置管理过程与验证过程协同工作，以识别并执行这些验证活动。

2)Verify the product or service configuration meets the configuration requirements.

2)验证产品或服务配置满足配置要求。

> **NOTE 21** This is performed by comparing requirements, constraints, and waivers (variances) with results of formal verification activities.

> **注 21**：这通过将要求、约束与豁免（偏离）同正式验证活动的结果相比较来完成。

3)Monitor the incorporation of approved configuration changes.

3)监视已批准配置更改的纳入。

4)Perform configuration and configuration management verification activities and audits to establish product baselines.

4)执行配置及配置管理验证活动与审核，以建立产品基线。

> **NOTE 22** Typical audits include the functional configuration audit (FCA) that is focused on functional and performance capabilities and the physical configuration audit (PCA) that is focused on system conformance to operational and configuration information items. The verification process is used to perform configuration verification and audits.

> **注 22**：典型的审核包括：聚焦于功能与性能能力的功能配置审核（FCA），以及聚焦于系统对运行信息部件与配置信息部件符合性的物理配置审核（PCA）。使用验证过程执行配置验证与审核。

5)Record the configuration management audit and other configuration evaluation results and disposition action items.

5)记录配置管理审核及其他配置评估结果，并对措施项作出处置。

##### 6.3.6 Information management process 信息管理过程

###### 6.3.6.1 Purpose 目的

The purpose of the information management process is to generate, obtain, confirm, transform, retain, retrieve, disseminate, and dispose of information for designated stakeholders.

信息管理过程的目的是为指定的利益相关方生成、获取、确认、变换、留存、检索、分发和处置信息。

Information management plans, executes, and controls the provision of information for designated stakeholders that is unambiguous, complete, verifiable, consistent, modifiable, traceable, and presentable. Information includes technical, project, organizational, agreement, and user information. Information is often derived from data records of the organization, system, process, or project.

信息管理对为指定利益相关方提供明确、完整、可验证、一致、可修改、可追溯且可呈现的信息进行规划、执行和控制。信息包括技术信息、项目信息、组织信息、协议信息与用户信息。信息常常源自组织、系统、过程或项目的数据记录。

###### 6.3.6.2 Outcomes 预期结果

As a result of the successful performance of the information management process:

信息管理过程成功执行的结果是：

a) information to be managed is identified;

a) 待管理的信息得到识别；

b) information representations are defined;

b) 信息表示得到定义；

c) information is managed;

c) 信息得到管理；

d) the status of information is identified;

d) 信息的状态得到识别；

e) information is available to designated stakeholders.

e) 信息可为指定的利益相关方所获取。

###### 6.3.6.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the information management process.

就信息管理过程而言，下列活动与任务应按照适用的组织方针与规程实施。

> **NOTE 1** ISO/IEC/IEEE 15289 summarises requirements for the content of life cycle process information items (documentation) and provides guidance on their development.

> **注 1**：ISO/IEC/IEEE 15289 概述了对生存周期过程信息部件（文档）内容的要求，并对其编制提供指南。

a) Prepare for information management. This activity consists of the following tasks.

a) 准备信息管理。本活动由下列任务组成。

1) Define the strategy for information management.

1) 定义信息管理策略。

> **NOTE 2** Information about the same topic can be developed in different ways at different points in the life cycle and for different audiences.

> **注 2**：关于同一主题的信息，可以在生存周期的不同时点、针对不同受众以不同方式编制。

2) Define the items of information that will be managed.

2) 定义将被管理的信息部件。

> **NOTE 3** This includes the information that will be managed during the system life cycle and possibly maintained for a defined period beyond. Organizational policy, agreements, or legislation are taken into account.

> **注 3**：这包括在系统生存周期内将被管理、并可能在此后规定期限内继续维护的信息。考虑组织方针、协议或法规。

3) Designate authorities and responsibilities for information management.

3) 指定信息管理的职权与职责。

> **NOTE 4** Due regard is paid to information and data legislation, security and privacy, e.g. ownership, agreement restrictions, rights of access, data rights, intellectual property and patents. Where restrictions or constraints apply, information is identified accordingly. Staff having knowledge of such items of information are informed of their obligations and responsibilities.

> **注 4**：适当顾及信息与数据法规、安全与隐私，例如所有权、协议限制、访问权、数据权利、知识产权与专利。凡适用限制或约束之处，相应标明有关信息。知悉此类信息的员工应被告知其义务与职责。

4) Define the content, formats, and structure of information items.

4) 定义信息部件的内容、格式与结构。

> **NOTE 5** The information originates and terminates in many forms (e.g. audio-visual, textual, graphical, numerical) and media (e.g. electronic, printed, magnetic, optical). Organization constraints, e.g. infrastructure, inter-organizational communications, and distributed project workings, are taken into account. Relevant information item standards and conventions are used taking into account policy, agreements, and legislation constraints.

> **注 5**：信息以多种形式（例如音频视频、文本、图形、数字）和多种介质（例如电子、印刷、磁性、光学）产生和终止。考虑组织约束，例如基础设施、组织间通信与分布式项目工作方式。在考虑方针、协议与法规约束的前提下，使用相关的信息部件标准与惯例。

5) Define information maintenance actions.

5) 定义信息维护措施。

> **NOTE 6** Information maintenance includes status reviews of stored information for integrity, validity, and availability. It also includes any needs for replication or transformation to an alternative medium, as necessary, either to retain infrastructure as technology changes so that archived media can be read or to migrate archived media to newer technology.

> **注 6**：信息维护包括对已存储信息进行状态评审，以检查完整性、有效性与可用性。它还包括对复制或变换到替代介质的任何需要（视需要而定），以便在技术变化时保留基础设施从而使存档介质仍可读取，或者将存档介质迁移到更新的技术。

b) Perform information management. This activity consists of the following tasks.

b) 执行信息管理。本活动由下列任务组成。

1) Obtain, develop, or transform the identified items of information.

1) 获取、编制或变换已识别的信息部件。

> **NOTE 7** This includes collecting the data, information, or information items from appropriate sources (e.g. resulting from any life cycle process), and writing, illustrating, or transforming it into useable information for stakeholders. It includes reviewing, validating, and editing information per information standards.

> **注 7**：这包括从适当的来源（例如由任何生存周期过程产生）收集数据、信息或信息部件，并撰写、图解或将其变换为利益相关方可用的信息。它包括按照信息标准评审、确认和编辑信息。

2) Maintain information items and their storage records, and record the status of information.

2) 维护信息部件及其存储记录，并记录信息的状态。

> **NOTE 8** Information items are maintained in accordance with their integrity, security, and privacy requirements. The status of information items is maintained (e.g. version description, date of issue or validity date, record of distribution, security classification). Legible information is stored and retained in such a way that it is readily retrievable.

> **注 8**：信息部件按其完整性、安全与隐私要求予以维护。维护信息部件的状态（例如版本说明、发布日或有效日期、分发记录、安全密级）。清晰可读的信息以易于检索的方式存储和留存。

> **NOTE 9** The source data and tools used to transform information, along with the resulting documentation is placed under configuration control in accordance with the configuration management process. ISO/IEC/IEEE 26531 provides information on requirements for content management systems useful for life cycle information and documentation.

> **注 9**：用于变换信息的源数据与工具，连同所产生的文档，按照配置管理过程置于配置控制之下。ISO/IEC/IEEE 26531 提供了有关内容管理系统要求的信息，这些系统可用于生存周期信息与文档。

3) Publish, distribute, or provide access to information to designated stakeholders.

3) 向指定的利益相关方发布、分发信息或提供对信息的访问。

> **NOTE 10** Information is provided to designated stakeholders in an appropriate form, as required by agreed schedules or defined circumstances. Information items include official documentation used for certification, accreditation, licence, or assessment ratings, as required.

> **注 10**：信息按约定的时间安排或规定情况的要求，以适当形式提供给指定的利益相关方。信息部件包括按需用于认证、认可、许可或评定等级的正式文档。

4) Archive designated information.

4) 存档指定的信息。

> **NOTE 11** Archiving is done in accordance with the audit, knowledge retention, regulatory, agreement, and project closure purposes. The media, location, and protection of the information are selected in accordance with the specified storage and retrieval periods, taking into account organizational policy, agreements, and legislation. Arrangements are put in place to retain necessary information items after project closure.

> **注 11**：存档依据审核、知识留存、法规、协议与项目收尾等目的进行。信息的介质、位置与保护措施按照规定的存储期与检索期选择，并考虑组织方针、协议与法规。作出安排，以便在项目收尾后留存必要的信息部件。

5) Dispose of unwanted, invalid, or unvalidated information.

5) 处置不需要的、无效的或未确认的信息。

> **NOTE 12** Legislative rules, organization policy, and security and privacy requirements are taken into account.

> **注 12**：考虑法规规则、组织方针以及安全与隐私要求。

##### 6.3.7 Measurement process 测量过程

###### 6.3.7.1 Purpose 目的

The purpose of the measurement process is to collect, analyse, and report objective data and information to support effective management and address information needs about the products, services, and processes.

测量过程的目的是收集、分析和报告客观的数据与信息，以支持有效管理并满足有关产品、服务与过程的信息需要。

###### 6.3.7.2 Outcomes 预期结果

As a result of the successful performance of the measurement process:

测量过程成功执行的结果是：

a) information needs are identified;

a) 信息需要得到识别；

b) an appropriate set of measures, based on the information needs, are identified or developed;

b) 基于信息需要识别或制定出一组适当的度量；

c) required data is managed;

c) 所需的数据得到管理；

d) the data is analysed and the results interpreted;

d) 数据得到分析，结果得到解释；

e) measurement results provide objective information that support decisions.

e) 测量结果提供支持决策的客观信息。

###### 6.3.7.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the measurement process.

就测量过程而言，下列活动与任务应按照适用的组织方针与规程实施。

> **NOTE 1** ISO/IEC/IEEE 15939 provides a more detailed set of measurement activities and tasks that are aligned with the activities and tasks shown below.

> **注 1**：ISO/IEC/IEEE 15939 提供了与下列活动与任务相一致的一套更详细的测量活动与任务。

> **NOTE 2** ISO 9001:2015, 7.1.5 specifies quality management system requirements for measurement and monitoring of processes and products.

> **注 2**：ISO 9001:2015 的 7.1.5 规定了针对过程和产品的测量与监视的质量管理体系要求。

a) Prepare for measurement. This activity consists of the following tasks.

a) 准备测量。本活动由下列任务组成。

1) Define the measurement strategy.

1) 定义测量策略。

2) Describe the characteristics of the organization that are relevant to measurement.

2) 描述组织中与测量相关的特性。

3) Identify and prioritise the information needs.

3) 识别信息需要并排定其优先次序。

> **NOTE 3** The information needs are based on the organization's strategic objectives, the project objectives, identified risks, and other items related to project decisions.

> **注 3**：信息需要以组织的战略目标、项目目标、已识别的风险以及与项目决策相关的其他事项为依据。

4) Select and specify measures that satisfy the information needs.

4) 选择并规定满足信息需要的度量。

5) Define data collection, analysis, access, and reporting procedures.

5) 定义数据收集、分析、访问与报告规程。

6) Define criteria for evaluating the information items and the measurement process.

6) 定义用于评估信息部件和测量过程的准则。

7) Identify and plan for the necessary enabling systems or services to be used.

7) 识别并规划将使用的必要使能系统或服务。

8) Obtain or acquire access to the enabling systems or services to be used.

8) 取得或获得对将使用的使能系统或服务的访问。

b) Perform measurement. This activity consists of the following tasks.

b) 执行测量。本活动由下列任务组成。

1) Integrate procedures for data generation, collection, analysis, and reporting into the relevant processes.

1) 将数据生成、收集、分析与报告的规程集成到相关过程中。

> **NOTE 4** Some of these required changes are integrated into other life cycle processes.

> **注 4**：其中一些所需的更改被集成到其他生存周期过程中。

2) Collect, store, and verify data.

2) 收集、存储并验证数据。

3) Analyse data and develop information items.

3) 分析数据并编制信息部件。

4) Record results and inform the measurement users.

4) 记录结果并告知测量用户。

> **NOTE 5** The measurement analyses results are reported to relevant stakeholders in a timely, usable fashion to support decision-making and assist in corrective, preventive, adaptive, additive, and perfective actions; risk management; and improvements. Results are reported to decision process participants, technical and management review participants, and product and process improvement process owners.

> **注 5**：测量分析结果以及时、可用的方式报告给相关利益相关方，以支持决策，并有助于纠正性、预防性、适应性、追加性与完善性措施、风险管理以及改进。结果报告给决策过程的参与者、技术评审与管理评审的参与者，以及产品和过程改进过程的所有者。

##### 6.3.8 Quality assurance process 质量保证过程

###### 6.3.8.1 Purpose 目的

The purpose of the quality assurance process is to help ensure the effective application of the organization’s quality management process to the project.

质量保证过程的目的是帮助确保组织的质量管理过程在项目中得到有效应用。

QA focuses on providing confidence that quality requirements are fulfilled. Proactive analysis of the project life cycle processes and outputs is performed to help ensure that the product being produced or the service being developed is of the desired quality and that organization and project policies and procedures are followed.

QA 着眼于提供质量要求得到满足的信任。对项目生存周期过程与输出开展主动分析，以帮助确保正在生产的产品或正在开发的服务具有所期望的质量，并确保组织与项目的方针和规程得到遵循。

> **NOTE** Establishing an assurance case (see 5.10) can be applied to guide QA activities and to help ensure critical quality characteristics are considered.

> **注**：建立保证案例（见 5.10）能用于指导 QA 活动，并有助于确保考虑关键质量特性。

###### 6.3.8.2 Outcomes 预期结果

As a result of the successful performance of the quality assurance process:

质量保证过程成功执行的结果是：

a) QA procedures, including criteria and methods for QA evaluations, are implemented;

a) QA 程序（包括 QA 评估的准则和方法）得以实施；

b) evaluations of products, services, and processes are performed, consistent with quality management policies, procedures, and requirements;

b) 产品、服务和过程的评估按照质量管理方针、程序和需求实施；

c) results of evaluations are provided to relevant stakeholders;

c) 将评估结果提供给相关利益相关方；

d) incidents are resolved;

d) 事件得到解决；

e) prioritised problems are treated.

e) 已排定优先次序的问题得到处理。

> **NOTE** Outcomes a) through d) align with the outcomes of the quality management process.

> **注**：预期结果 a) 至 d) 与质量管理过程的预期结果相一致。

###### 6.3.8.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures.

以下活动与任务应按照适用的组织方针与程序予以实施。

a)Prepare for quality assurance. This activity consists of the following tasks.

a) 为质量保证做准备。本活动由以下任务组成。

1)Define a QA strategy.

1) 定义 QA 策略。

> **NOTE 1** The strategy is consistent with the quality management policies, objectives, and procedures; and includes:

> **注 1**：该策略与质量管理方针、目标和程序相一致，并包括：

a) project QA procedures;

a) 项目 QA 程序；

b) defined roles, responsibilities, accountabilities, and authorities;

b) 所规定的角色、职责、问责和职权；

c) activities appropriate to each life cycle process;

c) 适宜于每个生存周期过程的活动；

d) activities appropriate to each supplier (including subcontractors);

d) 适宜于每个供应方（包括分包方）的活动；

e) required verification, validation, monitoring, measurement, inspection, and test activities specific to the product or service;

e) 针对产品或服务所需的验证、确认、监视、测量、检验和试验活动；

f) criteria for product or service acceptance and evaluation criteria and methods for process, product, and service evaluations.

f) 产品或服务的验收准则，以及针对过程、产品和服务评估的评估准则与方法。

2)Establish independence of QA from other life cycle processes.

2) 确立 QA 相对于其他生存周期过程的独立性。

> **NOTE 2** Resources for QA are often assigned from distinct organizations for independence from project management.

> **注 2**：为使 QA 独立于项目管理，QA 的资源往往由不同的组织分派。

b)Perform product or service evaluations. This activity consists of the following tasks.

b) 执行产品或服务评估。本活动由以下任务组成。

1)Evaluate products and services for conformance to established criteria, contracts, standards, and regulations.

1) 评估产品和服务与既定准则、合同、标准和法规的符合性。

> **NOTE 3** This includes system quality requirements that are derived from the stakeholder needs and requirements definition and system requirements definition processes. See ISO/IEC 25010 for more information.

> **注 3**：这包括由利益相关方需要与需求定义过程和系统需求定义过程导出的系统质量要求。更多信息见 ISO/IEC 25010。

2)Perform verification and validation of the outputs of the life cycle processes to determine conformance to specified requirements.

2) 对生存周期过程的输出执行验证和确认，以判定与规定要求的符合性。

c)Perform process evaluations. This activity consists of the following tasks.

c) 执行过程评估。本活动由以下任务组成。

1)Evaluate project life cycle processes for conformance.

1) 评估项目生存周期过程的符合性。

2)Evaluate tools and environments that support or automate the process for conformance.

2) 评估支持该过程或使其自动化的工具与环境的符合性。

3)Evaluate supplier processes for conformance to process requirements.

3) 评估供应方过程与过程要求的符合性。

> **NOTE 4** Typically, items such as a collaborative development environment, process measures that suppliers are required to provide, or a risk process that suppliers are required to use are considered.

> **注 4**：通常考虑诸如协同开发环境、要求供应方提供的过程测量值，或要求供应方使用的风险过程等事项。

d)Manage QA records and reports. This activity consists of the following tasks.

d) 管理 QA 记录和报告。本活动由以下任务组成。

1)Create records and reports related to QA activities.

1) 创建与 QA 活动有关的记录和报告。

> **NOTE 5** Records and reports are created using the information management process and taking into account organizational, regulatory, and project requirements.

> **注 5**：记录和报告使用信息管理过程创建，并考虑组织要求、法规要求和项目要求。

2)Maintain, store, and distribute records and reports.

2) 保持、存储并分发记录和报告。

3)Identify incidents and problems associated with product, service, and process evaluations.

3) 识别与产品、服务和过程评估有关的事件和问题。

> **NOTE 6** This includes the capture of lessons learned and the conduct of surveillance reviews of process implementation through the supply chain.

> **注 6**：这包括捕获经验教训，以及对整个供应链中过程实施情况开展监督审查。

e)Treat incidents and problems. This activity consists of the following tasks.

e) 处理事件和问题。本活动由以下任务组成。

> **NOTE 7** In the terminology of quality management, problems are often described as “non-conformities” which, if left untreated, can cause the project to fail to meet its requirements.

> **注 7**：在质量管理的术语中，问题常被称为“不合格”，若不予处理，能导致项目无法满足其要求。

> **NOTE 8** For additional information and examples of problem categories and priority classifications, see ISO/IEC/IEEE 24748-1:2018, Annex G.

> **注 8**：关于问题类别与优先级分类的更多信息与示例，见 ISO/IEC/IEEE 24748-1:2018 附录 G。

1)Incidents are recorded, analysed, and classified.

1) 记录、分析和分类事件。

2)Incidents are resolved or elevated to problems.

2) 解决事件，或将事件升级为问题。

3)Problems are recorded, analysed, and classified.

3) 记录、分析和分类问题。

> **NOTE 9** Analysis results include potential treatment options.

> **注 9**：分析结果包括潜在的处理方案。

4)Treatments for problems are prioritised and implementation is tracked.

4) 对问题的处理排定优先次序，并跟踪实施情况。

> **NOTE 10** Implementation is done in the technical processes after initiation by the project assessment and control process.

> **注 10**：经项目评定与控制过程启动后，实施在技术过程中完成。

5)Trends in incidents and problems are noted and analysed.

5) 关注并分析事件和问题的趋势。

6)Stakeholders are informed of the status of incidents and problems.

6) 将事件和问题的状态告知利益相关方。

7)Incidents and problems are tracked to closure.

7) 跟踪事件和问题直至关闭。

#### 6.4 Technical processes 技术过程

##### 6.4.1 Business or mission analysis process 业务或任务分析过程

###### 6.4.1.1 Purpose 目的

The purpose of the business or mission analysis process is to define the overall strategic problem or opportunity, characterize the solution space, and determine potential solution class(es) that can address a problem or take advantage of an opportunity.

业务或任务分析过程的目的是定义总体战略问题或机会，表征解空间，并确定能够处理问题或利用机会的潜在解类。

> **NOTE 1** The organizational strategy and concept of operations of the organization(s) with a potential need for the system solution establishes the context within which the business or mission analysis is performed. The organizational concept of operations reflects the leadership's intended way of operating the organization. It describes the organization’s assumptions and how it intends to use the system to be developed, existing systems, and possible future systems in support of an overall operation or series of operations of the business. In the case that the organization is the SoI, the organization’s strategy is part of the system definition.

> **注 1**：对于具有潜在系统解需要的组织，其组织战略与运行构想确立了开展业务或任务分析的语境。组织运行构想反映领导层运行组织的预期方式。它描述组织的各项假设，以及组织打算如何使用待开发的系统、现有系统和可能的未来系统，以支持业务的总体运行或一系列运行。在组织即 SoI 的情况下，组织战略是系统定义的一部分。

> **NOTE 2** In some domains, this relates to the concept of identifying and analysing capabilities that are needed or desired by the organization. This process focuses on the necessary capabilities and interacts with the portfolio management process for identifying the trade space that can address the capability. The identified problems or opportunities are often translated into target capabilities. As applicable within a given domain, the problem or opportunity space includes the target capabilities.

> **注 2**：在某些业务域中，这涉及识别并分析组织所需或所期望的能力这一概念。本过程聚焦于必要的能力，并与项目组合管理过程交互，以识别能够应对该能力的权衡空间。所识别的问题或机会往往转换为目标能力。在给定业务域内视适用情况，问题或机会空间包括目标能力。

> **NOTE 3** Business or mission analysis is part of the activities of concept definition – the set of systems engineering activities in which the problem space and the needs of the business or enterprise and stakeholders are closely examined.

> **注 3**：业务或任务分析是概念定义活动的一部分——概念定义是一组系统工程活动，其中细致考察问题空间以及业务或企业及利益相关方的需要。

###### 6.4.1.2 Outcomes 预期结果

As a result of the successful performance of the business or mission analysis process:

业务或任务分析过程成功执行后：

a) the problem or opportunity space is defined;

a) 问题或机会空间得到界定；

b) the solution space is characterized;

b) 解空间得到表征；

c) preliminary operational concepts and other concepts in the life cycle stages are defined;

c) 初步运行概念以及生存周期各阶段中的其他概念得到界定；

d) alternative solution classes are analysed;

d) 备选解类得到分析；

e) the preferred alternative solution class(es) are selected;

e) 优选的备选解类得到选定；

f) enabling systems or services needed for business or mission analysis are available;

f) 业务或任务分析所需的使能系统或服务可用；

g) traceability of strategic problems and opportunities and the preferred alternative solution classes is established.

g) 战略问题与机会以及优选的备选解类的追溯性得以建立。

###### 6.4.1.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the business or mission analysis process.

以下活动与任务应按照适用于业务或任务分析过程的组织方针与程序予以实施。

a) Prepare for business or mission analysis. This activity consists of the following tasks.

a) 为业务或任务分析做准备。本活动由以下任务组成。

1) Review changes to the organization strategy and concept of operations to identify potential problems and opportunities with respect to desired organization mission(s), vision, goals, and objectives.

1) 审查组织战略与运行构想的变更，以针对所期望的组织任务、愿景、目标和目的，识别潜在的问题与机会。

> **NOTE 1** This includes identified deficiencies or gaps in existing capabilities, systems, products, or services.

> **注 1**：这包括现有能力、系统、产品或服务中已识别的缺陷或差距。

2) Define the business or mission analysis strategy.

2) 定义业务或任务分析策略。

> **NOTE 2** This includes the approach to be used to identify and define the problem space, characterize the solution space, and select a solution class.

> **注 2**：这包括用于识别并定义问题空间、表征解空间以及选择解类的途径。

3) Identify and plan for the necessary enabling systems or services needed to support business or mission analysis.

3) 识别支持业务或任务分析所需的必要使能系统或服务，并作出规划。

> **NOTE 3** This includes identification of requirements and interfaces for enabling systems. Enabling systems for business or mission analysis include the business systems and repositories of the organization.

> **注 3**：这包括识别使能系统的需求和接口。用于业务或任务分析的使能系统包括组织的业务系统和存储库。

4) Obtain or acquire access to the enabling systems or services to be used.

4) 获得或取得对将使用的使能系统或服务的访问权。

> **NOTE 4** The validation process is used to objectively confirm that the enabling system achieves its intended use for its enabling functions.

> **注 4**：使用确认过程客观地确认使能系统就其使能功能达成了其预期用途。

b) Define the problem or opportunity space. This activity consists of the following tasks.

b) 定义问题或机会空间。本活动由以下任务组成。

1) Analyse the problems and opportunities in the context of relevant trade-space factors.

1) 在相关权衡空间因素的语境中分析问题与机会。

> **NOTE 5** This analysis is focused on understanding the scope, basis, or drivers of the problems or opportunities, as opposed to the synthesis that is the focus of system analysis and decision management needed for trade-off studies. The focus here includes changes in mission requirements, business needs and opportunities, capabilities, performance improvement, or lack of existing systems, security and safety improvement, factors such as cost and effectiveness, regulation changes, user dissatisfaction, and PESTEL (political, economic, social, technological, environmental, and legal) factors. This can be accomplished through external, internal, or SWOT (strengths, weaknesses, opportunities, and threats) analyses.

> **注 5**：本分析聚焦于理解问题或机会的范围、依据或驱动因素，这与权衡研究所需要的、以综合为焦点的系统分析和决策管理不同。此处的焦点包括任务需求的变化、业务需要与机会、能力、绩效改进或现有系统的缺乏、安全与安全性的改进、成本与有效性等因素、法规变化、用户不满，以及 PESTEL（政治、经济、社会、技术、环境与法律）因素。这能通过外部、内部或 SWOT（优势、劣势、机会与威胁）分析来完成。

> **NOTE 6** The outputs of the analysis are considered as part of the portfolio management decisions.

> **注 6**：分析的输出作为项目组合管理决策的一部分予以考虑。

2) Define the mission, business, or operational problem or opportunity to be addressed by a solution.

2) 定义拟由解予以处理的任务、业务或运行问题或机会。

> **NOTE 7** This definition includes the context, any key parameters, and critical business success measures without regard to a specific solution, since the solution can be an operational change, a change to an existing product or service, or a new system.

> **注 7**：该定义包括语境、任何关键参数以及关键业务成功度量，而不考虑具体解，因为解能是运行变更、对现有产品或服务的更改，或新系统。

3) Prioritise the potential problem or opportunity against other business needs.

3) 相对于其他业务需要，对潜在问题或机会排定优先次序。

> **NOTE 8** This task attempts to develop an understanding of the relative importance of addressing this new business need (the problem or opportunity) versus other business needs that are not part of the new solution. This is especially important when there is a limited amount of resources available.

> **注 8**：本任务试图理解处理这一新业务需要（问题或机会）相对于不属于新解的其他业务需要的相对重要性。在可用资源有限时，这一点尤为重要。

c) Characterize the solution space. This activity consists of the following tasks.

c) 表征解空间。本活动由以下任务组成。

1) Define preliminary operational concepts and other life cycle concepts.

1) 定义初步运行概念及其他生存周期概念。

> **NOTE 9** This involves the identification of major stakeholder groups such as customers, users, administrations, regulators, and system owners that are defined in the stakeholder needs and requirements definition process.

> **注 9**：这涉及识别主要的利益相关方群体，例如顾客、用户、管理部门、监管机构和系统所有者，这些均在利益相关方需要与需求定义过程中定义。

> **NOTE 10** Preliminary life cycle concepts include preliminary acquisition concepts, preliminary deployment concepts, preliminary operational concepts, preliminary support concepts, and preliminary retirement concepts. Operational concepts include high level operational modes or states, operational scenarios, potential use cases, or usage within a proposed business strategy. These concepts enable feasibility analysis and evaluation of alternatives. These concepts are further refined within the stakeholder needs and requirements definition process.

> **注 10**：初步生存周期概念包括初步获取概念、初步部署概念、初步运行概念、初步保障概念和初步退役概念。运行概念包括高层级的运行模式或状态、运行场景、潜在用例，或在所提议业务策略中的使用方式。这些概念支持可行性分析以及对备选方案的评估。这些概念在利益相关方需要与需求定义过程中进一步细化。

> **NOTE 11** The operating environment can have vulnerabilities associated with specific security threats and safety hazards. These vulnerabilities are reviewed in association with the product under development. The system and human interfaces are an element of the system assurance context and related vulnerabilities are examined in the context of mission critical threads.

> **注 11**：运行环境可能存在与特定安全威胁和安全性危害相关的脆弱性。这些脆弱性结合待开发的产品予以审查。系统接口与人的接口是系统保证语境的一个要素，相关脆弱性在任务关键线程的语境中予以考察。

2) Identify alternative solution classes that span the potential solution space.

2) 识别跨越潜在解空间的备选解类。

> **NOTE 12** These classes can range from simple operational changes to various system developments or modifications. The solution space can include the identification of existing assets, systems, and software products suitable for reuse, and changes in services that can address the need for operational or functional modifications. This includes deducing what potential expected services will be needed. The solution space characterization often invokes the system architecture definition process for a user architecture viewpoint resulting in architecture views (e.g. capability views, programme views, operational views, and user or human views) as proposed by ISO/IEC/IEEE 42010.

> **注 12**：这些解类的范围从简单的运行变更到各种系统开发或修改不等。解空间能包括识别适于重用的现有资产、系统和软件产品，以及能够应对运行或功能修改需要的服务变更。这包括推断将需要哪些潜在的预期服务。解空间表征往往为建立用户架构视角而调用系统架构定义过程，从而形成 ISO/IEC/IEEE 42010 所提议的架构视图（例如能力视图、项目群视图、运行视图以及用户视图或人的视图）。

d) Evaluate alternative solution classes. This activity consists of the following tasks.

d) 评估备选解类。本活动由以下任务组成。

> **NOTE 13** If no single system solution alternative exists from evaluation results, an SoS solution can be alternatively identified and evaluated as an alternative solution class. Further information of SoS can be found in 5.4, ISO/IEC/IEEE 21840, and ISO/IEC/IEEE 21841.

> **注 13**：如果评估结果中不存在单一系统解备选方案，则可替代地识别 SoS 解，并将其作为备选解类予以评估。关于 SoS 的更多信息见 5.4、ISO/IEC/IEEE 21840 和 ISO/IEC/IEEE 21841。

1) Assess each alternative solution class.

1) 评定每个备选解类。

> **NOTE 14** A solution class refers to the means of achieving a solution, such as a new system, adapting or modifying an existing system, linking system elements from various systems, exercising operational considerations. Solution classes look at different approaches to providing a solution.

> **注 14**：解类指实现解的手段，例如新系统、改编或修改现有系统、将来自不同系统的系统元素关联起来、实施运行方面的考虑。解类考察提供解的不同途径。

> **NOTE 15** Each alternative solution class is assessed against defined criteria that are established based on the organization's strategy. Feasibility of the solution class and its capability to meet the strategic needs and requirements are key decision criteria. The portfolio management process provides some criteria to be considered.

> **注 15**：依据基于组织战略建立的规定准则，对每个备选解类进行评定。解类的可行性及其满足战略需要与需求的能力是关键决策准则。项目组合管理过程提供一些宜予考虑的准则。

> **NOTE 16** The system analysis process is used to assess the value of each criterion for each alternative solution class. Structured affordability trade-offs are recommended. Including cost as a criterion aids affordability decisions. The assessment of alternatives can include modelling, simulation, analytical techniques, or expert judgement to understand the risks, feasibility, and value of the alternative solution classes.

> **注 16**：使用系统分析过程评定每个备选解类各项准则的值。宜进行结构化的可负担性权衡。将成本作为一项准则有助于可负担性决策。备选方案的评定能包括建模、仿真、分析技术或专家判断，以理解备选解类的风险、可行性与价值。

2) Select the preferred alternative solution class(es).

2) 选出优选的备选解类。

> **NOTE 17** The decision management process is used to evaluate alternatives and to guide selection. Selected alternatives are validated in the context of the organization's strategy. Feedback on risks, feasibility, market factors, and alternatives is provided for use in updating the organization's strategy.

> **注 17**：使用决策管理过程评估备选方案并指导选择。所选备选方案在组织战略的语境中得到确认。提供关于风险、可行性、市场因素和备选方案的反馈，以供更新组织战略之用。

3) Provide feedback to strategic level life cycle concepts to reflect the selected solution class(es).

3) 向战略层级的生存周期概念提供反馈，以反映所选的解类。

e) Manage the business or mission analysis. This activity consists of the following tasks.

e) 管理业务或任务分析。本活动由以下任务组成。

1) Record key business or mission analysis decisions and the rationale.

1) 记录关键的业务或任务分析决策及其理由。

> **NOTE 18** Rationale includes information about major alternatives and enablers.

> **注 18**：理由包括有关主要备选方案与使能因素的信息。

2) Maintain traceability of business or mission analysis and the alternative solution class(es).

2) 维护业务或任务分析以及备选解类的追溯性。

> **NOTE 19** Through the life cycle, bi-directional traceability is maintained between the business or mission problems and opportunities, and the preferred alternative solution classes with the organizational strategy, stakeholder needs and requirements, and system analysis results supporting decisions.

> **注 19**：在整个生存周期内，在业务或任务问题与机会以及优选的备选解类，与组织战略、利益相关方需要与需求以及支持决策的系统分析结果之间，维护双向追溯性。

3) Provide key artefacts that have been selected for baselines.

3) 提供已选定用于基线的关键人工制品。

> **NOTE 20** The configuration management process is used to establish and maintain configuration items and baselines. The business or mission analysis process identifies candidates for the baseline, and then provides the artefacts to configuration management.

> **注 20**：使用配置管理过程建立并维护配置项与基线。业务或任务分析过程识别基线的候选对象，随后将人工制品提供给配置管理。

##### 6.4.2 Stakeholder needs and requirements definition process 利益相关方需要与需求定义过程

###### 6.4.2.1 Purpose 目的

The purpose of the stakeholder needs and requirements definition process is to define the stakeholder needs and requirements for a system that can provide the capabilities needed by users and other stakeholders in a defined environment.

利益相关方需要与需求定义过程的目的是，针对能够在规定环境中提供用户与其他利益相关方所需能力的系统，定义利益相关方需要与需求。

It identifies stakeholders, or stakeholder classes, involved with the system throughout its life cycle, and their needs. It analyses and transforms these needs into a common set of stakeholder requirements that express the intended interaction the system will have with its operational environment and that are the reference against which each resulting operational capability is validated. The stakeholder requirements are defined considering the context of the SoI, which includes the interoperating systems and enabling systems. This also includes consideration of laws and regulations, environmental restrictions, and ethical values.

本过程识别在系统整个生存周期中与系统有关的利益相关方或利益相关方类别及其需要。本过程分析这些需要，并将其转换为共同的一组利益相关方需求，这些需求表达系统将与其运行环境进行的预期交互，并且是对由此产生的每项运行能力进行确认所依据的参照。利益相关方需求的定义考虑 SoI 的语境，其中包括互操作系统和使能系统。这还包括考虑法律和法规、环境限制以及伦理价值观。

###### 6.4.2.2 Outcomes 预期结果

As a result of the successful performance of the stakeholder needs and requirements definition process:

利益相关方需要与需求定义过程成功执行后：

a) stakeholders of the system are identified;

a) 识别出系统的利益相关方；

b) required characteristics, context of use of capabilities, operational concepts, and other life cycle concepts are defined;

b) 所需特性、能力的使用语境、运行概念及其他生存周期概念得到界定；

c) constraints on a system are identified;

c) 识别出对系统的约束；

d) stakeholder needs are defined;

d) 利益相关方需要得到界定；

e) prioritised stakeholder needs are transformed into stakeholder requirements;

e) 已排定优先次序的利益相关方需要转换为利益相关方需求；

f) critical performance measures and quality characteristics are defined;

f) 关键性能度量与质量特性得到界定；

g) stakeholder agreement that their needs and expectations are reflected adequately in the requirements is achieved;

g) 利益相关方就其需要与期望已在需求中得到充分反映达成一致；

h) enabling systems or services needed for stakeholder needs and requirements are available;

h) 利益相关方需要与需求所需的使能系统或服务可用；

i) traceability of stakeholder requirements to stakeholders and their needs is established.

i) 利益相关方需求对利益相关方及其需要的追溯性得以建立。

###### 6.4.2.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the stakeholder needs and requirements definition process.

以下活动与任务应按照适用于利益相关方需要与需求定义过程的组织方针与程序予以实施。

a)Prepare for stakeholder needs and requirements definition. This activity consists of the following tasks.

a) 为利益相关方需要与需求定义做准备。本活动由以下任务组成。

1)Identify the stakeholders who have an interest in the solution throughout its life cycle.

1) 识别在解的整个生存周期中与解有利害关系的利益相关方。

> **NOTE 1** This includes individuals and classes of stakeholders who are users, operators, supporters, developers, producers, trainers, maintainers, disposers, acquirer and supplier organizations, parties responsible for external interfacing entities, regulatory bodies, and others who have a legitimate interest in the system solution. Where direct communication is not practicable (e.g. for consumer products and services), representatives or designated proxy stakeholders are selected.

> **注 1**：这包括作为用户、操作者、支持人员、开发者、生产者、培训者、维护者、处置者的个人和利益相关方类别，获取方组织和供应方组织，负责外部接口实体的各方，监管机构，以及对系统解具有正当利益的其他各方。在直接沟通不可行时（例如对于消费类产品和服务），选择代表或指定的代理利益相关方。

2)Define the stakeholder needs and requirements definition strategy.

2) 定义利益相关方需要与需求定义策略。

> **NOTE 2** Some stakeholders have interests that oppose the system or oppose each other. When the stakeholder interests oppose each other, but do not oppose the system, this process is intended to gain consensus among the stakeholder classes to establish a common set of acceptable requirements. The intent or desires of those that oppose the system, or detractors of the system, are addressed through the risk management process, threat analyses of the system analysis process, or the system requirements for security, adaptability, or resilience. In this case, the stakeholder needs are not satisfied, but rather addressed in a manner to help ensure system assurance and integrity if actions from the detractors are encountered.

> **注 2**：有些利益相关方的利益与系统相抵触，或彼此相抵触。当利益相关方的利益彼此抵触，但不与系统相抵触时，本过程旨在争取各利益相关方类别达成共识，以建立共同的一组可接受需求。反对系统者或系统贬损者的意图或愿望，通过风险管理过程、系统分析过程的威胁分析，或针对安全、适应性或韧性的系统需求予以处理。在这种情况下，并不满足利益相关方需要，而是以某种方式予以处理，以便在遇到贬损者的行动时有助于确保系统保证与完整性。

3)Identify and plan for the necessary enabling systems or services needed to support stakeholder needs and requirements definition.

3) 识别支持利益相关方需要与需求定义所需的必要使能系统或服务，并作出规划。

> **NOTE 3** This includes identification of requirements and interfaces for the enabling systems. Enabling systems for stakeholder needs and requirements definition include tools for facilitation and requirements management.

> **注 3**：这包括识别使能系统的需求和接口。用于利益相关方需要与需求定义的使能系统包括引导工具和需求管理工具。

4)Obtain or acquire access to the enabling systems or services to be used.

4) 获得或取得对将使用的使能系统或服务的访问权。

> **NOTE 4** The validation process is used to objectively confirm that the enabling system achieves its intended use for its enabling functions.

> **注 4**：使用确认过程客观地确认使能系统就其使能功能达成了其预期用途。

b)Develop the operational concept and other life cycle concepts. This activity consists of the following tasks.

b) 开发运行概念及其他生存周期概念。本活动由以下任务组成。

> **NOTE 5** Other life cycle concepts can include acquisition concepts, deployment concepts, support concepts, security concepts, and retirement concepts. In this activity, the preliminary life cycle concepts defined within the business or mission analysis process are further developed in the context of specific stakeholder needs, as associated scenarios and interactions are defined. More information on operational concepts can be found in ISO/IEC/IEEE 29148:2018, Clauses 5 and 6; and an annotated outline for a system operational concept is provided in ISO/IEC/IEEE 29148:2018, Annex A.

> **注 5**：其他生存周期概念能包括获取概念、部署概念、保障概念、安全概念和退役概念。在本活动中，业务或任务分析过程内定义的初步生存周期概念在具体利益相关方需要的语境中得到进一步开发，同时定义相关联的场景与交互。关于运行概念的更多信息见 ISO/IEC/IEEE 29148:2018 第 5 章和第 6 章；系统运行概念的带注释大纲在 ISO/IEC/IEEE 29148:2018 附录 A 中给出。

1)Define context of use within the concept of operations, the preliminary life cycle concepts, and the preferred solution class(es).

1) 在运行构想、初步生存周期概念以及优选的备选解类之内定义使用语境。

> **NOTE 6** Context of use is often captured using a context of use description (ISO/IEC 25063). Preliminary life cycle concepts and preferred alternative solution class(es) are developed by the business or mission analysis process.

> **注 6**：使用语境往往借助使用语境描述（ISO/IEC 25063）予以捕获。初步生存周期概念和优选的备选解类由业务或任务分析过程开发。

2)Define the context of use and a set of scenarios (or use cases) to identify all required capabilities that correspond to anticipated operational concepts and other life cycle concepts.

2) 定义使用语境以及一组场景（或用例），以识别对应于预期运行概念及其他生存周期概念的所有所需能力。

> **NOTE 7** Scenarios are used to analyse the operation of the system in its intended environment to identify additional needs or requirements that possibly have not been explicitly identified by any of the stakeholders, e.g. legal, regulatory, and social obligations. The context of use of the system is identified and analysed, including the activities that users perform to achieve system objectives, the relevant characteristics of the end users of the system (e.g. expected training, degree of fatigue), the physical environment (e.g. available light, temperature), and any equipment to be used (e.g. protective or communication equipment).

> **注 7**：场景用于分析系统在其预期环境中的运行，以识别可能未被任何利益相关方明确识别的附加需要或需求，例如法律义务、法规义务和社会义务。识别并分析系统的使用语境，包括用户为实现系统目标而执行的活动、系统最终用户的相关特性（例如预期培训、疲劳程度）、物理环境（例如可用光照、温度）以及将使用的任何设备（例如防护设备或通信设备）。

> **NOTE 8** These scenarios often motivate updates to the operational or other life cycle concepts. Abuse and failure scenarios highlight the need for additional functional requirements (or more specific derived requirements) to mitigate risks that are identified in the abuse or failure scenarios.

> **注 8**：这些场景往往促使更新运行概念或其他生存周期概念。滥用场景和故障场景突显了需要附加的功能需求（或更具体的派生需求），以缓解滥用场景或故障场景中所识别的风险。

3)Characterize the operational environment and the intended users.

3) 表征运行环境和预期用户。

4)Identify interactions between users and the system and the factors affecting the interactions.

4) 识别用户与系统之间的交互以及影响这些交互的因素。

> **NOTE 9** Usability requirements take into account human capabilities and skills limitations. Where possible, applicable standards, e.g. ISO 9241-210, and accepted professional practices are used to define:

> **注 9**：易用性要求考虑人的能力与技能限制。在可能的情况下，使用适用标准（例如 ISO 9241-210）和公认的专业实践界定：

a) physical, mental, and learned capabilities;

a) 身体能力、心智能力和习得能力；

b) workplace, environment, and facilities, including other equipment in the context of use;

b) 工作场所、环境和设施，包括使用语境中的其他设备；

c) normal, unusual, and emergency conditions;

c) 正常状况、异常状况和应急状况；

d) operator and user recruitment, training, and culture.

d) 操作者与用户的招聘、培训和文化。

> **NOTE 10** If usability is important, usability requirements are planned, specified, and implemented through the life cycle processes. Further information on human-system issues can be found in ISO TS 18152 and information on usability in ISO/IEC TR 25060.

> **注 10**：若易用性重要，则易用性要求贯穿各生存周期过程予以规划、规定和实施。关于人-系统问题的进一步信息可参见 ISO TS 18152，关于易用性的信息可参见 ISO/IEC TR 25060。

5)Identify all interface boundaries across which the SoI interacts with external systems.

5) 识别 SoI 与外部系统交互所跨越的全部接口边界。

> **NOTE 11** Identifying the interactions between the SoI and the interfacing, enabling, and interoperating systems is helpful for identifying interface boundaries (also see 5.2.3).

> **注 11**：识别 SoI 与接口系统、使能系统和互操作系统之间的交互，有助于识别接口边界（另见 5.2.3）。

6)Identify the constraints on a system solution.

6) 识别对系统解的约束。

> **NOTE 12** These result from:

> **注 12**：这些约束源自：

- instances or areas of stakeholder-defined solution;

- 由利益相关方定义的解的实例或领域；

- implementation decisions made elsewhere in the system structure;

- 在系统结构中其他地方作出的实现决策；

- required use of defined enabling, legacy, or interfacing systems or system elements, resources and staff; or

- 要求使用已定义的使能系统、遗留系统或接口系统，或者系统元素、资源与人员；或

- stakeholder defined affordability objectives. Include those that are unavoidable consequences of existing agreements, management decisions, and technical decisions.

- 利益相关方所定义的可负担性目标。其中包括现有协议、管理决策和技术决策所不可避免导致的约束。

c)Define stakeholder needs. This activity consists of the following tasks.

c) 定义利益相关方需要。本活动由以下任务组成。

1)Identify stakeholder needs within the constraints imposed by the life cycle concepts.

1) 在生存周期概念所施加的约束范围内识别利益相关方需要。

> **NOTE 13** Identification of stakeholder needs includes elicitation of needs, wants, desires, expectations, and perceived constraints of identified stakeholders; identification of implicit stakeholder needs based on domain knowledge and context understanding; and documented gaps from previous activities. Needs often include measures of effectiveness (further information can be found in ISO/IEC/IEEE 24748-2) and identification of critical operational issues. Functional analysis is often used to aid the elicitation of needs. Quality characteristics of the quality model in ISO/IEC 25010 and quality model application to requirements analysis in ISO/IEC 25030 are also useful to elicit and identify quality characteristics requirements, which are often implicit stakeholder needs. Additionally, the needs can also include considerations for the SoI to interact with other systems as it participates in a system of systems (further information can be found in ISO/IEC/IEEE 21839).

> **注 13**：识别利益相关方需要包括：引出已识别利益相关方的需要、愿望、期望、预期以及所感知的约束；基于领域知识与语境理解识别隐含的利益相关方需要；以及记录此前活动留下的差距。需要往往包括有效性度量（进一步信息可参见 ISO/IEC/IEEE 24748-2）以及对关键运行问题的识别。功能分析常用于辅助引出需要。ISO/IEC 25010 中质量模型的质量特性以及 ISO/IEC 25030 中质量模型在需求分析上的应用，也有助于引出和识别质量特性要求，而这些要求往往是隐含的利益相关方需要。此外，需要还可包括对 SoI 参与系统的系统时与其他系统交互的考虑（进一步信息可参见 ISO/IEC/IEEE 21839）。

> **NOTE 14** Based on analysis of the impact of adverse or hostile stakeholders, constraints are derived that can mitigate risk.

> **注 14**：基于对不利或敌对利益相关方影响的分析，导出能减轻风险的约束。

2)Prioritise and down-select needs.

2) 对需要排定优先次序并进行筛选。

> **NOTE 15** The decision management process is typically used to support prioritization. The system analysis process is used to analyse needs for feasibility or other factors.

> **注 15**：决策管理过程通常用于支持优先排序。使用系统分析过程来分析需要的可行性或其他因素。

3)Record the stakeholder needs and rationale.

3) 记录利益相关方需要及其理由。

> **NOTE 16** Needs concentrate on system purpose and behaviour, and are described in the context of the operational environment and conditions. It is useful to trace needs to their sources and rationale.

> **注 16**：需要聚焦于系统的目的与行为，并在运行环境与运行条件的语境中加以描述。将需要追溯至其来源与理由是有用的。

> **NOTE 17** It is good practice to review needs for format and quality.

> **注 17**：评审需要的格式与质量是一种良好实践。

d)Transform stakeholder needs into stakeholder requirements. This activity consists of the following tasks.

d) 将利益相关方需要转换为利益相关方需求。本活动由以下任务组成。

1)Identify the stakeholder requirements and functions that relate to critical quality characteristics, such as assurance, safety, security, environment, or health.

1) 识别与关键质量特性（例如保证、安全性、安全、环境或健康）相关的利益相关方需求与功能。

> **NOTE 18** ISO/IEC/IEEE 15026 series provides additional information on system and software assurance.

> **注 18**：ISO/IEC/IEEE 15026 系列就系统保证与软件保证提供了补充信息。

> **NOTE 19** Identifying safety risks facilitates the identification of safety requirements and functions. Safety risks include those associated with methods of operations and support, health and safety, threats to property, and environmental influences. Applicable standards, e.g. the IEC 61508 series, and accepted professional practices can be used.

> **注 19**：识别安全性风险有助于识别安全性要求与功能。安全性风险包括与运行和支持方法、健康与安全性、财产威胁以及环境影响有关的风险。可使用适用的标准（例如 IEC 61508 系列）以及公认的专业实践。

> **NOTE 20** Identifying security risks facilitates the identification of security requirements and functions. Safety risks include applicable areas of system security (e.g. physical, procedural, communications, computers); access and damage to protected personnel, properties, and information; compromise of sensitive information; and denial of approved access to property and information. Security functions such as mitigation and containment are typical considerations.

> **注 20**：识别安全风险有助于识别安全要求与功能。安全性风险包括系统安全的适用领域（例如物理、规程、通信、计算机）；对受保护人员、财产和信息的访问与损害；敏感信息的泄露；以及对财产和信息的已批准访问的拒绝。减轻与遏制等安全功能是典型的考虑事项。

> **NOTE 21** ISO/IEC 25030 provides further information regarding quality characteristics from a quality in use perspective.

> **注 21**：ISO/IEC 25030 从使用质量的视角就质量特性提供了进一步信息。

2)Define stakeholder requirements, consistent with life cycle concepts, scenarios, interactions, constraints, critical quality characteristics, and SoS considerations.

2) 定义与生存周期概念、场景、交互、约束、关键质量特性及 SoS 考虑事项一致的利益相关方需求。

> **NOTE 22** More information on stakeholder requirements can be found in ISO/IEC/IEEE 29148:2018, Clauses 5 and 6; and ISO/IEC/IEEE 29148:2018, Clauses 8 and 9 provides a description of and an annotated outline for a stakeholder requirements specification.

> **注 22**：关于利益相关方需求的更多信息可参见 ISO/IEC/IEEE 29148:2018 第 5 章和第 6 章；ISO/IEC/IEEE 29148:2018 第 8 章和第 9 章给出了利益相关方需求规格的说明和带注释大纲。

> **NOTE 23** The stakeholder requirements are reviewed at key decision times in the life cycle to help ensure that account is taken of any changes of need. Including supporting rationale for stakeholder requirements aids in future analysis efforts.

> **注 23**：在生存周期的关键决策时点对利益相关方需求进行评审，以帮助确保顾及需要的任何变化。为利益相关方需求提供支持性理由，有助于今后的分析工作。

> **NOTE 24** The stakeholder requirements are recorded in a form suitable for requirements management through the life cycle. These records establish the stakeholder requirements baseline, and retain changes of need and their origin throughout the system life cycle. These records are the basis for traceability to decisions made by the business or mission analysis process as well as stakeholder needs, system requirements, and subsequent system elements.

> **注 24**：利益相关方需求以适合在整个生存周期内进行需求管理的形式予以记录。这些记录建立利益相关方需求基线，并在整个系统生存周期内保留需要的变化及其来源。这些记录是向业务或任务分析过程所作决策以及利益相关方需要、系统需求和后续系统元素进行追溯的基础。

> **NOTE 25** Information on SoS considerations for an SoI is provided in 5.4.4 and ISO/IEC/IEEE 21839.

> **注 25**：关于 SoI 的 SoS 考虑事项的信息见 5.4.4 和 ISO/IEC/IEEE 21839。

e)Analyse stakeholder needs and requirements. This activity consists of the following tasks.

e) 分析利益相关方需要与需求。本活动由以下任务组成。

1)Analyse the complete set of stakeholder requirements.

1) 分析完整的利益相关方需求集。

> **NOTE 26** Stakeholder requirements are analysed for characteristics of individual requirements, as well as characteristics of the set of requirements. Potential analysis characteristics include that the requirements are necessary, implementation independent, unambiguous, complete, singular, achievable, verifiable, and conforming. For a set of requirements, the characteristics are complete, consistent, feasible (or affordable), and bounded. ISO/IEC/IEEE 29148 provides additional information on characteristics of requirements.

> **注 26**：对利益相关方需求，既分析单条需求的特性，也分析需求集的特性。潜在的分析特性包括：需求是必要的、实现独立的、无歧义的、完整的、单一的、可实现的、可验证的和符合的。对于需求集，其特性是完整的、一致的、可行的（或可负担的）和有界的。ISO/IEC/IEEE 29148 对需求特性提供了补充信息。

> **NOTE 27** The system analysis process is used to assess feasibility and affordability. The verification and validation processes are used in the review of stakeholder requirements.

> **注 27**：使用系统分析过程评定可行性与可负担性。在评审利益相关方需求时使用验证过程与确认过程。

2)Define critical performance measures and quality characteristics that enable the assessment of technical achievement.

2) 定义能够对技术成果进行评定的关键性能度量与质量特性。

> **NOTE 28** This includes defining technical and quality measures and critical performance parameters associated with each effectiveness measure identified in the stakeholder requirements. The critical performance measures (e.g. measures of effectiveness and measures of suitability) are defined, analysed, and reviewed to help ensure stakeholder requirements are met and to help ensure identification of project cost, schedule, or performance risk associated with any non-compliance. ISO/IEC/IEEE 15939 provides a process to identify, define and use appropriate measures. INCOSE-TP-2003-020-01 provides information on the selection, definition, and implementation of critical performance measures. The ISO/IEC 25000 family of standards provides relevant quality measures.

> **注 28**：这包括定义与利益相关方需求中识别的每项有效性度量相关的技术度量、质量度量以及关键性能参数。定义、分析并评审关键性能度量（例如有效性度量与适用性度量），以帮助确保满足利益相关方需求，并帮助确保识别与任何不符合相关的项目成本、进度或性能风险。ISO/IEC/IEEE 15939 给出识别、定义和使用适当度量的过程。INCOSE-TP-2003-020-01 提供关于关键性能度量的选择、定义与实施的信息。ISO/IEC 25000 族标准提供相关的质量度量。

3)Feed back the analysed requirements to applicable stakeholders to validate that their needs and expectations have been adequately captured and expressed.

3) 将分析后的需求反馈给适用的利益相关方，以确认其需要与期望已得到充分捕获和表达。

4)Resolve stakeholder requirements issues.

4) 解决利益相关方需求的问题。

> **NOTE 29** This includes requirements that violate the characteristics for individual requirements or the set of requirements.

> **注 29**：这包括违反单条需求特性或需求集特性的需求。

f)Manage the stakeholder needs and requirements definition. This activity consists of the following tasks.

f) 管理利益相关方需要与需求定义。本活动由以下任务组成。

1)Obtain explicit agreement on the stakeholder requirements.

1) 就利益相关方需求取得明确一致。

> **NOTE 30** This includes confirming that stakeholder requirements meet stakeholder needs, are expressed correctly, comprehensible to originators, and that the resolution of conflict in the requirements has not corrupted or compromised stakeholder intentions.

> **注 30**：这包括确认利益相关方需求满足利益相关方需要、表达正确、对提出者可理解，并且需求中冲突的解决未曲解或损害利益相关方的意图。

2)Record key stakeholder requirements decisions and the rationale.

2) 记录关键的利益相关方需求决策及其理由。

> **NOTE 31** Rationale includes information about major alternatives and enablers.

> **注 31**：理由包括有关主要备选方案与使能因素的信息。

3)Maintain traceability of stakeholder needs and requirements.

3) 保持利益相关方需要与需求的追溯性。

> **NOTE 32** Through the life cycle, bi-directional traceability is maintained between the stakeholder needs and requirements and the stakeholders and sources, organizational strategy, and business or mission problems and opportunities. Additional traceability to systems making up the system solution facilitates the transition to the system requirements definition process. This is often facilitated by an appropriate data repository.

> **注 32**：在整个生存周期内，在利益相关方需要与需求，与利益相关方及其来源、组织战略以及业务或任务问题与机会之间保持双向追溯性。与构成系统解的各系统之间的附加追溯性有助于向系统需求定义过程过渡。这通常借助适当的数据存储库来实现。

4)Provide key artefacts that have been selected for baselines.

4) 提供已选定用于基线的关键人工制品。

> **NOTE 33** The configuration management process is used to establish and maintain configuration items and baselines. The stakeholder needs and requirements definition process identifies candidates for the baseline, and then provides the artefacts to configuration management. For the stakeholder needs and requirements definition process, the stakeholder needs, stakeholder requirements, and operational concept are typical artefacts that are baselined.

> **注 33**：使用配置管理过程建立并维护配置项与基线。利益相关方需要与需求定义过程识别基线的候选对象，随后将人工制品提供给配置管理。就利益相关方需要与需求定义过程而言，利益相关方需要、利益相关方需求和运行概念是通常被纳入基线的人工制品。

##### 6.4.3 System requirements definition process 系统需求定义过程

###### 6.4.3.1 Purpose 目的

The purpose of the system requirements definition process is to transform the stakeholder, user-oriented view of desired capabilities into a technical view of a solution that meets the operational needs of the user.

系统需求定义过程的目的是将利益相关方以用户为导向的所需能力视图，转换为满足用户运行需要的解的技术视图。

This process creates a set of measurable system requirements that specify, from the supplier’s perspective, what characteristics, attributes, and functional and performance requirements the system is to possess, to satisfy stakeholder requirements. As far as constraints permit, the requirements should not imply any specific implementation.

本过程创建一组可测量的系统需求，从供应方的角度规定系统为满足利益相关方需求而应具备的特性、属性以及功能要求和性能要求。在约束允许的范围内，这些需求宜不暗示任何特定的实现。

###### 6.4.3.2 Outcomes 预期结果

As a result of the successful performance of the system requirements definition process:

系统需求定义过程成功执行后：

a) the system description, including system external interfaces, functions, and boundaries, for a system solution is defined;

a) 系统解的系统描述，包括系统外部接口、功能与边界，得以定义；

b) system requirements (functional, performance, process, quality, and interface) and design constraints are defined;

b) 系统需求（功能、性能、过程、质量与接口）以及设计约束得以定义；

c) critical performance measures are defined;

c) 关键性能度量得以定义；

d) the system requirements are analysed;

d) 系统需求得到分析；

e) enabling systems or services needed for system requirements definition are available;

e) 系统需求定义所需的使能系统或服务可用；

f) traceability of system requirements to stakeholder requirements is developed.

f) 建立了系统需求对利益相关方需求的追溯性。

###### 6.4.3.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the system requirements definition process.

以下活动与任务应按照适用于系统需求定义过程的组织方针与程序予以实施。

a)Prepare for system requirements definition. This activity consists of the following tasks.

a) 准备进行系统需求定义。本活动由以下任务组成。

1)Define the functional boundary of the system in terms of the behaviour and properties to be provided.

1) 从将要提供的行为与属性的角度定义系统的功能边界。

> **NOTE 1** The functional boundary definition is partly based on the context of use and operational scenarios defined in the frame of the stakeholder needs and requirements definition process. This includes the system’s stimuli and its responses to user and environment behaviour, and an analysis and description of the required interactions between the system and its environment in terms of interface properties and constraints, such as mechanical, electrical, mass, thermal, data, and procedural flows. This establishes the expected system behaviour, expressed in quantitative terms, at its boundary.

> **注 1**：功能边界的定义部分基于利益相关方需要与需求定义过程中所定义的使用情境与运行场景。这包括系统的刺激因素及其对用户与环境行为的响应，以及从接口属性与约束（例如机械流、电气流、质量流、热流、数据流和规程性的流）的角度，对系统与其环境之间所需交互的分析与描述。这确立了系统在其边界处用定量术语表述的预期行为。

> **NOTE 2** This includes an evaluation of alternative boundaries and a selection among the alternatives.

> **注 2**：这包括对备选边界的评定以及在备选方案之间作出选择。

2)Define the system requirements definition strategy.

2) 定义系统需求定义策略。

> **NOTE 3** This includes the approach to be used to identify and define the system requirements, and manage the requirements through the system’s life cycle.

> **注 3**：这包括用于识别和定义系统需求并在系统生存周期内管理需求的方法。

3)Identify and plan for the necessary enabling systems or services needed to support system requirements definition.

3) 识别并规划支持系统需求定义所需的必要使能系统或服务。

> **NOTE 4** This includes identification of requirements and interfaces for the enabling systems. Enabling systems for system requirements definition include tools for facilitation and requirements management.

> **注 4**：这包括识别使能系统的需求与接口。系统需求定义的使能系统包括用于引导与需求管理的工具。

4)Obtain or acquire access to the enabling systems or services to be used.

4) 获取或取得将使用的使能系统或服务的访问权。

> **NOTE 5** The validation process is used to objectively confirm that the enabling system achieves its intended use for its enabling functions.

> **注 5**：使用确认过程客观地确认使能系统就其使能功能达成了其预期用途。

b)Define system requirements. This activity consists of the following tasks.

b) 定义系统需求。本活动由以下任务组成。

1)Define each function that the system is required to perform.

1) 定义要求系统执行的每项功能。

> **NOTE 6** This includes how well the system, including its operators, is required to perform each function, the conditions under which the system is to be capable of performing the function, the conditions under which the system is to commence performing that function and the conditions under which the system is to cease performing that function. In some cases, functions are derived from analysis of critical quality characteristics (e.g. system diagnosing function or highly frequent data backup function for reliability). Functions can interact adversely.

> **注 6**：这包括系统（含其操作者）执行每项功能所要求的程度、系统能够执行该功能的条件、系统开始执行该功能的条件以及系统停止执行该功能的条件。有些情况下，功能由对关键质量特性的分析导出（例如为提高可靠性而设的系统诊断功能或高频数据备份功能）。功能可能产生不利的相互作用。

> **NOTE 7** Conditions for the performance of functions can incorporate reference to required states and modes of operation of the system. System requirements depend heavily on abstract representations of proposed system characteristics and sometimes employ multiple modelling techniques and perspectives to give a sufficiently complete description of the desired system requirements.

> **注 7**：功能执行的条件可包含对系统所需状态与运行模式的引用。系统需求在很大程度上取决于对所提议系统特性的抽象表示，有时采用多种建模技术和视角，以对所需的系统需求给出足够完整的描述。

> **NOTE 8** Enabling functions that are required to support the SoI in achieving its functionality are also identified and defined concurrently with the function of the SoI. This is necessary to help ensure that the enabling functions are identified and accounted for.

> **注 8**：为支持 SoI 实现其功能所需的使能功能，也与 SoI 的功能同时识别和定义。这有助于确保使能功能被识别并予以考虑。

> **NOTE 9** This includes an evaluation of alternative functions and sets of functions, and a selection among alternatives.

> **注 9**：这包括对备选功能与功能集的评定，以及在备选方案之间作出选择。

2)Define necessary implementation constraints.

2) 定义必要的实现约束。

> **NOTE 10** This includes the implementation decisions that are allocated from architecture definition at higher levels in the structure of the system and are introduced by stakeholder requirements or are solution limitations.

> **注 10**：这包括在系统结构中由较高层级的架构定义分配而来的实现决策，以及由利益相关方需求引入的实现决策或解的限制。

3)Identify system requirements that relate to risks, criticality of the system, or critical quality characteristics.

3) 识别与风险、系统关键性或关键质量特性相关的系统需求。

> **NOTE 11** Critical quality characteristics commonly include those related to health, safety, security, assurance, reliability, resilience, availability, and supportability. Which quality characteristics are important is dependent on the project and domain. This includes analysis and definition of:

> **注 11**：关键质量特性通常包括与健康、安全性、安全、保证、可靠性、韧性、可用性和保障性有关的特性。哪些质量特性重要取决于项目和领域。这包括对下列各项的分析与定义：

a) safety considerations, including those relating to methods of utilization and support, environmental influences and personnel injury (see the IEC 61508 series for functional safety and ISO 14001 for environmental safety);

a) 安全性考虑事项，包括与使用和支持方法、环境影响和人员伤害有关的考虑事项（功能安全性见 IEC 61508 系列，环境安全性见 ISO 14001）；

b) security considerations, including those related to compromise and protection of sensitive information, data and material (see ISO/IEC/IEEE 15026-4 for system and software assurance and the ISO/IEC 27036 series for information security requirements for the outsourcing of products and services);

b) 安全考虑事项，包括与敏感信息、数据和材料的泄露与保护有关的考虑事项（系统保证与软件保证见 ISO/IEC/IEEE 15026-4，产品和服务外包的安全要求见 ISO/IEC 27036 系列）；

c) external system quality factors (see ISO/IEC 25030);

c) 外部系统质量因素（见 ISO/IEC 25030）；

d) human interaction and human-factors engineering (ergonomics) considerations (see ISO 9241-210 for usability).

d) 人的交互与人因工程（工效学）考虑事项（易用性见 ISO 9241-210）。

4)Define system requirements and rationale.

4) 定义系统需求及其理由。

> **NOTE 12** This includes defining system requirements consistent with stakeholder requirements, functional boundaries, functions, constraints, cost targets, identified interfaces, critical quality characteristics, and SoS considerations. Conduct of this task benefits from iterative and recursive steps in parallel with other life cycle processes through the system structure. More information on system requirements can be found in ISO/IEC/IEEE 29148:2018, Clauses 5 and 6; and a description of and an annotated outline for a system requirements specification in ISO/IEC/IEEE 29148:2018, Clauses 8 and 9.

> **注 12**：这包括定义与利益相关方需求、功能边界、功能、约束、成本目标、已识别的接口、关键质量特性和 SoS 考虑事项相一致的系统需求。执行本任务得益于在系统结构中与其他生存周期过程并行开展的迭代与递归步骤。关于系统需求的更多信息可参见 ISO/IEC/IEEE 29148:2018 第 5 章和第 6 章；ISO/IEC/IEEE 29148:2018 第 8 章和第 9 章给出了系统需求规格的说明和带注释大纲。

> **NOTE 13** The system requirements are recorded in a form suitable for requirements management through the life cycle. These records establish the system requirements baseline and include the associated rationale, decisions, and assumptions. They are the basis for traceability to information items and subsequent system elements.

> **注 13**：系统需求以适合在整个生存周期内进行需求管理的形式予以记录。这些记录建立系统需求基线，并包括相关理由、决策和假设。它们是向信息部件及后续系统元素进行追溯的基础。

> **NOTE 14** The system analysis process is used to determine appropriate values for requirement parameters, considering the estimated cost, schedule, and technical performance of the system. The validation process is used to determine if the requirements address the stakeholders’ needs. The verification process determines the quality of the requirements with respect to the attributes and characteristics of good requirements.

> **注 14**：使用系统分析过程确定需求参数的适当取值，同时考虑系统的估计成本、进度和技术性能。使用确认过程确定需求是否应对了利益相关方的需要。验证过程则就良好需求的属性与特性确定需求的质量。

c)Analyse system requirements. This activity consists of the following tasks.

c) 分析系统需求。本活动由以下任务组成。

1)Analyse the complete set of system requirements.

1) 分析完整的系统需求集。

> **NOTE 15** System requirements are analysed for characteristics of individual requirements, as well as characteristics of the set of requirements. Potential analysis characteristics include that the requirements are necessary, implementation free, unambiguous, consistent, complete, singular, feasible, traceable, verifiable, affordable, and bounded. ISO/IEC/IEEE 29148 provides additional information on characteristics of requirements. Deficiencies, conflicts and weaknesses are identified and resolved within the complete set of system requirements.

> **注 15**：对系统需求，既分析单条需求的特性，也分析需求集的特性。潜在的分析特性包括：需求是必要的、实现无关的、无歧义的、一致的、完整的、单一的、可行的、可追溯的、可验证的、可负担的和有界的。ISO/IEC/IEEE 29148 对需求特性提供了补充信息。在完整的系统需求集内识别并解决缺陷、冲突与薄弱之处。

> **NOTE 16** The system analysis process is used to assess feasibility, affordability, and other requirements characteristics.

> **注 16**：使用系统分析过程评定可行性、可负担性以及其他需求特性。

2)Define critical performance measures that enable the assessment of technical achievement.

2) 定义能够对技术成果进行评定的关键性能度量。

> **NOTE 17** This includes defining technical and quality measures and critical performance parameters associated with each effectiveness measure identified in the system requirements. The critical performance measures (e.g. measures of performance and technical performance measures) are analysed and reviewed to help ensure system requirements are met and to help ensure identification of project cost, schedule, or performance risk associated with any non-compliance. ISO/IEC/IEEE 15939 provides a process to identify, define, and use appropriate measures. INCOSE-TP-2003-020-01 provides information on the selection, definition, and implementation of critical performance measures. The ISO/IEC 25000 family of standards provides relevant quality measures.

> **注 17**：这包括定义与系统需求中识别的每项有效性度量相关的技术度量、质量度量以及关键性能参数。分析并评审关键性能度量（例如性能度量与技术性能度量），以帮助确保满足系统需求，并帮助确保识别与任何不符合相关的项目成本、进度或性能风险。ISO/IEC/IEEE 15939 给出识别、定义和使用适当度量的过程。INCOSE-TP-2003-020-01 提供关于关键性能度量的选择、定义与实施的信息。ISO/IEC 25000 族标准提供相关的质量度量。

3)Feed back the analysed requirements to applicable stakeholders for review.

3) 将分析后的需求反馈给适用的利益相关方进行评审。

> **NOTE 18** Feedback helps ensure that the specified system requirements have been adequately captured and expressed. Confirmation is made that they are a necessary and sufficient response to stakeholder requirements and a necessary and sufficient input to other processes, in particular architecture and design. This is one application of the validation process applied for the specific requirements.

> **注 18**：反馈有助于确保所规定的系统需求已得到充分捕获和表达。确认这些需求是对利益相关方需求的必要且充分的响应，并且是其他过程（尤其是架构过程与设计过程）的必要且充分的输入。这是将确认过程应用于特定需求的一种情形。

4)Resolve system requirements issues.

4) 解决系统需求的问题。

> **NOTE 19** This includes requirements that violate the characteristics for individual requirements or the set of requirements.

> **注 19**：这包括违反单条需求特性或需求集特性的需求。

d)Manage system requirements. This activity consists of the following tasks.

d) 管理系统需求。本活动由以下任务组成。

> **NOTE 20** Maintaining system requirements includes defining, recording, and controlling the baseline, generally under formal configuration management, along with managing any changes resulting from the application of other life cycle processes such as architecture or design.

> **注 20**：维护系统需求包括定义、记录和控制基线（通常置于正式配置管理之下），以及管理由架构或设计等其他生存周期过程的应用所引起的任何更改。

1)Obtain explicit agreement on the system requirements.

1) 就系统需求取得明确一致。

> **NOTE 21** This includes confirming that system requirements meet stakeholder requirements, are expressed correctly, comprehensible to originators, and that the resolution of conflict in the requirements has not corrupted or compromised stakeholder intentions.

> **注 21**：这包括确认系统需求满足利益相关方需求、表达正确、对提出者可理解，并且需求中冲突的解决未曲解或损害利益相关方的意图。

2)Record key system requirements decisions and the rationale.

2) 记录关键的系统需求决策及其理由。

> **NOTE 22** Rationale includes information about major alternatives and enablers.

> **注 22**：理由包括有关主要备选方案与使能因素的信息。

3)Maintain traceability of the system requirements.

3) 保持系统需求的追溯性。

> **NOTE 23** Through the life cycle, bi-directional traceability is maintained between the system requirements and the stakeholder needs and requirements, architecture elements, interface definitions, analysis results, verification methods or techniques, and allocated, decomposed, and derived requirements. This helps ensure that all achievable stakeholder requirements are met by one or more system requirements, and all system requirements meet or contribute to meeting at least one stakeholder requirement. This is often facilitated by an appropriate data repository.

> **注 23**：在整个生存周期内，在系统需求与利益相关方需要和需求、架构元素、接口定义、分析结果、验证方法或技术以及已分配、已分解和派生的需求之间保持双向追溯性。这有助于确保所有可实现的利益相关方需求都由一项或多项系统需求予以满足，并且所有系统需求都满足或有助于满足至少一项利益相关方需求。这通常借助适当的数据存储库来实现。

4)Provide key artefacts that have been selected for baselines.

4) 提供已选定用于基线的关键人工制品。

> **NOTE 24** The configuration management process is used to establish and maintain configuration items and baselines. The system requirements definition process identifies candidates for the baseline and then provides the artefacts to configuration management. For the system requirements definition process, the system requirements are typical artefacts that are baselined.

> **注 24**：使用配置管理过程建立并维护配置项与基线。系统需求定义过程识别基线的候选对象，随后将人工制品提供给配置管理。就系统需求定义过程而言，系统需求是通常被纳入基线的人工制品。

##### 6.4.4 System architecture definition process 系统架构定义过程

###### 6.4.4.1 Purpose 目的

The purpose of the system architecture definition process is to generate system architecture alternatives, select one or more alternative(s) that address stakeholder concerns and system requirements, and express this in consistent views and models.

系统架构定义过程的目的是生成系统架构备选方案，选择一个或多个应对利益相关方关注点和系统需求的备选方案，并在一致的视图与模型中表达该架构。

The system architecture definition activities define a solution based on principles, concepts, and properties logically related to and consistent with each other. The solution architecture has features, properties, and characteristics which satisfy, as far as possible, the problem or opportunity expressed by a set of system requirements (traceable to mission, business and stakeholder requirements) and life cycle concepts (e.g. operational, support).

系统架构定义活动基于彼此在逻辑上相关且一致的原则、概念和属性来定义解。解架构具有若干特征、属性与特性，它们尽可能满足由一组系统需求（可追溯至任务、业务和利益相关方需求）以及生存周期概念（例如运行概念、保障概念）所表达的问题或机会。

This process transforms related architectures (e.g. strategic, enterprise, reference, and SoS architectures), organizational and project policies and directives, life cycle concepts and constraints, stakeholder concerns and requirements, and system requirements and constraints into the fundamental concepts and properties of the system and the governing principles for evolution of the system and its related life cycle processes.

本过程将相关架构（例如战略架构、企业架构、参考架构和 SoS 架构）、组织与项目的方针和指令、生存周期概念与约束、利益相关方关注点与需求，以及系统需求与约束，转化为基本的系统的概念与属性，以及系统及其相关生存周期过程演进的管控原则。

> **NOTE** When the enterprise or SoS is the SoI, then the enterprise architecture or SoS architecture is the system architecture.

> **注**：当企业或 SoS 为 SoI 时，企业架构或 SoS 架构即为系统架构。

###### 6.4.4.2 Outcomes 预期结果

As a result of the successful performance of the system architecture definition process:

系统架构定义过程成功执行后：

a) problem space is refined with respect to key stakeholder concerns, context, and perspectives;

a) 针对关键利益相关方关注点、语境与角度，对问题空间进行了细化；

b) alignment of the architecture with applicable policies, directives, objectives, and constraints is achieved;

b) 架构与适用的方针、指令、目标和约束之间的对齐得以实现；

c) concepts, properties, characteristics, behaviours, functions, or constraints that are significant to architecture decisions of the system are allocated to architectural entities;

c) 对系统架构决策具有重要意义的理念、属性、特性、行为、功能或约束被分配到架构实体；

d) identified stakeholder concerns are addressed by the system architecture;

d) 已识别的利益相关方关注点由系统架构予以应对；

e) traceability of system architecture elements to key architecturally-relevant stakeholder and system requirements is established;

e) 系统架构元素对关键的、与架构相关的利益相关方需求和系统需求的追溯性得以建立；

f) architecture views and models of the system are developed;

f) 系统的架构视图与模型得以开发；

g) system elements including their interfaces with each other are defined;

g) 系统元素及其彼此之间的接口得到定义；

h) enabling systems or services needed for system architecture definition are available.

h) 系统架构定义所需的使能系统或服务可用。

###### 6.4.4.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the system architecture definition process.

以下活动与任务应按照适用于系统架构定义过程的组织方针与程序予以实施。

> **NOTE 1** Activities b) through d) of the system architecture definition process correspond to the three core processes in ISO/IEC/IEEE 42020. The tasks below each of these activities correspond to the activities in each of those 42020 architecture processes. The activities and tasks are edited to reflect the scope of the system only. ISO/IEC/IEEE 42020 provides additional detail on the following activities and tasks.

> **注 1**：系统架构定义过程的活动 b) 至 d) 对应于 ISO/IEC/IEEE 42020 中的三个核心过程。以下每项活动之下的任务对应于各 42020 架构过程中的活动。这些活动与任务经过编辑，以仅反映系统的范围。ISO/IEC/IEEE 42020 对以下活动与任务提供了更多细节。

a)Prepare for system architecture definition. This activity consists of the following tasks.

a) 准备进行系统架构定义。本活动由以下任务组成。

1)Identify key milestones and decisions to be informed by the system architecture effort.

1) 识别系统架构工作需为其提供输入的关键里程碑与决策。

2)Define the strategy for system architecture definition.

2) 定义系统架构定义的策略。

3)Prepare for and plan the support to architecture governance and architecture management efforts of the organization.

3) 为支持组织的架构治理与架构管理工作做好准备并作出规划。

4)Identify and plan for the necessary enabling systems or services needed to support system architecture definition efforts.

4) 识别支持系统架构定义工作所需的必要使能系统或服务，并作出规划。

5)Obtain or acquire access to the enabling systems or services to be used in the system architecture definition efforts.

5) 获取或取得对系统架构定义工作中将使用的使能系统或服务的访问权。

> **NOTE 2** The validation process is used to objectively confirm that the enabling system achieves its intended use for its enabling functions.

> **注 2**：使用确认过程客观地确认使能系统就其使能功能达成了其预期用途。

b)Conceptualise the system architecture. This activity consists of the following tasks.

b) 对系统架构进行概念化。本活动由以下任务组成。

1)Characterize the problem space.

1) 表征问题空间。

> **NOTE 3** This is done in conjunction with the business or mission analysis process, which identifies and defines the problem (or opportunity) space. It includes any key considerations, such as SoS interactions, required quality characteristics.

> **注 3**：本任务与业务或任务分析过程协同完成，该过程识别并定义问题（或机会）空间。它包括任何关键考虑事项，例如 SoS 交互、所需的质量特性。

2)Establish architecture objectives and critical success criteria.

2) 建立架构目标与关键成功准则。

3)Synthesize potential solution(s) in the solution space.

3) 在解空间中综合潜在解。

> **NOTE 4** The business or mission analysis process establishes preferred alternative solutions classes for the solution space. Potential solutions within the preferred alternative solution classes are identified and analysed.

> **注 4**：业务或任务分析过程为解空间建立优选的备选解类。在优选的备选解类内识别并分析潜在解。

4)Characterize solutions and the trade space.

4) 表征解与权衡空间。

5)Formulate candidate architecture(s).

5) 构建候选架构。

6)Capture architecture concepts and properties.

6) 捕获架构概念与属性。

7)Relate the architecture to other architectures and to relevant affected entities to help ensure consistency.

7) 将架构与其他架构以及相关受影响的实体关联起来，以帮助确保一致性。

8)Coordinate use of architecture by intended users.

8) 协调预期用户对架构的使用。

c)Evaluate the system architecture. This activity consists of the following tasks.

c) 评估系统架构。本活动由以下任务组成。

> **NOTE 5** This activity is performed in conjunction with the system analysis and decision management processes.

> **注 5**：本活动与系统分析过程和决策管理过程协同执行。

1)Determine evaluation objectives and criteria.

1) 确定评估目标与准则。

2)Determine evaluation methods and integrate with evaluation objectives and criteria.

2) 确定评估方法，并与评估目标与准则相整合。

> **NOTE 6** The measurement process is used to establish measures and associated measurement techniques, methods and tools to support the evaluation.

> **注 6**：使用测量过程建立测量以及相关的测量技术、方法和工具，以支持评估。

3)Collect and review evaluation-related information.

3) 收集并评审与评估有关的信息。

4)Analyse architecture concepts and properties and assess the value of the architecture.

4) 分析架构概念与属性，并评定架构的价值。

5)Combine the analyses and assessments into an overall evaluation to select a preferred system architecture solution.

5) 将各项分析与评定综合为总体评估，以选择优选的系统架构解。

6)Characterize architecture(s) based on assessment results.

6) 基于评定结果表征架构。

7)Formulate findings and recommendations.

7) 形成发现与建议。

8)Capture and communicate evaluation results.

8) 捕获并沟通评估结果。

d)Elaborate the system architecture. This activity consists of the following tasks.

d) 细化系统架构。本活动由以下任务组成。

1)Identify or develop architecture viewpoints and model kinds and legends that are governed by these architecture viewpoints.

1) 识别或开发架构视角，以及受这些架构视角管控的模型种类和图例。

2)Develop models and views of the architecture(s).

2) 开发架构的模型与视图。

> **NOTE 7** Models include such items as systems, system elements, interfaces, activities, roles, personnel, techniques, processes, policies, rules, principles, objectives, capabilities, nodes, links, data elements, layers, protocols, hardware items, software items. Architecture viewpoints that include the human as part of a system capture the human requirements to inform how the human impacts system definition (i.e. user or human views).

> **注 7**：模型包括诸如系统、系统元素、接口、活动、角色、人员、技术、过程、方针、规则、原则、目标、能力、节点、链路、数据元素、层、协议、硬件项、软件项等条目。将人作为系统一部分的架构视角捕获人的需求，以说明人如何影响系统定义（即用户视图或人的视图）。

> **NOTE 8** The following are typical considerations in the identification or development of architecture viewpoints:

> **注 8**：以下是识别或开发架构视角时的典型考虑事项：

a) selection, adaptation, or development of viewpoints and model kinds based on stakeholder concerns;

a) 基于利益相关方关注点选择、改编或开发视角与模型种类；

b) identification of expected users of architecture elaboration information, including relevant architecture descriptions, models, and data;

b) 识别架构细化信息的预期用户，包括相关架构描述、模型和数据；

c) identification potential architecture framework(s) or reference architectures to be used in developing models and views.

c) 识别在开发模型与视图时将要使用的潜在架构框架或参考架构。

> **NOTE 9** The following are typical considerations to define the system context and boundaries in terms of interfaces and interactions with external entities:

> **注 9**：以下是在接口和与外部实体的交互方面定义系统语境与边界的典型考虑事项：

a) definition of the system context and boundaries in terms of interfaces and interactions with external entities;

a) 就与外部实体的接口和交互而言，定义系统语境与边界；

b) identification of architectural entities and relationships between entities that address key stakeholder concerns and critical system requirements;

b) 识别应对关键利益相关方关注点和关键系统需求的架构实体以及实体之间的关系；

c) allocation of concepts, properties, characteristics, behaviours, functions, or constraints that are significant to architecture decisions of the system to architectural entities;

c) 将对系统架构决策具有重要意义的理念、属性、特性、行为、功能或约束分配到架构实体；

d) selection, adaptation, or development of models of the candidate architectures of the system;

d) 选择、改编或开发系统候选架构的模型；

e) composition of views from the models according to identified viewpoints to express how the architecture addresses stakeholder concerns and meets stakeholder and system requirements;

e) 按照已识别的视角由模型组成视图，以表达架构如何应对利益相关方关注点并满足利益相关方需求与系统需求；

f) harmonization of the architecture models and views with each other during the development of models and views of the architecture(s).

f) 在开发架构的模型与视图期间，使各架构模型与视图彼此协调一致。

3)Relate the architecture to other architectures and to relevant affected entities to help ensure consistency of the elaborated system architecture.

3) 将架构与其他架构以及相关受影响的实体关联起来，以帮助确保细化后的系统架构的一致性。

4)Assess the architecture elaboration.

4) 评定架构细化。

5)Coordinate use of elaborated architecture by intended users.

5) 协调预期用户对细化后架构的使用。

e)Manage results of system architecture definition. This activity consists of the following tasks.

e) 管理系统架构定义的结果。本活动由以下任务组成。

1)Monitor, assess, and control the system architecture definition activities and tasks.

1) 监视、评定并控制系统架构定义的活动与任务。

2)Obtain agreement on the architecture definition.

2) 就架构定义取得一致意见。

3)Provide support to organizational architecture governance and architecture management efforts.

3) 为组织的架构治理与架构管理工作提供支持。

4)Record key system architecture decisions and the rationale.

4) 记录关键的系统架构决策及其理由。

> **NOTE 10** Rationale includes information about major alternatives and enablers.

> **注 10**：理由包括有关主要备选方案与使能因素的信息。

5)Maintain traceability of the system architecture.

5) 维护系统架构的追溯性。

> **NOTE 11** Through the life cycle, bi-directional traceability is maintained between the architectural entities (models, views, and viewpoints) to the requirements (including allocated, decomposed, and derived), interface definitions, analysis results, and verification methods or techniques. If possible, traceability is also maintained between the architecture entities and the stakeholder concerns.

> **注 11**：在整个生存周期内，在架构实体（模型、视图和视角）与需求（包括已分配、已分解和派生的需求）、接口定义、分析结果以及验证方法或技术之间维护双向追溯性。如有可能，还在架构实体与利益相关方关注点之间维护追溯性。

6)Provide key artefacts that have been selected for baselines.

6) 提供已选定用于基线的关键人工制品。

> **NOTE 12** The configuration management process is used to establish and maintain configuration items and baselines. The system architecture definition process identifies candidates for the baseline and then provides the artefacts to configuration management.

> **注 12**：使用配置管理过程建立并维护配置项与基线。系统架构定义过程识别基线的候选对象，随后将人工制品提供给配置管理。

##### 6.4.5 Design definition process 设计定义过程

###### 6.4.5.1 Purpose 目的

The purpose of the design definition process is to provide sufficient detailed data and information about the system and its elements to realise the solution in accordance with the system requirements and architecture.

设计定义过程的目的是提供关于系统及其元素的足够详细的数据与信息，以按照系统需求与架构实现解。

This process transforms architecture and requirements into a design of the system that can be realised. This process results in sufficiently detailed data and information about the system and its elements to enable implementation consistent with architectural entities defined in models and views of the system architecture, in conformance with applicable system requirements, and in alignment with design guidelines and standards adopted by the organization or project.

本过程将架构与需求转换为可实现的系统设计。本过程产生关于系统及其元素的足够详细的数据与信息，以使实现与系统架构的模型和视图中定义的架构实体相一致，与适用的系统需求相符，并与组织或项目采用的设计指南和标准保持一致。

> **NOTE 1** Design definition considers any applicable technologies and their contribution to the system solution. Design provides the ‘implement-to’ level of the definition, such as drawings and detailed design descriptions.

> **注 1**：设计定义考虑任何适用的技术及其对系统解的贡献。设计提供定义的‘实现级’，例如图样和详细设计描述。

> **NOTE 2** This process provides feedback to the system architecture definition process to consolidate or confirm the allocation, partitioning, and alignment of architectural entities to system elements that comprise the system.

> **注 2**：本过程向系统架构定义过程提供反馈，以整合或确认将架构实体分配、划分并对齐到构成系统的系统元素。

###### 6.4.5.2 Outcomes 预期结果

As a result of the successful performance of the design definition process:

设计定义过程成功执行后：

a) design alternatives for system elements are assessed;

a) 对系统元素的设计备选方案进行了评定；

b) system requirements are allocated to the system design or its elements;

b) 系统需求被分配到系统设计或其元素；

c) interfaces between system design elements comprising the system are defined;

c) 定义了构成系统的各系统设计元素之间的接口；

d) design characteristics of each system element are defined;

d) 定义了每个系统元素的设计特性；

e) enabling systems or services needed for design definition are available;

e) 设计定义所需的使能系统或服务可用；

f) design enablers necessary for design definition efforts are defined;

f) 定义了设计定义工作所必需的设计使能因素；

g) system design is evaluated;

g) 对系统设计进行了评估；

h) traceability of the design is established.

h) 建立了设计的追溯性。

###### 6.4.5.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the design definition process.

以下活动与任务应按照适用于设计定义过程的组织方针与程序予以实施。

a) Prepare for design definition. This activity consists of the following tasks.

a) 准备进行设计定义。本活动由以下任务组成。

1) Define the design definition strategy.

1) 定义设计定义的策略。

2) Determine technologies required for each system element comprising the system.

2) 确定构成系统的每个系统元素所需的技术。

3) Determine the necessary categories of system characteristics represented in the design.

3) 确定设计中表示的系统特性的必要类别。

> **NOTE 1** Examples of system characteristic categories, many of which are the result of an architecture description, include the following: affordability, agility, assurance, autonomy, availability, complexity, flexibility, interoperability, maintainability, modularity, reliability, resilience, security, and usability. Many others exist.

> **注 1**：系统特性类别的示例（其中许多是架构描述的结果）包括：可负担性、敏捷性、保证、自主性、可用性、复杂性、灵活性、互操作性、可维护性、模块化、可靠性、韧性、安全性和易用性。此外还存在许多其他类别。

4) Define principles for evolution of the design.

4) 定义设计演进的原则。

> **NOTE 2** This includes defining periodic assessment of the design characteristics in case of evolution of the system and of its architecture as well as forecasting potential obsolescence of system elements and technologies, their replacement by others over time in the system life cycle, and the consequences for the system design.

> **注 2**：这包括：在系统及其架构演进的情况下，定义对设计特性的定期评定；以及预测系统元素与技术的潜在过时、其在系统生存周期内随时间被其他元素与技术替换，以及对系统设计的后果。

5) Identify and plan for the necessary enabling systems or services needed to support design definition efforts.

5) 识别支持设计定义工作所需的必要使能系统或服务，并作出规划。

6) Obtain or acquire access to the enabling systems or services to be used in the design definition efforts.

6) 获取或取得对设计定义工作中将使用的使能系统或服务的访问权。

> **NOTE 3** The validation process is used to objectively confirm that the enabling system achieves its intended use for its enabling functions.

> **注 3**：使用确认过程客观地确认使能系统就其使能功能达成了其预期用途。

b) Create the system design. This activity consists of the following tasks.

b) 创建系统设计。本活动由以下任务组成。

1) Allocate system requirements to system elements.

1) 将系统需求分配到系统元素。

> **NOTE 4** Some of the system requirements are often allocated to system elements during the system architecture definition process. The purpose of this task is to complete the allocation to the extent necessary to address all system requirements and architecture objectives.

> **注 4**：部分系统需求往往在系统架构定义过程中被分配到系统元素。本任务的目的是在应对所有系统需求与架构目标所需的程度上完成分配。

2) Transform architectural entities and relationships into design elements.

2) 将架构实体与关系转换为设计元素。

> **NOTE 5** This task helps to ensure that each architectural entity (e.g. enterprise or project goals, capabilities and effects, operational activities, resource functions) and relationship is mapped into the appropriate system design elements to help ensure that all the architectural objectives are addressed by the design. ISO/IEC/IEEE 42020 provides more detail on architecture entities.

> **注 5**：本任务有助于确保每个架构实体（例如企业或项目目标、能力与效果、运行活动、资源功能）和关系都映射到适当的系统设计元素，以帮助确保设计应对所有架构目标。ISO/IEC/IEEE 42020 对架构实体提供了更多细节。

3) Transform architectural characteristics into design characteristics.

3) 将架构特性转换为设计特性。

> **NOTE 6** Design characteristics include functionality, behaviour, dimensions, shapes, materials, critical quality characteristics, data processing structures, etc. Margins appropriate for the application are considered as necessary.

> **注 6**：设计特性包括功能、行为、尺寸、形状、材料、关键质量特性、数据处理结构等。视需要，考虑适合应用的裕度。

4) Define the necessary design enablers.

4) 定义必要的设计使能因素。

> **NOTE 7** Design enablers include product standards and specifications, models, equations, algorithms, calculations, formal expressions and values of parameters, patterns, heuristics, etc. that are associated with allocated system characteristics. Consider critical properties in the context of their planned operational environment during the definition of necessary design enablers.

> **注 7**：设计使能因素包括与已分配的系统特性相关联的产品标准与规格、模型、方程、算法、计算、形式化表达式和参数值、模式、启发式方法等。在定义必要的设计使能因素期间，在其计划的运行环境语境中考虑关键属性。

5) Examine design alternatives.

5) 考察设计备选方案。

> **NOTE 8** Feasibility of allocated system characteristics is assessed and trade-offs across the architecture and requirements are performed when allocated system characteristics cannot be readily implemented or when there are significant design or realization challenges to be overcome.

> **注 8**：当已分配的系统特性难以直接实现，或存在需要克服的重大设计或实现挑战时，评定已分配系统特性的可行性，并在架构与需求之间进行权衡。

> **NOTE 9** In addition to new design alternatives, any candidate non-developmental-items (NDI) are usually identified for consideration. This includes COTS (commercial-off-the-shelf), reuse of a previous design, or acquirer provided items. Use of NDI is often preferable for reliability, cost, and interoperability considerations, unless design characteristics cannot be realised by existing artefacts.

> **注 9**：除新的设计备选方案外，通常还识别任何候选的非研制项（NDI）以供考虑。这包括 COTS（商用货架产品）、对先前设计的重用，或获取方提供的项目。出于可靠性、成本和互操作性方面的考虑，使用 NDI 往往更可取，除非现有的人工制品无法实现设计特性。

6) Refine or define the interfaces between the system elements and with external entities.

6) 细化或定义系统元素之间的接口以及与外部实体之间的接口。

> **NOTE 10** Interfaces are identified and defined in the system architecture definition process to the level or extent needed for the architecture intent and understanding. They are refined in design definition process based on the design characteristics, interfaces and interactions of the system element with other system elements comprising the system and with external entities, such as constituent systems of an SoS. It is possible that additional interfaces need to be identified and defined that were not addressed in the system architecture definition process.

> **注 10**：在系统架构定义过程中，接口被识别并定义到架构意图和理解所需的层级或程度。在设计定义过程中，基于系统元素与构成系统的其他系统元素以及与外部实体（例如 SoS 的组成系统）之间的设计特性、接口和交互，对这些接口进行细化。可能需要识别并定义系统架构定义过程中未予处理的附加接口。

7) Establish the design artefacts.

7) 建立设计人工制品。

> **NOTE 11** This task formalises the design characteristics of the system element through dedicated artefacts depending on the implementation technology. Examples of artefacts include data sheets (electronics), databases (software), documents (operator role), and exportable data files (mechanics).

> **注 11**：本任务依据实现技术，通过专用人工制品将系统元素的设计特性形式化。人工制品的示例包括数据表（电子）、数据库（软件）、文档（操作员角色）和可导出数据文件（机械）。

8) Capture the design.

8) 捕获设计。

> **NOTE 12** This includes the design description in a form that can be used to either procure or realise the system elements that comprise the system c) Evaluate the system design. This activity consists of the following tasks.

> **注 12**：这包括以可用于采购或实现构成系统的系统元素的形式给出的设计描述c) 评估系统设计。本活动由以下任务组成。

> **NOTE 13** This design evaluation activity can provide useful information to the verification process.

> **注 13**：本设计评估活动能为验证过程提供有用的信息。

1) Analyse each system design alternative against criteria developed from expected design properties and characteristics.

1) 依据由预期设计属性与特性制定的准则，分析每个系统设计备选方案。

2) Assess each system design alternative for how well it meets the stakeholder requirements and system requirements.

2) 评定每个系统设计备选方案在多大程度上满足利益相关方需求与系统需求。

> **NOTE 14** The assessment includes any associated risks with respect to its suitability for the intended application.

> **注 14**：评定包括与其预期应用适宜性有关的任何相关风险。

> **NOTE 15** Design suitability includes consideration of ease of integration, usability in operation, ease of maintenance, and eventual system disposal.

> **注 15**：设计适宜性包括考虑集成便利性、运行中的易用性、维护便利性以及最终的系统处置。

3) Combine the analyses and assessments into an overall evaluation to select a preferred system design solution.

3) 将各项分析与评定综合为总体评估，以选择优选的系统设计解。

d) Manage results of design definition. This activity consists of the following tasks.

d) 管理设计定义的结果。本活动由以下任务组成。

1) Obtain agreement on the design.

1) 就设计取得一致意见。

2) Map design characteristics up to the system elements.

2) 将设计特性向上映射到系统元素。

> **NOTE 16** This task consists of establishing traceability between the detailed design characteristics and the architectural entities of the system architecture.

> **注 16**：本任务包括在详细设计特性与系统架构的架构实体之间建立追溯性。

> **NOTE 17** This facilitates providing feedback to the system architecture definition process to possibly modify the physical arrangement of system elements to obtain architectural characteristics (e.g. modularity, usability, inter-operability, safeguard) as expected for the parent system architecture to meet stakeholder concerns.

> **注 17**：这有助于向系统架构定义过程提供反馈，以便可能修改系统元素的物理布局，从而获得父系统架构为应对利益相关方关注点所预期的架构特性（例如模块化、易用性、互操作性、防护）。

3) Record key design decisions and the rationale.

3) 记录关键设计决策及其理由。

> **NOTE 18** Rationale includes information about major implementation options and enablers.

> **注 18**：理由包括有关主要实现选项与使能因素的信息。

4) Maintain traceability of the system design.

4) 维护系统设计的追溯性。

> **NOTE 19** Through the life cycle, bi-directional traceability is maintained between the design characteristics and the architectural entities, identified interfaces, analysis results, verification methods or techniques, and system element requirements.

> **注 19**：在整个生存周期内，在设计特性与架构实体、已识别的接口、分析结果、验证方法或技术以及系统元素需求之间维护双向追溯性。

5) Provide key artefacts that have been selected for baselines.

5) 提供已选定用于基线的关键人工制品。

> **NOTE 20** The configuration management process is used to establish and maintain configuration items and baselines. The design definition process identifies candidates for the baseline and then provides the artefacts to configuration management.

> **注 20**：使用配置管理过程建立并维护配置项与基线。设计定义过程识别基线的候选对象，随后将人工制品提供给配置管理。

##### 6.4.6 System analysis process 系统分析过程

###### 6.4.6.1 Purpose 目的

The purpose of the system analysis process is to provide a rigorous basis of data and information for technical understanding to aid decision-making and technical assessments across the life cycle.

系统分析过程的目的是为技术理解提供严谨的数据与信息基础，以在整个生存周期内辅助决策与技术评定。

System analysis covers a wide range of differing analytic functions, levels of complexity, and levels of rigor. It is used to provide input for diverse technical assessments and analytical needs concerning operational concepts, determination of requirement values, resolution of requirements conflicts, assessment of alternative architectures or system elements, performance and risk analyses, and evaluation of engineering strategies (integration, verification, validation, and maintenance). Formality and rigor of the analysis will depend on the criticality of the information needed or artefact supported, the amount of information/data available, the size of the project, and the schedule for the results.

系统分析涵盖范围广泛的各种分析功能、复杂程度和严谨程度。它用于为多种技术评定和分析需要提供输入，这些需要涉及：运行概念、需求值的确定、需求冲突的解决、备选架构或系统元素的评定、性能与风险分析，以及工程策略（集成、验证、确认和维护）的评估。分析的形式化程度与严谨程度将取决于所需信息或所支持人工制品的关键性、可获取的信息／数据量、项目的规模以及结果的进度安排。

> **NOTE 1** This process is often used in conjunction with the decision management, project assessment and control, and risk management processes.

> **注 1**：本过程往往与决策管理过程、项目评定与控制过程以及风险管理过程协同使用。

> **NOTE 2** Typical approaches include mathematical analysis, modelling, simulation, experimentation, and other techniques to analyse technical performance, system behaviour, feasibility, affordability, critical quality characteristics, SoS considerations, technical risks, life cycle costs, and to perform sensitivity analysis of the potential range of values for parameters across all life cycle stages.

> **注 2**：典型途径包括数学分析、建模、仿真、试验以及其他技术，用以分析技术性能、系统行为、可行性、可负担性、关键质量特性、SoS 考虑事项、技术风险、生存周期成本，并对所有生存周期阶段中参数的潜在取值范围进行敏感性分析。

###### 6.4.6.2 Outcomes 预期结果

As a result of the successful performance of the system analysis process:

系统分析过程成功执行后：

a) system analyses needed are identified;

a) 识别出所需的系统分析；

b) system analysis assumptions and results are validated;

b) 系统分析的假设与结果得到确认；

c) system analysis results are provided for decisions or technical assessment needs;

c) 为决策或技术评定需要提供系统分析结果；

d) enabling systems or services needed for system analysis are available;

d) 系统分析所需的使能系统或服务可用；

e) traceability of the system analysis results is established.

e) 建立了系统分析结果的追溯性。

###### 6.4.6.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the system analysis process.

以下活动与任务应按照适用于系统分析过程的组织方针与程序予以实施。

a) Prepare for system analysis. This activity consists of the following tasks.

a) 准备进行系统分析。本活动由以下任务组成。

1) Define the system analysis strategy.

1) 定义系统分析的策略。

2) Identify the problem or question that requires system analysis.

2) 识别需要系统分析的问题或疑问。

> **NOTE 1** This includes technical and functional objectives, critical quality characteristics, various properties, technology maturity, manufacturing maturity, technical risks, etc. The problem statement or question to be answered by the analysis is essential to establish the objectives of the analysis and the expectations and utility of the results.

> **注 1**：这包括技术与功能目标、关键质量特性、各种属性、技术成熟度、制造成熟度、技术风险等。由分析予以解答的问题陈述或疑问，对于建立分析的目标以及结果的期望与效用至关重要。

3) Identify the stakeholders of the system analysis.

3) 识别系统分析的利益相关方。

4) Define the scope, objectives, and level of fidelity of the system analysis.

4) 定义系统分析的范围、目标和保真度水平。

> **NOTE 2** The necessary level of fidelity (accuracy or precision) is an important factor in determining the appropriate level of rigor.

> **注 2**：必要的保真度水平（准确度或精密度）是确定适当严谨程度的重要因素。

5) Select the system analysis methods.

5) 选择系统分析的方法。

> **NOTE 3** The methods are chosen based on time, cost, fidelity, technical drivers, and criticality of analysis. Analysis methods have a wide range of levels of rigor and include expert judgement, “back of the envelope” calculation, spreadsheet computations, historical data and trend analysis, engineering models, simulation, visualization, and prototyping. Due to cost and schedule constraints, organizations typically perform system analysis only for critical characteristics.

> **注 3**：这些方法基于时间、成本、保真度、技术驱动因素和分析的关键性来选择。分析方法具有范围广泛的严谨程度，包括专家判断、“粗略”计算、电子表格计算、历史数据与趋势分析、工程模型、仿真、可视化以及原型制作。由于成本与进度约束，组织通常仅针对关键特性执行系统分析。

6) Identify and plan for the necessary enabling systems or services needed to support system analysis.

6) 识别支持系统分析所需的必要使能系统或服务，并作出规划。

> **NOTE 4** This includes identification of requirements and interfaces for the enabling systems. The system analysis enabling systems include the tools, relevant models, and potential data repositories needed to support the analysis. The methods chosen will be a major factor in determining what tools are appropriate to support the analysis. This also includes determining the availability of relevant models and data.

> **注 4**：这包括识别使能系统的需求与接口。系统分析使能系统包括支持分析所需的工具、相关模型以及潜在的数据存储库。所选择的方法将是确定哪些工具适合支持分析的主要因素。这还包括确定相关模型与数据的可用性。

7) Obtain or acquire access to the enabling systems or services to be used.

7) 获取或取得对将使用的使能系统或服务的访问权。

> **NOTE 5** The validation process is used to objectively confirm that the enabling system achieves its intended use for its enabling functions.

> **注 5**：使用确认过程客观地确认使能系统就其使能功能达成了其预期用途。

8) Identify and validate assumptions.

8) 识别并确认假设。

> **NOTE 6** Validation of assumptions is an ongoing concern. If assumptions change or are determined to be incorrect over time, the analysis is revised.

> **注 6**：假设的确认是一项持续的工作。如果假设随时间发生变化或被判定为不正确，则修订分析。

9) Plan for and collect the data and inputs needed for the analysis.

9) 规划并收集分析所需的数据与输入。

> **NOTE 7** The origin, quality, and validity of data is important to the formulation and execution of the analysis. Criteria for trustworthiness of data needed for the analysis are established. Data and inputs are reviewed for quality and validity (i.e. trustworthy data). Use authoritative sources.

> **注 7**：数据的来源、质量与有效性对于分析的制定与执行很重要。为分析所需数据的可信性建立准则。评审数据与输入的质量与有效性（即可信数据）。使用权威来源。

b) Perform system analysis. This activity consists of the following tasks.

b) 执行系统分析。本活动由以下任务组成。

1) Apply the selected analysis methods to perform the required system analysis.

1) 应用所选的分析方法执行所需的系统分析。

2) Review the analysis results for quality and validity.

2) 评审分析结果的质量与有效性。

> **NOTE 8** The results are coordinated with associated analyses that have been previously completed. Trustworthiness of the results is determined in the review.

> **注 8**：结果与先前已完成的相关分析相协调。结果的可信性在评审中确定。

3) Establish conclusions and recommendations.

3) 形成结论与建议。

> **NOTE 9** The appropriate subject matter experts and stakeholders are identified and engaged in this task.

> **注 9**：在本任务中识别并吸纳相应的领域专家与利益相关方。

4) Record the results of the system analysis, c) Manage system analysis. This activity consists of the following tasks.

4) 记录系统分析的结果，c) 管理系统分析。本活动由以下任务组成。

1) Maintain traceability of system analysis results.

1) 维护系统分析结果的追溯性。

> **NOTE 10** Through the life cycle, bi-directional traceability is maintained between the system analysis results and any system definition item for which the analysis is supporting a decision or providing rationale (e.g. system requirement values, architecture alternatives). This is often facilitated by an appropriate data repository. Trustworthy data includes a requirement to maintain the traceability of the data used for analysis.

> **注 10**：在整个生存周期内，在系统分析结果与该分析为其支撑决策或提供理由的任何系统定义条目（例如系统需求值、架构备选方案）之间维护双向追溯性。这往往借助适当的数据存储库来实现。可信数据包括维护用于分析的数据的追溯性这一要求。

2) Provide key artefacts that have been selected for baselines.

2) 提供已选定用于基线的关键人工制品。

> **NOTE 11** The configuration management process is used to establish and maintain configuration items and baselines. The system analysis process identifies candidates for the baseline and then provides the artefacts to configuration management. For the system analysis process, the analysis results or reports are typical artefacts that are baselined.

> **注 11**：使用配置管理过程建立并维护配置项和基线。系统分析过程确定基线的候选对象，随后将这些人工制品提供给配置管理。对于系统分析过程，分析结果或报告是典型的纳入基线的人工制品。

##### 6.4.7 Implementation process 实现过程

###### 6.4.7.1 Purpose 目的

The purpose of the implementation process is to realise a specified system element.

实现过程的目的是实现一个规定的系统元素。

This process transforms requirements, architecture, and design, including interfaces, into actions that create a system element according to the practices of the selected implementation technology, using appropriate technical specialties or disciplines. This process results in a system element that satisfies specified system requirements (including allocated and derived requirements), architecture, and design.

本过程将需求、架构与设计（包括接口）转换为按照所选实现技术的实践创建系统元素的各项行动，并运用适当的技术专业或学科。本过程产生的系统元素满足规定的系统需求（包括已分配需求与派生需求）、架构与设计。

For system elements that need to be manufactured, after the definition of system element is elaborated to a point that it can be built, a manufacturing approach or procedure is developed or adapted according the system element definition and the desired production rate. The manufacturing of the system elements is then performed over the time with quality control and production optimisation.

对于需要制造的系统元素，在系统元素的定义被细化到可建造的程度之后，根据系统元素定义与期望的生产率制定或适配制造途径或规程。随后，在质量控制与生产优化下，随时间推移执行系统元素的制造。

> **NOTE 1** An effective and efficient manufacturing approach is crucial when large series of items have to be produced. In that case, acceptance of the first produced elements is generally distinguished from the following mass production.

> **注 1**：当必须大批量生产物品时，有效且高效的制造途径至关重要。在这种情况下，通常将首批生产元素的验收与随后的批量生产区分开来。

> **NOTE 2** Implementation applies to elements, in concept, development, and production stages. Production can include manufacturing of a single element or mass production.

> **注 2**：实现在概念阶段、开发阶段和生产阶段均适用于元素。生产能包括单个元素的制造或批量生产。

###### 6.4.7.2 Outcomes 预期结果

As a result of the successful performance of the implementation process:

实现过程成功执行后：

a) implementation constraints that influence the requirements, architecture, or design are identified;

a) 影响需求、架构或设计的实现约束得到识别；

b) a system element is realised;

b) 系统元素得到实现；

c) enabling systems or services needed for implementation are available;

c) 实现所需的使能系统或服务可用；

d) implementation results and anomalies are identified;

d) 实现结果与异常得到识别；

e) traceability is established.

e) 追溯性得到建立。

###### 6.4.7.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the implementation process.

以下活动与任务应按照适用于实现过程的组织方针与程序予以实施。

a)Prepare for implementation. This activity consists of the following tasks.

a) 准备进行实现。本活动由以下任务组成。

1)Define an implementation strategy.

1) 定义实现策略。

> **NOTE 1** Implementation strategies include building new, acquiring new, and reusing existing elements (with or without modification). If the strategy is to reuse, then the project determines the extent, source, and suitability of the reused system elements. The implementation strategy includes procedures, fabrication processes, tools and equipment, tolerances, and verification uncertainties. In the case of repeated system element implementation (e.g. mass production, replacement system elements) the procedures and fabrication processes are defined to achieve consistent and repeatable producibility.

> **注 1**：实现策略包括新建、新购以及重用现有元素（加以修改或不加修改）。如果策略是重用，则项目确定所重用系统元素的程度、来源与适宜性。实现策略包括规程、制造工艺、工具与设备、公差以及验证不确定度。在重复实现系统元素（例如批量生产、替换系统元素）的情况下，定义规程与制造工艺，以实现一致且可重复的可生产性。

> **NOTE 2** The implementation strategy often invokes the agreement processes, or requires enabling systems and services that include specialised life cycle development and support environments.

> **注 2**：实现策略往往调用协议过程，或要求具备包含专门化生存周期开发与支持环境的使能系统和服务。

2)Identify constraints and objectives from implementation on the system requirements, architecture and design characteristics, or implementation techniques.

2) 识别实现对于系统需求、架构与设计特性或实现技术所构成的约束与目标。

> **NOTE 3** Constraints include current or anticipated limitations of the chosen implementation technology, acquirer furnished materials or system elements for adaptation and limitations resulting from the use of required implementation enabling systems.

> **注 3**：约束包括所选实现技术当前或预期的局限、获取方提供的用于适配的材料或系统元素，以及因使用所需的实现使能系统而产生的局限。

3)Identify and plan for the necessary enabling systems or services needed to support implementation.

3) 识别支持实现所需的必要使能系统或服务，并作出规划。

> **NOTE 4** This includes identification of requirements and interfaces for the enabling systems.

> **注 4**：这包括识别使能系统的需求与接口。

4)Obtain or acquire access to the enabling systems or services, and materials to be used.

4) 获取或取得对将使用的使能系统或服务以及材料的访问权。

> **NOTE 5** The validation process is used to objectively confirm that the integration enabling system (including tools) achieves its intended use for its enabling functions.

> **注 5**：使用确认过程客观地确认集成使能系统（包括工具）就其使能功能达成了其预期用途。

b)Perform implementation. This activity consists of the following tasks.

b) 执行实现。本活动由以下任务组成。

> **NOTE 6** Throughout the implementation process, the verification process is used to objectively confirm the system element's conformance to requirements and the product's quality characteristics. The validation process is used to objectively confirm the element is ready to be used in its intended operational environment in accordance with stakeholder requirements.

> **注 6**：在整个实现过程中，使用验证过程客观地确认系统元素对需求的符合性以及产品的质量特性。使用确认过程客观地确认该元素已按照利益相关方需求，准备好在预期运行环境中使用。

1)Realise or adapt system elements, according to the strategy, constraints, and defined implementation procedures.

1) 按照策略、约束以及所定义的实现规程，实现或适配系统元素。

> **NOTE 7** This is done using the implementation enabling systems and specified resources. Realizing system elements can include development or acquisition. Adaptation includes configuration of system elements that are reused or modified. Realization or adaptation is conducted with regard to standards that govern applicable safety, security, privacy, quality, environmental guidelines or legislation, and the practices of the relevant implementation technology.

> **注 7**：这借助实现使能系统和规定的资源来完成。实现系统元素能包括开发或获取。适配包括对重用或修改的系统元素进行配置。实现或适配的开展需遵循规定适用的安全性、安全、隐私、质量与环境指南或法规的标准，以及相关实现技术的实践。

> **NOTE 8** System elements can include the following.

> **注 8**：系统元素能包括以下内容。

a) Hardware: Hardware elements are either acquired or fabricated. Hardware elements are fabricated using applicable techniques relevant to the physical implementation technology and materials selected. The ISO 22400 series specifies requirements for key performance indicators (KPIs) useful for manufacturing systems.

a) 硬件：硬件元素或为获取，或为制造。硬件元素使用与所选物理实现技术和材料相关的适用技术制造。ISO 22400 系列规定了对于制造系统有用的关键绩效指标（KPIs）的要求。

b) Software: System elements realised in software are either acquired or developed. ISO/IEC/IEEE 12207 applies to system elements realised in software.

b) 软件：以软件实现的系统元素或为获取，或为开发。ISO/IEC/IEEE 12207 适用于以软件实现的系统元素。

c) Services: Service elements including a set of services to be provided are acquired or developed. The ISO/IEC 20000 series applies to system elements realised in services.

c) 服务：包含一组将要提供的服务的服务元素或为获取，或为开发。ISO/IEC 20000 系列适用于以服务实现的系统元素。

d) Utilization and support resources: Other system elements include utilization and support resources such as operational procedures, maintenance procedures as well as workforce and user training.

d) 使用与保障资源：其他系统元素包括使用与保障资源，例如运行规程、维护规程以及人员队伍和用户培训。

e) Prototypes: Prototypes are either acquired or fabricated. Often, they are used in early stages to better understand the strategic problem or opportunity and the solution space.

e) 原型：原型或为获取，或为制造。原型往往在早期阶段使用，以更好地理解战略问题或机会以及解空间。

2)Place the system element in a state for future use, as needed.

2) 视需要将系统元素置于供将来使用的状态。

> **NOTE 9** The system element is contained to achieve continuance of its characteristics. Conveyance, packaging, and storage, and their durations, influence the specified containment. Final configuration and product information is captured by the configuration management and information management processes when the system element is stored.

> **注 9**：对系统元素予以封存，以保持其特性持续。运输、包装与存储及其持续时间，影响所规定的封存方式。当系统元素被存储时，最终配置与产品信息由配置管理过程和信息管理过程捕获。

3)Record objective evidence from check-out that the system element meets requirements.

3) 记录检查中表明系统元素满足要求的客观证据。

> **NOTE 10** Evidence is provided in accordance with supply agreements, legislation, and organization policy. Evidence includes element modifications made due to processing changes or any non-conformances found during check-out or the verification and validation processes. The objective evidence is part of the system element's as-implemented configuration baseline established through the configuration management process and includes the results of unit testing, analysis, inspections, walk-through events, demonstrations, product or technical reviews, or other verification exercises.

> **注 10**：证据按照供应协议、法规和组织方针提供。证据包括因工艺变更而对元素所做的修改，或在检查或验证与确认过程中发现的任何不合格。客观证据是通过配置管理过程建立的系统元素“按实现状态”配置基线的一部分，并包括单元测试、分析、检查、走查活动、演示、产品或技术评审或其他验证演练的结果。

c)Manage results of implementation. This activity consists of the following tasks.

c) 管理实现的结果。本活动由以下任务组成。

1)Record implementation results and any anomalies encountered.

1) 记录实现结果及所遇到的任何异常。

> **NOTE 11** This includes anomalies due to the implementation strategy, the implementation enabling systems, or incorrect system definition. The project assessment and control process is used to analyse the data to identify the root cause, to enable corrective, preventive, adaptive, additive, or perfective actions and to record lessons learned.

> **注 11**：这包括因实现策略、实现使能系统或错误的系统定义而产生的异常。使用项目评定与控制过程分析数据，以识别根本原因，从而能采取纠正、预防、适应、增加或完善措施，并记录经验教训。

2)Maintain traceability of the implemented system elements.

2) 维护已实现系统元素的追溯性。

> **NOTE 12** Bi-directional traceability is maintained between the implemented system elements and the system architecture, design, and system requirements including interface requirements and definitions that are necessary for implementation.

> **注 12**：在已实现系统元素与系统架构、设计以及系统需求（包括实现所必需的接口需求与接口定义）之间维护双向追溯性。

3)Provide key artefacts that have been selected for baselines.

3) 提供已选定用于基线的关键人工制品。

> **NOTE 13** The configuration management process is used to establish and maintain configuration items and baselines. The implementation process identifies candidates for the baseline and then provides the artefacts to configuration management. For the implementation process, the system elements are typical artefacts that are baselined.

> **注 13**：使用配置管理过程建立并维护配置项和基线。实现过程确定基线的候选对象，随后将这些人工制品提供给配置管理。对于实现过程，系统元素是典型的纳入基线的人工制品。

##### 6.4.8 Integration process 集成过程

###### 6.4.8.1 Purpose 目的

The purpose of the integration process is to synthesize a set of system elements into a realised system that satisfies the system requirements.

集成过程的目的是将一组系统元素综合为一个满足系统需求的已实现系统。

This process encompasses planning for, preparing for, and aggregating a progressively more complete set of system elements or artefacts. Interfaces are identified and activated to enable interoperation and subsequent verification and possibly validation of the requirements (including characteristics) of the system elements or elements as intended. This process also connects and checks out interfaces of the SoI with enabling systems for which there is direct interaction.

本过程涵盖对逐步更完整的一组系统元素或人工制品进行规划、准备和聚合。识别并激活接口，以实现互操作，并使系统元素或元素的需求（包括特性）按预期得到后续验证以及可能的确认。本过程还连接并检查 SoI 与存在直接交互的使能系统之间的接口。

> **NOTE** A detailed description of the integration process can be found in ISO/IEC/IEEE 24748-6.

> **注**：集成过程的详细描述见 ISO/IEC/IEEE 24748-6。

###### 6.4.8.2 Outcomes 预期结果

As a result of the successful performance of the integration process:

集成过程成功执行后：

a) integration constraints that influence system requirements, architecture, or design, including interfaces, are identified;

a) 影响系统需求、架构或设计（包括接口）的集成约束得到识别；

b) approaches and checkpoints for the correct activation of the identified interfaces and system functions are defined;

b) 正确激活已识别接口与系统功能的途径与检查点得到定义；

c) enabling systems or services needed for integration are available;

c) 集成所需的使能系统或服务可用；

d) a system composed of implemented system elements or artefacts is integrated;

d) 由已实现系统元素或人工制品构成的系统得到集成；

e) the system external interfaces (system to external environment) and system internal interfaces

e) 系统外部接口（系统与外部环境之间）与系统内部接口

(between implemented system elements) are checked;

（已实现系统元素之间）得到检查；

f) integration results and anomalies are identified;

f) 集成结果与异常得到识别；

g) traceability of the integrated system elements is established.

g) 已集成系统元素的追溯性得到建立。

###### 6.4.8.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the Integration process.

以下活动与任务应按照适用于集成过程的组织方针与程序予以实施。

a) Prepare for integration. This activity consists of the following tasks.

a) 准备进行集成。本活动由以下任务组成。

1) Identify and define checkpoints for the correct activation and integrity of the interfaces and the selected system functions as the system elements are synthesized.

1) 在系统元素被综合的过程中，为接口与所选系统功能的正确激活和完整性识别并定义检查点。

> **NOTE 1** The verification process is applied for detailed verification of the interfaces.

> **注 1**：应用验证过程对接口进行详细验证。

> **NOTE 2** ISO/IEC/IEEE 15026 series and ISO/IEC 27000 provide information on assurance, integrity, and security. Typical considerations include anti-counterfeit, anti-tamper, system and software assurance, and interoperability elements when identifying and defining checkpoints.

> **注 2**：ISO/IEC/IEEE 15026 系列和 ISO/IEC 27000 提供了关于保证、完整性与安全的信息。在识别和定义检查点时，典型的考虑事项包括防伪、防篡改、系统与软件保证以及互操作性要素。

2) Define the integration strategy.

2) 定义集成策略。

> **NOTE 3** The integration is performed according to a predefined integration strategy that sequences the order for aggregating the evolving system elements (the actual system, concepts, requirements, models, mock-ups, prototypes, procedures, plans, or other documents) based on the priorities of the system requirements and system architecture definition focusing on the interfaces, while minimizing integration time and cost and providing appropriate risk treatments.

> **注 3**：集成按照预先定义的集成策略执行，该策略基于系统需求的优先次序以及聚焦于接口的系统架构定义，对聚合不断演进的系统元素（实际系统、概念、需求、模型、实物模型、原型、规程、计划或其他文档）的顺序作出安排，同时尽量缩短集成时间、降低集成成本，并提供适当的风险处理。

> **NOTE 4** This strategy often provides for subsequent verification against a sequence of progressively more complete system element configurations. It is dependent on system element availability and is consistent with a fault isolation and diagnosis strategy.

> **注 4**：该策略往往为针对一系列逐步更完整的系统元素配置进行后续验证作出安排。它取决于系统元素的可用性，并与故障隔离与诊断策略保持一致。

3) Identify constraints and objectives from integration to be incorporated in the system requirements, architecture or design.

3) 识别来自集成的、需纳入系统需求、架构或设计的约束与目标。

> **NOTE 5** This includes requirements such as accessibility, safety for integrators, required interfaces for sets of implemented system elements and for enablers, and interface constraints.

> **注 5**：这包括诸如可访问性、集成人员的安全性、已实现系统元素集合与使能因素所需的接口以及接口约束等要求。

4) Identify and plan for the necessary enabling systems or services needed to support integration.

4) 识别支持集成所需的必要使能系统或服务，并作出规划。

> **NOTE 6** This includes identification of requirements and interfaces for the enabling systems. Enabling systems for integration include integration facilities, assembly equipment, training systems, discrepancy reporting systems, simulators, measurement devices, and facility security.

> **注 6**：这包括识别使能系统的需求与接口。集成使能系统包括集成设施、装配设备、培训系统、差异报告系统、模拟器、测量装置以及设施安全。

5) Obtain or acquire access to the enabling systems or services, and materials to be used.

5) 获取或取得对将使用的使能系统或服务以及材料的访问权。

> **NOTE 7** The validation process is used to objectively confirm that the integration enabling system (including tools) achieves its intended use for its enabling functions.

> **注 7**：使用确认过程客观地确认集成使能系统（包括工具）就其使能功能达成了其预期用途。

b) Perform integration. This activity consists of the following tasks.

b) 执行集成。本活动由以下任务组成。

1) Check interface availability and conformance of the interfaces in accordance with interface definitions and integration schedules.

1) 按照接口定义与集成进度安排，检查接口的可用性以及接口的符合性。

> **NOTE 8** This includes interfaces internal to the SoI (e.g. between system elements including operators), and between the SoI and external systems or entities (including interfacing, enabling, interoperating systems, as well as users of the SoI).

> **注 8**：这包括 SoI 内部的接口（例如系统元素之间，包括操作者），以及 SoI 与外部系统或实体之间的接口（包括接口系统、使能系统、互操作系统以及 SoI 的用户）。

2) Perform actions to address any conformance or availability issues.

2) 采取措施处理任何符合性或可用性问题。

3) Combine the implemented system elements or artefacts in accordance with planned sequences.

3) 按照计划的顺序合并已实现的系统元素或人工制品。

4) Integrate system element configurations until the complete system is synthesized.

4) 集成系统元素配置，直至综合出完整的系统。

5) Check for expected results of the interfaces, selected functions, and critical quality characteristics.

5) 检查接口、所选功能以及关键质量特性的预期结果。

> **NOTE 9** This is performed several times at different integration levels to confirm that specific interfaces have been established.

> **注 9**：为确认特定接口得到建立，这一检查在不同集成层级上执行若干次。

c) Manage results of integration. This activity consists of the following tasks.

c) 管理集成的结果。本活动由以下任务组成。

1) Record integration results and any anomalies encountered.

1) 记录集成结果及所遇到的任何异常。

> **NOTE 10** This includes anomalies due to the integration strategy, the integration enabling systems (including tools), execution of the integration or incorrect system or element definition. Where inconsistencies exist at the interface between the system, its specified operational environment and any systems that enable the utilization stage, the deviations lead to corrective actions or requirement changes. The project assessment and control process is used to analyse the data to identify the root cause, to enable corrective, preventive, adaptive, additive, or perfective actions and to record lessons learned.

> **注 10**：这包括因集成策略、集成使能系统（包括工具）、集成的执行或错误的系统或元素定义而产生的异常。当系统、其规定的运行环境与任何使能使用阶段的系统之间的接口存在不一致时，偏差导致采取纠正措施或更改需求。使用项目评定与控制过程分析数据，以识别根本原因，从而能采取纠正、预防、适应、增加或完善措施，并记录经验教训。

2) Maintain traceability of the integrated system elements.

2) 维护已集成系统元素的追溯性。

> **NOTE 11** Bi-directional traceability is maintained between the integrated system elements and the integration strategy, system architecture, design, as well as stakeholder and system requirements including interface requirements and definitions that are necessary for integration.

> **注 11**：在已集成系统元素与集成策略、系统架构、设计以及利益相关方需求和系统需求（包括集成所必需的接口需求与接口定义）之间维护双向追溯性。

3) Provide key artefacts that have been selected for baselines.

3) 提供已选定用于基线的关键人工制品。

> **NOTE 12** The configuration management process is used to establish and maintain configuration items and baselines. The integration process identifies candidates for the baseline and then provides the artefacts to configuration management. For the integration process, the integration strategy is a typical artefact that is baselined.

> **注 12**：使用配置管理过程建立并维护配置项和基线。集成过程确定基线的候选对象，随后将这些人工制品提供给配置管理。对于集成过程，集成策略是典型的纳入基线的人工制品。

##### 6.4.9 Verification process 验证过程

###### 6.4.9.1 Purpose 目的

The purpose of the verification process is to provide objective evidence that a system, system element, or artefact fulfils its specified requirements and characteristics.

验证过程的目的是提供客观证据，表明系统、系统元素或人工制品满足其规定的要求与特性。

The verification process identifies the anomalies in any artefact (e.g. system requirements, architecture description, or design description), implemented system elements, or life cycle processes using appropriate methods, techniques, standards, or rules. This process provides the necessary information to determine resolution of identified anomalies.

验证过程运用适当的方法、技术、标准或规则，识别任何人工制品（例如系统需求、架构描述或设计描述）、已实现系统元素或生存周期过程中的异常。本过程为确定已识别异常的解决方式提供必要的信息。

> **NOTE 1** The verification process determines that the "solution is built right". The validation process determines that the "right solution is built".

> **注 1**：验证过程判定“解被正确构建”。确认过程判定“正确的解被构建”。

> **NOTE 2** Construction of an assurance case (see 5.10) can be helpful to provide insight for verification activities and to present verification results.

> **注 2**：构建保证案例（见 5.10）能有助于为验证活动提供洞察，并呈现验证结果。

###### 6.4.9.2 Outcomes 预期结果

As a result of the successful performance of the verification process:

验证过程成功执行后：

a) constraints of verification that influence the requirements, architecture, or design are identified;

a) 影响需求、架构或设计的验证约束得到识别；

b) enabling systems or services needed for verification are available;

b) 验证所需的使能系统或服务可用；

c) the system, system element, or artefact is verified;

c) 系统、系统元素或人工制品得到验证；

d) data providing information for corrective actions are reported;

d) 报告为纠正措施提供信息的数据；

e) objective evidence that the realised system fulfils the requirements, architecture, and design is provided;

e) 表明已实现系统满足需求、架构与设计的客观证据得到提供；

f) verification results and anomalies are identified;

f) 验证结果与异常得到识别；

g) traceability of the verified system elements is established.

g) 已验证系统元素的追溯性得到建立。

###### 6.4.9.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the verification process.

以下活动与任务应按照适用于验证过程的组织方针与程序予以实施。

a) Prepare for verification. This activity consists of the following tasks.

a) 准备进行验证。本活动由以下任务组成。

1) Identify the verification scope and corresponding verification actions.

1) 识别验证范围及相应的验证行动。

> **NOTE 1** Scope includes system, system elements, artefacts, or information items which will be verified against applicable requirements, characteristics, or other properties. For each verification action, the strategy describes what will be verified (actual system, model, mock-up, prototype, procedure, plan, or other document), the verification method, and the expected result as defined by the success criteria.

> **注 1**：范围包括将对照适用的需求、特性或其他属性加以验证的系统、系统元素、人工制品或信息部件。对于每项验证行动，策略描述将验证什么（实际系统、模型、实物模型、原型、规程、计划或其他文档）、验证方法以及由成功准则所定义的预期结果。

2) Identify the constraints that potentially limit the feasibility of verification actions.

2) 识别可能限制验证行动可行性的约束。

> **NOTE 2** Constraints include technical feasibility, cost, time, availability of verification enablers or qualified personnel, contractual constraints, and characteristics such as criticality of the mission.

> **注 2**：约束包括技术可行性、成本、时间、验证使能因素或合格人员的可用性、合同约束，以及任务关键性等特性。

3) Select appropriate verification methods and associated success criteria for every verification action.

3) 为每项验证行动选择适当的验证方法与相关成功准则。

> **NOTE 3** Verification methods include: inspection (including peer review), analysis (including modelling, simulation, and analogy/similarity), demonstration, and testing. The selection of one or more verification methods is made according to the type of system, the needs of the item being verified, the objectives of the project, and the acceptable risks. Selected methods and success criteria are coordinated with relevant stakeholders to help ensure the verification strategy is acceptable.

> **注 3**：验证方法包括：检查（包括同行评审）、分析（包括建模、仿真和类比／相似）、演示和测试。根据系统类型、被验证条目的需要、项目的目标以及可接受的风险，选择一种或多种验证方法。所选方法与成功准则与相关利益相关方协调，以帮助确保验证策略可接受。

4) Define the verification strategy.

4) 定义验证策略。

> **NOTE 4** The definition includes trading off what will be verified (scope) against the constraints or limits, and deduces what verification actions to use. Verification actions that are candidates for deletion are evaluated for the risks their withdrawal imposes. The prioritised verification strategy encompasses the most appropriate verification method for every verification action and the necessary verification enabling systems (simulators, test-benches, qualified personnel, location, facilities, etc.) according to selected verification methods. Under some regulatory situations, the strategy can include the verification of all system elements. The strategy also identifies any points in the system life cycle requiring evidence that the system meets its requirements.

> **注 4**：该定义包括就将验证什么（范围）与约束或限制进行权衡，并推断出宜采用哪些验证行动。对于候选删除的验证行动，评定其撤销所带来的风险。按优先次序排列的验证策略通过同时定义以下内容而得到：每项验证行动最适当的验证方法；按照所选验证方法所需的验证使能系统（模拟器、试验台、合格人员、场所、设施等）。在某些监管情形下，策略能包括对所有系统元素的验证。策略还识别系统生存周期中需要提供系统满足其要求的证据的任何时点。

> **NOTE 5** The verification strategy and schedule are updated according to the progress of the project; in particular planned verification actions are redefined or rescheduled when unexpected events or system evolutions occur.

> **注 5**：验证策略与进度安排根据项目的进展予以更新；特别是当发生非预期事件或系统演进时，重新定义或重新安排计划的验证行动。

> **NOTE 6** This strategy generally focuses on minimizing cost and schedule, and/or risk, providing a balanced approach for confirming that the system or system element has been “built right”.

> **注 6**：该策略通常聚焦于尽量降低成本、缩短进度和／或降低风险，为确认系统或系统元素已“被正确构建”提供一种平衡的途径。

5) Identify constraints and objectives from the verification strategy to be incorporated in the system requirements, architecture, and design.

5) 识别来自验证策略的、需纳入系统需求、架构与设计的约束与目标。

> **NOTE 7** This includes practical limitations of accuracy, uncertainty, or repeatability that are imposed by the verification enablers; the associated measurement methods; the level of system integration; and the availability, accessibility, and interconnection with enablers.

> **注 7**：这包括验证使能因素所施加的准确度、不确定度或重复性方面的实际限制；相关的测量方法；系统集成的层级；以及与使能因素的可用性、可访问性和互连。

6) Identify and plan for the necessary enabling systems or services needed to support verification.

6) 识别支持验证所需的必要使能系统或服务，并作出规划。

> **NOTE 8** Verification enabling systems include verification equipment, simulators, test automation tools, facilities, etc.

> **注 8**：验证使能系统包括验证设备、模拟器、测试自动化工具、设施等。

7) Obtain or acquire access to the enabling systems or services to be used to support verification.

7) 获取或取得对将用于支持验证的使能系统或服务的访问权。

> **NOTE 9** The acquisition of the enabling systems can be done through various ways such as rental, procurement, development, reuse, subcontracting; usually the acquisition of the complete set of enablers is a mix of these ways. The validation process is used to objectively confirm that the verification enabling system achieves its intended use for its enabling functions.

> **注 9**：使能系统的获取能通过多种方式进行，如租赁、采购、开发、复用、分包；整套使能物的获取通常为这些方式的混合。使用确认过程客观地确认验证使能系统就其使能功能达成了其预期用途。

b) Perform verification. This activity consists of the following tasks.

b) 执行验证。本活动由以下任务组成。

1) Define the verification procedures, each supporting one or a set of verification actions.

1) 定义验证程序，每项程序支持一项或一组验证行动。

> **NOTE 10** The procedures identify the purpose of the verification with success criteria (expected results), the verification method to be applied, the necessary enabling systems (facilities, equipment, etc.), and the environmental conditions to perform each verification procedure (resources, qualified personnel, etc.).

> **注 10**：这些程序确定验证的目的及成功准则（预期结果）、拟采用的验证方法、必要的使能系统（设施、设备等），以及执行每项验证程序的环境条件（资源、合格人员等）。

2) Perform the verification procedures.

2) 执行验证程序。

> **NOTE 11** Verification, according to the verification strategy, occurs at the appropriate time in the schedule. Verification activities are performed at the appropriate point in the system life cycle in the defined environment, with defined enabling systems and resources. The performance of a verification action consists of capturing a result from the execution of the verification procedure, comparing the obtained result with the expected result as defined by the success criteria, and deducing a degree of correctness of the submitted element and confidence in the result. The necessity of repeating verification actions is determined as anomalies are resolved.

> **注 11**：按照验证策略，验证在进度安排中的适当时机进行。验证活动在系统生存周期中的适当时点、在规定的环境下、使用规定的使能系统和资源来执行。执行一项验证行动包括：从验证程序的执行中采集结果，将所得结果与成功准则所定义的预期结果进行比较，并推断所提交元素的正确程度以及对结果的信心。随着异常得到解决，确定重复验证行动的必要性。

c) Manage results of verification. This activity consists of the following tasks.

c) 管理验证的结果。本活动由以下任务组成。

1) Record verification results and any anomalies encountered.

1) 记录验证结果及所遇到的任何异常。

> **NOTE 12** This includes anomalies due to the verification strategy, the verification enabling systems, execution of the verification action, or incorrect system definition. The project assessment and control process is used to analyse the data to identify the root cause, to enable corrective, preventive, adaptive, additive, or perfective actions, and to record lessons learned.

> **注 12**：这包括由验证策略、验证使能系统、验证行动的执行或错误的系统定义所导致的异常。使用项目评定与控制过程分析数据，以识别根本原因，从而能采取纠正、预防、适应、增加或完善措施，并记录经验教训。

> **NOTE 13** The evaluation of verification results in the project assessment and control process and follow-up corrective action can vary greatly depending on the purpose of the verification. For elements of a system, this can imply a simple problem resolution action to address a failed system element verification followed by re-verification, or more significant actions such as major project re-direction based on a failure to attain a key milestone, e.g. failed system testing.

> **注 13**：在项目评定与控制过程中对验证结果的评估以及后续纠正措施，能因验证目的的不同而有很大差异。对于系统的各元素，这可能意味着采取简单的问题解决行动来处理某项失败的系统元素验证，随后重新验证；也可能意味着采取更重大的行动，例如因未能达到某个关键里程碑（如系统测试失败）而对项目作重大重新定向。

2) Record operational incidents and problems during verification and track their resolution.

2) 记录验证期间的运行事件和问题，并跟踪其解决情况。

> **NOTE 14** Performing problem resolution is handled through the quality assurance and project assessment and control processes. Any actual changes to the requirements, architecture, design, or system elements are done within other technical processes.

> **注 14**：问题解决的执行通过质量保证过程以及项目评定与控制过程来处理。对需求、架构、设计或系统元素的任何实际更改，均在其他技术过程中完成。

> **NOTE 15** Operational incidents are those that occur in the operational environment.

> **注 15**：运行事件是在运行环境中发生的事件。

3) Obtain agreement from the approval authority that the system, system element, or artefact meets the specified requirements.

3) 从批准机构取得一致意见，确认系统、系统元素或人工制品满足规定要求。

4) Maintain traceability for verification.

4) 维护验证的追溯性。

> **NOTE 16** Bi-directional traceability is maintained between the verified system elements and the verification strategy, system architecture, design, and system requirements. Traceability of the verified system, system elements, or artefacts typically includes traceable verification results or evidence, such as anomalies, deviations or requirement satisfaction.

> **注 16**：在经验证的系统元素与验证策略、系统架构、设计及系统需求之间维护双向追溯性。对经验证的系统、系统元素或人工制品的追溯，通常包括可追溯的验证结果或证据，例如异常、偏差或需求满足情况。

5) Provide key artefacts that have been selected for baselines.

5) 提供已选定用于基线的关键人工制品。

> **NOTE 17** The configuration management process is used to establish and maintain configuration items and baselines. The verification process identifies candidates for the baseline, and then provides the artefacts to configuration management. For the verification process, the verification strategy is a typical artefact that is baselined.

> **注 17**：使用配置管理过程建立并维护配置项和基线。验证过程确定基线的候选对象，随后将这些人工制品提供给配置管理。对于验证过程，验证策略是典型的纳入基线的人工制品。

##### 6.4.10 Transition process 转换过程

###### 6.4.10.1 Purpose 目的

The purpose of the transition process is to establish a capability for a system to provide services specified by stakeholder requirements in the operational environment.

转换过程的目的是使系统具备在运行环境中提供利益相关方需求所规定服务的能力。

This process moves the system in an orderly, planned manner to be operable in the intended environment, which may be a new or changed environment, e.g., operations or validation. As a result of the transition, the system is functional and compatible with enabling, interfacing, and interoperating systems in the environment. It installs a verified system, together with relevant enabling systems (e.g. planning system, support system, operator training system, user training system), as defined in agreements. The transition process can be used every time the system or system elements are transitioned from one entity or environment to another.

本过程以有序、有计划的方式将系统移至预期环境，使其能在该环境中运行；该环境可能是新的或已变更的环境，例如运行环境或确认环境。作为转换的结果，系统能发挥功能，并与环境中的使能系统、接口系统和互操作系统相兼容。它安装经验证的系统以及相关的使能系统（例如规划系统、支持系统、操作者培训系统、用户培训系统），如协议中所定义。每当系统或系统元素从一个实体或环境转换到另一个实体或环境时，都能使用转换过程。

> **NOTE** In the case of system upgrades, a typical goal is that transition activities are accomplished with minimal disruption to ongoing operations.

> **注**：在系统升级的情况下，典型目标是使转换活动对正在进行的运行造成的干扰最小。

###### 6.4.10.2 Outcomes 预期结果

As a result of the successful performance of the transition process:

转换过程成功执行后：

a) transition constraints that influence system requirements, architecture, or design are identified;

a) 影响系统需求、架构或设计的转换约束得到识别；

b) enabling systems or services needed for transition are available;

b) 转换所需的使能系统或服务可用；

c) the site is prepared;

c) 现场准备就绪；

d) the system installed in its operational environment is capable of delivering its specified functions;

d) 安装在其运行环境中的系统能够交付其规定的功能；

e) operators, users and other stakeholders necessary to the system utilization and support are trained;

e) 系统使用与保障所必需的操作者、用户及其他利益相关方得到培训；

f) transition results and anomalies are identified;

f) 转换结果和异常得到识别；

g) the installed system is activated and ready for operation;

g) 已安装的系统被激活并准备好运行；

h) traceability of the transitioned elements is established.

h) 经转换的元素的追溯性得到建立。

###### 6.4.10.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the transition process.

以下活动与任务应按照适用于转换过程的组织方针与程序予以实施。

a) Prepare for the transition. This activity consists of the following tasks.

a) 为转换做准备。本活动由以下任务组成。

1) Define a transition strategy.

1) 定义转换策略。

> **NOTE 1** The transition strategy includes all activities from site delivery and installation through deployment and commissioning of the system in accordance with agreements using appropriate mechanisms to help ensure system integrity is maintained. The strategy involves all the stakeholders, including human operators. The strategy includes roles and responsibilities, facilities considerations, shipping and receiving, contingency back out plans, training, installation acceptance demonstration tasks, operational readiness reviews, operations commencement, transition success criteria, rights of access, data rights, and integration with other plans. Commissioning of the system is considered along with the decommissioning of the old system, when one exists. In this case, the transition and disposal processes are used concurrently.

> **注 1**：转换策略包括按照协议、使用适当的机制、从现场交付与安装到系统部署与投运的所有活动，以帮助确保系统完整性得以保持。该策略涉及所有利益相关方，包括作为操作者的人员。该策略包括角色与职责、设施方面的考虑、发运与接收、应急回退计划、培训、安装验收演示任务、运行准备就绪评审、运行开始、转换成功准则、访问权、数据权以及与其他计划的整合。系统的投运与旧系统（若存在）的退役一并考虑。在此情况下，转换过程与处置过程并发使用。

2) Identify and define any facility or site changes needed.

2) 识别并定义所需的任何设施或现场更改。

> **NOTE 2** This includes changes needed for installation or use.

> **注 2**：这包括安装或使用所需的更改。

3) Identify and arrange training of operators, users, and other stakeholders necessary for system utilization and support.

3) 识别并安排系统使用与保障所必需的操作者、用户及其他利益相关方的培训。

> **NOTE 3** In addition to formal or informal training, organizational change management activities can be helpful for adapting to changes required for use of transitioned systems.

> **注 3**：除正式或非正式培训外，组织更改管理活动能有助于适应经转换系统的使用所要求的变更。

4) Identify system constraints from transition to be incorporated in the system requirements, architecture or design.

4) 识别由转换产生的、将纳入系统需求、架构或设计的系统约束。

5) Identify and plan for the necessary enabling systems or services needed to support transition.

5) 识别支持转换所需的必要使能系统或服务，并作出规划。

> **NOTE 4** This includes identification of requirements and interfaces for the enabling systems.

> **注 4**：这包括确定使能系统的需求和接口。

6) Obtain or acquire access to the enabling systems or services to be used.

6) 获取或取得对将使用的使能系统或服务的访问权。

> **NOTE 5** The validation process is used to objectively confirm that the transition enabling system achieves its intended use for its enabling functions.

> **注 5**：使用确认过程客观地确认转换使能系统就其使能功能达成了其预期用途。

7) Identify and arrange shipping and receiving of system elements and enabling systems.

7) 识别并安排系统元素和使能系统的发运与接收。

b) Perform the transition. This activity consists of the following tasks.

b) 执行转换。本活动由以下任务组成。

1) Prepare the site of operation in accordance with installation requirements.

1) 按照安装要求准备运行现场。

> **NOTE 6** It is presupposed that site preparation is conducted in accordance with applicable health, safety, security, and environmental regulations.

> **注 6**：前提是现场准备按照适用的健康、安全性、安全和环境法规进行。

2) Deliver the system for installation at the correct location and time.

2) 在正确的地点和时间交付系统以供安装。

> **NOTE 7** Sometimes intermediate storage prior to delivery is a necessary consideration.

> **注 7**：有时，交付前的中间存储是必须考虑的事项。

3) Install the system in its operational environment and interface to its environment.

3) 将系统安装在其运行环境中，并与其环境接口。

> **NOTE 8** The system installation includes configuring it with required operational data, taking into account changes to the operating environment or the organization’s process changes. Consideration of data migration is sometimes necessary. This includes data that will be or is stored in a cloud resource.

> **注 8**：系统安装包括使用所需的运行数据对其进行配置，并考虑运行环境的变更或组织的流程变更。有时需要考虑数据迁移。这包括将存储在或已存储在云资源中的数据。

4) Demonstrate proper installation of the system.

4) 演示系统的正确安装。

> **NOTE 9** Acceptance tests are usually defined in the agreement to demonstrate satisfactory installation. Where the exact location or environment of operation is not available, a representative example is selected. Specific attention is given to the physical interfaces, including interfaces to any functions supplied by virtual resources (e.g. cloud).

> **注 9**：验收测试通常在协议中规定，以证明安装令人满意。在无法获得确切的运行地点或运行环境时，选取有代表性的示例。特别关注物理接口，包括与虚拟资源（例如云）所提供的任何功能的接口。

5) Provide training of the operators, users, and other stakeholders necessary for system utilization and support.

5) 提供系统使用与保障所必需的操作者、用户及其他利益相关方的培训。

6) Perform activation and check-out of the system.

6) 执行系统的激活与检查。

> **NOTE 10** This task takes all steps needed to activate the system to an operational state, including power-up, instrument checks, assessment of environmental conditions, assessment of connections to external systems, and other readiness evaluations, in accordance with operational procedures and organizational policies, taking into account regulations. This task also interacts with the validation process to objectively confirm that the system fulfils the stakeholder requirements in the operational environment.

> **注 10**：本任务采取将系统激活至运行状态所需的所有步骤，包括加电、仪器检查、环境条件评定、与外部系统连接的评定以及其他准备就绪评估；这些步骤按照运行程序和组织方针并考虑法规进行。本任务还与确认过程交互，以客观地确认系统在运行环境中满足利益相关方需求。

> **NOTE 11** This task includes integrity checks and conformance with technical standards. Anti-counterfeit, system and software assurance, and interoperability elements are usually considered when identifying and defining checkpoints.

> **注 11**：本任务包括完整性检查以及与技术标准的符合性。在确定和定义检查点时，通常考虑防伪、系统与软件保证以及互操作性方面的要素。

7) Demonstrate the installed system is capable of delivering its required functions.

7) 演示已安装的系统能够交付其所需的功能。

> **NOTE 12** Acceptance tests, as specified in agreements, can define the criteria that demonstrate that the system or system element possesses the capability to deliver the required functions and services when installed in its operational environment and staffed by operators. Specific attention is given to the key functions and logical interfaces with respect to adequately addressing changes in business processes and workflow.

> **注 12**：协议中规定的验收测试能确定准则，用以证明系统或系统元素在安装于其运行环境并配备操作者时，具备交付所需功能和服务的能力。特别关注关键功能和逻辑接口，以充分应对业务流程和工作流的变更。

> **NOTE 13** This is an operational readiness task that examines readiness of functional capability for an operational state. The validation process evaluates whether the system meets the stakeholder needs.

> **注 13**：这是一项运行准备就绪任务，考察功能能力对运行状态的准备就绪情况。确认过程评估系统是否满足利益相关方需要。

8) Demonstrate the functions provided by the system are sustainable by the enabling systems.

8) 演示系统所提供的功能能由使能系统予以持续保障。

> **NOTE 14** This is an operational readiness task that examines readiness of enabling systems for an operational state.

> **注 14**：这是一项运行准备就绪任务，考察使能系统对运行状态的准备就绪情况。

9) Review the system for operational readiness.

9) 评审系统的运行准备就绪情况。

> **NOTE 15** This includes the results functional demonstration, validation activities, and sustainment demonstration.

> **注 15**：这包括功能演示的结果、确认活动以及持续保障演示。

10) Commission the system for operations.

10) 使系统投入运行。

> **NOTE 16** This includes providing support to the users and operators during the operations commencement (commissioning) of the system.

> **注 16**：这包括在系统开始运行（投运）期间向用户和操作者提供支持。

c) Manage results of transition. This activity consists of the following tasks.

c) 管理转换的结果。本活动由以下任务组成。

1) Record transition results and any anomalies encountered.

1) 记录转换结果及所遇到的任何异常。

> **NOTE 17** This includes anomalies due to the transition strategy, the transition enabling systems, execution of the transition or incorrect system definition. Where inconsistencies exist at the interface between the system, its specified operational environment and any systems that enable the utilization stage, the deviations are resolved through corrective actions or changes to the requirements. The project assessment and control process is used to analyse the data to identify the root cause, to enable corrective, preventive, adaptive, additive, or perfective actions and to record lessons learned.

> **注 17**：这包括由转换策略、转换使能系统、转换的执行或错误的系统定义所导致的异常。在系统、其规定的运行环境与任何使能使用阶段的系统之间的接口处存在不一致时，通过纠正措施或更改需求来消除偏差。使用项目评定与控制过程分析数据，以识别根本原因，从而能采取纠正、预防、适应、增加或完善措施，并记录经验教训。

2) Record operational incidents and problems during transition and track their resolution.

2) 记录转换期间的运行事件和问题，并跟踪其解决情况。

> **NOTE 18** Performing problem resolution is handled through the quality assurance and project assessment and control processes. Any actual changes to the requirements, architecture, design, or system elements are done within other technical processes.

> **注 18**：问题解决的执行通过质量保证过程以及项目评定与控制过程来处理。对需求、架构、设计或系统元素的任何实际更改，均在其他技术过程中完成。

3) Maintain traceability of the transitioned system elements.

3) 维护经转换的系统元素的追溯性。

> **NOTE 19** Bi-directional traceability is maintained between the transitioned system elements and the transition strategy, system architecture, design, and system requirements. Traceability records are updated when a system element is changed.

> **注 19**：在经转换的系统元素与转换策略、系统架构、设计及系统需求之间维护双向追溯性。系统元素发生更改时，更新追溯记录。

4) Provide key artefacts that have been selected for baselines.

4) 提供已选定用于基线的关键人工制品。

> **NOTE 20** The configuration management process is used to establish and maintain configuration items and baselines. The transition process identifies candidates for the baseline and then provides the artefacts to configuration management. For the transition process, the transition strategy is a typical artefact that is baselined.

> **注 20**：使用配置管理过程建立并维护配置项和基线。转换过程确定基线的候选对象，随后将这些人工制品提供给配置管理。对于转换过程，转换策略是典型的纳入基线的人工制品。

##### 6.4.11 Validation process 确认过程

###### 6.4.11.1 Purpose 目的

The purpose of the validation process is to provide objective evidence that the system, when in use, fulfils its business or mission objectives and stakeholder needs and requirements, achieving its intended use in its intended operational environment.

确认过程的目的是提供客观证据，证明系统在使用时满足其业务或任务目标以及利益相关方需要与需求，并在其预期运行环境中达成其预期用途。

The objective of validating a system, system element, or artefact is to acquire confidence in its ability to meet validation criteria. Validation is confirmed by stakeholders. This process provides the necessary information so that identified anomalies can be resolved by the appropriate technical process where the anomaly was created.

确认系统、系统元素或人工制品的目标是获得对其满足确认准则之能力的信心。确认由利益相关方予以认定。本过程提供必要的信息，使已识别的异常能由产生该异常的相应技术过程予以解决。

> **NOTE 1** The validation process determines that the "right solution is built". The verification process determines that the "solution is built right".

> **注 1**：确认过程确定的是“构建了正确的解”。验证过程确定的是“正确地构建了解”。

> **NOTE 2** Validation is also applicable to the artefacts (e.g. requirements, architecture, design, design characteristics, or system elements) produced in the definition and realization of the system.

> **注 2**：确认也适用于在系统的定义与实现中产生的人工制品（例如需求、架构、设计、设计特性或系统元素）。

> **NOTE 3** Construction of an assurance case (see 5.10) can be helpful to provide insight for validation activities and to present validation results.

> **注 3**：构建保证案例（见 5.10）能有助于为确认活动提供洞察并呈现确认结果。

###### 6.4.11.2 Outcomes 预期结果

As a result of the successful performance of the validation process:

确认过程成功执行后：

a) validation criteria are defined;

a) 确认准则得到定义；

b) the availability of services required by stakeholders is confirmed;

b) 利益相关方所需服务的可用性得到认定；

c) constraints of validation that influence the requirements, architecture, or design are identified;

c) 影响需求、架构或设计的确认约束得到识别；

d) the system, system element, or artefact is validated;

d) 系统、系统元素或人工制品得到确认；

e) enabling systems or services needed for validation are available;

e) 确认所需的使能系统或服务可用；

f) validation results and anomalies are identified;

f) 确认结果和异常得到识别；

g) objective evidence of successful validation is provided;

g) 成功确认的客观证据得到提供；

h) traceability of the validated system elements is established.

h) 经确认的系统元素的追溯性得到建立。

###### 6.4.11.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the validation process.

以下活动与任务应按照适用于确认过程的组织方针与程序予以实施。

a) Prepare for validation. This activity consists of the following tasks.

a) 为确认做准备。本活动由以下任务组成。

1) Identify the validation scope and corresponding validation actions.

1) 确定确认范围及相应的确认行动。

> **NOTE 1** Scope includes system, system elements, or artefacts which will be validated against applicable validation criteria. For each validation action, the strategy describes what will be validated (e.g. the actual system, a model, a mock-up, a prototype, a procedure, a plan, or other document), the validation method, and the expected result as defined by the success criteria. The scope also includes evaluating that the product or service is predictable in its intended environment and does not enable any unintended users that can negatively impact the intended use of the system.

> **注 1**：范围包括将对照适用的确认准则予以确认的系统、系统元素或人工制品。对于每项确认行动，策略描述将确认什么（例如实际系统、模型、样机、原型、程序、计划或其他文档）、确认方法以及成功准则所定义的预期结果。范围还包括评估：产品或服务在其预期环境中是可预测的，并且不会使任何可能对系统预期用途产生负面影响的非预期用户得以使用。

> **NOTE 2** The supplier, the acquirer, or an agent of the acquirer participates in or performs validation. The responsibility is generally designated in the agreement.

> **注 2**：供应方、获取方或获取方的代理人参与或执行确认。该职责通常在协议中指定。

2) Identify the constraints that potentially limit the feasibility of validation actions.

2) 识别可能限制确认行动可行性的约束。

> **NOTE 3** Constraints include technical feasibility, cost, time, availability of validation enablers or qualified personnel, contractual constraints, and characteristics such as criticality of the mission.

> **注 3**：约束包括技术可行性、成本、时间、确认使能物或合格人员的可用性、合同约束，以及诸如使命关键程度等特性。

3) Select appropriate validation methods and associated success criteria for each validation action.

3) 为每项确认行动选择适当的确认方法及相关的成功准则。

> **NOTE 4** Validation methods include: inspection, analysis, analogy/similarity, demonstration, simulation, peer-review, testing, or certification. The selection of validation methods is made according to the type and purpose of the system, the objectives of the project, regulatory or legal requirements, and the acceptable risks of a validation action.

> **注 4**：确认方法包括：检查、分析、类比／相似性、演示、仿真、同行评审、测试或认证。确认方法的选择依据系统的类型和目的、项目的目标、监管或法律要求以及某项确认行动的可接受风险。

> **NOTE 5** Where appropriate, validation steps or states are defined (e.g. in-house validation, on-site validation, operational validation) that progressively build confidence in conformance of the delivered system, then the installed system, then the in-service system, and assist diagnosis of any encountered discrepancies. Appropriate validation methods needed to perform the validation actions are selected, as are defined in the purpose, conditions and success criteria for each validation action.

> **注 5**：在适当时，定义确认步骤或确认状态（例如内部确认、现场确认、运行确认），以逐步建立对交付系统、随后对已安装系统、再对在役系统之符合性的信心，并有助于诊断所遇到的任何差异。选择执行确认行动所需的适当确认方法，这些方法按每项确认行动的目的、条件和成功准则加以确定。

4) Define the validation strategy.

4) 定义确认策略。

> **NOTE 6** The definition includes the trade-off analysis of what will be validated (scope) against the constraints or limits and deduces what validation actions to keep. Validation actions that are candidates for deletion are evaluated for the risks their withdrawal imposes. The prioritised validation strategy is obtained defining concurrently: the most appropriate validation method for every validation action; the necessary validation enablers (simulators, test-benches, qualified personnel, location, facilities, etc.) according to selected validation methods.

> **注 6**：该定义包括就“将确认什么（范围）”与约束或限值进行权衡分析，并推断出保留哪些确认行动。对于候选删除的确认行动，评定其撤销所带来的风险。按优先次序排列的确认策略通过同时定义以下内容而得到：每项确认行动最适当的确认方法；按照所选确认方法所需的确认使能物（模拟器、试验台、合格人员、场所、设施等）。

> **NOTE 7** The validation strategy and schedule are updated according to the progress of the project; in particular planned validation actions are redefined or rescheduled when unexpected events or system evolutions occur.

> **注 7**：确认策略和进度计划根据项目进展予以更新；特别是当发生非预期事件或系统演进时，重新定义或重新安排已规划的确认行动。

5) Identify system constraints from the validation strategy to be incorporated in the stakeholder needs and requirements transformed from those needs.

5) 识别由确认策略产生的系统约束，这些约束将纳入利益相关方需要以及由这些需要转换而来的需求。

> **NOTE 8** This includes practical limitations of accuracy, uncertainty, or repeatability that are imposed by the validation enablers; the associated measurement methods; and the availability, accessibility and interconnection with enablers.

> **注 8**：这包括由确认使能物所施加的准确度、不确定度或可重复性方面的实际限制；相关的测量方法；以及使能物的可用性、可访问性和互连情况。

6) Identify and plan for the necessary enabling systems or services needed to support validation.

6) 识别支持确认所需的必要使能系统或服务，并作出规划。

> **NOTE 9** This includes identification of requirements and interfaces for enabling systems. Validation enabling systems include validation equipment, simulators, test automation tools, facilities, etc.

> **注 9**：这包括确定使能系统的需求和接口。确认使能系统包括确认设备、模拟器、测试自动化工具、设施等。

7) Obtain or acquire access to the enabling systems or services to be used to support validation.

7) 获取或取得对将用于支持确认的使能系统或服务的访问权。

> **NOTE 10** There are various ways to obtain access to enabling systems such as rental, procurement, development, reuse, or subcontracting. Usually access to the complete set of enablers is a mix of these ways. The validation process is also used to objectively confirm that the validation enabling system achieves its intended use for its enabling functions.

> **注 10**：获取使能系统的访问权有多种方式，如租赁、采购、开发、复用或分包。对整套使能物的访问通常是这些方式的混合。确认过程还用于客观地确认确认使能系统就其使能功能达成了其预期用途。

b) Perform validation. This activity consists of the following tasks.

b) 执行确认。本活动由以下任务组成。

1) Define the validation procedures, each supporting one or a set of validation actions.

1) 定义确认程序，每项程序支持一项或一组确认行动。

> **NOTE 11** This includes the identification of the success criteria (expected results), the validation method to be applied, the corresponding validation enablers (facilities, equipment, etc.), and the environment conditions to perform the validation procedure (resources, qualified personnel, etc.).

> **注 11**：这包括确定成功准则（预期结果）、拟采用的确认方法、相应的确认使能物（设施、设备等），以及执行确认程序的环境条件（资源、合格人员等）。

2) Perform the validation procedures.

2) 执行确认程序。

> **NOTE 12** The performance of a validation action consists of capturing a result from the execution of the validation procedure; comparing the obtained result with the expected result as defined by the success criteria; deducing a degree of compliance of the element; and deciding about the acceptability of compliance, if possible, uncertainty (lack of confidence) remains.

> **注 12**：执行一项确认行动包括：从确认程序的执行中采集结果；将所得结果与成功准则所定义的预期结果进行比较；推断该元素的符合程度；以及就符合性的可接受性作出判定，若可能，仍存在不确定度（信心不足）。

> **NOTE 13** System validation activities are performed at the appropriate point the system life cycle, in the defined environment (as close as possible of the operational environment, or representative of it), with the intended users or acceptable surrogates, and with defined enablers and resources. Validation results are reviewed to confirm that the services of the system that are required by stakeholders are available.

> **注 13**：系统确认活动在系统生存周期中的适当时点、在规定环境（尽可能接近运行环境或能代表运行环境）中、与预期用户或可接受的替代者一起、并使用规定的使能物和资源来执行。评审确认结果，以认定利益相关方所要求的系统服务可用。

c) Manage results of validation. This activity consists of the following tasks.

c) 管理确认的结果。本活动由以下任务组成。

1) Record validation results and any anomalies encountered.

1) 记录确认结果及所遇到的任何异常。

> **NOTE 14** This includes anomalies due to the validation strategy, the validation enabling systems, execution of the validation action, or incorrect system definition. The project assessment and control process is used to analyse the data to identify the root cause, to enable corrective, preventive, adaptive, additive, or perfective actions, and to record lessons learned.

> **注 14**：这包括由确认策略、确认使能系统、确认行动的执行或错误的系统定义所导致的异常。使用项目评定与控制过程分析数据，以识别根本原因，从而能采取纠正、预防、适应、增加或完善措施，并记录经验教训。

2) Record operational incidents and problems during validation and track their resolution.

2) 记录确认期间的运行事件和问题，并跟踪其解决情况。

> **NOTE 15** Performing problem resolution is handled through the quality assurance and project assessment and control processes. Any actual changes to the requirements, architecture, design, or system elements are done within other technical processes.

> **注 15**：问题解决的执行通过质量保证过程以及项目评定与控制过程来处理。对需求、架构、设计或系统元素的任何实际更改，均在其他技术过程中完成。

3) Obtain agreement that the validation criteria have been met.

3) 就确认准则已得到满足取得一致意见。

4) Maintain traceability for validation.

4) 维护确认的追溯性。

> **NOTE 16** Bi-directional traceability is maintained between the validated system elements and the validation strategy, mission or business analysis, life cycle concepts, stakeholder requirements, system architecture, design, and system requirements. Traceability of the validated system, system elements, or artefacts typically includes traceable validation results or evidence, such as deviations from or achievements of intended use of the system.

> **注 16**：在经确认的系统元素与确认策略、任务或业务分析、生存周期概念、利益相关方需求、系统架构、设计及系统需求之间维护双向追溯性。对经确认的系统、系统元素或人工制品的追溯，通常包括可追溯的确认结果或证据，例如对系统预期用途的偏离或达成情况。

5) Provide key artefacts that have been selected for baselines.

5) 提供已选定用于基线的关键人工制品。

> **NOTE 17** The configuration management process is used to establish and maintain configuration items and baselines. The validation process identifies candidates for the baseline and then provides the artefacts to configuration management. For the validation process, the validation strategy is a typical artefact that is baselined.

> **注 17**：配置管理过程用于建立并维护配置项和基线。确认过程识别基线的候选对象，然后将人工制品提供给配置管理。对于确认过程，确认策略是典型的被基线化的人工制品。

##### 6.4.12 Operation process 运行过程

###### 6.4.12.1 Purpose 目的

The purpose of the operation process is to use the system to provide its products or services.

运行过程的目的是使用系统提供其产品或服务。

This process establishes requirements for and assigns personnel to operate the system, and monitors the products or services and operator-system performance. To sustain products or services, it identifies and analyses operational anomalies in relation to agreements, stakeholder requirements, and organizational constraints.

本过程规定运行系统的人员要求并分配人员，并监视产品／服务以及操作员-系统性能。为维持产品／服务，本过程结合协议、利益相关方要求和组织约束识别并分析运行异常。

> **NOTE** ISO/IEC 20000-1 details the operation of a service management system, including operation and improvement of managed operational services.

> **注**：ISO/IEC 20000-1 详细规定了服务管理系统的运行，包括对受管理的运行服务所进行的运行与改进。

###### 6.4.12.2 Outcomes 预期结果

As a result of the successful performance of the operation process:

作为运行过程成功执行的结果：

a) operation constraints that influence system requirements, architecture, or design are identified;

a) 影响系统需求、架构或设计的运行约束得到识别；

b) enabling systems, services, and material needed for operation are available;

b) 运行所需的使能系统、服务和物资可供使用；

c) trained, qualified operators are available;

c) 训练有素、具备资格的操作员可供使用；

d) system products or services that meet stakeholder requirements are delivered;

d) 满足利益相关方要求的系统产品或服务得到交付；

e) system performance during operation is monitored;

e) 运行期间的系统性能得到监视；

f) support to the stakeholders is provided.

f) 向利益相关方提供支持。

###### 6.4.12.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the operation process.

组织应按照适用的组织方针和规程，针对运行过程实施下列活动与任务。

a)Prepare for operation. This activity consists of the following tasks.

a) 准备运行。本活动由下列任务组成。

1)Define an operation strategy.

1) 规定运行策略。

> **NOTE 1** This defines approaches, schedules, resources, and specific considerations required to perform system operation, and usually is created in early life cycle stages. It often includes:

> **注 1**：本策略规定执行系统运行所需的方法、进度、资源和特定考虑事项，通常在生存周期早期阶段编制。它常常包括：

a) the capacity, availability, schedule considerations, and security of products or services as they are introduced, routinely operated, and disposed;

a) 产品／服务在引入、日常运行和处置时的容量、可用性、进度考虑事项和安全性；

b) the human resources strategy and qualification requirements;

b) 人力资源策略和资格要求；

c) the release and re-acceptance criteria and schedules of the system to permit modifications that sustain existing or enhanced products or services;

c) 系统的发布与重新验收准则和进度，以允许为维持现有产品或服务或为增强产品／服务而实施修改；

d) the approach to implement the operational modes in the system operational concept, including normal and contingency operations; this can include an approach for critical operational issues and for resiliency in the face of cyber security threats and attacks;

d) 在系统运行概念中实施各运行模式的方法，包括正常运行和应急运行；这可包括针对关键运行问题的方法，以及面对网络安全威胁和攻击时的韧性方法；

e) measures for operation that will provide insight into performance levels.

e) 能深入了解性能水平的运行度量。

> **NOTE 2** The ISO 22400 series specifies requirements for key performance indicators (KPI) useful for manufacturing systems.

> **注 2**：ISO 22400 系列规定了可用于制造系统的关键绩效指标（KPI）的要求。

a) The operational and occupational safety strategy for operators and others using or in contact with the system during operation, accounting for any safety regulations.

a) 针对操作员以及其他在运行期间使用系统或与系统接触的人员的运行安全和职业安全策略，并考虑任何安全法规。

b) The environmental protection and sustainability strategy for operating the system.

b) 运行系统的环境保护与可持续性策略。

c) Monitoring procedures for changes in external conditions (e.g. threats, need for improved performance) and the results of operational monitoring activities.

c) 针对外部条件变化（例如威胁、对改进性能的需要）的监视规程，以及运行监视活动的结果。

2)Identify system constraints and objectives from operation to be incorporated in the system requirements, architecture, or design.

2) 识别来自运行的、需纳入系统需求、架构或设计的系统约束和目标。

> **NOTE 3** It is generally helpful to identify the following: cyber security threats that are related to operation; required resiliency objectives from operation; areas that are high priority for automation to address operational needs.

> **注 3**：识别下列各项通常是有益的：与运行有关的网络安全威胁；运行所要求的韧性目标；为满足运行需要而高优先进行自动化的领域。

3)Identify and plan for the necessary enabling systems or services needed to support operation.

3) 识别支持运行所需的必要使能系统或服务并作出规划。

> **NOTE 4** This includes identification of requirements and interfaces for the enabling systems.

> **注 4**：这包括识别使能系统的要求和接口。

4)Obtain or acquire access to the enabling systems or services to be used.

4) 获得或取得对将使用的使能系统或服务的访问权。

> **NOTE 5** The validation process is used to objectively confirm that the operation enabling system achieves its intended use for its enabling functions.

> **注 5**：确认过程用于客观地确认运行使能系统针对其使能功能达到其预期用途。

5)Identify or define training and qualification requirements to sustain the workforce needed for system operation.

5) 识别或规定培训和资格要求，以维持系统运行所需的人员队伍。

6)Assign trained, qualified personnel to be operators.

6) 分配训练有素、具备资格的人员担任操作员。

> **NOTE 6** The training and qualification includes awareness of the system in its operational environment and a defined programme of familiarization, with appropriate fault detection and isolation instruction. Operator knowledge, skill and experience requirements guide the personnel selection criteria, and where relevant, their authorization to operate is confirmed. The scope of qualification depends on the SoI and its environment. For example, in some environments regulatory requirements include certification of operators, whereas in others there is no certification requirement. A training mode of the operational system sometimes impacts product or service availability.

> **注 6**：培训和资格包括对系统在其运行环境中的认识，以及一项已规定的熟悉计划，并配有适当的故障检测与隔离指导。操作员的知识、技能和经验要求指导人员选择准则，并在相关时确认其操作授权。资格的范围取决于 SoI 及其环境。例如，在某些环境中法规要求包括操作员认证，而在另一些环境中则没有认证要求。运行系统的培训模式有时会影响产品或服务的可用性。

b)Perform operation. This activity consists of the following tasks.

b) 执行运行。本活动由下列任务组成。

1)Use the system in its intended operational environment.

1) 在其预期的运行环境中使用系统。

> **NOTE 7** The operation strategy guides the system usage. Where agreed, continuous service capacity and quality is maintained when the system replaces an existing system that is being retired.

> **注 7**：运行策略指导系统的使用。在达成一致的情况下，当系统替换正在退役的现有系统时，维持持续的服务容量和质量。

2)Apply materials and other resources, as required, to operate the system and sustain its product and service capabilities.

2) 按需投入物资和其他资源，以运行系统并维持其产品和服务能力。

> **NOTE 8** This includes energy sources for hardware, connectivity for software, and provisions for operators.

> **注 8**：这包括硬件的能源、软件的连接性以及为操作员提供的保障。

3)Monitor system operation.

3) 监视系统运行。

> **NOTE 9** This often includes:

> **注 9**：这常常包括：

a) managing adherence to the operation strategy and operational procedures;

a) 管理对运行策略和运行规程的遵守；

b) monitoring that the system is operated in a safe manner and compliant with legislated guidelines concerning occupational safety and environmental protection.

b) 监视系统以安全的方式运行，并符合有关职业安全和环境保护的法定指南。

4)Use the measures defined in the strategy and analyse them to confirm that system performance is within acceptable parameters.

4) 使用策略中定义的度量并对其进行分析，以确认系统性能处于可接受参数范围内。

> **NOTE 10** Monitoring the system includes reviewing that the performance is within established thresholds, periodic instrument readings are acceptable, and service and response times are acceptable. Operator feedback and suggestions are useful input for improving system operational performance.

> **注 10**：监视系统包括审查性能是否处于既定阈值之内、定期仪表读数是否可接受，以及服务时间和响应时间是否可接受。操作员的反馈和建议是改进系统运行性能的有用输入。

> **NOTE 11** Cost of operation is also monitored against objectives and constraints, and to identify potential improvements.

> **注 11**：运行成本也对照目标和约束加以监视，并用于识别潜在的改进。

5)Identify and record when system or service performance is not within acceptable parameters.

5) 识别并记录系统或服务性能不处于可接受参数范围内的情况。

> **NOTE 12** The system sometimes exhibits unacceptable performance when system elements implemented in hardware have exceeded their useful life or the system’s operational environment affects the operating and maintenance personnel (including staff turnover, operator stress and fatigue).

> **注 12**：当以硬件实现的系统元素已超过其使用寿命，或系统的运行环境影响运行人员和维护人员（包括人员更替、操作员紧张和疲劳）时，系统有时会表现出不可接受的性能。

6)Perform system contingency operations, if necessary.

6) 必要时执行系统应急运行。

> **NOTE 13** This includes operating the system in a degraded mode, performing back-out and restore operation, system shutdown, implementation of work-around procedures to restore operation, or other modes for special conditions. If needed, the operator performs steps necessary to enter into contingency operations and possibly power down the system. Contingency operations are performed according to pre-established procedures for such an event. Often these procedures are accompanied by a continuity plan.

> **注 13**：这包括以降级模式运行系统、执行回退和恢复运行、系统关机、实施临时替代规程以恢复运行，或针对特殊条件的其他模式。必要时，操作员执行进入应急运行所需的步骤，并可能关闭系统电源。应急运行按照为此类事件预先制定的规程执行。这些规程往往附有连续性计划。

c)Manage results of operation. This activity consists of the following tasks.

c) 管理运行结果。本活动由下列任务组成。

1)Record results of operation and any anomalies encountered.

1) 记录运行结果以及遇到的任何异常。

> **NOTE 14** This includes anomalies due to the operation strategy, the operation enabling systems, execution of the operation, or incorrect system definition. The project assessment and control process is used to analyse the data to identify the root cause; to enable corrective, preventive, adaptive, additive, or perfective actions; and to record lessons learned.

> **注 14**：这包括因运行策略、运行使能系统、运行执行或错误的系统定义而产生的异常。项目评定与控制过程用于分析数据以识别根本原因；支持采取纠正性、预防性、适应性、增加性或完善性措施；并记录经验教训。

2)Record operational incidents and problems and track their resolution.

2) 记录运行事件和问题并跟踪其解决。

> **NOTE 15** Performing problem resolution is handled through the quality assurance and project assessment and control processes. Any actual changes to the requirements, architecture, design, or system elements are done within other technical processes.

> **注 15**：问题的解决通过质量保证过程和项目评定与控制过程来处理。对需求、架构、设计或系统元素的任何实际更改在其他技术过程内完成。

> **NOTE 16** If an incident is experienced during operation, the operator records the incident and performs actions prescribed in validated operating procedures to restore normal operations.

> **注 16**：如果在运行期间发生事件，操作员记录该事件，并执行经确认的运行规程中规定的措施，以恢复正常运行。

3)Maintain traceability for operations.

3) 保持运行的追溯性。

> **NOTE 17** Maintain bi-directional traceability to operational results and artefacts, strategic needs, system operational concept, concept of operations, and stakeholder requirements. Traceability of the operational results and artefacts typically includes evidence, incidents, and problems.

> **注 17**：保持与运行结果和人工制品、战略需要、系统运行概念、运行构想以及利益相关方要求之间的双向追溯性。运行结果和人工制品的追溯性通常包括证据、事件和问题。

4)Provide key artefacts that have been selected for baselines.

4) 提供已选定用于基线的关键人工制品。

> **NOTE 18** The configuration management process is used to establish and maintain configuration items and baselines. The operation process identifies candidates for the baseline and then provides the artefacts to configuration management.

> **注 18**：配置管理过程用于建立并维护配置项和基线。运行过程识别基线的候选对象，然后将人工制品提供给配置管理。

d)Support stakeholders. This activity consists of the following tasks.

d) 支持利益相关方。本活动由下列任务组成。

1)Provide assistance and consultation to stakeholders as requested.

1) 按请求向利益相关方提供帮助和咨询。

> **NOTE 19** Assistance and consultation includes the provision or recommendation of sources for training, documentation, vulnerability resolution, cyber security reporting, and other support services supporting effective use of the product or service.

> **注 19**：帮助和咨询包括提供或推荐培训来源、文档、脆弱性解决、网络安全报告，以及支持有效使用产品或服务的其他支持服务。

2)Record and monitor requests and subsequent actions for support.

2) 记录并监视支持请求及随后的措施。

3)Determine the degree to which delivered products or services satisfy the needs of stakeholders.

3) 确定所交付的产品或服务满足利益相关方需要的程度。

> **NOTE 20** The results are analysed and required action to restore or amend system or services to provide continued customer satisfaction is identified. Wherever possible the benefit of such action is agreed upon by stakeholders or their representatives. The customer satisfaction data also serves as an input to the quality management process.

> **注 20**：对结果进行分析，并识别为恢复或改善系统或服务以持续提供顾客满意所需的措施。只要可能，此类措施的收益由利益相关方或其代表商定。顾客满意度数据还用作质量管理过程的输入。

##### 6.4.13 Maintenance process 维护过程

###### 6.4.13.1 Purpose 目的

The purpose of the maintenance process is to sustain the capability of the system to provide a product or service.

维护过程的目的是维持系统提供产品或服务的能力。

This process monitors the system’s capability to deliver products or services, records incidents for analysis, takes corrective, preventive, adaptive, additive, and perfective actions and confirms restored capability. The process includes packaging, handling, storage, and transportation for the required replacement system elements. This is often required to support the objectives of the Integration and Transition processes, including required system and software assurance.

本过程监视系统交付产品或服务的能力，记录事件以供分析，采取纠正性、预防性、适应性、增加性和完善性措施，并确认能力得到恢复。本过程包括对所需更换系统元素的包装、装卸、贮存和运输。为支持集成过程和转换过程的目标（包括所需的系统和软件保证），常常需要这样做。

The need for maintenance can arise from multiple causes other than failures, such as changes to interfacing systems or infrastructure, evolving security threats, and technical obsolescence of system elements and enabling systems over the system life cycle.

维护需要可能由失效以外的多种原因引起，例如接口系统或基础设施的变更、不断演变的安全威胁，以及系统元素和使能系统在系统生存周期内的技术过时。

> **NOTE** More detail on software maintenance can be found in ISO/IEC/IEEE 14764.

> **注**：关于软件维护的更多细节见 ISO/IEC/IEEE 14764。

###### 6.4.13.2 Outcomes 预期结果

As a result of the successful performance of the maintenance process:

作为维护过程成功执行的结果：

a) maintenance and logistics constraints that influence system requirements, architecture, or design are identified;

a) 影响系统需求、架构或设计的维护与后勤约束得到识别；

b) enabling systems or services needed for maintenance and logistics are available;

b) 维护与后勤所需的使能系统或服务可供使用；

c) replacement, repaired, or revised system elements are made available;

c) 更换、修复或修改后的系统元素可供使用；

d) the need for required maintenance and logistics actions are reported;

d) 对所需维护与后勤措施的需要得到报告；

e) failure and life cycle data, including associated costs, is determined.

e) 失效和生存周期数据（包括相关成本）得到确定。

###### 6.4.13.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the maintenance process.

组织应按照适用的组织方针和规程，针对维护过程实施下列活动与任务。

a)Prepare for maintenance and logistics. This activity consists of the following tasks.

a) 准备维护与后勤。本活动由下列任务组成。

1)Define a maintenance strategy.

1) 规定维护策略。

> **NOTE 1** The maintenance strategy, also known as the maintenance concept, defines the approaches, priorities, schedules, resources, and specific considerations required to perform maintenance in conformance with operational availability requirements. It generally includes:

> **注 1**：维护策略又称维护概念，它规定为符合运行可用性要求而执行维护所需的方法、优先级、进度、资源和特定考虑事项。它通常包括：

a) the corrective, preventive, adaptive, additive, and perfective maintenance strategy to sustain products or services in the operational environment to achieve customer satisfaction;

a) 为在运行环境中维持产品或服务以实现顾客满意而采取的纠正性、预防性、适应性、增加性和完善性维护策略；

b) the scheduled preventive maintenance actions that reduce the likelihood of system failure without undue loss of services or impact on normal operations (e.g. suspension or restriction of the products or services);

b) 计划安排的预防性维护措施，其在不过度损失服务或不影响正常运行（例如暂停或限制产品／服务）的前提下降低系统失效的可能性；

c) approach to help ensure that sourced materials and system elements that do not meet specified quality, origin and functionality (e.g. counterfeit) are not introduced into the system.

c) 帮助确保不符合规定质量、来源和功能（例如假冒）的外购材料和系统元素不被引入系统的方法。

d) the skill and personnel levels required to effect repairs, replacements, and restoration accounting for maintenance staff requirements and any relevant legislation regarding health and safety, security, and the environment;

d) 实施修理、更换和恢复所需的技能水平和人员数量，并考虑维护人员要求以及有关健康与安全性、安全和环境的任何相关法规；

e) measures for maintenance that will provide insight into performance levels, effectiveness, and efficiency.

e) 能深入了解性能水平、有效性和效率的维护度量。

> **NOTE 2** In most cases, the extension of capability, mid-life upgrade, or evolution of legacy systems becomes a new system development project that will apply the set of processes within an appropriate life cycle as applicable.

> **注 2**：在多数情况下，能力扩展、中期升级或遗留系统的演进会成为一个新的系统开发项目，该项目将视情况在适当的生存周期内应用这组过程。

> **NOTE 3** Reliability-centered maintenance (RCM) is a cost-effective maintenance strategy to address dominant causes of equipment failures [supported by failure modes, effects, and criticality analysis (FMECA) and fault tree analysis]. It provides a systematic approach to defining a routine maintenance programme composed of cost-effective tasks that preserve important functions. SAE JA1011 provides detailed information. Condition-based maintenance (CBM) is a strategy to improve system reliability by reducing the amount of time the system is unavailable while conducting routine or corrective maintenance.

> **注 3**：以可靠性为中心的维护（RCM）是一种经济有效的维护策略，用于处理设备失效的主导原因[由故障模式、影响及危害性分析（FMECA）和故障树分析提供支持]。它提供一种系统化的方法，用于规定由经济有效的任务组成的例行维护大纲，以保持重要功能。SAE JA1011 给出了详细信息。基于状态的维护（CBM）是一种通过减少系统在执行例行维护或纠正性维护期间不可用的时间来改进系统可靠性的策略。

> **NOTE 4** The ISO 18435 series specifies a set of methods for use when integrating diagnostics, capability assessment, and maintenance applications with other applications in production, control, and other manufacturing operations.

> **注 4**：ISO 18435 系列规定了将诊断、能力评定和维护应用与生产、控制及其他制造运行中的其他应用集成时使用的一组方法。

2)Define a logistics strategy.

2) 规定后勤策略。

> **NOTE 5** The logistics strategy defines the approaches, schedules, resources, and specific considerations required to perform logistics throughout the life cycle. It generally includes:

> **注 5**：后勤策略规定在整个生存周期内执行后勤所需的方法、进度、资源和特定考虑事项。它通常包括：

a) acquisition logistics to help ensure supportability implications are considered early during the development stage;

a) 获取后勤，以帮助确保在开发阶段早期即考虑保障性影响；

b) operations logistics to help ensure that the necessary material and resources, in the right quantity and quality, are available at the right place and time throughout the utilization and support stages;

b) 运行后勤，以帮助确保在整个使用阶段和保障阶段，必要物资和资源以恰当的数量和质量在恰当的地点和时间可供使用；

c) the number and type of replacement system elements to be stored, their storage locations and conditions, their anticipated replacement rate, and their storage life and renewal frequency.

c) 拟贮存的更换系统元素的数量和类型、其贮存地点和条件、其预期更换率，以及其贮存寿命和更新频次。

3)Identify constraints and objectives from maintenance or logistics to be incorporated in the system requirements, architecture, or design.

3) 识别来自维护或后勤的、需纳入系统需求、架构或设计的约束和目标。

> **NOTE 6** These often result from the need to

> **注 6**：这些通常源于以下需要：

- reuse existing maintenance enabling systems;

- 复用现有的维护使能系统；

- reuse existing holdings of replaceable system element and accommodate re-supply limitations;

- 复用现有的可更换系统元素库存，并适应再供应限制；

- conduct maintenance in specific locations or environments; or

- 在特定地点或环境中进行维护；或

- enhancing or simplifying existing maintenance activities.

- 增强或简化现有的维护活动。

4)Identify trade-offs such that the system and associated maintenance and logistics actions results in a solution that is affordable, operable, supportable, and sustainable.

4) 识别权衡，使系统及相关的维护与后勤措施形成经济可承受、可运行、可保障且可持续的解决方案。

> **NOTE 7** The system analysis and decision management processes are used to perform the assessments and trade-off decisions.

> **注 7**：系统分析过程和决策管理过程用于执行评定和权衡决策。

5)Identify and plan for the necessary enabling systems, products, or services needed to support maintenance and logistics.

5) 识别支持维护与后勤所需的必要使能系统、产品或服务并作出规划。

> **NOTE 8** This includes identification of requirements and interfaces for the enabling systems.

> **注 8**：这包括识别使能系统的要求和接口。

6)Obtain or acquire access to the enabling systems or services to be used.

6) 获得或取得对将使用的使能系统或服务的访问权。

> **NOTE 9** The validation process is used to objectively confirm that the maintenance enabling system achieves its intended use for its enabling functions.

> **注 9**：确认过程用于客观地确认维护使能系统针对其使能功能达到其预期用途。

b)Perform maintenance. This activity consists of the following tasks.

b) 执行维护。本活动由下列任务组成。

1)Monitor and review stakeholder requirements as well as incident and problem reports to identify future corrective, preventive, adaptive, additive, or perfective maintenance needs.

1) 监视并审查利益相关方要求以及事件和问题报告，以识别未来的纠正性、预防性、适应性、增加性或完善性维护需要。

> **NOTE 10** Anomalies, incidents, and problems resulting from system monitoring in the operation process are a major trigger for maintenance actions.

> **注 10**：由运行过程中的系统监视所产生的异常、事件和问题，是维护措施的主要触发因素。

2)Record maintenance incidents and problems and track their resolution.

2) 记录维护事件和问题并跟踪其解决。

> **NOTE 11** If an incident is experienced during maintenance, the maintenance staff records the incident and performs actions prescribed in validated maintenance procedures.

> **注 11**：如果在维护期间发生事件，维护人员记录该事件，并执行经确认的维护规程中规定的措施。

> **NOTE 12** Performing maintenance problem identification and resolution is handled through the quality assurance and project assessment and control processes.

> **注 12**：维护问题的识别与解决通过质量保证过程和项目评定与控制过程来处理。

3)Analyse the impact of changes introduced by maintenance actions on the system and system elements.

3) 分析维护措施所引入的更改对系统和系统元素的影响。

> **NOTE 13** Changes on the system and system elements can include data structures, data, related functionality, documentation, and interfaces.

> **注 13**：对系统和系统元素的更改能包括数据结构、数据、相关功能、文档和接口。

> **NOTE 14** Reviews and analyses often include factors such as the category of maintenance action; size of modification; cost involved; time to modify; and impacts on performance, safety, or security.

> **注 14**：审查和分析常常包括下列因素：维护措施的类别；修改的规模；涉及的成本；修改所需的时间；以及对性能、安全性或安全的影响。

4)Upon encountering faults that cause a system failure, restore the system to operational status.

4) 在遇到导致系统失效的故障时，将系统恢复到运行状态。

> **NOTE 15** Sometimes it is not possible to restore full operational status until the cause of the fault is corrected. In that case, the system is restored to a degraded mode consistent with the contingency planning.

> **注 15**：有时在故障原因得到纠正之前无法恢复完整的运行状态。在这种情况下，将系统恢复到与应急策划一致的降级模式。

> **NOTE 16** Typically, cyber security aspects are taken into account to reduce malicious threats to an acceptable level when restoring the system.

> **注 16**：通常，在恢复系统时会考虑网络安全方面，以将恶意威胁降低到可接受的水平。

5)Correct anomalies (defects, errors, and faults), replace, or upgrade system elements.

5) 纠正异常（缺陷、错误和故障），更换或升级系统元素。

> **NOTE 17** For random system failures, the fault is isolated down to the planned level of system element replacement, repair, revision, or reconfiguration. Then the corrective actions for the system element are performed and correct system performance is verified. Actions are recorded to estimate the useful life of degradable system elements.

> **注 17**：对于随机系统失效，将故障隔离到系统元素更换、修理、修订或重新配置的计划层级。然后执行针对该系统元素的纠正措施，并验证系统性能正确。记录各项措施，以估计性能会退化的系统元素的使用寿命。

6)Perform preventive maintenance by replacing, upgrading, or servicing system elements prior to failure.

6) 在失效之前通过更换、升级或保养系统元素来实施预防性维护。

7)Perform adaptive, additive, or perfective maintenance as required.

7) 按需执行适应性、增加性或完善性维护。

> **NOTE 18** Adaptive, additive, and perfective maintenance actions usually involve change to the system requirements, architecture, or design. It can be necessary to establish a new project to modify the existing system. If so, the portfolio management process can be the starting point to initiate the work in the development stage.

> **注 18**：适应性、增加性和完善性维护措施通常涉及对系统需求、架构或设计的更改。可能有必要设立新项目来修改现有系统。若如此，项目组合管理过程能作为在开发阶段启动该工作的起点。

c)Perform logistics support. This activity consists of the following tasks.

c) 执行后勤保障。本活动由下列任务组成。

> **NOTE 19** The logistics actions enable the system to sustain operational readiness. The actions include provisions for staffing, supply support, support equipment, technical data needs (user documentation) and agreed data rights, training support, communications, equipment/computing resource support, and facilities.

> **注 19**：后勤措施使系统能够维持运行就绪状态。这些措施包括下列各项安排：人员配备、供应保障、保障设备、技术数据需要（用户文档）和商定的数据权利、培训支持、通信、设备／计算资源保障以及设施。

1)Perform acquisition logistics.

1) 执行获取后勤。

> **NOTE 20** Acquisition logistics considers the supportability needs of the system concurrently with the definition of the system requirements. This includes performing analysis to determine whether it is more cost-effective to influence the initial design of the system or to plan for spare parts and repairs during utilization. This also includes validating the availability of suppliers for support and technology refresh over the intended life of the system, for the hardware and software selected. These decisions are often constrained by availability requirements and impact the supply chain management and commitments. Acquisition logistics considerations are included in the agreement resulting from the agreement processes. Supportability implications are also considered during the development stage.

> **注 20**：获取后勤在定义系统需求的同时考虑系统的保障性需要。这包括执行分析，以确定影响系统的初始设计与策划使用期间的备件和修理何者更具成本效益。这还包括针对所选硬件和软件，确认在系统的预期寿命内存在可提供支持和进行技术更新的供应方。这些决策常常受到可用性要求的约束，并影响供应链管理以及各项承诺。获取后勤的考虑事项纳入由协议过程产生的协议中。保障性影响也在开发阶段予以考虑。

2)Perform operational logistics.

2) 执行运行后勤。

> **NOTE 21** Operational logistics is the concurrent tuning of both the SoI and enabling systems throughout the operational life to help ensure effective and efficient delivery of system functions. It also includes taking the steps necessary to help ensure that the necessary material and resources, in the right quantity and quality, are available at the right place and time.

> **注 21**：运行后勤是在整个运行寿命期内对 SoI 和使能系统同时进行调优，以帮助确保有效且高效地交付系统功能。它还包括采取必要步骤，以帮助确保必要物资和资源以恰当的数量和质量在恰当的地点和时间可供使用。

3)Implement logistics actions needed during the life cycle.

3) 实施生存周期内所需的后勤措施。

> **NOTE 22** This typically includes packaging, handling, storage, transportation, installation, monitoring, and communications.

> **注 22**：这通常包括包装、装卸、贮存、运输、安装、监视和通信。

4)Confirm that logistics actions are implemented.

4) 确认后勤措施得到实施。

> **NOTE 23** Logistics actions can include satisfying the required replenishment levels so that stored system elements meet repair rates and planned schedules. This can include monitoring the quality and availability of spares, their transportation and their continued integrity during storage. Logistics actions can also include satisfying supportability requirements to achieve operational readiness. This can include staffing, supply, support equipment, technical data needs (manuals, instructions, lists, etc.), personnel and training, equipment/computing resources, and facilities.

> **注 23**：后勤措施能包括满足所需的补充水平，以使贮存的系统元素满足修理率和计划进度。这能包括监视备件的质量和可用性、其运输及其在贮存期间的持续完好性。后勤措施还能包括满足保障性要求以实现运行就绪状态。这能包括人员配备、供应、保障设备、技术数据需要（手册、说明书、清单等）、人员和培训、设备／计算资源以及设施。

d)Manage results of maintenance and logistics. This activity consists of the following tasks.

d) 管理维护与后勤的结果。本活动由下列任务组成。

1)Record maintenance and logistics results and any anomalies encountered.

1) 记录维护与后勤结果以及遇到的任何异常。

> **NOTE 24** This includes anomalies due to the maintenance strategy, the maintenance enabling systems, execution of the maintenance and logistics, or incorrect system definition. The project assessment and control process is used to analyse the data to identify the root cause; to enable corrective, preventive, adaptive, additive, or perfective actions; and to record lessons learned.

> **注 24**：这包括因维护策略、维护使能系统、维护与后勤的执行或错误的系统定义而产生的异常。项目评定与控制过程用于分析数据以识别根本原因；支持采取纠正性、预防性、适应性、增加性或完善性措施；并记录经验教训。

2)Record maintenance and logistics incidents and problems and track their resolution.

2) 记录维护与后勤的事件和问题并跟踪其解决。

> **NOTE 25** Performing problem resolution is handled through the quality assurance and project assessment and control processes. Any actual changes to the requirements, architecture, design, or system elements are done within other technical processes.

> **注 25**：问题解决的执行由质量保证过程以及项目评定与控制过程处理。对需求、架构、设计或系统元素的任何实际更改均在其他技术过程内完成。

3)Identify and record trends of incidents, problems, and maintenance and logistics actions.

3) 识别并记录事件、问题以及维护与后勤措施的趋势。

> **NOTE 26** This is used to inform operations and maintenance personnel, and other projects that are creating or utilizing similar system entities.

> **注 26**：这用于告知运行与维护人员，以及正在创建或使用类似系统实体的其他项目。

> **NOTE 27** Incident and problem reporting, including resulting action taken, is tracked through incident and process management activity of the quality assurance process (6.3.8.3).

> **注 27**：事件与问题报告（包括由此采取的措施）通过质量保证过程(6.3.8.3)的事件与过程管理活动加以跟踪。

4)Maintain traceability for maintenance and logistics.

4) 保持维护与后勤的追溯性。

> **NOTE 28** Bi-directional traceability is maintained between maintenance, logistics, system elements, and life cycle artefacts.

> **注 28**：在维护、后勤、系统元素与生存周期人工制品之间保持双向追溯性。

5)Provide key artefacts that have been selected for baselines.

5) 提供已选定用于基线的关键人工制品。

> **NOTE 29** The configuration management process is used to establish and maintain configuration items and baselines. The maintenance process identifies candidates for the baseline and then provides the artefacts to configuration management. Examples include maintenance plans and life cycle support plans.

> **注 29**：配置管理过程用于建立并保持配置项与基线。维护过程识别基线的候选者，随后将这些人工制品提供给配置管理。示例包括维护计划与生存周期保障计划。

6)Monitor customer satisfaction with the system, maintenance, and logistics.

6) 监视对系统、维护与后勤的顾客满意。

> **NOTE 30** The customer satisfaction data is used in the quality management process. ISO 10004 contains guidelines for monitoring and measuring customer satisfaction.

> **注 30**：顾客满意数据用于质量管理过程。ISO 10004 包含监视和测量顾客满意的指南。

##### 6.4.14 Disposal process 处置过程

###### 6.4.14.1 Purpose 目的

The purpose of the disposal process is to end the existence of a system element or system for a specified intended use, appropriately handle replaced or retired elements, appropriately handle any waste products, and to properly attend to identified critical disposal needs (e.g. per an agreement; per organizational policy; or for environmental, legal, safety, or security aspects).

处置过程的目的是：针对规定的预期用途终止系统元素或系统的存在，妥善处理被更换或退役的元素，妥善处理任何废弃物，并恰当应对已识别的关键处置需要（例如依据协议；依据组织方针；或出于环境、法律、安全性或安全方面的考虑）。

This process deactivates, disassembles, and removes the system or any of its system elements from the specific use. It addresses any waste products, consigning them to a final condition and returning the environment to its original or an acceptable condition. The waste products can be in-process resulting during any life cycle stage, e.g. waste materials during fabrication. This process destroys, stores, or reclaims system elements and waste products in an environmentally sound manner, in accordance with legislation, agreements, organizational constraints and stakeholder requirements. Disposal includes preventing expired, non-reusable, or inadequate elements from getting back into the supply chain. Where required, it maintains records in order that the health of operators and users, and the safety of the environment, can be monitored. When part of the system will continue to be in use in a modified form, the disposal process helps ensure the proper handling of the portion being disposed of.

本过程停用、拆解系统或其任何系统元素，并将其从特定用途中移除。它处理任何废弃物，使其归于最终状态，并使环境恢复到原始状态或可接受状态。废弃物可以是任何生存周期阶段中产生的过程性废弃物，例如制造过程中的废料。本过程按照法规、协议、组织约束与利益相关方要求，以环境无害的方式销毁、贮存或回收系统元素与废弃物。处置包括防止过期、不可复用或不合格的元素重新进入供应链。在需要时，本过程保持记录，以便能监视操作人员与使用者的健康以及环境的安全性。当系统的一部分将以改装形式继续使用时，处置过程帮助确保妥善处理被处置的那部分。

> **NOTE 1** The disposal process is intended to be applicable throughout the life cycle of the system, including disposing prototypes during the concept and development stages, dealing with waste during the production stage, decommissioning elements from modifications during the utilization and support stages, and ultimately removing the system from service during the retirement stage.

> **注 1**：处置过程预期适用于系统的整个生存周期，包括在概念与开发阶段处置原型，在生产阶段处理废弃物，在使用与保障阶段对因改装而退役的元素实施退役处理，以及最终在退役阶段将系统撤出服务。

> **NOTE 2** During the retirement stage, the disposal process can be used to dispose of the system at the end of its life or, if the system is still useful, to manage the transition from its current life cycle to a new life cycle, whether in a different part of the organization or to a different organization.

> **注 2**：在退役阶段，处置过程能用于在系统寿命终结时处置该系统；或者，如果系统仍然有用，则用于管理其从当前生存周期向新的生存周期的转换，无论是在组织内的另一部分，还是移交给另一组织。

###### 6.4.14.2 Outcomes 预期结果

As a result of the successful performance of the disposal process:

作为处置过程成功执行的结果：

a) disposal constraints are provided as inputs to requirements, architecture, design, and implementation;

a) 处置约束作为对需求、架构、设计和实施的输入予以提供；

b) enabling systems or services needed for disposal are available;

b) 处置所需的使能系统或服务可供使用；

c) the system elements or waste products are destroyed, stored, reclaimed, or recycled in accordance with safety and security requirements;

c) 系统元素或废弃物按照安全性要求与安全要求被销毁、贮存、回收或再循环；

d) the environment is returned to its original or an agreed state;

d) 环境恢复到其原始状态或约定的状态；

e) records of disposal actions and analysis are available.

e) 处置措施与分析的记录可供使用。

###### 6.4.14.3 Activities and tasks 活动与任务

The following activities and tasks shall be implemented in accordance with applicable organization policies and procedures with respect to the disposal process.

组织应按照适用的组织方针和程序，针对处置过程实施下列活动与任务。

a)Prepare for disposal. This activity consists of the following tasks.

a) 准备处置。本活动由下列任务组成。

1)Define a disposal strategy for the system, to include each system element and any resulting waste products.

1) 为系统确定处置策略，包括每个系统元素以及由此产生的任何废弃物。

> **NOTE 1** This defines schedules, actions and resources that:

> **注 1**：这确定了时间表、措施与资源，用以：

a) permanently terminate the system's functions and delivery of services;

a) 永久终止系统的功能与服务提供；

b) transform the system into, or retain it in, a socially and physically acceptable state, thereby avoiding subsequent adverse effects on stakeholders, society and the environment;

b) 将系统转换为、或使其保持在社会与物理上可接受的状态，从而避免对利益相关方、社会与环境产生后续不利影响；

c) take account of the health, safety, security and privacy applicable to disposal actions and to the long-term condition of resulting physical material and information;

c) 考虑适用于处置措施、并适用于所产生的物理材料与信息长期状况的健康、安全性、安全与隐私；

d) considers transition of the system for future use in modified or adapted form, including legacy migration.

d) 考虑系统以改装或适配形式供未来使用的转换，包括遗留系统迁移。

2)Identify constraints and objectives from disposal on the system requirements, architecture and design characteristics, or implementation techniques.

2) 从处置出发，识别对系统需求、架构与设计特性或实施技术的约束与目标。

> **NOTE 2** This includes issues of disassembly, including their associated enabling systems, access to and availability of storage locations, and available skill levels.

> **注 2**：这包括拆解问题，含其相关联的使能系统、贮存场所的可达性与可用性，以及可获得的技能水平。

3)Identify and plan for the necessary enabling systems or services needed to support disposal.

3) 识别并规划支持处置所需的必要使能系统或服务。

> **NOTE 3** This includes identification of requirements and interfaces for the enabling systems.

> **注 3**：这包括识别使能系统的要求与接口。

4)Obtain or acquire access to the enabling systems or services to be used.

4) 获得或取得对将要使用的使能系统或服务的访问权。

> **NOTE 4** The validation process is used to objectively confirm that the disposal enabling system achieves its intended use for its enabling functions.

> **注 4**：确认过程用于客观确认处置使能系统就其使能功能达成其预期用途。

5)Specify containment facilities, storage locations, inspection criteria, and storage periods, if the system is to be stored.

5) 如果系统将被贮存，则规定围护设施、贮存场所、检查准则与贮存期限。

6)Define preventive methods to preclude disposed elements and materials that should not be repurposed, reclaimed, or reused from re-entering the supply chain.

6) 确定预防方法，以防止不应被改作他用、回收或复用的已处置元素与材料重新进入供应链。

b)Perform disposal. This activity consists of the following tasks.

b) 实施处置。本活动由下列任务组成。

1)Deactivate the system or system element to prepare it for removal.

1) 停用系统或系统元素，以备移除。

> **NOTE 5** Interfaces to other systems are considered, for example, power or fuel are disconnected in accordance with disassembly instructions, taking into account relevant health, safety, security and privacy legislation. When the SoI is being modified for technology or capability upgrades, only the impacted system elements are deactivated and removed. This can apply to a prototype of the SoI during the concept or development stage.

> **注 5**：考虑与其他系统的接口，例如，按照拆解说明断开电力或燃料，同时考虑相关的健康、安全性、安全与隐私法规。当 SoI 因技术或能力升级而被改装时，只停用并移除受影响的系统元素。这能适用于概念阶段或开发阶段的 SoI 原型。

2)Remove the system, system element, or waste material from use or production for appropriate disposition and action.

2) 将系统、系统元素或废料从使用或生产中移除，以进行适当处置并采取相应措施。

> **NOTE 6** The disposition includes reuse, recycling, reconditioning, overhaul, destruction, or transition to another life cycle. It is presupposed that the disposition and subsequent actions are conducted in accordance with relevant safety, security, privacy, and environmental standards, directives, and laws. Elements of the system that have useful life remaining, either in their current condition or following overhaul or modification, are transferred to other systems-of-interest or to a life cycle in another organization. Where appropriate, system elements are reconditioned to extend their useful life. Services and subscriptions, including cloud-based assets are released or halted. Operators are reallocated, redeployed, or retired. This task includes the removal of waste material from production or other stages.

> **注 6**：处置包括复用、再循环、修复、大修、销毁或转换到另一生存周期。前提是处置及后续措施按照相关的安全性、安全、隐私与环境标准、指令和法律实施。对于仍有剩余使用寿命的系统元素——无论是处于当前状态，还是在经过大修或改装之后——将其移交给其他所关注系统或另一组织中的生存周期。在适当情况下，对系统元素进行修复以延长其使用寿命。服务与订阅（包括基于云的资产）被释放或停止。操作人员被重新调配、重新部署或退职。本任务包括从生产或其他阶段移除废料。

3)Withdraw impacted operating staff from the system or system element and record relevant operating knowledge.

3) 使受影响的运行人员退出系统或系统元素，并记录相关的运行知识。

> **NOTE 7** This is conducted in accordance with relevant safety, security, privacy, and environmental standards, directives, and laws. Action is performed to safeguard and secure knowledge and skills possessed by operators. It can be related to knowledge management process.

> **注 7**：这按照相关的安全性、安全、隐私与环境标准、指令和法律实施。采取措施以保护和保全操作人员所拥有的知识与技能。这能与知识管理过程相关。

4)Disassemble the system or system element into manageable elements to facilitate its removal for reuse, recycling, reconditioning, overhaul, archiving, or destruction.

4) 将系统或系统元素拆解为可管理的元素，以便于将其移除以供复用、再循环、修复、大修、归档或销毁。

5)Handle system elements and their parts that are not intended for reuse in a manner that will help ensure they do not get back into the supply chain.

5) 处理不拟复用的系统元素及其零件，处理方式应有助于确保它们不会重新进入供应链。

6)Conduct destruction of the system elements, as necessary, to reduce the amount of waste treatment or to make the waste easier to handle.

6) 必要时销毁系统元素，以减少废弃物处理量或使废弃物更易于处理。

> **NOTE 8** This activity includes obtaining the destruction services required to melt, crush, incinerate, demolish, or eradicate the system or its elements as necessary.

> **注 8**：本活动包括获取必要的销毁服务，以按需熔化、压碎、焚烧、拆除或消灭系统或其元素。

c)Finalise the disposal. This activity consists of the following tasks.

c) 完成处置。本活动由下列任务组成。

1)Confirm that no detrimental health, safety, security, and environmental factors exist following disposal.

1) 确认处置之后不存在对健康、安全性、安全与环境有害的因素。

2)Return the environment to its original state or to a state that is specified by agreement.

2) 使环境恢复到其原始状态或协议规定的状态。

3)Identify and record information about the disposed system or system element.

3) 识别并记录关于已处置系统或系统元素的信息。

> **NOTE 9** Information includes disposal records gathered through the lifetime of the system to permit audits and reviews in the event of long-term hazards to health, safety, security, and the environment; to maintain knowledge of disposal logistics (method and location); and to permit future system creators and users to build a knowledge base from experiences. This information provides traceability of disposal.

> **注 9**：信息包括在系统整个寿命期内收集的处置记录，以便在出现对健康、安全性、安全与环境的长期危害时能够进行审核与评审；保持对处置后勤（方法与地点）的了解；并使未来的系统创建者与使用者能够从经验中构建知识库。该信息提供处置的追溯性。

4)Provide key artefacts that have been selected for baselines.

4) 提供已选定用于基线的关键人工制品。

> **NOTE 10** The configuration management process is used to establish and maintain configuration items and baselines. The disposal process identifies candidates for the baseline and then provides the artefacts to configuration management. Examples include disposal plans and records.

> **注 10**：配置管理过程用于建立并保持配置项与基线。处置过程识别基线的候选者，随后将这些人工制品提供给配置管理。示例包括处置计划与记录。

## Annex A (normative) — Tailoring process ｜ 附录 A（规范性）——裁剪过程

### A.1 General 总则

This annex provides requirements for the tailoring of the processes included in this document.

本附录给出对本文件所含过程进行裁剪的要求。

> **NOTE 1** Tailoring is not a requirement for conformance to this document. In fact, tailoring is not permitted if a claim of "full conformance" is to be made. If a claim of "tailored conformance" is made, then this process is applied to perform the tailoring.

> **注 1**：裁剪不是符合本文件的一项要求。事实上，如果拟作出“完全符合”的声明，则不允许裁剪。如果作出“裁剪符合”的声明，则应用本过程来执行裁剪。

> **NOTE 2** Additional guidance for tailoring can be found in the ISO/IEC/IEEE 24748-1 and ISO/IEC/IEEE 24748-2, which provide guidelines on the application of life cycle processes.

> **注 2**：关于裁剪的附加指南见 ISO/IEC/IEEE 24748-1 与 ISO/IEC/IEEE 24748-2，它们给出了生存周期过程应用的指南。

### A.2 Tailoring process 裁剪过程

#### A.2.1 Purpose 目的

The purpose of the tailoring process is to adapt the life cycle processes included in this document to satisfy particular circumstances or factors that:

裁剪过程的目的是：使本文件所含的生存周期过程适应于满足以下特定情况或因素：

a) surround an organization that is employing this document in an agreement;

a) 围绕在协议中使用本文件的组织的情况或因素；

b) influence a project that is required to meet an agreement in which this document is referenced;

b) 影响需要满足引用本文件的协议的项目的因素；

c) reflect the needs of an organization to supply products or services.

c) 反映组织提供产品或服务之需要的因素。

#### A.2.2 Outcomes 预期结果

As a result of the successful performance of the tailoring process:

作为裁剪过程成功执行的结果：

a) modified or new life cycle processes are defined to achieve the purposes and outcomes of a life cycle model.

a) 定义修改后的或新的生存周期过程，以实现生存周期模型的目的与预期结果。

#### A.2.3 Activities and tasks 活动与任务

If the life cycle processes included in this document are tailored, then the organization or project shall implement the following tasks in accordance with applicable policies and procedures with respect to the tailoring process, as required.

如果对本文件所含的生存周期过程进行裁剪，则组织或项目应视需要，按照适用的方针和程序，针对裁剪过程实施下列任务。

a) Identify and record the circumstances that influence tailoring. These influences include, but are not limited to:

a) 识别并记录影响裁剪的情况。这些影响包括但不限于：

1) stability of, and variety in, operational environments;

1) 运行环境的稳定性与多样性；

2) risks, commercial or performance, to the concern of stakeholders;

2) 利益相关方所关注的商业风险或性能风险；

3) novelty, size, and complexity;

3) 新颖性、规模与复杂性；

4) starting date and duration of utilization;

4) 使用的起始日期与持续时间；

5) integrity issues such as safety, security, privacy, usability, availability;

5) 安全性、安全、隐私、易用性、可用性等完整性问题；

6) emerging technology opportunities;

6) 新兴技术机会；

7) profile of budget and organizational resources available;

7) 可获得的预算与组织资源的概况；

8) availability of the services of enabling systems;

8) 使能系统所提供服务的可获得性；

9) roles, responsibilities, accountabilities, and authorities in the overall life cycle of the system;

9) 系统整个生存周期中的角色、职责、问责与职权；

10) the need to conform to other standards.

10) 需要符合其他标准。

b) In the case of properties critical to the system, take due account of the life cycle structures recommended or mandated by standards relevant to the dimension of the criticality.

b) 对于系统所至关重要的特性，适当考虑由与关键性维度相关的标准所推荐或强制要求的生存周期结构。

c) Obtain input from parties affected by the tailoring decisions. This includes, but may not be limited to:

c) 获取受裁剪决策影响的各方的输入。这包括但不限于：

1) the system stakeholders;

1) 系统利益相关方；

2) the interested parties to an agreement made by the organization;

2) 组织所订立协议的各相关方；

3) the contributing organizational functions.

3) 做出贡献的组织职能。

d) Make tailoring decisions in accordance with the decision management process to achieve the purposes and outcomes of the selected life cycle model.

d) 按照决策管理过程作出裁剪决策，以实现所选生存周期模型的目的与预期结果。

> **NOTE 1** Organizations establish standard life cycle models as a part of the life cycle model management process. It is sometimes appropriate for an organization to tailor processes of this document to achieve the purposes and outcomes of the stages of a life cycle model to be established.

> **注 1**：组织作为生存周期模型管理过程的一部分建立标准生存周期模型。有时，组织适宜裁剪本文件的过程，以实现拟建立的生存周期模型各阶段的目的与预期结果。

> **NOTE 2** Projects select an organizationally-established life cycle model for the project as a part of the project planning process. It is sometimes appropriate to tailor organizationally adopted processes to achieve the purposes and outcomes of the stages of the selected life cycle model.

> **注 2**：项目作为项目规划过程的一部分为项目选择组织已建立的生存周期模型。有时，适宜裁剪组织所采用的过程，以实现所选生存周期模型各阶段的目的与预期结果。

> **NOTE 3** In cases where projects are directly applying this document, it is sometimes appropriate to tailor processes of this document to achieve the purposes and outcomes of the stages of a suitable life cycle model.

> **注 3**：在项目直接应用本文件的情况下，有时适宜裁剪本文件的过程，以实现合适的生存周期模型各阶段的目的与预期结果。

e) Select the life cycle processes that require tailoring and delete selected outcomes, activities, or tasks.

e) 选择需要裁剪的生存周期过程，并删除所选定的预期结果、活动或任务。

> **NOTE 4** Irrespective of tailoring, organizations and projects are always permitted to implement processes that achieve additional outcomes or implement additional activities and tasks beyond those required for conformance to this document.

> **注 4**：无论是否裁剪，始终允许组织与项目实施能够实现附加预期结果的过程，或实施超出符合本文件所需的附加活动与任务。

> **NOTE 5** An organization or project sometimes encounter a situation where there is the desire to modify a provision of this document. Because of unanticipated consequences on other processes, outcomes, activities or tasks, such modifications are generally avoided. If necessary, modification is performed by deleting the provision (making the appropriate claim of tailored conformance) and, with careful consideration of consequences, implementing a process that achieves additional outcomes or performs additional activities and tasks beyond those of the tailored standard.

> **注 5**：组织或项目有时会遇到希望修改本文件某项规定的情形。由于对其他过程、预期结果、活动或任务可能产生非预期后果，此类修改通常予以避免。必要时，修改通过以下方式进行：删除该规定（作出相应的裁剪符合性声明），并在仔细考虑后果之后，实施能够实现超出经裁剪标准的附加预期结果或执行附加活动与任务的过程。

## Annex B (informative) — Example process artefacts and information items ｜ 附录 B（资料性）——过程人工制品与信息部件示例

Table B.1 provides a possible set of work products, including artefacts and information items, associated with each process. This list is not all-inclusive: for each process, an organization may decide to develop a policy, plan, procedures, reports, and records to demonstrate the outcomes or perform the activities and tasks. Where less intensive documentation is considered sufficient, information items can be combined. Also, the organizational policies and procedures can be applied or tailored for each process and project. Typical titles are shown, including common examples of alternate titles and details in parentheses. An artefact is any kind of work product and includes information items. Information items represent an identifiable body of information for human use to communicate to stakeholders.

表 B.1 给出了与每个过程相关联的一组可能的工作产品，包括人工制品与信息部件。该清单并非无所不包：对于每个过程，组织可决定制定方针、计划、程序、报告与记录，以证实预期结果或执行活动与任务。在认为较少文档即已足够的情况下，能合并信息部件。此外，组织方针与程序能针对每个过程和项目加以应用或裁剪。表中给出典型标题，包括常见替代标题示例以及括号内的细节。人工制品是任何种类的工作产品，包括信息部件。信息部件表示可识别的一组信息，供人使用以与利益相关方沟通。

> **NOTE 1** ISO/IEC/IEEE 15289 provides information on content and management of information items.

> **注 1**：ISO/IEC/IEEE 15289 给出了关于信息部件内容与管理的信息。

> **NOTE 2** Every process has a strategy, whether or not it is documented. When it is documented, then it would be an artefact.

> **注 2**：每个过程都有策略，无论其是否形成文件。当策略形成文件时，它便是一项人工制品。

**Table B.1 — Sample artefacts and information items by process**

**表 B.1 — 各过程的人工制品与信息部件示例**

| Process Process group ／ 过程 过程组 | Typical title ／ 典型标题 |
| --- | --- |
| Agreement processes ／ 协议过程 |  |

**Acquisition process**

**获取过程**

Request for supply (request for proposal, request for tender)Info item

供应请求（征求建议书、征求投标书）信息部件

Agreement (contract)Info item

协议（合同）信息部件

Info item

信息部件

Acquisition records and reports (acquisition approach, agreement changes, supplier selection report, supply acceptance, delivery acceptance)

获取记录与报告（获取途径、协议更改、供应方选择报告、供应验收、交付验收）

**Supply process**

**供应过程**

Supply response (proposal, tender)Info item

供应响应（建议书、投标书）信息部件

Agreement (contract)Info item

协议（合同）信息部件

Info item

信息部件

Supply records and reports (supply approach, system and element delivery records, change requests)

供应记录与报告（供应途径、系统与元素交付记录、更改请求）

**Organizational project-enabling processes**

**组织项目使能过程**

**Life cycle model management process**

**生存周期模型管理过程**

Life cycle management policies and proceduresInfo item

生存周期管理方针与程序信息部件

Authorised life cycle models and processesArtefact

经批准的生存周期模型与过程人工制品

Info item

信息部件

Life cycle model management records and reports (model and process assessment, improvement)

生存周期模型管理记录与报告（模型与过程评定、改进）

**Infrastructure management process**

**基础设施管理过程**

Infrastructure elementsArtefact

基础设施元素人工制品

Info item

信息部件

Infrastructure records and reports (requirements for infrastructure, change requests, descriptions)

基础设施记录与报告（对基础设施的要求、更改请求、描述）

**Portfolio management process**

**项目组合管理过程**

Project portfolioArtefact

项目组合人工制品

Project authorizationArtefact

项目授权人工制品

Project closure reportInfo item

项目收尾报告信息部件

**Table B.1** *(continued)***Table B.1** *(continued)*

**表 B.1** *(续)***表 B.1** *(续)*

**ProcessTypical titleType**

**过程典型标题类型**

**Process** **group**

**过程** **组**

Info item

信息部件

Portfolio management records and reports (portfolio analysis, evaluations, project direction)

项目组合管理记录与报告（项目组合分析、评估、项目指导）

**Human resource management process**

**人力资源管理过程**

Skill development assets (training materials)Info item

技能开发资产（培训材料）信息部件

Info item

信息部件

Human resource records and reports (skill needs, skill inventory, training records, staff assignments)

人力资源记录与报告（技能需要、技能清单、培训记录、人员分派）

**Quality management process**

**质量管理过程**

Quality management policies and proceduresInfo item

质量管理方针与程序信息部件

Info item

信息部件

Quality management records and reports (criteria and methods, assessment results, corrective and preventive action report)

质量管理记录与报告（准则与方法、评定结果、纠正与预防措施报告）

**Knowledge management process**

**知识管理过程**

Knowledge management elements (assets)Artefact

知识管理元素（资产）人工制品

Knowledge asset records and reportsInfo item

知识资产记录与报告信息部件

**Technical management processes**

**技术管理过程**

**Project planning process**

**项目规划过程**

Project plans (management, technical, and process specific)Info item

项目计划（管理、技术与过程专用）信息部件

Project life cycle model (tailored)Artefact

项目生存周期模型（经裁剪）人工制品

Breakdown structureArtefact

分解结构人工制品

Resource requestInfo item

资源请求信息部件

Info item

信息部件

Project planning records and reports (objectives, constraints, schedules, budgets)

项目规划记录与报告（目标、约束、进度、预算）

**Project assessment and control process**

**项目评定与控制过程**

Authorization to proceed to next milestone (record)Info item

进入下一里程碑的授权（记录）信息部件

Change requestsInfo item

更改请求信息部件

Info item

信息部件

Project assessment and control records and reports (project performance data, project control requests, meeting minutes, reviews, status, variances, corrective actions)

项目评定与控制记录与报告（项目绩效数据、项目控制请求、会议纪要、评审、状态、偏差、纠正措施）

**Decision management process**

**决策管理过程**

Decision registerArtefact

决策登记册人工制品

Info item

信息部件

Decision records and reports (decision requests, trade-off analysis)

决策记录与报告（决策请求、权衡分析）

**Risk management process**

**风险管理过程**

Risk registerArtefact

风险登记册人工制品

Risk records and reports (profiles)Info item

风险记录与报告（风险概况）信息部件

**Configuration management process**

**配置管理过程**

Configuration baselinesArtefact

配置基线人工制品

Info item

信息部件

Configuration management records (variances, change requests, changes)

配置管理记录（偏差、更改请求、更改）

Info item

信息部件

Configuration management reports (status, evaluation, audit, results, release)

配置管理报告（状态、评估、审核、结果、发布）

**Information management process**

**信息管理过程**

Information item registerArtefact

信息部件登记册人工制品

Information management records and reportsInfo item

信息管理记录与报告信息部件

**Measurement process**

**测量过程**

Measurement registerArtefact

测量登记册人工制品

**Table B.1** *(continued)***Table B.1** *(continued)*

**表 B.1** *(续)***表 B.1** *(续)*

**ProcessTypical titleType**

**过程典型标题类型**

**Process** **group**

**过程** **组**

Info item

信息部件

Measurement records and reports (information need, evaluation)

测量记录与报告（信息需要、评估）

**Quality assurance process**

**质量保证过程**

Incident records and reportsInfo item

事件记录与报告信息部件

Problem records and reportsInfo item

问题记录与报告信息部件

Info item

信息部件

Quality assurance records and reports (criteria and methods, evaluations, corrective actions)

质量保证记录与报告（准则与方法、评估、纠正措施）

**Technical processes**

**技术过程**

**General (applies to all technical processes)**

**通用（适用于所有技术过程）**

Requirements for enabling systems (records)Artefact

对使能系统的要求（记录）人工制品

Traceability mappingArtefact

追溯性映射人工制品

**Business or mission analysis process**

**业务或任务分析过程**

Life cycle conceptsInfo item

生存周期概念信息部件

Problem or opportunity statementArtefact

问题或机会陈述人工制品

Solution alternatives (with preliminary operational concepts)Artefact

备选解（含初步运行概念）人工制品

Info item

信息部件

Business or mission analysis reports (solution alternatives analysis and recommendations)

业务或任务分析报告（备选解分析与建议）

**Stakeholder needs and requirements definition process**

**利益相关方需要与需求定义过程**

Info item

信息部件

System life cycle concepts (operational, acquisition, support, deployment, security, etc.)

系统生存周期概念（运行、获取、保障、部署、安全等）

Info item

信息部件

Stakeholder needs (critical performance needs, product need assessment)

利益相关方需要（关键性能需要、产品需要评定）

Stakeholder needs and requirementsArtefact

利益相关方需要与需求人工制品

Info item

信息部件

Stakeholder needs and requirements reports (identification of stakeholders and requirements)

利益相关方需要与需求报告（利益相关方与需求的识别）

**System requirements definition process**

**系统需求定义过程**

System requirementsArtefact

系统需求人工制品

Requirements records (system, system element)Info item

需求记录（系统、系统元素）信息部件

System requirements reports (definitions, rationale, changes)Info item

系统需求报告（定义、理由、更改）信息部件

**System architecture definition process**

**系统架构定义过程**

Architecture views, viewpoints, and modelsArtefact

架构视图、架构视角与模型人工制品

Interface definition (initial)Artefact

接口定义（初始）人工制品

Architecture descriptionArtefact

架构描述人工制品

Architecture reports (assessments, rationales)Info item

架构报告（评定、理由）信息部件

**Design definition process**

**设计定义过程**

Design baselines (design characteristics)Artefact

设计基线（设计特性）人工制品

Design descriptionsArtefact

设计描述人工制品

Interface definitionArtefact

接口定义人工制品

Design reports (design evaluations, rationales)Info item

设计报告（设计评估、理由）信息部件

**System analysis process**

**系统分析过程**

System analysis modelsArtefact

系统分析模型人工制品

Info item

信息部件

System analysis records and reports (evaluations, results, recommendations)

系统分析记录与报告（评估、结果、建议）

**Implementation process**

**实现过程**

System elementsArtefact

系统元素人工制品

**Table B.1** *(continued)***Table B.1** *(continued)*

**表 B.1** *(续)***表 B.1** *(续)*

**ProcessTypical titleType**

**过程典型标题类型**

**Process** **group**

**过程** **组**

Info item

信息部件

Implementation records and reports (constraints on solution, unit test results)

实现记录与报告（对解的约束、单元测试结果）

**Integration process**

**集成过程**

Integrated system elementsArtefact

集成后的系统元素人工制品

Interface control descriptionArtefact

接口控制描述人工制品

Integration records and reports (discrepancies)Info item

集成记录与报告（差异）信息部件

**Verification process**

**验证过程**

Verified systemArtefact

经验证的系统人工制品

Info item

信息部件

Verification records and reports (approach, criteria, results, discrepancies)

验证记录与报告（途径、准则、结果、差异）

**Transition process**

**转换过程**

Prepared target environment (operational site)Artefact

已准备好的目标环境（运行现场）人工制品

Transitioned system/elementArtefact

已转换的系统／元素人工制品

Info item

信息部件

Transition records and reports (approach, constraints, discrepancies, installation, release approach, contingency/backout approach)

转换记录与报告（途径、约束、差异、安装、发布途径、应急／回退途径）

**Validation process**

**确认过程**

Validated systemArtefact

经确认的系统人工制品

Info item

信息部件

Validation records and reports (approach, constraints, discrepancies)

确认记录与报告（途径、约束、差异）

**Operation process**

**运行过程**

Info item

信息部件

Operation procedures (user documentation, information for users, continuity procedures, security procedures)

运行程序（用户文档、供用户使用的信息、连续性程序、安全程序）

Customer support records (requests, problem reports)Info item

顾客支持记录（请求、问题报告）信息部件

Info item

信息部件

Operation records and reports (approach, constraints, discrepancies, monitoring, evaluation, customer satisfaction))

运行记录与报告（途径、约束、差异、监视、评估、顾客满意）

**Maintenance process**

**维护过程**

Replacement system elementsArtefact

更换用系统元素人工制品

Info item

信息部件

Maintenance/logistics records and reports (approach, constraints, maintenance/supply requests, discrepancies)

维护／后勤记录与报告（途径、约束、维护／供应请求、差异）

**Disposal process**

**处置过程**

Disposed/archived systems and elementsArtefact

已处置／已归档的系统与元素人工制品

Info item

信息部件

Disposal/archive records and reports (approach, constraints, outcomes)

处置／归档记录与报告（途径、约束、预期结果）

## Annex C (informative) — Process reference model for assessment purposes ｜ 附录 C（资料性）——用于评定目的的过程参考模型

### C.1 General 总则

It is understood that some users of this document desire to assess the implemented processes in accordance with ISO/IEC 33004:2015. This annex provides a process reference model suitable for use in conjunction with ISO/IEC 33004:2015.

可以理解，本文件的一些使用者希望按照 ISO/IEC 33004:2015 评定所实施的过程。本附录给出一个适合与 ISO/IEC 33004:2015 结合使用的过程参考模型。

The process reference model is composed of the processes in the body of this document, including the name, statement of purpose, and statement of outcomes for each process. Clause C.3 identifies the processes in the process reference model and the clauses in which they are defined.

过程参考模型由本文件正文中的各过程组成，其中包括每个过程的名称、目的陈述和预期结果陈述。C.3 标识了过程参考模型中的各过程及其定义所在的条款。

### C.2 Conformance with ISO/IEC 33004 与 ISO/IEC 33004 的符合性

#### C.2.1 General 总则

ISO/IEC 33004:2015, 5.3 places requirements on process reference models suitable for assessment by that document. Table C.1 and C.2.3 quote the requirements for process reference models and describe how these are met by this document.

ISO/IEC 33004:2015 的 5.3 对适用于按该文件评定的过程参考模型提出了要求。表 C.1 和 C.2.3 引述了对过程参考模型的要求，并描述了本文件如何满足这些要求。

#### C.2.2 Requirements for process reference models 对过程参考模型的要求

**Table C.1 — Implementation of requirements for process reference models in ISO/IEC 33004**

**表 C.1 — ISO/IEC 33004 中过程参考模型要求的实施**

| Process reference model requirements (see ISO/IEC 33004:2015, 5.3.1) ／ 过程参考模型要求（见 ISO/IEC 33004:2015, 5.3.1） | ISO/IEC/IEEE 15288 implementation ／ ISO/IEC/IEEE 15288 的实施 |
| --- | --- |
| a) Declaration of domain ／ a) 领域的声明 | This is provided in Clause 1. ／ 这由第 1 章给出。 |
| b) Description of relationship between the process reference model and context of use. ／ b) 对过程参考模型与使用语境之间关系的描述。 | This is provided by Clause 5. ／ 这由第 5 章给出。 |
| c) Description of processes ／ c) 对过程的描述 | This is provided in Clause C.3. ／ 这由 C.3 给出。 |
| d) Description of relationship between processes ／ d) 对过程之间关系的描述 | This is provided in Clause C.3 in the description of each process. For example, some process descriptions include the statement that the process contains lower-level processes. ／ 这由 C.3 中每个过程的描述给出。例如，一些过程描述包括该过程包含较低层级过程的陈述。 |
| Process reference model community of interest and consensus (see ISO/IEC 33004:2015, 5.3.2) ／ 过程参考模型的利益共同体与共识（见 ISO/IEC 33004:2015, 5.3.2） |  |
| a) Characterization of community of interest ／ a) 对利益共同体的表征 | The relevant community of interest is the users of this document and ISO/IEC/IEEE 12207. ／ 相关的利益共同体是本文件和 ISO/IEC/IEEE 12207 的使用者。 |
| b) Achievement of consensus ／ b) 共识的达成 | Both this document and ISO/IEC/IEEE 12207 are International Standards satisfying the consensus requirements of ISO, IEC and IEEE. ／ 本文件和 ISO/IEC/IEEE 12207 都是满足 ISO、IEC 和 IEEE 共识要求的国际标准。 |
| c) If no action taken to achieve consensus, action documented ／ c) 若未采取行动达成共识，则记录所采取的行动 | Not applicable ／ 不适用 |
| Unique process descriptions (see ISO/IEC 33004:2015, 5.3.3) ／ 唯一的过程描述（见 ISO/IEC 33004:2015, 5.3.3） | The process descriptions are unique. The process descriptions are per the requirements of ISO/IEC/IEEE 24774. ／ 过程描述是唯一的。过程描述符合 ISO/IEC/IEEE 24774 的要求。 |

#### C.2.3 Process descriptions 过程描述

ISO/IEC 33004:2015, 5.4 identifies the following requirements for a process description:

ISO/IEC 33004:2015 的 5.4 标识了对过程描述的下列要求：

a) a process is described in terms of its purpose and process outcomes;

a) 过程按其目的和过程预期结果加以描述；

b) the set of process outcomes is necessary and sufficient to achieve the purpose of the process;

b) 过程预期结果集对实现该过程的目的而言必要且充分；

c) process descriptions do not contain or imply aspects of the process quality characteristic beyond the basic level of any relevant process measurement framework conformant with ISO/IEC 33003.

c) 过程描述不包含也不隐含超出任何符合 ISO/IEC 33003 的相关过程测量框架基本层级的过程质量特性内容。

Process outcomes include:

过程预期结果包括：

- production of an artefact;

- 人工制品的产生；

- a significant change of state;

- 状态的显著变化；

- meeting of specified constraints, e.g. requirements, goals, and objectives.

- 满足规定约束，例如需求、目标和目的。

These requirements are met by the process descriptions in Clause 6. Some outcomes can be interpreted as contributing to levels of capability above level 1. However, conforming implementation of the relevant processes does not require achievement of these higher levels of capability.

第 6 章中的过程描述满足了这些要求。一些预期结果能解释为对高于等级 1 的能力等级的贡献。然而，相关过程的合规实施并不要求达到这些更高的能力等级。

### C.3 The process reference model 过程参考模型

The process reference model is composed of the statement of purpose and outcomes of each of the processes included in Clause 6. The process reference model for the system life cycle is composed of the set of processes in Figure 4.

过程参考模型由第 6 章所含每个过程的目的陈述和预期结果陈述组成。系统生存周期的过程参考模型由图 4 中的过程集合组成。

## Annex D (informative) — Model-based systems and software engineering (MBSSE) ｜ 附录 D（资料性）— 基于模型的系统与软件工程（MBSSE）

### D.1 MBSE description MBSE 描述

MBSE is the formalised application of modelling to support systems engineering throughout the whole life cycle of an SoI.

MBSE 是建模的形式化应用，用以在 SoI 的整个生存周期内支持系统工程。

Typically, there is a need to address both systems and software engineering in a digital environment. Consequently, the scope and content of this annex includes both MBSE and MBSSE.

通常需要在数字环境中同时处理系统工程与软件工程。因此，本附录的范围和内容同时涵盖 MBSE 和 MBSSE。

### D.2 Implementation of system life cycle processes in an MBSE approach 以 MBSE 途径实施系统生存周期过程

This document provides a common process reference model for the engineering of systems. This document provides a comprehensive set of processes from which an organization can develop system life cycle models appropriate to its products; services; and the framework for development, assessment, support, and improvement of the life cycle processes.

本文件为系统的工程化提供通用的过程参考模型。本文件提供一套全面的过程，组织可据以制定适合其产品和服务的系统生存周期模型，以及用于生存周期过程开发、评定、支持和改进的框架。

Execution of these life cycle processes can be greatly facilitated through the adoption of MBSE. ISO/IEC/IEEE 24641 specifies a reference framework for systems and software engineering with a model-based approach. In this approach, the systems engineering activities rely on evolving models that serve as the “main or major source of knowledge” about the SoI and its life cycle processes.

通过采用 MBSE 能极大促进这些生存周期过程的执行。ISO/IEC/IEEE 24641 规定了采用基于模型途径开展系统与软件工程的参考框架。在该途径中，系统工程活动依赖不断演化的模型，这些模型充当关于 SoI 及其生存周期过程的“主要或重要知识来源”。

The set of system life cycle processes included in this document and their relationships to the supporting ISO/IEC/IEEE 24641 reference framework, as model-based supporting activities, are included in ISO/IEC/IEEE 24641:2023, Annex A and Annex E. MBSE adoption and application often includes a set of milestones of capabilities and maturity enhancement for those practicing MBSE. As an example, see Reference [58].

本文件所含的系统生存周期过程集合，以及它们作为基于模型的支持活动而与起支撑作用的 ISO/IEC/IEEE 24641 参考框架之间的关系，见 ISO/IEC/IEEE 24641:2023 的附录 A 和附录 E。MBSE 的采用和应用往往还包括一组面向 MBSE 实践者的能力与成熟度提升里程碑。示例见参考文献 [58]。

### D.3 MBSE as a practice 作为实践的 MBSE

MBSE utilises modelling environments to express engineering data as models in the execution of the processes detailed in the systems engineering framework elicited in the processes and relationships covered in 5.7 through 5.9. In addition to integrating concepts, requirements, architecture and design data, the models also support measurement, project assessment and control, system analysis, decision management, verification, and validation processes.

MBSE 利用建模环境，在执行 5.7 至 5.9 所涵盖的过程与关系引出的系统工程框架中详述的各过程时，将工程数据表达为模型。除集成概念、需求、架构和设计数据外，这些模型还支持测量、项目评定与控制、系统分析、决策管理、验证和确认过程。

This modelling approach results in the following.

这种建模途径带来下列结果。

- A single source of truth for system definition that accelerates data maturity, integration, and utility.

- 用于系统定义的单一事实来源，可加速数据的成熟、集成与利用。

This single source of truth allows more aggressive development schedules to be pursued. For example, as stated in 5.2, a system element in one context can be an SoI in another. In MBSE, a model of the SoI can be effectively integrated with models of enabling systems or interoperating systems to provide a model of a complete solution.

该单一事实来源允许采用更为进取的开发进度。例如，如 5.2 所述，一个语境中的系统元素在另一语境中能是 SoI。在 MBSE 中，SoI 的模型能有效地与使能系统或互操作系统的模型集成，以提供完整解决方案的模型。

- The ability to support multiple stakeholder viewpoints and views. As described in 5.2, an SoI may

- 支持多个利益相关方视角和视图的能力。如 5.2 所述，一个 SoI 可能

need to be represented as a hierarchical decomposition or a network. By using tailored model element relationships in MBSE, both are achievable using the same dataset comprising the SoI.

需要表示为层次分解或网络。通过在 MBSE 中使用经裁剪的模型元素关系，两者都能使用构成该 SoI 的同一数据集来实现。

- The ability to rapidly and thoroughly analyse the integrated model-based dataset by query helps

- 通过查询快速而彻底地分析基于模型的集成数据集的能力有助于

ensure model completeness and accuracy, and greatly reduces the time required and errors introduced through manual data verification. This feature greatly facilitates and provides the formality and rigor described in 6.4.6.

确保模型的完整性和准确性，并极大减少所需时间以及通过人工数据验证引入的错误。这一特性极大促进并提供 6.4.6 所述的形式化与严谨性。

### D.4 Benefits of executing system life cycle processes in an MBSE environment 在 MBSE 环境中执行系统生存周期过程的效益

The use of MBSE does accelerate the system life cycle processes. One key value of MBSE comes to fruition during verification and validation (see 6.4.9 and 6.4.11).

使用 MBSE 确实能加速系统生存周期过程。MBSE 的一项关键价值在验证和确认期间得以实现（见 6.4.9 和 6.4.11）。

The MBSE dataset also provides valuable information for service support of the system in operation.

MBSE 数据集还为运行中系统的服务支持提供有价值的信息。

A more complete list of benefits provided by incorporation of MBSE support activities in system life cycle processes is provided in Table D.1.

将 MBSE 支持活动纳入系统生存周期过程所带来的更完整效益清单见表 D.1。

**Table D.1 — System life cycle processes supported by an MBSE environment**

**表 D.1 — MBSE 环境所支持的系统生存周期过程**

| MBSE benefit ／ MBSE 效益 | MBSE support activity description ／ MBSE 支持活动描述 | Reference in this document ／ 本文件中的引用 |
| --- | --- | --- |
| More thorough understanding of the concept and system definition ／ 对构想和系统定义更透彻的理解 | Delivering systems engineering data as enhances specificity, clarity, and accurate interpretation of the data. ／ 以……形式交付系统工程数据，可增强数据的明确性、清晰度和准确解读。 | 6.4.1 to 6.4.5 ／ 6.4.1 至 6.4.5 |
| Better ability to perform trade-offs ／ 更好地执行权衡的能力 | Through data query and analyses, modelling allows comparison of solution alternatives much more expeditiously, comprehensively, and accurately than can be executed through manual review of data. Solution alternatives can be compared by query and analyses against a common set of requirements functions, and key performance parameters. ／ 通过数据查询和分析，建模使解决方案备选方案的比较远比通过人工审查数据更为迅速、全面和准确。能通过查询和分析，对照一组共同的需求、功能和关键性能参数来比较解决方案备选方案。 | 6.3.3 6.4.6 |
| More effective and efficient measurement ／ 更有效且高效的测量 | Modelling allows more expeditious, comprehensive, and accurate collection of data to support measures and perform analyses of proposed SoI and system element solutions than can be executed through manual reviews of data. Proposed solutions can be analysed by query to determine to what extent solutions achieve targeted values of technical measures (e.g. measures of effectiveness, measures of performance, technical performance measures). ／ 建模能以比人工审查数据远为迅速、全面和准确的方式收集数据，以支持测量并对所提出的 SoI 和系统元素解决方案进行分析。能通过查询分析所提出的解决方案，以确定这些解决方案在多大程度上达到技术测量的目标值（例如有效性测量、性能测量、技术性能测量）。 | 6.3.7 |
| Better ability to perform impact analysis ／ 更好地执行影响分析的能力 | Relationships in the integrated system definition dataset allows, by model query, rapid determination of the impact of changes to system definition, including impacts within and between system elements, at the interfaces, across the overall SoI, and possibly between the SoI and interoperating/enabling systems. ／ 集成系统定义数据集中的关系允许通过模型查询快速确定系统定义更改的影响，包括系统元素内部及系统元素之间的影响、接口处的影响、整个 SoI 范围的影响，以及可能存在的 SoI 与互操作系统／使能系统之间的影响。 | 6.4.6 |
| Help ensure consistency and completeness of requirements ／ 有助于确保需求的一致性和完整性 | Model analysis can, for instance, rapidly and thoroughly determine whether requirements, architectures, and design completely specify system elements; whether the system and system elements fully satisfy allocated requirements and functionality; and whether system interfaces are fully defined and reconciled. ／ 例如，模型分析能快速而彻底地确定需求、架构和设计是否完整地规定了系统元素；系统和系统元素是否完全满足所分配的需求和功能；以及系统接口是否得到完整定义并协调一致。 | 6.4.1 6.4.2 6.4.3 |
| Help ensure consistency and completeness of architecture and design ／ 有助于确保架构和设计的一致性和完整性 | Through the establishment of data relationships, modelling allows more effective integration of architecture and design data. Querying the integrated data allows rapid identification of missing data elements and model construction errors. ／ 通过建立数据关系，建模使架构和设计数据得到更有效的集成。查询集成后的数据能快速识别缺失的数据元素和模型构建错误。 | 6.4.4 6.4.5 6.4.6 |
| Enable reuse and adaptability ／ 使能复用和适应性 | Delivering systems engineering data as models that enhance specificity, clarity, and accurate interpretation of the data and facilitates their reuse. Knowledge assets from model-based system element representations (models, views, architecture and design patterns, etc.) can be exploited across the organization. The models better facilitate capturing the integrated technical information for the reusable patterns. Additionally, the models can be used to explore alternatives and impacts, enabling the identification of alternatives that increase the adaptability. ／ 以模型形式交付系统工程数据，增强数据的明确性、清晰度和准确解读，并促进其复用。来自基于模型的系统元素表示（模型、视图、架构和设计模式等）的知识资产能在整个组织内加以利用。模型更好地促进捕获可复用模式的集成技术信息。此外，这些模型能用于探究备选方案和影响，从而识别出提高适应性的备选方案。 | 6.2.6 6.4.4 6.4.5 6.4.6 |

**Table D.1** *(continued)***Table D.1** *(continued)*

**表 D.1** *（续）***表 D.1** *（续）*

| MBSE benefit ／ MBSE 效益 | MBSE support activity description ／ MBSE 支持活动描述 | Reference in this document ／ 本文件中的引用 |
| --- | --- | --- |
| Surrogate for verification and validation activities ／ 作为验证和确认活动的替代物 | Model analysis can detect requirements, architecture, and design errors through model verification and validation, in advance of pro-ducing and integrating physical system components. Validated models allow verification and validation activities to be done via simulated and modelled representations when it is not feasible to use the actual system. ／ 模型分析能在生产和集成物理系统组件之前，通过模型验证和确认来检测需求、架构和设计错误。经确认的模型允许在无法使用实际系统时，通过仿真和建模的表示来开展验证和确认活动。 | 6.3.8 6.4.9 6.4.11 |
| Reduction of risk ／ 风险降低 | Models can be analysed to identify technical and programmatic risks that would not otherwise have been apparent. Additionally, system definition elements (requirements, architecture, design, interfaces) that are developed and integrated within the models can be leveraged to affect risk treatment decisions. ／ 能对模型进行分析，以识别原本不会显现的技术风险和项目风险。此外，在模型内开发和集成的系统定义元素（需求、架构、设计、接口）能用于影响风险处理决策。 | 6.3.4 |
| Early detection of interface / integration issues ／ 接口／集成问题的早期检测 | Relationships in the integrated system definition dataset allows, by model query, rapid determination of missing, improperly defined and incompatible interfaces. ／ 集成系统定义数据集中的关系允许通过模型查询快速确定缺失的、定义不当的和不兼容的接口。 | 6.4.8 6.4.4 6.4.5 |
| Better understanding and management of dependencies ／ 更好地理解和管理依赖关系 | Delivering systems engineering data as models enhances specificity, clarity, and accurate interpretation of the data so that life cycle process and technical dependencies may be assessed. ／ 以模型形式交付系统工程数据可增强数据的明确性、清晰度和准确解读，从而能评定生存周期过程依赖关系和技术依赖关系。 | 6.3.1 6.3.2 |

### D.5 Model types useful in MBSE MBSE 中有用的模型类型

Various types of models are used in MBSE. Among them are the following.

MBSE 中使用各种类型的模型。其中包括下列各项。

a) Prescriptive models express either the expectations in terms of needs or requirements on the acquirer side, or committed requirements on the supplier side. They are used to reduce risks through analysis, validation and optimization of the system architecture models and are mathematically based to support mathematical analyses or simulation.

a) 规定性模型表达以需要或需求形式表述的、针对获取方一侧的期望，或供应方一侧已承诺的需求。这些模型用于通过对系统架构模型的分析、确认和优化来降低风险，并且基于数学，以支持数学分析或仿真。

b) Descriptive models (sometimes referred to as constructive models or system architecture models)

b) 描述性模型（有时称为构造性模型或系统架构模型）

capture the system’s behaviour, structure, constraints, interfaces, requirements, and serve as a repository to define product entities and their relationships.

捕获系统的行为、结构、约束、接口、需求，并充当定义产品实体及其关系的储存库。

c) Verification models are supported by descriptive and prescriptive models and are used to verify and validate that the system architecture and analysis models meet the customer’s requirements and needs.

c) 验证模型由描述性模型和规定性模型支持，用于验证和确认系统架构模型和分析模型满足顾客的需求和需要。

d) Cognitive models allow a simplified representation aimed at modelling psychological or intellectual processes. They can be enriched with representation of the virtual reality to represent human factors. Cognitive models replicate human reasoning and problem-solving for predictive purposes.

d) 认知模型允许采用简化的表示，其目的在于对心理或智力过程建模。这些模型能用虚拟现实的表示加以丰富，以表示人的因素。认知模型复制人的推理和问题求解，以用于预测目的。

All of the above models can be further classified according to the domain that they represent, called "domain specific models". For example, models may be related to the properties of the system (performance, reliability, mass property, power, etc.), technology implementation (electrical, mechanical, software, human, etc.), and application domain (automotive, aerospace, medical, defence, etc.).

上述所有模型都能按其表示的域进一步分类，称为“特定域模型”。例如，模型可能与系统的特性（性能、可靠性、质量特性、功率等）、技术实现（电气、机械、软件、人等）以及应用域（汽车、航空航天、医疗、国防等）相关。

Different degrees of abstraction (conceptual, logical, technical, and physical models) and formalisation vary according to the intent of models. Depending on the intent, the following models can be used.

不同的抽象程度（概念模型、逻辑模型、技术模型和物理模型）和形式化程度随模型意图而变化。依意图而定，能使用下列模型。

- Formal models are necessary to provide verifiable evidence or to directly generate system elements

- 形式化模型对于提供可验证的证据或直接生成系统元素是必要的

(i.e., hardware or software elements).

（即硬件或软件元素）。

- Semi-formal models are generally used as specification for further description or development

- 半形式化模型通常用作进一步描述或开发

activities.

活动的规格。

- Informal models are utilised when complete formal specification is impractical and can be based on

- 当完整的形式化规格不切实际时使用非形式化模型，它们能基于

heuristics or expert judgement.

启发式方法或专家判断。

As proposed by architecture description frameworks, models can be elaborated per stakeholder perspectives or viewpoints. They can also be elaborated to reflect aspects of the entity of interest (see ISO/IEC/IEEE 42010). In addition, practitioners may use a tool-supported modelling framework to organize models according to levels of abstraction and domain of coverage. By using this type of framework, various views of these models can be produced and packaged for stakeholder use. This approach is cost-effective, because the same model can often be used to reflect a multitude of views (both in form and level of detail, according to stakeholder viewpoints), as well as eliminate many correspondence problems across views that otherwise may arise if using purely description-based views.

如架构描述框架所提出的，模型能按利益相关方角度或视角加以细化。模型也能加以细化，以反映所关注实体的各个方面体（见 ISO/IEC/IEEE 42010）。此外，实践者可使用工具支持的建模框架，按抽象层级和覆盖域来组织模型。通过使用这类框架，能产生这些模型的各种视图并打包供利益相关方使用。这种途径具有成本效益，因为同一个模型往往能用于反映众多视图（依利益相关方视角，在形式和详细程度上均可），还能消除若使用纯粹基于描述的视图则可能产生的许多跨视图对应问题。

Verification and validation of models can be performed to anticipate these activities with the system itself. In particular, these activities allow assessment of the needs and requirements, evaluation of the system definition against these requirements, and evaluation of the quality characteristics of the systems.

能对模型执行验证和确认，以预先开展针对系统本身的这些活动。特别地，这些活动允许评定需要和需求、对照这些需求评估系统定义，以及评估系统的质量特性。

> **NOTE** The added value of verification and validation depends on the accuracy and fidelity of the models. The modelling effort is often limited by partial knowledge of the solution and by availability of time and resources.

> **注**：验证和确认的附加价值取决于模型的准确性和保真度。建模工作往往受限于对解决方案的部分了解以及时间和资源的可用性。

## Bibliography 参考文献

[1] ISO 9000:2015, *Quality management systems — Fundamentals and vocabulary*

[1] ISO 9000:2015, *质量管理体系 — 基础和词汇*

[2] ISO 9001:2015, *Quality management systems — Requirements*

[2] ISO 9001:2015, *质量管理体系 — 要求*

[3] ISO 9004, *Quality management — Quality of an organization — Guidance to achieve sustained* *success*

[3] ISO 9004, *质量管理 — 组织的质量 — 实现持续* *成功的指南*

[4] ISO 9241-210, *Ergonomics of human-system interaction — Part 210: Human-centred design for* *interactive systems*

[4] ISO 9241-210, *人-系统交互工效学 — 第 210 部分：以人为中心的* *交互式系统设计*

[5] ISO 10004, *Quality management — Customer satisfaction — Guidelines for monitoring and* *measuring*

[5] ISO 10004, *质量管理 — 顾客满意 — 监视和* *测量指南*

[6] ISO 10007, *Quality management — Guidelines for configuration management*

[6] ISO 10007, *质量管理 — 配置管理指南*

[7] ISO/IEC/IEEE 12207:2017, *Systems and software engineering — Software life cycle processes*

[7] ISO/IEC/IEEE 12207:2017, *系统与软件工程 — 软件生存周期过程*

[8] ISO 14001, *Environmental management systems — Requirements with guidance for use*

[8] ISO 14001, *环境管理体系 — 要求及使用指南*

[9] ISO/IEC/IEEE 14764, *Software engineering — Software life cycle processes — Maintenance*

[9] ISO/IEC/IEEE 14764, *软件工程 — 软件生存周期过程 — 维护*

[10] ISO/IEC/IEEE 15026 (all parts), *Systems and software engineering — Systems and software* *assurance*

[10] ISO/IEC/IEEE 15026（所有部分）, *系统与软件工程 — 系统与软件* *保证*

[11] ISO/IEC/IEEE 15289:2019, *Systems and software engineering — Content of life-cycle information* *items (documentation)*

[11] ISO/IEC/IEEE 15289:2019, *系统与软件工程 — 生存周期信息* *部件（文档）的内容*

[12] ISO/IEC 15408-3, *Information security, cybersecurity and privacy protection — Evaluation criteria* *for IT security — Part 3: Security assurance components*

[12] ISO/IEC 15408-3, *信息安全性、网络安全和隐私保护 — IT 安全* *评估准则 — 第 3 部分：信息安全性保证组件*

[13] ISO 15704, *Enterprise modelling and architecture — Requirements for enterprise-referencing* *architectures and methodologies*

[13] ISO 15704, *企业建模与架构 — 对企业参照* *架构与方法论的要求*

[14] ISO/IEC/IEEE 15939, *Systems and software engineering — Measurement process*

[14] ISO/IEC/IEEE 15939, *系统与软件工程 — 测量过程*

[15] ISO/IEC/IEEE 16085, *Systems and software engineering — Life cycle processes — Risk management*

[15] ISO/IEC/IEEE 16085, *系统与软件工程 — 生存周期过程 — 风险管理*

[16] ISO/IEC/IEEE 16326, *Systems and software engineering — Life cycle processes — Project* *management*

[16] ISO/IEC/IEEE 16326, *系统与软件工程 — 生存周期过程 —* *项目管理*

[17] ISO/TS 18152, *Ergonomics of human-system interaction — Specification for the process assessment* *of human-system issues*

[17] ISO/TS 18152, *人-系统交互工效学 —* *人-系统问题的过程评定规格*

[18] ISO 18435 (all parts), *Industrial automation systems and integration — Diagnostics, capability* *assessment and maintenance applications integration*

[18] ISO 18435（所有部分）, *工业自动化系统与集成 —* *诊断、能力评定和维护应用集成*

[19] ISO 19014-4:2020, *Earth-moving machinery — Functional safety — Part 4: Design and evaluation* *of software and data transmission for safety-related parts of the control system*

[19] ISO 19014-4:2020, *土方机械 — 功能安全 — 第 4 部分：* *控制系统安全相关部分的软件和数据传输的设计与评估*

[19] ISO/IEC 20000 (all parts), *Information technology — Service management*

[19] ISO/IEC 20000（所有部分）, *信息技术 — 服务管理*

[20] ISO/IEC/IEEE 21839:2019, *Systems and software engineering — System of systems (SoS)* *considerations in life cycle stages of a system*

[20] ISO/IEC/IEEE 21839:2019, *系统与软件工程 —* *系统生存周期阶段中系统的系统（SoS）考量*

[21] ISO/IEC/IEEE 21840:2019, *Systems and software engineering — Guidelines for the utilization of* *ISO/IEC/IEEE 15288 in the context of system of systems (SoS)*

[21] ISO/IEC/IEEE 21840:2019, *系统与软件工程 — 系统的系统（SoS）语境中* *使用 ISO/IEC/IEEE 15288 的指南*

[22] ISO/IEC/IEEE 21841, *Systems and software engineering — Taxonomy of systems of systems*

[22] ISO/IEC/IEEE 21841, *系统与软件工程 — 系统的系统分类*

[23] ISO 22400 (all parts), *Automation systems and integration — Key performance indicators (KPIs)* *for manufacturing operations management*

[23] ISO 22400（所有部分）, *自动化系统与集成 —* *制造运行管理的关键性能指标（KPI）*

[24] ISO/IEC/IEEE 24641:2023, *Systems and software engineering — Methods and tools for model-* *based systems and software engineering*

[24] ISO/IEC/IEEE 24641:2023, *系统与软件工程 —* *基于模型的系统与软件工程的方法和工具*

[25] ISO/IEC/IEEE 24748-1:20182), *Systems and software engineering — Life cycle management — Part* *1: Guidelines for life cycle management*

[25] ISO/IEC/IEEE 24748-1:20182), *系统与软件工程 — 生存周期管理 — 第* *1 部分：生存周期管理指南*

[26] ISO/IEC/IEEE 24748-2, *Systems and software engineering — Life cycle management — Part 2:* *Guidelines for the application of ISO/IEC/IEEE 15288 (System life cycle processes)*

[26] ISO/IEC/IEEE 24748-2, *系统与软件工程 — 生存周期管理 — 第 2 部分：* *ISO/IEC/IEEE 15288（系统生存周期过程）应用指南*

[27] ISO/IEC/IEEE 24748-4:2016, *Systems and software engineering — Life cycle management — Part* *4: Systems engineering planning*

[27] ISO/IEC/IEEE 24748-4:2016, *系统与软件工程 — 生存周期管理 — 第* *4 部分：系统工程规划*

[28] ISO/IEC/IEEE 24748-5, *Systems and software engineering — Life cycle management — Part 5:* *Software development planning*

[28] ISO/IEC/IEEE 24748-5, *系统与软件工程 — 生存周期管理 — 第 5 部分：* *软件开发规划*

[29] ISO/IEC/IEEE 24748-6:—3), *Systems and software engineering — Life cycle management — Part 6:* *System and software integration*

[29] ISO/IEC/IEEE 24748-6:—3), *系统与软件工程 — 生存周期管理 — 第 6 部分：* *系统与软件集成*

[28] ISO/IEC/IEEE 24748-8:2019, *Systems and software engineering — Life cycle management — Part* *8: Technical reviews and audits on defense programs*

[28] ISO/IEC/IEEE 24748-8:2019, *系统与软件工程 — 生存周期管理 — 第* *8 部分：国防项目的技术评审与审核*

[30] ISO/IEC/IEEE 24765, *Systems and software engineering — Vocabulary*

[30] ISO/IEC/IEEE 24765, *系统与软件工程 — 词汇*

[31] ISO/IEC/IEEE 24774:2021, *Systems and software engineering — Life cycle management —* *Specification for process description*

[31] ISO/IEC/IEEE 24774:2021, *系统与软件工程 — 生存周期管理 —* *过程描述规格*

[32] ISO/IEC 25000, *Systems and software engineering — Systems and software Quality Requirements* *and Evaluation (SQuaRE) — Guide to SQuaRE*

[32] ISO/IEC 25000, *系统与软件工程 — 系统与软件质量* *要求和评价（SQuaRE） — SQuaRE 指南*

[33] ISO/IEC 25010:2011, *Systems and software engineering — Systems and software Quality* *Requirements and Evaluation (SQuaRE) — System and software quality models*

[33] ISO/IEC 25010:2011, *系统与软件工程 — 系统与软件质量* *要求和评价（SQuaRE） — 系统与软件质量模型*

[34] ISO/IEC 25030, *Systems and software engineering — Systems and software quality requirements* *and evaluation (SQuaRE) — Quality requirements framework*

[34] ISO/IEC 25030, *系统与软件工程 — 系统与软件质量要求* *和评价（SQuaRE） — 质量要求框架*

[35] ISO/IEC/TR 25060, *Systems and software engineering — Systems and software product Quality* *Requirements and Evaluation (SQuaRE) — Common Industry Format (CIF) for usability: General* *framework for usability-related information*

[35] ISO/IEC/TR 25060, *系统与软件工程 — 系统与软件产品质量* *要求和评价（SQuaRE） — 可用性的通用行业格式（CIF）：* *可用性相关信息的通用框架*

[36] ISO/IEC 25063, *Systems and software engineering — Systems and software product Quality* *Requirements and Evaluation (SQuaRE) — Common Industry Format (CIF) for usability: Context of* *use description*

[36] ISO/IEC 25063, *系统与软件工程 — 系统与软件产品质量* *要求和评价（SQuaRE） — 可用性的通用行业格式（CIF）：* *使用语境描述*

[37] ISO/IEC/IEEE 26531, *Systems and software engineering — Content management for product life-* *cycle, user and service management documentation*

[37] ISO/IEC/IEEE 26531, *系统与软件工程 —* *产品生存周期、用户和服务管理文档的内容管理*

[38] ISO/IEC 26550, *Software and systems engineering — Reference model for product line engineering* *and management*

[38] ISO/IEC 26550, *软件与系统工程 —* *产品线工程与管理的参考模型*

[39] ISO/IEC 26580, *Software and systems engineering — Methods and tools for the feature-based* *approach to software and systems product line engineering*

[39] ISO/IEC 26580, *软件与系统工程 —* *基于特征的软件与系统产品线工程途径的方法和工具*

[40] ISO/IEC 27000, *Information technology — Security techniques — Information security management* *systems — Overview and vocabulary*

[40] ISO/IEC 27000, *信息技术 — 安全技术 — 信息安全管理* *体系 — 概述和词汇*

[41] ISO/IEC 27036 (all parts), *Cybersecurity — Supplier relationships*

[41] ISO/IEC 27036（所有部分）, *网络安全 — 供应方关系*

2) Freely available on the www​.iso​.org website.

2) 可在 www​.iso​.org 网站上免费获取。

3) Under preparation. Stage at the time of publication: ISO/IEC/IEEE FDIS 24748-6:2023.

3) 正在制定中。出版时的阶段：ISO/IEC/IEEE FDIS 24748-6:2023。

[42] ISO/IEC/TR 29110-1:2016, *Systems and software engineering — Lifecycle profiles for Very Small* *Entities (VSEs) — Part 1: Overview*

[42] ISO/IEC/TR 29110-1:2016, *系统与软件工程 — 极小型* *实体（VSE）生存周期轮廓 — 第 1 部分：概述*

[43] ISO/IEC/IEEE 29148:2018, *Systems and software engineering — Life cycle processes —* *Requirements engineering*

[43] ISO/IEC/IEEE 29148:2018, *系统与软件工程 — 生存周期过程 —* *需求工程*

[44] ISO 31000, *Risk management — Guidelines*

[44] ISO 31000, *风险管理 — 指南*

[45] IEC 31010, *Risk management — Risk assessment techniques*

[45] IEC 31010, *风险管理 — 风险评估技术*

[46] ISO/IEC 33002:2015, *Information technology — Process assessment — Requirements for* *performing process assessment*

[46] ISO/IEC 33002:2015, *信息技术 — 过程评定 —* *执行过程评定的要求*

[47] ISO/IEC 33004:2015, *Information technology — Process assessment — Requirements for process* *reference, process assessment and maturity models*

[47] ISO/IEC 33004:2015, *信息技术 — 过程评定 — 过程参考、过程评定* *与成熟度模型的要求*

[48] ISO/IEC/IEEE 42010, *Systems and software engineering — Architecture description*

[48] ISO/IEC/IEEE 42010, *系统与软件工程 — 架构描述*

[49] ISO/IEC/IEEE 42020:2019, *Software, systems and enterprise — Architecture processes*

[49] ISO/IEC/IEEE 42020:2019, *软件、系统与企业 — 架构过程*

[50] ISO/IEC/IEEE 42030, *Software, systems and enterprise — Architecture evaluation framework*

[50] ISO/IEC/IEEE 42030, *软件、系统与企业 — 架构评估框架*

[51] IEC 60300-1, *Dependability management - Part 1: Guidance for management and application*

[51] IEC 60300-1, *可信性管理 - 第 1 部分：管理与应用指南*

[52] IEC 61508 (all parts), *Functional safety of electrical/electronic/ programmable electronic safety-* *related systems*

[52] IEC 61508（所有部分）, *电气／电子／可编程电子安全相关系统的* *功能安全*

[53] IEC 62741, *Demonstration of dependability requirements – The dependability case*

[53] IEC 62741, *可信性要求的论证 – 可信性情形*

[54] ISO Guide 73:2009, *Risk management — Vocabulary*

[54] ISO Guide 73:2009, *风险管理 — 词汇*

[55] ANSI/AIAA G-043B-2018, *ANSI/AIAA Guide to the Preparation of Operational Concept Documents*

[55] ANSI/AIAA G-043B-2018, *ANSI/AIAA 运行概念文件编制指南*

[56] SAE EIA-649-C-2019, *Configuration Management Standard*

[56] SAE EIA-649-C-2019, *配置管理标准*

[57] IEEE Std 828-2012, *IEEE Standard for Configuration Management in Systems and Software* *Engineering*

[57] IEEE Std 828-2012, *IEEE 系统与软件* *配置管理标准*

[58] INCOSE-MBCM-2020-001.1, *Model-Based Capabilities Matrix and User’s Guide*, Version 1.0, January 2020

[58] INCOSE-MBCM-2020-001.1, *基于模型的能力矩阵与用户指南*，版本 1.0，2020 年 1 月

[59] INCOSE-TP-2003-002-5, Systems Engineering Handbook, *A Guide for System Life Cycle Processes* *and Activities*, 20234)

[59] INCOSE-TP-2003-002-5, 系统工程手册，*系统生存周期过程* *与活动指南*，20234)

[60] INCOSE-TP-2003-020-01, *Technical Measurement*, Version 1.0, 27 December 2005

[60] INCOSE-TP-2003-020-01, *技术测量*，版本 1.0，2005 年 12 月 27 日

[61] INCOSE-TP-2020-002-06, *Systems Engineering and System Definition*, Version 1.0, 08 January 2020

[61] INCOSE-TP-2020-002-06, *系统工程与系统定义*，版本 1.0，2020 年 1 月 8 日

[62] NATO AEP-67 *Engineering for System Assurance in NATO Programs*

[62] NATO AEP-67 *NATO 计划中的系统保障工程*

[63] SAE ARP4754A, *Guidelines for Development of Civil Aircraft and Systems*

[63] SAE ARP4754A, *民用飞机与系统研制指南*

[64] SAE JA1011, *Evaluation Criteria for Reliability-Centered Maintenance (RCM) Processes*

[64] SAE JA1011, *以可靠性为中心的维护（RCM）过程的评估准则*

[65] Tukker A.2004, , Eight Types of Product Service Systems: Eight Ways to Sustainability?, Business Strategy and the Environment **13**, p. 246

[65] Tukker A.2004, , 产品服务系统的八种类型：通往可持续性的八条途径？，Business Strategy and the Environment **13**，p. 246

[66] ANSI/AAMI/IEC 62304:2006/A1:​2016, *Medical device software — Software life cycle processes*

[66] ANSI/AAMI/IEC 62304:2006/A1:​2016, *医疗器械软件 — 软件生存周期过程*

[67] ISO 13485, *Medical devices — Quality management systems — Requirements for regulatory* *purposes*

[67] ISO 13485, *医疗器械 — 质量管理体系 — 用于法规的* *要求*

4) Under preparation.

4) 在制定中。

[68] PMI *Practice Standard for Work Breakdown Structures*, 2006

[68] PMI *工作分解结构实践标准*，2006

[69] STANAG 4427*Configuration Management in System Life Cycle Management*

[69] STANAG 4427*系统生存周期管理中的配置管理*

[70] ISO/IEC 19770 (all parts), *Information technology — IT asset management*

[70] ISO/IEC 19770（所有部分）, *信息技术 — IT 资产管理*

## IEEE notices and abstract IEEE 通告与摘要

**Important Notices and Disclaimers Concerning IEEE Standards Documents**

**关于 IEEE 标准文件的重要通告与免责声明**

IEEE Standards documents are made available for use subject to important notices and legal disclaimers. These notices and disclaimers, or a reference to this page (https://​standards​.ieee​.org/​ipr/​disclaimers​ .html), appear in all standards and may be found under the heading “Important Notices and Disclaimers Concerning IEEE Standards Documents.”

IEEE 标准文件在提供使用时，须遵守重要通告与法律免责声明。这些通告与免责声明，或对本页（https://​standards​.ieee​.org/​ipr/​disclaimers​ .html）的引用，出现在所有标准中，并可在“关于 IEEE 标准文件的重要通告与免责声明”这一标题下查到。

**Notice and Disclaimer of Liability Concerning the Use of IEEE Standards Documents**

**关于使用 IEEE 标准文件的责任通告与免责声明**

IEEE Standards documents are developed within the IEEE Societies and the Standards Coordinating Committees of the IEEE Standards Association (IEEE SA) Standards Board. IEEE develops its standards through an accredited consensus development process, which brings together volunteers representing varied viewpoints and interests to achieve the final product. IEEE Standards are documents developed by volunteers with scientific, academic, and industry-based expertise in technical working groups. Volunteers are not necessarily members of IEEE or IEEE SA, and participate without compensation from IEEE. While IEEE administers the process and establishes rules to promote fairness in the consensus development process, IEEE does not independently evaluate, test, or verify the accuracy of any of the information or the soundness of any judgments contained in its standards.

IEEE 标准文件由 IEEE 各学会以及 IEEE 标准协会（IEEE SA）标准委员会的各标准协调委员会制定。IEEE 通过经认可的共识制定过程制定其标准，该过程汇聚代表不同观点与利益的志愿者，以形成最终成果。IEEE 标准是由具备科学、学术和产业专长的志愿者在技术工作组中制定的文件。志愿者不一定是 IEEE 或 IEEE SA 的成员，且不因参与而从 IEEE 获得报酬。尽管 IEEE 管理该过程并制定规则以促进共识制定过程的公正性，但 IEEE 不独立评估、测试或验证其标准中所含任何信息的准确性，也不验证其中任何判断的可靠性。

IEEE does not warrant or represent the accuracy or completeness of the material contained in its standards, and expressly disclaims all warranties (express, implied and statutory) not included in this or any other document relating to the standard, including, but not limited to, the warranties of: merchantability; fitness for a particular purpose; non-infringement; and quality, accuracy, effectiveness, currency, or completeness of material. In addition, IEEE disclaims any and all conditions relating to results and workmanlike effort. In addition, IEEE does not warrant or represent that the use of the material contained in its standards is free from patent infringement. IEEE Standards documents are supplied “AS IS” and “WITH ALL FAULTS.”

IEEE 不担保也不声明其标准中所含材料的准确性或完整性，并明确否认本文件或与标准有关的任何其他文件中未包含的一切担保（明示、默示和法定担保），包括但不限于以下担保：可销售性；特定用途适用性；不侵权；以及材料的质量、准确性、有效性、时效性或完整性。此外，IEEE 否认与结果和专业水准努力有关的一切条件。此外，IEEE 不担保也不声明使用其标准中所含材料不会侵犯专利权。IEEE 标准文件按“现状”与“含全部瑕疵”提供。

Use of an IEEE standard is wholly voluntary. The existence of an IEEE Standard does not imply that there are no other ways to produce, test, measure, purchase, market, or provide other goods and services related to the scope of the IEEE standard. Furthermore, the viewpoint expressed at the time a standard is approved and issued is subject to change brought about through developments in the state of the art and comments received from users of the standard.

使用 IEEE 标准完全出于自愿。IEEE 标准的存在，并不意味着不存在其他方式来生产、试验、测量、采购、营销或提供与该 IEEE 标准范围有关的其他货物和服务。此外，标准在批准和发布之时所表达的观点，会随技术发展水平的进展以及标准用户提出的意见而变化。

In publishing and making its standards available, IEEE is not suggesting or rendering professional or other services for, or on behalf of, any person or entity, nor is IEEE undertaking to perform any duty owed by any other person or entity to another. Any person utilizing any IEEE Standards document, should rely upon his or her own independent judgment in the exercise of reasonable care in any given circumstances or, as appropriate, seek the advice of a competent professional in determining the appropriateness of a given IEEE standard.

IEEE 在出版并提供其标准时，并非为任何人或实体、亦非代表任何人或实体提议或提供专业服务或其他服务，IEEE 也不承诺履行任何其他人或实体对他人所负的任何义务。任何使用任何 IEEE 标准文件的人，宜在任何特定情形下尽到合理注意，依靠其自身的独立判断；或在适当情况下，就某一给定 IEEE 标准是否适当征询有能力的专业人员的意见。

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

Subject to payment of the appropriate licensing fees, IEEE will grant users a limited, non-exclusive license to photocopy portions of any individual standard for company or organizational internal use or individual, non-commercial use only. To arrange for payment of licensing fees, please contact Copyright Clearance Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA; +1 978

在支付相应许可费的前提下，IEEE 将授予使用者一项有限的、非排他的许可，仅为公司或组织内部使用或个人非商业使用而影印任何单项标准的部分内容。为安排支付许可费，请联系 Copyright Clearance Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA；+1 978

750 8400; https://​www​.copyright​.com/​. Permission to photocopy portions of any individual standard for educational classroom use can also be obtained through the Copyright Clearance Center.

750 8400；https://​www​.copyright​.com/。为教育课堂教学使用而影印任何单项标准部分内容的许可，也可通过 Copyright Clearance Center 获得。

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

IEEE 标准不担保也不确保安全性、安全、健康或环境保护，也不确保免于与其他设备或网络相互干扰。IEEE 标准的制定活动在形成任何安全性建议时，会考虑提交给标准制定工作组的研究与信息。关于安全性实践、技术或技术实现的变化、或外围系统影响的其他信息，也可能与本标准实施期间的安全性考虑相关。IEEE 标准文件的实施者和使用者负责确定并遵守所有适当的安全性、安全、环境、健康和干扰防护实践，以及所有适用的法律和法规。

**Abstract**

**摘要**

This document establishes a common framework of process descriptions for describing the life cycle of systems created by humans, defining a set of processes and associated terminology from an engineering viewpoint. These processes can be applied to systems of interest, their system elements, and to system of systems. Selected sets of these processes can be applied throughout the stages of a system's life cycle. This is accomplished through the involvement of stakeholders, with the ultimate goal of achieving customer satisfaction.

本文件建立了过程描述的通用框架，用以描述人造系统的生存周期，并从工程视角定义了一组过程及相关术语。这些过程能应用于所关注系统、其系统元素以及系统的系统。这些过程的选定集合能应用于系统生存周期的各个阶段。这是通过利益相关方的参与来实现的，最终目标是实现顾客满意。

This document also specifies processes that support the definition, control and improvement of the system life cycle processes used within an organization or a project. Organizations and projects can use these processes when acquiring and supplying systems.

本文件还规定了支持对一个组织或一个项目内所使用的系统生存周期过程进行定义、控制和改进的过程。组织与项目在获取和供应系统时能使用这些过程。

This document concerns systems that can be configured with one or more of the following system elements: hardware elements, software elements, data, humans, processes, services, procedures, facilities, materials, and naturally occurring entities.

本文件所涉及的系统，能由一个或多个下列系统元素配置而成：硬件元素、软件元素、数据、人员、过程、服务、规程、设施、材料和自然存在的实体。
