# Task 4：非功能相关方需求设计 + 系统非功能需求架构设计

## 任务概述

将非功能相关方需求（SR-NFR）直接映射到系统非功能需求（SysReq-NFR），完成SysReq-NFR 0-5级的设计。这是非功能需求的平行体系。

**目标**：建立清晰的SR-NFR → SysReq-NFR映射关系，定义系统非功能需求的完整架构

## 输入和输出

| 项目 | 内容 |
|------|------|
| **输入** | `sr-nfr.md`（来自Task 1） |
| **输出** | `sysreq-nfr.md`（SysReq-NFR 0-5级完整结构）<br>`sr-nfr-to-sysreq-nfr-mapping.md`（映射矩阵） |
| **占位符** | 为SysReq-NFR 5级节点预留PA权衡关系 |

## 快速开始（5分钟）

1. **阅读指南**：[guideline-sr-nfr-to-sysreq-nfr.md](guidelines/guideline-sr-nfr-to-sysreq-nfr.md)
2. **查看模板**：[sysreq-nfr-template.md](templates/sysreq-nfr-template.md)
3. **查看示例**：[sr-nfr-design-example.md](examples/sr-nfr-design-example.md)
4. **使用检查清单**：[sr-nfr-design-checklist.md](checklists/sr-nfr-design-checklist.md)

## 关键活动

### 1. SR-NFR → SysReq-NFR映射
- 将非功能相关方需求映射到系统非功能需求
- 建立N:1映射关系（多条SR-NFR可映射到一个SysReq-NFR 5级节点）

**Skill**：[sr-nfr-to-sysreq-nfr-mapping.md](skills/sr-nfr-to-sysreq-nfr-mapping.md)

### 2. SysReq-NFR 5级节点定义
- 定义非功能需求承接层（SysReq-NFR 5级）
- 明确每个非功能需求的量化指标和验证方法

### 3. 非功能需求分类
- 质量特性需求（Performance, Reliability, Security, Availability, Maintainability）
- 环境适应性需求（Compatibility, Scalability, Portability, Integration Adaptability）
- 可实现性需求（Producibility, Testability, Deliverability, Deployability, Operability, Maintainability in Operations, Retirability）

## 工作流

详见 [task-4-workflow.md](workflows/task-4-workflow.md)

**关键步骤**：
1. 分析非功能相关方需求
2. 创建非功能需求根节点（SysReq-NFR 0级）
3. 分类需求类别（SysReq-NFR 1级）
4. 定义需求类型（SysReq-NFR 2级）
5. 定义需求子类型（SysReq-NFR 3级）
6. 细分需求（SysReq-NFR 4级）
7. 定义非功能需求承接层（SysReq-NFR 5级）
8. 建立SR-NFR → SysReq-NFR映射
9. 验证映射完整性
10. 标记占位符
11. 交付检查

## 输出文件结构

```
08-products/projects/<project-name>/04-sr-nfr-design/
├── sysreq-nfr.md                # SysReq-NFR 0-5级完整结构（输出）
├── sr-nfr-to-sysreq-nfr-mapping.md  # SR-NFR → SysReq-NFR映射矩阵（输出）
└── sysreq-nfr-design-notes.md   # 设计过程中的注记
```

## SysReq-NFR层级结构

| 层级 | 名称 | 说明 |
|------|------|------|
| 0级 | 非功能需求根节点 | 整个系统的非功能需求顶层根节点 |
| 1级 | 需求类别 | 三大类：质量特性需求、环境适应性需求、可实现性需求 |
| 2级 | 需求类型 | 具体类型（如：性能、安全、可测试性、可部署性等） |
| 3级 | 需求子类型 | 子类型（如：响应时间、吞吐量、数据加密、自动化部署等） |
| 4级 | 需求细分 | 对第3级的更细分类 |
| **5级** | **非功能需求承接层** | **★ 承接相关方非功能需求的关键层级**<br>- 具体的需求名称<br>- 需求描述<br>- 量化指标定义<br>- 验证方法 |

## 非功能需求三大类

### 1. 质量特性需求（Quality Attributes）
- **性能需求（Performance）**：响应时间、吞吐量、资源利用率
- **可靠性需求（Reliability）**：故障率、平均无故障时间（MTBF）
- **安全性需求（Security）**：数据加密、访问控制、审计日志
- **可用性需求（Availability）**：系统可用性、故障恢复时间（RTO）
- **可维护性需求（Maintainability）**：代码可读性、文档完整性

### 2. 环境适应性需求（Environmental Adaptation）
- **兼容性需求（Compatibility）**：浏览器兼容性、操作系统兼容性
- **可扩展性需求（Scalability）**：水平扩展、垂直扩展
- **可移植性需求（Portability）**：跨平台支持、容器化部署
- **集成适应性需求（Integration Adaptability）**：第三方系统集成、API兼容性

### 3. 可实现性需求（Implementability）
- **可生产性需求（Producibility）**：开发效率、代码质量
- **可测试性需求（Testability）**：单元测试覆盖率、集成测试覆盖率
- **可交付性需求（Deliverability）**：发布流程、版本管理
- **可部署性需求（Deployability）**：自动化部署、蓝绿部署
- **可操作性需求（Operability）**：监控告警、日志收集
- **可运维性需求（Maintainability in Operations）**：故障诊断、性能调优
- **可退役性需求（Retirability）**：数据迁移、系统下线

## 检查清单

完成Task 4前，请使用 [sr-nfr-design-checklist.md](checklists/sr-nfr-design-checklist.md) 进行检查：

- [ ] 所有非功能相关方需求都已分析
- [ ] 需求类别分类合理（质量特性、环境适应性、可实现性）
- [ ] 需求类型定义清晰
- [ ] 需求子类型定义完整
- [ ] 需求细分合理
- [ ] 非功能需求承接层（SysReq-NFR 5级）定义明确
- [ ] 每个SysReq-NFR 5级节点都有量化指标
- [ ] 每个SysReq-NFR 5级节点都有验证方法
- [ ] SR-NFR → SysReq-NFR映射完整（每条SR-NFR都映射到至少一个SysReq-NFR 5级节点）
- [ ] 占位符已标记
- [ ] 版本号已更新

## 常见问题

**Q：非功能需求为什么不经过业务架构层？**
A：非功能需求是系统级别的需求，与具体的业务组件无关。它们直接从相关方需求映射到系统需求，形成平行的体系。

**Q：如何定义非功能需求的量化指标？**
A：量化指标应该是可测量、可验证的。例如：响应时间 < 200ms、系统可用性 > 99.9%。详见 [sysreq-nfr-template.md](templates/sysreq-nfr-template.md)

**Q：一个SR-NFR可以映射到多个SysReq-NFR 5级节点吗？**
A：不可以。每条SR-NFR只能映射到唯一的SysReq-NFR 5级节点（1:1约束）。但一个SysReq-NFR 5级节点可以承接多条SR-NFR（N:1关系）。

## 相关资源

- **质量检查清单**：[07-shared-assets/quality-standards/quality-checklist.md](../07-shared-assets/quality-standards/quality-checklist.md)
- **设计决策模板**：[07-shared-assets/quality-standards/design-decision-template.md](../07-shared-assets/quality-standards/design-decision-template.md)
- **前置任务**：[Task 1：新增原始需求规范化](../01-task-normalization/README.md)
- **后续任务**：[Task 5：系统需求设计 + 产品架构设计](../05-task-sysreq-pa-design/README.md)

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-05-12 | 初始版本 |
