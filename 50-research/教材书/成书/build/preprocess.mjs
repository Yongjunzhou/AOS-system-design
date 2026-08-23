#!/usr/bin/env node
/**
 * preprocess.mjs — 教材书 → .book.md 清洗脚本
 *
 * 职责（不动源文件，输出到 build/）：
 *   1. 按 MANIFEST 顺序组装（序言/前言/01~16 章/17 附录）
 *   2. 剔除每文件末尾「## 版本变更记录」表（写作元数据）
 *   3. 提取 mermaid 块 → build/.mmd/chNN-figKK.mmd 源，替换为 ![](figs/chNN-figKK.svg)
 *      图号「图 N-K」按章内序号；修复 ch9 裸 `&` 转义
 *   4. 非编号/含「章首」的 ##/### 标题追加 {.unlisted}（附录除外）——双轨目录排除
 *   5. 输出 build/*.book.md + build/manifest.txt（顺序清单）
 *
 * 用法：node preprocess.mjs <SRC目录> <OUT目录>
 */
import { readFileSync, writeFileSync, mkdirSync, readdirSync, rmSync, statSync } from 'node:fs';
import { join, resolve } from 'node:path';

const SRC = resolve(process.argv[2] || '..');   // 教材书/ 源目录
const OUT = resolve(process.argv[3] || 'build'); // 输出目录

for (const d of ['', '.mmd', 'figs', 'assets']) mkdirSync(join(OUT, d), { recursive: true });
// 清空上次构建的 .mmd 与 .book.md（figs 保留已渲染图可复用）
const rmFile = p => { if (statSync(p).isFile()) rmSync(p); };
for (const f of readdirSync(join(OUT, '.mmd'))) rmFile(join(OUT, '.mmd', f));
for (const f of readdirSync(OUT).filter(f => f.endsWith('.book.md')))
  rmFile(join(OUT, f));

// ---------- MANIFEST：磁盘 glob + 前缀匹配，抗文件名变化 ----------
const all = readdirSync(SRC).filter(f => f.endsWith('.md'));
const EXCLUDE_RE = /从教材到问题分析|^00-(全书框架|案例设定|方法论的底座|重构开工包|目录)/;
const files = all.filter(f => !EXCLUDE_RE.test(f));
function findFile(prefix) {
  const hit = files.find(f => f.startsWith(prefix));
  if (!hit) throw new Error(`preprocess: 未找到源文件 ${prefix}*（实际：${files.slice(0, 8).join(', ')}…）`);
  return hit;
}
const chapters = Array.from({ length: 16 }, (_, i) => `${String(i + 1).padStart(2, '0')}-第${i + 1}章`);
const MANIFEST = ['00-序言', '00-前言', ...chapters, '17-附录'].map(prefix => [findFile(prefix), prefix]);

// ---------- 变换 ----------
function stripVersionRecord(text) {
  const i = text.search(/^##\s*版本变更记录\s*$/m);
  if (i === -1) return text;
  return text.slice(0, i).replace(/\n---\s*\n?$/, '').replace(/\s+$/, '\n');
}

/**
 * 剔除首标题后的元信息引用块（仅序言/前言）——写作契约保留在源文件，不入书。
 * 与「版本变更记录」同属写作元数据；章首导语（第4章/附录等给读者看）不受影响。
 * 结构：`# 标题` + 空行 + `> 元信息` + 空行 + `---`；替换后剩 `# 标题` + 空行 + `---`
 */
function stripLeadingMetaQuote(text, base) {
  if (base !== '00-序言' && base !== '00-前言') return text;
  return text.replace(/^(# .*?)\n\n>.*?\n\n(?=---)/ms, '$1\n\n');
}

function extractMermaid(text, chapterNo) {
  let figCount = 0;
  const chapDisp = String(parseInt(chapterNo, 10) || 0); // 图注用「1-3」非「01-3」
  return text.replace(/```mermaid\s*\n([\s\S]*?)\n```/g, (_m, body) => {
    figCount++;
    const figId = `ch${chapterNo}-fig${String(figCount).padStart(2, '0')}`;
    // 修复裸 &（ch9 "design & evolution"）；已转义实体原样保留
    const cleaned = body.replace(/&(?!amp;|lt;|gt;|quot;|#\d+;|#x[0-9a-fA-F]+;)/g, '&amp;');
    writeFileSync(join(OUT, '.mmd', figId + '.mmd'), cleaned + '\n');
    // 用 PNG（mermaid 的 SVG 含 <foreignObject>，typst 无法渲染；PNG 中文完整、3× 栅格打印清晰）
    return `\n![图 ${chapDisp}-${figCount}](figs/${figId}.png)\n`;
  });
}

function markUnlisted(text, isAppendix) {
  if (isAppendix) return text;
  return text.split('\n').map(line => {
    const m = line.match(/^(\#{2,3})\s+(.+?)\s*$/);
    if (!m) return line;
    const title = m[2].replace(/\s*\{[^}]*\}\s*$/, '').trim();
    // 章首·误解现场（带编号但约定不入目录）或未编号章末件 → 目录排除
    if (title.includes('章首') || !/^\d/.test(title)) return `${m[1]} ${title} {.unlisted}`;
    return line;
  }).join('\n');
}

// ---------- 主循环 ----------
const manifestRows = [];
for (const [srcName, base] of MANIFEST) {
  let text = readFileSync(join(SRC, srcName), 'utf8');
  text = stripVersionRecord(text);
  text = stripLeadingMetaQuote(text, base);
  const chap = base.match(/^(\d+)/)?.[1] ?? '00';
  text = extractMermaid(text, chap);
  text = markUnlisted(text, base === '17-附录');
  writeFileSync(join(OUT, base + '.book.md'), text);
  manifestRows.push(base);
  console.log(`✓ ${srcName} → ${base}.book.md（${(text.length / 1024).toFixed(0)} KB）`);
}
writeFileSync(join(OUT, 'manifest.txt'), manifestRows.join('\n') + '\n');
const mmdCount = readdirSync(join(OUT, '.mmd')).length;
console.log(`manifest.txt: ${manifestRows.length} 文件；mermaid 源 ${mmdCount} 个`);
