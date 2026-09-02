/**
 * render-fig05-snake.cjs — 图1-5 全书认知链 · 两列蛇形渲染
 *
 * 背景：mermaid 11.16 的 flowchart 子图 direction 指令失效（无法画两列蛇形），
 * 图1-5 改用手绘 SVG（build/assets/ch01-fig05-snake.svg）经无头 Chrome 直渲为 PNG。
 * SVG 即源（md 里已是显式图片引用），改版式改 SVG 后跑 bash build.sh --rerender 即可。
 *
 * 用法：node render-fig05-snake.cjs   （NODE_PATH 指向含 puppeteer-core 的 node_modules）
 */
const { existsSync, mkdirSync } = require('node:fs');
const path = require('node:path');

const CHROME = 'C:/Users/HUAWEI/.cache/puppeteer/chrome/win64-148.0.7778.97/chrome-win64/chrome.exe';
const SRC = path.join(__dirname, 'assets', 'ch01-fig05-snake.svg');
const OUT = path.join(__dirname, 'figs', 'ch01-fig05.png');
// SVG 内在尺寸（viewBox 660×810），3× 输出 = 1980×2430，与 mmdc -s 3 同分辨率
const W = 660, H = 810, SCALE = 3;

let puppeteer;
try { puppeteer = require('puppeteer-core'); }
catch (e) {
  console.error('无法加载 puppeteer-core：请确保 build.sh 设置了 NODE_PATH（npx 缓存目录）');
  throw e;
}

(async () => {
  if (!existsSync(SRC)) throw new Error(`SVG 源缺失：${SRC}`);
  mkdirSync(path.dirname(OUT), { recursive: true });
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: 'new', args: ['--no-sandbox', '--disable-gpu'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: W, height: H, deviceScaleFactor: SCALE });
  await page.goto('file://' + SRC.replace(/\\/g, '/'), { waitUntil: 'load' });
  await new Promise(r => setTimeout(r, 400));
  await page.screenshot({ path: OUT });
  await browser.close();
  console.log(`render-fig05-snake: ${OUT}（${W * SCALE}×${H * SCALE}px）`);
})().catch(e => { console.error(e); process.exit(1); });
