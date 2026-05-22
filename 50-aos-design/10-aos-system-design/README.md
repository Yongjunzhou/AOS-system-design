# 产品M（AOS 运营体系）— 阶段1：系统设计
**Product A (AOS Enterprise Operation System) — Phase 1: System Design**

**文档版本**：v1.0
**最后更新**：2026-05-20

---

## 目录用途

本目录是产品M（AOS 企业运营体系）阶段1（系统设计）的完整工作空间，包含 AOS 系统设计所需的设计准则、设计指南、AI 辅助文档和任务定义。

---

## 目录结构

```
10-aos-system-design/
├── 01-aos-system-design-standards/           # AOS 系统设计准则（产品L构件）
├── 02-aos-system-design-guidelines/          # AOS 设计指南（产品L构件）
├── 03-aos-system-design-ai-support/          # AOS AI 辅助文档（产品L构件）
├── 04-aos-system-design-tasks/               # AOS 任务定义（产品L构件）
└── 10-aos-system-product-data/               # AOS 产品数据（产品M设计输出）
```

---

## 各子目录说明

### [01-aos-system-design-standards/](01-aos-system-design-standards/README.md)
**AOS 系统设计准则 — 产品L构件**

| 文档 | 说明 |
|------|------|
| 01-aos-system-design-standards.md | 核心准则：5层结构、3条规则、多产品设计关系 |
| 02 ~ 06 | 各层规范（OR/SR/BA/SysReq/PA） |
| 07-aos-system-design-terminology-glossary.md | 术语对照表 |

### [02-aos-system-design-guidelines/](02-aos-system-design-guidelines/README.md)
**AOS 四种场景设计指南 — 产品L构件**

| 文档 | 适用场景 | 周期 |
|------|---------|------|
| 01-waterfall-aos-system-design-guide.md | 全新 AOS 系统，需求明确 | 30-48天 |
| 03-agile-aos-system-design-guide.md | AOS 迭代开发，需求渐进 | 13-21天 |
| 02-reverse-engineering-aos-system-design-guide.md | 已有 AOS 系统补文档 | 16-26天 |
| 04-devops-aos-system-design-guide.md | AOS 小变更快速交付 | 几小时-3天 |
| 05-aos-system-quick-reference-card.md | 快速参考 | — |

### [03-aos-system-design-ai-support/](03-aos-system-design-ai-support/README.md)
**AOS AI 辅助文档 — 产品L构件**

为团队M开展 AOS 系统设计提供 AI 辅助支持，包含决策框架、产品上下文、各场景提示词模板和检查清单。

### [04-aos-system-design-tasks/](04-aos-system-design-tasks/README.md)
**AOS 任务定义 — 产品L构件**

按四种场景组织的操作规程文档（共 26 个任务文档），AI 和 AOS 设计人员按任务定义执行系统设计操作。

### [10-aos-system-product-data/](10-aos-system-product-data/README.md)
**AOS 产品数据 — 产品M设计输出**

团队M使用产品L工具产出的 AOS 设计内容，按五层结构组织，包含从原始需求到产品架构的完整产品数据。

---

## 两层产品关系与三层工作层面

**两层产品关系**（产品L是工具、产品M是目标系统）、**三层工作层面**（自指设计 → 交付物构建 → 使用工具设计目标系统）和**自指关系**（运营体系包含设计自身的规则和工具）是同一客观事实的三个互补视角。

| 视角 | 焦点 | 说明 |
|------|------|------|
| **两层产品关系**（静态） | "谁是什么" | 产品L是设计工具，产品M是被设计的系统 |
| **三层工作层面**（动态） | "谁在做什么" | 团队L负责第1层自指设计和第2层交付物构建，团队M负责第3层系统设计 |
| **自指关系**（递归） | "谁包含谁" | 运营体系包含设计自身的规则和工具——产品L是支撑"设计运营体系本身"这项业务的工具 |

> **推论**：开发产品L所用的准则、规范、流程自然地适用于开发整个运营体系，因为运营体系的设计本身就是运营体系包含的一项业务。

### 三层工作面对应到本目录

| 层面 | 工作内容 | 负责方 | 对应目录 |
|------|---------|--------|---------|
| **第1层：自指设计** | 团队L用五层结构对产品L进行系统设计 | 团队L | `10-pipeline-design/` |
| **第2层：交付物构建** | 将产品L的准则/指南/AI辅助/任务适配为产品M的设计工具 | 团队L | 01-standards、02-guidelines、03-ai-support、04-tasks |
| **第3层：使用工具设计产品M** | 使用第2层工具，对运营体系进行系统设计 | 团队M | 10-product-data |

---

**文档版本**：v1.0
**最后更新**：2026-05-20
