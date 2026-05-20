# 产品A（AOS 运营体系）— 阶段1：系统设计
**Product A (AOS Enterprise Operation System) — Phase 1: System Design**

**文档版本**：v1.0
**最后更新**：2026-05-20

---

## 目录用途

本目录是产品A（AOS 企业运营体系）阶段1（系统设计）的完整工作空间，包含 AOS 系统设计所需的设计准则、设计指南、AI 辅助文档和任务定义。

---

## 目录结构

```
10-aos-system-design/
├── 01-aos-system-design-standards/           # AOS 系统设计准则（产品B构件）
├── 02-aos-system-design-guidelines/          # AOS 设计指南（产品B构件）
├── 03-aos-system-design-ai-support/          # AOS AI 辅助文档（产品B构件）
├── 04-aos-system-design-tasks/               # AOS 任务定义（产品B构件）
└── 10-aos-system-product-data/               # AOS 产品数据（产品A设计输出）
```

---

## 各子目录说明

### [01-aos-system-design-standards/](01-aos-system-design-standards/README.md)
**AOS 系统设计准则 — 产品B构件**

| 文档 | 说明 |
|------|------|
| 01-aos-system-design-standards.md | 核心准则：5层结构、3条规则、多产品设计关系 |
| 02 ~ 06 | 各层规范（OR/SR/BA/SysReq/PA） |
| 07-aos-system-design-terminology-glossary.md | 术语对照表 |

### [02-aos-system-design-guidelines/](02-aos-system-design-guidelines/README.md)
**AOS 四种场景设计指南 — 产品B构件**

| 文档 | 适用场景 | 周期 |
|------|---------|------|
| 01-waterfall-aos-system-design-guide.md | 全新 AOS 系统，需求明确 | 30-48天 |
| 03-agile-aos-system-design-guide.md | AOS 迭代开发，需求渐进 | 13-21天 |
| 02-reverse-engineering-aos-system-design-guide.md | 已有 AOS 系统补文档 | 16-26天 |
| 04-devops-aos-system-design-guide.md | AOS 小变更快速交付 | 几小时-3天 |
| 05-aos-system-quick-reference-card.md | 快速参考 | — |

### [03-aos-system-design-ai-support/](03-aos-system-design-ai-support/README.md)
**AOS AI 辅助文档 — 产品B构件**

为团队A开展 AOS 系统设计提供 AI 辅助支持，包含决策框架、产品上下文、各场景提示词模板和检查清单。

### [04-aos-system-design-tasks/](04-aos-system-design-tasks/README.md)
**AOS 任务定义 — 产品B构件**

按四种场景组织的操作规程文档（共 26 个任务文档），AI 和 AOS 设计人员按任务定义执行系统设计操作。

### [10-aos-system-product-data/](10-aos-system-product-data/README.md)
**AOS 产品数据 — 产品A设计输出**

团队A使用产品B工具产出的 AOS 设计内容，按五层结构组织，包含从原始需求到产品架构的完整产品数据。

---

## 两层产品关系

| 类型 | 目录 | 说明 |
|------|------|------|
| 产品B构件（工具） | 01-standards、02-guidelines、03-ai-support、04-tasks | 团队B交付给团队A的设计工具和规范 |
| 产品A设计输出 | 10-product-data | 团队A使用工具产出的 AOS 设计内容 |

---

**文档版本**：v1.0
**最后更新**：2026-05-20
