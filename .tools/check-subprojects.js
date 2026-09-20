#!/usr/bin/env node
/**
 * check-subprojects —— 校验子项目区每个条目都有独立记忆
 *
 * 【为什么需要】
 * AOS 根 CLAUDE.md §九 要求：子项目区内每个条目都建 `claude-memory/`
 * （`MEMORY.md` 索引 ＋ 一份主记忆）。规则写得很清楚，但 02／03／04 三个
 * 子项目建区时都漏了，直到 13 天后才发现——病根是规则躺在归档处，而动作
 * 发生在创建那一刻。本脚本把「漏了」从隐性变成显性：跑一遍即报。
 *
 * 【用法】
 *   node .tools/check-subprojects.js           列出所有条目状态
 *   node .tools/check-subprojects.js --quiet    只在有缺口时输出（供钩子用）
 *
 * 【退出码】有缺口 → 1；全齐 → 0
 */

'use strict';

const fs = require('fs');
const path = require('path');

const REPO_ROOT = path.resolve(__dirname, '..');
const ZONE = path.join(REPO_ROOT, '100-subprojects');
const QUIET = process.argv.includes('--quiet');

// 一个条目合规 = claude-memory/ 存在 ＋ MEMORY.md 存在 ＋ 至少一份主记忆
function problemsOf(dir) {
  const mem = path.join(dir, 'claude-memory');
  if (!fs.existsSync(mem) || !fs.statSync(mem).isDirectory()) {
    return ['缺 claude-memory/'];
  }
  const files = fs.readdirSync(mem);
  const p = [];
  if (!files.includes('MEMORY.md')) p.push('缺 claude-memory/MEMORY.md');
  if (!files.some((f) => f.endsWith('项目.md'))) p.push('缺主记忆（<项目名>项目.md）');
  return p;
}

if (!fs.existsSync(ZONE)) {
  console.error('找不到子项目区：' + ZONE);
  process.exit(1);
}

const entries = fs.readdirSync(ZONE, { withFileTypes: true })
  .filter((e) => e.isDirectory())
  .map((e) => e.name)
  .sort();

const lines = [];
let gaps = 0;
for (const name of entries) {
  const p = problemsOf(path.join(ZONE, name));
  if (p.length) { gaps++; lines.push('  ✗ ' + name + ' —— ' + p.join('；')); }
  else lines.push('  ✓ ' + name);
}

if (gaps) {
  console.log('子项目区记忆校验：' + entries.length + ' 个条目，' + gaps + ' 个有缺口\n');
  console.log(lines.join('\n'));
  console.log('\n补齐办法见 AOS 根 CLAUDE.md §九 建区配方。');
  process.exit(1);
}
if (!QUIET) console.log('子项目区记忆校验：' + entries.length + ' 个条目全齐 ✓');
process.exit(0);
