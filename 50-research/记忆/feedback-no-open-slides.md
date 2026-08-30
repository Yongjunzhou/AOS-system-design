---
name: feedback-no-open-slides
description: 修改幻灯片（pptx/key）时不要再打开它们（不弹 Keynote 窗口、不做打开导出的渲染验证），需要时用户自己打开查看
metadata:
  type: feedback
---

修改幻灯片（流程工程师培训 01 课件/答题版等）时，**不要打开幻灯片文件**：不 `activate`/`open` Keynote，不做「打开→导出 PDF→核对」的渲染验证。内容正确性改以**直接解析 pptx 内部 XML**（`ppt/slides/slideN.xml` 的 `<a:t>` 文本）核对。2026-08-30 用户定。

**Why:** 每轮改动反复打开 Keynote 会弹窗抢焦点、打断用户；渲染验证的多次导出也属多余。用户表示需要查看时会自己打开。

**How to apply:** 内容变更后只重新生成 `.pptx`；核对文字用 zipfile 读 pptx XML 即可。**`.key` 需要 Keynote 打开另存才能生成**——若用户要求继续产出 `.key`，须先获得许可并安静执行（不 activate）；否则只交付 `.pptx`，`.key` 由用户在 Keynote 里自行打开另存。相关：[[feedback-sync-01-concept-md]]。
