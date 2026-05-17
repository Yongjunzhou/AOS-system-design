# 系统设计流水线 — 产品数据
**System Design Pipeline — Product Data**

**目录用途**：包含流水线产品的 9 份产品数据文档及 AI Skill 定义，按系统设计准则的开发六步法和五层结构组织。

---

## 产品数据清单

| 编号 | 文档名称 | 对应层级 | 对应步骤 | 版本 | 状态 |
|------|---------|---------|---------|------|------|
| 01 | [原始需求详细定义](01-original-requirements.md) | 第 1 层 | 第 1 步 | v4.0 | 已完成 |
| 02 | [相关方需求架构定义](02-stakeholder-requirements-architecture.md) | 第 2 层（架构定义） | 第 1 步 | v2.0 | 已完成 |
| 03 | [相关方需求详细定义](03-stakeholder-requirements-detailed.md) | 第 2 层（详细定义） | 第 2 步 | v2.0 | 已完成 |
| 04 | [业务架构定义](04-business-architecture.md) | 第 3 层 | 第 2 步 | v1.0 | 待设计 |
| 05 | [系统需求架构定义](05-system-requirements-architecture.md) | 第 4 层（架构定义） | 第 3-4 步 | v2.0 | 已完成 |
| 06 | [系统需求详细定义](06-system-requirements-detailed.md) | 第 4 层（详细定义） | 第 5 步 | v2.0 | 已完成 |
| 07 | [产品架构定义](07-product-architecture.md) | 第 5 层 | 第 5 步 | v2.0 | 已完成 |
| 08 | [追溯矩阵](08-traceability-matrix.md) | 全层 | 第 6 步 | v2.0 | 已完成 |
| 09 | [验证报告](09-verification-report.md) | 全层 | 第 6 步 | v2.0 | 已完成 |

**补充文档**：
- 10-ai-skills/（AI Skill 定义，11 个文件，待迁移）

---

## 五层结构与文档对应

```
第1层：原始需求 (OR)         → 01-original-requirements.md
    ↓ N:1 分配
第2层：相关方需求 (SR)       → 02-...-architecture.md + 03-...-detailed.md
    ├─ 功能部分 ↓
    │   第3层：业务架构 (BA)  → 04-business-architecture.md（待设计）
    │       ↓
    │   第4层：系统需求 (SysReq) → 05-...-architecture.md + 06-...-detailed.md
    │       ↓
    │   第5层：产品架构 (PA)  → 07-product-architecture.md
    │
    └─ 非功能部分 ↓
        第4层：SysReq-NFR    → 05-...-architecture.md（非功能部分）
            ↓
        第5层：PA            → 07-product-architecture.md（非功能约束）

追溯矩阵                    → 08-traceability-matrix.md
验证报告                    → 09-verification-report.md
```

## 统计数据

| 层级 | 名称 | 架构末级数 | 详细末级数 |
|------|------|----------|----------|
| 1 | 原始需求 | — | 92 |
| 2 | 相关方需求 | 29（21F + 8NF） | 91（74F + 17NF） |
| 3 | 业务架构 | 待设计 | — |
| 4 | 系统需求 | 30（13F + 17NFR） | 85（功能 9级活动） |
| 5 | 产品架构 | 85 | — |

---

**版本**：v2.0  
**最后更新**：2026-05-17
