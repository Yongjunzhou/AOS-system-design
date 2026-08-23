#!/usr/bin/env node
/**
 * fix-typ.mjs — 修补 pandoc 生成的 .typ：
 *   给 figure 内 image() 注入适配 A5 版心的宽度（防溢出、保比例）
 *   pandoc 输出的图片无宽度，SVG 内在尺寸差异极大（宽 1841px ~ 高 984px），
 *   统一 width:100% 会让高图溢出页面。按每图 viewBox 计算 scale 注入 pt 宽度。
 *
 * 用法：node fix-typ.mjs <build目录>
 */
import { readFileSync, writeFileSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const OUT = process.argv[2] || '.';
const MAX_W = (110 / 25.4) * 72;    // 版心宽 110mm → 312.2pt
const MAX_H = (150 / 25.4) * 72;    // 图最大高 150mm → 425.2pt（避免撑满整页）

function pngSize(p) {
  try {
    const b = readFileSync(p);
    // PNG 签名(8) + 长度(4) + "IHDR"(4) → 宽高大端序各 4 字节
    if (b.slice(0, 8).toString('latin1') !== '\x89PNG\r\n\x1a\n') return null;
    return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
  } catch { return null; }
}

for (const f of readdirSync(OUT).filter(f => f.endsWith('.typ'))) {
  const path = join(OUT, f);
  let t = readFileSync(path, 'utf8');
  const orig = t;
  // 剥掉 pandoc 生成的独立 label 行（如 <本章判据>）——各章同名 label 会破坏 outline 定位，
  // 而书内无 @ 交叉引用这些 label，剥离安全
  t = t.replace(/^<[^>\n]+>\n/gm, '');
  t = t.replace(/image\("figs\/([^"]+)", alt: "([^"]*)"\)/g, (m, file, alt) => {
    const sz = pngSize(join(OUT, 'figs', file));
    if (!sz) return m;
    const wpt = sz.w * 0.75;   // px(96dpi) → pt(72dpi)
    const hpt = sz.h * 0.75;
    const scale = Math.min(MAX_W / wpt, MAX_H / hpt, 1);
    const w = wpt * scale;
    return `image("figs/${file}", alt: "${alt}", width: ${w.toFixed(1)}pt)`;
  });
  if (t !== orig) {
    writeFileSync(path, t);
    console.log(`fix-typ: ${f}（注入图片宽度）`);
  }
}
console.log('fix-typ.mjs 完成');
