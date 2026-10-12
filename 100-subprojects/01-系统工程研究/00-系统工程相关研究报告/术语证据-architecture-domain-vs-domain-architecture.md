# Verbatim evidence list: "architecture domain" vs "domain architecture"

Scope rule applied throughout: every quote below was copied character-for-character from a source I
retrieved during this research. Where a source could not be read, the item is listed under
"Could not verify" instead of being filled in from memory or from a secondary summary.

---

## 1. ISO/IEC/IEEE 42020:2019 — *Software, systems and enterprise — Architecture processes*

### 1.1 The published table of contents: E.4.1.5 is titled "Domain architecture" (VERIFIED)

- QUOTE (verbatim lines of the Contents, in printed order):

  > E.4 Architecture kinds, views and styles
  > E.4.1 Architecture kinds
  > E.4.1.1 General
  > E.4.1.2 Enterprise architecture
  > E.4.1.3 Overarching or strategic architecture
  > E.4.1.4 Reference architecture
  > E.4.1.5 Domain architecture
  > E.4.1.6 Baseline architecture
  > E.4.1.7 Target architecture
  > E.4.1.8 System architecture
  > E.4.1.9 Product line architecture
  > E.4.1.10 System of systems architecture
  > E.4.1.11 Product-service system architecture
  > E.4.1.12 Data architecture

  > Annex E (informative) Notes on terms and concepts

- SOURCE: ISO/IEC/IEEE 42020:2019 (E), *Software, systems and enterprise — Architecture processes*,
  Contents, Annex E (informative) "Notes on terms and concepts", E.4 "Architecture kinds, views and
  styles", E.4.1 "Architecture kinds", E.4.1.5 "Domain architecture". Header line of the retrieved PDF
  reads: "ISO/IEC/IEEE 42020:2019 (E) / Software, systems and enterprise — Architecture processes /
  Contents".
- URL (actually read): https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:311944607/toc-3094876/download
- Note: this is the official table-of-contents PDF published by DIN (the German ISO member) for the
  published 2019 edition. **The user's belief that E.4.1.5 exists is confirmed.**

### 1.2 The published E.4.1.5 body text — NOT OBTAINABLE

The body text of the published E.4.1.5 could not be read. Every full-text route failed: the ISO OBP
page and iso.org product page returned HTTP 403 (Cloudflare interstitial), ANSI/BSI, Intertek Inform and
Accuris previews returned HTTP 403, and the antpedia "full text" mirror served only a 3-page cover.
Stated explicitly: **I did not read the published E.4.1.5 text and therefore cannot quote it.**

### 1.3 A 2017 Public Enquiry draft of the 42020 annexes — body text of the same entry (DRAFT, numbering shifted by one)

- QUOTE (verbatim, complete entry as printed in the draft):

  > E.4.1.4 Domain architecture
  >
  > A generic, organizational structure or design for systems in a domain.
  >
  > [Based on IEEE Std 1517-1999 (R2004) IEEE Standard for Information Technology — Software Life Cycle
  > Processes — Reuse Processes, and modified by generalizing in terms of systems rather than software
  > systems]
  >
  > NOTE The domain architecture contains the architectural forms that are capable of satisfying
  > requirements within a specific domain. A domain architecture 1) can be adapted to create designs for
  > systems within a domain, and 2) provides a framework for configuring assets within individual
  > systems.

- SOURCE: ISO/IEC/IEEE 42020 **Public Enquiry draft** of the annexes. The PDF's own metadata records
  `title: "M315676 - Public Enquiry"`, `creationDate: 2017-05-30`. Printed page number at the foot of
  the page is **84**; the entry is labelled **E.4.1.4 Domain architecture** in this draft.
- URL (actually read): https://coe.qualiware.com/wp-content/uploads/2016/11/42020annexes.pdf
  (PDF page 27 of 61)
- Why the numbering differs: the draft has **no** "E.4.1.1 General" subclause, so its E.4.1.1 …
  E.4.1.10 are Enterprise architecture … Product-Service Systems Architecture, i.e. each one sits one
  number lower than in the published Contents. Two independent corroborations inside the draft:
  - QUOTE: "E.3.3.1 Reference Architectures — Reference Architectures are defined in E.4.1.3." (draft
    printed page 82; in the published Contents "Reference architecture" is E.4.1.4.)
  - QUOTE (draft E.4.1.3, printed page 84): "A reference architecture is used by a community of
    interest as a shared and agreed reference description that can be used for that community's
    business purposes." (in the published Contents this title is "E.4.1.4 Reference architecture")
  - Consequently draft E.4.1.4 "Domain architecture" occupies the slot that the published Contents
    labels "E.4.1.5 Domain architecture".
- **CAVEAT (important):** the wording in 1.3 is *draft* wording. It is **not** verified against the
  published 2019 edition. It must not be presented as the text of published clause E.4.1.5.

### 1.4 "domain architecture" used elsewhere in the draft

- QUOTE (draft E.4.1.8 Product line architecture, printed page 85):
  > According to ISO/IEC/IEEE 24765, a product line is:
  > • From the commercial viewpoint, a group of products or services sharing a common, managed set of
  > features that satisfy specific needs of a selected market or mission.
  > • From the engineering viewpoint, a collection of systems that are potentially derivable from a
  > single domain architecture.
- SOURCE: same document as 1.3, E.4.1.8, printed page 85.
- URL: https://coe.qualiware.com/wp-content/uploads/2016/11/42020annexes.pdf (PDF page 28 of 61)

### 1.5 "architecture domain" in 42020

- FINDING: the string **"architecture domain" occurs zero times** in the entire 61-page Public Enquiry
  draft annexes document (case-insensitive full-text search). It also does not occur in the published
  Contents (section 1.1 above).
- What I could NOT verify: whether the published edition's Clause 3 "Terms and definitions" defines
  "architecture domain". Clause 3 of the published edition could not be read (paywall). Note 2 of
  42010:2022, 3.2 shows that 42020:2019 does have a Clause 3 containing at least "3.3 architecture".

### 1.6 How 42020's draft annex uses the bare word "domain"

- QUOTE (draft E.4.1 Architecture kinds, printed page 83):
  > Different kinds of architecture can be considered according to their purpose, domains of
  > application, and roles within entity and architecture life cycles.
- QUOTE (draft E.4.1.2 Overarching or strategic architecture, printed page 83):
  > NOTE Notion of overarching architecture is described in the NATO Architecture Framework. A similar
  > architecture kind is called "strategic architecture" in The Open Group Architecture Framework
  > (TOGAF).
- QUOTE (draft E.4.1.3 Reference architecture, printed page 84):
  > Reference architectures are used to (1) aid understanding of the forms of likely solutions to
  > problems within a particular domain, and (2) to maximize the possible commonality in forms of
  > solutions to similar problems within such a domain.
- SOURCE: same document as 1.3, E.4.1 / E.4.1.2 / E.4.1.3, printed page 83-84.
- URL: https://coe.qualiware.com/wp-content/uploads/2016/11/42020annexes.pdf (PDF pages 26-27 of 61)

---

## 2. ISO/IEC/IEEE 42010:2011 — *Systems and software engineering — Architecture description*

### 2.1 Clause 3 "Terms and definitions" in full (3.1 through 3.10)

- QUOTE (verbatim, complete clause 3 as printed):

  > 3.1 architecting
  > process of conceiving, defining, expressing, documenting, communicating, certifying proper
  > implementation of, maintaining and improving an architecture throughout a system's life cycle
  >
  > 3.2 architecture
  > fundamental concepts or properties of a system in its environment embodied in its elements,
  > relationships, and in the principles of its design and evolution
  >
  > 3.3 architecture description
  > AD
  > work product used to express an architecture
  >
  > 3.4 architecture framework
  > conventions, principles and practices for the description of architectures established within a
  > specific domain of application and/or community of stakeholders
  >
  > EXAMPLE 1 Generalised Enterprise Reference Architecture and Methodologies (GERAM) [ISO 15704] is
  > an architecture framework.
  >
  > EXAMPLE 2 Reference Model of Open Distributed Processing (RM-ODP) [ISO/IEC 10746] is an
  > architecture framework.
  >
  > 3.5 architecture view
  > work product expressing the architecture of a system from the perspective of specific system
  > concerns
  >
  > 3.6 architecture viewpoint
  > work product establishing the conventions for the construction, interpretation and use of
  > architecture views to frame specific system concerns
  >
  > 3.7 concern
  > interest in a system relevant to one or more of its stakeholders
  >
  > 3.8 environment
  > context determining the setting and circumstances of all influences upon a system
  >
  > 3.9 model kind
  > conventions for a type of modelling
  >
  > 3.10 stakeholder
  > individual, team, organization, or classes thereof, having an interest in a system

- SOURCE: ISO/IEC/IEEE 42010:2011(E), First edition 2011-12-01, *Systems and software engineering —
  Architecture description*, Clause 3 "Terms and definitions", 3.1-3.10, printed pages 1-2. The
  clause ends at 3.10: printed page 3 begins "4 Conceptual foundations / 4.1 Introduction".
- URL (actually read): https://www.sis.se/api/document/preview/914062/ (SIS official preview PDF,
  PDF pages 7-9 of 11; every page carries the footer "This preview is downloaded from www.sis.se.
  Buy the entire standard via https://www.sis.se/std-914062")
- FINDING for the two target strings: **neither "architecture domain" nor "domain architecture" is a
  defined term in 42010:2011 Clause 3.**

### 2.2 Contents — no entry for either string

- QUOTE (verbatim Contents entries, printed page iii), the complete list of headed clauses and annexes:

  > 1 Scope / 2 Conformance / 3 Terms and definitions / 4 Conceptual foundations / 4.1 Introduction /
  > 4.2 Conceptual model of architecture description / 4.3 Architecting in the life cycle / 4.4 Uses of
  > architecture descriptions / 4.5 Architecture frameworks and architecture description languages /
  > 5 Architecture descriptions / 5.1 Introduction / 5.2 Architecture description identification and
  > overview / 5.3 Identification of stakeholders and concerns / 5.4 Architecture viewpoints /
  > 5.5 Architecture views / 5.6 Architecture models / 5.7 Architecture relations / 5.8 Architecture
  > rationale / 6 Architecture frameworks and architecture description languages / 6.1 Architecture
  > frameworks / 6.2 Adherence of an architecture description to an architecture framework /
  > 6.3 Architecture description languages / 7 Architecture viewpoints / Annex A (informative) Notes on
  > terms and concepts / Annex B (informative) Guide to architecture viewpoints / Annex C (informative)
  > Relationship to other standards / Bibliography

- SOURCE: ISO/IEC/IEEE 42010:2011(E), Contents, printed page iii.
- URL: https://www.sis.se/api/document/preview/914062/ (PDF page 3 of 11)
- FINDING: no clause, annex or subclause title in 42010:2011 contains "architecture domain" or
  "domain architecture".

### 2.3 How 42010:2011 uses the bare word "domain" (every occurrence in the readable portion)

- QUOTE (Introduction, printed page v):
  > Architecture frameworks and architecture description languages are being created as assets that
  > codify the conventions and common practices of architecting and the description of architectures
  > within different communities and domains of application.
- QUOTE (4.2.1 Context of architecture description, printed page 3):
  > The term system is used in this International Standard to refer to entities whose architectures are
  > of interest. The term is intended to encompass, but is not limited to, entities within the following
  > domains:
- QUOTE (4.2.1, printed page 4):
  > This International Standard takes no position on what constitutes a system within those domains—or
  > elsewhere. The nature of systems is not defined by this International Standard.
- QUOTE (4.2.1, printed page 4):
  > This International Standard is intended for use in the domains of systems listed above; however,
  > nothing herein precludes its use for architecture descriptions of entities of interest outside of
  > those domains (for example, natural systems and conceptual systems).
- SOURCE: ISO/IEC/IEEE 42010:2011(E), Introduction and 4.2.1, printed pages v, 3 and 4.
- URL: https://www.sis.se/api/document/preview/914062/ (PDF pages 5, 9, 10 of 11)

### 2.4 Not verified for 42010:2011

The SIS preview ends inside 4.2.2 (printed page 5). Clauses 4.3-7, Annex A, Annex B and Annex C and the
Bibliography were **not read**, so I cannot assert that the strings are absent from those clauses; I can
only report that neither string appears in Clause 3 or in the Contents.

---

## 3. ISO/IEC/IEEE 42010:2022 — *Software, systems and enterprise — Architecture description*

### 3.1 Contents — no entry for either string

- QUOTE (verbatim Contents entries, printed pages 1-2): the complete list is

  > Foreword / Introduction / 1 Scope / 2 Normative references / 3 Terms and definitions /
  > 4 Conformance / 5 Conceptual foundations / 5.1 General / 5.2 Conceptual models of an architecture
  > description / 5.2.1 Context of architecture description / 5.2.2 Architectures and architecture
  > descriptions / 5.2.3 Stakeholders and concerns / 5.2.4 Stakeholder perspectives / 5.2.5 Aspects /
  > 5.2.6 Architecture considerations / 5.2.7 Architecture views and architecture viewpoints /
  > 5.2.8 Model kinds, legends and architecture view components / 5.2.9 Architecture description (AD)
  > elements / 5.2.10 View methods / 5.2.11 AD element correspondence / 5.2.12 Architecture decisions
  > and rationale / 5.3 Architecture description in the life cycle / 5.4 Architecture description
  > frameworks and languages / 5.4.1 General / 5.4.2 Architecture description frameworks /
  > 5.4.3 ADF utilization / 5.4.4 Architecture description languages / 6 Specification of an
  > architecture description / 6.1-6.10 / 7 Architecture description frameworks and architecture
  > description languages / 7.1-7.2 / 8 Architecture viewpoints and model kinds / 8.1-8.3 /
  > Annex A (informative) Notes on terms and concepts / Annex B (informative) Guidelines to
  > specification of architecture viewpoints / Annex C (informative) Relationship to other standards /
  > Annex D (informative) Uses of architecture descriptions / Annex E (informative) Architecture and
  > architecture description life cycles / Annex F (informative) Architecture description frameworks /
  > Bibliography / IEEE Notices and Abstract

- SOURCE: ISO/IEC/IEEE 42010:2022-11 (E), *Software, systems and enterprise - Architecture
  description*, Contents, printed pages 1-2.
- URL (actually read): https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:361506868/toc-3400447/download
- FINDING: no clause or annex title in 42010:2022 contains "architecture domain" or
  "domain architecture".

### 3.2 Clause 3 as far as the preview reaches (3.1 through 3.7)

- QUOTE (verbatim):

  > 3.1 architecting
  > conceiving, defining, expressing, documenting, communicating, certifying proper implementation of,
  > maintaining and improving an architecture (3.2) throughout the life cycle of an entity of interest
  > (3.12)
  >
  > 3.2 architecture
  > fundamental concepts or properties of an entity in its environment (3.13) and governing principles
  > for the realization and evolution of this entity and its related life cycle processes
  > [SOURCE: ISO/IEC/IEEE 42020:2019, 3.3, modified — The notes to entry have been removed.]
  >
  > 3.3 architecture description
  > AD
  > work product used to express an architecture (3.2)
  >
  > 3.4 architecture description element
  > AD element
  > identified or named part of an architecture description (3.3)
  >
  > 3.5 architecture description framework
  > ADF
  > conventions, principles and practices for the description of architectures (3.2) established within
  > a specific domain of application or community of stakeholders (3.17)
  > EXAMPLE Generalized Enterprise-Referencing Architectures Modelling Framework (GERAM)
  > (ISO 15704:2019, Annex B), Reference Model of Open Distributed Processing (RM-ODP),[2] Unified
  > Architecture Framework (UAF)[48], and NATO Architecture Framework (NAF)[44].
  >
  > 3.6 architecture description language
  > ADL
  > means of expression, with syntax and semantics, consisting of a set of representations, conventions,
  > and associated rules intended to be used to describe an architecture (3.2)
  >
  > 3.7 architecture view
  > information part (3.14) comprising portion of an architecture description (3.3)

- SOURCE: NEN-ISO/IEC/IEEE 42010:2022, ISO/IEC/IEEE 42010:2022(E), Clause 3 "Terms and definitions",
  3.1-3.7, printed pages 1-2. (Every page of the file carries the watermark/footer "Dit document is een
  voorbeeld van NEN / This document is a preview by NEN".)
- URL (actually read): https://www.nen.nl/en/norm/pdf/preview/document/304144/ (PDF pages 11-12 of 13)
- FINDING: **neither string is among 42010:2022's definitions 3.1-3.7.** The preview stops at 3.7, so
  3.8-3.19 were not read.

### 3.3 How 42010:2022 uses the bare word "domain"

- QUOTE (Clause 1 Scope, printed page 1):
  > This document specifies requirements for the structure and expression of an architecture
  > description (AD) for various entities, including software, systems, enterprises, systems of
  > systems, families of systems, products (goods or services), product lines, service lines,
  > technologies and business domains.
- QUOTE (Introduction, printed page vii):
  > Architecture description languages (ADL) are used to codify the description of architectures within
  > different communities and domains of application.
- SOURCE: NEN-ISO/IEC/IEEE 42010:2022 preview, Clause 1 and Introduction, printed pages 1 and vii.
- URL: https://www.nen.nl/en/norm/pdf/preview/document/304144/ (PDF pages 9, 11 of 13)
- Cross-reference of note: 42010:2022, 3.2 records that its definition of "architecture" is taken
  from **ISO/IEC/IEEE 42020:2019, 3.3** (quote in 3.2 above).

---

## 4. TOGAF (The Open Group) — the term "Architecture Domain" is defined

### 4.1 The definition entry

- QUOTE (verbatim, the complete entry):

  > Architecture Domain
  > The architectural area being considered. There are four architecture domains within TOGAF:
  > business, data, application, and technology.

- SOURCE: The Open Group Architecture Framework (TOGAF), chapter "Definitions" (breadcrumb: "You are
  here: TOGAF Online > Part I: Introduction > Definitions"), alphabetical entry "Architecture Domain".
  The chapter opens: "For the purposes of TOGAF 9, the following terms and definitions apply." The
  page footer reads: "This is an unapproved standards draft, subject to change. This material contains
  intellectual Property of Capgemini relating to the TOGAF fast track submission ... Unapproved Draft,
  Subject to Change".
- URL (actually read): https://www.opengroup.org/architecture/doc-review/protected-sanity/htmlclean/chap03.html
- Caveat: this is a **TOGAF 9 development draft** hosted on opengroup.org, not a published TOGAF
  Standard edition. The definition is verbatim as printed on that page.

### 4.2 The adjacent "Business Domain" entry (a "domain" that is not called an architecture)

- QUOTE (verbatim, the complete entry):
  > Business Domain
  > A grouping of coherent business functions and activities (in the context of a business sector) over
  > which meaningful responsibility can be taken. For example, Finance, Human Resources (HR),
  > Automobile Manufacturing, Retail, etc. The phrase is often used to identify specific business
  > knowledge (a business domain expert).
- SOURCE: same chapter as 4.1, entry "Business Domain".
- URL: https://www.opengroup.org/architecture/doc-review/protected-sanity/htmlclean/chap03.html
- The same chapter also contains the entry "Architecture Framework", whose first sentence is:
  > A foundational structure, or set of structures, which can be used for developing a broad range of
  > different architectures.

---

## 5. DoDAF 2.02

- FINDING: **NOT VERIFIED — zero verbatim DoDAF 2.02 text was obtained.** No quote, no section number
  and no glossary page could be read, so I can **neither confirm nor deny** that DoDAF 2.02 defines
  "architecture domain" or "domain architecture", and I have no verbatim sentence showing how DoDAF
  2.02 uses the word "domain".
- Every DoDAF-hosted or archived copy was blocked at the network layer, with these outcomes:
  - `https://dodcio.defense.gov/Portals/0/Documents/DODAF/DoDAF_v2-02_web.pdf` — HTTP 403
    (AkamaiGHost "Access Denied"); lowercase path variant — HTTP 403; the Library index page
    `https://dodcio.defense.gov/Library/DoD-Architecture-Framework/` — HTTP 403.
  - `https://www.acq.osd.mil/asda/dpc/ce/ds/docs/DODAF/DoDAF_v2-02_Volume_I.pdf` — DNS resolution
    failure; `https://apps.dtic.mil/sti/pdfs/AD1080114.pdf` — DNS resolution failure.
  - `http://www.shareetech.com/files/DoDAF v2.02 Chg 1 Vol II Final 2015-01-19.pdf` — HTTP 403.
  - `https://media.defense.gov`, `https://www.dau.edu`, `https://www.mitre.org`,
    `https://www.incose.org`, `https://ntrs.nasa.gov`, `https://calhoun.nps.edu`,
    `https://irp.fas.org/doddir/dod/dodaf.pdf` — 403 or connection failure.
  - `https://web.archive.org/...` and `https://archive.org` — connection failed (both curl and
    Python), consistent with the non-public-IP resolution seen for web.archive.org elsewhere in this
    research.
  - Text-extraction proxies (`r.jina.ai`, `api.allorigins.win`, `corsproxy.io`,
    `api.codetabs.com/v1/proxy`) — all failed (000 / 403 / 522).
  - GitHub code search for DoDAF PDFs — HTTP 401 (authentication required); the `adlnet/DoDAF`
    repository contained only `.zip`/`.vsdx` artifacts.
- DoDAF 2.02 hosted **by DoDAF itself** therefore remains unread. Hosts confirmed reachable from this
  environment but not searched before the time box expired: `dair.nps.edu`, `omg.org`, `github.com` /
  `raw.githubusercontent.com`, `gitee.com`, `gitcode.com`, `sebokwiki.org`.

---

## 6. UAF (OMG Unified Architecture Framework) and NAF v4

### 6.1 UAF does **not** call its set "domains" — it calls them **Viewpoints**

- QUOTE (verbatim, normative document landing page):

  > Part 1 (UAF DMM) provides a formal domain meta model (DMM) organized as a number of View
  > Specifications, which are organized within a two-dimensional grid consisting of rows representing
  > Viewpoints related to stakeholder concerns and columns representing Aspects of the architecture in
  > terms of different ways of viewing the architectural features. The Viewpoints include the following
  > Architecture Management, Summary and Overview, Strategic, Operational, Services, Personnel,
  > Resources, Security, Project, Standards, and Actual Resources.

- SOURCE: OMG *Unified Architecture Framework (UAF) Specification, Version 1.2*, page "About the
  Unified Architecture Framework Specification Version 1.2", prose section "UAF — Unified Architecture
  Framework". No printed clause number on this HTML page.
- URL (actually read): https://www.omg.org/spec/UAF/1.2/About-UAF
- FINDING: the enumerated items (Strategic, Operational, Services, Personnel, Resources, Security,
  Project, Standards, Actual Resources …) are introduced by UAF as **"Viewpoints"**, and the
  "domain" in the name is part of **"domain meta model (DMM)"**, not a label for the items.

- QUOTE (verbatim, same enumeration in the UAF 1.3 About page):

  > The Viewpoints include the following Architecture Management, Summary and Overview, Strategic,
  > Operational, Services, Personnel, Resources, Security, Project, Standards, and Actual Resources.

- SOURCE: OMG UAF Specification Version 1.3, About page (Document Status: formal; Publication Date:
  April 2026; normative documents "Specification - DMM = formal/25-10-01", "Specification - UAFML =
  formal/25-10-03").
- URL (actually read): https://www.omg.org/spec/UAF/

### 6.2 The printed clause names in the UAF 1.2 DMM

- QUOTE (verbatim, table of contents, clause 8):

  > 8. DOMAIN METAMODEL DIAGRAMS
  > 8.1 VIEW SPECIFICATIONS
  > 8.1.1 View Specifications::Architecture Management
  > 8.1.2 View Specifications::Summary & Overview
  > 8.1.3 View Specifications::Strategic
  > 8.1.4 View Specifications::Operational
  > 8.1.5 View Specifications::Services
  > 8.1.6 View Specifications::Personnel
  > 8.1.7 View Specifications::Resources
  > 8.1.8 View Specifications::Security
  > 8.1.9 View Specifications::Projects
  > 8.1.10 View Specifications::Standards
  > 8.1.11 View Specifications::Actual Resources
  > 8.1.12 View Specifications::Motivation
  > 8.1.13 View Specifications::Information
  > 8.1.14 View Specifications::Parameters
  > 8.1.15 View Specifications::Other

- QUOTE (verbatim, table of contents, clause 9):

  > 9. DOMAIN METAMODEL (DMM) ELEMENTS
  > 9.1 DOMAIN METAMODEL
  > 9.1.1 Domain MetaModel::Architecture Management
  > 9.1.2 Domain MetaModel::Summary & Overview
  > 9.1.3 Domain MetaModel::Strategic
  > 9.1.4 Domain MetaModel::Operational
  > 9.1.5 Domain MetaModel::Services
  > 9.1.6 Domain MetaModel::Personnel
  > 9.1.7 Domain MetaModel::Resources
  > 9.1.8 Domain MetaModel::Security
  > 9.1.9 Domain MetaModel::Projects
  > 9.1.10 Domain MetaModel::Standards
  > 9.1.11 Domain MetaModel::Actual Resources
  > 9.1.12 Domain MetaModel::Parameters

- SOURCE: *Unified Architecture Framework (UAF) Domain Metamodel, Version 1.2 – change bar version*,
  OMG Document Number **formal/22-07-04**, Table of Contents, printed pages I-II.
- URL (actually read): https://www.omg.org/cgi-bin/doc?formal/22-07-04.pdf
- PAGE: PDF pages 5-6 (printed TOC pages I-II)
- FINDING: the printed names are **"View Specifications::&lt;Name&gt;"** and
  **"Domain MetaModel::&lt;Name&gt;"**. UAF does **not** call them "specification domains", and it does
  not call them "architecture domains".

### 6.3 UAF's Terms and Definitions clause defines no new terms

- QUOTE (verbatim):

  > No new terms and definitions have been required to create this specification. All terms are
  > available in the normative references or bibliographic citations for detailed explanation. The
  > modeling concepts specified in this standard e.g., MetaModel Elements, Viewpoints, Aspects, View
  > Specifications, etc. are defined in the appropriate section for that concept. Additional terms are
  > defined in Appendix C: Enterprise Architecture Guide (EAG).

- SOURCE: UAF 1.2 DMM (formal/22-07-04), clause 4 "Terms and Definitions", printed page 9.
- URL: https://www.omg.org/cgi-bin/doc?formal/22-07-04.pdf
- PAGE: PDF page 25 (printed page 9)

### 6.4 Where UAF's word "Domain" comes from

- QUOTE (verbatim): "A Domain Metamodel (DMM) uses UML Class models to represent individuals, types
  and tuples that maps the concepts defined in DoDAF, MODEM, NAF, and other frameworks."
- SOURCE: UAF 1.2 DMM (formal/22-07-04), clause 6.3 "Philosophy", printed page 12. URL as above;
  PDF page 28.
- QUOTE (verbatim, clause 5 acronym table): "DMM — Domain Meta Model"
- SOURCE: UAF 1.2 DMM (formal/22-07-04), clause 5 "Acronyms", Table 5:1, printed page 10; PDF page 26.

### 6.5 Full-text search of UAF 1.2 DMM for the two target strings (run locally over the whole document)

- FINDING (verified by full-text regex over the complete extracted text of UAF 1.2 DMM
  change-bar version, formal/22-07-04, 271 PDF pages):
  - `"architecture domain"` — **0 occurrences**
  - `"domain architecture"` — **0 occurrences**
  - `"specification domain"` — **0 occurrences**
  - `"Strategic domain"` — **0 occurrences**
  - `"domain"` (any case) — 412 occurrences; the only occurrence of "the domains" in the DMM reads:
    > The information model is an aspect across the domains and can be defined in any of its forms,
    > i.e., Conceptual, Logical or Physical.
    (UAF 1.2 DMM, clause 7 "UAF Grid", printed pages 13-18; located by local full-text search of the
    file downloaded from https://www.omg.org/cgi-bin/doc?formal/22-07-04.pdf)
- Caveat: this negative result covers the UAF 1.2 **DMM** only. The UAF 1.2 **UAFML** part,
  UAF 1.1 and the UAF 1.3 normative PDFs were not searched, so a defined term "architecture domain"
  or "domain architecture" elsewhere in UAF is **not ruled out**.

### 6.6 An OMG issue that quotes UAF's definition of "architecture"

- QUOTE (verbatim, from the issue body):
  > p23 we have a definition of 'architecture':
  > 'Architecture – fundamental concepts and properties related to an entity in its environment and
  > governing principles for the realization and evolution of this entity and its related life cycle
  > processes [ISO/IEC/IEEE 42020:2019] (Note: This architecture entity can be an enterprise or system
  > or some other kind of thing. These fundamental concepts and properties can be about key entities
  > and relationships, along with associated behaviors, which are characterized in an architectural
  > description.)'
  >
  > 3) The source for the definition should be ISO/IEC/IEEE 42010 not ISO/IEC/IEEE 42020
- QUOTE (verbatim, issue metadata): "Key: UAF14-153 / OMG Task Force: Unified Architecture Framework
  (UAF) 1.4 RTF / Status: open / Source: Eclectica Systems Ltd (Nic Plum) / Reported: UAF 1.2 —
  Thu, 18 Apr 2024 07:51 GMT / Updated: Fri, 20 Dec 2024 14:57 GMT"
- SOURCE: OMG Issue Tracker, issue UAF14-153, task force "Unified Architecture Framework (UAF) 1.4
  RTF"; page title as printed: "UAF14 — Inconsistent Definition of 'Architecture'. Unintelligable
  Note. Incorrect Reference. Step Name Should be 'Define Architecture Description Drivers and
  Challenges'". The issue's own text cites UAF DMM pages "p22", "p23", "p25" and "p 131".
- URL (actually read): https://issues.omg.org/issues/UAF13-151 (this key redirects to
  https://issues.omg.org/browse/UAF14-153)
- Caveat: this is a third-party issue report, not UAF text. The UAF sentences it quotes were **not**
  read by me in the specification itself.

### 6.7 NAF v4 — NOT VERIFIED

- FINDING: **zero NAF quotes.** No page of NAF v4 / v4.1 was read, and `www.naf.org.pl` was not
  reached. The NAF v4.1 PDF download
  (https://www.nato.int/content/dam/nato/webready/documents/publications-and-reports/NATO-Architecture-Framework-v4-1-en.pdf)
  had not completed when the time box expired and was killed. I therefore cannot state how NAF v4 uses
  the word "domain", nor whether it defines "architecture domain" or "domain architecture".

---

## 7. Sources that explicitly define "domain architecture" as a term

### 7.1 Peer-reviewed journal article devoted to the term

- QUOTE (verbatim from the published abstract):
  > Enterprise architecture is concerned with the fundamental organization of the operating environment
  > of an enterprise. The enterprise architecture is used to plan and control the construction of the
  > systems that populate the operating environment. As the scope covered can be considerable in large
  > enterprises, introducing domain architectures to partition and detail the enterprise architecture is
  > a plausible approach. We formulate prescriptive criteria that consistent domain architectures must
  > meet. By integrating the creation of domain architectures into an extended strategic alignment model
  > we develop a theory that accounts for both the creation, scope-setting and detailing. Based on the
  > creation viewpoint we derive a multi-level classification taxonomy. The primary differentiator is
  > that between domains that are created from business usage viewpoints and those that are created from
  > solution construction viewpoints. Four cases of domain architectures from actual practice are
  > described that illustrate the variety encountered. Domain classifications in all cases conform to
  > the theoretical model. The criteria, the developed theory and the cases have both academic relevance
  > as well as significance for practitioners.
- SOURCE: Bruls, W. A., van Steenbergen, M., Foorthuis, R. M., Bos, R., & Brinkkemper, S. (2010).
  "Domain Architectures as an Instrument to Refine Enterprise Architecture." *Communications of the
  Association for Information Systems*, Vol. 27, Article 27. DOI 10.17705/1CAIS.02727. Abstract.
- URL (actually read): https://aisel.aisnet.org/cais/vol27/iss1/27/
- Caveat: I read the abstract; the full-text PDF
  (https://aisel.aisnet.org/cgi/viewcontent.cgi?article=3553&context=cais) returned HTTP 403
  (Cloudflare), so I could **not** verify any formal definition sentence inside the article body.

### 7.2 The 42020 Public Enquiry draft (draft standard, quoting an older IEEE standard)

The definition quoted in **1.3** above is itself a definition of the term "domain architecture",
attributed in the draft to IEEE Std 1517-1999 (R2004):

- QUOTE (verbatim):
  > A generic, organizational structure or design for systems in a domain.
  > [Based on IEEE Std 1517-1999 (R2004) IEEE Standard for Information Technology — Software Life Cycle
  > Processes — Reuse Processes, and modified by generalizing in terms of systems rather than software
  > systems]
- SOURCE: ISO/IEC/IEEE 42020 Public Enquiry draft (PDF metadata: "M315676 - Public Enquiry"), draft
  clause E.4.1.4 "Domain architecture", printed page 84. **Draft text.**
- URL: https://coe.qualiware.com/wp-content/uploads/2016/11/42020annexes.pdf (PDF page 27 of 61)
- I did **not** obtain IEEE Std 1517-1999 itself, so the attribution is reported as the draft prints
  it, not as independently confirmed.

---

## Could not verify

1. **ISO/IEC/IEEE 42020:2019 published body text, including E.4.1.5.** Paywalled. Failed access
   routes, all with the outcome shown:
   - https://www.iso.org/obp/ui/#iso:std:iso-iec-ieee:42020:ed-1:v1:en — HTTP 403 (Cloudflare
     "Just a moment..." interstitial; the OBP is a JavaScript application that a plain fetch cannot
     render even when reachable).
   - https://www.iso.org/standard/68982.html — HTTP 403.
   - https://webstore.ansi.org/preview-pages/BSI/preview_30329615.pdf — HTTP 403.
   - https://www.intertekinform.com/preview/825371132625.pdf — HTTP 403.
   - https://store.accuristech.com/atis/products/preview/2124134 — HTTP 403.
   - https://img.antpedia.com/.../ISO IEC IEEE 42020-2019.pdf — downloaded, but contains only the
     3-page cover (the site claims 126 pages; it serves a cover only).
   - https://www.din.de/.../toc-3094876/download — succeeded, but it is the **Contents only**
     (quoted in 1.1); it contains no clause body text.
   - IEEE Xplore holds P42020/V1.9 (Aug 2018) and P42020 FDIS (Mar 2019) drafts but they are
     paywalled.
   **Consequently: the published E.4.1.5 sentence(s) are NOT verified, and whether published 42020
   Clause 3 defines "architecture domain" is NOT verified.** The closest verified material is the
   2017 Public Enquiry draft in 1.3, which must be labelled draft text.
2. **ISO/IEC/IEEE 42020 Clause 3 definition list** — not readable; only indirect evidence exists
   (42010:2022, 3.2 cites "ISO/IEC/IEEE 42020:2019, 3.3" for "architecture", so Clause 3 exists and
   contains at least 3.3).
3. **ISO/IEC/IEEE 42010:2011 full text beyond printed page 5** — the SIS preview ends inside 4.2.2.
   Clauses 4.3-7, Annex A, Annex B, Annex C and the Bibliography were not read, so absence of the
   two target strings is verified only for the Contents and Clause 3.
4. **ISO/IEC/IEEE 42010:2022 definitions 3.8-3.19** — the NEN preview stops at 3.7.
5. **The official ISO/IEC/IEEE 42010 web site (iso-architecture.org), including its FAQ and its copy
   of the 42010 FDIS draft** — the domain no longer resolves (DNS returns SOA only, no A record) and
   a direct HTTP request fails with a connection error. `web.archive.org` and `arquivo.pt` are both
   unreachable from this environment (the former resolves to a non-public IP and is refused).
6. **TOGAF published editions (9.1, 9.2, 10th edition)** — not read. The TOGAF Standard 10th edition
   public HTML at https://pubs.opengroup.org/togaf-standard/ returned HTTP 401 Unauthorized. The
   "Architecture Domain" definition quoted in 4.1 is from the publicly reachable unapproved TOGAF 9
   development draft at the URL given.
7. **DoDAF 2.02 — nothing.** No DoDAF 2.02 text was readable at all (see section 5 for the full list of
   403/000/DNS failures, including the official `dodcio.defense.gov` volumes). Whether DoDAF 2.02
   defines or uses either target string is **neither confirmed nor denied**.
8. **UAF beyond the 1.2 DMM.** The UAF 1.2 **UAFML** part (formal/22-07-05), UAF 1.1, the UAF 1.3
   normative PDFs and the OMG XMI files were not searched, so the absence of "architecture domain" /
   "domain architecture" in UAF is verified only for the UAF 1.2 DMM.
   `https://www.omg.org/spec/UAF/1.2/PDF` returned HTTP 404 on direct fetch.
9. **UAF 1.2 DMM clause 7 "UAF Grid" (printed pages 13-18)** was not read as prose; only its single
   "the domains" sentence was located by local full-text search.
10. **NAF v4 / v4.1 — nothing.** Zero pages read; `www.naf.org.pl` never reached; the NATO PDF download
    was killed at the time box.
11. **The full text of the CAIS 2010 article** — abstract only; the PDF endpoint returned HTTP 403.
12. **IEEE Std 1517-1999 (R2004)** — not obtained; its wording is reported only as the 42020 Public
    Enquiry draft prints the attribution.
13. **Search engines were of limited use for the target strings.** Bing (cn.bing.com) returned
    suppressed/irrelevant results; Mojeek returned HTTP 403; DuckDuckGo HTML failed to fetch. No
    indexed snippet was found that contains the published 42020 E.4.1.5 text.
14. **Environment-wide access limits encountered.** `web.archive.org` resolves to a non-public IP and is
    refused; `arquivo.pt` fails; `iso-architecture.org` no longer resolves (DNS returns SOA only, no A
    record) so the official 42010 site, its FAQ and its hosted 42010 FDIS draft were all unreachable;
    `ri.ufs.br` timed out; `r.jina.ai` resolves to a non-public IP. Various Cloudflare-protected
    standards resellers (ANSI, BSI, Intertek Inform, Accuris, ISO itself) returned HTTP 403 to every
    method tried.

## Status summary of the six requested investigations

| # | Target | Status |
|---|---|---|
| 1 | ISO/IEC/IEEE 42020:2019 — E.4.1.5 exists; "domain architecture" used | **Partly verified.** E.4.1.5 titled "Domain architecture" verified from the official Contents. Body text **not** verified (paywalled); closest text is a 2017 Public Enquiry draft (labelled as draft). "architecture domain": zero occurrences in that draft; published Clause 3 **not** readable. |
| 2 | ISO/IEC/IEEE 42010:2011 | **Verified for Contents and Clause 3.1-3.10:** no "architecture domain", no "domain architecture". Rest of the document **not** read. |
| 3 | ISO/IEC/IEEE 42010:2022 | **Verified for Contents and Clause 3.1-3.7:** no "architecture domain", no "domain architecture". 3.8-3.19 **not** read. |
| 4 | TOGAF "Architecture Domain" | **Verified** verbatim, from the publicly reachable TOGAF 9 unapproved development draft. Published TOGAF editions **not** read (401). |
| 5 | DoDAF 2.02 | **Not verified** — no text accessible. |
| 6 | UAF | **Partly verified.** Enumeration verified and it is labelled "Viewpoints"; clauses and full-text negatives for the DMM verified. UAFML / 1.1 / 1.3 **not** searched. |
| 7 | NAF v4 | **Not verified** — no text accessible. |
| 8 | Authoritative definition of "domain architecture" | **Partly verified.** 42020 Public Enquiry draft definition (draft text) and a peer-reviewed article abstract. Full journal article **not** read (403). |
