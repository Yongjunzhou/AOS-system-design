/**
 * align_ascii.mjs — 将 Markdown 代码块中的 ASCII 图对齐
 *
 * 对齐策略：
 *   1. 找边框行（含 ┌┐└┘ 的行），记录其中分隔符（┬┴┼）的位置
 *   2. 对内容行，在对应位置的 │ 前补空格
 *   3. 所有行补到和目标长度一致
 *
 * 用法：node align_ascii.mjs <输入.md> [输出.md]
 */

import { readFileSync, writeFileSync } from 'fs';

const inputPath = process.argv[2];
if (!inputPath) { console.error('用法: node align_ascii.mjs <输入.md> [输出.md]'); process.exit(1); }
const outputPath = process.argv[3] || inputPath;
const content = readFileSync(inputPath, 'utf-8');
const lines = content.split('\n');

const result = [];
let inCode = false, codeLines = [];

for (let i = 0; i < lines.length; i++) {
  const L = lines[i];
  if (/^```/.test(L)) {
    if (inCode) {
      result.push(...alignBlock(codeLines));
      result.push(L); codeLines = []; inCode = false;
    } else {
      inCode = true; result.push(L);
    }
    continue;
  }
  inCode ? codeLines.push(L) : result.push(L);
}
if (codeLines.length) result.push(...alignBlock(codeLines));

writeFileSync(outputPath, result.join('\n'), 'utf-8');
console.log(`✅ 已处理: ${inputPath} → ${outputPath}`);

// ───── 对齐核心 ─────

function isDiagram(rows) {
  const v = rows.filter(r => r.trim().length);
  return v.length >= 3 && v.some(r => /[┌┐└┘├┤]/.test(r));
}

function alignBlock(rows) {
  if (!isDiagram(rows)) return rows;

  // 目标宽度 = 最长行
  const target = Math.max(...rows.map(r => r.length));

  // 找边框中的分隔位置：┬ ┴ ┼ 所在列
  const separators = new Set();
  for (const row of rows) {
    for (const ch of ['┬', '┴', '┼']) {
      let idx = -1;
      while ((idx = row.indexOf(ch, idx + 1)) >= 0) separators.add(idx);
    }
  }
  // 去掉首尾（第1列和最后1列不是列分隔，是边框角）
  separators.delete(0);

  if (separators.size === 0) {
    // 没有内部分隔的简单边框，只是右侧补齐
    return rows.map(r => r.padEnd(target, ' '));
  }

  // 内容行对齐：在 separators 位置的 │ 前补空格，对齐到边框的 separator 位置
  const sepList = [...separators].sort((a, b) => a - b);

  return rows.map(row => {
    if (row.length >= target) return row;

    // 找到所有 │ 的位置（跳过第0列和末位的边框）
    const pipes = [];
    for (let j = 0; j < row.length; j++) {
      if (row[j] === '│' && j > 0 && j < row.length - 1) pipes.push(j);
    }

    // 按 separators 对齐每个 │
    let result = row;
    for (let s = 0; s < sepList.length && s < pipes.length; s++) {
      const targetPos = sepList[s];
      const currentPos = pipes[s];
      if (currentPos < targetPos) {
        const need = targetPos - currentPos;
        // 在当前 │ 前插 need 个空格
        result = result.slice(0, currentPos) + ' '.repeat(need) + result.slice(currentPos);
        // 后面的 pipe 位置右移
        for (let p = s + 1; p < pipes.length; p++) pipes[p] += need;
      }
    }

    // 最后补长
    if (result.length < target) result = result.padEnd(target, ' ');
    return result;
  });
}
