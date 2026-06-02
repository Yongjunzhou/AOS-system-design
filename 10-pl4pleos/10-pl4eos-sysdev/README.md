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
10-pl4eos-sysdev/
├── 10-pl4eos-sysdev-spec/           # 设计准则（通用方法论 + 元流水线专有）
├── 20-pl4eos-sysdev-tasks/          # 四种场景的操作规程（任务定义）
└── 90-pl4eos-system-product-data/   # 流水线的标准产品数据
```

---

## 各子目录说明

### [10-pl4eos-sysdev-spec/](10-pl4eos-sysdev-spec/README.md)
**设计准则 — 通用方法论 + 元流水线专有**

| 文档 | 说明 |
|------|------|
| 01-pl4eos-sysdev-spec.md | 核心准则：5层结构、3条规则、质量指标 |
| 04-pl4eos-terminology-glossary.md | 术语英文对照表 |

### [20-pl4eos-sysdev-tasks/](20-pl4eos-sysdev-tasks/README.md)
**四种场景的操作规程**

### [90-pl4eos-system-product-data/](90-pl4eos-system-product-data/README.md)
**流水线的标准产品数据 — 9 份文档**

按五层结构组织的完整产品数据，详见该目录的 README。

---

## 通用 vs 专用

| 类型 | 目录 | 说明 |
|------|------|------|
| 通用（参考） | 10-pl4eos-sysdev-spec | 定义方法论，设计线和 EOS 参考共用 |
| 设计线 专用 | 20-pl4eos-sysdev-tasks、90-pl4eos-system-product-data | 仅用于流水线产品本身的设计 |

---

**文档版本**：v1.0  
**最后更新**：2026-05-17
