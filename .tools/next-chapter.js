#!/usr/bin/env node
'use strict';
/**
 * next-chapter.js —— 逐章修订：算"下一章"、打印开工语、可选体检
 *
 * 用法：
 *   node .tools/next-chapter.js                # 列章状态 + 打印下一章与开工语
 *   node .tools/next-chapter.js --chapter 1    # 点名第 1 章
 *   node .tools/next-chapter.js --check        # 顺带体检（工作区／远端／复算脚本）
 *
 * 说明：章状态只读 claude-memory/ 入口文件的状态行，未必反映最新正文——
 *       状态行陈旧时先更新入口文件，再跑本脚本。
 */
const fs = require('fs');
const path = require('path');
const cp = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const SUB = path.join(ROOT, '100-subprojects', '01-系统工程研究');
const MEM = path.join(SUB, 'claude-memory');
const BOOK = path.join(SUB, '03-架构师是个怎样的物种');
const WORKSTYLE = path.join(SUB, '.work-style');

const args = process.argv.slice(2);
const ci = args.indexOf('--chapter');
const wantChapter = ci >= 0 ? Number(args[ci + 1]) : null;
const wantCheck = args.includes('--check');

function sh(cmd) {
  try {
    return cp.execSync(cmd, { cwd: ROOT, encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] }).trim();
  } catch (e) {
    return null;
  }
}

function entries() {
  if (!fs.existsSync(MEM)) return [];
  return fs.readdirSync(MEM)
    .filter((f) => /^pending-ch\d+-(revision|rewrite)\.md$/.test(f))
    .map((f) => {
      const n = Number(f.match(/^pending-ch(\d+)-/)[1]);
      const head = fs.readFileSync(path.join(MEM, f), 'utf8').split('\n').slice(0, 60);
      let status = '';
      for (const line of head) {
        if (/状态/.test(line)) {
          status = line.replace(/^[>\s*]+/, '').replace(/状态\*{0,2}[：:]\*{0,2}/, '').replace(/\*\*/g, '').trim();
          break;
        }
      }
      const done = status !== '' && /收工|收口|已落地|已提交|双推/.test(status) && !/待开工|待出|待确认|进行中/.test(status);
      return { n, f, status, done };
    })
    .sort((a, b) => a.n - b.n || a.f.localeCompare(b.f));
}

const es = entries();
const doneN = [...new Set(es.filter((e) => e.done).map((e) => e.n))].sort((a, b) => a - b);
const open = es.filter((e) => !e.done);
const suggested = open.length ? Math.min(...open.map((e) => e.n)) : (doneN.length ? Math.max(...doneN) + 1 : 1);
const next = wantChapter && !Number.isNaN(wantChapter) ? wantChapter : suggested;

console.log('=== 章状态（读自 claude-memory/ 入口文件的状态行）===');
if (!es.length) console.log('  （未找到 pending-ch*.md 入口文件）');
for (const e of es) {
  const flag = e.done ? '收工  ' : '未收工';
  console.log(`  第 ${String(e.n).padStart(2)} 章  ${flag}  ${e.f}`);
  if (e.status) console.log(`             ${e.status.slice(0, 60)}${e.status.length > 60 ? '…' : ''}`);
}

console.log('');
console.log('=== 下一章 ===');
console.log(`  章号      ：第 ${next} 章${wantChapter ? '（点名）' : `（建议：最小未收工章）`}`);
console.log(`  工作目录  ：${SUB}`);
console.log('  开工语    ：新开一个对话、工作目录选上面那个，然后发——');
console.log('                开工下一章');
console.log(`                开工第${next}章`);
if (doneN.includes(next)) {
  console.log(`  ★ 提醒    ：第 ${next} 章入口状态为「已收工」——若确要重做，照《逐章修订手册》四阶段走（手册对所有章一视同仁，无例外）。`);
}

if (wantCheck) {
  console.log('');
  console.log('=== 体检 ===');
  const st = sh('git status --porcelain');
  console.log(`  1) 工作区：${st === '' ? '干净 ✓' : `有 ${st.split('\n').length} 项未提交改动——开工前先提交或收好`}`);
  sh('git fetch --quiet');
  const behind = sh('git rev-list --count HEAD..origin/master');
  const ahead = sh('git rev-list --count origin/master..HEAD');
  console.log(`  2) 远端  ：${behind === null ? '（取不到 origin/master，跳过）' : behind === '0' ? '已最新 ✓' : `落后 origin/master ${behind} 个提交——先 git pull`}${ahead && ahead !== '0' ? `；本地领先 ${ahead} 个提交（未推）` : ''}`);
  const need = [
    'ch2_layout.py', 'check_tail_order.py', 'check_glued_paragraphs.py', 'audit_plainwords.py',
    'audit_verbosity.py', 'audit_metaphor_density.py', 'audit_chapter_openings.py',
    'audit_dialogue_cite.py', 'slim_bold_ch4.py', 'scan_block_matchers.py',
  ];
  const have = fs.existsSync(WORKSTYLE) ? fs.readdirSync(WORKSTYLE) : [];
  const missing = need.filter((x) => !have.includes(x));
  console.log(`  3) 复算脚本：在库两把尺子——${['00-风格参考-量尺.py', '00-三条线索-核对.py'].filter((x) => fs.existsSync(path.join(BOOK, x))).join('、') || '（缺失！）'}`);
  console.log(`               .work-style/ 缺 ${missing.length} 个：${missing.length ? missing.join('、') : '无 ✓'}（按手册 §十一 的用途重建）`);
}
