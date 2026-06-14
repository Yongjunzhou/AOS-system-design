#!/bin/bash
# 检查文档编号格式一致性
# 报告文档中出现的编号模式分布
# Usage: bash check-numbering.sh <文档.md>

TARGET="$1"
if [ -z "$TARGET" ] || [ ! -f "$TARGET" ]; then
    echo "用法: bash $0 <文档.md>"
    exit 1
fi

THREE_DIGIT=$(grep -oE '[A-Z]+-[0-9]{3}' "$TARGET" | sort -u | head -20)
DOT_TWO=$(grep -oE '[A-Z]+-[0-9]+\.[0-9]{2}' "$TARGET" | sort -u | head -20)
DOT_ONE=$(grep -oE '[A-Z]+-[0-9]+\.[0-9][^0-9]' "$TARGET" | grep -oE '[A-Z]+-[0-9]+\.[0-9]' | sort -u | head -20)

[ -n "$THREE_DIGIT" ] && echo "📋 架构编号（3位）: $(echo "$THREE_DIGIT" | tr '\n' ' ')"
[ -n "$DOT_TWO" ] && echo "📋 详细编号（.01格式）: $(echo "$DOT_TWO" | tr '\n' ' ')"
[ -n "$DOT_ONE" ] && echo "⚠️  单数字编号（.1格式）: $(echo "$DOT_ONE" | tr '\n' ' ')"

if [ -z "$THREE_DIGIT" ] && [ -z "$DOT_TWO" ]; then
    echo "✅ 未检测到目标格式的编号"
fi
