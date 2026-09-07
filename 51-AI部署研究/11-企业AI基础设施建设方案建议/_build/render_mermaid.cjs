const fs = require('fs');
const path = require('path');
const puppeteer = require('puppeteer');

const CHROME = 'C:\\Users\\HUAWEI\\.cache\\puppeteer\\chrome\\win64-148.0.7778.97\\chrome-win64\\chrome.exe';
const SRC = path.resolve(__dirname, '..', '11-企业AI基础设施建设方案建议.md');
const OUT = __dirname;

const md = fs.readFileSync(SRC, 'utf8');
// 提取所有 ```mermaid ... ``` 块
const blocks = [];
const re = /```mermaid\n([\s\S]*?)```/g;
let m;
while ((m = re.exec(md)) !== null) blocks.push(m[1]);

console.log('mermaid blocks:', blocks.length);

function esc(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

(async () => {
  const html = `<!doctype html><html><head><meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<style>
 body{margin:0;background:#fff}
 .d{width:1600px}
 .d svg{max-width:100%;height:auto}
</style></head><body>
${blocks.map((b, i) => `<div class="d" id="d${i}"><pre class="mermaid">${esc(b)}</pre></div>`).join('\n')}
</body></html>`;
  fs.writeFileSync(path.join(OUT, 'deck.html'), html);

  const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'shell', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1700, height: 1200, deviceScaleFactor: 2 });
  const diag = new Promise((res, rej) => {
    page.on('pageerror', e => rej(new Error('pageerror: ' + e.message)));
    setTimeout(() => rej(new Error('render timeout')), 60000);
  });
  const loadP = page.goto('file://' + path.join(OUT, 'deck.html').replace(/\\/g, '/'), { waitUntil: 'networkidle2' });
  await Promise.race([Promise.all([loadP]), diag]);
  try {
    await page.waitForFunction(() => document.querySelectorAll('.mermaid svg').length >= 1, { timeout: 45000 });
  } catch (e) {
    const err = await page.evaluate(() => (window.mermaid && mermaid.parseError) || 'no mermaid svg');
    console.error('mermaid failed:', err);
  }
  // 等全部 svg 出现
  const want = blocks.length;
  await page.waitForFunction((n) => document.querySelectorAll('.mermaid svg').length >= n, { timeout: 60000 }, want);
  const n = await page.evaluate(() => document.querySelectorAll('.mermaid svg').length);
  console.log('rendered svg:', n);
  for (let i = 0; i < blocks.length; i++) {
    const el = await page.$(`#d${i} .mermaid svg`);
    if (!el) { console.error('missing svg #d' + i); continue; }
    const file = path.join(OUT, `diagram_${String(i + 1).padStart(2, '0')}.png`);
    await el.screenshot({ path: file });
    console.log('saved', file);
  }
  await browser.close();
})().catch(e => { console.error('ERR', e); process.exit(1); });
