# CSA ISO/IEC/IEEE 42030:20

> **Software, systems and enterprise — Architecture evaluation framework**
>
> (ISO/IEC/IEEE 42030:2019, IDT)

> **转换说明 / About this file**
>
> 本文件由 `ISO IEC IEEE 42030-2020.docx` 转换生成，正文为**英文原文照录**，未作翻译或改写。
>
> **源件性质（重要）**：本目录内没有 42030 的 PDF，只有这一份 docx；而它本身是 **CSA 采标件的 PDF→Word 转换产物**（`CSA ISO/IEC/IEEE 42030:20`，等同采用 ISO/IEC/IEEE 42030:2019）。因此它与另两份由 PDF 直转的文件不同，带三处源伤，均已尽量修补，仍存疑处如实标注：
>
> 1. **条款号在源件正文中整体丢失**（标题只剩 `Scope`／`General` 这样的文字）。本文件已从 docx 的 Word 自动编号定义中还原——每个编号组的 `w:start` 编码了续号（如第 4 章那组 L0 start=4），故 `1`~`8`、`4.3.1`、`A.1`、`A.3.2.1` 这类号**是还原所得，不是从版面抄录的**。还原结果与源件内交叉引用（如正文 `See A.4 for …`）自洽，但**用前建议对一次正版**。
> 2. **插图全部未收录（20 幅）**：源件把矢量插图切成了大量小位图碎片（图 A.5 碎成 16 块），部分图完全丢失；更要紧的是**位图与图题在文档流中整体错位**——图题集中在 337~462 段，而位图落在 843／907／968／1022 段，按「就近取图」会把图 B.1 的题注配上一块写着 `processes` 的碎片。**错图比无图有害，故一幅不取**，只在每处原位插入 `> **图未收录**` 说明。需原图请查正版 PDF。
> 3. **页眉页脚混入正文**且 `ISO/IEC/IEEE 42030:2019(E)` 被误标为 Heading 4，已按版式构件剔除。
>
> **其他处理**：表格按 Word 表结构转 Markdown（跨页表被源件拆成多张，故表块数多于表数）；印刷目录已替换为按标题层级生成的 Markdown 目录；断行连字符已还原（`identi- fying` → `identifying`，`one- and` 类悬挂连字符保留）；封面与版权页照录于正文之前。
>
> **校验**：拿源 docx 逐段回查，受检 1073 段中 **1068 段命中**；未命中的 5 段全部是**印刷目录行**（带页码的 `AE report recommendations 31`、`Annex A (informative) … 34` 等），按设计已由生成目录取代，非内容缺失。表格 33 块列数自洽，无残留控制符。


---

## Contents

  - [Foreword](#foreword)
  - [Introduction](#introduction)
  - [Software, systems and enterprise — Architecture evaluation framework](#software-systems-and-enterprise-architecture-evaluation-framework)
    - [1 Scope](#1-scope)
    - [2 Normative references](#2-normative-references)
    - [3 Terms and definitions](#3-terms-and-definitions)
      - [3.1 architecture](#31-architecture)
      - [3.2 architecture description](#32-architecture-description)
      - [3.3 architecture entity](#33-architecture-entity)
      - [3.4 architecture evaluation AE](#34-architecture-evaluation-ae)
      - [3.5 architecture evaluation framework](#35-architecture-evaluation-framework)
      - [3.6 concern](#36-concern)
      - [3.7 environment](#37-environment)
      - [3.8 factor](#38-factor)
      - [3.9 stakeholder](#39-stakeholder)
      - [3.10 value](#310-value)
    - [4 Conceptual foundation](#4-conceptual-foundation)
      - [4.1 General](#41-general)
      - [4.2 Architecture evaluation context](#42-architecture-evaluation-context)
      - [4.3 Architecture evaluation tiers](#43-architecture-evaluation-tiers)
        - [4.3.1 Evaluation synthesis](#431-evaluation-synthesis)
        - [4.3.2 Value assessment](#432-value-assessment)
        - [4.3.3 Architectural analysis](#433-architectural-analysis)
      - [4.4 Architecture evaluation conceptual model](#44-architecture-evaluation-conceptual-model)
      - [4.5 Comparison between assessment and analysis](#45-comparison-between-assessment-and-analysis)
      - [4.6 Architecture evaluation factors](#46-architecture-evaluation-factors)
      - [4.7 Customized architecture evaluation frameworks](#47-customized-architecture-evaluation-frameworks)
      - [4.8 Tailoring](#48-tailoring)
    - [5 Conformance](#5-conformance)
      - [5.1 General](#51-general)
      - [5.2 Creating AE artifacts](#52-creating-ae-artifacts)
      - [5.3 Using generic AE framework to conduct AE efforts](#53-using-generic-ae-framework-to-conduct-ae-efforts)
      - [5.4 Verbal forms for the expression of provisions](#54-verbal-forms-for-the-expression-of-provisions)
    - [6 Architecture evaluation framework elements](#6-architecture-evaluation-framework-elements)
      - [6.1 Evaluation synthesis](#61-evaluation-synthesis)
        - [6.1.1 General requirements](#611-general-requirements)
        - [6.1.2 Architecture evaluation objectives](#612-architecture-evaluation-objectives)
        - [6.1.3 Architecture evaluation approaches](#613-architecture-evaluation-approaches)
        - [6.1.4 Architecture evaluation factors](#614-architecture-evaluation-factors)
        - [6.1.5 Architecture evaluation results](#615-architecture-evaluation-results)
      - [6.2 Value assessment](#62-value-assessment)
        - [6.2.1 General requirements](#621-general-requirements)
        - [6.2.2 Value assessment objectives](#622-value-assessment-objectives)
        - [6.2.3 Value assessment methods](#623-value-assessment-methods)
        - [6.2.4 Value assessment factors](#624-value-assessment-factors)
        - [6.2.5 Value assessment results](#625-value-assessment-results)
      - [6.3 Architectural analysis](#63-architectural-analysis)
        - [6.3.1 General requirements](#631-general-requirements)
        - [6.3.2 Architectural analysis objectives](#632-architectural-analysis-objectives)
        - [6.3.3 Architectural analysis methods](#633-architectural-analysis-methods)
        - [6.3.4 Architectural analysis factors](#634-architectural-analysis-factors)
        - [6.3.5 Architectural analysis results](#635-architectural-analysis-results)
    - [7 Customized architecture evaluation frameworks](#7-customized-architecture-evaluation-frameworks)
      - [7.1 General requirements](#71-general-requirements)
      - [7.2 Framework requirements for architecture evaluation](#72-framework-requirements-for-architecture-evaluation)
      - [7.3 Framework requirements for value assessment](#73-framework-requirements-for-value-assessment)
      - [7.4 Framework requirements for architectural analysis](#74-framework-requirements-for-architectural-analysis)
      - [7.5 Framework requirements for architecture evaluation work products](#75-framework-requirements-for-architecture-evaluation-work-products)
    - [8 Architecture evaluation work products](#8-architecture-evaluation-work-products)
      - [8.1 General requirements](#81-general-requirements)
      - [8.2 Architecture evaluation plan](#82-architecture-evaluation-plan)
        - [8.2.1 AE plan requirements](#821-ae-plan-requirements)
        - [8.2.2 AE plan recommendations](#822-ae-plan-recommendations)
        - [8.2.3 AE plan permissions](#823-ae-plan-permissions)
      - [8.3 Architecture evaluation report](#83-architecture-evaluation-report)
        - [8.3.1 AE report requirements](#831-ae-report-requirements)
        - [8.3.2 AE report recommendations](#832-ae-report-recommendations)
        - [8.3.3 AE report permissions](#833-ae-report-permissions)
  - [Annex A (informative) — Value and quality concepts](#annex-a-informative-value-and-quality-concepts)
    - [A.1 General](#a1-general)
    - [A.2 Evaluation factors](#a2-evaluation-factors)
    - [A.3 Value](#a3-value)
      - [A.3.1 General](#a31-general)
      - [A.3.2 What is “Value”?](#a32-what-is-value)
      - [A.3.3 Value-focused thinking](#a33-value-focused-thinking)
      - [A.3.4 Value assessment of system architectures](#a34-value-assessment-of-system-architectures)
      - [A.3.5 Ring’s value model](#a35-rings-value-model)
      - [A.3.6 Stakeholder values, qualities and measures](#a36-stakeholder-values-qualities-and-measures)
      - [A.3.7 Value articulation framework](#a37-value-articulation-framework)
    - [A.4 Quality](#a4-quality)
      - [A.4.1 General](#a41-general)
      - [A.4.2 What is “Quality”?](#a42-what-is-quality)
      - [A.4.3 Architecture quality attributes](#a43-architecture-quality-attributes)
      - [A.4.4 Boehm and Nupul’s quality model and ontology](#a44-boehm-and-nupuls-quality-model-and-ontology)
      - [A.4.5 The ISO/IEC 25000 family of standards on quality](#a45-the-isoiec-25000-family-of-standards-on-quality)
        - [A.4.5.1 General](#a451-general)
        - [A.4.5.2 ISO/IEC 25000 Quality model framework](#a452-isoiec-25000-quality-model-framework)
  - [Annex B (informative) — Relationship to other standards](#annex-b-informative-relationship-to-other-standards)
    - [B.1 ISO/IEC standards in the domain of systems and software engineering](#b1-isoiec-standards-in-the-domain-of-systems-and-software-engineering)
    - [B.2 ISO standards in the domain of enterprise activities](#b2-iso-standards-in-the-domain-of-enterprise-activities)
    - [B.3 Relationship between architecture standards](#b3-relationship-between-architecture-standards)
  - [Annex C (informative) — Architecture evaluation examples](#annex-c-informative-architecture-evaluation-examples)
    - [C.1 General](#c1-general)
    - [C.2 Business and IT architecture evaluation](#c2-business-and-it-architecture-evaluation)
      - [C.2.1 Situation](#c21-situation)
      - [C.2.2 Business/IT architecture — Evaluation synthesis](#c22-businessit-architecture-evaluation-synthesis)
      - [C.2.3 Business/IT architecture — Value assessment](#c23-businessit-architecture-value-assessment)
      - [C.2.4 Business/IT architecture — Architectural analysis](#c24-businessit-architecture-architectural-analysis)
    - [C.3 Software architecture evaluation](#c3-software-architecture-evaluation)
      - [C.3.1 Situation](#c31-situation)
      - [C.3.2 Software architecture — Evaluation synthesis](#c32-software-architecture-evaluation-synthesis)
      - [C.3.3 Software architecture — Value assessment](#c33-software-architecture-value-assessment)
      - [C.3.4 Software architecture — Architectural analysis](#c34-software-architecture-architectural-analysis)
    - [C.4 Service architecture evaluation](#c4-service-architecture-evaluation)
      - [C.4.1 Situation](#c41-situation)
      - [C.4.2 Service architecture — Evaluation synthesis](#c42-service-architecture-evaluation-synthesis)
      - [C.4.3 Service architecture — Value assessment](#c43-service-architecture-value-assessment)
      - [C.4.4 Service architecture — Architectural analysis](#c44-service-architecture-architectural-analysis)
    - [C.5 Enterprise architecture evaluation](#c5-enterprise-architecture-evaluation)
      - [C.5.1 Situation](#c51-situation)
      - [C.5.2 Enterprise architecture — Evaluation synthesis](#c52-enterprise-architecture-evaluation-synthesis)
      - [C.5.3 Enterprise architecture — Value assessment](#c53-enterprise-architecture-value-assessment)
      - [C.5.4 Enterprise architecture — Architectural analysis](#c54-enterprise-architecture-architectural-analysis)
  - [Annex D (informative) — Example architecture evaluation frameworks](#annex-d-informative-example-architecture-evaluation-frameworks)
    - [D.1 General](#d1-general)
    - [D.2 Architecture Tradeoff Analysis Method (ATAM)](#d2-architecture-tradeoff-analysis-method-atam)
      - [D.2.1 Overview](#d21-overview)
        - [D.2.1.1 General](#d211-general)
        - [D.2.1.2 Purpose](#d212-purpose)
        - [D.2.1.3 Basic approach](#d213-basic-approach)
        - [D.2.1.4 Conceptual flow](#d214-conceptual-flow)
        - [D.2.1.5 Sequence of steps](#d215-sequence-of-steps)
        - [D.2.1.6 Expected results](#d216-expected-results)
      - [D.2.2 Evaluation synthesis](#d22-evaluation-synthesis)
      - [D.2.3 Value assessment](#d23-value-assessment)
      - [D.2.4 Architectural analysis](#d24-architectural-analysis)
      - [D.2.5 Evaluation plan and report](#d25-evaluation-plan-and-report)
    - [D.3 The Method Framework and QUASAR method](#d3-the-method-framework-and-quasar-method)
      - [D.3.1 Overview](#d31-overview)
      - [D.3.2 Evaluation synthesis](#d32-evaluation-synthesis)
      - [D.3.3 Value assessment](#d33-value-assessment)
      - [D.3.4 Architectural analysis](#d34-architectural-analysis)
      - [D.3.5 Evaluation plan and report](#d35-evaluation-plan-and-report)
    - [D.4 Analysis of Alternatives (AoA)](#d4-analysis-of-alternatives-aoa)
      - [D.4.1 Overview](#d41-overview)
        - [D.4.1.1 General](#d411-general)
        - [D.4.1.2 Basic approach](#d412-basic-approach)
        - [D.4.1.3 Study objectives](#d413-study-objectives)
        - [D.4.1.4 Maturity assessment](#d414-maturity-assessment)
        - [D.4.1.5 Risk assessment](#d415-risk-assessment)
      - [D.4.2 Evaluation synthesis](#d42-evaluation-synthesis)
      - [D.4.3 Value assessment](#d43-value-assessment)
      - [D.4.4 Architectural analysis](#d44-architectural-analysis)
      - [D.4.5 Evaluation plan and report](#d45-evaluation-plan-and-report)
  - [Bibliography](#bibliography)
  - [IEEE notices and abstract](#ieee-notices-and-abstract)
    - [Important Notices and Disclaimers Concerning IEEE Standards Documents](#important-notices-and-disclaimers-concerning-ieee-standards-documents)
    - [Notice and Disclaimer of Liability Concerning the Use of IEEE Standards Documents](#notice-and-disclaimer-of-liability-concerning-the-use-of-ieee-standards-documents)
    - [Translations](#translations)
    - [Official statements](#official-statements)
    - [Comments on standards](#comments-on-standards)
    - [Laws and regulations](#laws-and-regulations)
    - [Copyrights](#copyrights)
    - [Photocopies](#photocopies)
    - [Updating of IEEE Standards documents](#updating-of-ieee-standards-documents)
    - [Errata](#errata)
    - [Patents](#patents)
    - [Abstract and keywords](#abstract-and-keywords)

---

## Cover and copyright pages (source lay-out, verbatim)

(ISO/IEC/IEEE 42030:2019, IDT)

National Standard of Canada

Software, systems and enterprise — Architecture evaluation framework

(ISO/IEC/IEEE 42030:2019, IDT)

Legal Notice for Standards

Canadian Standards Association (operating as “CSA Group”) develops standards through a consensus standards development process approved by the Standards Council of Canada. This process brings together volunteers representing varied viewpoints and interests to achieve consensus and develop a standard. Although CSA Group administers the process and establishes rules to promote fairness in achieving consensus, it does not independently test, evaluate, or verify the content of standards.

Disclaimer and exclusion of liability

This document is provided without any representations, warranties, or conditions of any kind, express or implied, including, without limitation, implied warranties or conditions concerning this document’s fitness for a particular purpose or use, its merchantability, or its non-infringement of any third party’s intellectual property rights. CSA Group does not warrant the accuracy, completeness, or currency of any of the information published in this document. CSA Group makes no representations or warranties regarding this document’s compliance with any applicable statute, rule, or regulation.

IN NO EVENT SHALL CSA GROUP, ITS VOLUNTEERS, MEMBERS, SUBSIDIARIES, OR AFFILIATED COMPANIES, OR THEIR EMPLOYEES, DIRECTORS, OR OFFICERS, BE LIABLE FOR ANY DIRECT, INDIRECT, OR INCIDENTAL DAMAGES, INJURY, LOSS, COSTS, OR EXPENSES, HOWSOEVER CAUSED, INCLUDING BUT NOT LIMITED TO SPECIAL OR CONSEQUENTIAL DAMAGES, LOST REVENUE, BUSINESS INTERRUPTION, LOST OR DAMAGED DATA, OR ANY OTHER COMMERCIAL OR ECONOMIC LOSS, WHETHER BASED IN CONTRACT, TORT (INCLUDING NEGLIGENCE), OR ANY OTHER THEORY OF LIABILITY, ARISING OUT OF OR RESULTING FROM ACCESS TO OR POSSESSION OR USE OF THIS DOCUMENT, EVEN IF CSA GROUP HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES, INJURY, LOSS, COSTS, OR EXPENSES.

In publishing and making this document available, CSA Group is not undertaking to render professional or other services for or on behalf of any person or entity or to perform any duty owed by any person or entity to another person or entity. The information in this document is directed to those who have the appropriate degree of experience to use and apply its contents, and CSA Group accepts no responsibility whatsoever arising in any way from any and all use of or reliance on the information contained in this document.

CSA Group is a private not-for-profit company that publishes voluntary standards and related documents. CSA Group has no power, nor does it undertake, to enforce compliance with the contents of the standards or other documents it publishes.

Intellectual property rights and ownership

As between CSA Group and the users of this document (whether it be in printed or electronic form), CSA Group is the owner, or the authorized licensee, of all works contained herein that are protected by copyright, all trade-marks (except as otherwise noted to the contrary), and all inventions and trade secrets that may be contained in this document, whether or not such inventions and trade secrets are protected by patents and applications for patents. Without limitation, the unauthorized use, modification, copying, or disclosure of this document may violate laws that protect CSA Group’s and/or others’ intellectual property and may give rise to a right in CSA Group and/or others to seek legal redress for such use, modification, copying, or disclosure. To the extent permitted by licence or by law, CSA Group reserves all intellectual property rights in this document.

Patent rights

Attention is drawn to the possibility that some of the elements of this standard may be the subject of patent rights. CSA Group shall not be held responsible for identifying any or all such patent rights. Users of this standard are expressly advised that determination of the validity of any such patent rights is entirely their own responsibility.

Authorized use of this document

This document is being provided by CSA Group for informational and non-commercial use only. The user of this document is authorized to do only the following:

If this document is in electronic form:

load this document onto a computer for the sole purpose of reviewing it;

search and browse this document; and

print this document if it is in PDF format.

Limited copies of this document in print or paper form may be distributed only to persons who are authorized by CSA Group to have such copies, and only if this Legal Notice appears on each such copy.

In addition, users may not and may not permit others to

alter this document in any way or remove this Legal Notice from the attached standard;

sell this document without authorization from CSA Group; or

make an electronic copy of this document.

If you do not agree with any of the terms and conditions contained in this Legal Notice, you may not load or use this document or make any copies of the contents hereof, and if you do make such copies, you are required to destroy them immediately. Use of this document constitutes your acceptance of the terms and conditions of this Legal Notice.

Standards Update Service

July 2020

Title: Software, systems and enterprise — Architecture evaluation framework

To register for e-mail notification about any updates to this publication

go to store.csagroup.org

click on Product Updates

The List ID that you will need to register for updates to this publication is 2428383.

If you require assistance, please e-mail techsupport@csagroup.org or call 416-747-2233.

Visit CSA Group’s policy on privacy at www.csagroup.org/legal to find out how we protect your personal information.

Canadian Standards Association (operating as “CSA Group”), under whose auspices this National Standard has been produced, was chartered in 1919 and accredited by the Standards Council of Canada to the National Standards system in 1973. It is a not-for-profit, nonstatutory, voluntary membership association engaged in standards development and certification activities.

CSA Group standards reflect a national consensus of producers and users — including manufacturers, consumers, retailers, unions and professional organizations, and governmental agencies. The standards are used widely by industry and commerce and often adopted by municipal, provincial, and federal governments in their regulations, particularly in the fields of health, safety, building and construction, and the environment.

Individuals, companies, and associations across Canada indicate their support for CSA Group’s standards development by volunteering their time and skills to Committee work and supporting CSA Group’s objectives through sustaining memberships. The more than 7000 committee volunteers and the 2000 sustaining memberships together form CSA Group’s total membership from which its Directors are chosen. Sustaining memberships represent a major source of income for CSA Group’s standards development activities.

CSA Group offers certification and testing services in support of and as an extension to its standards development activities. To ensure the integrity of its certification process, CSA Group regularly and continually audits and inspects products that bear the

CSA Group Mark.

In addition to its head office and laboratory complex in Toronto, CSA Group has regional branch offices in major centres across Canada and inspection and testing agencies in eight countries. Since 1919, CSA Group has developed the necessary expertise to meet its corporate mission: CSA Group is an independent service organization whose mission is to provide an open and effective forum for activities facilitating the exchange of goods and services through the use of standards, certification and related services to meet national and international needs.

For further information on CSA Group services, write to CSA Group

178 Rexdale Boulevard Toronto, Ontario, M9W 1R3 Canada

A National Standard of Canada is a standard developed by a Standards Council of Canada (SCC) accredited Standards Development Organization, in compliance with requirements and guidance set out by SCC. More information on National Standards of Canada can be found at www.scc.ca.

SCC is a Crown corporation within the portfolio of Innovation, Science and Economic Development (ISED) Canada. With the goal of enhancing Canada's economic competitiveness and social well-being, SCC leads and facilitates the development and use of national and international standards. SCC also coordinates Canadian participation in standards development, and identifies strategies to advance Canadian standardization efforts.

Accreditation services are provided by SCC to various customers, including product certifiers, testing laboratories, and standards development organizations. A list of SCC programs and accredited bodies is publicly available at www.scc.ca.

Standards Council of Canada 600-55 Metcalfe Street Ottawa, Ontario, K1P 6L5 Canada

Cette Norme Nationale du Canada n’est disponible qu’en anglais.

Although the intended primary application of this Standard is stated in its Scope, it is important to note that it remains the responsibility of the users to judge its suitability for their particular purpose.

®A trademark of the Canadian Standards Association, operating as “CSA Group”

National Standard of Canada

Software, systems and enterprise — Architecture evaluation framework

(ISO/IEC/IEEE 42030:2019, IDT)

Prepared by

International Organization for Standardization/ International Electrotechnical Commission

Reviewed by

®A trademark of the Canadian Standards Association, operating as “CSA Group”

Published in July 2020 by CSA Group

A not-for-profit private sector organization

178 Rexdale Boulevard, Toronto, Ontario, Canada M9W 1R3

To purchase standards and related publications, visit our Online Store at store.csagroup.org

or call toll-free 1-800-463-6727 or 416-747-4044.

ICS 35.080

ISBN 978-1-4883-3082-7

© 2020 Canadian Standards Association

All rights reserved. No part of this publication may be reproduced in any form whatsoever without the prior permission of the publisher.

CSA ISO/IEC/IEEE 42030:20 Software, systems and enterprise — Architecture evaluation framework

Software, systems and enterprise — Architecture evaluation framework (ISO/IEC/IEEE 42030:2019, IDT)

CSA Preface

Standards development within the Information Technology sector is harmonized with international standards development. Through the CSA Technical Committee on Information Technology (TCIT), Canadians serve as the SCC Mirror Committee (SMC) on ISO/IEC Joint Technical Committee 1 on Information Technology (ISO/IEC JTC1) for the Standards Council of Canada (SCC), the ISO member body for Canada and sponsor of the Canadian National Committee of the IEC. Also, as a member of the International Telecommunication Union (ITU), Canada participates in the International Telegraph and Telephone Consultative Committee (ITU-T).

For brevity, this Standard will be referred to as “CSA ISO/IEC/IEEE 42030” throughout.

At the time of publication, ISO/IEC/IEEE 42030:2019 is available from ISO and IEC in English only. CSA Group will publish the French version when it becomes available from ISO and IEC.

The International Standard was reviewed by the CSA TCIT under the jurisdiction of the CSA Strategic Steering Committee on Information and Communications Technology and deemed acceptable for use in Canada. From time to time, ISO/IEC may publish addenda, corrigenda, etc. The TCIT will review these documents for approval and publication. For a listing, refer to the Current Standards Activities page at standardsactivities.csa.ca. This Standard has been formally approved, without modification, by the Technical Committee and has been developed in compliance with Standards Council of Canada requirements for National Standards of Canada. It has been published as a National Standard of Canada by CSA Group.

© 2020 Canadian Standards Association

All rights reserved. No part of this publication may be reproduced in any form whatsoever without the prior permission of the publisher. ISO/IEC material is reprinted with permission. Where the words “this International Standard” appear in the text, they should be interpreted as “this National Standard of Canada”.

Inquiries regarding this National Standard of Canada should be addressed to CSA Group

178 Rexdale Boulevard, Toronto, Ontario, Canada M9W 1R3 1-800-463-6727 • 416-747-4000

www.csagroup.org

To purchase standards and related publications, visit our Online Store at store.csagroup.org or call toll-free 1-800-463-6727 or 416-747-4044.

July 2020 © 2020 Canadian Standards Association CSA/5

CSA ISO/IEC/IEEE 42030:20 Software, systems and enterprise — Architecture evaluation framework

This Standard is subject to review within five years from the date of publication, and suggestions for its improvement will be referred to the appropriate committee. The technical content of IEC and ISO publications is kept under constant review by IEC and ISO. To submit a proposal for change, please send the following information to inquiries@csagroup.org and include “Proposal for change” in the subject line:

Standard designation (number);

relevant clause, table, and/or figure number;

wording of the proposed change; and

rationale for the change.

July 2020 © 2020 Canadian Standards Association CSA/6

CSA Technical Committee on Information Technology

J. MacFie Microsoft Canada, Ottawa, Ontario, Canada

Category: Producer Interest

Chair

F. Coallier École de technologie supérieure (Université du Québec) (ÉTS),

Montréal, Québec, Canada

Category: General Interest

Vice-Chair

M. Ally Athabasca University, Edmonton, Alberta, Canada

Non-voting

R. Balderston Canadian Bank Note Company Limited, Ottawa, Ontario, Canada

Non-voting

L. Bertsch Horizon Technologies Inc., Victoria, British Columbia, Canada

Non-voting

J. Bérubé IDEgenic Inc.,

Bromont, Québec, Canada

Category: General Interest

T. Capel Comgate Engineering Ltd., Ottawa, Ontario, Canada Category: General Interest

J. A. Carter University of Saskatchewan, Saskatoon, Saskatchewan, Canada

Non-voting

P. Cotton Vancouver, British Columbia, Canada Non-voting

D. Ferguson Lyngsoe Systems Ltd., Mississauga, Ontario, Canada Category: User Interest

R. J. Gates Toronto, Ontario, Canada Non-voting

G. Gauthier Université du Québec à Montréal (UQAM), Montréal, Québec, Canada

Non-voting

P. J. Haighton Organization Metrics, Ottawa, Ontario, Canada Category: User Interest

V. A. Hailey The VHG Corporation, Gormley, Ontario, Canada

Non-voting

J. Harlan InterDigital Canada, Ltd., Montréal, Québec, Canada

Non-voting

C. Ho Innovation, Science and Economic Development Canada,

Ottawa, Ontario, Canada

Non-voting

G. K. Holman Crane Softwrights Ltd., Kars, Ontario, Canada

Non-voting

W. Jager ECD Technology Ltd., Stittsville, Ontario, Canada

Non-voting

A. W. Kark Witan Consulting Services Inc., Ottawa, Ontario, Canada

Non-voting

F. A. Khan TwelveDot Inc.,

Osgoode, Ontario, Canada

Category: Producer Interest

J. Knoppers Information Management Services Inc., Ottawa, Ontario, Canada

Category: User Interest

A. LaBonté Québec, Québec, Canada

Category: General Interest

G. Martin-Cocher BlackBerry Ltd.,

Mississauga, Ontario, Canada

Non-voting

C. P. Provencher Provencher InfoSec, Montréal, Québec, Canada Category: Producer Interest

A. Robinson Information Systems Architects, a Fountain Technical Services Group, Ottawa, Ontario, Canada

Non-voting

D. Sheppard ConCon Management Services Corp., Toronto, Ontario, Canada

Non-voting

S. Tremblay Excelsa Technologies Consulting Inc., Navan, Ontario, Canada

Non-voting

I. Verhappen CIMA+,

Calgary, Alberta, Canada

Category: User Interest

A. Kostruba CSA Group,

Toronto, Ontario, Canada

Project Manager

INTERNATIONAL STANDARD

ISO/IEC/

IEEE 42030

First edition

2019-07

Software, systems and enterprise — Architecture evaluation framework

Logiciel, systèmes et entreprise — Cadre d'évaluation de l'architecture

© ISO/IEC 2019

© IEEE 2019

COPYRIGHT PROTECTED DOCUMENT

© ISO/IEC 2019

© IEEE 2019

All rights reserved. Unless otherwise specified, or required in the context of its implementation, no part of this publication may be reproduced or utilized otherwise in any form or by any means, electronic or mechanical, including photocopying, or posting on the internet or an intranet, without prior written permission. Permission can be requested from either ISO at the address below or ISO’s member body in the country of the requester.

ISO copyright office Institute of Electrical and Electronics Engineers, Inc

CP 401 • Ch. de Blandonnet 8 3 Park Avenue, New York

CH-1214 Vernier, Geneva NY 10016-5997, USA

Tel. +41 22 749 01 11

Fax +41 22 749 09 47

copyright@iso.org stds.ipr@ieee.org

www.iso.org www.ieee.org

ii © IEEE 2019 – All rights reserved


---

## Foreword

ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) form the specialized system for worldwide standardization. National bodies that are members of ISO or IEC participate in the development of International Standards through technical committees established by the respective organization to deal with particular fields of technical activity. ISO and IEC technical committees collaborate in fields of mutual interest. Other international organizations, governmental and non-governmental, in liaison with ISO and IEC, also take part in the work. In the field of information technology, ISO and IEC have established a joint technical committee, ISO/IEC JTC 1.

The procedures used to develop this document and those intended for its further maintenance are described in the ISO/IEC Directives, Part 1. In particular, the different approval criteria needed for the different types of ISO documents should be noted. This document was drafted in accordance with the rules given in the ISO/IEC Directives, Part 2 (see www.iso.org/directives).

IEEE Standards documents are developed within the IEEE Societies and the Standards Coordinating Committees of the IEEE Standards Association (IEEE-SA) Standards Board. The IEEE develops its standards through a consensus development process, approved by the American National Standards Institute, which brings together volunteers representing varied viewpoints and interests to achieve the final product. Volunteers are not necessarily members of the Institute and serve without compensation. While the IEEE administers the process and establishes rules to promote fairness in the consensus development process, the IEEE does not independently evaluate, test, or verify the accuracy of any of the information contained in its standards.

Attention is drawn to the possibility that some of the elements of this document may be the subject of patent rights. ISO and IEC shall not be held responsible for identifying any or all such patent rights. Details of any patent rights identified during the development of the document will be in the Introduction and/or on the ISO list of patent declarations received (see www.iso.org/patents).

Any trade name used in this document is information given for the convenience of users and does not constitute an endorsement.

For an explanation of the voluntary nature of standards, the meaning of ISO specific terms and expressions related to conformity assessment, as well as information about ISO's adherence to the World Trade Organization (WTO) principles in the Technical Barriers to Trade (TBT), see www.iso

.org/iso/foreword.html.

This document was prepared by Joint Technical Committee ISO/IEC JTC 1, Information technology, Subcommittee SC 7, Software and systems engineering, in cooperation with the Systems and Software Engineering Standards Committee of the IEEE Computer Society, under the Partner Standards Development Organization cooperation agreement between ISO and IEEE.

Any feedback or questions on this document should be directed to the user’s national standards body. A complete listing of these bodies can be found at www.iso.org/members.html.

CSA ISO/IEC/IEEE 42030:20 v

## Introduction

The complexity of human-made systems has grown to an unprecedented level. This complexity leads to new opportunities and greater challenges for organizations that conceive, develop, industrialize, produce, maintain, utilize, recycle and dismantle enterprises, systems and software, and for various stakeholders that are impacted by these things. To address these opportunities and challenges, organizations increasingly apply concepts, principles, procedures and tools to drive better architecture strategies, make better architecture-related decisions, create more useful and effective architectures and improve architecture maturity. Architecture-related activities are not only strategic in nature; they are tactical and operational as well. Furthermore, the use of architecture frameworks, architecture description languages and generalist modeling languages have become common practice in commercial, public service, government, civil and military domains.

The concept of architecture used in this document goes beyond the case where the architecture entity is a system. Architecture is increasingly being applied to things not normally thought of as systems, including entities with system-like structure and behavior such as enterprises, services, data, business functions, mission areas, product lines, families of systems, software items, etc. This allows for a more generalized usage of the concept of architecture when the evaluation elements specified in this document are applied.

Architecture evaluations are performed for many reasons, such as:

a) determining if an entity of interest has been or is being architected in such a way that it fulfils its intended purpose (or can be changed in a way that suits a new purpose);

b) evaluating the effectiveness and suitability of an architecture towards addressing stakeholder needs and expectations;

c) identifying risks for mitigation;

d) identifying opportunities for the improvement of an entity or its architecture;

e) clarifying the problem space and stakeholder needs; and

f) assessing progress towards meeting architecture objectives.

Architecture evaluations can be performed on any kind of architecture, including a reference architecture, an architecture for a family of systems or an architecture for a product line where there are multiple kinds of architecture entities for a single architecture.

This document provides a generic, conceptual guiding framework that can be used for the planning, execution and documentation of architecture evaluations. Execution is addressed by specification of evaluation elements that can be used during performance of an evaluation effort. Planning and documentation are addressed by specification of work products for the evaluation effort. An organization using this document can establish specific frameworks for the work products and the evaluation elements that can be used as the basis for multiple, recurring architecture evaluation efforts. An organization can also establish tools, methods, best practices, capabilities and resources based on the generic framework provided in this document. The generic framework makes it easier to compare evaluations and evaluation frameworks used in specific cases. Implementation of the proposed architecture framework will in time result in improvement of architecture maturity of the organization.

vi CSA ISO/IEC/IEEE 42030:20

INTERNATIONAL STANDARD ISO/IEC/IEEE 42030:2019(E)

## Software, systems and enterprise — Architecture evaluation framework

### 1 Scope

This document specifies the means to organize and record architecture evaluations for enterprise, systems and software fields of application.

The aim of this document is to enable architecture evaluations that are used to:

a) validate that architectures address the concerns of stakeholders;

b) assess the quality of architectures with respect to their intended purpose;

c) assess the value of architectures to their stakeholders;

d) determine whether architecture entities address their intended purpose;

e) provide knowledge and information about architecture entities; f) assess progress towards achieving architecture objectives;

g) clarify understanding of problem space and of stakeholder needs and expectations;

h) identify risks and opportunities associated with architectures; and

i) support decision making where architectures are involved.

NOTE This document addresses the evaluation of an architecture and not an evaluation of the architecture description’s suitability. Matters concerning the evaluation of the architecture description fall within the scope of the architecture conceptualization and architecture elaboration processes as defined in ISO/IEC/IEEE 42020. However, it is sometimes the case that the architecture description is evaluated concurrently with the evaluation of the architecture itself.

The entity being evaluated can be of several kinds, as illustrated in the following examples: enterprise, organization, solution, system, subsystem, business, data (as a data element or data structure), application, information technology (as a collection), mission, product, service, software item, hardware item, etc. The kind of entity can also be a product line, family of systems, system of systems, etc. It also spans the variety of applications that utilize digital technology such as mobile, cloud, big data, robotics, Internet of Things (IoT), web, desktop, embedded systems, and so on.

The generic Architecture Evaluation (AE) framework specified in this document can be used in support of the Architecture Evaluation process defined in ISO/IEC/IEEE 42020. Specific frameworks can be derived from this generic framework, which can provide a mapping to the system life cycle processes in ISO/IEC/IEEE 15288 or to the software life cycle processes in ISO/IEC/IEEE 12207.

### 2 Normative references

There are no normative references in this document.

### 3 Terms and definitions

For the purposes of this document, the following terms and definitions apply.

ISO, IEC and IEEE maintain terminological databases for use in standardization at the following addresses:

- ISO Online browsing platform: available at https://www.iso.org/obp

- IEC Electropedia: available at http://www.electropedia.org/

- IEEE Standards Dictionary Online: available at: http: /ieeexplore.ieee.org/xpls/dictionary.jsp

NOTE Definitions for other terms typically can be found in ISO/IEC/IEEE 247651).

#### 3.1 architecture

fundamental concepts or properties of an entity in its environment (3.7) and governing principles for the realization and evolution of this entity and its related life cycle processes

Note 1 to entry: Architecture entity (3.3) is the term used in this document when referring to the entity being architected or the entity subject to architecture processes. The fundamental concepts or properties of the architecture entity are usually intended to be embodied in the entity’s components, the relationships between components, and the relationships between the entity and its environment.

Note 2 to entry: The concept of architecture used in this document applies broadly to the entity being architected or evaluated. This allows for a more generalized usage when the elements in this document are applied.

Note 3 to entry: The entity to be architected can be of several kinds, as illustrated in the following examples: enterprise, organization, solution, system, subsystem, business, data (as a data element or data structure), application, information technology (as a collection), mission, product, service, software item, hardware item, product line, family of systems, system of systems, etc. It also spans the variety of applications that utilize digital technology such as mobile, cloud, big data, robotics, Internet of Things (IoT), web, desktop, embedded systems, and so on.

Note 4 to entry: Representation of the concepts or properties of an entity and governing principles is captured in architecture models.

Note 5 to entry: Architectures can address a wide range of concerns (3.6) expressed, for example, through architecture views and models, as illustrated in the following examples associated with particular kinds of architectures such as: security architecture, functional architecture, physical architecture, resilience architecture, etc.

[SOURCE: ISO/IEC/IEEE 42020:2019, 3.3]

#### 3.2 architecture description

work product used to express an architecture (3.1)

Note 1 to entry: This document does not require the existence or use of an architecture description when performing an architecture evaluation (3.4). Some value (3.10) assessment methods do not demand existence of documented architecture models or views. Examples are customer focus group, expert panels and quality workshops where sufficient knowledge of the architecture is in the people participating in use of these methods. The same is true for architectural analysis in that not all methods applied here necessarily need an explicit description of the architecture.

[SOURCE: ISO/IEC/IEEE 42010:2011, 3.3, modified — The abbreviated term “AD” has been removed; Note 1 to entry has been added.]

1) System and software engineering — Vocabulary, available at www.computer.org/sevocab.

#### 3.3 architecture entity

thing being characterized by an architecture (3.1)

EXAMPLE The following are kinds of architecture entities that can be dealt with by the architecture processes: enterprise, organization, solution, system (including software systems), subsystem, business, data (as a data element or data structure), application, information technology (as a collection), mission, product, service, software item, hardware item, product line, family of systems, system of systems, collection of systems, collection of applications, etc.

Note 1 to entry: When referring to the architecture itself of these architecture entities, it is common practice to place the name of the kind of entity in front of the word architecture. For example, the phrase system architecture is used when the thing being dealt with during the architecting effort is a system. Likewise, for the other kinds of entities that are being dealt with during the architecting effort.

[SOURCE: ISO/IEC/IEEE 42020:2019, 3.6, modified — The words “considered, described, discussed, studied, or otherwise addressed during the architecting effort” have been replaced with “characterized by an architecture”.]

#### 3.4 architecture evaluation AE

judgment about one or more architectures (3.1) with respect to the specified evaluation objectives

EXAMPLE 1 Various kinds of judgments could be made during an architecture evaluation, such as validating that architectures address the concerns (3.6) of stakeholders (3.9), assessing the quality of architectures with respect to their intended purpose, assessing the value (3.10) of architectures or architecture entities to their stakeholders, determining whether architecture entities address their intended purpose, providing knowledge and information about architecture entities and identifying risks and opportunities associated with architectures.

EXAMPLE 2 Examples of architecture evaluations are provided in Annex C.

Note 1 to entry: A decision regarding disposition of the architecture is usually outside the scope of an AE effort, although it could be done in conjunction with the AE effort. The AE results are often reported to a decision maker who makes the actual determination of disposition based on those results and sometimes also on other factors (3.8) not considered by the AE effort. Sometimes this determination is called an “evaluation” but for the purpose of this document, the evaluation is limited to just the judgment with respect to relevant evaluation objectives.

#### 3.5 architecture evaluation framework

conventions, principles and practices for evaluating architectures (3.1) in a consistent and repeatable manner

EXAMPLE Examples of AE frameworks are provided in Annex D for the following cases: Architecture Tradeoff Analysis Method (ATAM), the Method Framework and QUASAR method and Analysis of Alternatives (AoA).

Note 1 to entry: This framework can be generic in nature or specific to a domain of application, a collection of concerns (3.6) to be examined or a methodology. This document defines a generic AE framework and a specific AE framework can be derived from the generic framework.

Note 2 to entry: An AE framework can enable AE efforts to be performed in a more consistent and repeatable manner.

Note 3 to entry: The evaluation framework can consist of different sub-architecture frameworks for an entity with many layers or levels. These could be defined and consolidated as part of the comprehensive architecture framework package.

#### 3.6 concern

matter of interest or importance to a stakeholder (3.9)

EXAMPLE Affordability, agility, availability, dependability, flexibility, maintainability, reliability, resilience, usability and viability are examples of concerns. Survivability, depletion, degradation, loss, obsolescence are examples of concerns. The PESTEL mnemonic is a reminder of other possible areas of concern: political, economic, social, technological, environmental, and legal. A longer list of examples is provided in 4.2.

Note 1 to entry: The concept of concern is similar to “quality attributes” as used in the ATAM. See Annex D for an overview of the ATAM approach. In ATAM, quality attributes are typically decomposed into concerns.

Note 2 to entry: The concept of concern is similar to the concept of quality. See A.4 for an overview of the quality

concept.

[SOURCE: ISO/IEC/IEEE 42020:2019, 3.8, modified — In EXAMPLE, reference to 4.2 has been added; Notes 1 and 2 to entry have been added.]

#### 3.7 environment

context determining the setting and circumstances of influences upon an architecture entity (3.3) or

upon which the architecture entity can have an influence

Note 1 to entry: There can be things beyond the environment that have an indirect impact on the architecture entity. It could be important to account for these indirect effects by incorporating these causative agents in the environment even though they are not usually considered to be within the immediate context. Value (3.10) chain analysis is an example of where this is done.

#### 3.8 factor

circumstance, fact or influence that contributes to a result or outcome

Note 1 to entry: A factor is something that contributes causally to a result. Factors identification can sometimes be driven by knowledge of desired effects.

#### 3.9 stakeholder

role, position, individual or organization having a right, share, claim or other interest in an architecture entity (3.3) or its architecture (3.1) that reflects their needs and expectations

[SOURCE: ISO/IEC/IEEE 42020:2019, 3.20]

#### 3.10 value

regard that something is held to deserve; the importance, worth, or usefulness of something to somebody

Note 1 to entry: Architecture evaluation (3.4) is focused primarily on the value of an architecture (3.1) with respect to stakeholder (3.9) concerns (3.6) or architecture objectives for that thing. However, sometimes the purpose of the evaluation effort is, by inference, to determine the impact of the architecture on the value of the architecture entity (3.3) when the entity is developed or evolved to align with the architecture concepts and properties.

Note 2 to entry: The determination of architecture value can take various aspects into account, such as worth, significance, importance, usefulness, benefit, and quality. These words have similar but not identical meaning. Worth is usually what one is willing to pay for something. Significance is about being worthy of attention. Importance is about the state or fact of being of great significance or value. Usefulness is about serving some purpose, or about being advantageous, helpful or of good effect. Benefit is about an advantage or profit gained from something. Quality is about the degree of excellence of something. Throughout this document, the term value is used to mean one or more of these other concepts, as appropriate.

Note 3 to entry: Even though a new architecture could be found to be of greater value with respect to the current situation, this needs to be balanced against the costs and risks of adopting the new architecture. So, it is not necessarily the case that when examining architecture alternatives, the one with the maximum value is proposed as the preferred choice since the extra cost or risk of this architecture might not be worth the extra burden. This is sometimes referred to as the benefit-cost ratio or some other term with similar meaning.

Note 4 to entry: Value is determined primarily in the Value Assessment Tier of the evaluation framework illustrated in Figure 1. Requirements on value assessment are specified in 6.2.

### 4 Conceptual foundation

#### 4.1 General

This clause introduces key concepts used in this document with respect to architecture evaluation. The terms and the concepts presented in this clause are used in Clauses 6 through 8 to express requirements. The conceptual model of architecture evaluation is presented in parts throughout this clause.

The generic AE framework work products and elements, illustrated in Figure 1 and specified in this document, can be used in support of the Architecture Evaluation process defined in ISO/IEC/IEEE 42020. Specific frameworks can be derived from this generic framework.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 1 — Generic architecture evaluation framework**

These specific frameworks may range from those targeting industry segments, such as automotive or refinery operations, to those targeting common business processes, such as portfolio management and program planning, and to those targeting common business architectures, such as banking, retail, insurance, telecom, travel and hospitality, etc. Specific frameworks allow the user to capture and reuse concepts common to many enterprises and thereby increase the efficiency with which architectures can be evaluated.

Architecture evaluation makes a judgment with respect to how well architecture objectives have been or will be achieved. It can provide answers to an identified set of questions to, for example, provide inputs to strategic decision making (such as whether it would be cheaper in the long run to modify an existing architecture to close value gaps), or to produce a new architecture that better addresses current and future stakeholder needs. An architecture evaluation can also provide inputs to decisions made at the operational and tactical levels. For example, the evaluation may provide useful information regarding capability limitations of the entity in question.

The subclauses below describe the elements used in each tier of the generic framework and describe the different kinds of specific frameworks that utilize these elements.

#### 4.2 Architecture evaluation context

Figure 2 depicts the context of architecture evaluation in terms of key concepts and the relations

between them.

NOTE 1 The graphical notation used in this document is a simplified version of entity-relationship modeling. NOTE 2 Only the key associations are shown in the diagrams.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 2 — Context of architecture evaluation**

The AE effort can be performed at many stages of entity development, including during conceptual design through to during the operation and maintenance. The evaluation may need to be updated to reflect changes as the entity design progresses through its lifecycle.

An AE effort is often performed to determine the potential or actual value of the associated architecture entity. However, the primary focus of the AE effort is on the value of the architecture itself even though the ultimate aim could be a determination of the value of the architecture entity, or the impact on the environment, or the impact on the business that uses the architecture entity, etc. But the value of the architecture entity or other benefits might be determined by some other effort, such as system analysis, requirements analysis, business needs analysis, portfolio management, program assessment and evaluation, environmental impact assessment, etc.

Architecture evaluation makes a judgment regarding the extent to which architecture objectives have been or will be achieved. Because of this, it is dealing with the degree to which the architecture provides things such as needs satisfaction, feasibility, understandability, usability desired qualities.

The environment within which the architecture entity is situated could provide strategic context for determining the ways in which the architecture evaluation is conducted. The environment could also be a key factor in understanding the nature of stakeholder concerns. States and modes of operation of the architecture entity are often from the usage perspective of entities in the environment.

Stakeholders have interests in the architecture or associated architecture entities. These interests (called concerns) are usually the primary focus of architecture evaluation. This judgment provided by the AE effort represents the extent to which stakeholder concerns have been or will be satisfied by decisions that affect the associated architecture entities or their environments. This judgment can also

represent the extent to which the architecture fulfills its intended purpose. Ways to measure this will be identified or specified during the AE effort along with the means by which these measures will be ascertained.

NOTE 3 Determination of the extent to which concerns are satisfied could entail either measurement of the degree to which something is done or a determination of whether something is true or not. Pass/fail criteria could need to be established prior to performing the evaluation. These criteria could be defined in the AE plan or could be established by the organization as a matter of policy or directive.

EXAMPLE 1 Stakeholders include people and organizations such as: users, operators, acquirers, owners, suppliers, developers, builders and maintainers. It also includes authorities engaged in certifying the architecture entity for a variety of purposes such as its readiness for use, conformance to legal provisions and compliance with regulations and policies with respect to safety, security, privacy, environmental impact, etc., as well as evaluators such as funding agencies, integration authorities, governance boards, management boards, client representatives and regulatory authorities. Stakeholders can go beyond individuals and organizations to also include things like governmental bodies, supply chains, value chains, institutions, and social groups.

EXAMPLE 2 Concerns include such things as: affordability, agility, alignment with business goals and strategies, autonomy, availability, behavior, business impact, capability, complexity, compliance to regulation, concurrency, control, cost, customer experience, data accessibility, deadlock, disposability, environment impact, error and exception handling, extensibility, evolvability, feasibility, flexibility, functionality, graceful degradation, information assurance, interoperability, inter-process communication, known limitations, maintainability, misuse, mission impact, modifiability, modularity, openness, performance, portability, privacy, quality of service, recoverability, reliability, resilience, resource utilization, schedule, security, shortcomings, state transitions through lifecycle, scalability, software and systems assurance (ISO/IEC 15026-1), structure, subsystem integration, architecture entity features, architecture entity properties, architecture entity purposes, usability, usage, viability, etc.

EXAMPLE 3 The PESTEL mnemonic is a reminder of other possible areas of concern: political, economic, social, technological, environmental, and legal. Survivability, depletion, degradation, loss and obsolescence are other examples of areas of concern. Other mnemonics that could be useful include STEEPLED that adds ethics and demographic factors, SPELIT that adds intercultural factors, STEER that adds regulatory factors and STEP that adds ecological factors.

EXAMPLE 4 Examples of value include such things as: physiological well-being, safety from harm, feelings, aesthetics, price, savings, sense of belonging, self-esteem and self-actualization.

Architecture principles, although not shown in the diagram, will shape the architecture and can perform a key role in the architecture evaluation. An understanding of these principles can help guide proper evaluation of an architecture. These principles will influence selection of AE factors used throughout the evaluation effort and help in the identification of relevant concerns. Architectural features and functions need to be consistent with the architecture principles. See Reference [17] and [18].

#### 4.3 Architecture evaluation tiers

##### 4.3.1 Evaluation synthesis

Synthesis involves the combination of results from multiple value assessments to determine to what extent the evaluation objectives will be achieved. Stakeholders who have concerns about the subject of the evaluation could have specific goals that should be addressed in the evaluation. (These concerns could be about the architecture, the architecture entity or both.) These goals should be considered when establishing the factors and objectives to be used in the evaluation. These goals might not correspond to the original goals for the architecture when it was initially conceived.

NOTE 1 The experts involved in the evaluation are also stakeholders and can bring important evaluation objectives that are not a known concern for traditional stakeholders (such as acquirer, user, service provider), but are concerns that the profession defines to be important (and where the evaluators could be the best placed stakeholders to represent the profession).

Architecture trade-offs are identified and characterized during architecture development. However, they can be revisited during the evaluation synthesis. Trade-offs among stakeholder concerns and feasibility limitations will be identified. Typical trade-offs to consider are the following: cost vs

performance, cost vs schedule, weight vs speed, accuracy vs timeliness, acquisition cost vs operating cost, ease of use vs security, flexibility vs predictability, agility vs robustness, risk vs reward, etc. Trade-offs could be with respect to the various factors within a single architecture or across alternative architectures under examination.

An AE effort examines one or more architectures with respect to potential stakeholder concerns about the associated architecture entities. Figure 3 depicts AE elements that can be used in an evaluation synthesis effort in terms of the key concepts and the relations between them. Most of these concepts are also used in related standards described in Annex B.

NOTE 2 Value is determined primarily in the Value Assessment Tier of the evaluation framework illustrated in

Figure 1. Requirements on value assessment are specified in 6.2.

The evaluation synthesis effort is the result of applying the concepts in the document during the evaluation of one or more architectures to determine their value to stakeholders or the extent to which the architecture objectives are satisfied.

NOTE 3 The evaluation synthesis effort is usually a non-trivial exercise that requires a pre-defined mapping of attributes and issues (gaps in desired outcomes) across the lineage of interactions between stakeholders and assets (and the services they rely upon to get their jobs done) and with respect to dependencies on the designs, development efforts and operations (used to deliver those assets and services), and finally with respect to the architectural artifacts relied upon by the designers, developers, users and operators.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 3 — Key concepts with respect to evaluation synthesis effort**

AE objectives are derived from one or more of the relevant concerns. One or more AE approaches are used to address the AE objectives. AE objectives assigned to an AE approach help to determine what concerns are relevant to that approach and what approaches are relevant to each concern. More than one approach could be used within a single evaluation effort to improve the ability to address different aspects of the architecture leading to more accurate, cost-effective and timely evaluations.

EXAMPLE 1 Examples of AE approaches are: review panel, prototype demonstration, system experiment, modeling and simulation, model walkthrough, technical analysis, compliance audit, concept review and user symposium.

EXAMPLE 2 Examples of AE objectives are:

- Will the business solution meet primary business needs?

- Is the system affordable?

- Will the service be dependable?

- Will the product have sufficient market penetration?

- What is the return on investment?

NOTE 4 The AE approach does not necessarily have to be highly structured or formal in nature, which is why this is not called a “method.” A method, on the other hand, is a particular form of procedure for accomplishing something, especially a systematic or established one.

NOTE 5 Evaluation of artifacts used to guide the design, development and delivery of assets and/or services can provide useful insights when assessing the value of architecture(s).

Evaluation factors are established based on relevant stakeholder concerns. The evaluation factors will contribute to addressing one or more of the evaluation objectives. The evaluation approach determines how necessary information will be gathered and processed, and how evaluation criteria will be applied on the processed information to generate evaluation results for use in the AE report.

The evaluation approach will use value assessment results as one of the criteria for making judgment(s) about the architecture. Other criteria for making these judgments could include such things as technical feasibility, operational suitability, backward/forward compatibility, technology maturity, budget constraints, time limits, window of opportunity, intellectual property advantages, etc.

NOTE 6 Evaluation factors could be derived from the desired outcomes that stakeholders are trying to obtain from the services and assets they rely upon.

EXAMPLE 3 Examples of AE factors are cost, schedule, performance and risk.

The AE plan guides management and execution of the AE effort by specifying, among other things, the evaluation objectives. It documents the purpose and scope of the evaluation and the circumstances under which the AE effort will be conducted. It documents the expected schedule and resources to deliver the evaluation results. The AE plan describes the evaluation approaches that will be driven by the evaluation objectives. The AE plan, if appropriate, can also specify the methods to be used for value assessment and architectural analysis.

The AE plan identifies necessary information sources, such as:

- those that are useful for creating an understanding of the architecture as a basis for generating evaluation results and drawing valid conclusions;

- those that are useful for creating an understanding of architecture entities as a basis for making relevant judgments about the architecture; and

- non-architecture-related sources, such as business plans, cost data, project schedules, software code and operating manuals.

NOTE 7 The activities in the Architecture Evaluation process specified in ISO/IEC/IEEE 42020 can be used as a guide when planning an AE effort. The planning activity specified in that AE process provides recommended tasks for planning an AE effort.

The overall conclusions of the AE effort are provided in AE reports along with any supporting data and information.

NOTE 8 More than one report could be needed to address different audiences or possibly be provided as interim reports along the way. For example, the sponsor could receive a highly detailed report while the decision maker could receive a high-level summary with only the factors most relevant to the decision at hand. There could be a sensitive or classified version of the report for people with the appropriate clearances and another version that only contains unclassified or less sensitive information.

##### 4.3.2 Value assessment

Value assessment is a determination regarding the amount and kind of value a stakeholder can expect from the architecture. Value can be defined as either a qualitative description or a quantitative extent of this expectation from the use, possession or operation of the architecture entity.

EXAMPLE 1 In some cases, the mere possession of an architecture entity can provide value to a stakeholder. For example, holding gold in the vault can provide security to the owner. A nation possessing a strong defensive capability can provide security to the citizens, hoping they never have to use such a capability.

Value assessment may identify gaps as well as opportunities for improving stakeholder value. Information from architectural analysis contributes to value assessment.

An AE approach specifies one or more value assessment objectives to be used in the value assessment effort. The use of particular value assessment methods for an AE effort can be influenced by the nature of the AE objectives, the available information sources, prior evaluations of this kind, available evaluation methods and tools, anticipated value assessment results and relevant architecture methodologies.

EXAMPLE 2 Examples of Assessment methods are: multi-attribute utility analysis (MAUA), mission impact assessment, business case analysis, socio-economic analysis, strategy-to-task analysis, user focus group, analysis of alternatives, environmental impact assessment, etc.

EXAMPLE 3 Examples of assessment objectives are:

- Will the business solution provide adequate productivity improvement?

- Is the system usable by available personnel?

- Will the service provide information in a timely manner?

- Will the product provide accurate and timely data?

Figure 4 depicts the elements that can be used in a value assessment effort in terms of the key concepts and the relations between them. Value assessment objectives are intended to satisfy the AE objectives and frame the relevant stakeholder concerns. Value assessment factors will frame the relevant AE factors.

EXAMPLE 4 Examples of value assessment factors are: development cost, operational cost, development time, training time, ease of use, maintainability, resilience, dependability.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 4 — Key concepts with respect to value assessment effort**

The assessment method may prescribe how necessary information will be gathered and processed, and how value assessment criteria will be applied on the processed information to generate value assessment results for use by an AE approach. The assessment method can be decomposed into specific activities, tasks, roles and artifacts pertinent to that method.

NOTE 1 Where available, one or more applicable value models can be referenced to assist in formulating the value assessment criteria. Value models are information structures that organize metrics for a set of value assessment factors such that they can serve as tools for assessing and managing value. These models are built over time based on best practices and lessons learned for a variety of value assessment factors. Value models can be developed by an industry, established within an organization or derived from the architecture requirements specification. See for example the Structured Metrics Meta-Model[67].

The assessment method will specify, if needed, objectives for one or more analysis methods to be employed and how the architectural analysis results will be used in the value assessment.

NOTE 2 If the information needed to perform a value assessment is already available from other sources (such as industry reports, design documentation, architecture descriptions, operational data, previous analyses, experiments, or demonstrations, etc.) then there can be no need to perform an architectural analysis.

##### 4.3.3 Architectural analysis

Architectural analysis examines the key attributes of an architecture, e.g. its characteristics along particular dimensions such as security, cost, performance, and so on, or the relevant attributes of the architecture entity, as well as actual or potential impacts on stakeholders or on the environment. It also examines architecture vision, principles, concepts and properties, etc. that are relevant to achieving the architectural analysis objectives. Analysis may also look at other aspects of the architecture such as forms, patterns, structures, behaviors, functions, flows, and so on, as well as examining the assumptions that were made about technologies, operations, policies, constraints, etc.

NOTE 1 Architectural analysis is optional since the information needed to generate value assessment results could already be available from other sources, hence removing the need to do analysis. The AE plan will indicate if and to what extent that architectural analysis is needed for a particular AE effort.

An assessment method will employ, if needed, one or more analysis methods. The employment of particular analysis methods for a particular AE effort can be influenced by the nature of the assessment objectives, the available information sources, prior analyses of this kind, available analysis methods and tools, anticipated analysis results and relevant architecture methodologies.

EXAMPLE 1 Examples of Analysis methods are: functional analysis; object oriented analysis, performance analysis, behavioral analysis, cost and schedule analysis, risk and opportunity analysis, failure modes, effects and criticality analysis (FMECA), focus group surveys and Delphi method. (All of these methods can be used for architectural analysis, as well as for architecture development.)

EXAMPLE 2 Examples of analysis objectives are:

- Will the business solution have a positive return on investment exceeding the hurdle rate?

- Is the system producible in large enough quantities to meet the target price?

- Will the service provide enough bandwidth to meet expected user demand?

- Will the product deliver data fast enough to meet its requirements?

- Will the equipment be reliable enough to provide the expected level of availability?

Figure 5 depicts the elements that can be used in an architectural analysis effort in terms of the key concepts and the relations between them. Analysis objectives are intended to satisfy the assessment objectives and frame the relevant stakeholder concerns. Analysis factors will frame the relevant assessment factors.

EXAMPLE 3 Examples of analysis factors are: operational latency, accuracy, resolution, mean time between failure, uptime.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 5 — Key concepts with respect to an architectural analysis effort**

The analysis method may prescribe how necessary information will be gathered and processed, and how analysis criteria will be applied on the processed information to generate analysis results for use by an assessment method. The analysis method can be decomposed into specific activities, tasks, roles and artifacts pertinent to that method.

Analysis factors are identified based on the relevant architectural features, functions, quality characteristics, conceptual properties, and so on, related to the analysis objectives.

EXAMPLE 4 Examples of Analysis factors are: functionality, performance, number of interfaces, types of message elements transmitted and received, size, weight, power, cyber security, threat vulnerability, resilience, latency and response time.

NOTE 2 A measures model can be used as a foundation for evaluating and assessing the quality of an architecture. The measures model can provide insights on how to achieve alignment back to functional, operational and performance measures for the organization. This can provide justification for investing in good architecture practices (part of the business case). See for example the Structured Metrics Meta-Model provided by OMG[67]. See Annex A for information about quality characteristics and value.

#### 4.4 Architecture evaluation conceptual model

The overall conceptual model used in this document for architecture evaluation is illustrated in Figure 6.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure 6 — Conceptual model for architecture evaluation**

#### 4.5 Comparison between assessment and analysis

Assessment is used to determine the extent to which an architecture provides value to stakeholders, where value is associated with addressing stakeholder concerns or meeting architecture objectives. Value is also associated with the extent to which the architecture is aligned to its intended purpose. A number of examples are provided in Table 1 to show the distinctions between assessment and analysis.

**Table 1 — Assessment vs analysis comparison**

| Characteristics | Value assessment | Architectural analysis |
|---|---|---|
| Goal orientation | Ends Objectives (often multi-level) | Means Objectives (often multi-level) |
| Results | Passes “judgment” | Matters of Fact |
| Breadth | Single, Unified Activity | Multiple, Separate Activities |
| Basis of work | Synthesis of analysis results | Technical and other analyses |
| Scope | Utility, Value, Worth, Priorities, Ranking, Trade-offs | Ways & Means |
| Focus | Effectiveness, Efficiencies, Equities | Performance determination, Limits identification (bounds) |
| Typical figures of merit | Measure of Effectiveness (MOE’s), Return on Investment (ROI), Breakeven Point, Key Success Factors (KSF’s) | Measures of Performance (MOP’s), Key Performance Parameters (KPP’s), Technical Performance Measures (TPM’s), Quality Metrics |
| Key items of interest | Competing Concerns, performing tradeoffs, achieving balance & robustness | Individual Concerns, determining system properties & characteristics |
| Primary questions of interest | So what? Who cares? What impacts? Why? Why not? | What, where, when, how, how much, how often? |

#### 4.6 Architecture evaluation factors

A factor is a circumstance, fact or influence that contributes to a result or outcome. It is something that contributes causally to a result. Identification of factors can sometimes be driven by knowledge of desired effects. Factors should be consistent with the architectural principles that shaped the architecture; and these principles should influence selection of factors to use in the evaluation.

The factors used in an architecture evaluation are central in helping to organize the evaluation effort and to achieve more transparent and understandable results.

EXAMPLE Vitruvius, the Roman architect, is known for asserting in his book De architectura[38] that a structure must exhibit the three qualities of firmitas, utilitas, venustas – that is, it must be solid, useful, beautiful. These are sometimes called the Vitruvian virtues or the Vitruvian Triad. This is a good example of factors that can be used in an architecture evaluation.

NOTE Examples of factors decomposition are provided in Annex A. Examples of value and quality factors are

provided in Annex A.

#### 4.7 Customized architecture evaluation frameworks

A generic AE framework is specified in this document that can be used in support of the Architecture Evaluation process defined in ISO/IEC/IEEE 42020. Specific frameworks can be derived from this generic framework. This clause describes the basic concepts regarding instantiation of specific AE frameworks while Clause 7 specifies provisions for instantiated specific AE frameworks.

The generic framework as illustrated by Figure 1 provides the elements and work products which could be instantiated or derived in specific frameworks. These specific frameworks may range from those targeting industry segments, like automotive or refinery operations, to those targeting common business processes, like portfolio management and program planning, and to those targeting common business architectures, like banking, retail, insurance, telecom, travel and hospitality, and so on. These frameworks allow the user to capture and reuse concepts common to many enterprises and thereby to increase the efficiency with which architectures can be evaluated.

Instantiation of specific frameworks will need adaptation to the requirements of the specific situation where an AE effort will be performed. The specific framework is usually defined or developed with respect to the processes, methods and tools used in the local context.

A specific AE framework provides a structure for reuse and evolution according to the evaluation needs. It may specify standardized practices for doing architecture evaluations. It can be used for:

- addressing specific evaluation objectives;

- evaluating certain kinds of concerns of stakeholders;

- addressing specific value assessment objectives; or

- addressing specific architectural analysis objectives.

A specific AE framework can instantiate or derive one or more tiers of the generic AE framework. In particular, it instantiates or derives one of the following:

- evaluation approach(es);

- assessment method(s); or

- analysis method(s).

NOTE The ATAM is an example of a specific AE framework that includes an evaluation approach based on the use of quality attribute workshops, and that specifies value assessment and analysis methods to be used. A summary description of ATAM is provided in Annex D.

A specific AE framework may include:

- corresponding objectives and factors;

- expected roles and responsibilities of evaluators;

- expected roles and responsibilities of stakeholders;

- conditions of applicability and guidance on proper utilization; and

- standardized format for evaluation results.

Communicating stakeholder perspectives requires clear semantics and terminology. The framework can include vocabulary, conventions, principles, practices, and applicable standards and regulatory requirements for evaluating architectures that can be generic in nature or specific to a domain of application, a collection of concerns to be examined or a particular methodology. The methods aggregated into a framework can share a common vocabulary, address similar concerns or be used together for other theoretical or practical considerations.

An AE approach can be developed afresh each time an evaluation is needed, or the constructs of the generic AE framework in this document can be used as the starting point and tailored for its particular use - either by way of specialization for a particular domain or with respect to concerns that are most relevant to the AE objectives.

#### 4.8 Tailoring

Tailoring may entail the addition, changing or removal of AE elements from the generic AE framework specified in this document. It may be performed for many reasons including the scale of the AE effort, the purpose of the evaluation, the intended uses of the AE results and the evaluation methodologies that will be employed. For example, if the purpose of the AE effort is to evaluate an architecture from an extant system or system design (i.e. to employ reverse architecting) then certain elements, such as architectural analysis, may not need to be performed.

In all cases where such tailoring of AE elements is employed, the rationale behind the tailoring shall be recorded. Recording the rationale will assist stakeholders in determining the value arising from the AE effort and the confidence they should attribute to its outcomes.

Tailoring may diminish the perceived value of a claim of conformance to this document. This is because it is difficult for other organizations to understand the extent to which tailoring may have removed

desirable provisions. An organization asserting a single-party claim of conformance to this document may find it advantageous to claim full conformance to a smaller set of AE elements rather than tailored conformance to a larger set of AE elements.

The AE elements described in this document are not intended to preclude or discourage the use of additional AE elements that organizations find useful. In particular, governance and directives of the organization will be applied for tailoring of the AE elements.

### 5 Conformance

#### 5.1 General

The requirements in this document are contained in Clauses 6 to 8. Situations in which claims of conformance with the provisions of this document can be made include those in 5.2 and 5.3.

NOTE An organization can have its own set of requirements or directives with respect to following the provisions of this document. For example, compliance can be limited to a set of architecture evaluation elements (objectives, approaches, factors and/or results) or work products (plan and/or report). This allows the architecture evaluation effort to be aligned and consistent with other efforts within the organizations of either those requesting evaluation to be done or those doing the evaluation.

EXAMPLE Specification of conformance for architecture evaluation objectives and results can be a way to establish contracts for the architecture evaluation efforts with freedom for the organization in charge of the architecture evaluation execution.

#### 5.2 Creating AE artifacts

Claims of conformance with the provisions of this document can be made in the following situations:

- When conformance is claimed for a customized architecture evaluation framework, the claim shall demonstrate that the architecture evaluation framework meets the requirements specified in Clause 7.

- When conformance is claimed for an architecture evaluation plan, the claim shall demonstrate that the requirements specified in 8.1 and 8.2 are met.

- When conformance is claimed for an architecture evaluation report, the claim shall demonstrate that the requirements specified in 8.1 and 8.3 are met.

#### 5.3 Using generic AE framework to conduct AE efforts

Claims of conformance with the provisions of this document can be made in the following situations:

a) When conformance is claimed for an evaluation synthesis effort, the claim shall demonstrate that the evaluation approach used meets the requirements specified in 6.1.

NOTE 1 Evaluation synthesis is the effort conducted using the elements in the Evaluation Synthesis Tier of the generic AE framework specified in this document. It involves the combination of results from multiple value assessments to determine to what extent the evaluation objectives will be achieved. See 4.3.1 for more information on this concept.

b) When conformance is claimed for a value assessment effort, the claim shall demonstrate that the assessment method used meets the requirements specified in 6.2.

NOTE 2 Value assessment is the effort conducted using the elements in the Value Assessment Tier of the generic AE framework specified in this document. It is concerned with a determination of the regard that something is held to deserve, or the importance, worth or usefulness of something to somebody. See 4.3.2 for more information on this concept. A comparison between the concepts of assessment and analysis is provided in 4.5.

c) When conformance is claimed for an architectural analysis effort, the claim shall demonstrate that the analysis method used meets the requirements specified in 6.3.

NOTE 3 Architectural analysis is the effort conducted using the elements in the Architectural Analysis Tier of the generic AE framework specified in this document. It is concerned with an examination of the key attributes of an architecture, e.g. its characteristics along particular dimensions such as security, cost, performance, and so on, or the relevant attributes of the architecture entity, as well as actual or potential impacts on stakeholders or on the environment. See 4.3.3 for more information on this concept. A comparison between the concepts of assessment and analysis is provided in 4.5.

d) When conformance is claimed for an architecture evaluation effort, the claim shall demonstrate that the requirements specified in Clauses 7 and 8 are met.

NOTE 4 Architectural evaluation is concerned with a judgment about one or more architectures with respect to the specified evaluation objectives. See 4.2 for more information on this concept.

#### 5.4 Verbal forms for the expression of provisions

Requirements of this document are marked by the use of the verb “shall”. Recommendations are marked by the use of the verb “should”. Permissions are marked by the use of the verb “may”. In the event of a conflict between normative figures and text, the text shall take precedence.

### 6 Architecture evaluation framework elements

#### 6.1 Evaluation synthesis

##### 6.1.1 General requirements

NOTE 1 Figure 3 depicts AE elements that can be used in an evaluation synthesis effort in terms of the key concepts and the relations between them. Most of these concepts are also used in related standards described in Annex B.

An architecture evaluation includes the following elements as specified in the subsequent subclauses:

a) one or more AE objectives;

b) one or more AE approaches;

c) one or more AE factors; and

d) one or more AE results.

The AE effort shall:

- identify one or more AE approaches to address the AE objectives;

- address the relevant AE factors;

- produce the appropriate AE results;

- determine the extent to which the AE objectives are met;

- address relevant concerns;

- address relevant business drivers and mission drivers;

- determine the value of the architecture; and

- produce one or more AE reports.

The AE effort shall examine the AE results to determine the extent to which the AE objectives have been met. The AE effort may need to integrate and examine the AE results coming from multiple AE approaches used in the evaluation.

The AE effort may determine the value of architecture entities associated with the architecture under evaluation.

The AE effort may specify the value assessment objectives that will satisfy the specified AE objectives. The AE effort may specify how to integrate AE results into the architecture description, when there is one.

NOTE 2 While it is desirable to have a documented architecture description for use in the architecture evaluation, producing a description is sometimes not feasible with resources available, or it could be unnecessary if the architecture is based on widely accepted solutions in the domain. This document does not mandate the use of an explicit architecture description, but this document does encourage documentation of evidence collected in support of the architecture evaluation, including any understanding of the architecture obtained through various mechanisms, either generated during the evaluation or used in the evaluation.

Evaluation approaches, assessment methods and analysis methods may identify factors not previously associated with a stakeholder concern or architecture feature which are nonetheless determined to be a critical factor with respect to having the architecture entity be fit-for-purpose. When identified, the relevant reports should specify the newly identified factors with recommendations for the elaboration of value assessment factors, architecture evaluation factors, concern definition and stakeholder identification sufficient to address the newly identified criticality.

##### 6.1.2 Architecture evaluation objectives

Each AE objective shall:

a) address one or more stakeholder concerns;

b) address relevant business drivers and mission drivers;

c) be expressed in terms of AE factors; and

d) be expressed in terms of expected or desired values or value range for the AE factors, when applicable.

EXAMPLE Examples of AE objectives are:

- Will the business solution meet primary business needs?

- Is the system affordable?

- Will the service be dependable?

- Will the product have sufficient market penetration?

Each AE objective shall be a statement describing the extent to which the AE effort will address one or more of the relevant stakeholder concerns, such that they can form the basis for deriving value assessment objectives.

The AE objectives should be compatible with the established purpose and scope for the AE effort. The AE objectives may be expressed as questions to facilitate understanding of their intent.

NOTE The reason for expressing the questions in such a manner and with sufficient elaboration is to ensure better understanding of the objectives by the assessors and stakeholders..

##### 6.1.3 Architecture evaluation approaches

Each AE approach shall provide the means to:

a) identify AE objectives to be addressed;

b) specify AE factors to be used and AE criteria to be applied;

c) specify one or more value assessment objectives, aligning them to the AE objectives;

d) specify one or more assessment methods to address the value assessment objectives;

e) specify the value assessment factors to be used, aligning them to relevant stakeholder concerns; f) specify value assessment criteria to be applied;

g) specify the type and form of value assessment results to be examined when executing the AE approach;

h) specify how and when the identified assessment methods will be employed;

i) specify the mechanisms through which the AE criteria will be applied on AE factors; and

j) generate the AE results.

Each AE approach should provide the means to:

k) examine the value assessment results to determine the extent to which the stakeholder concerns have been addressed;

l) examine the value assessment results to determine the extent to which the value assessment objectives have been met;

m) identify and characterize trade-offs between competing stakeholder concerns; and

n) formulate findings and recommendations to be included in the AE results.

An AE approach may be specified as an AE framework for reuse in multiple architecture evaluations. The AE framework specification should be in accordance with Clause 7.

EXAMPLE The ATAM is an example of a published AE framework. ATAM is described in Annex D.

##### 6.1.4 Architecture evaluation factors

Each AE factor used in the AE approach shall:

a) be representative of one or more stakeholder concerns;

b) be in a normalized form suitable for comparison or integration with other factors;

c) contribute to one or more AE objectives; and

d) be usable by the AE approach to generate the AE results. EXAMPLE Examples of AE factors are: cost, schedule, performance, risk. Each AE factor should be specific and measurable.

Each AE factor should enable the AE effort to produce accurate, reliable and timely results.

NOTE The recommendations above are based on the general rule that good metrics are SMART – Specific, Measurable, Accurate, Reliable and Timely.

##### 6.1.5 Architecture evaluation results

Each AE result shall be traceable to inputs used, the AE criteria applied to derive it and the AE approach that applied the criteria.

Each AE result should:

a) be the outcome of an impartial and objective examination done as part of using the AE approach;

b) document assumptions, risks and caveats to be taken into account while using the result; and

c) include a statement of estimated uncertainty of the stated result.

Discrepancies between AE results from different AE approaches used should be explained.

#### 6.2 Value assessment

##### 6.2.1 General requirements

NOTE 1 Figure 4 depicts the elements that can be used in a value assessment effort in terms of the key concepts and the relations between them. Value assessment objectives are intended to satisfy the AE objectives and frame the relevant stakeholder concerns. Value assessment factors will frame the relevant AE factors.

NOTE 2 Information on the nature of value and how it relates to the concept of quality is provided in Annex A.

Each value assessment includes the following elements as specified in the subsequent subclauses:

a) one or more value assessment objectives;

b) one or more value assessment methods;

c) one or more value assessment factors, and

d) one or more value assessment results.

The value assessment effort shall examine the value assessment results to determine the extent to which the value assessment objectives have been met. The value assessment effort may need to integrate and examine the architectural analysis results coming from multiple architectural analysis methods used in the evaluation. The value assessment effort may need to explain discrepancies between architectural analysis results from different architectural analysis methods used.

Each value assessment effort shall:

- specify value assessment objectives to address the relevant concerns;

- identify one or more value assessment methods to address the value assessment objectives;

- address the relevant value assessment factors;

- address relevant concerns;

- address relevant business drivers and mission drivers;

- determine the extent to which the value assessment objectives are met; and

- produce the appropriate value assessment results.

Each value assessment effort should be compatible with the established purpose and scope for the

AE effort.

Value assessment should determine the lineage from architecture artifacts to design, construction, and ultimately the products and services used to deliver value to stakeholders (note that there are no direct relationships between architecture and stakeholders).

Each value assessment effort may specify the architectural analysis objectives that will satisfy the specified value assessment objectives.

##### 6.2.2 Value assessment objectives

Each value assessment objective shall be a statement describing the extent to which the value assessment effort will address one or more of the relevant stakeholder concerns, such that they can form the basis for deriving architectural analysis objectives.

The value assessment objectives may be expressed as questions to facilitate understanding of their intent.

Each value assessment objective shall be expressible in terms of the kind of value a stakeholder expects to receive. Each value assessment objective shall include a qualitative description or quantitative extent of this expectation from use or operation of the architecture entity, or in its possession.

EXAMPLE 1 A qualitative description could state something like "profit should increase" while a quantitative extent could state something like "profit should increase by 50 % in 3 years”.

NOTE Information on the nature of value and how it relates to the concept of quality is provided in Annex A.

Each value assessment objective shall:

a) satisfy one or more AE objectives;

b) be expressed in terms of value assessment factors; and

c) be expressed in terms of expected or desired values or value range for the AE factors; and

d) enable identification of the information necessary to assess achievement of the value assessment objective.

EXAMPLE 2 Examples of value assessment objectives are:

- Will the business solution provide adequate productivity improvement?

- Does the system support level 5 trained personnel to control the factory process flow?

- Will the service provide information in a timely manner?

- Will the product provide accurate and timely data?

##### 6.2.3 Value assessment methods

Each value assessment method shall provide the means to:

a) address assigned value assessment objectives;

b) specify the value assessment factors to be used;

c) specify value assessment criteria to be applied;

d) specify the mechanisms through which the value assessment criteria will be applied on value assessment factors;

e) formulate findings and recommendations to be included in the value assessment results; and f) generate the value assessment results.

Each value assessment method should provide the means to:

— identify, if needed, one or more architectural analysis methods pertaining to the value assessment objectives it addresses;

NOTE 1 Architectural analysis is optional since the information needed to generate value assessment results could already be available from other sources, hence removing the need to do analysis. The AE plan will indicate if and to what extent that architectural analysis is needed for a particular AE effort.

- define architectural analysis objectives for the identified architectural analysis methods, derived from the value assessment objectives they address;

- specify how and when the identified analysis methods will be employed;

NOTE 2 The mechanism for using the information produced by architectural analysis can include specific quantitative methods such as value-quality correlation mechanism, utility functions, statistical functions, constructed scale, objective functions, linear weighted sum, harmonic average or other integrative mechanisms. It can also include specific qualitative methods such as logical reasoning, grounded theory, matrix analysis, discourse analysis, characteristics typology, inductive reasoning or generalization.

- determine the extent to which the architectural analysis objectives have been met;

- determine completeness of coverage for the AE approach that employs it and the relevant value assessment objectives defined by that AE approach;

- determine the extent to which relevant stakeholder concerns have been addressed; and

- formulate findings and recommendations to be included in the value assessment results.

Value assessment methods may be specified as an AE framework for reuse in multiple architecture evaluations. The AE framework specification should be in accordance with Clause 7.

##### 6.2.4 Value assessment factors

Each value assessment factor used in the value assessment method shall:

a) be representative of one or more AE factors;

b) be in a normalized form suitable for comparison or integration with other factors;

c) contribute to one or more value assessment objectives; and

d) be usable by the value assessment method to generate the value assessment results. Each value assessment factor should be specific and measurable.

Each value assessment factor should enable the value assessment effort to produce accurate, reliable and timely results.

NOTE The recommendations above are based on the general rule that good metrics are SMART – Specific, Measurable, Accurate, Reliable and Timely.

##### 6.2.5 Value assessment results

Each value assessment result shall be traceable to inputs used, the value assessment criteria applied to derive it and the assessment method that applied the criteria.

EXAMPLE Examples of the kinds of value assessment results are things like customer satisfaction index, experience index, interaction quality index, communication experience index, quality of experience, safety index.

Each value assessment result should:

a) be the outcome of an impartial and objective assessment done as part of using a value assessment method;

b) document assumptions, risks and caveats to be considered while using the result; and

c) include a statement of estimated uncertainty of the stated result.

If there were any limitations of the method or in the scope considered while producing the value assessment results, this should be factored in while integrating the results into a holistic value assessment effort.

Discrepancies between architecture analysis results from different architectural analysis methods used should be explained.

#### 6.3 Architectural analysis

##### 6.3.1 General requirements

NOTE 1 Figure 5 depicts the elements that can be used in an architectural analysis effort in terms of the key concepts and the relations between them. Analysis objectives are intended to satisfy the assessment objectives and frame the relevant stakeholder concerns. Analysis factors will frame the relevant assessment factors.

NOTE 2 Architectural analysis is optional since the information needed to generate value assessment results could already be available from other sources, hence removing the need to do analysis. The AE plan will indicate if and to what extent that architectural analysis is needed for a particular AE effort.

Each architectural analysis includes the following elements as specified in the subsequent sub clauses:

a) one or more architectural analysis objectives;

b) one or more architectural analysis methods;

c) one or more architectural analysis factors; and

d) one or more architectural analysis results. Each architectural analysis effort shall:

- specify architectural analysis objectives to address the relevant concerns;

- identify one or more architectural analysis methods to address the architectural analysis objectives;

- address the relevant architectural analysis factors;

- address relevant concerns;

- address relevant business drivers and mission drivers;

- determine the extent to which the architectural analysis objectives are met; and

- produce the appropriate architectural analysis results.

Each architectural analysis effort should be compatible with the established purpose and scope for the

AE effort.

The architectural analysis effort shall examine the architectural analysis results to determine the extent to which the architectural analysis objectives have been met. The architectural analysis effort may need to integrate and examine the architectural analysis results coming from multiple architectural analysis methods used in the evaluation. The architectural analysis effort may need to explain discrepancies between architectural analysis results from different architectural analysis methods used.

##### 6.3.2 Architectural analysis objectives

Each architectural analysis objective shall be a statement describing the extent to which the architectural analysis effort will address one or more of the relevant stakeholder concerns, such that they can form the basis for performing the architectural analysis.

Each architectural analysis objective shall:

a) satisfy one or more value assessment objectives;

b) be expressed in terms of expected or desired values or value range for the architectural analysis factors, when applicable; and

c) enable identification of the information necessary to assess achievement of the architecture analysis objective.

EXAMPLE Examples of architectural analysis objectives are:

- Will the business solution have a positive return on investment exceeding the hurdle rate?

- Is the complexity of the system justified given its intended purpose?

- Is the system producible in large enough quantities to meet the target price?

- Is the system maintainable with the expected number of maintenance personnel and their skill levels?

- Does the software application adequately handle cyber threats?

- Will the service provide enough bandwidth to meet expected user demand?

- Will the product deliver data fast enough to meet its requirements?

The architectural analysis objectives may be expressed as questions to facilitate understanding of

their intent.

##### 6.3.3 Architectural analysis methods

Each architectural analysis method shall provide the means to:

a) address assigned architectural analysis objectives;

b) identify the relevant architecture attributes;

c) specify architectural analysis factors to be used;

d) specify architectural analysis criteria to be applied; and

e) generate the architectural analysis results.

Each architectural analysis method should provide the means to:

- specify the mechanisms through which the architectural analysis criteria will be applied on architectural analysis factors;

- specify how and when particular analytical tools and techniques will be used;

- specify how and when particular measurement protocols will be used; and

- determine quantitative or qualitative measurements or indicators for relevant architecture or architecture entity attributes;

- examine architectural analysis factors to determine the extent to which the architectural analysis objectives have been met;

- determine completeness of coverage for the value assessment method that employs it and the relevant architectural analysis objectives defined by that value assessment method;

- determine the extent to which relevant stakeholder concerns have been addressed; and

- formulate findings and recommendations to be included in the architectural analysis results.

Each architectural analysis method may provide the means to:

- identify an architectural analysis factor not driven by a value assessment factor and thus lacking a related stakeholder concern, but which is nonetheless determined to be a critical factor with respect to having the architecture entity be fit-for-purpose; and

- report the newly identified architectural analysis factor with recommendations for the elaboration of value assessment factors, architecture evaluation factors, concern definition and stakeholder identification sufficient to address the newly identified criticality.

Architectural analysis methods may be specified as an AE framework for reuse in multiple architecture evaluations. The AE framework specification should be in accordance with Clause 7.

##### 6.3.4 Architectural analysis factors

Each architectural analysis factor used in the analysis method shall:

a) be representative of one or more value assessment factors;

b) be in a normalized form suitable for comparison or integration with other factors;

c) contribute to one or more architectural analysis objectives; and

d) be usable by the analysis method to generate the architectural analysis results. Each architectural analysis factor should be specific and measurable.

Each architectural analysis factor should enable the architectural analysis effort to produce accurate, reliable and timely results.

NOTE The recommendations above are based on the general rule that good metrics are SMART – Specific, Measurable, Accurate, Reliable and Timely.

##### 6.3.5 Architectural analysis results

Each architectural analysis result shall be traceable to inputs used, architectural analysis factors and architectural analysis criteria used to derive it and the analysis method that applied the criteria.

EXAMPLE Examples of architectural analysis results are readiness level, availability level, response time, safety level, reliability level, foot print, resource utilization.

Each architectural analysis result should:

a) be the outcome of an impartial and objective analysis done as part of using an analysis method;

b) document assumptions, risks, and caveats to be considered while using the result;, and

c) include a statement of estimated uncertainty of the stated result. Analysis results should be documented and retained for future reference.

If there were any limitations of the method or in the scope considered while producing the architectural analysis results, this should be factored in while integrating the results into a holistic architectural analysis effort.

Discrepancies between architecture analysis results from different architectural analysis methods used should be explained.

### 7 Customized architecture evaluation frameworks

#### 7.1 General requirements

NOTE 1 To reduce the work involved in generating the information required in an AE effort, and recognizing that the approaches and methods are typically knowledge elements that are reused across applicable contexts, this document defines the concept of a generic AE framework that can be used to derive specific frameworks relevant for AE objectives and sustaining the needed AE effort.

NOTE 2 Tailoring is not to be confused with the development of a customized AE framework. Tailoring (as described in 4.8) is taking some things from the standard and adopting it for conformance. On the other hand, customization is deriving a specific version of the AE framework that is applicable to a particular organization or situation.

A customized AE framework shall include:

a) information identifying the framework (e.g. name, identification code, version number);

b) information identifying the intended uses and users;

c) information identifying the roles and responsibilities of stakeholders;

d) AE plan outline of required and optional content;

e) AE report outline of required and optional content; and f) conditions of applicability.

EXAMPLE The following are example conditions of applicability:

- The AE framework is applicable where an architecture entity involves planning safety for manned vs unmanned transportation activities.

- The AE framework is applicable during the pre-concept phase of major acquisition programs.

- The AE framework is applicable when the evaluation is for an architecture entity that is very small and can be implemented in less than a month.

A customized AE framework should provide a completed, populated customizable model of an AE effort or some aspect of it. The customized AE framework should state how an AE effort should be done and what information should be captured.

A customized AE framework should include:

- questions that can be answered using the specified approaches and methods;

- identification of one or more stakeholder concerns framed by the framework;

- correlation of concerns to specific stakeholders to express the context of each concern;

- assignment of a priority for each concern (e.g. High, Medium, Low);

- identification of associated compliance document(s) to help assess risk of non-compliance;

- specify the form and format of the informational inputs needed by the method;

- include a mechanism for estimating time for:

e.1) preparation and training of resources,

e.2) conducting the evaluation, and

e.3) post-evaluation analysis and documentation;

- identify the form and/or format for expressing method outputs as the results; and

— provide a mechanism for correlating the inputs used and the criteria to be applied to each result

produced.

A customized AE framework should include adaptation guidelines if adaptation is allowed. The AE framework should enable specialization of the objectives, factors and criteria of its elements based on the objectives for which an architecture evaluation is sought.

A customized AE framework should enable adaptation for use with respect to the business and operational domain of the architecture entity of interest, evaluation purpose and scope, lifecycle stage of the architecture or architecture entity, and resources available for the evaluation effort.

A customized AE framework may include:

- sample of an AE plan;

- sample of an AE report;

- sample of an implementation of an evaluation synthesis approach;

- sample of an implementation of a value assessment method; and

- sample of an implementation of an architectural analysis method.

#### 7.2 Framework requirements for architecture evaluation

The framework shall specify the characteristics of its evaluation elements in accordance with the requirements of 6.1. The framework may include specification of relevant assessment objectives in accordance with the requirements of 6.2. The framework may include specification of relevant analysis objectives in accordance with the requirements of 6.3.

The framework may include AE objectives, factors and criteria.

#### 7.3 Framework requirements for value assessment

The framework shall specify the characteristics of its evaluation elements in accordance with the requirements of 6.2. The framework may include specification of relevant analysis objectives in accordance with the requirements of 6.3.

The framework may include value assessment objectives, factors and criteria.

#### 7.4 Framework requirements for architectural analysis

The framework shall specify the characteristics of its evaluation elements in accordance with the requirements of 6.3.

The framework may include architectural analysis objectives, factors and criteria.

#### 7.5 Framework requirements for architecture evaluation work products

The framework shall specify the characteristics of AE work products in accordance with the requirements of Clause 8.

### 8 Architecture evaluation work products

#### 8.1 General requirements

The AE effort shall produce an AE plan (in accordance with the requirements in 6.2).

A separate plan may be produced for each tier of the AE effort.

NOTE The activities in the Architecture Evaluation process specified in ISO/IEC/IEEE 42020 can be used as a guide when planning an AE effort. The planning activity specified in that AE process provides recommended tasks for planning an AE effort.

The AE effort shall produce one or more AE reports (in accordance with the requirements in 6.3).

The AE report may include required items “by reference” by pointing to the AE plan, where appropriate. A separate report may be produced for each tier of the AE effort.

#### 8.2 Architecture evaluation plan

##### 8.2.1 AE plan requirements

The AE plan shall include:

a) purpose and scope of the AE effort;

b) identification of previous related AE efforts;

c) identification of architecture(s) to be evaluated;

d) identification of architecture description(s) to be used, if applicable;

e) identification of architectural principle(s) that were used to develop the architecture(s); f) identification of relevant stakeholders;

g) identification of driving stakeholder concerns to be addressed;

h) identification of relevant business drivers and mission drivers;

i) definition of AE objectives and their relative importance;

j) identification of AE approaches to be employed;

k) identification of applicable constraints and conditions;

l) identification of resources required for the AE effort;

m) identification of referenced data that needs to be archived and/or baselined;

n) identification of necessary information sources; and

o) identification of relevant compliance documents, technical documentation, contract documentation, etc.

##### 8.2.2 AE plan recommendations

The AE plan should include:

a) definition of quality management procedures for the AE effort;

b) definition of architecture governance procedures for the AE effort;

c) specification of required precision and accuracy of the AE results;

d) specification of the required form and content of needed inputs;

e) specification of the required form and content of needed outputs; f) specification of the required form and content of the AE report;

e.g) identification of risks and opportunities for the AE effort;

e.h) identification of opportunity pursuit plans for critical items among the identified opportunities; and

e.i) identification of risk management plans for critical items among the identified risks.

The AE plan should provide the capability for the customer, requestor or sponsor, if applicable, to affix their approval.

The AE plan should provide the capability for the approving authority, if applicable, to affix their approval.

The AE plan should include the recommended items from ISO/IEC/IEEE 15289:

- date of issue and status;

- issuing organization;

- references (applicable policies, laws, standards, contracts, requirements and other plans and procedures);

- approval authority;

- planned activities and tasks;

- identification of tools, methods and techniques;

- schedules;

- budgets and cost estimates;

- resources and their allocation, including human resources, technical resources (infrastructure) and tools;

- responsibilities and authority, including the senior responsible owner and immediate process or service owner;

- interfaces among parties involved;

- risks and risk identification, assessment and mitigation activities;

- quality assurance and performance measures;

- environment, infrastructure, security and safety;

- training;

- approach for technical and management review and reporting;

- other plans (plans or task descriptions that expand on the details of a plan);

- glossary;

- change procedures and history; and

- termination process.

##### 8.2.3 AE plan permissions

The AE plan may include:

a) identification of sponsor, if any;

b) assumptions made in planning the AE effort;

c) ground rules established in planning the AE effort;

d) work breakdown structure;

e) definition of how the AE effort will be organized;

f) definition of timeframe for conducting the AE effort;

g) identification of AE frameworks to be employed, if applicable;

h) identification of assessment methods to be employed;

i) identification of the roles and responsibilities of stakeholders;

j) identification of the roles and responsibilities of evaluators;

k) identification of evaluator independence requirements, if applicable;

l) identification of approval authority for the AE report;

m) definition of value assessment objectives, factors, metrics and criteria to be used;

n) identification of analysis methods to be employed, if applicable; and

o) definition of architectural analysis objectives, factors and criteria to be used.

NOTE The activities in the Architecture Evaluation process specified in ISO/IEC/IEEE 42020 can be used as a guide when planning an AE effort. The planning activity specified in that AE process provides recommended tasks for planning an AE effort.

#### 8.3 Architecture evaluation report

##### 8.3.1 AE report requirements

The AE report provides results of reviews and evaluations, such as a risk assessment, quality assurance evaluation or an evaluation of project portfolios, design constraints, candidate architectures, suppliers, customer satisfaction, effectiveness of security controls, analysis of change records or change requests, personnel needs, measurement needs or financial variances. It can include evaluation criteria. Evaluations can be based on criteria of traceability, consistency, testability, risk reduction, usability and customer satisfaction and feasibility.

The AE report provides information and recommendations to assist future decision-making, and it can indicate trends and recommendations for future comparable situations. For software configuration management evaluations, the report provides information about functional completeness of the software items against their requirements and the physical completeness of the software items (whether their design and code reflect an up-to-date technical description).

Using the relevant AE plan contents where possible, each AE report shall include:

a) purpose and scope of the AE effort;

b) identified issues, risks and opportunities;

c) identified impacts on stakeholders;

d) definition of AE objectives addressed;

e) identification of stakeholder concerns addressed; f) identification of relevant stakeholders;

g) identification of architecture(s) that were evaluated;

h) identification of architecture description(s) that were used;

i) identification of resources used;

j) definition of tailoring performed on the AE process for this AE effort;

k) identification of AE frameworks employed, if any, with the rationale for their selection;

l) identification of data used, collected or produced that needs to be archived or baselined;

m) identification of information sources used in the AE effort; and

n) identification of other resources used in the AE effort, including participating people and organizations;

NOTE The resources actually used during the architecture evaluation can differ from the planned

resources.

o) presentation of AE results;

p) definition of evaluation synthesis objectives;

q) summary of overall results;

r) recommended architecture(s), if multiple architecture were examined;

s) relevant observations and findings;

t) architecture trade-offs identified and examined;

u) results from each of the AE approaches employed, mapped to the AE objectives they addressed; and

v) traceability of the conclusions to the objectives of the evaluation.

##### 8.3.2 AE report recommendations

Each AE report should include:

a) proposed way forward, when applicable (e.g. recommended modifications to the architecture, additional evaluation or analysis needed, etc.);

b) derivation of final conclusions from the value assessment and architectural analysis results;

NOTE In some domains such as safety critical systems it is often necessary to document the derivation of the conclusions all the way down to the analysis results.

c) description of how each AE approach was implemented, along with sources of information used;

d) sensitivity analysis on the results to help understand the impact of incomplete or inaccurate input data, etc.;

e) description of limitations of the AE effort;

f) description of the extent to which the AE results are useful or valid;

g) recommendations on mitigating the identified issues and risks;

h) traceability of concerns to specific stakeholders and to associated compliance documents;

i) assumptions made in execution of the AE effort;

j) any significant deviations from the AE plan along with the reasons for those deviations;

k) identification of impacts due to planning assumptions found to be false;

l) archiving and repository requirements for the AE report; and

m) lessons learned during the AE effort.

The AE report should provide the capability for the customer, requestor or sponsor, if applicable, to affix their approval.

The AE report should provide the capability for the approving authority, if applicable, to affix their approval.

If the evaluation identifies consequences of potential emergent properties of an architecture entity that are undesirable, then explicit actions to deal with them should be recommended. When these consequences are relatively obvious, evaluators should declare in the AE report any risks and potential unintended consequences, or incomplete consideration of potential emergent properties of an architecture entity, in order to provide the architects with an opportunity to mitigate those risks.

In the course of the evaluation, if one or more assumptions made during planning or execution of the architecture evaluation have proven to be false, then evaluators delivering the AE results should use their knowledge and skills and make reasonable efforts to declare in the AE report any risks and potential unintended consequences of the false assumptions in order to provide the architects with an opportunity to mitigate those risks.

The AE report should document the provenance of all information items used in an AE. This facilitates answering of questions about the results, findings and recommendations of the evaluation.

The AE report should include the recommended items from ISO/IEC/IEEE 15289:

- date of issue and status,

- issuing organization,

- contributors,

- summary,

- context (assumptions),

- body (including methods of obtaining results),

- conclusions and recommendations,

- references,

- bibliography,

- glossary, and

- change history.

##### 8.3.3 AE report permissions

Each AE report may include:

a) presentation of value assessment results;

b) definition of value assessment objectives;

c) relevant observations and findings;

d) results from each of the assessment methods employed, mapped to the value assessment objectives they addressed;

e) description of how each value assessment was implemented, along with sources of information used;

f) presentation of architectural analysis results;

g) definition of architectural analysis objectives;

h) relevant observations and findings;

i) results from each of the analysis methods employed, mapped to the architectural analysis objectives they addressed; and

j) description of how each architectural analysis was implemented, along with sources of information used.

k) implementation roadmap for the architecture;

l) action plan for implementing the recommendations;

m) ground rules established in executing the AE effort;

n) responses from stakeholders, including architects, from their review of AE results;

o) comments received on preliminary drafts of observations and findings;

p) recommendations with rationale based on findings of the AE effort; and

q) additional findings and recommendations beyond the purpose and scope of the evaluation.

Recommendations may be accompanied by implications, advantages and disadvantages, caveats or regrets associated with the recommendation.

Multiple reports may be generated for different target audiences.

NOTE AE reports could be generated for different target audiences due to access limitations or other factors. Also, multiple reports could be needed to allow for interim reports during the life of the effort.

It may be helpful to document in the report the level of rigor with which the AE effort was conducted, along with any known deficiencies such as incomplete or inaccurate data as inputs, key stakeholder inputs not received and use of models beyond their normal range of operation.

## Annex A (informative) — Value and quality concepts

### A.1 General

This annex complements Clauses 4 and 5 with additional information about value and quality concepts as used in this document.

Value and quality are two distinct attributes of an entity that ultimately determines its inferiority or superiority. It is often the case that quality of the entity is in the hands of the producer, while it is actually the consumer who determines the value of the entity, for which the consumer would willingly and knowingly pay. The value is a function of the quality that resides in the product or service, so this means that ultimately it is the consumer who determines what quality is acceptable. In other words, quality corresponds to the means, while value is subjective and is relative to the ends.

Carl Menger[52] wrote in 1871: "Value is nothing inherent in goods, no property of them, nor an independent thing existing by itself. It is a judgment economizing men make about the importance of goods at their disposal for the maintenance of their lives and well-being. Hence value does not exist outside the consciousness of men."

Drucker[29] had this to say about quality: "Quality in a product or service is not what the supplier puts in. It is what the customer gets out and is willing to pay for. A product is not quality because it is hard to make and costs a lot of money, as manufacturers typically believe. That is incompetence. Customers pay only for what is of use to them and gives them value. Nothing else constitutes quality".

### A.2 Evaluation factors

Value and quality are related to the factors used in the AE effort. These factors are used in each evaluation tier as illustrated in Figure A.1.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.1 — Factors decomposition example (Simple case)**

Often the factors decomposition can be performed in a strict hierarchical fashion as shown, but in more complex cases lower tier factors can impact more than one factor in a higher tier as illustrated in Figure A.2.

In similar fashion, the evaluation objectives in each tier can also be structured in a way where objectives in one tier will “satisfy” objectives in an upper tier. However, it is not always possible to have a simple and direct correlation between objectives in separate tiers.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.2 — Factors decomposition example (Complex case)**

Factors will be identified in each tier that best support the evaluation approach or methods used. But lower tier factors are not always needed, as illustrated in Figure A.3. In some cases, factors within a tier will need to be decomposed into lower level sub-factors to facilitate their use.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.3 — Selective factors decomposition**

The AE factors defined in this document are similar to quality attributes in ATAM (see Annex D) and quality characteristics in the ISO/IEC 25000 family of standards on Systems and software Quality Requirements and Evaluation (SQuaRE). A summary of key concepts in SQuaRE are provided in A.4.5.

### A.3 Value

#### A.3.1 General

This clause provides information on value, value-focused thinking, value models and value measures that could be useful in applying this document. The following items are covered:

- what is “Value”;

- Keeney’s value-focused thinking;

- value assessment of system architectures;

- Ring’s value model;

- stakeholder values, qualities and measures.

The inclusion of these items does not imply endorsement of these particular ways of addressing value. Exclusion of other items is not intended to imply their shortfalls. The intention is to include those items that can be related to the conceptual elements in this document.

#### A.3.2 What is “Value”?

The importance of the concept of “Value” during architecting has been underscored in numerous articles, journal papers, case studies, books, and in practice. However, there is relatively little information about what value is, what its characteristics are or how stakeholders can best determine it. There are a wide variety of opinions on the nature of “Value”; some of these are summarized below:

- Value as a higher order concept is misunderstood and sometimes mistaken with other concepts (e.g. cost, monetary return, importance, profit, advantage, return on investment).

- Value and quality are often treated as synonyms, whereas quality is more properly treated as the means while value is the ends.

- Value is perceptual and subjective.

- Value is determined based on a situation and is temporal in nature.

- Stakeholders (and architects) make trade-offs when assessing value.

- Value is created by consumption or utilization or possession.

- Value of a product is what buyers are willing to pay[53].

- Value is the consumer’s overall assessment of the utility of a product based on perceptions of what is received and what is given[55]; and

- Value reflects the customers desire to retain or obtain a system and depends on how much the system agrees with the value system of the customer[34].

#### A.3.3 Value-focused thinking

Keeney[16] considers value as the fundamental construct in decision making and presents procedures and theoretical foundations for value-focused thinking. He considers value-focused thinking to be applicable in situations where a complex decision is necessary with no clear solution possible and the decision that is being made is critical to the stakeholders affected by the decision. The central role of thinking about values is expressed in Figure A.4.

Per Keeney, value-focused thinking essentially is comprised of two activities: a) deciding what the stakeholder wants or expects, and b) figuring out how to get it for them. According to Keeney, what the stakeholder wants or expects could be certain benefits that are intangible (like emotions, feelings, superiority etc.), or it can be tangible (like goods, services, money, capabilities, etc.). Value-focused

thinking recognizes that design of any system or offering must uphold the expected value for its stakeholders without which stakeholders may not participate as anticipated or the system/offering may not be viable.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.4 — Thinking about values[21]**

#### A.3.4 Value assessment of system architectures

Selva & Crawley[54] espouse the line of thought that the key characteristics of system architecting is to maximize stakeholder value, rather than profit or performance. They propose quantification of stakeholders’ value using value functions that capture the needs and requirements of stakeholders. According to them, some common approaches to assess the value of an engineered system are:

- using end-to-end simulation models to simulate every function and its interaction with the surrounding context to calculate the value of the system-of-interest;

- observing system simulation experiments to quantify the value of a certain dataset (eg. numerical weather prediction);

- rating the importance of different customer attributes and their coupling to design features by means of House of Quality tools (sometimes known as Quality Function Deployment);

- computing the net present value of an architecture to determine its cardinal ranking amongst a collection;

- adopting the value of information approach to identify the probabilities of different scenarios and the availability of useful information in these scenarios to make a data-based decision;

- comparing the capabilities of the system architecture with the stakeholder requirements and use rule-based expert systems to assess the value of the system architecture.

#### A.3.5 Ring’s value model

Ring[56] defines a ”value cycle” with three levels, as shown in Figure A.5, that is useful in delivering value to stakeholders and to continuously manage and upgrade long-life systems. These levels are organized to focus on the system to be created, the system’s purpose and the value of the system to its stakeholders.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.5 — Ring’s system value cycle[56]**

The model promotes the thought process of discerning stakeholder’s value before the system is created rather than after the system becomes operational. The model takes into account the criteria that value is not stationary and changes over time and promotes a pursuit-type system rather than a requirements-based system so as to purposefully adapt the context to the solution system.

#### A.3.6 Stakeholder values, qualities and measures

Gilb[49] considers stakeholder values as those things that describe the improvements a stakeholder needs or wants from a specific solution and qualities (A.4.2) and as those things that describe the quality attributes of the specific solution. Gilb considers function as the purpose of the solution and qualities as the distinguishing elements between two solutions in the same solution space. It is normally intended that qualities will deliver improvement on the stakeholder values.

Accordingly, different solutions exhibit different qualities depending on the corresponding stakeholder values. Gilb espouses the view that quality and value measures are quantifiable (like in the case of more user-friendly, less reliability, enhanced performance and so on) and this quantification helps address stakeholder needs appropriately.

#### A.3.7 Value articulation framework

Doji[48] considers value to reside in the perception of the stakeholder and proposes the value articulation framework as the method for tracing value from conception to realization in an assured manner. He considers 4 dimensions as essential ingredients in establishing this trace. Regarding the context of technology management, these dimensions are: Stakeholder and their perception of value, Quality characteristics of the Technology that is developed (which are the carriers of value and hence are of potential value), Technology management discipline (which aids in translating the potential value into actual value), and lastly the value that accrues to the given Stakeholder. Once the elements pertaining to the different dimensions are identified, he utilizes the generic X-matrix representation, as shown in Figure A.6, to establish the corresponding linkages and trace value creation, across the various dimensions.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.6 — Doji’s value articulation framework[48]**

### A.4 Quality

#### A.4.1 General

This clause provides information on quality attributes, quality models and quality measures that could be useful in applying this document. The following items are covered in this clause:

- what is “Quality”;

- architecture quality attributes;

- Boehm and Nupul’s quality models and ontology;

- standards on System and Software Quality Requirements and Evaluation (SQuaRE) – the ISO/IEC 25000 family.

The inclusion of these items does not imply endorsement of these particular ways of addressing quality. Exclusion of other items is not intended to imply their shortfalls. The intention is to include those items that can be related to the conceptual elements in this document.

#### A.4.2 What is “Quality”?

The importance of the concept of “Quality” during architecting has been underscored in numerous articles, journal papers, case studies, books, and in practice. “Quality” is a subjective term for which each person or sector has its own definition. There are a wide variety of opinions on the nature of “Quality”; some of these are summarized below:

- Quality has a pragmatic interpretation as the non-inferiority or superiority of something.

- Quality is the characteristics of a product or service that bear on its ability to satisfy stated or

implied needs[26].

- Quality is a product or service free of deficiencies[26].

- Quality means “fitness for purpose”[30].

- Quality means “conformance to requirements”[28].

- Quality means “uniformity around a target”[32].

- Quality means “the loss a product imposes on society after it is shipped”[32].

- Quality in a product or service is not what the supplier puts in. It is what the customer gets out and is willing to pay for[29].

- Degree to which a set of inherent characteristics fulfills requirements[2].

- Quality is “excellence of the system in a chosen dimension and is the basis for satisfying its stated purpose”[34].

- Quality characteristics of a system are a set of essential and distinguishing attributes that have a pragmatic interpretation of the system’s inferiority or superiority[51].

In business, engineering and manufacturing, quality has a pragmatic interpretation as the non-inferiority or superiority of something; it is also defined as fitness for purpose. Quality is a perceptual, conditional and somewhat subjective attribute and may be understood differently by different people. Consumers may focus on the specification quality of a product/service or how it compares to competitors in the marketplace. Producers might measure the conformance quality or the degree to which the product/service was produced correctly[30].

Support personnel may measure quality in the degree that a product is reliable, maintainable or sustainable. A quality item (an item that has quality) can perform satisfactorily in service and is suitable for its intended purpose[31].

#### A.4.3 Architecture quality attributes

Architecture quality attributes are the extent to which the architecture can deliver value to its stakeholders. It is a set of essential and distinguishing attributes that have a pragmatic interpretation of the architecture’s inferiority or superiority. It is a function of:

- architecture process outcomes,

- impact of the architecture on various stakeholders,

- measure of extent of achievement of stakeholder concerns, and

- measure of capabilities of the architecture.

While ATAM does deal with quality attributes, these are attributes of the architecture entity, not the architecture itself. See more on ATAM in Annex D.

Architecture quality attributes are the overall factors that affect behavior, structure, design and experience of architectures. They represent areas of concern that potentially impact the structure and

behavior exhibited by the realized system. The extent to which the architecture handles a combination of quality attributes indicates the success of the architecting effort and overall quality of the realized system. The taxonomy for each architecture quality attribute would be:

a) Measures: The parameters by which the attributes are measured.

b) Factors: Policies and mechanisms of the system and its environment that impact the stakeholder

concerns.

c) Methods: Techniques for addressing concerns and processes for realizing the quality attributes

during productions.

While conceptualizing architecture to address the architecture quality attributes, it is necessary to consider potential impact of each of the quality attributes on other stakeholder concerns. While tradeoff analysis techniques aid architects in prioritizing architecture quality attributes, architectural tactics describe how a specific quality attribute can be achieved. The importance of each architecture quality attribute depends on the context and the stakeholder’s concerns for which the specific architecture is conceptualized. Table A.1 provides an example list of architecture quality attributes.

**Table A.1 — Architecture quality attributes**

| Quality attribute | Description |
|---|---|
| Coherence[35] | Being logical and consistent |
| Completeness[35] | Ability to form a whole |
| Elegance[39] | Form and function are graceful and stylish |
| Hierarchy[40] | Levels of abstractions |
| Modularity[37] | Separation of concerns |
| Variability[36] | Expandable in preplanned ways |
| Subsetability[36] | Support the production of a subset |
| Conceptual integrity[35] | Architecture unification |
| Commonality[36] | Sharing in preplanned ways |
| Durability[38] | Stand up robustly and remain in good condition |
| Utility[38] | Useful and function well for people |
| Beauty[38] | Delight people and raise their spirits |
| Robust[39] | Strong and not be vulnerable to changes |
| Feasible[39] | Should be able to implement |
| Flexible[39] | Adapt to changing conditions |
| Verifiable[39] | Perform as designed |
| Traceable[39] | Architectural elements can be traced in any direction |
| Cohesion[37] | Forming a unified whole |

#### A.4.4 Boehm and Nupul’s quality model and ontology

Boehm and Nupul[41] attempts to qualitatively define quality by a set of attributes and metrics. They utilize a hierarchical quality model structured around high-level quality characteristics, intermediate level quality characteristics and primitive quality characteristics for this purpose. Each of these characteristics contributes to the overall quality level. They consider high level quality characteristics to represent the basic high-level requirements, intermediate level quality characteristics to represent the quality factors (portability, reliability, efficiency, usability, testability, understandability and flexibility), and primitive level quality characteristics to represent the quality metrics (device independence, accuracy, completeness, robustness, consistency, accountability and so on) that measure a given primary characteristic.

Boehm and Nupul[27] present an ontology for reasoning about a system’s qualities. They espouse the view that functional requirements specifies what the system should do and hence it is additive in

nature, while non-functional requirements (system qualities) specifies how well the system performs its functions and hence it is multiplicative and system-wide in nature. He utilizes a variation of the IDEF5[57] ontology structure comprising the elements Class, Individual, Referent, Relation, State and Process to express the ontology of system qualities. These class hierarchies are organized in terms of stakeholder value propositions, and child-class system qualities as means for achieving the parent class system quality end objectives. They also espouse the view that class hierarchies do not necessarily maintain one-to-many relationships and there are many cases where many-to-many relationships exist, especially when one or more system qualities impacts one or more top level system qualities. Table A.2 presents a typical upper level of system quality hierarchy.

**Table A.2 — Upper level of system quality hierarchy[27]**

| Stakeholder value-based system quality ends | Contributing system quality means |
|---|---|
| Mission effectiveness | Stakeholders-satisfactory balance of Physical Capability, Cyber Capability, Human Usability, Speed, Endurability, Maneuverability, Accuracy, Impact, Scalability, Versatility, Interoperability |
| Resource utilization | Cost, Duration, Key Personnel, Other Scarce Resources; Manufacturability, Sustainability |
| Dependability | Security, Safety, Reliability, Maintainability, Availability, Survivability, Robustness |
| Flexibility | Modifiability, Tailorability, Adaptability |

#### A.4.5 The ISO/IEC 25000 family of standards on quality

##### A.4.5.1 General

The ISO/IEC 25000 family of standards, also known as SQuaRE (System and Software Quality Requirements and Evaluation), has the goal of creating a framework for the evaluation of software product quality. Some of these are discussed in this annex:

- ISO/IEC 25000, SQuaRE — Quality model framework;

- ISO/IEC 25010, SQuaRE — System and Software Quality models;

- ISO/IEC 25012, SQuaRE — Data Quality model;

- ISO/IEC 25020, SQuaRE — Measurement reference model and guide; and

- ISO/IEC 25021, SQuaRE — Quality measure elements.

##### A.4.5.2 ISO/IEC 25000 Quality model framework

This framework categorizes product quality into characteristics, which in some cases are further subdivided into sub-characteristics. A sub-characteristic in some cases can be divided into sub-sub-characteristics. This results in a quality breakdown structure as illustrated in Figure A.7.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.7 — ISO/IEC 25000 Quality model framework**

A.4.5.3) ISO/IEC 25010 System and software quality models

A.4.5.3.1) Quality in use model

This quality in use model defines five characteristics related to outcomes of interaction with a system. It characterizes the impact that the product has on stakeholders. This model is presented in Figure A.8.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.8 — ISO/IEC 25010 Quality in use model**

A.4.5.3.2) System/software product quality model

This product quality model categorizes system/software product quality properties into eight characteristics that focuses on the target system. This model is presented in Figure A.9.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.9 — ISO/IEC 25010 System/software product quality model**

A.4.5.4) ISO/IEC 25012 Data quality model

This data quality model, as illustrated in Table A.3, categorizes data quality attributes into fifteen characteristics that are considered from two points of view: inherent and system dependent. While the inherent data quality refers to the degree to which the quality characteristics of data have the potential to satisfy needs when data is used in specified conditions, system dependent data quality refers to the degree to which data quality is reached and preserved within a system when data is used under specific conditions.

**Table A.3 — ISO/IEC 25012 Data quality model**

| Characteristics | Inherent | System dependent | Characteristics | Inherent | System dependent |
|---|---|---|---|---|---|
| Accuracy | X |  | Efficiency | X | X |
| Completeness | X |  | Precision | X | X |
| Consistency | X |  | Traceability | X | X |
| Credibility | X |  | Understandability | X | X |
| Currentness | X |  | Availability |  | X |
| Accessibility | X | X | Portability |  | X |
| Compliance | X | X | Recoverability |  | X |
| Confidentiality | X | X |  |  |  |

A.4.5.5) ISO/IEC 25020 System and software product quality measurement reference model

This product quality measurement reference model describes the relationship between a quality model, its associated quality characteristics (and sub-characteristics), and system and software product attributes with the corresponding software quality measures, measurement functions, quality measure elements and measurement methods. This model is presented in Figure A.10.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure A.10 — ISO/IEC 25020 System/software product quality measurement reference model**

An illustration of this model as given in ISO/IEC 25021 is presented in Table A.4.

**Table A.4 — ISO/IEC 25021 Product quality measurement reference model**

| SNo | Element | Particulars |
|---|---|---|
| 1 | Quality measure element name | Number of records |
| 2 | Objective | To determine data quality of target data |
| 3 | Property to quantify | Record is a set of related data items treated as a unit |
| 4 | Relevant quality measures | Measure of accuracy |
| 5 | Measurement method | Review and analyze data records |
| 6 | List of sub-properties | Data item: lowest component of a group of data File: a set of related records |
| 7 | Input for the quality measure element | Physical files of a database |
| 8 | Numerical rules | Adding total records |
| 9 | Context of the quality measure element | Measure the accuracy and completeness to a group of data |
| 10 | Measurement constraints | Verify the impact of technology on the number of records generated for the same information |

## Annex B (informative) — Relationship to other standards

### B.1 ISO/IEC standards in the domain of systems and software engineering

The following is a list of standards in ISO/IEC JTC1, SC7 that are most relevant and directly influence the conceptual model and requirements for architecture evaluation:

- ISO/IEC/IEEE 42020: This standard complements the architecture-related processes identified in ISO/IEC/IEEE 15288, ISO/IEC/IEEE 12207, and ISO 15704 with activities and tasks that enable architects and others to more effectively and efficiently implement architecture practices. Implementing these practices will help ensure that the architecture has greater influence on business and mission success. It specifies a coherent set of processes for governance, management, conceptualization, evaluation and elaboration of architectures, and activities that enable these processes. Users of this standard can apply these processes in the context of:

B.1.1) understanding, development and evolution of entities through their life cycle stages such as conception, development, implementation, operation, sustainment, decommissioning, and disposal;

B.1.2) organization(s) acting as users, customers and providers of the solution specified by the architecture description; and

B.1.3) architecting of entities.

- ISO/IEC/IEEE 42010: This standard addresses the creation, analysis and sustainment of architectures of systems using architecture descriptions. A conceptual model of architecture description is established in this standard. The required contents of an architecture description are specified. Architecture viewpoints, architecture frameworks and architecture description languages are introduced for codifying conventions and common practices of architecture description. The required content of architecture viewpoints, architecture frameworks and architecture description languages is specified.

- ISO/IEC/IEEE 15288: This standard establishes a common framework for system life cycle processes, with well-defined terminology. It applies to the acquisition of systems, which can be comprised of products, services or both, as well as to the supply, development, operation, maintenance and disposal of systems, whether performed internally or externally to an organization. ISO/IEC/IEEE 15288 is intended to be used either stand alone, or jointly with other documents such as ISO/IEC/IEEE 12207, and supplies a process reference model that supports process capability assessment in accordance with ISO/IEC 15504-2.

### B.2 ISO standards in the domain of enterprise activities

- ISO 15704: This standard defines the requirements for enterprise-reference architectures and methodologies, as well as the requirements that such architectures and methodologies shall satisfy to be considered a complete enterprise reference architecture and methodologies. The scope of these enterprise-reference architectures and methodologies covers those constituents deemed necessary to carry out all types of enterprise creation projects as well as any incremental change projects required by the enterprise throughout the whole life of the enterprise, including:

- enterprise creation;

- major enterprise restructuring efforts; and

— incremental changes affecting only parts of the enterprise-life cycle.

### B.3 Relationship between architecture standards

Figure B.1 describes the main relationships between this document and other ISO standards related to architecture and related activities. This document does the following:

- formalizes the evaluation act of:

- architecture entities as defined by ISO/IEC/IEEE 42020;

- enterprise architectures as defined by ISO 15704;

- system architectures as defined by ISO/IEC/IEEE 15288;

- software architecture as defined by ISO/IEC/IEEE 12207;

- Considers evaluation of architecture possibly based evidence (formalized viewpoints, views and models) from architecture description as defined by ISO/IEC/IEEE 42010; and

- Addresses concerns of the stakeholders acting in the context of enterprises and projects as defined by ISO 15704.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure B.1 — Main relationships between ISO/IEC/IEEE 42030 and other ISO standards**

## Annex C (informative) — Architecture evaluation examples

### C.1 General

This annex provides examples using the architecture evaluation concepts outlined in this document for the following cases:

- business and information technology (IT) architecture;

- software architecture;

- service architecture; and

- enterprise architecture

The examples start off by identifying the relevant stakeholder concerns and using these to define the objectives for the evaluation. These objectives indicate the qualities that are expected from the architecture or its architecture entity. The qualities are tangibly expressed with the help of one or more factors. By implementing assessment and analysis methods with respect to these factors the evaluation results can be determined.

These factors are sometimes decomposed into subordinate factors to facilitate the examination. It is sometimes necessary to build a model to show how the factors contribute to the evaluation results. An example of this approach is described below:

- Concern: FUNCTIONALITY. For this example, use specific case of “License Sharing.” This can be elaborated as follows:

System provides function X, defined in the use-case view. It would be evaluated by doing a walkthrough (potentially of several views) of that associated use-case. The use-case can be further elaborated by "time to execute", which would likewise be evaluated using walkthroughs perhaps coupled to an executable model.

- Concern: SECURITY. For this example, use specific case of “Unauthorized Access”. This can be elaborated as follows:

System is secure to use in a hostile environment, further defined by resisting various anti-use-cases (provided in a threat anti-use-case view). These can be further measured by Information Assurance Technical Framework ratings for strength of mechanism and/or assurance level. These would then be evaluated by walkthroughs and examination of the properties of both selected system and components and specified process elements (possibly another view) by which they are composed. A threat anti-use-case can be used to describe the abuse cases or what an attack might do to break the system security.

### C.2 Business and IT architecture evaluation

#### C.2.1 Situation

A mail-order business (e.g. online clothing store) is trying to work out how to comply with new privacy regulations. One option is to update their current IT systems and business processes to fix gaps and achieve compliance. The alternative is to migrate to a SaaS software solution and associated business processes that comply with the regulations. They would like to evaluate their business and IT

architectures to determine which option is better. The stakeholder concerns in Table C.1 are deemed to be relevant.

**Table C.1 — Business/IT architecture — Stakeholder concerns**

| Stakeholder | Concerns |
|---|---|
| Business ownership | Lifecycle costs, potential business value |
| Business operations | Cycle-time to compliance, disruptions due to change in business processes and IT infrastructure |
| IT operations | Reliability, availability and ease of operations |

#### C.2.2 Business/IT architecture — Evaluation synthesis

**Table C.2 — Business/IT architecture — Evaluation synthesis**

| Objectives | Factors & subfactors | Evaluation synthesis approach | Results |
|---|---|---|---|
| Establish trade-offs among alternatives | Comparison of total life cycle cost of each option Including maintenance and business operations costs Comparison of business value impacts Transition comparison: cycle time, cost, disruptions, people impacts | Combine all one-time costs, and all annual costs: IT, business operations Estimate business impacts in a median scenario, making necessary assumptions and projections | Migration option has higher upfront cost ($6 M vs. $1,5 M), but lower annual cost ($2,2 M vs $2,7 M). Business capability impacts mostly balance out, no deal-breakers Likely positive long-term impact as SaaS solution evolves Substantial disruption impacts, both on brand image and people impacts: Medium ↓ |
| Determine stakeholder priorities, current business situation | Understand what is important to stakeholders Understand current pressures on the business and its impact on the decision | Stakeholder interviews Business environment study, study of management reports | Priority is no adverse impacts on capability, minimize cost Emphasis on short-term Considerable competitive pressure, struggle for survival |
| Develop overall recommendation | — Propose strategy, rationale | User symposium Weigh findings against business priorities Expand space of options if possible | Go with updating option, defer SaaS adoption due to survival pressures Plan on future migration to SaaS, rework business processes where possible to ease future transition (avoid disruption impacts when transition required) |

#### C.2.3 Business/IT architecture — Value assessment

**Table C.3 — Business/IT architecture — Value assessment**

| Value aspect being assessed | Objectives | Factors & subfactors | Value assessment method | Results |
|---|---|---|---|---|
| Total cost of ownership for updating solution | — Determine one-time costs and annual costs of updating option | Cost of IT systems update Cost of IT systems operation and maintenance Cost of business process changes | Project planning for updating project Obtain historical data for maintenance and operations costs, estimate changes | One-time cost of $1,5 M for updating Annual cost of $2,7 M |
|  | — Determine one-time costs and annual costs of updating option | — Business operations cost |  |  |
| Total cost of ownership for SaaS approach | Determine annual costs with SaaS approach Determine cost of migration, including training and business structural changes | SaaS solution procurement costs SaaS solution infrastructure costs SaaS business process operation costs Cost of migration | Project planning for migration project, including SaaS infrastructure Interactions with SaaS vendor Estimated impacts on operations costs | One-time cost of $6 M for migration Annual cost of $2,2 M |
| Business impact of missing and added SaaS capabilities | Determine impact of missing capabilities Determine value of added capabilities and modified business processes | Business impact of missing functionality No deal-breakers Business value of added capabilities and process improvements | Business impact analysis Market and order history analysis, to determine impact of new and missing features on market share and customer satisfaction | Some process efficiency impacts due to missing management reports: Low ↓ Small expected increase in market opportunity from analytics capabilities and process flexibilities: Low ↑ |
| Business impact of dependability and other quality characteristics | — Determine business impacts of quality characteristics once steady state reached | Estimated changes in dependability Expected changes in operability | — Financial assessment of risk impacts, effect of process changes on effort, rework | — Loss of reliability and increased cycle time to fix problems may result in slightly decreased satisfaction and revenue: Low ↓ |

Table C.3 (continued)

| Value aspect being assessed | Objectives | Factors & subfactors | Value assessment method | Results |
|---|---|---|---|---|
| Business impact of transition | — What will be the business impacts during the transition period? | Impact of cycle time Cost of disruptions People impacts | Analyze effects on order fulfilment and satisfaction Impact on brand image | Longer cycle time for SaaS migration and more quality problems will lead to ~10 % higher loss of revenue, and around 2 % reduction in market share due to brand image: Medium ↓ IT operations team will need to be downsized with the SaaS option: Medium ↓ |

#### C.2.4 Business/IT architecture — Architectural analysis

**Table C.4 — Business/IT architecture — Architectural analysis**

| Object being analyzed | Objectives | Factors & subfactors | Architectural analysis method | Results |
|---|---|---|---|---|
| IT architecture | — Customer information collection and storage policies | Customer personal information being collected and stored Storage locations | DB schema analysis tools Interview IT operations team Business process analysis | — List of customer information being collected and stored, with locations |
| IT architecture and business process architecture | — Customer information access control policies | IT access controls Business process access controls Business process need-to-know | Business process analysis IT system reviews Interviews with operations team Observation of business process execution | Business process gaps in need-to-know List of controls on access to customer information |
| IT and business process architecture | — Gaps in privacy compliance | Non-compliances to storage location restrictions Non-compliance to access control restrictions | — Analysis of controls required by privacy regulation | List of gaps in IT systems to be fixed List of gaps in business process to be fixed |

Table C.4 (continued)

| Object being analyzed | Objectives | Factors & subfactors | Architectural analysis method | Results |
|---|---|---|---|---|
| SaaS solution | — Identify missing and added functionality | Missing features compared to existing system Added features | Compare information in SaaS product literature with current system features Interact with SaaS vendor | Some management reports missing Some analytics features added |
| SaaS business process | — Identify changes required in business processes | Business process changes Required structural changes to accommodate process changes Effect on operability and outcomes | Business process analysis Operations impact analysis Risk analysis | Redefinition of roles for warehouse and financial personnel so the roles align to processes. Rework of processes so both groups align to each other. Errors and delays likely during transition More flexibility in business process |
| SaaS approach (solution + business process) | — Determine SaaS impact on reliability, availability and ease of operations | Experiences of current users of SaaS approach Reliability and availability of SaaS solution | Interview existing SaaS approach user base Failure modes and effects analysis | Some glitches experienced by SaaS users Loss of control leads to reliability issues: delays in fixing problems |

### C.3 Software architecture evaluation

#### C.3.1 Situation

A leading IT services provider utilizes a proprietary, hand-crafted resume management system for handling and processing resumes of potential candidates. While the recruitment processes of this organization are encoded in their work-flow systems, the resume management system lies outside. The organization’s top management has decided to increase the number of associates by a factor of 10X over the next 5 years. In this situation, the infrastructure team is trying to work out how best to facilitate resume handling and processing so as to handle the increasing demands. It has been decided by the top management that the existing outdated resume management system should be replaced with a best- in-class solution as the architecture of the existing system does not exist. There are two suppliers for the new resume management system. One solution is a cloud based software service and the other is a packaged commercial software product. They would like to evaluate both these options to determine which option is better.

The stakeholder concerns in Table C.5 are deemed to be relevant.

**Table C.5 — Software architecture — Stakeholder concerns**

| Stakeholder | Concerns |
|---|---|
| Human resources | Latency in achieving the recruitment goals due to change in infrastructure; loss of historical data |
| Chief information officer | Technologies involved in the new systems; support and upgrade options; hardware and other infrastructure options; security and privacy options |
| IT operations | Backup and recovery options; reliability, configurability, performance and maintainability options |

#### C.3.2 Software architecture — Evaluation synthesis

**Table C.6 — Software architecture — Evaluation synthesis**

| Objectives | Factors & subfactors | Evaluation synthesis approach | Results |
|---|---|---|---|
| Establish data migration costs | Comparison of data schema Including supporting file formats Comparison of migration capabilities Including ability to utilize existing classification Comparison of migration time Manual migration, batch migration | Migration analysis Regression analysis | Migration costs for the commercial product is $2 million. This is an additional feature in the system that needs to be procured. Migration costs for the cloud based service is $500 per 1 000 transactions. Migration effort is one time as data in old system is imported into the new instance for the commercial product. Migration effort is expended on demand basis for the cloud based service. |
| Establish ownership of data and related costs | Comparison of data ownership Conditions for ownership transfer Access & security options Comparison of data criticality Data quality, meta-data schema | Customer data analytics KNIME tool | All candidate data, relevant meta-data and relevant categorization are stored in the cloud by the service provider. Storage costs are fixed at $50 per month per GB of data. All candidate data, relevant meta-data are stored in organization’s infrastructure in-house. A RAID 1 TB storage costs $2 000. All data stored in the cloud are owned by the creators. Cloud software service only provides resources for managing the data. All data stored in the organization’s infrastructure are owned and managed by the organization. |

Table C.6 (continued)

| Objectives | Factors & subfactors | Evaluation synthesis approach | Results |
|---|---|---|---|
| Establish operating environment and related costs | Comparison of support effort 9x4 levels of availability L1, L2, L3 support options Comparison of maintenance effort Batch updates & patches Maintenance mode, time to recover | Operations Analysis Business Process Analysis | Enterprise infrastructure to facilitate internet based access of cloud based services. Integration with existing enterprise intranet infrastructure for commercial software product. Dedicated data and support center for managing the commercial software product in-house. |

#### C.3.3 Software architecture — Value assessment

**Table C.7 — Software architecture — Value assessment**

| Value aspect being assessed | Objectives | Factors & subfactors | Value assessment method | Results |
|---|---|---|---|---|
| Benefits in availing cloud services | — Determine one-time benefits and recurrent benefits of cloud option | Increasing infrastructure demands 10X in 5 years On demand availability Recruitment drives Pay as you go model Transaction based pricing | — Multiple criteria decision analysis of eliciting value | High quality flexible services (24 x 7 availability) Increased resource availability and elasticity (scale up of 5X) Very competitive costs (nearest competitor is twice the price) Self-management |
| Benefits in availing commercial product | — Determine one-time benefits and recurring benefits of commercial product | User experience Aesthetic and minimalistic design Connectivity Anytime, anywhere Completeness No external licenses | — Utility and behavior assessment | Industry standard in resume management Stable roadmap and planned upgrades Scalable across multiple geographies Multi-lingual |

Table C.7 (continued)

| Value aspect being assessed | Objectives | Factors & subfactors | Value assessment method | Results |
|---|---|---|---|---|
| Readiness levels of commercial product | Determine technology landscape Determine software and supplier health indices Determine competitor landscape | Software stability Minimal fixes Speed & performance Supplier stability Business continuity plans | Technology and business readiness level assessment Customer life-line survey | Software readiness level is 7 Software experience index is 5,7 Supplier readiness level is 6 Supplier customer satisfaction index is 92 % |
| Readiness levels of cloud service | Determine service landscape Determine technology landscape Determine s/w and service provider health indices | Service stability Service quality levels Software stability Minimal fixes Service provider stability Service continuity plans | Service scorecard assessment Service experience assessment Technology readiness level assessment | Service scorecard Slippage: 1/1 000 Down-time: 12 hours for 365 days Interaction score: 5,32 Service experience index: 4,7 Software service readiness level: 6 |

#### C.3.4 Software architecture — Architectural analysis

**Table C.8 — Software architecture — Architectural analysis**

| Object of interest | Objectives | Factors & subfactors | Architectural analysis method | Results |
|---|---|---|---|---|
| Quality attributes of cloud based software services | — Determine software and service quality levels | Under normal operating conditions Target: 1 000 transactions/ hour Under duress operating conditions Target: 100 transactions/ hour | Service quality attributes analysis Software quality attributes analysis Scenario based analysis | 9x2 levels of availability 9x4 levels of security 9x3 levels of privacy 256 bit encryption Sub 1 second response time |

Table C.8 (continued)

Table C.8 (continued)

| Object of interest | Objectives | Factors & subfactors | Architectural analysis method | Results |
|---|---|---|---|---|
| Commercial product architecture | — Interfacing and integration | Back end integration Front end integration Data Synchronization Customization | — Analysis of interfaces, data schema, batch scripts, events, event data, triggers | Supports Linux and windows operating systems Database Clusters for storing and managing large amounts of data Accessible across multiple digital technologies Most functions accessible thru Command console availability APIs available for integration with enterprise applications |

### C.4 Service architecture evaluation

#### C.4.1 Situation

A commercial airline services provider is trying to expand its services to cater to growing demand. Before expansion, the team would like to know whether the service architecture that it currently utilizes can be scaled-up, whether the current service quality levels can be retained, whether the cost of quality can be controlled and whether the difference that it brings to the passengers can be leveraged in some way.

The stakeholder concerns in Table C.9 are deemed to be relevant.

**Table C.9 — Service architecture — Stakeholder concerns**

| Stakeholder | Concerns |
|---|---|
| Passengers | Hassle free travel experience; on-time performance; connectivity to other destina-tions; value for money |
| Airlines’ top-management | Low-maintenance cost; average down-time below industry average; profitability; high level of safety; |
| Investors | High return on investments; superior brand value; |

#### C.4.2 Service architecture — Evaluation synthesis

**Table C.10 — Service architecture — Evaluation synthesis**

| Objectives | Factors & subfactors | Evaluation synthesis approach | Results |
|---|---|---|---|
| Establish service quality levels | Dependability of the service Average delays Missed connections Credibility of the service provider Successful claim resolution Efficiency of the service Baggage claims Oversales and overbooking Response times Dispute resolution timelines Service failure recovery timelines | — Airline quality rating methodology | On-time performance: 8,43 Denied boarding: 8,03/ month Mishandled baggage: 7,32 per 1 000 passengers Consumer complaints: 7,17 per 500 passengers Flight problems: 3 per day Customer service index: 4,32 Dispute resolution time: 60 days per complaint |
| Establish profes-sionalism levels | Professional training of Personnel Average re-training in a year Service attitude & pro-activeness Accuracy of operations Information accuracy Low rates of breakdown and accidents Provision of committed services Customer satisfaction index Customer experience index Service failure recovery Time to recover Maintenance network | — Multi-criteria decision making | Days of re-training: 45 days in a year Failed connections: 15 per 1 000 passengers Customer service Complaints: 30 per 1 000 passengers Service failures: 2 per 300 trips Non-availability of staff: 1 per 2 000 services Maintenance down-time: 1 week per year Cancellations: 50 per 1 000 passengers Refunds: 50 per 500 passengers |

Table C.10 (continued)

| Objectives | Factors & subfactors | Evaluation synthesis approach | Results |
|---|---|---|---|
| Establish operating environment and related costs | Aircraft support 9x4 levels of availability L1, L2, L3 support options Aircraft operations 9x6 levels of safety 9x5 levels of recoverability Staff availability Cancelled Trips | — Evaluate Service SOP & operations SOP cost & effort | Price: $350 million per aircraft Maintenance: $35 million per aircraft per year Run-time: 6 000 hours per year Maintenance-time: 144 hours per 6 months Planned halt-time: 2 hour per trip — Fuel: 2,91 L/100 km |

#### C.4.3 Service architecture — Value assessment

**Table C.11 — Service architecture — Value assessment**

| Value aspect being assessed | Objectives | Factors & subfactors | Value assessment method | Results |
|---|---|---|---|---|
| Inflight service | Determine the inflight experience index Determine the inflight service customer satisfaction index | Inflight entertainment Technology and content Inflight communication Cellular and internet Inflight meals Quality of meals and drinks Seating Quality of seating Seating arrangements | Airline service evaluation survey Analytic hierarchy process methodology | Passenger entertainment equipment conditions: 3,608 Seat and space comfortability: 3,585 Inflight entertainment programs and materials: 2,911 Interior cleanliness: 3,408 Meal variety and sufficiency: 3,123 Meal services: 3,362 Inflight service score: 0,214 |

Table C.11 (continued)

| Value aspect being assessed | Objectives | Factors & subfactors | Value assessment method | Results |
|---|---|---|---|---|
| Customer service | Determine the customer experience index Determine the customer service satisfaction index | Ticketing Price and options Check-in Efficiency and interaction Communication Clear and precise Baggage No damage Timely information Customer care Quality of interaction Timely issue resolution | Customer experience satisfaction survey Stakeholder value assessment Quality of experience metrics and measures | Ticketing experience Index: 4,32 Check-in experience index: 5,32 Communication experience index: 5,32 Baggage experience index: 4,32 Customer care interaction index: 4,87 Issue resolution time: <1/2 hour Interaction quality index: 6,32 Safety index: 5,32 |

#### C.4.4 Service architecture — Architectural analysis

**Table C.12 — Service architecture — Architectural analysis**

| Object being analyzed | Objectives | Factors & subfactors | Architectural analysis method | Results |
|---|---|---|---|---|
| Quality attributes of inflight services | — Determine service quality levels | Under normal operating conditions 8-hour International trip Under duress operating conditions Trip delayed by more than 8 hours | Service quality attributes analysis Scenario based analysis | Normal operations: 3 meals service 3 drinks service Soft-clean after every trip Toiletries refilled Air purged out Duress operations: 2 meals service 3 drinks service Poor cleaning Toiletries not refilled Pungent smell persists |

Table C.12 (continued)

| Object being analyzed | Objectives | Factors & subfactors | Architectural analysis method | Results |
|---|---|---|---|---|
| Quality attributes of baggage services | — Determine service quality levels | Under normal operating conditions 8-hour International trip Under duress operating conditions Trip delayed by more than 8 hours | Service quality attributes analysis Scenario based analysis | Normal operations: 1 in 5 000 bags misplaced 80 % claims honored 1 in 10 000 bags damaged Duress operations: 1 in 1 000 bags misplaced 1 in 2 000 bags damaged 60 % claims honored |

### C.5 Enterprise architecture evaluation

#### C.5.1 Situation

The enterprise has developed a new strategic plan. The enterprise architecture (EA) was revised to address the strategic goals and objectives in the plan and to align with the new strategic initiatives. The EA is now aligned with the strategic plan but its impact on existing programs needs to be assessed to determine necessary changes to program budgets and schedules. The corporate portfolio management process will be performed to realign the portfolio of programs, projects, technologies and systems. The architecture evaluation process is used to provide data for use during the portfolio realignment. The stakeholder concerns in Table C.13 are deemed to be relevant.

**Table C.13 — Enterprise architecture — Stakeholder concerns**

| Stakeholder | Concerns |
|---|---|
| Chief executive officer | Programs are in alignment with the new strategic goals and objectives |
| Chief information officer | Impact of new EA on cyber threat posture and cyber initiatives |
| Program manager | Cost and schedule impact on baselined program plans; increased risk of program execution |
| Enterprise operations | Improved customer satisfaction; improved profit margins |

#### C.5.2 Enterprise architecture — Evaluation synthesis

**Table C.14 — Enterprise architecture — Evaluation synthesis**

| Objectives | Factors & subfactors | Evaluation synthesis approach | Results |
|---|---|---|---|
| Align programs with strategic plan | Enterprise capability gaps Enterprise capability overlaps Synergy with business partners Marketplace coverage | — Review panel consisting of program managers | Review panel report to architecture governance board Business impact summary to board & shareholders Customer impact summary to board |
| Improve cyber threat resilience | Threat identification Threat countermeasure effectiveness Threat damage recovery Overall operational uptime | — Model walkthrough by cyber domain experts | — Cyber domain working group report to chief information officer and to architecture governance board |
| Improve customer satisfaction | Time to market Feature quality Ease of use Low cost operations | — System experiments to emulate new features in the revised EA | Board visit to system lab to witness customer engagement and observe reactions Customer survey report to architecture governance board |

#### C.5.3 Enterprise architecture — Value assessment

**Table C.15 — Enterprise architecture — Value assessment**

| Value aspect being assessed | Objectives | Factors & subfactors | Value assessment method | Results |
|---|---|---|---|---|
| Enterprise viability | Align programs with strategic plan | EA-program plan disconnects Business partner dependencies | — Business impact assessment | — Business impact assessment report to review panel |
| Assured customer deliveries | Improve cyber threat resilience | Threat damage impacts Threat response impacts Overall operational uptime | — Mission impact assessment | — Mission impact assessment report to cyber working group |
| Meeting profit targets | Improve customer satisfaction | Time to market Feature quality Ease of use Low cost operations | — Customer focus groups with follow-on surveys | — Customer reaction report to program managers and to architecture governance board |

#### C.5.4 Enterprise architecture — Architectural analysis

**Table C.16 — Enterprise architecture — Architectural analysis**

| Object being analyzed | Objectives | Factors & subfactors | Architectural analysis method | Results |
|---|---|---|---|---|
| Programs and projects | Align programs with strategic plan | Development cost & schedule Field support costs Program risks and opportunities | Cost analysis Schedule analysis Risk analysis | Revised program budgets & schedules Revised risk list and risk mitigation plans |
| None. No analysis is needed since assessment method above generates its own information to complete the assessment | Improve cyber threat resilience | — N/A | — N/A | — N/A |
| None. No analysis is needed since assessment method above generates its own information to complete the assessment | Improve customer satisfaction | — N/A | — N/A | — N/A |

## Annex D (informative) — Example architecture evaluation frameworks

### D.1 General

Example architecture evaluation frameworks are provided to illustrate how this document can be applied. This does not imply endorsement of these particular examples. The following examples are provided:

- Architecture Tradeoff Analysis Method (ATAM);

- Quality Assessment of System Architectures and their Requirements (QUASAR); and

- Analysis of Alternatives (AoA).

### D.2 Architecture Tradeoff Analysis Method (ATAM)

#### D.2.1 Overview

##### D.2.1.1 General

Architecture Tradeoff Analysis Method® [ATAM®2)], as described in Reference [59] is a framework for software architecture and design trade-offs. However, ATAM is also used for evaluating architectures of software-reliant systems relative to business and quality goals and for analysis of how those goals trade off against each other.

In the ATAM framework, quality attributes such as performance, availability, security and modifiability are derived from business drivers in order to express how software and system properties can sustain business goals.

NOTE 1 As summarized in Table D.1, the main ATAM concepts map to architecture evaluation concepts as defined in this document.

**Table D.1 — Mapping of the main ATAM concepts**

| ATAM concepts | Concepts as defined in this document |
|---|---|
| Business goal | Concern |
| Business objective | Evaluation objective |
| Business driver | Evaluation factor |
| Architecture quality | Assessment objective |
| Risk and non-risk | Assessment factors |
| Sensitivity point Tradeoff point | Assessment factors |
| Quality factor | Analysis factors |

2) ATAM and Architecture Tradeoff Analysis Method are registered trademarks of Carnegie Mellon University. This information is given for the convenience of users of this document and does not constitute an endorsement by ISO, IEC or IEEE of the method named.

##### D.2.1.2 Purpose

The purpose of the ATAM is to evaluate architectures in light of quality attribute requirements through business drivers with regard to business goals. Sensitivity points and trade-off points are formalized by ATAM evaluations which expose architectural risks that potentially inhibit the achievement of business goals of an organization. These evaluations can be executed at different life-cycle stages of the architecture and the system of interest it targets.

##### D.2.1.3 Basic approach

An ATAM evaluation examines an architecture in terms of quality attributes about the suitability of the architecture for the system for which it was designed to formulate one or more evaluation objectives. Suitability begins with an understanding of the business drivers: What business goals are most central to guarantee the system is fit for purpose and it motivates the system quality attributes? Examples of categories of objectives extracted from actual ATAM evaluations are described in Reference [60]: reduce total cost of ownership, improve capability/quality of system, improve market position, support improved business processes and improve confidence in and perception of the system. The evaluation factors include cost, schedule, quality and risk to achieving the objectives.

##### D.2.1.4 Conceptual flow

As illustrated in Figure D.1, business drivers and the architecture are elicited from project decision makers. These are refined into scenarios and the architectural decisions made in support of each one. Analysis of scenarios and decisions results in identification of risks, non-risks, sensitivity points and trade-off points in the architecture. Risks are synthesized into a set of risk themes, showing how each one threatens a business driver.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure D.1 — A conceptual flow of the ATAM**

##### D.2.1.5 Sequence of steps

The project starts with preliminary steps:

- Present the ATAM. The evaluation leader describes the evaluation method to the participants, sets expectations and answers questions.

- Present business drivers. A project spokesperson describes what business goals are motivating the development effort and hence what will be the architectural drivers.

- Present architecture. The architect describes the architecture, focusing on how it addresses the

business drivers.

- Identify architectural approaches. The architect identifies architectural approaches. The evaluation activities are conducted in a series of steps:

- Generate quality attribute utility tree. The evaluation team elicits quality factors that comprise system "utility" from the architecture team.

- Analyze architectural approaches. Architectural approaches that address the high-priority factors are analyzed. Architectural risks, non-risks, sensitivities and trade-offs are identified.

- Brainstorm and prioritize scenarios. The evaluation team elicits a larger set of scenarios from the entire group of stakeholders.

- Analyze architectural approaches. Architectural approaches that address the highly-ranked scenarios are analyzed. These scenarios are test cases to confirm the analysis performed thus far.

- Present results. The evaluation team presents the findings to the stakeholders.

##### D.2.1.6 Expected results

The primary evaluation result is the collection of risk themes that group related risks and summarize their impact on the architecture and the business drivers. Other outputs include the artifacts created or refined to conduct the analysis (e.g., architectural approaches, utility tree, scenarios) and the detailed analysis results (e.g., risks, non-risks, sensitivity points and trade-offs points).

NOTE 2 Risk themes extracted from ATAM evaluations are described in Reference [61].

#### D.2.2 Evaluation synthesis

ATAM is an architecture evaluation approach focusing on architecture quality. Considered evaluation objectives are business objectives derived from business goals. And business drivers are evaluation factors.

An evaluation synthesis can involve the combination of results from one or several value assessments where ATAM is one of those value assessments performed to determine to what extent the evaluation objectives (for the entire AE effort) will be achieved. This could involve an examination of trade-offs between the results from the different value assessments.

#### D.2.3 Value assessment

Value assessment in ATAM determines the extent to which architectural quality addresses the business goals from the system properties point of view: What are the quality attributes that motivate or influence the architecture? What are the desired results for these attributes to meet business and quality goals?

The assessment method is the scenario-based ATAM technique called “Analyze Architectural Approaches”. The method analyzes how well the architecture decisions meet the needs identified in prioritized scenarios that can occur during the lifecycle of the system. Given the high priority factors,

the evaluation team elicits and analyzes the architectural approaches that address those factors. For example, an architectural approach aimed at meeting modifiability goals will be subjected to modifiability analysis. The evaluation team records the discussion surrounding the architectural decision, risks, non-risks, sensitivities, trade-offs and open issues.

NOTE Analyze Architectural Approaches is not quality-attribute specific with specific criteria in the form of questions “embedded” in the technique. Any quality attribute can be analyzed.

The primary assessment result is the collection of potentially problematic architectural decisions that put the stakeholder needs at risk and how they trade-off against each other.

For value assessment, risks, non-risks, sensitivity points and trade-off points can be considered as assessment factors.

The focus is on the quality attributes of interest to a stakeholder and related quality attributes that are involved in trade-offs. The quality attributes are represented as a six-part scenario that is used to represent stakeholders’ interests, understand the requirements and provide the context and measure against which to analyze decisions. The six parts of a quality attribute scenario are: source, stimulus, artifact, environment, response and response measure.

An example modifiability scenario is: A developer wishes to change the UI during design time; the change is made and unit tested in three hours. Another example, a performance scenario, is: Users initiate transactions during normal operation; the transactions are processed with an average latency of two seconds. The values obtained in these scenarios support the evaluation objectives such as the business goals to enter new markets and reduce time to market.

#### D.2.4 Architectural analysis

Architectural analysis in ATAM examines the key attributes of the architecture along dimensions of quality such as availability, interoperability, modifiability, performance, security, testability and usability. The analysis factors are the response measure part of the six-part quality attribute scenario, such as latency, effort or time to repair in the case of performance, modifiability and availability.

ATAM doesn’t stipulate an analysis method. It brings together the necessary stakeholders to focus on a particular concern in a part of the system. The evaluation team may employ lightweight analysis techniques such as reflective questions, architectural tactics-based questionnaires, design-based checklists and quality attribute scenario-based analysis. Questions probe architectural decisions that bear on quality attribute requirements. For example, if the quality attribute of interest is performance then a question might be: How are priorities assigned to processes? If the quality attribute of interest is modifiability, then a question might be: Are there any places where layers are circumvented? The architect may have gathered the necessary information prior to the evaluation and present it as supporting evidence.

The responses will be evaluated in terms of how the decisions impact the execution of the scenario (e.g., two second latency, making changes within three hours) to inform the analysis result.

The analysis result is compared with the expected response to determine whether the stakeholder concerns associated with each quality attribute are satisfied or at risk. This assessment result in turn influences the evaluation result as risks are distilled into risk themes that impact the architecture and business drivers.

NOTE Quality attributes extracted for ATAM evaluations are described in Reference [62].

#### D.2.5 Evaluation plan and report

The ATAM process contains the guidance and aids needed to produce an evaluation plan and carry out an actual evaluation. Before the analysis can begin, a setup phase is conducted in which the evaluation team is created and a partnership is formed between the evaluation team and the project whose architecture is being evaluated.

The ATAM process provides guidance for producing an architecture evaluation report in the form of a presentation and a document. The presentation is a required artifact and its presentation to all stakeholders is a required step in the evaluation. The presentation recapitulates the steps of the ATAM evaluation and presents the outputs, including: business drivers, architectural approaches, utility tree, scenarios, risks and non-risks, sensitivities and tradeoffs and risk themes. The final report includes the outputs documented in the presentation as well as: an executive summary, more detailed description of the analysis and next steps. The evaluation team also reflects on the quality of the evaluation and recommends improvements to the ATAM materials.

NOTE ATAM plan and report are documented in Reference [63].

### D.3 The Method Framework and QUASAR method

#### D.3.1 Overview

The Method Framework for Engineering System Architectures (MFESA)[64] is a framework that enables systems architects and engineers to create methods for systems architectures. The framework comprises:

- an ontology of concepts and terminology;

- a metamodel of the types of method elements (components);

- a repository containing reusable method components together with reusable methods constructed from such method components; and

- a metamethod for creating project-specific methods for systems architecting.

QUality Assessment of System Architectures and their Requirements (QUASAR) is a method that can be used in conjunction with MFESA.

#### D.3.2 Evaluation synthesis

In fulfilment of part of one of the MFESA processes the QUASAR method[65][66] can be used to assess the quality of system architectures and their associated architecturally significant quality requirements. Whilst functional requirements satisfaction is handled by many requirements engineering (including requirements management) techniques, coverage of satisfaction of non-functional requirements (sometimes termed ‘ilities’) is generally not so well addressed, especially as they shift from external to internal and then a technical focus during system development.

QUASAR is based on the:

- production of requirements and architecture quality cases as an intrinsic part of requirements engineering and systems architecting; and

- independent assessment of these quality cases by assessment teams staffed by people who are trained and experienced in the requisite technical disciplines.

#### D.3.3 Value assessment

The quality of a system is based upon a quality model comprising quality characteristics, quality attributes and measurement scales and methods. QUASAR may be applied at different system tiers and can assess quality from both external and internal perspectives.

The characteristics which can be assessed include:

- external quality characteristics such as compliance, configurability, dependability, efficiency, environmental compatibility, functionality, habitability, interoperability, operability, serviceability and usability;

- internal quality characteristics such as feasibility, interoperability, portability, producibility, reusability, modifiability (including maintainability) and testability; and

- performance (quality) attributes such as jitter, latency, response time, schedulability and throughput.

#### D.3.4 Architectural analysis

In QUASAR[65][66] the achievement of quality is described in quality cases which are based on a generalization of safety/assurance cases and are formed from the recording of quality claims concerning the satisfaction of quality goals and non-functional requirements supported by clear and compelling arguments and sufficient and credible evidence. They are restricted to the level of detail appropriate for a system architecture description and the arguments may be simplified as compared with those used in safety/assurance cases.

The quality characteristics and attributes which are to be assessed may be structured by tiering these quality factors (as requirements cases) or by relating them to specific system entities such as subsystems, with the former approach being preferred. This can be achieved through structuring of the corresponding claims. Each of the leaf node quality factors can then be assessed based on the formulation of a specific claim.

Assessors probe the quality cases for their weaknesses and potential risk, and the structuring of the quality characteristics and attributes for their veracity. The assessors determine assessment results and provide corresponding reports.

Figure D.2 below shows how QUASAR and the associated structuring of quality characteristics and attributes conforms with the architecture evaluation framework tiers as defined in this document.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure D.2 — Correspondence of QUASAR concepts with those advocated in this document**

#### D.3.5 Evaluation plan and report

QUASAR[65][66] says nothing about the evaluation plan and report.

### D.4 Analysis of Alternatives (AoA)

#### D.4.1 Overview

##### D.4.1.1 General

Analysis of Alternatives (AoA) study is an approach applied in the United States as a requirement of military acquisition policy. The approach is documented in the AoA Handbook[58] published by the Office of Aerospace Studies at the Air Force Materiel Command. The AoA study ensures that at least three feasible alternatives are analyzed prior to making costly investment decisions. The AoA establishes and benchmarks metrics for Cost, Schedule, Performance (CSP) and Risk (CSPR) depending on military "needs" derived from the Joint Capabilities Integration Development System process. It moves away from employing a single acquisition source to the exploration of multiple alternatives so agencies have a basis for funding the best possible projects in a rational, defensible manner considering risk and uncertainty.

##### D.4.1.2 Basic approach

The AoA is designed to examine a broad spectrum of potential alternatives to the mission need described in a Mission Needs Statement. The key purpose of the AoA is to identify a "solution" that will fulfil the stated requirements as optimally as possible commensurate with established cost and schedule constraints, at the lowest practicable risk. The "solution" may be a specific design or configuration but it is more than likely to be a set of design parameter values the combination of which would provide the optimal and most desirable means of fulfilling the stated requirements. Thus, any specific design that complies with the optimal "solution" parameter values is deemed acceptable. Value is measured in terms of effectiveness (MOEs) and suitability (MOSs).

##### D.4.1.3 Study objectives

The objectives of the AoA are to:

1) refine alternatives;

2) refine criteria;

3) refine evaluation;

4) work to gain consensus;

5) reduce uncertainty; and

6) choose an alternative.

##### D.4.1.4 Maturity assessment

The AoA assesses critical technology elements (CTEs) associated with each proposed materiel solution, identified in the Initial Capabilities Document (ICD), including: technology maturity, integration risk, manufacturing feasibility and, where necessary, technology maturation and demonstration needs.

##### D.4.1.5 Risk assessment

Risk is analyzed in many ways, such as technological maturity, manufacturing capacity, quality standards, manufacturing design, material and supply chain capacity, interoperability, operational survival, aggressiveness of the schedule, cost reasonableness, among many others. Each MOE and capability can carry an associated risk.

#### D.4.2 Evaluation synthesis

AoA is an approach for performing the synthesis of possibly multiple value assessment methods that are conducted under the umbrella of the overall assessment of architectural alternatives. Various evaluation approaches could be used during an AoA:

- expert review panel;

- prototype demonstration;

- system experiment;

- modeling and simulation;

- model walkthrough;

- technical analysis;

- concept review; or

- user symposium.

NOTE Only modeling and simulation and technical analysis are described in the AoA Handbook, although these other approaches are often used.

An evaluation synthesis involves the combination of results from multiple value assessments to determine to what extent the evaluation objectives (for the entire AoA effort) will be achieved. This could involve an examination of trade-offs between the results from the different value assessments.

#### D.4.3 Value assessment

Measures of Effectiveness (MOEs) and Measures of Suitability (MOSs) are associated with relevant mission tasks as exemplified in Table D.2.

**Table D.2 — Example of mission tasks and associated measures**

| Mission task | Measures of Effectiveness |
|---|---|
| Defeat target | MOE 1.1: Probability of kill |
| Defeat target | MOE 1.2: Number of weapons to defeat target |
| Defeat target | MOE 1.3: Range |
| Defeat target | MOE 1.4: Collateral damage |
| Survive threat | MOE 2.1: Time to launch |
| Survive threat | MOE 2.2: Probability of survival |
| Survive threat | MOE 2.3: Counter threats |
| Support system | MOS 3.1: Deployability |
| Support system | MOS 3.2: Maintainability |
| Support system | MOS 3.3: Mission reliability |

In AoA, value assessment is called effectiveness analysis and is focused on determination of MOEs and their respective values for alternative solutions with respect to the cost, schedule, risk and other factors for each alternative. However, usually the measures of suitability (MOSs) are also used in the value assessment. The general approach for effectiveness analysis is illustrated in Figure D.3.

NOTE ICD is Initial Capabilities Document, CDD is Capability Description Document.

> **图未收录**：源 docx 系 PDF→Word 产物，本图在源件中已被切碎或丢失，且位图与图题在文档流中错位、无法可靠归属，故不收录。需原图请查正版 PDF。

**Figure D.3 — General approach for effectiveness analysis**

#### D.4.4 Architectural analysis

The measures of value used during the effectiveness analysis are often reliant upon various performance analyses. Various Measures of Performance (MOPs) can be examined as the basis for the AoA’s architectural analysis, as illustrated in Table D.3.

**Table D.3 — Measures of performance (MOP) framework example**

| Task | Attribute | Measure | Metric | Criteria | Analysis method |
|---|---|---|---|---|---|
| Enhance survivability | Survivability | Probability of survival | Probability | ≥0,85 | M&S (BRAWLER) |
| Enhance survivability | Conditions: | Combat range (beyond and within threat detection range); engagement environment (contested, highly contested) | Combat range (beyond and within threat detection range); engagement environment (contested, highly contested) | Combat range (beyond and within threat detection range); engagement environment (contested, highly contested) | Combat range (beyond and within threat detection range); engagement environment (contested, highly contested) |
| Detect and identify threats | Completeness | Number of threat detections | Percentage | ≥98 % of threats | Parametric analysis |
| Detect and identify threats | Accuracy | Number of threat identifications | Percentage | ≥95 % unambigu-ous id of threats | Parametric analysis |
| Detect and identify threats | Conditions: | Electronic signal density (high); emitter environment (red, blue, gray and white); threat classes (low to high priority) | Electronic signal density (high); emitter environment (red, blue, gray and white); threat classes (low to high priority) | Electronic signal density (high); emitter environment (red, blue, gray and white); threat classes (low to high priority) | Electronic signal density (high); emitter environment (red, blue, gray and white); threat classes (low to high priority) |
| Sustain and maintain | Availability | Operational availability (Ao) | Probability | ≥0,98 | M&S (LCOM); expert elicitation |
| Sustain and maintain | Reliability | Weapon system reliability | Probability | ≥0,98 | Comparative analysis; expert elicitation |
| Sustain and maintain | Conditions: | Operations tempo (peacetime, wartime) | Operations tempo (peacetime, wartime) | Operations tempo (peacetime, wartime) | Operations tempo (peacetime, wartime) |

Table D.3 (continued)

| Task | Attribute | Measure | Metric | Criteria | Analysis method |
|---|---|---|---|---|---|
| Deploy system | Deployability | Operator rating of ability to transport system | Mode | Operators can easily transport system | Statistical analysis of operator responses to questionnaire items |
| Deploy system | Conditions: | Austere airfield environment; transport by C-130 aircraft | Austere airfield environment; transport by C-130 aircraft | Austere airfield environment; transport by C-130 aircraft | Austere airfield environment; transport by C-130 aircraft |

#### D.4.5 Evaluation plan and report

The AoA Handbook[58] provides a standardized template for the AoA plan and report.

## Bibliography

1) ISO/IEC/IEEE 12207, Systems and software engineering — Software life cycle processes

2) ISO/IEC 15026-1, Systems and software engineering — Systems and software assurance — Part 1:

Concepts and vocabulary

3) ISO/IEC/IEEE 15288, Systems and software engineering — System life cycle processes

4) ISO/IEC/IEEE 15289, Systems and software engineering — Content of life-cycle information items (documentation)

5) ISO 15704, Industrial automation systems — Requirements for enterprise-reference architectures and methodologies

6) ISO/IEC 19501, Information technology — Open Distributed Processing — Unified Modeling Language (UML) Version 1.4.2

7) ISO/IEC 25000, Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Guide to SQuaRE

8) ISO/IEC 25010, Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models

9) ISO/IEC 25012, Software engineering — Software product Quality Requirements and Evaluation (SQuaRE) — Data quality model

10) ISO/IEC 25020, Systems and software engineering — Systems and software Quality Requirements

and Evaluation (SQuaRE) — Measurement reference model and guide

11) ISO/IEC 25021, Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Quality measure elements

12) ISO/IEC 33001, Information technology — Process assessment — Concepts and terminology

13) ISO/IEC/IEEE 42010:2011, Systems and software engineering — Architecture description

14) ISO/IEC/IEEE 42020:2019, Systems and software engineering — Architecture processes

15) Akao Yoji, 1990. Quality Function Deployment: Integrating Customer Requirements into

Product Design, trans. by Glenn H. Mazur and Japan Business Consultants, Ltd., Productivity Press, Cambridge, MA, USA

16) Clements Paul, Kazman Rick, Klein Mark, 2002. Evaluating Software Architectures: Methods and Case Studies, Addison-Wesley, Boston, MA, USA

17) Greefhorst Danny, Proper Erik, Architecture Principles - The Cornerstones of Enterprise Architecture, 1st Edition, Springer, 2011

18) Greefhorst D., Proper E., “The Roles of Principles in Enterprise Architecture, http://archixl

.nl/files/tear2010_principles.pdf

19) Hilliard R., M. Kurland, S. Litvintchouk, T. Rice, and S. Schwarm. 1996. Architecture Quality Assessment Version 2.0. The MITRE Corp. http://web.mit.edu/richh/www/writings/aqa-v2.pdf.

20) Kazman R., Klein M., Mario R Barbacci, Tom Longstaff, Howard Lipson, and Jeromy Carriere. July 1998. The Architecture Tradeoff Analysis Method. Software Engineering Institute, CMU/SEI-98-TR-008, Software Engineering Institute, Pittsburgh, PA, USA. http://www

.sei.cmu.edu/library/abstracts/reports/98tr008.cfm

21) Keeney R. L., 1996). Value-Focused Thinking: A Path to Creative Decisionmaking. Harvard University Press

22) NSA, Information Assurance Technical Framework, Unclassified, IATF Release 3.0-September 2000, A security guidance document developed by NSA’s ISSO organization with support from security advocates in government and industry

23) Obbink Henk, Kruchten Philippe, Kozaczynski Wojtek, Postema Herman, Ran Alexander, Dominick Lutz, Kazman Rick, Hilliard Rich, Tracz Will, Kahane Ed, 2002. Software Architecture Review and Assessment (SARA) Report, Version 1.0

24) Parnell Gregory S., (editor). 2017. Trade-off Analytics: Creating and Exploring the System Tradespace Wiley Series in Systems Engineering and Management

25) Vitruvius BC, De architectura, Marcus Vitruvius Pollio (1st century BC) (Transl. Morris Hicky Morgan, 1960), The Ten Books on Architecture. Courier Dover Publications. ISBN 0-486-20645-9

26) American Society for Quality, Glossary – Entry: Quality, retrieved 2017-08-01

27) Boehm B., Kukreja N., (2015), An initial Ontology for System Qualities, Proceedings of 25th INCOSE Symposium, Seattle, USA

28) Crosby Philip, (1979). Quality is Free. New York: McGraw-Hill. ISBN 0-07-014512-1

29) Drucker P. F., (1986). Innovation and entrepreneurship: Practice and principles. New York:

Harper Row

30) Juran, Joseph M and Joseph A Defeo (2010), Quality Control Handbook, New York, McGraw-

Hill, 6th Edition

31) Kiran D R, (2017), Total Quality Management: Key Concepts and Case Studies, Edition 1,

Elsevier, Butterworth Heinemann publications

32) Taguchi G., (1992). Taguchi on Robust Technology Development. ASME Press. ISBN 978- 99929-1-026-9

33) Kumar A., Doji S. L, Nikhil R Z, and Swaminathan N (2016), Value based System Architecting: Illustrated by Designing a Task Automation System, Proceedings of 26th INCOSE Symposium,

Edinburgh, UK

34) Kumar A., Doji S. L, Nikhil R Z, and Jose K R (2017), Value based Architecture of Digital Product-

Service Systems, Proceedings of 27th INCOSE Symposium, Adelaide, Australia

35) Len Bass, Paul Clements, Rick Kazman, 2003, Software Architecture in Practice, 2nd Edition,

Addison Wesley Publications, ISBN: 0-321-15495-9

36) Paul Clements, Rick Kazman, Mark Klein, 2002, Evaluating Software Architectures: Methods and Case Studies, 1st Edition, Addison Wesley Publications, ISBN-10: 0-201-70482-X

37) The qualities of architecture, John Critchley, March 10th, 2008

38) Vitruvius BC, De architectura, Marcus Vitruvius Pollio (1st century BC) (Transl. Morris 2106 Hicky Morgan, 1960), The Ten Books on Architecture. Courier Dover Publications. ISBN 0-2107 486-20645-9

39) Characteristics of Good Architecture, Enterprise Architect User Guide v13.0, Sparx Systems, 2018, url: http: /sparxsystems.com/enterprise_architect_user_guide/13.0/guidebooks/ea

_characteristics_of_good_architecture.html

40) Simon A, Herbert, 1962, The Architecture of Complexity, Proceedings of the American Philosophical Society, Vol. 106, No. 6. (Dec. 12, 1962), pp 467-482

41) Boehm B. W., Brown J. R., Kaspar H., Lipow M., McLeod G., Meritt M., Characteristics of

Software Quality, Edition 2, North-Holland Pub. Co., 1978

42) [Broy, 2009] Automotive Architecture Framework: Towards a Holistic and Standardised System Architecture Description, An overview on description concepts, models and methods

43) Parnell Gregory S., (ed.) (2017). Trade-off Analytics: Creating and Exploring the System Tradespace (Wiley Series in Systems Engineering and Management, January 2017)

44) Parnell Gregory S., Bresnick Terry, Tani Steven N., Johnson Eric R., (2013). Handbook of

Decision Analysis (Wiley Handbooks in Operations Research and Management Science, April 2013)

45) Weill P., (2007), Innovating in Information Systems: What do the most agile firms in the world do? Sixth e-Business Conference, Barcelona Spain

46) Mark W., Maier (1996), Architecting Principles for Systems-of-Systems, DOI: 10.1002/j.2334- 5837.1996.tb02054.x

47) Evans D., (2014), Styles of Architecting - A smarter approach to architecting the Defence Enterprise, Niteworks White Paper

48) Doji S., Lokku, Value distilled: A framework based approach to establish the trace of technology value in the context of engineering management, 2011 IEEE EUROCON - International Conference on Computer as a Tool, Lisbon, 2011, pp. 1-4

49) Gilb T., Fundamental Principles of Evolutionary Project Management, Proceedings of 15th INCOSE Symposium, 2005, New York, USA

50) Kumar A., Doji S. L, Nikhil R Z, and Jose K R, Value based Architecture of Digital Product-

Service Systems, Proceedings of 27th INCOSE Symposium, 2017, Adelaide, Australia

51) Kumar A., Doji S. L, Nikhil R Z, and Swaminathan N, Value based System Architecting: Illustrated by Designing a Task Automation System, Proceedings of 26th INCOSE Symposium, 2016, Edinburgh, U

52) Menger C., (1976). Principles of economics. (Dingwall J., Hoselitz B. E., Trans.). New York: New York University Press. (Original work published 1871)

53) Porter M.E., Competitive Advantage: Creating and Sustaining Superior Performance, ( Revised edition), The Free Press, 2004

54) Selva D., Crawley E.F., VASSAR: Value Assessment of System Architectures using Rules, in Proceedings of the 2013 IEEE Aerospace Conference, Big Sky, Montana, 2013

55) Zeithaml Valarie (1998),, Consumer Perceptions of Price, Quality, and Value: A Means-End Model and Synthesis of Evidence, Journal of Marketing, Vol. 52 (July 1988), 2-22

56) Ring J., 1998. A Value Seeking Approach to the Engineering of Systems. Proceedings of the IEEE

Conference on Systems, Man, and Cybernetics. p. 2704-2708

57) Perakath C., Benjamin et al., 1994, IDEF5 Method Report, Knowledge Based Systems, Inc

58) Office of Aerospace Studies, Air Force Material Command (AFMC) OAS/A9, Analysis of Alternatives, (AoA) Handbook, A Practical Guide to Analyzes of Alternatives" (PDF). Retrieved 24 August 2017

59) CMU/SEI-2000-TR-004, “ATAM: Method for Architecture Evaluation”, Rick Kazman, Mark Klein and Paul Clements, technical report, Software Engineering Institute, Carnegie Mellon University,

August 2000

60) CMU/SEI-2005-TR-021: “Categorizing Business Goals for Software Architectures”. Rick Kazman and Len Bass. Software Engineering Institute, Carnegie Mellon University, 2005

61) CMU/SEI-2006-TR-012, “Risk Themes Discovered Through Architecture Evaluations”. Len Bass, Robert Nord, William Wood and David Zubrow. Pittsburgh, PA: Software Engineering Institute,

Carnegie Mellon University, 2006

62) “Insights from 15 Years of ATAM Data: Towards Agile Architecture”, Stephany Bellomo, Ian Gorton, and Rick Kazman, IEEE Software, September/October, 2015, 32:5, 38-45

63) “Evaluating Software Architectures: Methods and Case Studies”, 2002 published by Addison- Wesley.

64) Firesmith Donald et al. , The Method Framework for Engineering System Architectures,

Auerbach/CRC Press 2009, ISBN 978-1-4200-8575-4

65) Firesmith D., QUality Assessment of System Architectures and their Requirements (QUASAR), presentation 2007, available online at http://www.sei.cmu.edu/library/assets/quality-assess.pdf

66) Firesmith D., QUASAR: A Method for the QUality Assessment of Software-Intensive System

Architectures, CMU/SEI-2006-HB-001, SEI Handbook 2006, available online at http://resources

.sei.cmu.edu/asset_files/Handbook/2006_002_001_14627.pdf

67) Structured Metrics Metamodel Specification Version 1.1.1, Object Management Group, URL:

https://www.omg.org/spec/SMM/1.1.1/

## IEEE notices and abstract

### Important Notices and Disclaimers Concerning IEEE Standards Documents

IEEE documents are made available for use subject to important notices and legal disclaimers. These notices and disclaimers, or a reference to this page, appear in all standards and may be found under the heading “Important Notices and Disclaimers Concerning IEEE Standards Documents.” They can also be obtained on request from IEEE or viewed at http: /standards.ieee.org/IPR/disclaimers.html.

### Notice and Disclaimer of Liability Concerning the Use of IEEE Standards Documents

IEEE Standards documents (standards, recommended practices, and guides), both full-use and trial-use, are developed within IEEE Societies and the Standards Coordinating Committees of the IEEE Standards Association (“IEEE-SA”) Standards Board. IEEE (“the Institute”) develops its standards through a consensus development process, approved by the American National Standards Institute (“ANSI”), which brings together volunteers representing varied viewpoints and interests to achieve the final product. IEEE Standards are documents developed through scientific, academic, and industry-based technical working groups. Volunteers in IEEE working groups are not necessarily members of the Institute and participate without compensation from IEEE. While IEEE administers the process and establishes rules to promote fairness in the consensus development process, IEEE does not independently evaluate, test, or verify the accuracy of any of the information or the soundness of any judgments contained in its standards.

IEEE Standards do not guarantee or ensure safety, security, health, or environmental protection, or ensure against interference with or from other devices or networks. Implementers and users of IEEE Standards documents are responsible for determining and complying with all appropriate safety, security, environmental, health, and interference protection practices and all applicable laws and regulations.

IEEE does not warrant or represent the accuracy or content of the material contained in its standards, and expressly disclaims all warranties (express, implied and statutory) not included in this or any other document relating to the standard, including, but not limited to, the warranties of: merchantability; fitness for a particular purpose; non-infringement; and quality, accuracy, effectiveness, currency, or completeness of material. In addition, IEEE disclaims any and all conditions relating to: results; and workmanlike effort. IEEE standards documents are supplied “AS IS” and “WITH ALL FAULTS.”

Use of an IEEE standard is wholly voluntary. The existence of an IEEE standard does not imply that there are no other ways to produce, test, measure, purchase, market, or provide other goods and services related to the scope of the IEEE standard. Furthermore, the viewpoint expressed at the time a standard is approved and issued is subject to change brought about through developments in the state of the art and comments received from users of the standard.

In publishing and making its standards available, IEEE is not suggesting or rendering professional or other services for, or on behalf of, any person or entity nor is IEEE undertaking to perform any duty owed by any other person or entity to another. Any person utilizing any IEEE Standards document, should rely upon his or her own independent judgment in the exercise of reasonable care in any given circumstances or, as appropriate, seek the advice of a competent professional in determining the appropriateness of a given IEEE standard.

IN NO EVENT SHALL IEEE BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO: PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE PUBLICATION, USE OF, OR RELIANCE UPON ANY STANDARD, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE AND REGARDLESS OF WHETHER SUCH DAMAGE WAS FORESEEABLE.

### Translations

The IEEE consensus development process involves the review of documents in English only. In the event that an IEEE standard is translated, only the English version published by IEEE should be considered the approved IEEE standard.

### Official statements

A statement, written or oral, that is not processed in accordance with the IEEE-SA Standards Board Operations Manual shall not be considered or inferred to be the official position of IEEE or any of its committees and shall not be considered to be, or be relied upon as, a formal position of IEEE. At lectures, symposia, seminars, or educational courses, an individual presenting information on IEEE standards shall make it clear that his or her views should be considered the personal views of that individual rather than the formal position of IEEE.

### Comments on standards

Comments for revision of IEEE Standards documents are welcome from any interested party, regardless of membership affiliation with IEEE. However, IEEE does not provide consulting information or advice pertaining to IEEE Standards documents. Suggestions for changes in documents should be in the form of a proposed change of text, together with appropriate supporting comments. Since IEEE standards represent a consensus of concerned interests, it is important that any responses to comments and questions also receive the concurrence of a balance of interests. For this reason, IEEE and the members of its societies and Standards Coordinating Committees are not able to provide an instant response to comments or questions except in those cases where the matter has previously been addressed. For the same reason, IEEE does not respond to interpretation requests. Any person who would like to participate in revisions to an IEEE standard is welcome to join the relevant IEEE working group.

Comments on standards should be submitted to the following address: Secretary, IEEE-SA Standards Board

445 Hoes Lane Piscataway, NJ 08854 USA

### Laws and regulations

Users of IEEE Standards documents should consult all applicable laws and regulations. Compliance with the provisions of any IEEE Standards document does not imply compliance to any applicable regulatory requirements. Implementers of the standard are responsible for observing or referring to the applicable regulatory requirements. IEEE does not, by the publication of its standards, intend to urge action that is not in compliance with applicable laws, and these documents may not be construed as doing so.

### Copyrights

IEEE draft and approved standards are copyrighted by IEEE under U.S. and international copyright laws. They are made available by IEEE and are adopted for a wide variety of both public and private uses. These include both use, by reference, in laws and regulations, and use in private self-regulation, standardization, and the promotion of engineering practices and methods. By making these documents available for use and adoption by public authorities and private users, IEEE does not waive any rights in copyright to the documents.

### Photocopies

Subject to payment of the appropriate fee, IEEE will grant users a limited, non-exclusive license to photocopy portions of any individual standard for company or organizational internal use or individual, non-commercial use only. To arrange for payment of licensing fees, please contact Copyright Clearance Center, Customer Service, 222 Rosewood Drive, Danvers, MA 01923 USA; +1 978 750 8400. Permission to photocopy portions of any individual standard for educational classroom use can also be obtained through the Copyright Clearance Center.

### Updating of IEEE Standards documents

7799

Users of IEEE Standards documents should be aware that these documents may be superseded at any time by the issuance of new editions or may be amended from time to time through the issuance of amendments, corrigenda, or errata. An official IEEE document at any point in time consists of the current edition of the document together with any amendments, corrigenda, or errata then in effect.

Every IEEE standard is subjected to review at least every ten years. When a document is more than ten years old and has not undergone a revision process, it is reasonable to conclude that its contents, although still of some value, do not wholly reflect the present state of the art. Users are cautioned to check to determine that they have the latest edition of any IEEE standard.

In order to determine whether a given document is the current edition and whether it has been amended through the issuance of amendments, corrigenda, or errata, visit the IEEE-SA Website at http: /ieeexplore.ieee.org/xpl/standards.jsp or contact IEEE at the address listed previously. For more information about the IEEE-SA or IEEE’s standards development process, visit the IEEE-SA Website at http: /standards.ieee.org.

### Errata

Errata, if any, for all IEEE standards can be accessed on the IEEE-SA Website: http: /standards.ieee

.org/findstds/errata/index.html. Users are encouraged to check this URL for errata periodically.

### Patents

Attention is called to the possibility that implementation of this standard may require use of subject matter covered by patent rights. By publication of this standard, no position is taken by the IEEE with respect to the existence or validity of any patent rights in connection therewith. If a patent holder or patent applicant has filed a statement of assurance via an Accepted Letter of Assurance, then the statement is listed on the IEEE-SA Website at http: /standards.ieee.org/about/sasb/patcom/patents

.html. Letters of Assurance may indicate whether the Submitter is willing or unwilling to grant licenses under patent rights without compensation or under reasonable rates, with reasonable terms and conditions that are demonstrably free of any unfair discrimination to applicants desiring to obtain such licenses.

Essential Patent Claims may exist for which a Letter of Assurance has not been received. The IEEE is not responsible for identifying Essential Patent Claims for which a license may be required, for conducting inquiries into the legal validity or scope of Patents Claims, or determining whether any licensing terms or conditions provided in connection with submission of a Letter of Assurance, if any, or in any licensing agreements are reasonable or non-discriminatory. Users of this standard are expressly advised that determination of the validity of any patent rights, and the risk of infringement of such rights, is entirely their own responsibility. Further information may be obtained from the IEEE Standards Association.

### Abstract and keywords

ICS 35.080

© ISO/IEC 2019 – All rights reserved 82

Copyright Notice

The Canadian adoption of this International Standard as a National Standard of Canada contains information copyright protected by CSA Group. All rights reserved. No part of this National Standard of Canada may be reproduced in any form whatsoever without the prior permission of CSA Group. ISO/IEC material is reprinted with permission.

Requests for permission to reproduce this National Standard of Canada or parts thereof should be addressed to:

Manager, Sales CSA Group

178 Rexdale Boulevard Toronto, Ontario M9W 1R3

Copyright violators will be prosecuted to the full extent of the law.

ISBN 978-1-4883-3082-7
