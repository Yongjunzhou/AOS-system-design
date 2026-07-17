#!/bin/bash
# 提取产品数据文档中的指定分节
# Usage: bash read-section.sh <文件路径> <分节名称>
#
# 分节名称示例：
#   "AI可以处理节点"     → 匹配 ## AI可以处理节点
#   "待 wft01-biz 处理"  → 匹配 ### 待 wft01-biz 处理
#   "AI最近变更"         → 匹配 ## AI最近变更
#   "自描述索引"         → 匹配 ## 自描述索引
#   "HEAD"               → 输出 **HEAD @上次 AI 运行** 字段值

TARGET="$1"
SECTION="$2"

if [ -z "$TARGET" ] || [ -z "$SECTION" ]; then
    echo "用法: bash $0 <文件路径> <分节名称>"
    exit 1
fi

if [ ! -f "$TARGET" ]; then
    echo "❌ 文件不存在: $TARGET"
    exit 1
fi

# 特殊处理：HEAD 字段
if [ "$SECTION" = "HEAD" ]; then
    result=$(grep -m1 '\*\*HEAD @上次 AI 运行\*\*' "$TARGET")
    if [ -n "$result" ]; then
        echo "$result"
    else
        echo "⚠️ 文件无 HEAD@上次AI运行 字段"
    fi
    exit 0
fi

# 查找分节标题行（匹配 ## 或 ### 级别）
# 先尝试精确匹配 ### 级别
header_line=$(grep -n "^### $SECTION" "$TARGET" | head -1)
header_level=3

# 如果 ### 没找到，尝试 ## 级别
if [ -z "$header_line" ]; then
    header_line=$(grep -n "^## $SECTION" "$TARGET" | head -1)
    header_level=2
fi

if [ -z "$header_line" ]; then
    echo "❌ 未找到分节: $SECTION"
    exit 0
fi

line_num=$(echo "$header_line" | cut -d: -f1)

# 确定标题的 # 数量
heading_chars=""
if [ "$header_level" -eq 3 ]; then
    heading_chars="###"
else
    heading_chars="##"
fi

# 从标题行开始，输出到下一个同级或更高级标题（或文件末尾）
# 同级或更高级 = 相同或更少的 # 数量
awk -v start="$line_num" -v hchars="$heading_chars" '
NR >= start {
    # 跳过标题行自身
    if (NR == start) {
        print
        next
    }
    # 遇到同级或更高级标题（不是更深层的子标题）→ 停止
    # 更高级 = ## （比 ### 少一个 #）
    if (hchars == "###") {
        # 当前在 ### 级别，遇到 ## 或 ### 都停止
        if ($0 ~ /^## / || $0 ~ /^### /) exit
    } else {
        # 当前在 ## 级别，遇到 ## 停止（不会有 ### 比 ## 高级，但也要停）
        if ($0 ~ /^## /) exit
    }
    print
}
' "$TARGET"
