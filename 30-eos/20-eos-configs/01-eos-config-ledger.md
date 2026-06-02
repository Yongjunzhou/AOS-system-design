# 台账定义

**状态**：待填充

## 说明

台账定义是台账引擎的配置产出，用于描述一个数据列表/看板的结构和展示方式。

## 主要配置项

| 项 | 说明 |
|----|------|
| 列定义 | 列名、数据类型、宽度、对齐 |
| 筛选条件 | 预设筛选器和自定义筛选 |
| 排序规则 | 默认排序和允许的排序方式 |
| 视图配置 | 列表/卡片/树形视图切换 |
| 行操作 | 操作按钮、批量操作、链接跳转 |

## 结构示例

```yaml
ledger:
  id: project-list
  columns:
    - field: projectName
      label: 项目名称
      width: 200
      sortable: true
    - field: status
      label: 状态
      type: enum
      filter: true
  actions:
    - label: 新建
      type: form
      target: project-apply
```

<!-- TODO: 填充完整的配置规范 -->
