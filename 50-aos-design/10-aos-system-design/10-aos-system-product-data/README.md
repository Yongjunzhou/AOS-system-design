# AOS 运营体系 — 产品数据
**AOS Enterprise Operation System — Product Data**

**版本**：v1.0
**最后更新**：2026-05-20

---

## 目录用途

本目录包含 AOS 企业运营体系的 9 份产品数据文档，按系统设计准则的五层结构和开发六步法组织。这些文档是**产品M（AOS）的设计输出**，由团队M使用产品L的设计工具产出。

---

## 产品数据清单

| 编号 | 文档名称 | 对应层级 | 对应步骤 | 状态 |
|------|---------|---------|---------|------|
| 01 | [原始需求详细定义](01-aos-original-requirements.md) | 第 1 层 | 第 1 步 | 待填充 |
| 02 | [相关方需求架构定义](02-aos-stakeholder-requirements-architecture.md) | 第 2 层（架构定义） | 第 1 步 | 待填充 |
| 03 | [相关方需求详细定义](03-aos-stakeholder-requirements-detailed.md) | 第 2 层（详细定义） | 第 2 步 | 待填充 |
| 04 | [业务架构定义](04-aos-business-architecture.md) | 第 3 层 | 第 2 步 | 待填充 |
| 05 | [系统需求架构定义](05-aos-system-requirements-architecture.md) | 第 4 层（架构定义） | 第 3-4 步 | 待填充 |
| 06 | [系统需求详细定义](06-aos-system-requirements-detailed.md) | 第 4 层（详细定义） | 第 5 步 | 待填充 |
| 07 | [产品架构定义](07-aos-product-architecture.md) | 第 5 层 | 第 5 步 | 待填充 |
| 08 | [追溯矩阵](08-aos-system-design-traceability-matrix.md) | 全层 | 第 6 步 | 待填充 |
| 09 | [验证报告](09-aos-system-design-verification-report.md) | 全层 | 第 6 步 | 待填充 |

> **说明**：当前所有文档为**空模板占位符**，等待团队M根据 AOS 实际业务需求填充设计内容。

---

## 五层结构与文档对应

```
第1层：原始需求 (OR)         → 01-aos-original-requirements.md
    ↓ N:1 分配
第2层：相关方需求 (SR)       → 02-aos-...-architecture.md + 03-aos-...-detailed.md
    ├─ 功能部分 ↓
    │   第3层：业务架构 (BA)  → 04-aos-business-architecture.md
    │       ↓
    │   第4层：系统需求 (SysReq) → 05-aos-...-architecture.md + 06-aos-...-detailed.md
    │       ↓
    │   第5层：产品架构 (PA)  → 07-aos-product-architecture.md
    │
    └─ 非功能部分 ↓
        第4层：SysReq-NFR    → 05-aos-...-architecture.md（非功能部分）
            ↓
        第5层：PA            → 07-aos-product-architecture.md（非功能约束）

追溯矩阵                    → 08-aos-system-design-traceability-matrix.md
验证报告                    → 09-aos-system-design-verification-report.md
```

---

## 使用指引

1. **使用场景**：选择适合当前任务的开发场景（瀑布式/敏捷式/逆向工程/DevOps）
2. **参考规范**：各层规范参见 [01-aos-system-design-standards/](../01-aos-system-design-standards/README.md)
3. **操作步骤**：按对应场景指南的步骤填充产品数据文档
4. **AI 辅助**：使用 [03-aos-system-design-ai-support/](../03-aos-system-design-ai-support/README.md) 的提示词模板自动生成

---

**版本**：v1.0
**最后更新**：2026-05-20
