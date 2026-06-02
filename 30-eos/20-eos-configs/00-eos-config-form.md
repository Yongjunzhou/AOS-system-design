# 表单定义

**状态**：待填充

## 说明

表单定义是表单引擎的配置产出，用于描述一个数据录入/展示界面的结构。

## 主要配置项

| 项 | 说明 |
|----|------|
| 字段列表 | 字段名、类型、校验规则、默认值 |
| 布局 | 字段排列方式、分组、标签 |
| 数据源 | 表单数据的来源和去向 |
| 行为 | 提交前/后动作、联动规则 |

## 结构示例

```yaml
form:
  id: project-apply
  fields:
    - name: projectName
      type: text
      label: 项目名称
      required: true
    - name: budget
      type: number
      label: 预算金额
      validate: [required, positive]
  layout:
    columns: 2
    groups:
      - label: 基本信息
        fields: [projectName, budget]
```

<!-- TODO: 填充完整的配置规范 -->
