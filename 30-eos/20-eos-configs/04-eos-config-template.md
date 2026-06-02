# 模板定义

**状态**：待填充

## 说明

模板定义是一种组合配置类型，将多个配置定义（表单、流程、台账等）打包为一个可复用的业务模板。

## 主要配置项

| 项 | 说明 |
|----|------|
| 包含的配置 | 模板中包含的表单、台账、流程等 |
| 配置关系 | 各配置之间的关联和依赖 |
| 初始化参数 | 实例化模板时需要提供的参数 |

## 结构示例

```yaml
template:
  id: project-management
  name: 项目管理模板
  includes:
    - form: project-apply
    - form: project-budget
    - ledger: project-list
    - process: project-approval
    - process: budget-change
  relations:
    - from: project-apply
      to: project-list
      type: feeds
```

<!-- TODO: 填充完整的配置规范 -->
