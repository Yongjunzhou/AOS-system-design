# EOS（企业运营体系）— 阶段1：系统设计
**Product A (EOS Enterprise Operation System) — Phase 1: System Design**

**文档版本**：v1.0
**最后更新**：2026-05-20

---

## 目录用途

本目录是EOS（企业运营体系）阶段1（系统设计）的完整工作空间，包含 EOS 系统设计所需的设计准则、设计指南、AI 辅助文档和任务定义。

---

## 目录结构

```
10-eos-system-design/
├── 10-eos-system-design-specification/           # EOS 系统设计准则（设计线构件）
├── 20-eos-system-design-tasks/               # EOS 任务定义（设计线构件）
├── 30-eos-system-design-ai-support/          # EOS AI 辅助文档（设计线构件）
└── 90-eos-system-product-data/               # EOS 产品数据（EOS设计输出）
```

---

## 各子目录说明

### [10-eos-system-design-specification/](10-eos-system-design-specification/README.md)
**EOS 系统设计准则 — 设计线构件**

| 文档 | 说明 |
|------|------|
| 01-eos-system-design-standards.md | 核心准则：5层结构、3条规则、多产品设计关系 |
| 04-eos-system-design-terminology-glossary.md | 术语对照表 |

### [20-eos-system-design-tasks/](20-eos-system-design-tasks/README.md)
**EOS 任务定义 — 设计线构件**

按四种场景组织的操作规程文档（共 26 个任务文档），AI 和 EOS 设计人员按任务定义执行系统设计操作。

### [30-eos-system-design-ai-support/](30-eos-system-design-ai-support/README.md)
**EOS AI 辅助文档 — 设计线构件**

为团队M开展 EOS 系统设计提供 AI 辅助支持，包含决策框架、产品上下文、各场景提示词模板和检查清单。

### [90-eos-system-product-data/](90-eos-system-product-data/README.md)
**EOS 产品数据 — EOS设计输出**

团队M使用设计线工具产出的 EOS 设计内容，按五层结构组织，包含从原始需求到产品架构的完整产品数据。

---

## 两层产品关系与三层工作层面

**两层产品关系**（设计线是工具、EOS是目标系统）、**三层工作层面**（流水线设计 → 交付物构建 → 使用工具设计目标系统）和**内嵌关系**（运营体系包含设计自身的规则和工具）是同一客观事实的三个互补视角。

| 视角 | 焦点 | 说明 |
|------|------|------|
| **两层产品关系**（静态） | "谁是什么" | 设计线是设计工具，EOS是被设计的系统 |
| **三层工作层面**（动态） | "谁在做什么" | 团队L负责第1层流水线设计和第2层交付物构建，团队M负责第3层系统设计 |
| **内嵌关系**（递归） | "谁包含谁" | 运营体系包含设计自身的规则和工具——设计线是支撑"设计运营体系本身"这项业务的工具 |

> **推论**：开发设计线所用的准则、规范、流程自然地适用于开发整个运营体系，因为运营体系的设计本身就是运营体系包含的一项业务。

### 三层工作面对应到本目录

| 层面 | 工作内容 | 负责方 | 对应目录 |
|------|---------|--------|---------|
| **第1层：流水线设计** | 设计线用通用方法论对自身进行系统设计 | 团队L | `10-eos-pipeline-design/` |
| **第2层：交付物构建** | 将设计线的准则/指南/AI辅助/任务适配为EOS的设计工具 | 团队L | 01-standards、02-guidelines、03-ai-support、04-tasks |
| **第3层：使用工具设计EOS** | 使用第2层工具，对运营体系进行系统设计 | 团队M | 10-product-data |

---

**文档版本**：v1.0
**最后更新**：2026-05-20
