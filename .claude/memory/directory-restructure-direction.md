---
name: directory-restructure-direction
description: 2026-06-02 完整目录结构调整方案确认：00-generalspec/10-pl4pleos/20-pl4eos/30-eos/80-sessions/90-hold
metadata:
  type: project
---

## 决策：完整目录结构调整方案

2026-06-02 全天讨论，基于产品分类框架调整目录结构。

### 一级目录（已确认）

| 编号 | 目录名 | 内容 |
|------|--------|------|
| `00` | `generalspec` | 通用设计规范 |
| `10` | `pl4pleos` | 元流水线（pl for pipeline → 产出 EOS 流水线的流水线） |
| `20` | `pl4eos` | EOS 流水线 |
| `30` | `eos` | EOS 产品本体 |
| `80` | `sessions` | 会话记录 |
| `90` | `hold` | 暂存归档 |

### 已决定的事项

- 产品数据（9 份标准文档）**随流水线走**，EOS 流水线的产品数据放在 `20-pl4eos/90-product-data/`
- `30-eos/` 保持职责单一，只装 EOS 产品实现层（引擎/配置/部署等）
- 两条流水线（`10-pl4pleos/` 和 `20-pl4eos/`）的内部结构镜像对称
- 所有子目录和文件名去掉越级重复的产品前缀

### 命名模式

`pl4X` 命名模式 = pipeline + 4(for) + X(产出物)。链式关系：`10-pl4pleos → 20-pl4eos → 30-eos`

### 待确定的事项

- [done] 一级目录方案 → 2026-06-02 下午确认
- 子目录与文件名的精简确认
- 实施步骤与迁移顺序

**Why:** 原目录结构未能体现产品分类。新结构让三个产品平级陈列，命名模式一致，身份清晰。
