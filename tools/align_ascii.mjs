/**
 * align_ascii.mjs — 将 Markdown 代码块中的 ASCII 图从 2:1 对齐展开为 1:1 对齐
 *
 * 原理：源代码的 ASCII 图在中文等宽终端（中文=2列，框线/拉丁=1列）下对齐。
 * md2pdf 用 Courier New（所有字符 1:1），中文被压缩导致偏移。
 * 修复：对每个中文字符/全角标点后补 1 空格，模拟 2 列宽度。
 *
 * 同时将每行补到目标长度（最长行的展开长度），确保分页不打乱布置。
 *
 * 用法：node tools/align_ascii.mjs <输入.md> [输出.md]
 */

import { readFileSync, writeFileSync } from 'fs';

const inputPath = process.argv[2];
if (!inputPath) {
  console.error('用法: node tools/align_ascii.mjs <输入.md> [输出.md]');
  process.exit(1);
}
const outputPath = process.argv[3] || inputPath;
const content = readFileSync(inputPath, 'utf-8');
const lines = content.split('\n');

// ─── 宽字符判断 ───

/** 按 Unicode East Asian Width 判断字符是否占 2 列
 *  参考：https://www.unicode.org/reports/tr11/
 *  只返回明确 Wide (W) 或 Fullwidth (F) 的字符。
 *  Ambiguous (A) 在中文终端中通常也是 2 列，这里也计入。
 */
function isWide(ch) {
  const cp = ch.codePointAt(0);
  // ── Fullwidth (F): U+FF01∼U+FF60, U+FFE0∼U+FFE6 ──
  if (cp >= 0xFF01 && cp <= 0xFF60) return true;
  if (cp >= 0xFFE0 && cp <= 0xFFE6) return true;
  // ── Wide (W) ──
  if (cp >= 0x1100 && cp <= 0x115F) return true;   // Hangul Jamo
  if (cp === 0x2329 || cp === 0x232A) return true;  // ⟨ ⟩
  if (cp >= 0x2E80 && cp <= 0x303E) return true;   // CJK Rad, Kangxi, CJK Sym
  if (cp >= 0x3040 && cp <= 0x33BF) return true;   // Hira/Kata/CJK Comp
  if (cp >= 0x3400 && cp <= 0x4DBF) return true;   // CJK Ext A
  if (cp >= 0x4E00 && cp <= 0xA4CF) return true;   // CJK Unified + Yi
  if (cp >= 0xA960 && cp <= 0xA97C) return true;   // Hangul Jamo
  if (cp >= 0xAC00 && cp <= 0xD7A3) return true;   // Hangul Syllables
  if (cp >= 0xD7B0 && cp <= 0xD7FF) return true;   // Hangul Jamo
  if (cp >= 0xF900 && cp <= 0xFAFF) return true;   // CJK Comp
  if (cp >= 0xFE10 && cp <= 0xFE19) return true;   // Vertical forms
  if (cp >= 0xFE30 && cp <= 0xFE6F) return true;   // CJK Comp Forms
  if (cp >= 0x1B000 && cp <= 0x1B0FF) return true; // CJK Comp
  if (cp >= 0x1F200 && cp <= 0x1F2FF) return true; // Enclosed Ideo
  if (cp >= 0x20000 && cp <= 0x2FFFF) return true; // CJK Ext B/C/D/E
  if (cp >= 0x30000 && cp <= 0x3FFFF) return true; // CJK Ext G
  // ── Ambiguous (A) — 中文终端通常视为 2 列 ──
  if (cp >= 0x2018 && cp <= 0x2019) return true;   // ' '
  if (cp >= 0x201C && cp <= 0x201D) return true;   // " "
  if (cp >= 0x2024 && cp <= 0x2026) return true;   // .‥…
  if (cp >= 0x2030 && cp <= 0x2030) return true;   // ‰
  if (cp >= 0x2032 && cp <= 0x2033) return true;   // ′″
  if (cp >= 0x203B && cp <= 0x203B) return true;   // ※
  if (cp >= 0x2103 && cp <= 0x2103) return true;   // ℃
  if (cp >= 0x2109 && cp <= 0x2109) return true;   // ℉
  if (cp >= 0x2160 && cp <= 0x216B) return true;   // 罗马数字
  if (cp === 0x2215) return true;  // ∕
  if (cp === 0x2225) return true;  // ∥
  if (cp >= 0x2229 && cp <= 0x222A) return true;   // ∩∪
  if (cp >= 0x2235 && cp <= 0x2236) return true;   // ∴∵
  if (cp >= 0x2252 && cp <= 0x2252) return true;   // ≒
  if (cp === 0x2261) return true;  // ≡
  if (cp >= 0x2266 && cp <= 0x2267) return true;   // ≦≧
  if (cp === 0x22A5) return true;  // ⊥
  if (cp === 0x22BF) return true;  // ⊿
  if (cp === 0x2312) return true;  // ⌒
  if (cp === 0x2500) return false; // ─ (框线, N) — 明确指出非宽！
  if (cp === 0x2502) return false; // │ (框线, N)
  // ¥, 〜, · 等常用符号（Ambiguous，中文终端通常宽）
  if (ch === '¥' || ch === '〜' || ch === '·' || ch === '―') return true;
  // ←↑↓→↔↕ — Ambiguous，中文终端算宽
  if (cp >= 0x2190 && cp <= 0x2199) return true;
  return false;
}

/** 判断一行是否为框线边框（全是框线/空格） */
function isBorderLine(s) {
  const visible = s.replace(/\s/g, '');
  if (visible.length < 4) return false;
  const box = (visible.match(/[─│┌┐└┘├┤┬┴┼═║╔╗╚╝╠╣╦╩╬]/g) || []).length;
  return box / visible.length > 0.5;
}

/** 对一行做 2:1→1:1 展开（每个宽字符后补 1 空格） */
function expandLine(line) {
  const out = [];
  for (const ch of line) {
    out.push(ch);
    if (isWide(ch)) out.push(' ');
  }
  return out.join('');
}

/** 判断代码块是否需要展开（有框线的 ASCII 图） */
function isDiagram(rows) {
  const nonEmpty = rows.filter(r => r.trim().length > 0);
  if (nonEmpty.length < 3) return false;
  const borderCount = nonEmpty.filter(isBorderLine).length;
  return borderCount >= 2; // 至少上下两条边框
}

/** 展开代码块并统一行长度 */
function expandBlock(rows) {
  if (!isDiagram(rows)) return rows;

  // 每行展开，取最长为 target
  const expanded = rows.map(expandLine);
  const target = Math.max(...expanded.map(r => r.length));

  return expanded.map(r => {
    if (r.length >= target) return r;
    // 找最后一个列分隔符（│），在其前补空格
    // 这样右列的内容不会被推到右边
    const lastDivider = r.lastIndexOf('│');
    if (lastDivider < 0) return r.padEnd(target, ' ');
    // 在最后一个 │ 前插空格
    return r.slice(0, lastDivider) + ' '.repeat(target - r.length) + r.slice(lastDivider);
  });
}

// ─── 处理文件 ───

const result = [];
let inCode = false;
let codeBlock = [];

for (let i = 0; i < lines.length; i++) {
  const L = lines[i];
  if (/^```/.test(L)) {
    if (inCode) {
      result.push(...expandBlock(codeBlock));
      result.push(L);
      codeBlock = [];
      inCode = false;
    } else {
      inCode = true;
      result.push(L);
    }
    continue;
  }
  inCode ? codeBlock.push(L) : result.push(L);
}
if (codeBlock.length) result.push(...expandBlock(codeBlock));

writeFileSync(outputPath, result.join('\n'), 'utf-8');
console.log(`✅ 已处理: ${inputPath} → ${outputPath}`);
