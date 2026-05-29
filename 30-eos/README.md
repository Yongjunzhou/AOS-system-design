# EOS 产品本体

**EOS（Enterprise Operation System）**——企业运营体系的信息化形态，以引擎为能力基础、以配置为使用方式的统一可配置平台。

本目录是 EOS 产品的**实物载体**，由 EOS 流水线（`20-eos-design/`）的四条子线运行产生：

| 流水线 | 产出 | 30-eos/ 对应目录 |
|--------|------|----------------|
| 系统设计线 | 定义产品规格（架构、引擎清单、配置类型） | `10-product-specification/` |
| 组件开发线 | 实现引擎代码、配置定义文件 | `20-engines/` + `30-configurations/` |
| 集成交付线 | 打包部署、测试验证 | `40-deployment/` |
| 系统运维线 | 监控、事件、容量 | `50-operation/` |

## 当前阶段

EOS 开发处于**阶段1（系统设计）**，本目录仅有 `10-product-specification/` 的内容。其余目录为框架占位，待对应流水线启动后逐步填充。

## 目录结构

```
30-eos/
├── 10-product-specification/    ← 产品规格说明（设计线产出）
├── 20-engines/                  ← 引擎实现（开发线产出）
├── 30-configurations/           ← 配置定义（开发线产出）
├── 40-deployment/               ← 部署交付（集成线产出）
└── 50-operation/                ← 运维数据（运维线产出）
```

详见各目录内的 README。
