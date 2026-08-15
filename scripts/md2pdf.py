#!/usr/bin/env python3
"""将 Markdown 文档转换为 PDF（markdown → HTML → 浏览器无头打印）。

用法:
    python scripts/md2pdf.py <输入.md> [输出.pdf]

依赖:
    pip install markdown
    系统需安装 Microsoft Edge 或 Chrome（自动探测路径）。
"""
import os
import subprocess
import sys
import tempfile


def find_browser():
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    raise SystemExit("未找到 Edge/Chrome 浏览器，无法打印 PDF")


CSS = """
@page {
  size: A4;
  margin: 16mm 15mm 18mm 15mm;
}
body {
  font-family: "Microsoft YaHei", "微软雅黑", "PingFang SC", sans-serif;
  font-size: 11pt;
  line-height: 1.65;
  color: #1a1a1a;
}
h1 { font-size: 22pt; text-align: center; margin: 0.4em 0; }
h2 { font-size: 16pt; border-bottom: 2px solid #2c5f8a; padding-bottom: 4px;
     margin: 1.2em 0 0.6em; color: #14395e; }
h3 { font-size: 13.5pt; margin: 1.1em 0 0.5em; color: #1f4e79; }
h4 { font-size: 12pt; margin: 1em 0 0.4em; }
h5, h6 { font-size: 11pt; }
p { margin: 0.5em 0; }
ul, ol { margin: 0.5em 0; padding-left: 1.6em; }
li { margin: 0.2em 0; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 9.5pt; }
th, td { border: 1px solid #bbb; padding: 4px 7px; vertical-align: top; }
th { background: #eef3f8; }
tr { page-break-inside: avoid; }
code {
  font-family: Consolas, "Courier New", "Microsoft YaHei", monospace;
  background: #f4f4f4; padding: 1px 3px; border-radius: 3px; font-size: 0.92em;
}
pre {
  background: #f6f8fa; border: 1px solid #dcdcdc; border-radius: 4px;
  padding: 8px 10px;
  font-family: Consolas, "Microsoft YaHei", "SimHei", monospace;
  font-size: 8.5pt; line-height: 1.35; white-space: pre; overflow: hidden;
}
blockquote {
  margin: 0.6em 0; padding: 2px 12px; border-left: 3px solid #c8a24a;
  background: #fbf8f0; color: #444;
}
strong { font-weight: bold; }
hr { border: none; border-top: 1px solid #ccc; margin: 1.2em 0; }
"""


def md_to_html(src_md, dst_html):
    import markdown

    with open(src_md, encoding="utf-8") as f:
        text = f.read()
    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists"],
    )
    html = (
        '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n'
        '<meta charset="utf-8">\n'
        f"<style>{CSS}</style>\n</head>\n<body>{body}</body>\n</html>\n"
    )
    with open(dst_html, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = os.path.abspath(sys.argv[1])
    out = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".pdf"
    browser = find_browser()
    with tempfile.TemporaryDirectory() as td:
        html = os.path.join(td, "doc.html")
        md_to_html(src, html)
        url = "file:///" + html.replace("\\", "/")
        cmd = [
            browser,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={out}",
            url,
        ]
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=120)
        except subprocess.CalledProcessError:
            # 旧版浏览器用 --print-to-pdf-no-header
            cmd = [b for b in cmd if b != "--no-pdf-header-footer"]
            cmd.insert(-2, "--print-to-pdf-no-header")
            subprocess.run(cmd, check=True, capture_output=True, timeout=120)
    print("PDF 已生成:", out)


if __name__ == "__main__":
    main()
