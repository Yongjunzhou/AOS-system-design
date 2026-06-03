# 设计线 — 运营体系系统设计流水线
**Product B — System Design Pipeline**

**文档版本**：v2.0  
**最后更新**：2026-05-17

---

## 产品定位

系统设计流水线（System Design Pipeline）是为 EOS 开发者打造的"设计工具"，帮助他们将原始需求逐层推导至产品架构。设计线 的范围严格限定在产品开发阶段1（系统设计）。

---

## 目录结构

```
10-pl4pleos/
├── 00-pl4pleos-spec/                   # 设计描述文档
│   ├── 01-pl4pleos-spec-sysdev.md     #   系统设计规范
│   ├── 02-pl4pleos-spec-comdev.md     #   构件开发规范（待编写）
│   ├── 03-pl4pleos-spec-sysint.md     #   集成交付规范（待编写）
│   ├── 04-pl4pleos-spec-sysops.md     #   系统运维规范（待编写）
│   └── 06-pl4pleos-glossary.md        #   术语对照
├── 10-pl4pleos-subpl-sysdev/           # 系统设计子线
│   ├── 00-presysdev-4-pl4eos/         #   OR 预处理
│   ├── 10-wfsysdev-4-pl4eos/          #   瀑布（6 任务）
│   ├── 20-resysdev-4-pl4eos/          #   逆向工程（8 任务）
│   ├── 30-agsysdev-4-pl4eos/          #   敏捷（8 任务）
│   ├── 40-opsysdev-4-pl4eos/          #   DevOps（4 任务）
│   └── README.md
├── 20-pl4pleos-subpl-comdev/           # 构件开发子线（待扩展）
├── 30-pl4pleos-subpl-sysint/           # 集成交付子线（待扩展）
├── 40-pl4pleos-subpl-sysops/           # 系统运维子线（待扩展）
└── 80-pl4pleos-2-pl4eosdata/           # 运行数据—元流水线到 pl4eos 的产品数据
```

---

## 各子目录说明

### 10-pl4eos-sysdev/

设计线 阶段1 的完整工作空间，详见 [10-pl4eos-sysdev/README.md](10-pl4eos-sysdev/README.md)。

| 子目录 | 性质 | 文档数 | 说明 |
|--------|------|--------|------|
| `10-pl4eos-sysdev-spec/` | 通用（参考） | 8 | 5层结构、映射规则、各层通用规范、术语表 |
| `20-pl4eos-sysdev-tasks/` | 设计线 构件 | 26 | 瀑布/敏捷/逆向工程/DevOps 四种场景的操作规程 |
| `90-pl4eos-system-product-data/` | 设计线 设计输出 | 10 | 标准产品数据（01-OR ~ 09-验证报告 + README） |

### 20-pl4eos-comdev/

设计线 阶段2 的工作空间。当前为空，待系统设计完成后扩展。

### 30-pl4eos-sysint/

设计线 阶段3 的工作空间。当前为空，待构件开发完成后扩展。

---

## 产品数据概览

产品数据位于 `10-pl4eos-sysdev/90-pl4eos-system-product-data/`，按五层结构组织：

| 编号 | 文档 | 层级 | 版本 | 状态 |
|------|------|------|------|------|
| 01 | 原始需求详细定义 | 第1层 | v4.0 | 已完成 |
| 02 | 相关方需求架构定义 | 第2层（架构） | v2.0 | 已完成 |
| 03 | 相关方需求详细定义 | 第2层（详细） | v2.0 | 已完成 |
| 04 | 业务架构定义 | 第3层 | v1.0 | 待设计 |
| 05 | 系统需求架构定义 | 第4层（架构） | v2.0 | 已完成 |
| 06 | 系统需求详细定义 | 第4层（详细） | v2.0 | 已完成 |
| 07 | 产品架构定义 | 第5层 | v2.0 | 已完成 |
| 08 | 追溯矩阵 | 全层 | v2.0 | 已完成 |
| 09 | 验证报告 | 全层 | v2.0 | 已完成 |

---

## 遗留问题

| 编号 | 描述 | 优先级 |
|------|------|--------|
| 1 | 业务架构（04）待设计，当前 SR-F → SysReq-F 映射跳过 BA 层 | P1 |
| 2 | AI Skills 子目录（11 个 Skill 定义文件）待迁移至产品数据 | P1 |

---

**文档版本**：v2.0  
**最后更新**：2026-05-17
