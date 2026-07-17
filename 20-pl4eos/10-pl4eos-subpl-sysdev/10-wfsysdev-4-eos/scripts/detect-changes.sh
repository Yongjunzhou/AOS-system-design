#!/bin/bash
# 检测人类自上次 AI 运行以来对产品数据文档的修改
# Usage: bash detect-changes.sh <文件路径>
#
# 工作原理：
#   1. 读取文件头 **HEAD @上次 AI 运行** 字段获取上次 commit hash
#   2. git diff <hash>..HEAD -- <文件> 获取变更
#   3. 按 §A.5 协议分类变更类型
#
# 输出：结构化变更摘要，供 AI 消费

TARGET="$1"

if [ -z "$TARGET" ]; then
    echo "用法: bash $0 <文件路径>"
    exit 1
fi

if [ ! -f "$TARGET" ]; then
    echo "❌ 文件不存在: $TARGET"
    exit 1
fi

# Step 1：读取 HEAD @上次 AI 运行
head_line=$(grep -m1 '\*\*HEAD @上次 AI 运行\*\*' "$TARGET")

if [ -z "$head_line" ]; then
    echo "⚠️ 文件无 HEAD@上次AI运行 字段"
    echo "LAST_HEAD=NONE"
    exit 0
fi

# 提取 hash（格式：**HEAD @上次 AI 运行**：<hash> 或 **HEAD @上次 AI 运行**： <hash>）
last_hash=$(echo "$head_line" | sed 's/.*：\s*//' | xargs)

if [ -z "$last_hash" ]; then
    echo "⚠️ HEAD@上次AI运行 字段为空"
    echo "LAST_HEAD=EMPTY"
    exit 0
fi

echo "📋 上次 AI 运行 commit: $last_hash"

# Step 2：检查该 hash 是否仍在 git 历史中
if ! git rev-parse --quiet --verify "$last_hash" > /dev/null 2>&1; then
    echo "⚠️ 上次 commit ($last_hash) 不在当前 git 历史中（可能已被 rebase/squash）"
    echo "   无法执行 diff，请人工检查文件变更"
    echo "LAST_HEAD=GONE"
    exit 0
fi

# Step 3：git diff
# 使用 --unified=3 获取上下文
diff_output=$(git diff "$last_hash"..HEAD -- "$TARGET" 2>&1)
diff_exit=$?

if [ $diff_exit -ne 0 ]; then
    echo "❌ git diff 执行失败: $diff_output"
    exit 0
fi

if [ -z "$diff_output" ]; then
    echo "✅ 人类未修改此文件（自 $last_hash 以来无变更）"
    echo "HAS_CHANGES=0"
    exit 0
fi

echo "HAS_CHANGES=1"
echo ""

# Step 4：分析 diff 中的变更类型
# 提取新增行（以 + 开头）
added_lines=$(echo "$diff_output" | grep '^+' | grep -v '^+++')

# 检查是否包含反馈标注
has_agree=$(echo "$added_lines" | grep -q '\[同意\]' && echo 1 || echo 0)
has_modify=$(echo "$added_lines" | grep -q '\[修改\]' && echo 1 || echo 0)
has_reject=$(echo "$added_lines" | grep -q '\[驳回\]' && echo 1 || echo 0)
has_processed=$(echo "$added_lines" | grep -q '\[已处理\]' && echo 1 || echo 0)

# 统计各类变更
agree_count=$(echo "$added_lines" | grep -c '\[同意\]' 2>/dev/null || echo 0)
modify_count=$(echo "$added_lines" | grep -c '\[修改\]' 2>/dev/null || echo 0)
reject_count=$(echo "$added_lines" | grep -c '\[驳回\]' 2>/dev/null || echo 0)

echo "=== 变更分类 ==="

if [ "$has_agree" = "1" ] || [ "$has_modify" = "1" ] || [ "$has_reject" = "1" ]; then
    echo "📋 检测到反馈标注:"
    [ "$agree_count" -gt 0 ] && echo "   [同意] × $agree_count"
    [ "$modify_count" -gt 0 ] && echo "   [修改] × $modify_count"
    [ "$reject_count" -gt 0 ] && echo "   [驳回] × $reject_count"
    [ "$has_processed" = "1" ] && echo "   ⚠️ 含 [已处理] 标记（可能已处理过）"
    echo "FEEDBACK_TYPE=ANNOTATION"
else
    echo "   无结构化反馈标注"
    echo "FEEDBACK_TYPE=FREE_TEXT"
fi

# Step 5：输出变更行（带行号，供 AI 定位）
echo ""
echo "=== 变更详情（新增/修改行，+ 开头） ==="
# 限制输出行数避免 stdout 爆炸
changed_count=$(echo "$added_lines" | wc -l)
echo "   变更行数: $changed_count"
echo ""

if [ "$changed_count" -gt 50 ]; then
    echo "⚠️ 变更量较大（>$changed_count 行），仅输出前 50 行:"
    echo ""
    echo "$added_lines" | head -50
    echo ""
    echo "... 省略剩余 $((changed_count - 50)) 行。请用 Read 工具按需读取文件中的变更区域。"
else
    echo "$added_lines"
fi

echo ""
echo "LAST_HEAD=$last_hash"
