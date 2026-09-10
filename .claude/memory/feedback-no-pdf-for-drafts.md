---
name: feedback-no-pdf-for-drafts
description: 研究报告/草案类文档先只出 md，不要急着转 PDF（定稿后再转）
metadata:
  type: feedback
---

**研究报告与草案类文档，先只产出 `.md`，不要顺手生成 PDF**（2026-09-10 人类就在 95 号报告生成 PDF 后立即指示"不要生成 PDF，先 md"）。

**Why**：这类文档还在来回打磨，每次改动都重跑 md2pdf 是浪费（渲染耗时、且生成的 PDF 很快作废）；PDF 是定稿产物，出早了只会积累废件。

**How to apply**：新写/大改研究报告、草案、待审议的文档时，只交付 md，等人类说"定稿/转 PDF"再跑 `tools/md2pdf/md2pdf.js`。已定稿文档的**内容修改**仍按惯例同步重生成其 PDF（如 91/94 这类已有 PDF 的规范文档），本约定针对的是"新稿/草稿"。

关联 [[95-product-data-itemization-tree-allocation-report]]。
