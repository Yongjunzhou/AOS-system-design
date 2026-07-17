#!/bin/bash
# 更新产品数据文档的元信息
# Usage: bash update-meta.sh <文件路径> <操作> [参数...]
#
# 操作：
#   bump-version      递增次版本号 + 更新修订日期
#   update-head       更新 HEAD @上次 AI 运行 = $(git rev-parse HEAD)
#   add-recent-change <Skill名> <操作类型> <节点ID> <摘要>
#                     追加 AI最近变更 行，保留最近30条
#   move-node         <节点ID> <from-section> <to-section>
#                     在 AI可以处理节点 中移动节点条目

TARGET="$1"
OP="$2"

if [ -z "$TARGET" ] || [ -z "$OP" ]; then
    echo "用法: bash $0 <文件路径> <操作> [参数...]"
    echo "操作: bump-version | update-head | add-recent-change | move-node"
    exit 1
fi

if [ ! -f "$TARGET" ]; then
    echo "❌ 文件不存在: $TARGET"
    exit 1
fi

# 确保文件在 git 中可写
if [ ! -w "$TARGET" ]; then
    echo "❌ 文件不可写: $TARGET"
    exit 1
fi

case "$OP" in
    bump-version)
        # 递增次版本号 + 更新修订日期
        ver_line=$(grep -n '\*\*文档版本\*\*' "$TARGET" | head -1)
        if [ -z "$ver_line" ]; then
            echo "⚠️ 文件无 **文档版本** 字段，跳过"
            exit 0
        fi
        ver_ln=$(echo "$ver_line" | cut -d: -f1)

        # 提取当前版本号
        current_ver=$(echo "$ver_line" | grep -oE 'v[0-9]+\.[0-9]+' | head -1)
        if [ -z "$current_ver" ]; then
            echo "⚠️ 无法解析版本号，跳过"
            exit 0
        fi

        major=$(echo "$current_ver" | cut -d. -f1 | tr -d 'v')
        minor=$(echo "$current_ver" | cut -d. -f2)
        new_minor=$((minor + 1))
        new_ver="v${major}.${new_minor}"

        today=$(date +%Y-%m-%d)

        # 更新版本号
        sed -i "${ver_ln}s/v[0-9]\+\.[0-9]\+/${new_ver}/" "$TARGET"

        # 更新修订日期
        date_line=$(grep -n '\*\*修订日期\*\*' "$TARGET" | head -1)
        if [ -n "$date_line" ]; then
            date_ln=$(echo "$date_line" | cut -d: -f1)
            sed -i "${date_ln}s/[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/${today}/" "$TARGET"
        fi

        echo "✅ 版本号: ${current_ver} → ${new_ver} | 修订日期: ${today}"
        ;;

    update-head)
        # 更新 HEAD @上次 AI 运行
        head_line=$(grep -n '\*\*HEAD @上次 AI 运行\*\*' "$TARGET" | head -1)
        if [ -z "$head_line" ]; then
            echo "⚠️ 文件无 HEAD@上次AI运行 字段，跳过"
            exit 0
        fi
        head_ln=$(echo "$head_line" | cut -d: -f1)

        current_hash=$(git rev-parse HEAD 2>/dev/null)
        if [ -z "$current_hash" ]; then
            echo "❌ 无法获取当前 git commit hash"
            exit 1
        fi

        # 替换 hash（格式可能是 **HEAD @上次 AI 运行**：<hash> 或 **HEAD @上次 AI 运行**： <hash>）
        sed -i "${head_ln}s/：\s*[a-f0-9]*/：${current_hash}/" "$TARGET"

        echo "✅ HEAD @上次 AI 运行 → ${current_hash}"
        ;;

    add-recent-change)
        SKILL="$3"
        OP_TYPE="$4"
        NODE_ID="$5"
        SUMMARY="$6"

        if [ -z "$SKILL" ] || [ -z "$OP_TYPE" ] || [ -z "$SUMMARY" ]; then
            echo "用法: bash $0 <文件> add-recent-change <Skill名> <操作类型> <节点ID> <摘要>"
            exit 1
        fi

        # 定位 AI最近变更 分节 + 其表格分隔行
        section_start=$(grep -n '^## AI最近变更' "$TARGET" | head -1 | cut -d: -f1)
        if [ -z "$section_start" ]; then
            echo "⚠️ 文件无 ## AI最近变更 分节，跳过"
            exit 0
        fi

        # 在 AI最近变更 分节内找第一个 |--- 分隔行
        separator=$(awk -v start="$section_start" '
        NR > start {
            if ($0 ~ /^[|]---/) {print NR; exit}
            if ($0 ~ /^## /) exit
        }
        ' "$TARGET")
        if [ -z "$separator" ]; then
            echo "⚠️ 在 AI最近变更 分节内未找到表格分隔行，跳过"
            exit 0
        fi

        # 在分隔行后插入新行
        insert_ln=$((separator + 1))
        now=$(date +%Y-%m-%d)
        node_link="[→](#${NODE_ID})"
        new_row="| ${now} | ${SKILL} | ${OP_TYPE} ${node_link} | ${NODE_ID} | ${SUMMARY} |"

        sed -i "${insert_ln}i\\${new_row}" "$TARGET"

        # 确保不超过30条——统计表格数据行
        # 从分隔行+1开始，统计到空行或下一个 ## 为止
        data_rows=$(awk -v start="$separator" '
        NR > start {
            if ($0 ~ /^$/ || $0 ~ /^## /) exit
            if ($0 ~ /^[|]/) count++
        }
        END {print count}
        ' "$TARGET")

        if [ "$data_rows" -gt 30 ]; then
            # 删除最旧的行（分隔行后第一行数据）
            oldest=$((separator + 1))
            sed -i "${oldest}d" "$TARGET"
            echo "📋 已滚动删除最旧记录（保留最近30条）"
        fi

        echo "✅ 已追加 AI最近变更: ${SKILL} | ${OP_TYPE} | ${NODE_ID}"
        ;;

    move-node)
        NODE_ID="$3"
        FROM_SECTION="$4"
        TO_SECTION="$5"

        if [ -z "$NODE_ID" ] || [ -z "$FROM_SECTION" ] || [ -z "$TO_SECTION" ]; then
            echo "用法: bash $0 <文件> move-node <节点ID> <from-section> <to-section>"
            echo "  from/to-section: wft01-biz | wft01-eng | wft01-nfr | feedback | downstream-return"
            exit 1
        fi

        # 映射分节名称
        case "$FROM_SECTION" in
            wft01-biz) from_name="待 wft01-biz 处理" ;;
            wft01-eng) from_name="待 wft01-eng 处理" ;;
            wft01-nfr) from_name="待 wft01-nfr 处理" ;;
            feedback) from_name="待反馈处理" ;;
            downstream-return) from_name="待下游退回处理" ;;
            *) echo "❌ 不支持的分节: $FROM_SECTION"; exit 1 ;;
        esac

        case "$TO_SECTION" in
            wft01-biz) to_name="待 wft01-biz 处理" ;;
            wft01-eng) to_name="待 wft01-eng 处理" ;;
            wft01-nfr) to_name="待 wft01-nfr 处理" ;;
            feedback) to_name="待反馈处理" ;;
            downstream-return) to_name="待下游退回处理" ;;
            *) echo "❌ 不支持的分节: $TO_SECTION"; exit 1 ;;
        esac

        # 在源分节中查找节点行
        from_header=$(grep -n "^### ${from_name}" "$TARGET" | head -1 | cut -d: -f1)
        if [ -z "$from_header" ]; then
            echo "⚠️ 未找到源分节: ### ${from_name}"
            exit 0
        fi

        # 找到含节点ID的表格行
        node_line=$(awk -v start="$from_header" -v nid="$NODE_ID" '
        NR >= start {
            if ($0 ~ nid) {print NR": "$0; exit}
            if ($0 ~ /^### / && NR > start) exit
        }' "$TARGET")

        if [ -z "$node_line" ]; then
            echo "⚠️ 在 ${from_name} 中未找到节点: ${NODE_ID}"
            exit 0
        fi

        node_ln=$(echo "$node_line" | cut -d: -f1)
        node_content=$(echo "$node_line" | cut -d: -f2-)

        # 从源分节删除该行
        sed -i "${node_ln}d" "$TARGET"

        # 在目标分节插入（表格末尾，下一个 ### 或空行之前）
        to_header=$(grep -n "^### ${to_name}" "$TARGET" | head -1 | cut -d: -f1)
        if [ -z "$to_header" ]; then
            echo "⚠️ 未找到目标分节: ### ${to_name}，回滚删除操作"
            # 简单回滚：重新插入到原位置
            sed -i "${node_ln}i\\${node_content}" "$TARGET"
            exit 0
        fi

        # 检查目标分节是否为空（含"当前无"等占位文本）
        is_empty=$(awk -v start="$to_header" 'NR > start {
            if ($0 ~ /^### /) exit
            if ($0 ~ /当前无/) {print "1"; exit}
            if ($0 ~ /^\|/) {print "0"; exit}
        }' "$TARGET")

        if [ "$is_empty" = "1" ]; then
            # 替换占位文本为表格 + 节点行
            placeholder_ln=$(awk -v start="$to_header" 'NR > start {
                if ($0 ~ /当前无/) {print NR; exit}
                if ($0 ~ /^### /) exit
            }' "$TARGET")

            if [ -n "$placeholder_ln" ]; then
                # 先获取原表头（从其他分节复制表格格式）
                table_head=$(grep -A1 '^| 节点 ID' "$TARGET" | head -2)
                if [ -n "$table_head" ]; then
                    sed -i "${placeholder_ln}d" "$TARGET"
                    # 在目标分节标题后插入表头和节点行
                    sed -i "${to_header}a\\${table_head}\n${node_content}" "$TARGET"
                else
                    # 直接替换占位文本为节点行
                    sed -i "${placeholder_ln}c\\${node_content}" "$TARGET"
                fi
            fi
        else
            # 在表格末尾追加（最后一个表格行之后，下一个 ### 或空行之前）
            insert_ln=$(awk -v start="$to_header" 'NR > start {
                if ($0 ~ /^### /) {print NR - 1; exit}
                if ($0 ~ /^$/ && last_table) {print NR - 1; exit}
                if ($0 ~ /^\|/) last_table=1
            }' "$TARGET")

            if [ -n "$insert_ln" ]; then
                sed -i "${insert_ln}a\\${node_content}" "$TARGET"
            else
                # 回退：在标题后插入
                sed -i "${to_header}a\\${node_content}" "$TARGET"
            fi
        fi

        echo "✅ ${NODE_ID}: ${from_name} → ${to_name}"
        ;;

    *)
        echo "❌ 不支持的操作: $OP"
        echo "   支持: bump-version | update-head | add-recent-change | move-node"
        exit 1
        ;;
esac
