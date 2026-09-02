// book.typ — 《架构师是个怎样的物种？》A5 书模板
//
// 由 pandoc（markdown→typst）产出的各章 .typ 被 #include 进来，
// 本模板负责全部版式：A5 页面/页眉页脚/字体/标题/表格/引用/ASCII 盒/图。
// 图宽由 build/fix-typ.mjs 按 viewBox 注入（适配 A5 版心，防溢出）。

#let accent = rgb("#A63D2F")
#let SERIF = ("Noto Serif SC", "SimSun")
#let SANS = ("Noto Sans SC", "SimHei", "Microsoft YaHei")

#let book(book-title: "", body) = {
  set document(title: book-title)

  set page(
    paper: "a5",                                  // 148×210mm
    margin: (x: 19mm, top: 18mm, bottom: 20mm),   // 版心 110×172mm
    header: context {
      // 页眉 = 当前页所属章名（最近的前置一级标题；每章起新页，按页码判定）；封面页（第1页）不显示
      if counter(page).get().first() != 1 {
        let cur = here().page()
        let ch = query(heading.where(level: 1)).rev().find(h => h.location().page() <= cur)
        if ch != none {
          set text(size: 8pt, font: SANS, fill: luma(140))
          align(center)[#ch.body]
        }
      }
    },
    footer: context {
      if counter(page).get().first() != 1 {
        set text(size: 9pt, font: SANS)
        align(center)[#counter(page).display()]
      }
    },
  )

  // 中文正文：思源宋体、五号（10.5pt）、两端对齐、1.6 倍行距、段首两字缩进、段间小幅留白
  set text(font: SERIF, size: 10.5pt, lang: "zh", region: "cn")
  set par(justify: true, leading: 1.6em, spacing: 0.3em, first-line-indent: 2em)
  set heading(numbering: none)                     // 编号已内嵌在标题文本（范式丙）
  show list: set par(first-line-indent: 0em)       // 列表段不缩进
  show enum: set par(first-line-indent: 0em)       // 有序列表段不缩进
  show quote: set par(first-line-indent: 0em)      // 引用块不缩进

  show strong: set text(weight: 700)               // 思源可变字体原生加粗

  // 标题：思源黑体，按层级缩放；章级起新页
  show heading.where(level: 1): it => pagebreak(weak: true) + it
  show heading.where(level: 1): set text(font: SANS, size: 20pt, weight: 700)
  show heading.where(level: 2): set text(font: SANS, size: 14pt, weight: 700)
  show heading.where(level: 3): set text(font: SANS, size: 12pt, weight: 700)
  show heading.where(level: 4): set text(font: SANS, size: 10.5pt, weight: 700)

  // 引用块（章首导语 + 概念卡）：朱红左竖线
  show quote: it => block(
    width: 100%,
    stroke: (left: 2pt + accent),
    inset: (left: 1em, top: .3em, bottom: .3em),
    it,
  )

  // 表格：9pt 小字防溢出；列宽/对齐沿用 pandoc 默认（auto），整体居中由 figure 负责
  show table: set text(size: 9pt)
  show table.header: set text(weight: 700)
  show table.cell: set block(inset: (x: 2pt, y: 1.5pt))

  // 裸围栏 ASCII 概念档案：NSimSun 保证 box-drawing（┌─│┐）与 ASCII 同格宽对齐
  show raw: set text(font: ("NSimSun", "SimSun", "DejaVu Sans Mono"), size: 8.5pt)
  show raw: set block(fill: none, inset: 0pt, radius: 0pt, stroke: none)

  // 图：居中；宽度由 fix-typ.mjs 注入
  show figure: it => align(center, it)
  show figure.caption: set text(size: 9pt, fill: luma(120))
  show figure.caption: set par(first-line-indent: 0em)

  body
}
