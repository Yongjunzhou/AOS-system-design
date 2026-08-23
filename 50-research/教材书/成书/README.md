# 成书（教材书 → EPUB + PDF 双轨构建）

`50-research/教材书/` 的 Markdown 教材书《架构师是个怎样的物种？——从工程师到架构师》转为双轨成品的构建管道。**源 `.md` 零改动**，全部构建产物在本目录。

## 产物

| 文件 | 说明 |
|---|---|
| `架构师-打印版.pdf` | A5 打印稿（实体书版式：封面/版权页/目录/页眉页码/正文宋体） |
| `架构师-电子版.epub` | 电子书（微信读书 / Apple Books / 多看等，重排版式） |

## 重建

```bash
bash build.sh        # 增量：mermaid 图已存在则跳过渲染
bash build.sh --rerender   # 强制重渲全部 19 个 mermaid 图
```

一键产出双格式。命令内部自行设置工具 PATH，无需额外环境变量。

## 目录结构

```
成书/
  build.sh             # 单入口（预处理 → 图 → 封面 → pandoc→typst → typst → pandoc→epub）
  main.typ             # PDF 入口：封面/版权/序前/目录/章节/封底组装
  template/book.typ    # A5 版式模板（页面/字体/标题/表格/引用/ASCII 盒/图）
  build/
    preprocess.mjs     # 清洗：剔「版本变更记录」/ mermaid 提取 / .unlisted 归一化
    fix-typ.mjs        # 修补 pandoc→typst：剥重复 label / 按图尺寸注入适配宽度
    crop-cover.ps1     # 封面裁书脊（60px）→ 前封 800×1132
    metadata.yaml      # EPUB 元数据（书名/作者/语言）
    assets/book.css    # EPUB 版式
    puppeteer.json     # mmdc 复用本机 Chrome（免下载 Chromium）
    mermaid.json       # mmdc 中文标签字体
    *.book.md / *.typ  # 中间产物（预处理后的正文 / pandoc 转换结果）
    .mmd/ figs/        # mermaid 源 / 渲染后的 PNG
```

## 依赖

- **pandoc**（markdown→typst / markdown→epub3）
- **typst**（typst compile）
- **node/npx + @mermaid-js/mermaid-cli**（mermaid 图渲染，复用本机 Chrome）
- **calibre**（EPUB 校验/精修，可选）

## 关键设计决策

- **图用 PNG 而非 SVG**：mermaid 的 SVG 含 `<foreignObject>`，typst 无法渲染（中文标签会消失）。PNG 为 3× 栅格，A5 打印清晰度 >600dpi。
- **目录自动生成**：PDF 用 typst `outline()`、EPUB 用 pandoc `--toc`。章首·误解现场与章末件（本章问题/判据/练习等）通过 `{.unlisted}` → `outlined:false` 排除，与 `00-目录.md` 的三级结构一致。
- **剔「版本变更记录」**：每文件尾的写作元数据表不入书；章末参考文献保留。
- **图片尺寸按 viewBox 注入**：mermaid 图宽高差异极大（1841×94 到 220×734），`fix-typ.mjs` 按比例适配 A5 版心（宽≤110mm、高≤150mm）防溢出。

## 注意

- `puppeteer.json` 里是本机 Chrome 路径；若换机器，改该文件或装 puppeteer 自带 Chromium。
- 渲染好的 `figs/*.png` 已随构建提交，拉取后无需重渲（除非图源变化）。
- 生成 PDF/EPUB 是构建产物，随提交保留（书籍成品即版本快照）。
