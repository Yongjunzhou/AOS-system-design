/**
 * md2pdf — 将 Markdown 文档转换为高质量 PDF
 *
 * 用法：
 *   node md2pdf.js <文档名或路径> [output.pdf]
 *
 * 智能匹配：
 *   - "25"         → 在项目中搜索 **\/25-*.md 或 **\/25*.md
 *   - "引擎"       → 在项目中搜索文件名含"引擎"的 .md
 *   - 相对/绝对路径 → 直接使用
 *
 * 特性：
 *   - 完整 GFM 支持（表格、代码块、任务列表等）
 *   - Mermaid 图表渲染
 *   - A4 排版，适配中文
 */

import { readFileSync, readdirSync, existsSync, statSync } from 'fs';
import { resolve, dirname, basename, extname, join, relative } from 'path';
import { fileURLToPath } from 'url';
import { Marked } from 'marked';
import puppeteer from 'puppeteer';

// ---- 项目根目录（从脚本位置推导） ----
const __dirname = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(__dirname, '../..');

// ---- MIME 类型映射 ----
const MIME_TYPES = {
  '.css': 'text/css',
  '.js':  'application/javascript',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.gif': 'image/gif',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
};

// ============================================================
// 1. CLI 参数解析 + 智能文件匹配
// ============================================================

const args = process.argv.slice(2);
if (args.length === 0 || args.includes('--help') || args.includes('-h')) {
  console.log(`
md2pdf — Markdown → PDF 转换器

用法: node md2pdf.js <输入> [输出.pdf] [选项]

输入支持三种形式：
  数字       如 "25"    → 在项目内搜索 **\/25-*.md 或 **\/25*.md
  关键词     如 "引擎"  → 在项目内搜索文件名包含"引擎"的 .md
  路径       如 doc.md  → 直接使用该文件

选项:
  --list          只列出匹配结果，不转换
  --format A4     页面格式（默认 A4）
  --landscape     横向页面
  --no-mermaid    跳过 Mermaid 渲染
  --help, -h      显示此帮助

示例:
  node md2pdf.js 25
  node md2pdf.js 引擎资产
  node md2pdf.js 25-eos-engine-models
  node md2pdf.js ./docs/design.md --landscape
  `);
  process.exit(args.length === 0 ? 1 : 0);
}

const options = {
  format:    args.includes('--format')    ? args[args.indexOf('--format') + 1] : 'A4',
  landscape: args.includes('--landscape'),
  mermaid:   !args.includes('--no-mermaid'),
  listOnly:  args.includes('--list'),
};

// 提取非选项参数
const positional = args.filter(a => !a.startsWith('--') && !['A4','A3','Letter','Legal'].includes(a));

// ---- 智能搜索：数字 / 关键词 / 路径 ----
const input = positional[0];
let inputPath;

if (!input) {
  console.error('❌ 请指定要转换的文档（数字、关键词或路径）');
  process.exit(1);
}

// 判断是路径还是搜索词
const isPath = input.includes('/') || input.includes('\\') || input.endsWith('.md');
if (isPath && existsSync(input)) {
  // 直接路径
  inputPath = resolve(input);
} else if (isPath) {
  // 像路径但不存在 → 报错
  console.error(`❌ 文件不存在: ${input}`);
  // 尝试搜一下
  console.log(`🔍 尝试搜索...`);
  const hits = searchMdInProject(input.replace(/\.md$/, ''));
  if (hits.length > 0) {
    console.log(`找到 ${hits.length} 个匹配:`);
    hits.forEach((f, i) => console.log(`  ${i + 1}. ${f.rel}`));
  } else {
    console.log('  未找到匹配的 .md 文件');
  }
  process.exit(1);
} else {
  // 搜索词 → 在项目中搜索
  const hits = searchMdInProject(input);

  if (hits.length === 0) {
    console.error(`❌ 未找到匹配 "${input}" 的 .md 文件`);
    process.exit(1);
  }

  if (hits.length === 1) {
    inputPath = hits[0].abs;
    console.log(`🔍 匹配到: ${hits[0].rel}`);
  } else {
    // 多个匹配 → 列出并选择第一个（或让用户指定）
    if (options.listOnly) {
      console.log(`找到 ${hits.length} 个匹配:`);
      hits.forEach((f, i) => console.log(`  ${i + 1}. ${f.rel}`));
      process.exit(0);
    }
    // 尝试精确匹配
    const exact = hits.find(h => basename(h.abs, '.md') === input);
    if (exact) {
      inputPath = exact.abs;
      console.log(`🔍 精确匹配: ${exact.rel}`);
    } else {
      // 取第一个，告知用户
      inputPath = hits[0].abs;
      console.log(`🔍 匹配到 ${hits.length} 个，使用第一个: ${hits[0].rel}`);
      console.log(`  其他匹配:`);
      hits.slice(1, 5).forEach(f => console.log(`    - ${f.rel}`));
      if (hits.length > 5) console.log(`    ... 共 ${hits.length} 个`);
    }
  }
}

// 输出路径
let outputPath;
if (positional[1]) {
  outputPath = resolve(positional[1]);
} else {
  const dir = dirname(inputPath);
  const name = basename(inputPath, extname(inputPath));
  outputPath = resolve(dir, `${name}.pdf`);
}

// ============================================================
// 2. 读取 Markdown 并转换为 HTML
// ============================================================

console.log(`📖 读取: ${relative(PROJECT_ROOT, inputPath)}`);

const mdContent = readFileSync(inputPath, 'utf-8');

// 解析图片引用，转为 base64 data URI（让 puppeteer 直接渲染无需网络）
const mdDir = dirname(inputPath);

const marked = new Marked({
  gfm: true,
  breaks: false,
});

let bodyHtml = marked.parse(mdContent);

// Mermaid 块：<pre><code class="language-mermaid"> → <div class="mermaid">
bodyHtml = bodyHtml.replace(
  /<pre><code class="language-mermaid">([\s\S]*?)<\/code><\/pre>/g,
  (_, code) => `<div class="mermaid">${unescapeHtml(code)}</div>`
);

// 图片引用：<img src="xxx.png"> → 内联 base64
bodyHtml = bodyHtml.replace(
  /<img\s+src="([^"]+)"/g,
  (match, src) => {
    if (src.startsWith('http://') || src.startsWith('https://') || src.startsWith('data:')) {
      return match; // 外部 URL 或已内联，保持原样
    }
    const imgPath = resolve(mdDir, src);
    if (!existsSync(imgPath)) return match;
    try {
      const ext = extname(imgPath).toLowerCase();
      const mime = MIME_TYPES[ext] || 'application/octet-stream';
      const data = readFileSync(imgPath);
      const b64 = data.toString('base64');
      return `<img src="data:${mime};base64,${b64}"`;
    } catch {
      return match;
    }
  }
);

// ============================================================
// 3. CSS 样式表
// ============================================================

const css = `
  @page {
    size: ${options.format} ${options.landscape ? 'landscape' : 'portrait'};
    margin: 20mm 18mm 20mm 18mm;
    @bottom-center {
      content: counter(page);
      font-size: 9pt;
      color: #999;
      font-family: "Microsoft YaHei", sans-serif;
    }
  }

  * { box-sizing: border-box; }

  body {
    font-family: "Microsoft YaHei", "SimSun", "PingFang SC", "Noto Sans SC", sans-serif;
    font-size: 11pt;
    line-height: 1.75;
    color: #1a1a1a;
    max-width: 100%;
  }

  /* ---- 标题 ---- */
  h1 { font-size: 20pt; margin: 1.2em 0 0.4em; padding-bottom: 6px; border-bottom: 2px solid #1a1a1a; page-break-before: always; }
  h1:first-child { page-break-before: avoid; }
  h2 { font-size: 15pt; margin: 1.0em 0 0.3em; padding-bottom: 4px; border-bottom: 1px solid #ccc; page-break-before: always; }
  h3 { font-size: 13pt; margin: 0.8em 0 0.2em; }
  h4 { font-size: 11.5pt; margin: 0.6em 0 0.2em; }
  h5 { font-size: 11pt; margin: 0.5em 0 0.2em; color: #555; }
  h6 { font-size: 11pt; margin: 0.5em 0 0.2em; color: #777; font-weight: normal; }

  /* ---- 段落 ---- */
  p { margin: 0.5em 0; text-align: justify; }

  /* ---- 行内格式 ---- */
  strong { color: #1a1a1a; }
  code {
    font-family: "Cascadia Code", "Fira Code", "Consolas", "Courier New", monospace;
    font-size: 9.5pt;
    background: #f0f0f0;
    padding: 1px 4px;
    border-radius: 3px;
  }
  a { color: #1a6fb5; text-decoration: none; }

  /* ---- 引用块 ---- */
  blockquote {
    margin: 0.6em 0;
    padding: 0.4em 1em;
    border-left: 4px solid #5b9bd5;
    background: #f5f8fc;
    color: #444;
  }
  blockquote p { margin: 0.3em 0; }

  /* ---- 代码块 ---- */
  pre {
    background: #f8f8f8;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    padding: 10px 14px;
    font-size: 9pt;
    line-height: 1.5;
    overflow-x: auto;
    white-space: pre-wrap;
    word-break: break-all;
    page-break-inside: avoid;
  }
  pre code { background: none; padding: 0; }

  /* ---- 表格 ---- */
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.8em 0;
    font-size: 10pt;
    page-break-inside: avoid;
  }
  th, td {
    border: 1px solid #d0d0d0;
    padding: 5px 8px;
    text-align: left;
    vertical-align: top;
  }
  th {
    background: #f0f0f0;
    font-weight: bold;
    white-space: nowrap;
  }
  tr:nth-child(even) td { background: #fafafa; }

  /* ---- 列表 ---- */
  ul, ol { margin: 0.4em 0; padding-left: 1.8em; }
  li { margin: 0.2em 0; }

  /* ---- 水平线 ---- */
  hr { border: none; border-top: 1px solid #ccc; margin: 1.5em 0; page-break-after: avoid; }

  /* ---- Mermaid 图表 ---- */
  .mermaid {
    margin: 1em 0;
    padding: 10px;
    background: #fafcff;
    border: 1px solid #e0e5ec;
    border-radius: 4px;
    text-align: center;
    page-break-inside: avoid;
  }
  .mermaid svg { max-width: 100%; height: auto; }

  /* ---- 打印优化 ---- */
  @media print {
    body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  }
`;

// ============================================================
// 4. 组装 HTML + 渲染 PDF
// ============================================================

const mermaidCdn = 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js';

const html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>${escapeHtml(basename(inputPath, extname(inputPath)))}</title>
<style>${css}</style>
${options.mermaid ? `<script src="${mermaidCdn}"></script>` : ''}
</head>
<body>
${bodyHtml}
${options.mermaid ? `<script>mermaid.initialize({startOnLoad:true, theme:"default", securityLevel:"loose"});</script>` : ''}
</body>
</html>`;

console.log(`🖨️  启动浏览器渲染...`);

const browser = await puppeteer.launch({
  headless: true,
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
});

try {
  const page = await browser.newPage();

  await page.setContent(html, {
    waitUntil: options.mermaid ? 'networkidle0' : 'load',
    timeout: 60000,
  });

  if (options.mermaid) {
    console.log('⏳ 等待 Mermaid 图表渲染...');
    await page.waitForFunction(() => {
      const mermaidEls = document.querySelectorAll('.mermaid');
      if (mermaidEls.length === 0) return true;
      return Array.from(mermaidEls).every(el => el.querySelector('svg'));
    }, { timeout: 30000 }).catch(() => {
      console.warn('⚠️ 部分 Mermaid 图表可能未完成渲染，继续生成 PDF...');
    });
  }

  console.log(`📄 写入 PDF: ${relative(PROJECT_ROOT, outputPath)}`);
  await page.pdf({
    path: outputPath,
    format: options.format,
    landscape: options.landscape,
    printBackground: true,
    displayHeaderFooter: false,
    margin: { top: '20mm', bottom: '20mm', left: '18mm', right: '18mm' },
    preferCSSPageSize: true,
  });

  console.log(`✅ 完成！PDF 已生成: ${relative(PROJECT_ROOT, outputPath)}`);
} finally {
  await browser.close();
}

// ============================================================
// 工具函数
// ============================================================

/**
 * 在项目根目录下递归搜索匹配的 .md 文件
 * @param {string} keyword - 搜索关键词
 * @returns {{abs: string, rel: string}[]}
 */
function searchMdInProject(keyword) {
  const results = [];
  const isNumeric = /^\d+$/.test(keyword);

  walk(PROJECT_ROOT, (absPath, relPath) => {
    if (!absPath.endsWith('.md')) return;
    const name = basename(absPath);
    const nameNoExt = basename(absPath, '.md');

    if (isNumeric) {
      // 数字匹配：文件名以数字开头（如 25-, 25_, 25. 或纯 25）
      const prefix = nameNoExt.split(/[-_.]/)[0];
      if (prefix === keyword) {
        results.push({ abs: absPath, rel: relPath });
      }
    } else {
      // 关键词匹配（不区分大小写）
      const kw = keyword.toLowerCase();
      if (nameNoExt.toLowerCase().includes(kw)) {
        results.push({ abs: absPath, rel: relPath });
      }
    }
  });

  // 跳过 node_modules / .git / .claude
  return results.filter(r =>
    !r.rel.includes('node_modules/') &&
    !r.rel.includes('.git/') &&
    !r.rel.includes('.claude/memory') &&
    !r.rel.startsWith('tools/md2pdf/')
  );
}

/**
 * 递归遍历目录
 */
function walk(dir, callback, _relPrefix = '') {
  let entries;
  try {
    entries = readdirSync(dir, { withFileTypes: true });
  } catch {
    return; // 跳过无权限目录
  }
  for (const ent of entries) {
    const abs = join(dir, ent.name);
    const rel = _relPrefix ? `${_relPrefix}/${ent.name}` : ent.name;
    if (ent.isDirectory()) {
      walk(abs, callback, rel);
    } else if (ent.isFile()) {
      callback(abs, rel);
    }
  }
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function unescapeHtml(text) {
  return text
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&amp;/g, '&');
}
