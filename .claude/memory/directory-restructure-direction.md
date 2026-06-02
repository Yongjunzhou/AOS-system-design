---
name: directory-restructure-direction
description: 2026-06-02 确定一级目录结构调整方案：00-generalspec/10-meta-pipeline/20-pipeline4eos/30-eos
metadata:
  type: project
---

## 决策：一级目录结构调整

2026-06-02 上午讨论，基于产品分类框架（product-classification-framework）调整一级目录结构。

### 新的一级目录

| 编号 | 目录名 | 内容 | 对应旧路径 |
|------|--------|------|-----------|
| `00` | `generalspec` | 通用设计规范 | `00-general/` |
| `10` | `meta-pipeline` | 元流水线产品（AI Skill 形态） | `10-eos-pipeline-design/` |
| `20` | `pipeline4eos` | EOS 流水线产品（AI Skill 形态），含其设计子线的准则/任务/产品数据 | `20-eos-design/10-eos-system-design/` |
| `30` | `eos` | EOS 产品本体（软件形态），仅装产品实现层内容 | `30-eos/` |

### 已决定的事项

- 产品数据（9 份标准文档）**随流水线走**（选项 A），EOS 流水线的产品数据放在 `20-pipeline4eos/90-product-data/`
- `30-eos/` 保持职责单一，只装 EOS 产品实现层（引擎/配置/部署等）
- 两条流水线（`10-meta-pipeline/` 和 `20-pipeline4eos/`）的内部结构镜像对称

### 待确定的事项

- 子目录与文件的重命名细化（消除越级重复前缀）
- `200-put-on-hold/` 和 `99-sessions/` 的编号处理
- 各产品数据文件名的精简方案
- 实施步骤与迁移顺序

**Why:** 原目录结构未能体现产品分类——元流水线和 EOS 流水线是同类产品（AI Skill 形态的流水线类产品），却不在同一层次；目录名中的 "design" 后缀使路径读作活动而非产品。新结构让三个产品平级陈列，身份清晰。
