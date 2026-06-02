# 配置定义

本目录存放 EOS 所有**业务配置定义文件**，由 EOS 流水线**组件开发线**运行产出。每个配置定义是引擎运行时的具体配置实例。

## 配置类型

| # | 目录 | 配置内容 | 对应引擎 | 状态 |
|---|------|---------|---------|------|
| 1 | `form-definitions/` | 表单定义 JSON/YAML | 表单引擎 | 待填充 |
| 2 | `tab-definitions/` | 标签页定义 | 标签页引擎 | 待填充 |
| 3 | `menu-definitions/` | 菜单定义 | 菜单引擎 | 待填充 |
| 4 | `ledger-definitions/` | 台账定义 | 台账引擎 | 待填充 |
| 5 | `dictionary-definitions/` | 字典定义 | 字典引擎 | 待填充 |
| 6 | `process-definitions/` | 流程定义 BPMN | 流程引擎 | 待填充 |
| 7 | `ticket-definitions/` | 工单定义 | 工单引擎 | 待填充 |
| 8 | `indicator-definitions/` | 指标定义 | 指标引擎 | 待填充 |
| 9 | `project-definitions/` | 项目定义 | 项目引擎 | 待填充 |

## 当前文档

| # | 文档 | 说明 |
|---|------|------|
| 00 | `00-eos-config-form.md` | 表单定义配置规范（模板） |
| 01 | `01-eos-config-ledger.md` | 台账定义配置规范（模板） |
| 02 | `02-eos-config-process.md` | 流程定义配置规范（模板） |
| 03 | `03-eos-config-indicator.md` | 指标定义配置规范（模板） |
| 04 | `04-eos-config-template.md` | 模板定义配置规范（模板） |

## 说明

- 配置类型清单与 `00-eos-product-spec/02-eos-configuration-catalog.md` 一致
- 本目录阶段1（系统设计）为空，阶段2（构件开发）启动后逐步填充
