# Task 3：业务架构细化 + 系统功能需求架构设计

## 任务概述

将业务架构（BA）映射到系统功能需求（SysReq），完成SysReq 0-9级的设计。这是从业务架构到系统需求的映射。

**目标**：建立清晰的BA → SysReq映射关系，定义系统功能需求的完整架构

## 输入和输出

| 项目 | 内容 |
|------|------|
| **输入** | `ba-design.md`（来自Task 2）<br>`sr-to-ba-mapping.md`（来自Task 2） |
| **输出** | `sysreq-functional.md`（SysReq 0-9级完整结构）<br>`ba-to-sysreq-mapping.md`（映射矩阵） |
| **占位符** | 为SysReq 9级节点预留PA映射关系 |

## 快速开始（5分钟）

### 第一次使用？按照这个顺序：

1. **了解核心概念**（2分钟）
   - 阅读 [guideline-ba-to-sysreq-mapping.md](guidelines/guideline-ba-to-sysreq-mapping.md) 的"核心概念"部分
   - 理解 SysReq 层级结构（0-9 级）
   - 理解 BA → SysReq 的映射关系

2. **查看完整示例**（2分钟）
   - 阅读 [ba-to-sysreq-example.md](examples/ba-to-sysreq-example.md)
   - 理解 BA → SysReq 的映射过程
   - 学习如何分解到 SysReq 9 级

3. **准备开始工作**（1分钟）
   - 查看 [sysreq-template.md](templates/sysreq-template.md)
   - 准备输入文件（ba-design.md）
   - 准备输出文件（sysreq-functional.md）

### 工作过程中：

- **遇到问题？** 查看 [sysreq-best-practices.md](guidelines/sysreq-best-practices.md)
- **需要检查质量？** 使用 [ba-to-sysreq-checklist.md](checklists/ba-to-sysreq-checklist.md)
- **需要 AI 辅助？** 使用 [skills/](skills/) 目录中的 Skill 定义

## 关键活动

### 1. 架构模式匹配
- 识别业务组件对应的系统架构模式
- 选择合适的系统需求架构模式

**Skill**：[07-shared-assets/patterns/architecture-patterns.md](../07-shared-assets/patterns/architecture-patterns.md)

### 2. BA → SysReq映射
- 将业务架构节点映射到系统需求节点
- 建立N:1映射关系（一个BA 5级节点可能在多个业务上应用）

**Skill**：[ba-to-sysreq-mapping.md](skills/ba-to-sysreq-mapping.md)

### 3. SysReq 5级节点定义
- 定义组件实例（SysReq 5级）
- 明确每个组件实例的职责和范围

### 4. SysReq 6-9级分解
- 定义功能模块（SysReq 6级）
- 定义系统用例（SysReq 7级）
- 定义用例场景（SysReq 8级）
- 定义场景活动（SysReq 9级）

## 工作流

详见 [task-3-workflow.md](workflows/task-3-workflow.md)

**关键步骤**：
1. 分析业务架构节点
2. 识别独立信息系统（SysReq 1级）
3. 创建功能需求分支（SysReq 2级）
4. 定义业务组件类型（SysReq 3级）
5. 定义业务组件小类（SysReq 4级）
6. 定义组件实例（SysReq 5级）
7. 定义功能模块（SysReq 6级）
8. 定义系统用例（SysReq 7级）
9. 定义用例场景（SysReq 8级）
10. 定义场景活动（SysReq 9级）
11. 建立BA → SysReq映射
12. 验证映射完整性
13. 标记占位符
14. 交付检查

## 输出文件结构

```
08-products/projects/<project-name>/03-ba-sysreq-design/
├── sysreq-functional.md         # SysReq 0-9级完整结构（输出）
├── ba-to-sysreq-mapping.md      # BA → SysReq映射矩阵（输出）
└── sysreq-design-notes.md       # 设计过程中的注记
```

## SysReq层级结构（功能分支）

| 层级 | 名称 | 说明 |
|------|------|------|
| 0级 | 根节点 | 整个系统的顶层根节点 |
| 1级 | 独立信息系统 | 一个独立的信息系统 |
| 2级 | 功能需求分支 | 功能需求分支（与非功能需求分支分离） |
| 3级 | 业务组件类型 | 流程、工单、计划、指标等业务组件类型 |
| 4级 | 业务组件小类 | 业务组件类型下的小类分类 |
| **5级** | **组件实例（承接层）** | **★ 承接BA 5级节点的关键层级**<br>- 具体的组件实例<br>- 与BA 5级节点是N:1映射关系 |
| 6级 | 功能模块 | 以标签页为载体的功能模块 |
| 7级 | 系统用例 | 在标签页上提供的功能 |
| 8级 | 用例场景 | 系统用例的具体场景 |
| **9级** | **场景活动** | **★ 映射到产品架构末级节点**<br>- 用例场景的具体活动步骤 |

## 检查清单

完成Task 3前，请使用 [ba-to-sysreq-checklist.md](checklists/ba-to-sysreq-checklist.md) 进行检查：

- [ ] 所有业务架构节点都已分析
- [ ] 独立信息系统定义清晰
- [ ] 功能需求分支已创建
- [ ] 业务组件类型分类合理
- [ ] 业务组件小类定义完整
- [ ] 组件实例（SysReq 5级）定义明确
- [ ] 功能模块（SysReq 6级）定义清晰
- [ ] 系统用例（SysReq 7级）定义完整
- [ ] 用例场景（SysReq 8级）定义具体
- [ ] 场景活动（SysReq 9级）定义详细
- [ ] BA → SysReq映射完整（每个BA 5级节点都映射到至少一个SysReq 5级节点）
- [ ] 占位符已标记
- [ ] 版本号已更新

## 常见问题

**Q：SysReq 5级和BA 5级的关系是什么？**
A：BA 5级是业务组件，SysReq 5级是组件实例。一个BA 5级节点可以在多个业务上应用，因此可能映射到多个SysReq 5级节点（N:1关系）。

**Q：SysReq 9级（场景活动）如何映射到产品架构？**
A：SysReq 9级是最细粒度的功能需求，映射到产品架构末级节点（前后端组件）。这个映射在Task 5中完成。

**Q：如何处理跨越多个组件实例的功能？**
A：这类功能应该在SysReq 8级（用例场景）中定义为跨组件的场景。

## 相关资源

- **架构模式库**：[07-shared-assets/patterns/architecture-patterns.md](../07-shared-assets/patterns/architecture-patterns.md)
- **设计决策模板**：[07-shared-assets/quality-standards/design-decision-template.md](../07-shared-assets/quality-standards/design-decision-template.md)
- **前置任务**：[Task 2：功能相关方需求设计 + 业务架构初步设计](../02-sr-ba-design/README.md)
- **后续任务**：[Task 5：系统需求设计 + 产品架构设计](../05-sysreq-pa-design/README.md)

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-05-12 | 初始版本 |
