# EOS 运营体系 — 产品数据
**EOS Enterprise Operation System — Product Data**

**版本**：v1.0
**最后更新**：2026-05-20

---

## 目录用途

本目录包含 EOS 企业运营体系的 9 份产品数据文档，按系统设计准则的五层结构和开发六步法组织。这些文档是**EOS的设计输出**，由团队M使用设计线的设计工具产出。

---

## 产品数据清单

| 编号 | 文档名称 | 对应层级 | 对应步骤 | 状态 |
|------|---------|---------|---------|------|
| 01 | [原始需求详细定义](01-eos-original-requirements.md) | 第 1 层 | 第 1 步 | 待填充 |
| 02 | [相关方需求架构定义](02-eos-stakeholder-requirements-architecture.md) | 第 2 层（架构定义） | 第 1 步 | 待填充 |
| 03 | [相关方需求详细定义](03-eos-stakeholder-requirements-detailed.md) | 第 2 层（详细定义） | 第 2 步 | 待填充 |
| 04 | [业务架构定义](04-eos-business-architecture.md) | 第 3 层 | 第 2 步 | 待填充 |
| 05 | [系统需求架构定义](05-eos-system-requirements-architecture.md) | 第 4 层（架构定义） | 第 3-4 步 | 待填充 |
| 06 | [系统需求详细定义](06-eos-system-requirements-detailed.md) | 第 4 层（详细定义） | 第 5 步 | 待填充 |
| 07 | [产品架构定义](07-eos-product-architecture.md) | 第 5 层 | 第 5 步 | 待填充 |
| 08 | [追溯矩阵](08-eos-system-design-traceability-matrix.md) | 全层 | 第 6 步 | 待填充 |
| 09 | [验证报告](09-eos-system-design-verification-report.md) | 全层 | 第 6 步 | 待填充 |
| 21 | [输出产品架构目录](21-eos-output-architecture.md) | 全层（跨层资产） | ort03/wft01/wft02 | 活跃 |

> **说明**：当前所有文档为**空模板占位符**，等待团队M根据 EOS 实际业务需求填充设计内容。

---

## 五层结构与文档对应

```
第1层：原始需求 (OR)         → 01-eos-original-requirements.md
    ↓ N:1 分配
第2层：相关方需求 (SR)       → 02-eos-...-architecture.md + 03-eos-...-detailed.md
    ├─ 功能部分 ↓
    │   第3层：业务架构 (BA)  → 04-eos-business-architecture.md
    │       ↓
    │   第4层：系统需求 (SysReq) → 05-eos-...-architecture.md + 06-eos-...-detailed.md
    │       ↓
    │   第5层：产品架构 (PA)  → 07-eos-product-architecture.md
    │
    └─ 非功能部分 ↓
        第4层：SysReq-NFR    → 05-eos-...-architecture.md（非功能部分）
            ↓
        第5层：PA            → 07-eos-product-architecture.md（非功能约束）

追溯矩阵                    → 08-eos-system-design-traceability-matrix.md
验证报告                    → 09-eos-system-design-verification-report.md
```

---

## 使用指引

1. **使用场景**：选择适合当前任务的开发场景（瀑布式/敏捷式/逆向工程/DevOps）
2. **参考规范**：各层规范参见 [10-eos-system-design-specification/](../10-eos-system-design-specification/README.md)
3. **操作步骤**：按对应场景指南的步骤填充产品数据文档
4. **AI 辅助**：使用 [30-eos-system-design-ai-support/](../30-eos-system-design-ai-support/README.md) 的提示词模板自动生成

---

**版本**：v1.0
**最后更新**：2026-05-20
