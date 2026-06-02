# 流程定义

**状态**：待填充

## 说明

流程定义是流程引擎的配置产出，用于描述一个业务流程的节点、转换和规则。

## 主要配置项

| 项 | 说明 |
|----|------|
| 节点定义 | 审批节点、任务节点、条件分支、并行网关 |
| 转换条件 | 节点间的流转条件和路由规则 |
| 表单绑定 | 各节点关联的表单定义 |
| 审批规则 | 会签、或签、一票否决等 |
| 超时设置 | 节点超时时间和自动处理规则 |

## 结构示例

```yaml
process:
  id: purchase-approval
  nodes:
    - id: start
      type: start
      next: [dept-approve]
    - id: dept-approve
      type: approval
      assignee: dept-manager
      next: [finance-approve]
    - id: finance-approve
      type: approval
      assignee: finance-manager
      next: [end]
```

<!-- TODO: 填充完整的配置规范 -->
