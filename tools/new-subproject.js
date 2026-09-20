#!/usr/bin/env node
/**
 * new-subproject —— 在子项目区新建子项目，配件一次建齐
 *
 * 【为什么需要】
 * §九 的建区配方是四件事：建子目录 → 建子 CLAUDE.md → 建 claude-memory/
 * → 在指针区加一行。配方写得很清楚，但 02／03／04 三个子项目建区时都漏了
 * 记忆，直到 13 天后才发现。病根是：**规则躺在归档处，动作发生在创建那一刻**。
 * 本脚本把前三件收进一条命令；第四件仍人工（它改的是权威文档，脚本代笔不妥，
 * 但会打印出可粘贴的一行）。
 *
 * 【用法】
 *   node tools/new-subproject.js <名>              建下一个顺号子项目
 *   node tools/new-subproject.js --dry-run <名>     只显示将建什么
 *
 * 【建的什么】
 *   NN 自动取区内现有最大号 +1（`00-topic-research` 是杂项选题区，不参与编号）
 *   50-subprojects/NN-<名>/
 *   ├── CLAUDE.md                 子 CLAUDE.md（隔离协议与边界齐备，定位留待填）
 *   └── claude-memory/
 *       ├── MEMORY.md             索引
 *       └── <名>项目.md            主记忆
 */

'use strict';

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.resolve(__dirname, '..');
const ZONE = path.join(REPO_ROOT, '50-subprojects');

const argv = process.argv.slice(2);
const DRY_RUN = argv.includes('--dry-run');
const name = argv.filter((a) => !a.startsWith('--'))[0];

if (!name) {
  console.error('用法：node tools/new-subproject.js [--dry-run] <名>');
  console.error('  例：node tools/new-subproject.js 供应链研究');
  process.exit(1);
}

// ── 取下一个顺号（00 是杂项选题区，跳过） ──────────────────────────
if (!fs.existsSync(ZONE)) {
  console.error('❌ 找不到子项目区：' + ZONE);
  process.exit(1);
}
const used = fs.readdirSync(ZONE, { withFileTypes: true })
  .filter((e) => e.isDirectory())
  .map((e) => /^(\d+)-/.exec(e.name))
  .filter(Boolean)
  .map((m) => parseInt(m[1], 10))
  .filter((n) => n > 0);
const nn = String((used.length ? Math.max(...used) : 0) + 1).padStart(2, '0');

const DIR = path.join(ZONE, nn + '-' + name);
if (fs.existsSync(DIR)) {
  console.error('❌ 已存在：' + DIR);
  process.exit(1);
}

const today = new Date().toISOString().slice(0, 10);

const SUB_CLAUDE_MD = `# CLAUDE.md（50-subprojects/${nn}-${name} · ${name}子项目）

本目录是 AOS 子项目区（\`50-subprojects/\`）下的研究子项目。**定位待补**——写清本子项目负责共同目标「把不同专业的工作或事项工程化」在哪一个专业领域上的展开。

## 子项目边界（项目集内 · 操作互不干扰）

本子项目是 AOS 项目集内子项目区（\`50-subprojects/\`）的一员，各子项目共同指向「**把不同专业的工作或事项工程化**」这一目标。按 AOS 主 CLAUDE.md §九 **自包含在本目录内**：

- **处理本子项目**：工作目录 = 本目录（\`50-subprojects/${nn}-${name}/\`），读本文件 + \`claude-memory/\`。
- **处理 AOS 主项目 / 其他子项目**：工作目录 = 对应目录，读对应 CLAUDE.md——**不擅自改动其内容**，除非明确要求。
- **主题上可互引、操作上自包含**：本子项目的方法与结论可被其他子项目引用，反之亦然；改动落在谁家由谁做。

## 记忆隔离协议

本子项目的记忆**独立存放**，与 AOS 根记忆（\`.claude/memory/\`，auto-memory 即此目录）**互不干扰**：

- 本子项目的记忆位于 [\`claude-memory/\`](claude-memory/)：\`claude-memory/MEMORY.md\`（索引）+ \`claude-memory/${name}项目.md\`（主记忆）。
- **编写/研究本子项目时**：先读 \`claude-memory/MEMORY.md\` 与相关记忆文件，写入 \`claude-memory/\` 目录。
- **禁止**把本子项目内容写入 AOS 根 \`.claude/memory/\` 或 auto-memory。

## 提交边界（单仓库 + 约定分区）

仓库是 AOS 单一 git 仓库，本子项目不建独立 git。**每次提交只针对本目录内容**：commit message 注明归属（如 \`[${name}]\`），本目录改动不与 AOS 主线或其他子项目改动混提；反之亦然。

## 工作风格与文档纪律

- **禁止选项式交互**：讨论/确认一律自由散文陈述（背景 + 问题 + 建议 + 理由），不用 AskUserQuestion 选项卡/选项卡片让用户做多选题；用户自由回答"改/不改/怎么改"，再据其指示执行（2026-08-25 用户定，仓库全级生效）。

## 文档规范

- Markdown + Mermaid；中文为主体、术语附英文。
- **md→PDF（用户指定的统一转换方式）**：用 AOS 根 \`tools/md2pdf/\` 下的转换工具（\`node tools/md2pdf/md2pdf.js <md路径> [输出.pdf]\`，marked + puppeteer 渲染，支持 Mermaid）。工具在仓库根一级，从本目录相对写即 \`../../tools/md2pdf/md2pdf.js\`；默认输出与源文件同名 .pdf。规则源头见 AOS 根 CLAUDE.md §七。

## 关键文件导航

（待补）
`;

const MEMORY_INDEX = `# ${name}子项目记忆索引（独立于 AOS 项目记忆）

> 本目录是 **50-subprojects/${nn}-${name} 子项目** 的**独立记忆**，与 AOS 项目根记忆（\`.claude/memory/\`）**互不干扰**。
> 处理本子项目内容时：先读本索引 → 读对应记忆文件 → 写入本目录；**不要**写入 AOS 根 \`.claude/memory/\` 或项目 auto-memory。
> 本记忆随仓库版本管理（位于子项目内），可跨设备共享（机制见 AOS 根 CLAUDE.md §八）。

- **${today} 建区**：按 AOS 根 CLAUDE.md §九 建区配方建区（子 CLAUDE.md 与 \`claude-memory/\` 由 \`tools/new-subproject.js\` 一次建齐）。定位与内容待补。详见 [${name}项目.md](${name}项目.md)
`;

const MAIN_MEMORY = `---
name: ${name}项目
description: ${name}子项目主记忆——本子项目的定位/现行内容/决策（独立于 AOS 项目记忆，存放于 50-subprojects/${nn}-${name}/claude-memory/）
metadata:
  type: project
---

> 本文件是 **50-subprojects/${nn}-${name} 子项目** 的独立主记忆，与 AOS 根 \`.claude/memory/\` 互不干扰。处理本子项目内容时读/写本目录。

## 定位

AOS 项目集内子项目区的一员。项目集内各子项目共同指向「**把不同专业的工作或事项工程化**」；本子项目负责该目标在 **<待补>** 上的展开。${today} 建区。

## 现行内容

（待补）
`;

const FILES = [
  [path.join(DIR, 'CLAUDE.md'), SUB_CLAUDE_MD],
  [path.join(DIR, 'claude-memory', 'MEMORY.md'), MEMORY_INDEX],
  [path.join(DIR, 'claude-memory', name + '项目.md'), MAIN_MEMORY],
];

console.log('new-subproject —— 在子项目区新建子项目\n');
console.log('  子项目区 : ' + ZONE);
console.log('  新目录   : ' + nn + '-' + name);
console.log('  编号来源 : 区内现有最大号 ' + (used.length ? Math.max(...used) : 0) + ' + 1\n');
console.log('将要建：');
for (const [f] of FILES) console.log('  ' + path.relative(REPO_ROOT, f));

if (DRY_RUN) {
  console.log('\n（--dry-run：未写入任何文件。）');
  process.exit(0);
}

for (const [f, content] of FILES) {
  fs.mkdirSync(path.dirname(f), { recursive: true });
  fs.writeFileSync(f, content, 'utf-8');
}

console.log('\n✅ 已建。\n');
console.log('还剩一件要人工做——到 AOS 根 CLAUDE.md §九「子项目区指针区」加一行：\n');
console.log('  | ' + name + ' | `50-subprojects/' + nn + '-' + name + '/` | 研究型 | `claude-memory/` | <一句话说明>。见 [`CLAUDE.md`](50-subprojects/' + nn + '-' + name + '/CLAUDE.md) |\n');
console.log('建完可跑 node tools/check-subprojects.js 复验。');
