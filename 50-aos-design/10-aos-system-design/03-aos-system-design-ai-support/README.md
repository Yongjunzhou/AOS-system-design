# AOS 系统设计 AI 辅助文档

> 产品B构件：为团队A开展产品A（AOS企业运营体系）的系统设计提供 AI 辅助支持。

本目录包含 AI 在产品A系统设计过程（阶段1）中的工作指令、检查清单和示例文档。

## 目录结构

```
03-aos-system-design-ai-support/
├── 00-overview.md                          # AI 工作文档需求理解确认书
├── 01-product-context-aos.md              # AOS 产品上下文
├── 02-ai-decision-framework-aos.md        # AI 决策框架
├── README.md                               # 本文档
├── 01-waterfall-aos-system-design/        # 场景1：瀑布式 / 新研产品（6步）
│   ├── README.md                          # 场景概述 + Skill 定义
│   ├── workflow-prompts.md                # 提示词模板集
│   ├── product-example.md                 # 产品数据范例
│   └── checklist.md                       # AI 自检清单
├── 03-agile-aos-system-design/            # 场景2：敏捷式 / 增量需求（8步）
│   ├── README.md
│   ├── workflow-prompts.md
│   ├── product-example.md
│   └── checklist.md
├── 02-reverse-engineering-aos-system-design/ # 场景3：逆向工程（8步）
│   ├── README.md
│   ├── workflow-prompts.md
│   ├── product-example.md
│   └── checklist.md
└── 04-devops-aos-system-design/           # 场景4：DevOps / 快速修复（4步/3模式）
    ├── README.md
    ├── workflow-prompts.md
    ├── product-example.md
    └── checklist.md
```

## 文档说明

| 文档 | 说明 |
|------|------|
| `00-overview.md` | AI 工作文档需求理解确认书，定义 AI 辅助文档的编写原则和目录结构 |
| `01-product-context-aos.md` | AOS 产品上下文，描述产品定位、用户画像、设计约束，为 AI 提供统一的产品认知 |
| `02-ai-decision-framework-aos.md` | AI 决策框架，提供分解粒度判断、合并/拆分决策、需求歧义处理等决策规则 |
| `README.md`（各场景） | 场景概述 + Skill 定义，告诉 AI "能否做这个任务" |
| `workflow-prompts.md`（各场景） | 提示词模板集，告诉 AI "每一步具体怎么做" |
| `product-example.md`（各场景） | 产品数据范例，告诉 AI "产出长什么样" |
| `checklist.md`（各场景） | AI 自检清单，告诉 AI "做完后怎么确认" |

## 四种开发场景

| 场景 | 适用情况 | 周期 | 任务数 |
|------|---------|------|--------|
| 瀑布式 | 全新 AOS 系统，需求明确 | 30-48天 | 6 |
| 敏捷式 | AOS 迭代开发，需求渐进 | 13-21天 | 8 |
| 逆向工程 | 已有 AOS 系统补文档 | 16-26天 | 8 |
| DevOps | AOS 小变更快速交付 | 几小时-3天 | 4 |

## 使用方式

AI 在执行为团队A生成系统设计文档的任务时：

1. 首先阅读 `00-overview.md` 和 `01-product-context-aos.md`，建立对文档需求和 AOS 产品的统一认知
2. 遇到设计判断时，查阅 `02-ai-decision-framework-aos.md` 的决策规则
3. 根据当前设计场景，进入对应的场景子目录
4. 阅读场景 `README.md` 确认是否匹配当前任务
5. 按 `workflow-prompts.md` 的步骤使用提示词模板执行
6. 参照 `product-example.md` 的格式产出设计文档
7. 使用 `checklist.md` 自行验证产出质量
