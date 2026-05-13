# Task 5：系统需求设计 + 产品架构设计

## 任务概述

将系统功能需求和非功能需求映射到产品架构（PA），完成PA末级节点设计和非功能权衡。这是从系统需求到产品架构的最终映射。

**目标**：建立清晰的SysReq → PA映射关系，定义前后端组件，完成非功能权衡决策

## 输入和输出

| 项目 | 内容 |
|------|------|
| **输入** | `sysreq-functional.md`（来自Task 3）<br>`ba-to-sysreq-mapping.md`（来自Task 3）<br>`sysreq-nfr.md`（来自Task 4）<br>`sr-nfr-to-sysreq-nfr-mapping.md`（来自Task 4） |
| **输出** | `pa-design.md`（PA末级节点设计）<br>`sysreq-to-pa-mapping.md`（映射矩阵）<br>`nfr-tradeoff-decisions.md`（非功能权衡决策） |
| **占位符** | 无 |

## 快速开始（5分钟）

### 第一次使用？按照这个顺序：

1. **了解核心概念**（2分钟）
   - 阅读 [guideline-sysreq-to-pa-mapping.md](guidelines/guideline-sysreq-to-pa-mapping.md) 的"核心概念"部分
   - 理解 PA 末级节点的分类（前端、后端、数据库、其他）
   - 理解非功能权衡决策

2. **查看完整示例**（2分钟）
   - 阅读 [sysreq-to-pa-example.md](examples/sysreq-to-pa-example.md)
   - 理解 SysReq → PA 的映射过程
   - 学习如何进行非功能权衡

3. **准备开始工作**（1分钟）
   - 查看 [pa-template.md](templates/pa-template.md)
   - 准备输入文件（sysreq-functional.md、sysreq-nfr.md）
   - 准备输出文件（pa-design.md、nfr-tradeoff-decisions.md）

### 工作过程中：

- **遇到问题？** 查看 [pa-best-practices.md](guidelines/pa-best-practices.md)
- **需要检查质量？** 使用 [sysreq-to-pa-checklist.md](checklists/sysreq-to-pa-checklist.md) 和 [nfr-tradeoff-checklist.md](checklists/nfr-tradeoff-checklist.md)
- **需要 AI 辅助？** 使用 [skills/](skills/) 目录中的 Skill 定义

## 关键活动

### 1. SysReq → PA映射
- 将系统功能需求（SysReq 9级）映射到产品架构末级节点
- 建立N:1映射关系（多个SysReq 9级可映射到一个PA末级节点）

**Skill**：[sysreq-to-pa-mapping.md](skills/sysreq-to-pa-mapping.md)

### 2. PA末级节点定义
- 定义前后端组件
- 明确每个组件的职责和接口

### 3. 非功能权衡分析
- 分析非功能需求对产品架构的影响
- 进行权衡决策（性能 vs 成本、安全 vs 易用性等）
- 记录权衡理由

### 4. 技术栈选型
- 选择合适的技术栈
- 记录技术决策和理由

## 工作流

详见 [task-5-workflow.md](workflows/task-5-workflow.md)

**关键步骤**：
1. 分析系统功能需求（SysReq 9级）
2. 分析系统非功能需求（SysReq-NFR 5级）
3. 识别前端组件
4. 识别后端组件
5. 定义组件接口
6. 进行非功能权衡分析
7. 进行技术栈选型
8. 建立SysReq → PA映射
9. 验证映射完整性
10. 记录权衡决策
11. 交付检查

## 输出文件结构

```
08-products/projects/<project-name>/05-sysreq-pa-design/
├── pa-design.md                 # PA末级节点设计（输出）
├── sysreq-to-pa-mapping.md      # SysReq → PA映射矩阵（输出）
├── nfr-tradeoff-decisions.md    # 非功能权衡决策（输出）
└── pa-design-notes.md           # 设计过程中的注记
```

## PA末级节点定义

产品架构末级节点是**前后端组件**，包括：

### 前端组件
- **页面/视图**：用户界面的主要容器
- **功能模块**：页面上的功能区域
- **组件**：可复用的UI组件
- **服务**：前端业务逻辑服务

### 后端组件
- **API端点**：RESTful API或GraphQL端点
- **业务服务**：业务逻辑处理服务
- **数据访问层**：数据库访问和缓存
- **第三方集成**：与外部系统的集成

## 非功能权衡决策

### 常见权衡场景

| 权衡 | 选项A | 选项B | 决策因素 |
|------|-------|-------|---------|
| 性能 vs 成本 | 高性能架构（高成本） | 标准架构（低成本） | 业务需求、预算 |
| 安全 vs 易用性 | 高安全（复杂认证） | 易用（简单认证） | 数据敏感度、用户体验 |
| 可扩展性 vs 复杂性 | 微服务架构 | 单体架构 | 业务增长预期、团队能力 |
| 实时性 vs 成本 | 实时处理 | 批量处理 | 业务需求、基础设施成本 |

### 权衡决策记录

每个权衡决策应该记录：
- **权衡项**：要权衡的两个方面
- **选项A**：第一个选项及其优缺点
- **选项B**：第二个选项及其优缺点
- **决策**：最终选择
- **理由**：决策的原因
- **影响**：决策对系统的影响

## 检查清单

完成Task 5前，请使用 [sysreq-to-pa-checklist.md](checklists/sysreq-to-pa-checklist.md) 和 [nfr-tradeoff-checklist.md](checklists/nfr-tradeoff-checklist.md) 进行检查：

**功能映射检查**：
- [ ] 所有SysReq 9级节点都已分析
- [ ] 前端组件定义清晰
- [ ] 后端组件定义清晰
- [ ] 组件接口定义完整
- [ ] SysReq → PA映射完整（每个SysReq 9级都映射到至少一个PA末级节点）
- [ ] 版本号已更新

**非功能权衡检查**：
- [ ] 所有SysReq-NFR 5级节点都已分析
- [ ] 性能需求的权衡已决策
- [ ] 安全需求的权衡已决策
- [ ] 可扩展性需求的权衡已决策
- [ ] 其他非功能需求的权衡已决策
- [ ] 每个权衡决策都有明确的理由
- [ ] 权衡决策对PA的影响已评估
- [ ] 技术栈选型已确定
- [ ] 版本号已更新

## 常见问题

**Q：PA末级节点应该有多细粒度？**
A：PA末级节点应该是可以独立开发、测试、部署的最小单位。通常是一个前端页面/模块或一个后端API/服务。

**Q：一个SysReq 9级可以映射到多个PA末级节点吗？**
A：可以。一个场景活动可能需要多个前后端组件协作实现（N:1关系）。

**Q：如何处理跨越多个PA末级节点的非功能需求？**
A：这类需求应该在权衡决策中明确说明，并在相关的PA末级节点中都进行相应的设计。

**Q：技术栈选型应该在这个阶段进行吗？**
A：是的。技术栈选型是非功能权衡的重要部分，应该在这个阶段进行，并记录在 `nfr-tradeoff-decisions.md` 中。

## 相关资源

- **架构模式库**：[07-shared-assets/patterns/architecture-patterns.md](../07-shared-assets/patterns/architecture-patterns.md)
- **设计决策模板**：[07-shared-assets/quality-standards/design-decision-template.md](../07-shared-assets/quality-standards/design-decision-template.md)
- **前置任务**：[Task 3：业务架构细化 + 系统功能需求架构设计](../03-task-ba-sysreq-design/README.md) 和 [Task 4：非功能相关方需求设计 + 系统非功能需求架构设计](../04-task-sr-nfr-design/README.md)
- **后续任务**：[Task 6：端到端符合性分析](../06-task-traceability-analysis/README.md)

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-05-12 | 初始版本 |
