# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AOS（Architecture & Orchestration System）是一个系统设计治理项目，核心目标是将企业系统设计流程标准化、资产化、自动化。它定义了从「相关方需求」到「产品架构」的完整四层设计链路，并通过 AI Skill 实现流程自动化。

## Core Architecture: 四层映射模型

```
相关方需求 (SR) ──N:1──→ 业务架构 (BA) ──N:1──→ 系统需求 (SysReq) ──N:1──→ 产品架构 (PA)
```

- **N:1 多对一映射**：多条下层需求映射到唯一的上层承接节点
- **1:1 约束**：每条需求只能分配到唯一的承接点
- **语义覆盖**：上层节点的内容必须完整覆盖分配到它的所有下层需求

## 4 条核心设计准则

| 准则 | 内容 | 对应文件 |
|------|------|----------|
| 准则 1 | 需求规范化、分解、初步 BA 设计、冲突/重复检测、分类确认 | `01-standards/guidelines/guideline-1-normalization.md` |
| 准则 2 | SR → BA 映射（N:1 分配） | `01-standards/guidelines/guideline-2-sr-to-ba-mapping.md` |
| 准则 3 | BA → SysReq 映射（N:1 分配） | `01-standards/guidelines/guideline-3-ba-to-sr-mapping.md` |
| 准则 4 | SysReq → PA 映射（N:1 分配） | `01-standards/guidelines/guideline-4-sr-to-pa-mapping.md` |

## 9 个 AI Skill（自动化资产）

按处理流程排列：`requirement-normalization` → `requirement-decomposition` → `conflict-detection` → `duplicate-detection` → `business-pattern-matching` → `architecture-pattern-matching` → `sr-to-ba-mapping` → `ba-to-sr-mapping` → `sr-to-pa-mapping`

所有 Skill 定义位于 `02-pipeline/skills/`，每个 Skill 描述特定任务的输入、输出和处理步骤。

## 新增需求处理流程（12 步）

1. 收集原始需求
2. 规范化 + 分解（调用 Skill）
3. 冲突检测（调用 Skill）
4. 重复检测（调用 Skill）
5. 分类和建议
6. 人工确认
7. SR ↔ BA 同步设计（调用 Skill，满足准则 2）
8. BA ↔ SysReq 同步设计（调用 Skill，满足准则 3）
9. SysReq ↔ PA 同步设计（调用 Skill，满足准则 4）
10. 验证映射关系
11. 更新映射矩阵
12. 更新版本日志

详见 `02-pipeline/workflows.md`。

## Key Commands

```bash
# 验证项目映射关系
python 02-pipeline/tools/validate.py --project <project-name> --check all

# 生成追溯矩阵报告
python 02-pipeline/tools/generate-report.py --project <project-name> --report traceability

# 生成项目汇总报告
python 02-pipeline/tools/generate-report.py --project <project-name> --report summary
```

## Project Structure

```
01-standards/        # 组织资产：4 条准则 + 4 个模板 + 3 个模式库
02-pipeline/         # 自动化资产：9 个 Skill + 2 个工具脚本 + 工作流定义
03-products/         # 产品数据：按项目组织的设计文档
.claude/             # Claude Code 配置
```

每个项目目录（`03-products/projects/<project-name>/`）包含 7 个文件：
`requirements.md`、`business-architecture.md`、`system-requirements.md`、`product-architecture.md`、`analysis.md`（需求分析核心）、`mappings.md`（映射矩阵核心）、`changelog.md`。

## 关键设计文件

- `02-pipeline/workflows.md` — 12 步新增需求处理流程（触发所有工作的总入口）
- `01-standards/guidelines/README.md` — 4 条准则总览
- `03-products/projects/<name>/analysis.md` — ★ 原始需求→规范化→分解→确认的完整链路
- `03-products/projects/<name>/mappings.md` — ★ SR→BA→SysReq→PA 的 N:1 映射关系

## 文档规范

- 所有文档使用 Markdown + Mermaid 格式
- 版本号格式：`v[主版本].[次版本]`
- 变更记录统一写入 `changelog.md`
