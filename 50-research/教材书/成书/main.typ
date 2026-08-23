// main.typ — 《架构师是个怎样的物种？》PDF 入口（位于 成书/ 根，路径相对根解析）
// 组装：封面 → 版权页 → 序言 → 前言 → 目录 → 第1~16章 → 附录 → 封底占位
#import "template/book.typ": book, SANS

#show: book.with(book-title: "架构师是个怎样的物种？——从工程师到架构师")

// ── 封面页（全页图，A5 148×210 恰好贴合 800×1132 前封比例）──
#set page(margin: 0pt)
#align(center + horizon, image("build/assets/cover-800x1132.png", width: 148mm, height: 210mm))
#pagebreak()

// ── 版权页占位 ──
#set page(margin: (x: 19mm, top: 18mm, bottom: 20mm))
#align(center)[
  #v(6cm)
  #text(font: SANS, size: 16pt, weight: 700)[架构师是个怎样的物种？]
  #v(.6cm)
  #text(size: 11pt)[——从工程师到架构师]
  #v(3cm)
  #text(size: 10pt)[著：周拥军] \
  #text(size: 10pt)[2026 年 8 月] \
  #v(2cm)
  #text(size: 9pt, fill: luma(140))[自出版 · EPUB / A5 打印稿] \
  #text(size: 9pt, fill: luma(140))[ISBN：—（待定）]
]
#pagebreak(weak: true)

// ── 序言 / 前言 ──
#include "build/00-序言.typ"
#include "build/00-前言.typ"

// ── 目录（outline 自动生成，页码回填；outlined:false 的章首/章末件已排除）──
#pagebreak(weak: true)
#outline(title: "目录", depth: 3)
#pagebreak(weak: true)

// ── 正文章节 ──
#include "build/01-第1章.typ"
#include "build/02-第2章.typ"
#include "build/03-第3章.typ"
#include "build/04-第4章.typ"
#include "build/05-第5章.typ"
#include "build/06-第6章.typ"
#include "build/07-第7章.typ"
#include "build/08-第8章.typ"
#include "build/09-第9章.typ"
#include "build/10-第10章.typ"
#include "build/11-第11章.typ"
#include "build/12-第12章.typ"
#include "build/13-第13章.typ"
#include "build/14-第14章.typ"
#include "build/15-第15章.typ"
#include "build/17-附录.typ"

// ── 封底占位 ──
#pagebreak(weak: true)
#align(bottom + center)[
  #text(size: 9pt, fill: luma(150))[
    把那些你天天挂在嘴边、却从没真正想清楚的词，放到你有把握判定的位置。
  ]
]
