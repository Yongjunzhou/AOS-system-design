#!/bin/bash
# 检查文档中 .md 超链接的有效性
# Usage: bash check-links.sh <文档.md>

TARGET="$1"
if [ -z "$TARGET" ] || [ ! -f "$TARGET" ]; then
    echo "用法: bash $0 <文档.md>"
    exit 1
fi

LINKS=$(grep -oP '\[.*?\]\([^)]+\.md\)' "$TARGET" | grep -oP '\([^)]+\.md\)' | tr -d '()' | sort -u)

if [ -z "$LINKS" ]; then
    echo "✅ 文档中无 .md 链接"
    exit 0
fi

VALID=0
BROKEN=0
for link in $LINKS; do
    DIR=$(dirname "$TARGET")
    if [ -f "$DIR/$link" ] || [ -f "$link" ] || [ -f "$(pwd)/$link" ]; then
        VALID=$((VALID + 1))
    else
        echo "❌ 链接无效: $link"
        BROKEN=$((BROKEN + 1))
    fi
done

echo "有效 $VALID 个"
[ "$BROKEN" -gt 0 ] && echo "无效 $BROKEN 个" || echo "✅ 全部有效"
