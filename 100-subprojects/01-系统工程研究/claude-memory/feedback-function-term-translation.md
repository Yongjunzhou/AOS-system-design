---
name: feedback-function-term-translation
description: function 在术语位是「功能」，不译「函数」——数学习语 a function of X 改写为「由…决定」
metadata:
  type: feedback
---

用户 2026-09-24 裁定的**术语译名**：

> **function 是功能，不能翻译为函数。**

**Why：** 当轮回答在讲"跳过架构定义对产品结果的影响"时，引了 SEBoK 质量属性知识区的开篇句——`Every system has a set of properties that are largely a function of the system as a whole rather than just its constituent parts.`——并把它译成"每个系统都有一组属性，**主要是整体的函数**，而不只是各组成部分的函数"。用户直接点出：**function 在本领域的术语位是「功能」**。这是引文分寸问题的又一实例（与 [[feedback-quote-original-and-chinese]] 同族）：译名一旦走形，读者无法复核，且会把领域概念（功能）与数学对象（函数）混为一谈。

**How to apply：**

- **术语位（系统工程／架构语境）**：`function` 一律译 **功能**——SEBoK、ISO/IEC/IEEE 15288 的 Function/Functional Architecture、Functional Analysis 等都是此位。与之配套的 `functional requirement` ＝功能需求、`functional architecture` ＝功能架构，不写作"函数需求""函数架构"。
- **英文数学习语 `a function of X`（＝由 X 决定／随 X 而变）不入术语位**：不译"X 的函数"，改写为**「由 X 决定」「随 X 而变」**。上例的正确译法：`…largely a function of the system as a whole rather than just its constituent parts` → **「……在很大程度上由系统整体决定，而不只由各组成部分决定」**。
- **与既有定名的边界（★待裁·见下）**：本仓库另有用户 2026-09-03 定名的 **Y=F(X) 函数法**（20 号报告 H1、教材第 6 章"一个函数，三个动作""函数的单值性"），那里用的是**数学位**（映射、单值性、N:1 约束），不在本条射程内。程序位（代码里的 function，如第 12 章"改一个函数内部的排序算法"、第 8 章"金额校验这个函数"）与数学习语位（第 3 章"质量不是时间的函数"）同理属既有用法。

**★ 待裁（本条适用边界）**：本条是"**术语位 function ＝功能**"的最小解释，据此只需登记一条译名规则，已落地的 Y=F(X) 函数法、教材三处既有"函数"用法**不动**；若用户本意是"全仓库禁用『函数』二字"，则会牵动 20 号报告 H1／摘要／正文（数十处）与教材第 3、6、8、12 章及训侧派生件——须先摆全量清单再动。两种解释在下次涉及该词的会话开工时请用户一句定夺。

**常见违例（见到即改）**：把 SE 语境的 function 译成"函数"／把 `a function of X` 直译"X 的函数"／因本条而顺手改掉数学位与程序位的既有"函数"（越界改动）。

**相关**：[[feedback-quote-original-and-chinese]]（原文＋中译并列，与本条同属译名分寸）、[[feedback-global-replace-new-passages-only]]（改动波及面：本条不在既有文本上做全局替换，除非用户明示）。
