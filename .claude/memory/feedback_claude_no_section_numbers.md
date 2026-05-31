---
name: claude-md
description: CLAUDE.md 保持层级标题格式，不增加章节编号
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 821932d6-dd45-456c-85f4-e0e3230cd701
---

CLAUDE.md 使用 `##` / `###` / `####` 层级标题即可，不添加数字章节号（如 §1、1.1）。

**Why:** CLAUDE.md 是指导性文档而非规范文件，频繁更新时维护编号成本高，且三层标题已足够清晰。正式章节号只用于规范文档（如通用准则的 §1.7.4）。

**How to apply:** 编辑 CLAUDE.md 时只使用 markdown 层级标题，不添加数字编号。引用时使用标题名称（如"项目概览中..."）而非编号。
