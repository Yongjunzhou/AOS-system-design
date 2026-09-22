---
name: progress-dsh-memory-mechanism
description: 进行中的工作：把"工作随时可被接续"落成机制——读写触发已写入 AGENTS.md §八，两类文件记忆已建，hook 自动注入待裁
metadata:
  type: progress
---

# 进行中的工作：记忆机制建设

**当前状态**：机制骨架已落地并提交（`<待补：本次提交号>`）。人类 2026-09-22 定「先落它」，据此落成四处：`AGENTS.md` 八、项目记忆新增「读写时机」节（开工先读、收尾四条触发、三类记忆各用各的前缀、每条写回同步索引、不另建副本）；`CLAUDE.md` §八 命名规则第 3、5 条把 `progress-<对象>` 纳入前缀表并与 `AGENTS.md` 交叉引用；新增本文件与 `progress-93-skill-guide.md`；`MEMORY.md` 索引补两行。

## 下一轮从哪继续

**待裁一项：第三层 hook 自动注入。** 现在"开工先读"靠 `AGENTS.md` 的一句话约束，Agent 读不读取决于自觉。要变成机械触发，可用已装在本机的 `dsh-hooks-claude-code` 桥跑一份 `hooks.json`，用 `SessionStart` 输出 JSON `additionalContext` 把 `MEMORY.md` 索引直接注入每个新会话。**为什么没直接做**：它落在机器级配置（`~/.dsh/` 或 `~/.claude/`，在会话工作区之外），需要人类授权；且 `~/.claude/settings.json` 现有 allow 规则只放行了 `Read(//e/e/mywork/AOS/_current/**)`，Claude Code 侧注入会撞它自己的权限门禁。倾向**只做 DSH 一侧**，不动 Claude Code 的现有配置。已知边界两条：该桥的 `SessionStart` 只支持 JSON `additionalContext`（不支持纯 stdout），且 hook 分离运行，注入可能赶不上第一个请求——落地前先验这两条。

**验证一项：拿干净会话试闭环。** 机制好不好用，看一个新会话能否仅凭 `AGENTS.md` 与 `MEMORY.md` 就自动读到在办项、并说清下一步。做不到就说明规则写得不够可执行，改规则而不是怪 Agent。

## 待裁与阻塞

- **`progress-` 前缀是本轮新增**，此前前缀表只认 `feedback-` 与 `pending-`；若人类不认这个类型，改法是撤 `AGENTS.md` §八 那张表的一行与 `CLAUDE.md` 命名规则第 3 条，两份 `progress-*` 改名或并入 `pending-*`。
- **`pending-*` 与 `progress-*` 的界线**目前写作"一件事的未决状态"对"一个对象进行到哪一步"，实做中可能重叠；用几轮后若发现分不清，应合并其中一类而不是硬撑两套。

## 本轮改动的文件与提交号

- `AGENTS.md`（新增「读写时机」节，并把 Codex 专属段落改写为工具中立表述）
- `CLAUDE.md` §八 命名规则（第 3、5 条纳入 `progress-`）
- 新增 `progress-dsh-memory-mechanism.md`、`progress-93-skill-guide.md`
- `MEMORY.md` 索引补两行
- 同轮另有一处环境修复（与本机制无关）：`env-dsh-pwsh-sandbox-acl.md` 与两个修复脚本，提交 `c0394991`

## 关联记忆

[[env-dsh-pwsh-sandbox-acl]]、[[feedback-work-style]]、[[feedback-proactive-planning]]、[[progress-93-skill-guide]]。
