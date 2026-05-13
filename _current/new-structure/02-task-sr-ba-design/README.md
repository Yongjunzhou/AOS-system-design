# Task 2：功能相关方需求设计 + 业务架构初步设计

## 任务概述

将功能相关方需求（SR）映射到业务架构（BA），完成BA 0-5级的设计。这是从需求到架构的第一步映射。

**目标**：建立清晰的SR → BA映射关系，定义业务组件（BA 5级）

## 输入和输出

| 项目 | 内容 |
|------|------|
| **输入** | `sr-functional.md`（来自Task 1） |
| **输出** | `ba-design.md`（BA 0-5级完整结构）<br>`sr-to-ba-mapping.md`（映射矩阵） |
| **占位符** | 为BA 5级节点预留下游映射关系 |

## 快速开始（5分钟）

### 第一次使用？按照这个顺序：

1. **了解核心概念**（2分钟）
   - 阅读 [guideline-sr-to-ba-mapping.md](guidelines/guideline-sr-to-ba-mapping.md) 的"核心概念"部分
   - 理解 BA 层级结构（0-5 级）
   - 理解业务组件的两大类（配置方式、开发方式）

2. **查看完整示例**（2分钟）
   - 阅读 [sr-to-ba-example.md](examples/sr-to-ba-example.md)
   - 理解 SR → BA 的映射过程
   - 学习如何定义业务组件

3. **准备开始工作**（1分钟）
   - 查看 [ba-template.md](templates/ba-template.md)
   - 准备输入文件（sr-functional.md）
   - 准备输出文件（ba-design.md）

### 工作过程中：

- **遇到问题？** 查看 [ba-best-practices.md](guidelines/ba-best-practices.md)
- **需要检查质量？** 使用 [sr-to-ba-checklist.md](checklists/sr-to-ba-checklist.md)
- **需要 AI 辅助？** 使用 [skills/](skills/) 目录中的 Skill 定义

## 关键活动

### 1. 业务模式匹配
- 识别需求对应的业务模式
- 选择合适的业务架构模式

**Skill**：[business-pattern-matching.md](../07-shared-assets/patterns/business-patterns.md)

### 2. SR → BA映射
- 将功能相关方需求映射到业务架构节点
- 建立N:1映射关系（多条SR可映射到一个BA 5级节点）

**Skill**：[sr-to-ba-mapping.md](skills/sr-to-ba-mapping.md)

### 3. BA 5级节点定义
- 定义业务组件（BA 5级）
- 明确每个业务组件的职责和范围

## 工作流

详见 [task-2-workflow.md](workflows/task-2-workflow.md)

**关键步骤**：
1. 分析功能相关方需求
2. 识别业务域（BA 1级）
3. 识别端到端项目（BA 2级）
4. 设计项目业务对象架构（BA 3级）
5. 分解工作包（BA 4级）
6. 定义业务组件（BA 5级）
7. 建立SR → BA映射
8. 验证映射完整性
9. 标记占位符
10. 交付检查

## 输出文件结构

```
08-products/projects/<project-name>/02-sr-ba-design/
├── ba-design.md                 # BA 0-5级完整结构（输出）
├── sr-to-ba-mapping.md          # SR → BA映射矩阵（输出）
└── ba-design-notes.md           # 设计过程中的注记
```

## BA层级结构

| 层级 | 名称 | 说明 |
|------|------|------|
| 0级 | 架构根节点 | 整个系统的顶层根节点 |
| 1级 | 业务域 | 按业务领域划分 |
| 2级 | 端到端项目 | 跨越多个业务域的项目 |
| 3级 | 项目业务对象架构节点 | 端到端业务的架构节点 |
| 4级 | 工作包（WBS） | 对象架构节点下的工作分解结构 |
| **5级** | **业务组件（承接层）** | **★ 承接相关方需求的关键层级**<br>- 计划定义、流程定义、工单定义、指标定义等<br>- ★ 末级，不再分解 |

## 检查清单

完成Task 2前，请使用 [sr-to-ba-checklist.md](checklists/sr-to-ba-checklist.md) 进行检查：

- [ ] 所有功能相关方需求都已分析
- [ ] 业务域划分合理
- [ ] 端到端项目定义清晰
- [ ] 业务对象架构完整
- [ ] 工作包分解合理
- [ ] 业务组件（BA 5级）定义明确
- [ ] SR → BA映射完整（每条SR都映射到至少一个BA 5级节点）
- [ ] 占位符已标记
- [ ] 版本号已更新

## 常见问题

**Q：BA 5级是末级，那么如何处理复杂的业务组件？**
A：复杂的业务组件在Task 3中分解为系统需求（SysReq 6-9级）。BA 5级只定义业务组件的名称和职责。

**Q：一个SR可以映射到多个BA 5级节点吗？**
A：不可以。每条SR只能映射到唯一的BA 5级节点（1:1约束）。但一个BA 5级节点可以承接多条SR（N:1关系）。

**Q：如何处理跨越多个业务域的需求？**
A：这类需求应该映射到BA 2级（端到端项目）下的业务组件。

## 相关资源

- **业务模式库**：[07-shared-assets/patterns/business-patterns.md](../07-shared-assets/patterns/business-patterns.md)
- **设计决策模板**：[07-shared-assets/quality-standards/design-decision-template.md](../07-shared-assets/quality-standards/design-decision-template.md)
- **前置任务**：[Task 1：新增原始需求规范化](../01-task-normalization/README.md)
- **后续任务**：[Task 3：业务架构细化 + 系统功能需求架构设计](../03-task-ba-sysreq-design/README.md)

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-05-12 | 初始版本 |
