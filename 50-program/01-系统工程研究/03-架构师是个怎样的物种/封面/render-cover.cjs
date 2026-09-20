/**
 * render-cover.cjs — 封面（前封 800 + 书脊 60 → 860×1132）SVG → PNG 预览渲染
 *
 * 源即 SVG（改版式改 SVG 后跑 node render-cover.cjs 即可），与成书管线 `成书/build/render-fig05-snake.cjs` 同法。
 * 用法：node render-cover.cjs   （NODE_PATH 指向含 puppeteer-core 的 node_modules）
 */
const { existsSync } = require('node:fs');
const path = require('node:path');

const CHROME = 'C:/Users/HUAWEI/.cache/puppeteer/chrome/win64-148.0.7778.97/chrome-win64/chrome.exe';
const SRC = path.join(__dirname, '封面-前封书脊.svg');
const OUT = path.join(__dirname, '封面-前封书脊.png');
const W = 860, H = 1132;

let puppeteer;
try { puppeteer = require('puppeteer-core'); }
catch (e) {
  console.error('无法加载 puppeteer-core：请确保 NODE_PATH 指向含 puppeteer-core 的 node_modules（见 build.sh）');
  throw e;
}

(async () => {
  if (!existsSync(SRC)) throw new Error(`SVG 源缺失：${SRC}`);
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--disable-gpu'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
  await page.goto('file://' + SRC.replace(/\\/g, '/'), { waitUntil: 'load' });
  await new Promise(r => setTimeout(r, 500));
  await page.screenshot({ path: OUT });
  await browser.close();
  console.log(`render-cover: ${OUT}（${W}×${H}px）`);
})().catch(e => { console.error(e); process.exit(1); });
