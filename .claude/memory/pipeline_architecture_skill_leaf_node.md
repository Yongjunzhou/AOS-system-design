---
name: ai-skill-product-architecture
description: AI Skill 产品形态的架构模式——PA 末级节点为 Skill（加工单元）。此为四种产品形态之一，非通用模式
metadata:
  type: project
---

> **注意**：本记忆已被 [product-classification-framework](product_classification_framework.md) 覆盖部分结论。当前的有效范围：**AI Skill 产品形态**的架构模式，而非"流水线类产品的统一模式"。流水线类产品可以是 AI Skill、软件、实物等多种形态，各有不同 PA 节点。

## AI Skill 产品形态的架构

```
流水线（Pipeline）
└── 子流水线（Sub-pipeline）──按产出阶段分组
    └── Skill ──架构末级节点，每个 Skill 对应
        ├── 一种输入（前一工序的产物）
        ├── 一道加工逻辑（AI 执行）
        └── 一种输出（一份标准文档/产物）
```

## 关键要点

1. **Skill 是架构末级节点**，不是软件引擎、管理器、编辑器等。每个 Skill 是一个完整的加工工序，边界 = 一种产出类型的全生命周期。

2. **子流水线的编排 = 流程本身**。子线的先后顺序就是工序流程，不是功能分类的静态分组。

3. **执行主体 = AI**。这是 AI Skill 产品与服务（知识/方法）产品的根本区别——后者执行主体是人，PA 节点是流程模板/工作准则等。

4. **系统设计规范是设计描述（Design Description）**，不是构件也不是需求。

## 设计线 Skill 示例

```
设计线（子流水线）
├── 原始需求分析 Skill              ──→ OR
├── 相关方需求架构定义 Skill        ──→ SR
├── 业务架构定义 Skill              ──→ BA
├── 系统功能需求架构定义 Skill      ──→ SysReq-F
├── 系统非功能需求架构定义 Skill    ──→ SysReq-NF
├── 产品架构定义 Skill              ──→ PA
└── 追溯验证 Skill                  ──→ 追溯矩阵 + 验证报告
```

## 应用范围

适用于：A1 元流水线、A2 EOS 流水线（均为 AI Skill 形态的流水线产品）
不适用于：A3 EOS（软件形态的流水线产品，PA 节点为软件组件）
