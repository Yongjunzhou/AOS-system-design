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

## 二、我是...我应该做什么？

### 👤 业务部门（需求提出方）

**你的任务**：提出清晰的相关方需求

**快速步骤**：
1. 阅读 [需求规范化指南](../01-standards/guidelines/guideline-1-normalization.md#二规范化规则)
2. 按照模板填写需求（参考 [相关方需求模板](../01-standards/templates/stakeholder-requirements-template.md)）
3. 提交给企业架构团队进行规范化处理

**关键点**：
- 需求要清晰、具体、可测量
- 区分功能需求（做什么）和非功能需求（如何做）
- 提供背景和原因

---

### 👨‍💼 企业架构团队

**你的任务**：规范化需求，设计业务架构

**快速步骤**：

#### 第1步：规范化和分解需求（1-2小时）
```
原始需求 
  → 检查完整性（9个必填字段）
  → 分解为原子需求
  → 冲突检测
  → 重复检测
  → 分类确认
```

参考：[准则1：需求规范化](../01-standards/guidelines/guideline-1-normalization.md)

#### 第2步：创建业务架构占位符（1-2小时）
```
规范化的需求
  → 快速扫描末级节点
  → 创建BA占位符
  → 建立映射表
  → 冻结占位符结构
```

参考：[占位符规范](../01-standards/guidelines/guideline-placeholder.md)

#### 第3步：设计业务架构（2-3天）
```
填充BA占位符
  → 设计业务流程
  → 定义参与角色
  → 标记关键决策点
  → 预留SysReq占位符
```

参考：[准则2：SR→BA映射](../01-standards/guidelines/guideline-2-sr-to-ba-mapping.md)

**关键工具**：
- 模板：[业务架构模板](../01-standards/templates/business-architecture-template.md)
- 验证：`python 02-pipeline/tools/validate.py --project <name> --check ba`

---

### 🏗️ 系统设计团队

**你的任务**：设计系统需求和产品架构

**快速步骤**：

#### 第1步：创建系统需求占位符（1-2小时）
```
业务架构
  → 快速扫描BA承接点
  → 创建SysReq占位符
  → 建立映射表
  → 冻结占位符结构
```

#### 第2步：设计系统需求（2-3天）
```
填充SysReq占位符
  → 设计功能需求
  → 标记非功能约束
  → 预留PA占位符
```

参考：[准则3：BA→SysReq映射](../01-standards/guidelines/guideline-3-ba-to-sr-mapping.md)

#### 第3步：创建产品架构占位符（1-2小时）
```
系统需求
  → 快速扫描SysReq承接点
  → 创建PA占位符
  → 建立映射表
```

#### 第4步：设计产品架构（2-3天）
```
填充PA占位符
  → 设计组件架构
  → 定义组件职责
  → 设计组件通信
```

参考：[准则4：SysReq→PA映射](../01-standards/guidelines/guideline-4-sr-to-pa-mapping.md)

**关键工具**：
- 模板：[系统需求模板](../01-standards/templates/system-requirements-template.md)、[产品架构模板](../01-standards/templates/product-architecture-template.md)
- 验证：`python 02-pipeline/tools/validate.py --project <name> --check all`

---

### 🔍 IT管理部门

**你的任务**：质量检查、版本管理、文档发布

**快速步骤**：

1. **质量检查**
   - 检查所有文档是否符合模板要求
   - 验证映射关系的完整性
   - 生成质量报告

2. **版本管理**
   - 记录所有变更到 `changelog.md`
   - 更新版本号（v1.0 → v1.1）
   - 追踪变更影响范围

3. **文档发布**
   - 审核文档内容
   - 发布到文档库
   - 管理访问权限

**关键工具**：
- 验证：`python 02-pipeline/tools/validate.py --project <name> --check all`
- 报告：`python 02-pipeline/tools/generate-report.py --project <name> --report summary`

---

### 🤖 AI/Skill开发团队

**你的任务**：开发自动化Skill，优化流水线

**快速步骤**：

1. **了解Skill定义**
   - 阅读 [Skill定义文档](../02-pipeline/skills/)
   - 理解输入、输出、处理逻辑

2. **开发核心Skill**
   - requirement-normalization：需求规范化
   - requirement-decomposition：需求分解
   - conflict-detection：冲突检测
   - duplicate-detection：重复检测
   - sr-to-ba-mapping：SR→BA映射
   - ba-to-sr-mapping：BA→SysReq映射
   - sr-to-pa-mapping：SysReq→PA映射

3. **优化提示词**
   - 建立提示词库
   - 优化检测精准度
   - 记录最佳实践

**关键文件**：
- Skill定义：`02-pipeline/skills/*.md`
- 工具脚本：`02-pipeline/tools/*.py`

---

## 三、常见场景

### 场景1：新增一个相关方需求

**时间**：1-2天

**步骤**：
1. 业务部门提出需求
2. 企业架构团队规范化和分解（1-2小时）
3. 企业架构团队创建BA占位符（1-2小时）
4. 企业架构团队设计BA（1-2天）
5. 系统设计团队创建SysReq占位符（1-2小时）
6. 系统设计团队设计SysReq（1-2天）
7. 系统设计团队创建PA占位符（1-2小时）
8. 系统设计团队设计PA（1-2天）
9. IT管理部门质量检查和发布

**关键文档**：
- [准则1](../01-standards/guidelines/guideline-1-normalization.md)
- [准则2](../01-standards/guidelines/guideline-2-sr-to-ba-mapping.md)
- [准则3](../01-standards/guidelines/guideline-3-ba-to-sr-mapping.md)
- [准则4](../01-standards/guidelines/guideline-4-sr-to-pa-mapping.md)

---

### 场景2：修改已有的相关方需求

**时间**：1-3天

**步骤**：
1. 业务部门提出修改需求
2. 企业架构团队评估影响范围
3. 更新相关的BA、SysReq、PA文档
4. 更新映射关系
5. 更新changelog.md
6. IT管理部门质量检查和发布

**关键工具**：
- 影响分析：`python 02-pipeline/tools/generate-report.py --project <name> --report impact`

---

### 场景3：验证映射关系的完整性

**时间**：30分钟

**步骤**：
```bash
# 验证所有映射关系
python 02-pipeline/tools/validate.py --project <name> --check all

# 生成追溯矩阵报告
python 02-pipeline/tools/generate-report.py --project <name> --report traceability

# 生成项目汇总报告
python 02-pipeline/tools/generate-report.py --project <name> --report summary
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
- [准则总览](../01-standards/guidelines/README.md) - 5条核心准则

### 📋 模板库
- [相关方需求模板](../01-standards/templates/stakeholder-requirements-template.md)
- [业务架构模板](../01-standards/templates/business-architecture-template.md)
- [系统需求模板](../01-standards/templates/system-requirements-template.md)
- [产品架构模板](../01-standards/templates/product-architecture-template.md)

### 🔧 工具脚本
- [验证工具](../02-pipeline/tools/validate.py)
- [报告生成工具](../02-pipeline/tools/generate-report.py)

### 📖 示例项目
- [Project-A](../03-products/projects/project-a/)

### 🎯 工作流程
- [新增需求处理流程](../02-pipeline/workflows.md)

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
