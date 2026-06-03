---
name: directory-restructure-direction
description: 2026-06-02 完整目录结构调整方案确认：00-generalspec/10-pl4pleos/20-pl4eos/30-eos/80-sessions/90-hold
metadata: 
  node_type: memory
  type: project
  originSessionId: cd3a4513-26ab-4341-ad97-d7184f0c430a
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

### 命名模式（2026-06-03 优化确认）

#### 一级目录

| 编号 | 目录名 | 内容 |
|------|--------|------|
| `00` | `generalspec` | 通用设计规范 |
| `10` | `pl4pleos` | 元流水线（pl for pipeline → 产出 EOS 流水线的流水线） |
| `20` | `pl4eos` | EOS 流水线 |
| `30` | `eos` | EOS 产品本体 |
| `80` | `sessions` | 会话记录 |
| `90` | `hold` | 暂存归档 |

#### 子线目录

`{seq}-{产品前缀}-subpl-{领域}`

| 目录 | 含义 |
|------|------|
| `10-pl4pleos-subpl-sysdev/` | 元流水线的系统设计子线 |
| `10-pl4eos-subpl-sysdev/` | EOS 流水线的系统设计子线 |

#### Skill 目录（子线内）

`{seq}-{variant}{domain}-4-{target}/`

| 目录 | 含义 |
|------|------|
| `10-wfsysdev-4-pl4eos/` | 用瀑布为 EOS 流水线做系统设计 |
| `10-wfsysdev-4-eos/` | 用瀑布为 EOS 做系统设计 |
| `00-presysdev-4-pl4eos/` | 为 EOS 流水线做预处理 |

#### 运行数据目录

`{seq}-{产品前缀}-2-{输出产品}data/`

| 目录 | 含义 |
|------|------|
| `80-pl4pleos-2-pl4eosdata/` | 元流水线运行数据 → 到 pl4eos 的产品数据 |
| `80-pl4eos-2-eosdata/` | EOS 流水线运行数据 → 到 EOS 的产品数据 |

数据文件以输出产品为前缀：`01-pl4eos-original-requirements.md`、`01-eos-original-requirements.md`。

#### 简写映射

| 简写 | 含义 |
|------|------|
| `4` | for |
| `2` | to |
| `pl` | pipeline |
| `subpl` | sub-pipeline |
| `data` | (输出)产品数据 |

#### 链式命名

```
pl4pleos ──→ subpl-X-4-pl4eos ──→ 80-pl4pleos-2-pl4eosdata
pl4eos   ──→ subpl-X-4-eos      ──→ 80-pl4eos-2-eosdata
```

### 待确定的事项

- [done] 一级目录方案 → 2026-06-02 下午确认
- 子目录与文件名的精简确认
- 实施步骤与迁移顺序

**Why:** 原目录结构未能体现产品分类。新结构让三个产品平级陈列，命名模式一致，身份清晰。
