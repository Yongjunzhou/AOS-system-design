# AOS 端到端工作流指南

**目的**：帮助团队理解 6 个任务的完整流程、依赖关系和并行工作机制

**版本**：v1.0  
**最后更新**：2026-05-13

---

## 一、完整流程概览

### 流程图

```
┌─────────────────────────────────────────────────────────────────────┐
│                    相关方需求收集和规范化                              │
│                      (Task 1: 需求规范化)                            │
│  输入：原始需求  →  规范化  →  分解  →  冲突检测  →  输出：SR 清单   │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
    ┌──────────────────────┐   ┌──────────────────────┐
    │  Task 2: SR → BA     │   │  Task 4: SR-NFR      │
    │  业务架构设计        │   │  非功能需求设计      │
    │  输出：BA 5级节点    │   │  输出：SysReq-NFR    │
    └──────────┬───────────┘   └──────────┬───────────┘
               │                          │
               └────────────┬─────────────┘
                            │
                            ▼
                ┌──────────────────────┐
                │  Task 3: BA → SysReq │
                │  系统需求设计        │
                │  输出：SysReq 9级    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Task 5: SysReq → PA │
                │  产品架构设计        │
                │  输出：PA 末级节点   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  Task 6: 追溯分析    │
                │  符合性检查          │
                │  输出：追溯矩阵      │
                └──────────────────────┘
```

### 流程说明

| 阶段 | 任务 | 输入 | 输出 | 关键活动 |
|------|------|------|------|---------|
| 1 | Task 1：需求规范化 | 原始需求 | SR 清单 | 规范化、分解、冲突检测 |
| 2 | Task 2：SR → BA | SR 清单 | BA 5级节点 | 业务架构设计、N:1 映射 |
| 2 | Task 4：SR-NFR | SR-NFR | SysReq-NFR | 非功能需求设计 |
| 3 | Task 3：BA → SysReq | BA 5级 | SysReq 9级 | 系统需求设计、9级分解 |
| 4 | Task 5：SysReq → PA | SysReq 9级 | PA 末级 | 产品架构设计、权衡决策 |
| 5 | Task 6：追溯分析 | 所有输出 | 追溯矩阵 | 符合性检查、缺陷识别 |

---

## 二、任务依赖关系

### 依赖图

```
Task 1 (需求规范化)
  ├─→ Task 2 (SR → BA)
  │     └─→ Task 3 (BA → SysReq)
  │           └─→ Task 5 (SysReq → PA)
  │                 └─→ Task 6 (追溯分析)
  │
  └─→ Task 4 (SR-NFR)
        └─→ Task 6 (追溯分析)
```

### 关键依赖说明

| 任务 | 前置任务 | 说明 |
|------|---------|------|
| Task 2 | Task 1 | 需要 SR 清单作为输入 |
| Task 3 | Task 2 | 需要 BA 5级节点作为输入 |
| Task 4 | Task 1 | 需要 SR-NFR 清单作为输入 |
| Task 5 | Task 3 | 需要 SysReq 9级节点作为输入 |
| Task 6 | Task 2, 3, 4, 5 | 需要所有映射矩阵作为输入 |

---

## 三、并行工作指南

### 可并行的任务

**第一阶段**（Task 1 完成后）：
- Task 2 和 Task 4 可以并行进行
- Task 2 处理功能需求，Task 4 处理非功能需求
- 两个团队可以独立工作，不相互阻塞

**第二阶段**（Task 2 完成后）：
- Task 3 可以开始
- 同时 Task 2 团队可以支持 Task 4 的非功能需求设计

**第三阶段**（Task 3 完成后）：
- Task 5 可以开始
- 同时 Task 3 团队可以支持 Task 6 的追溯分析准备

### 并行工作的最佳实践

1. **占位符创建**（快速，1-2 小时）
   - 下游团队快速扫描上游文档
   - 识别所有末级节点
   - 在下游文档中创建对应的占位符
   - 建立上下游的映射关系

2. **具体设计**（深入，2-6 天）
   - 下游团队填充占位符的具体内容
   - 设计业务流程、系统需求、产品架构等
   - 为下一层级预留占位符

3. **验证和冻结**（1-2 天）
   - 验证设计的完整性和一致性
   - 冻结下游文档
   - 准备交付给下一个任务

---

## 四、两阶段工作流程（解耦模式）

### 第一阶段：占位符创建（快速）

**目的**：快速建立上下游的映射关系，解耦上下游工作

**步骤**：
1. 下游团队快速扫描上游文档（15-30 分钟）
2. 识别所有末级节点（15-30 分钟）
3. 在下游文档中创建对应的占位符（15-30 分钟）
4. 建立上下游的映射关系（15-30 分钟）
5. 冻结占位符结构（5-10 分钟）

**输出**：
- 下游文档的占位符结构
- 上下游的映射关系清单

**时间**：1-2 小时

### 第二阶段：具体设计（深入）

**目的**：填充占位符，完成具体的设计

**步骤**：
1. 分析上游文档的详细内容（1-2 天）
2. 填充占位符的具体内容（2-4 天）
3. 设计业务流程、系统需求、产品架构等（1-3 天）
4. 为下一层级预留占位符（1 天）
5. 验证设计的完整性和一致性（1 天）
6. 冻结下游文档（1 天）

**输出**：
- 完整的下游文档
- 为下一层级预留的占位符

**时间**：2-6 天

### 优势

- ✅ 上下游文档相对独立
- ✅ 多个团队可以并行工作
- ✅ 时间缩短 30-50%
- ✅ 避免过度的同步迭代

---

## 五、各任务的关键输出

### Task 1：需求规范化

**输出文件**：
- `normalized-requirements.md` — 规范化后的需求清单
- `requirement-decomposition.md` — 需求分解结构
- `conflict-analysis.md` — 冲突分析报告
- `duplicate-analysis.md` — 重复检测报告

**关键内容**：
- SR 清单（功能需求）
- SR-NFR 清单（非功能需求）
- 冲突和重复的检测结果

### Task 2：SR → BA 映射

**输出文件**：
- `ba-design.md` — 业务架构设计（BA 0-5 级）
- `sr-to-ba-mapping.md` — SR → BA 映射矩阵
- `business-component-definitions.md` — 业务组件定义

**关键内容**：
- BA 5 级节点（业务组件）
- SR → BA 的 N:1 映射关系
- 每个 BA 5 级节点的职责定义

### Task 3：BA → SysReq 映射

**输出文件**：
- `sysreq-functional.md` — 系统功能需求（SysReq 0-9 级）
- `ba-to-sysreq-mapping.md` — BA → SysReq 映射矩阵
- `sysreq-component-definitions.md` — 系统需求组件定义

**关键内容**：
- SysReq 5 级节点（组件实例）
- SysReq 9 级节点（场景活动）
- BA → SysReq 的 N:1 映射关系

### Task 4：SR-NFR → SysReq-NFR 映射

**输出文件**：
- `sysreq-nfr.md` — 系统非功能需求（SysReq-NFR 0-5 级）
- `sr-nfr-to-sysreq-nfr-mapping.md` — SR-NFR → SysReq-NFR 映射矩阵
- `nfr-definitions.md` — 非功能需求定义

**关键内容**：
- SysReq-NFR 5 级节点（非功能需求承接层）
- SR-NFR → SysReq-NFR 的 N:1 映射关系
- 每个非功能需求的量化指标和验证方法

### Task 5：SysReq → PA 映射

**输出文件**：
- `pa-design.md` — 产品架构设计（PA 末级节点）
- `sysreq-to-pa-mapping.md` — SysReq → PA 映射矩阵
- `nfr-tradeoff-decisions.md` — 非功能权衡决策

**关键内容**：
- PA 末级节点（前后端组件）
- SysReq 9 级 → PA 的 N:1 映射关系
- 非功能权衡决策和技术栈选型

### Task 6：端到端追溯分析

**输出文件**：
- `traceability-matrix.md` — 完整的追溯矩阵
- `compliance-report.md` — 符合性分析报告
- `defect-list.md` — 缺陷清单

**关键内容**：
- 完整的 SR → BA → SysReq → PA 追溯链路
- 符合性检查结果（追溯完整性、映射一致性、设计完整性）
- 缺陷识别和改进建议

---

## 六、质量检查点

### Task 1 完成后

- [ ] 所有 SR 都已规范化
- [ ] 所有 SR-NFR 都已规范化
- [ ] 冲突和重复都已检测
- [ ] SR 清单已冻结

### Task 2 完成后

- [ ] 所有 SR 都映射到 BA 5 级节点
- [ ] 每个 BA 5 级节点都有明确的职责
- [ ] BA 5 级节点已冻结

### Task 3 完成后

- [ ] 所有 BA 5 级节点都映射到 SysReq 5 级节点
- [ ] 所有 SysReq 9 级节点都已定义
- [ ] SysReq 9 级节点已冻结

### Task 4 完成后

- [ ] 所有 SR-NFR 都映射到 SysReq-NFR 5 级节点
- [ ] 每个 SysReq-NFR 5 级节点都有量化指标
- [ ] SysReq-NFR 5 级节点已冻结

### Task 5 完成后

- [ ] 所有 SysReq 9 级节点都映射到 PA 末级节点
- [ ] 每个 PA 末级节点都有明确的职责
- [ ] 非功能权衡决策已明确
- [ ] PA 末级节点已冻结

### Task 6 完成后

- [ ] 追溯矩阵已生成
- [ ] 符合性检查已完成
- [ ] 缺陷已识别和分类
- [ ] 改进建议已提出

---

## 七、常见问题

**Q：如何处理需求变更？**

A：
1. 在 Task 1 中更新 SR 清单
2. 评估变更对下游任务的影响
3. 更新相应的映射矩阵
4. 在 Task 6 中重新进行追溯分析

**Q：如何处理跨任务的冲突？**

A：
1. 在相应的任务中识别冲突
2. 记录冲突的详细信息
3. 邀请相关团队进行讨论
4. 做出权衡决策
5. 更新相应的文档

**Q：如何加快工作进度？**

A：
1. 使用占位符创建快速建立上下游映射
2. 多个团队并行工作
3. 使用 AI Skill 自动化重复工作
4. 定期进行质量检查，避免返工

**Q：如何确保文档的一致性？**

A：
1. 在每个任务完成后进行质量检查
2. 使用追溯矩阵验证映射关系
3. 定期进行跨任务的一致性检查
4. 建立变更管理流程

---

## 八、工具和资源

### 相关文档

- [Task 1：需求规范化](../01-task-normalization/README.md)
- [Task 2：SR → BA 映射](../02-task-sr-ba-design/README.md)
- [Task 3：BA → SysReq 映射](../03-task-ba-sysreq-design/README.md)
- [Task 4：SR-NFR → SysReq-NFR 映射](../04-task-sr-nfr-design/README.md)
- [Task 5：SysReq → PA 映射](../05-task-sysreq-pa-design/README.md)
- [Task 6：端到端追溯分析](../06-task-traceability-analysis/README.md)

### AI Skill

- `requirement-normalization` — 需求规范化
- `requirement-decomposition` — 需求分解
- `conflict-detection` — 冲突检测
- `duplicate-detection` — 重复检测
- `sr-to-ba-mapping` — SR → BA 映射
- `ba-to-sysreq-mapping` — BA → SysReq 映射
- `sysreq-to-pa-mapping` — SysReq → PA 映射
- `traceability-analysis` — 追溯分析

### 验证工具

```bash
# 验证项目映射关系
python 07-shared-assets/tools/validate.py --project <project-name> --check all

# 生成追溯矩阵报告
python 07-shared-assets/tools/generate-report.py --project <project-name> --report traceability

# 生成项目汇总报告
python 07-shared-assets/tools/generate-report.py --project <project-name> --report summary
```

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-05-13 | 初始版本 |
