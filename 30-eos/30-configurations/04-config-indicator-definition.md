# 指标定义

**状态**：待填充

## 说明

指标定义是指标引擎的配置产出，用于描述一个绩效指标的计算逻辑和展示方式。

## 主要配置项

| 项 | 说明 |
|----|------|
| 指标公式 | 计算公式和取数规则 |
| 数据来源 | 指标数据的来源台账/表单 |
| 聚合方式 | 求和、均值、计数、自定义 |
| 目标值 | 指标的目标值、阈值、预警线 |
| 展示方式 | 数值、图表、仪表盘 |

## 结构示例

```yaml
indicator:
  id: project-completion-rate
  name: 项目完成率
  formula: completed_count / total_count * 100
  source:
    ledger: project-list
    filter: date_range = current_month
  target:
    value: 90
    warning: 80
    critical: 60
```

<!-- TODO: 填充完整的配置规范 -->
