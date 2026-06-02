# 通用标准指南（General Standards）

本目录存放与特定产品（Pipeline / EOS）**无关**的通用准则、指南和规范，即抽象于具体产品之上、可被任何采用本方法论的产品参考的方法论基础内容。

## 文件清单

| 文件 | 内容 | 说明 |
|------|------|------|
| `01-general-sysdev-spec.md` | **通用系统设计规范**（合并版） | 第一部分（§一~§八）：五层结构方法论核心、基本术语、核心规则、验收标准、检查清单；第二部分（§九~§十二 + 附录）：四种设计模式的操作框架 |
| `03-document-authoring-conventions.md` | 文档编写约定 | 规范文档的统一风格、结构和格式约定 |
| `04-general-terminology-glossary.md` | 通用术语对照（v2.0） | 核心术语英中对照（11个分类） |

> **合并说明**：原 `01-general-sysdev-standards.md`（设计准则）和 `02-general-sysdev-4modes-guide.md`（4模式指南）已合并为 `01-general-sysdev-spec.md`。旧文档已归档至 `90-hold/00-archived-spec-docs/general/`。

## 与产品目录的关系

```
00-generalspec/                 # 通用方法论基础（产品无关）
    01/03/04 文件

10-pl4pleos/                    # 元流水线：参考通用规范，按流水线场景适配
    └── 规范/指南/AI辅助/产品数据

20-pl4eos/                      # EOS 开发空间（含 EOS 流水线构件）：参考通用规范，按 EOS 领域适配
    └── 规范/指南/AI辅助/产品数据
```

> **原则**：通用内容下沉到 `00-generalspec/`，产品内容在各产品目录中独立维护。
> 各产品目录通过「参考」（reference）的方式使用通用规范，而非直接共享文件。
