#!/usr/bin/env bash
# ai-commit.sh <message>
# AI 标识提交：author/committer = EOS-AI，message 前缀 [AI]，Co-Authored-By trailer。
# 提交后输出新基线 hash，供 AI 记录到状态文档 `HEAD @上次AI运行` 字段。
# 用法示例：scripts/ai-commit.sh "ort01: 已生成切分方案，等待反馈"
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "用法: ai-commit.sh <commit message>" >&2
  exit 1
fi
MSG="$1"

# 无变更时基线不变，避免空提交报错
if [ -z "$(git status --porcelain)" ]; then
  echo "无变更，基线不变: $(git rev-parse HEAD)"
  exit 0
fi

# 提交全部文档/状态表变更（基线 = 人类看到的完整状态；人类未提交的编辑一并纳入）
git add -A

GIT_AUTHOR_NAME="EOS-AI" GIT_AUTHOR_EMAIL="ai@eos.local" \
GIT_COMMITTER_NAME="EOS-AI" GIT_COMMITTER_EMAIL="ai@eos.local" \
  git commit -m "[AI] ${MSG}" -m "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>" >/dev/null

echo "新基线: $(git rev-parse HEAD)"
