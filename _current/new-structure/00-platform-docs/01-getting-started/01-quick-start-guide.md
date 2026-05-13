# AOS 系统设计流水线 - 快速开始指南

**目的**：帮助新用户快速理解和使用 AOS 系统设计流水线

**版本**：v1.0  
**最后更新**：2026-05-12

---

## 一、5分钟快速了解

### 什么是 AOS？

AOS（Architecture & Orchestration System）是一个系统设计治理项目，将企业系统设计流程标准化、资产化、自动化。

**核心流程**：
```
相关方需求 (SR) 
  ↓ [规范化、分解]
业务架构 (BA) 
  ↓ [分配映射]
系统需求 (SysReq) 
  ↓ [分配映射]
产品架构 (PA)
```

### 核心特点

- ✅ **两轨模型**：功能需求和非功能需求分开处理
- ✅ **两阶段工作流**：占位符创建（1-2小时）+ 具体设计（2-6天）
- ✅ **多对一映射**：多条需求可映射到一个承接点
- ✅ **完整追溯**：从需求到架构的完整链路

---

## 二、6 个核心任务

AOS 采用**任务驱动架构**，将整个设计流程分解为 6 个独立的工作单元。每个任务都有完整的指南、模板、检查清单、Skill 和工作流。

### Task 1：需求规范化 📋

**目标**：收集、规范化、分解原始需求，检测冲突和重复

**快速开始**：
- 📖 [Task 1 README](../01-normalization/README.md)
- 📝 [规范化指南](../01-normalization/guidelines/)
- 📋 [检查清单](../01-normalization/checklists/)
- 🎯 [工作流](../01-normalization/workflows/)

**关键输出**：规范化的相关方需求（SR）

---

### Task 2：SR → BA 映射 🏢

**目标**：将相关方需求映射到业务架构 5 级节点

**快速开始**：
- 📖 [Task 2 README](../02-sr-ba-design/README.md)
- 📝 [映射指南](../02-sr-ba-design/guidelines/)
- 📋 [检查清单](../02-sr-ba-design/checklists/)
- 🎯 [工作流](../02-sr-ba-design/workflows/)

**关键输出**：业务架构设计 + SR→BA 映射矩阵

---

### Task 3：BA → SysReq 映射 ⚙️

**目标**：将业务架构映射到系统需求 5 级节点

**快速开始**：
- 📖 [Task 3 README](../03-ba-sysreq-design/README.md)
- 📝 [映射指南](../03-ba-sysreq-design/guidelines/)
- 📋 [检查清单](../03-ba-sysreq-design/checklists/)
- 🎯 [工作流](../03-ba-sysreq-design/workflows/)

**关键输出**：系统需求设计 + BA→SysReq 映射矩阵

---

### Task 4：SR-NFR → SysReq-NFR 映射 🎯

**目标**：将相关方非功能需求映射到系统非功能需求

**快速开始**：
- 📖 [Task 4 README](../04-sr-nfr-design/README.md)
- 📝 [映射指南](../04-sr-nfr-design/guidelines/)
- 📋 [检查清单](../04-sr-nfr-design/checklists/)
- 🎯 [工作流](../04-sr-nfr-design/workflows/)

**关键输出**：系统非功能需求 + SR-NFR→SysReq-NFR 映射矩阵

---

### Task 5：SysReq → PA 映射 🔧

**目标**：将系统需求映射到产品架构末级节点（前后端组件）

**快速开始**：
- 📖 [Task 5 README](../05-sysreq-pa-design/README.md)
- 📝 [映射指南](../05-sysreq-pa-design/guidelines/)
- 📋 [检查清单](../05-sysreq-pa-design/checklists/)
- 🎯 [工作流](../05-sysreq-pa-design/workflows/)

**关键输出**：产品架构设计 + SysReq→PA 映射矩阵 + 非功能权衡决策

---

### Task 6：端到端追溯分析 ✅

**目标**：验证完整的追溯链路，生成符合性报告

**快速开始**：
- 📖 [Task 6 README](../06-traceability-analysis/README.md)
- 📝 [分析指南](../06-traceability-analysis/guidelines/)
- 📋 [检查清单](../06-traceability-analysis/checklists/)
- 🎯 [工作流](../06-traceability-analysis/workflows/)

**关键输出**：追溯矩阵 + 符合性报告 + 缺陷清单

---

## 三、我是...我应该做什么？

### 👤 业务部门（需求提出方）

**你的任务**：提出清晰的相关方需求

**快速步骤**：
1. 阅读 [Task 1 规范化指南](../01-normalization/guidelines/)
2. 按照模板填写需求（参考 [相关方需求模板](../01-normalization/templates/)）
3. 提交给企业架构团队进行规范化处理

**关键点**：
- 需求要清晰、具体、可测量
- 区分功能需求（做什么）和非功能需求（如何做）
- 提供背景和原因

---

### 👨‍💼 企业架构团队

**你的任务**：执行 Task 1 和 Task 2

**快速步骤**：

#### Task 1：需求规范化（1-2小时）
- 参考：[Task 1 README](../01-normalization/README.md)
- 检查完整性、分解、冲突检测、重复检测、分类确认

#### Task 2：SR → BA 映射（2-3天）
- 参考：[Task 2 README](../02-sr-ba-design/README.md)
- 创建占位符、设计业务架构、建立映射关系

**关键工具**：
- 验证：`python 07-shared-assets/tools/validate.py --project <name> --check ba`

---

### 🏗️ 系统设计团队

**你的任务**：执行 Task 3、Task 4 和 Task 5

**快速步骤**：

#### Task 3：BA → SysReq 映射（2-3天）
- 参考：[Task 3 README](../03-ba-sysreq-design/README.md)
- 创建占位符、设计系统需求、建立映射关系

#### Task 4：SR-NFR → SysReq-NFR 映射（1-2天）
- 参考：[Task 4 README](../04-sr-nfr-design/README.md)
- 设计非功能需求、建立映射关系

#### Task 5：SysReq → PA 映射（2-3天）
- 参考：[Task 5 README](../05-sysreq-pa-design/README.md)
- 创建占位符、设计产品架构、建立映射关系

**关键工具**：
- 验证：`python 07-shared-assets/tools/validate.py --project <name> --check all`

---

### 🔍 质量保证团队

**你的任务**：执行 Task 6 和质量检查

**快速步骤**：

#### Task 6：端到端追溯分析（1-2天）
- 参考：[Task 6 README](../06-traceability-analysis/README.md)
- 验证追溯链路、生成符合性报告、识别缺陷

#### 质量检查
- 验证所有映射关系的完整性
- 生成质量报告
- 记录变更到 `changelog.md`

**关键工具**：
- 验证：`python 07-shared-assets/tools/validate.py --project <name> --check all`
- 报告：`python 07-shared-assets/tools/generate-report.py --project <name> --report summary`

---

### 🤖 AI/Skill开发团队

**你的任务**：开发自动化Skill，优化流水线

**快速步骤**：

1. **了解Skill定义**
   - 查看各任务目录下的 `skills/` 子目录
   - 理解输入、输出、处理逻辑

2. **开发核心Skill**
   - Task 1：requirement-normalization、requirement-decomposition、conflict-detection、duplicate-detection
   - Task 2：business-pattern-matching、sr-to-ba-mapping
   - Task 3：architecture-pattern-matching、ba-to-sysreq-mapping
   - Task 4：sr-nfr-to-sysreq-nfr-mapping
   - Task 5：sysreq-to-pa-mapping
   - Task 6：traceability-analysis

3. **优化提示词**
   - 建立提示词库
   - 优化检测精准度
   - 记录最佳实践

**关键文件**：
- Skill定义：各任务目录下的 `skills/` 子目录
- 工具脚本：`07-shared-assets/tools/`

---

### 场景1：新增一个相关方需求

**时间**：3-5天

**步骤**：
1. 业务部门提出需求
2. 执行 Task 1：需求规范化（1-2小时）
3. 执行 Task 2：SR → BA 映射（2-3天）
4. 执行 Task 3：BA → SysReq 映射（2-3天）
5. 执行 Task 4：SR-NFR → SysReq-NFR 映射（1-2天）
6. 执行 Task 5：SysReq → PA 映射（2-3天）
7. 执行 Task 6：端到端追溯分析（1-2天）

**关键文档**：
- [Task 1 README](../01-normalization/README.md)
- [Task 2 README](../02-sr-ba-design/README.md)
- [Task 3 README](../03-ba-sysreq-design/README.md)
- [Task 4 README](../04-sr-nfr-design/README.md)
- [Task 5 README](../05-sysreq-pa-design/README.md)
- [Task 6 README](../06-traceability-analysis/README.md)

---

### 场景2：修改已有的相关方需求

**时间**：1-3天

**步骤**：
1. 业务部门提出修改需求
2. 评估影响范围（涉及哪些任务）
3. 更新相关任务的输出文档
4. 更新映射关系
5. 执行 Task 6：端到端追溯分析
6. 更新 changelog.md

**关键工具**：
- 影响分析：`python 07-shared-assets/tools/generate-report.py --project <name> --report impact`

---

### 场景3：验证映射关系的完整性

**时间**：30分钟

**步骤**：
```bash
# 验证所有映射关系
python 07-shared-assets/tools/validate.py --project <name> --check all

# 生成追溯矩阵报告
python 07-shared-assets/tools/generate-report.py --project <name> --report traceability

# 生成项目汇总报告
python 07-shared-assets/tools/generate-report.py --project <name> --report summary
```

---

## 四、关键概念速查

### 相关方需求 (SR)
- **定义**：来自企业各业务部门对信息系统的需求
- **格式**：SR-F-XXX（功能）或 SR-NF-XXX（非功能）
- **末级节点**：能够映射到业务架构的原子需求

### 业务架构 (BA)
- **定义**：从用户视角描述业务流程的架构
- **层级**：0-5级，其中5级是承接层
- **承接层**：业务组件或配置业务

### 系统需求 (SysReq)
- **定义**：从系统视角描述功能和约束的需求规格
- **层级**：0-9级，其中5级是承接层
- **承接层**：组件实例

### 产品架构 (PA)
- **定义**：从产品视角描述实现方案的架构
- **末级节点**：前后端组件

### 两轨模型
- **功能需求**：SR → BA → SysReq → PA
- **非功能需求**：SR → 非功能需求架构 → 系统约束 → PA约束

### 两阶段工作流
- **第一阶段**：占位符创建（1-2小时）
- **第二阶段**：具体设计（2-6天）

---

## 五、常见问题

### Q1：我是新手，应该从哪里开始？

**A**：
1. 阅读本指南（5分钟）
2. 根据你的角色，阅读对应的准则（30分钟）
3. 查看示例项目 `03-products/projects/project-a/`（30分钟）
4. 开始实践

### Q2：需求规范化需要多长时间？

**A**：通常 1-2 小时，取决于需求的复杂度。使用自动化工具可以加快速度。

### Q3：占位符创建和具体设计可以并行吗？

**A**：可以。占位符创建完成后，下游团队可以立即开始创建下一层级的占位符，而上游团队继续进行具体设计。

### Q4：如何处理需求变更？

**A**：
1. 评估影响范围
2. 更新相关文档
3. 更新映射关系
4. 记录到 changelog.md
5. 更新版本号

### Q5：如何验证映射关系的正确性？

**A**：使用验证工具：
```bash
python 02-pipeline/tools/validate.py --project <name> --check all
```

---

## 六、相关资源

### 📚 核心文档
- [CLAUDE.md](../CLAUDE.md) - 项目总体指导
- [相关方需求文档](pipeline-stakeholder-requirements.md) - 完整的需求定义

### 📋 6 个核心任务
- [Task 1：需求规范化](../01-normalization/README.md)
- [Task 2：SR → BA 映射](../02-sr-ba-design/README.md)
- [Task 3：BA → SysReq 映射](../03-ba-sysreq-design/README.md)
- [Task 4：SR-NFR → SysReq-NFR 映射](../04-sr-nfr-design/README.md)
- [Task 5：SysReq → PA 映射](../05-sysreq-pa-design/README.md)
- [Task 6：端到端追溯分析](../06-traceability-analysis/README.md)

### 🔧 工具脚本
- [验证工具](../07-shared-assets/tools/validate.py)
- [报告生成工具](../07-shared-assets/tools/generate-report.py)

### 📖 示例项目
- [Project-A](../08-products/projects/project-a/)

### 🎯 共享资产
- [业务模式库](../07-shared-assets/patterns/business-patterns.md)
- [质量检查清单](../07-shared-assets/quality-standards/quality-checklist.md)

---

## 七、获取帮助

### 遇到问题？

1. **查看常见问题**：本指南的第五部分
2. **查看相关准则**：根据你的任务查看对应的准则文档
3. **查看示例项目**：参考 `03-products/projects/project-a/` 中的实际例子
4. **联系团队**：向你的团队负责人或架构师咨询

---

**最后更新**：2026-05-12  
**版本**：v1.0
