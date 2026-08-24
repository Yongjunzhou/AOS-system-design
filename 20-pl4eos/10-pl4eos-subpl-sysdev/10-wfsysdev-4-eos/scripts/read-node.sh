#!/bin/bash
# 按节点ID提取产品数据文档中的节点块
# Usage: bash read-node.sh <文件路径> <节点ID>
#
# 支持的节点ID格式（自动识别）：
#   OR-NNN           → 01文件，匹配 #### OR-NNN
#   bph-biz-GOV-NNN    → 02文件，通过 <!-- BLOCK: ... --> 定位
#   @node-xxx        → 23文件，匹配 ##### @node-xxx
#   @prod-xxx        → 23文件，匹配 ##### @prod-xxx
#   @engine-xxx      → 25文件，匹配 #### @engine-xxx
#   @nfr-NNN         → 22文件，匹配 #### @nfr-NNN

TARGET="$1"
NODE_ID="$2"

if [ -z "$TARGET" ] || [ -z "$NODE_ID" ]; then
    echo "用法: bash $0 <文件路径> <节点ID>"
    exit 1
fi

if [ ! -f "$TARGET" ]; then
    echo "❌ 文件不存在: $TARGET"
    exit 1
fi

# 根据节点ID前缀判断格式
case "$NODE_ID" in
    OR-*|ROLE-*)
        # 格式A：OR-NNN / ROLE-XXX → #### OR-NNN / #### ROLE-XXX 标题
        header_line=$(grep -n "^#### $NODE_ID " "$TARGET" | head -1)
        if [ -z "$header_line" ]; then
            echo "❌ 未找到节点: $NODE_ID"
            exit 0
        fi
        start_line=$(echo "$header_line" | cut -d: -f1)
        # 输出到下一个 #### 标题、--- 分隔线、或 ## 章节标题
        awk -v start="$start_line" '
        NR >= start {
            if (NR > start && ($0 ~ /^#### / || $0 ~ /^---$/ || $0 ~ /^## /)) exit
            print
        }
        ' "$TARGET"
        ;;
    bph-biz-*|bph-nfr-*)
        # 格式B：通过 <!-- BLOCK: XXX --> 和 <!-- /BLOCK: XXX --> 定位
        start_line=$(grep -n "<!-- BLOCK: $NODE_ID -->" "$TARGET" | head -1 | cut -d: -f1)
        if [ -z "$start_line" ]; then
            echo "❌ 未找到节点: $NODE_ID"
            exit 0
        fi
        end_line=$(grep -n "<!-- /BLOCK: $NODE_ID -->" "$TARGET" | head -1 | cut -d: -f1)
        if [ -z "$end_line" ]; then
            # 无结束标记，输出到文件末尾
            end_line=$(wc -l < "$TARGET")
        fi
        sed -n "${start_line},${end_line}p" "$TARGET"
        ;;
    @node-*|@prod-*)
        # 格式C：##### @node-xxx 或 ##### @prod-xxx
        header_line=$(grep -n "^##### $NODE_ID " "$TARGET" | head -1)
        if [ -z "$header_line" ]; then
            echo "❌ 未找到节点: $NODE_ID"
            exit 0
        fi
        start_line=$(echo "$header_line" | cut -d: -f1)
        awk -v start="$start_line" '
        NR >= start {
            if (NR > start && ($0 ~ /^##### @/ || $0 ~ /^---$/ || $0 ~ /^## /)) exit
            print
        }
        ' "$TARGET"
        ;;
    @engine-*)
        # 格式D：@engine-xxx（25文件，BLOCK ID 为去掉@后的大写形式）
        # 例：@engine-flow → BLOCK: ENGINE-FLOW
        block_id=$(echo "${NODE_ID#@}" | tr '[:lower:]' '[:upper:]')
        start_line=$(grep -n "<!-- BLOCK: $block_id" "$TARGET" | head -1 | cut -d: -f1)
        if [ -n "$start_line" ]; then
            end_line=$(grep -n "<!-- /BLOCK: $block_id" "$TARGET" | head -1 | cut -d: -f1)
            if [ -z "$end_line" ]; then
                end_line=$(wc -l < "$TARGET")
            fi
            sed -n "${start_line},${end_line}p" "$TARGET"
        else
            echo "❌ 未找到节点: $NODE_ID"
            exit 0
        fi
        ;;
    @nfr-*)
        # 格式E：#### @nfr-NNN
        header_line=$(grep -n "^#### $NODE_ID " "$TARGET" | head -1)
        if [ -z "$header_line" ]; then
            echo "❌ 未找到节点: $NODE_ID"
            exit 0
        fi
        start_line=$(echo "$header_line" | cut -d: -f1)
        awk -v start="$start_line" '
        NR >= start {
            if (NR > start && ($0 ~ /^#### / || $0 ~ /^---$/ || $0 ~ /^## /)) exit
            print
        }
        ' "$TARGET"
        ;;
    *)
        echo "❌ 不支持的节点ID格式: $NODE_ID"
        echo "   支持的格式: OR-NNN, bph-biz-GOV-NNN, bph-nfr-NNN, @node-xxx, @prod-xxx, @engine-xxx, @nfr-NNN"
        exit 0
        ;;
esac
