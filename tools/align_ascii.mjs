/**
 * align_ascii.mjs — Markdown 文件透传工具
 *
 * 原功能（已移除）：将代码块中的 ASCII 图从 2:1 对齐展开为 1:1 对齐。
 * 该功能已取消——宽度调整不可靠，会引入非预期的布局问题。
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
writeFileSync(outputPath, content, 'utf-8');
console.log(`✅ 已复制: ${inputPath} → ${outputPath}`);
