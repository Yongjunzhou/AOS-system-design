---
name: feedback-global-replace-new-passages-only
description: 全局替换类脚本只对新增段落做，不再全库扫——会误伤"源文本就用该写法"的地方
metadata:
  type: feedback
---

**全局文本替换（引号归一、标点统一、术语换名等）只对本次新增的段落执行，不再对全文件／全库扫描重跑。**

**Why:** ISO 9000:2026 中英对照版会话中，同一个坑踩了两次——全库引号归一两次都改到了"英文原文的那一行"：源文 `This document (EN ISO 9000:2026) has been prepared by Technical Committee ISO/TC 176 "Quality management and quality assurance" …` 此处**源文自己就用直引号**，归一成弯引号即破坏了"英文逐字照录"这条底线。两次都是靠事后保真比对才发现。

**How to apply:**
- 新写的段落，**落笔时直接用目标写法**（如弯引号 `“”`），不要事后靠全局转换补救。
- 必须批量处理时，**限定行范围或限定新增内容**，并对"源文原样"区域（英文原文行、代码块、mermaid 块）设白名单排除。
- 任何批量替换后**必须跑一次保真比对**：源文实质行 × 译本逐字命中，确认零新增偏差（本会话的判据：源文 L80+ 实质行未命中恒为 6 处——附录 A 的 Key 4 行已合并、§4.4.3 源文自身断行 2 行，均属有意改动）。

**相关**：[[feedback-yizhu-editorial-rule]]。
