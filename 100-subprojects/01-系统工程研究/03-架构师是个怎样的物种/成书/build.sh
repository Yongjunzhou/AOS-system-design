#!/usr/bin/env bash
# build.sh — 《架构师是个怎样的物种？》成书构建单入口
# 用法：bash build.sh [--rerender]   （--rerender 强制重渲 mermaid 图）
# 产物：架构师-打印版.pdf + 架构师-电子版.epub
set -euo pipefail
cd "$(dirname "$0")"

# 工具链 PATH（pandoc/typst 由 winget 安装，非系统 PATH）
export PATH="/c/Users/HUAWEI/AppData/Local/Pandoc:/c/Users/HUAWEI/AppData/Local/Microsoft/WinGet/Packages/Typst.Typst_Microsoft.Winget.Source_8wekyb3d8bbwe/typst-x86_64-pc-windows-msvc:$PATH"
# 图1-5 蛇形渲染依赖 puppeteer-core（随 mmdc 下载在 npx 缓存里）
# 注：find 目标为 Windows 专有路径；在非 Windows 上 find 会返回非 0，pipefail 下触发 set -e 退出——
# 加 `|| true` 使跨平台安全（Windows 路径存在时正常、不存在时无害跳过）。
PPC="$(find /c/Users/HUAWEI/AppData/Local/npm-cache/_npx -maxdepth 4 -type d -name puppeteer-core 2>/dev/null | head -1 || true)"
if [ -n "$PPC" ]; then
  export NODE_PATH="$(dirname "$PPC")${NODE_PATH:+:$NODE_PATH}"
fi

OUT=build
mkdir -p "$OUT/.mmd" "$OUT/figs" "$OUT/assets"

echo "[1/6] 预处理（剔版本记录 / mermaid 提取 / .unlisted 归一化）"
node "$OUT/preprocess.mjs" .. "$OUT"

echo "[2/6] mermaid → PNG"
if [ "${1:-}" = "--rerender" ] || [ -z "$(ls "$OUT/figs"/*.png 2>/dev/null)" ]; then
  for mmd in "$OUT"/.mmd/ch*.mmd; do
    base=$(basename "$mmd" .mmd)
    npx -y @mermaid-js/mermaid-cli@11.16 -i "$mmd" -o "$OUT/figs/$base.png" -b white -s 3 -p "$OUT/puppeteer.json" -c "$OUT/mermaid.json"
  done
else
  echo "  图已存在（重渲请加 --rerender）"
fi

echo "[2.5/6] 图1-5 蛇形渲染（mermaid 子图方向失效 → 手绘 SVG 直渲）"
if [ "${1:-}" = "--rerender" ] || [ ! -f "$OUT/figs/ch01-fig05.png" ]; then
  node "$OUT/render-fig05-snake.cjs"
else
  echo "  图1-5 蛇形 PNG 已存在"
fi

echo "[3/6] 封面裁剪（书脊 60px → 前封 800×1132）"
if [ ! -f "$OUT/assets/cover-800x1132.png" ]; then
  powershell -ExecutionPolicy Bypass -File "$OUT/crop-cover.ps1" "../封面/封面-前封书脊.png" "$OUT/assets/cover-800x1132.png"
fi

echo "[4/6] 逐章 pandoc → typst + fix-typ（剥 label / 注入图宽）"
while IFS= read -r base; do
  pandoc -f markdown -t typst "$OUT/$base.book.md" -o "$OUT/$base.typ"
done < "$OUT/manifest.txt"
node "$OUT/fix-typ.mjs" "$OUT"

echo "[5/6] typst compile → PDF"
typst compile main.typ 架构师-打印版.pdf

echo "[6/6] pandoc → EPUB"
args=(); while IFS= read -r base; do args+=("$OUT/$base.book.md"); done < "$OUT/manifest.txt"
pandoc -f markdown -t epub3 "${args[@]}" \
  --metadata-file="$OUT/metadata.yaml" \
  --toc --toc-depth=3 --split-level=1 \
  --epub-cover-image="$OUT/assets/cover-800x1132.png" \
  --css="$OUT/assets/book.css" \
  --resource-path="$OUT" \
  -o 架构师-电子版.epub

echo "════════ 完成 ════════"
ls -la 架构师-打印版.pdf 架构师-电子版.epub
