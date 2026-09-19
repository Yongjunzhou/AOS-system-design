#!/usr/bin/env node
/**
 * setup-memory —— 把 Claude Code 的记忆加载点指到本仓库目录
 *
 * 【为什么需要】
 * Claude Code 默认把记忆读写在本机的
 *     ~/.claude/projects/<仓库路径转义>/memory/
 * 而本仓库的记忆（见 CLAUDE.md §八）存放在仓库内 .claude/memory/ 并纳入 git。
 * 于是记忆有了两份：仓库一份（跟着 git 走）、本机一份（会话真正读的）。
 * 换机器 pull 之后仓库那份更新了，本机那份不会动 —— 记忆就落后。
 *
 * 本脚本把加载点**直接指到仓库内那份**，从此只有一份文件：
 * 读的是它、写的也是它，pull 即最新，无需任何复制。
 *
 * 【用法】
 *   node tools/setup-memory.js             写入本机用户级设置（先自动备份）
 *   node tools/setup-memory.js --check     只报当前状态
 *   node tools/setup-memory.js --dry-run   只显示将要写入什么
 *
 * 【注意】
 * 1. 每台机器跑一次即可，之后永久有效；仓库换位置后要重跑。
 * 2. 路径必须是绝对路径（Claude Code 不接受相对路径），而两台机器的仓库
 *    位置通常不同，所以这一步无法随 git 同步，只能各机器各跑一次。
 * 3. 改的是**本机用户级**设置 ~/.claude/settings.json，不进本仓库。
 * 4. 写完需重启会话才生效。
 */

'use strict';

const fs = require('fs');
const path = require('path');
const os = require('os');

const REPO_ROOT = path.resolve(__dirname, '..');
const MEMORY_DIR = path.join(REPO_ROOT, '.claude', 'memory');
const SETTINGS_PATH = path.join(os.homedir(), '.claude', 'settings.json');
const KEY = 'autoMemoryDirectory';

const argv = process.argv.slice(2);
const CHECK_ONLY = argv.includes('--check');
const DRY_RUN = argv.includes('--dry-run');

function ok(msg) { console.log('  ' + msg); }
function die(msg) { console.error('❌ ' + msg); process.exit(1); }

console.log('setup-memory —— 把记忆加载点指到本仓库\n');
console.log('  仓库根目录 : ' + REPO_ROOT);
console.log('  记忆目录   : ' + MEMORY_DIR);
console.log('  设置文件   : ' + SETTINGS_PATH);
console.log('');

// ── 前置检查：仓库里的记忆目录得存在 ────────────────────────────────
if (!fs.existsSync(MEMORY_DIR) || !fs.statSync(MEMORY_DIR).isDirectory()) {
  die('仓库内找不到记忆目录：' + MEMORY_DIR);
}
if (!fs.existsSync(path.join(MEMORY_DIR, 'MEMORY.md'))) {
  die('记忆目录里没有 MEMORY.md：' + MEMORY_DIR + '（仓库记忆索引缺失）');
}

// ── 读取现有设置 ────────────────────────────────────────────────────
let settings = {};
let rawBefore = null;
if (fs.existsSync(SETTINGS_PATH)) {
  rawBefore = fs.readFileSync(SETTINGS_PATH, 'utf-8');
  try {
    settings = JSON.parse(rawBefore);
  } catch (e) {
    die('设置文件不是合法 JSON，未做任何改动：' + SETTINGS_PATH + '\n     ' + e.message);
  }
} else {
  ok('（设置文件尚不存在，将新建）');
}

const current = settings[KEY];

// ── 已正确 → 不写 ──────────────────────────────────────────────────
if (current === MEMORY_DIR) {
  console.log('✅ 已经指向本仓库，无需改动。');
  console.log('');
  console.log('   （若刚换过机器，重启会话即可生效。）');
  process.exit(0);
}

if (CHECK_ONLY) {
  console.log('⚠️  尚未指向本仓库（当前：' + (current === undefined ? '未设置' : current) + '）');
  console.log('   跑  node tools/setup-memory.js  即可写入。');
  process.exit(1);
}

// ── 生成新设置 ──────────────────────────────────────────────────────
const next = { ...settings, [KEY]: MEMORY_DIR };
const rawAfter = JSON.stringify(next, null, 2) + '\n';

console.log('将要改动：');
console.log('   ' + KEY + ': ' + (current === undefined ? '（原本没有这一项）' : current));
console.log('              ↓');
console.log('   ' + KEY + ': ' + MEMORY_DIR);
console.log('');
console.log('   设置文件里其余内容（含 env、theme 等）原样保留。');

if (DRY_RUN) {
  console.log('');
  console.log('（--dry-run：未写入任何文件。）');
  process.exit(0);
}

// ── 备份 → 写入 ─────────────────────────────────────────────────────
const dir = path.dirname(SETTINGS_PATH);
if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

if (rawBefore !== null) {
  const stamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
  const backup = SETTINGS_PATH + '.bak-' + stamp;
  fs.writeFileSync(backup, rawBefore, 'utf-8');
  console.log('');
  console.log('   已备份原设置：' + backup);
}

fs.writeFileSync(SETTINGS_PATH, rawAfter, 'utf-8');

console.log('');
console.log('✅ 已写入。');
console.log('');
console.log('   下一步：**重启会话** 才生效。');
console.log('   生效后，本机记忆读写的就是仓库内 .claude/memory/ —— 与 git 同一份，');
console.log('   换机器 pull 即最新，不再需要复制。');
