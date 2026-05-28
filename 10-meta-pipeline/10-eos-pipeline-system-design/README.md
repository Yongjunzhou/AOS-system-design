# 系统设计流水线 — 阶段1：系统设计
**System Design Pipeline — Phase 1: System Design**

**文档版本**：v1.0  
**最后更新**：2026-05-17

---

## 目录用途

本目录是设计线（系统设计流水线）阶段1（系统设计）的完整工作空间，包含通用设计方法论、AI 辅助文档和流水线自身的产品数据。

---

## 目录结构

```
10-eos-pipeline-system-design/
├── 01-eos-pipeline-system-design-specification/     # 通用设计准则（两个项目参考）
├── 02-eos-pipeline-system-design-guidelines/    # 四种场景的设计指南（共享）
├── 03-eos-pipeline-system-design-ai-support/    # 流水线产品的 AI 辅助文档
└── 10-eos-pipeline-system-product-data/         # 流水线的标准产品数据
```

---

## 各子目录说明

### [01-eos-pipeline-system-design-specification/](01-eos-pipeline-system-design-specification/README.md)
**通用设计准则 — 两个项目参考**

| 文档 | 说明 |
|------|------|
| 01-eos-pipeline-system-design-standards.md | 核心准则：5层结构、3条规则、质量指标 |
| 04-eos-pipeline-terminology-glossary.md | 术语英文对照表 |

### [02-eos-pipeline-system-design-guidelines/](02-eos-pipeline-system-design-guidelines/README.md)
**四种场景的设计指南 — 两个项目参考**

| 文档 | 适用场景 | 周期 |
|------|---------|------|
| 01-waterfall-eos-pipeline-system-design-guide.md | 全新系统，需求明确 | 30-48天 |
| 03-agile-eos-pipeline-system-design-guide.md | 迭代开发，需求渐进 | 13-21天 |
| 02-reverse-engineering-eos-pipeline-system-design-guide.md | 已有系统补文档 | 16-26天 |
| 04-devops-eos-pipeline-system-design-guide.md | 小变更快速交付 | 几小时-3天 |
| 05-eos-pipeline-system-quick-reference-card.md | 快速参考 | — |

### [03-eos-pipeline-system-design-ai-support/](03-eos-pipeline-system-design-ai-support/)
**流水线产品的 AI 辅助文档**

| 子目录/文件 | 说明 |
|------------|------|
| 00-ai-document-requirements-understanding.md | AI 文档理解要求 |
| 01-eos-pipeline-system-design-waterfall/ | 瀑布式场景：README + checklist + example + prompts |
| 02-eos-pipeline-system-design-agile/ | 敏捷式场景：同上 |
| 03-eos-pipeline-system-design-reverse-engineering/ | 逆向工程场景：同上 |
| 04-eos-pipeline-system-design-devops/ | DevOps 场景：同上 |

### [10-eos-pipeline-system-product-data/](10-eos-pipeline-system-product-data/README.md)
**流水线的标准产品数据 — 9 份文档**

按五层结构组织的完整产品数据，详见该目录的 README。

---

## 通用 vs 专用

| 类型 | 目录 | 说明 |
|------|------|------|
| 通用（参考） | 01-standards、02-guidelines | 定义方法论，设计线 和EOS 参考共用 |
| 设计线 专用 | 03-ai-support、10-product-data | 仅用于流水线产品本身的设计 |

---

**文档版本**：v1.0  
**最后更新**：2026-05-17
