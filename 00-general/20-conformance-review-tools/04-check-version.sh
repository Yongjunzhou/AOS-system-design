#!/bin/bash
# 检查文档版本号是否存在
# Usage: bash check-version.sh <文档.md>

TARGET="$1"
if [ -z "$TARGET" ] || [ ! -f "$TARGET" ]; then
    echo "用法: bash $0 <文档.md>"
    exit 1
fi

if grep -qE "[vV][0-9]+\.[0-9]" "$TARGET"; then
    line=$(grep -nE "[vV][0-9]+\.[0-9]" "$TARGET" | head -1)
    echo "✅ 版本号存在: $(echo "$line" | awk -F: '{print $2}' | xargs)"
else
    echo "❌ 未找到版本号（格式: vX.X）"
fi
