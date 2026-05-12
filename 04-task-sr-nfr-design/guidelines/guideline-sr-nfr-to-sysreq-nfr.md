# 非功能相关方需求设计指南

## 概述

非功能需求是系统级别的需求，与具体的业务组件无关。本指南定义了如何将非功能相关方需求（SR-NFR）映射到系统非功能需求（SysReq-NFR）。

## 关键特点

- **平行体系**：非功能需求采用平行的架构体系，不经过业务架构层
- **直接映射**：SR-NFR直接映射到SysReq-NFR（无中间层）
- **N:1关系**：多条SR-NFR可映射到一个SysReq-NFR 5级节点
- **1:1约束**：每条SR-NFR只能映射到唯一的SysReq-NFR 5级节点

## 非功能需求三大类

### 1. 质量特性需求（Quality Attributes）
- 性能需求（Performance）
- 可靠性需求（Reliability）
- 安全性需求（Security）
- 可用性需求（Availability）
- 可维护性需求（Maintainability）

### 2. 环境适应性需求（Environmental Adaptation）
- 兼容性需求（Compatibility）
- 可扩展性需求（Scalability）
- 可移植性需求（Portability）
- 集成适应性需求（Integration Adaptability）

### 3. 可实现性需求（Implementability）
- 可生产性需求（Producibility）
- 可测试性需求（Testability）
- 可交付性需求（Deliverability）
- 可部署性需求（Deployability）
- 可操作性需求（Operability）
- 可运维性需求（Maintainability in Operations）
- 可退役性需求（Retirability）

## 映射步骤

### 步骤1：分析SR-NFR
- 理解每条非功能相关方需求
- 识别需求的类别和类型
- 确定需求的优先级

### 步骤2：分类和组织
- 将SR-NFR按照三大类进行分类
- 在每个类别下进行进一步分类
- 识别相关的SR-NFR

### 步骤3：定义SysReq-NFR 5级节点
- 为每个SR-NFR定义对应的SysReq-NFR 5级节点
- 明确节点的名称和职责
- 定义量化指标和验证方法

### 步骤4：建立映射关系
- 记录SR-NFR → SysReq-NFR的映射关系
- 确保映射的完整性和一致性
- 标记映射的理由

## 最佳实践

1. **量化指标**：每个SysReq-NFR 5级节点都应该有明确的量化指标
2. **验证方法**：每个SysReq-NFR 5级节点都应该有明确的验证方法
3. **完整性**：确保所有SR-NFR都被映射
4. **一致性**：确保映射关系的一致性
5. **可追溯性**：保持SR-NFR和SysReq-NFR之间的可追溯性

## 常见问题

**Q：非功能需求为什么不经过业务架构层？**
A：非功能需求是系统级别的需求，与具体的业务组件无关。它们直接从相关方需求映射到系统需求，形成平行的体系。

**Q：如何定义非功能需求的量化指标？**
A：量化指标应该是可测量、可验证的。例如：响应时间 < 200ms、系统可用性 > 99.9%。

**Q：一个SR-NFR可以映射到多个SysReq-NFR 5级节点吗？**
A：不可以。每条SR-NFR只能映射到唯一的SysReq-NFR 5级节点（1:1约束）。但一个SysReq-NFR 5级节点可以承接多条SR-NFR（N:1关系）。
