# 引擎实现

本目录存放 EOS 所有引擎的**软件实现**，由 EOS 流水线**组件开发线**运行产出。

## 引擎清单

| # | 引擎目录 | 说明 | 状态 |
|---|---------|------|------|
| 1 | `form-engine/` | 表单引擎 | 待开发 |
| 2 | `tab-engine/` | 标签页引擎 | 待开发 |
| 3 | `menu-engine/` | 菜单引擎 | 待开发 |
| 4 | `ledger-engine/` | 台账引擎 | 待开发 |
| 5 | `dictionary-engine/` | 字典引擎 | 待开发 |
| 6 | `master-data-engine/` | 主数据引擎 | 待开发 |
| 7 | `relation-engine/` | 关系引擎 | 待开发 |
| 8 | `process-engine/` | 流程引擎 | 待开发 |
| 9 | `ticket-engine/` | 工单引擎 | 待开发 |
| 10 | `progress-engine/` | 进展引擎 | 待开发 |
| 11 | `project-engine/` | 项目引擎 | 待开发 |
| 12 | `wbs-engine/` | WBS 引擎 | 待开发 |
| 13 | `plan-engine/` | 计划引擎 | 待开发 |
| 14 | `indicator-engine/` | 指标引擎 | 待开发 |
| 15 | `kanban-engine/` | 看板引擎 | 待开发 |
| 16 | `xbom-engine/` | xBOM 引擎 | 待开发 |
| 17 | `version-engine/` | 版本管理引擎 | 待开发 |
| 18 | `mrp-engine/` | MRP 运算引擎 | 待开发 |
| 19 | `mro-engine/` | MRO 算法引擎 | 待开发 |
| 20 | `trace-engine/` | 追踪引擎 | 待开发 |
| 21 | `cax-engine/` | CAX 桥接引擎 | 待开发 |

## 每个引擎目录的典型结构

```
form-engine/
├── src/                    # 源码
├── tests/                  # 测试
├── docs/                   # 引擎专有文档
├── build.gradle/pom.xml    # 构建配置
└── README.md               # 引擎说明
```

## 说明

- 引擎清单与 `10-product-specification/02-engine-catalog.md` 一致
- 各引擎的规格定义见产品规格说明，实现在此目录按构件展开
- 本目录阶段1（系统设计）为空，阶段2（构件开发）启动后逐步填充
