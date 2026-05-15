# Task 1：新增原始需求规范化

## 任务概述

将原始需求转化为规范化的相关方需求（SR），为后续的业务架构设计奠定基础。

**目标**：确保所有需求都符合规范格式、逻辑清晰、无冲突、无重复

## 输入和输出

| 项目 | 内容 |
|------|------|
| **输入** | 原始需求文档（可能格式不统一、表述不清） |
| **输出** | `sr-functional.md`（功能相关方需求）<br>`sr-nfr.md`（非功能相关方需求） |
| **占位符** | 标记待确认项 |

## 快速开始（5分钟）

### 第一次使用？按照这个顺序：

1. **了解核心概念**（2分钟）
   - 阅读 [guideline-normalization.md](guidelines/guideline-normalization.md) 的"核心概念"部分
   - 理解功能需求 vs 非功能需求的区别
   - 理解业务组件 vs 引擎组件的区别

2. **查看完整示例**（2分钟）
   - 阅读 [normalization-example.md](examples/normalization-example.md)
   - 理解规范化的完整过程
   - 学习如何处理重复和冲突需求

3. **准备开始工作**（1分钟）
   - 查看 [sr-template.md](templates/sr-template.md) 和 [sr-nfr-template.md](templates/sr-nfr-template.md)
   - 准备输入文件（原始需求）
   - 准备输出文件（规范化需求）

### 工作过程中：

- **遇到问题？** 查看 [common-errors-and-best-practices.md](guidelines/common-errors-and-best-practices.md)
- **需要检查质量？** 使用 [normalization-checklist.md](checklists/normalization-checklist.md)
- **需要 AI 辅助？** 使用 [skills/](skills/) 目录中的 Skill 定义

## 关键活动

### 1. 需求规范化
- 统一需求格式
- 明确需求描述
- **补充性能指标**（关键改进）
  - 功能需求：添加响应时间、吞吐量、并发数等指标
  - 非功能需求：添加验证条件、测试方法、具体数值等指标

**Skill**：[requirement-normalization.md](skills/requirement-normalization.md)

### 2. 需求分解
- 将复杂需求分解为原子需求
- 识别需求之间的依赖关系
- **为每个分解后的需求补充性能指标**

**Skill**：[requirement-decomposition.md](skills/requirement-decomposition.md)

### 3. 冲突检测
- 识别相互矛盾的需求
- 标记需要人工确认的冲突
- **检查性能指标是否冲突**（如响应时间 < 100ms 和 < 500ms）

**Skill**：[conflict-detection.md](skills/conflict-detection.md)

### 4. 重复检测
- 识别重复的需求
- 合并相同的需求
- **检查性能指标是否一致**

**Skill**：[duplicate-detection.md](skills/duplicate-detection.md)

### 5. 分类和确认
- 将需求分为功能需求（SR）和非功能需求（SR-NFR）
- 人工确认规范化结果
- **确认每个需求都包含需求描述和性能指标**

## 工作流

详见 [task-1-workflow.md](workflows/task-1-workflow.md)

**12步工作流**：
1. 收集原始需求
2. 规范化 + 分解
3. 冲突检测
4. 重复检测
5. 分类和建议
6. 人工确认
7. 生成SR（功能）
8. 生成SR-NFR（非功能）
9. 标记占位符
10. 版本控制
11. 交付检查
12. 归档

## 输出文件结构

```
08-products/projects/<project-name>/01-normalization/
├── raw-requirements.md          # 原始需求（输入）
├── sr-functional.md             # 规范化的功能相关方需求（输出）
├── sr-nfr.md                    # 规范化的非功能相关方需求（输出）
└── normalization-notes.md       # 规范化过程中的注记
```

## 检查清单

完成Task 1前，请使用 [normalization-checklist.md](checklists/normalization-checklist.md) 进行检查：

- [ ] 所有需求都符合规范格式
- [ ] 所有需求都有明确的描述
- [ ] 没有相互矛盾的需求
- [ ] 没有重复的需求
- [ ] 功能需求和非功能需求已分类
- [ ] 占位符已标记
- [ ] 版本号已更新

## 常见问题

**Q：如何区分功能需求和非功能需求？**
A：功能需求描述系统应该做什么（What），非功能需求描述系统应该如何做（How）。详见 [guideline-normalization.md](guidelines/guideline-normalization.md)

**Q：如何处理冲突的需求？**
A：标记冲突，记录冲突的原因，等待人工确认。详见 [conflict-detection.md](skills/conflict-detection.md)

**Q：占位符应该如何标记？**
A：使用 `[TODO: ...]` 标记待确认项。详见 [sr-template.md](templates/sr-template.md)

## 相关资源

- **业务模式库**：[07-shared-assets/patterns/business-patterns.md](../07-shared-assets/patterns/business-patterns.md)
- **质量检查清单**：[07-shared-assets/quality-standards/quality-checklist.md](../07-shared-assets/quality-standards/quality-checklist.md)
- **下一步**：完成Task 1后，进入 [Task 2：功能相关方需求设计 + 业务架构初步设计](../02-sr-ba-design/README.md)

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-05-12 | 初始版本 |
