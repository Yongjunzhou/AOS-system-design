"""取源：小宇宙单集链接 → 元信息 + 音频文件。

只用标准库（urllib），不引入额外依赖。
"""
from __future__ import annotations

import json
import os
import re
import urllib.request

from .util import log

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def _get(url: str, referer: str | None = None, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    if referer:
        req.add_header("Referer", referer)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fetch_episode(url: str) -> dict:
    """抓小宇宙单集页，返回 {title, podcast, author, duration, audio_url, source}。"""
    html = _get(url).decode("utf-8", "ignore")
    m = re.search(r'id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        raise RuntimeError("页面里没有 __NEXT_DATA__，小宇宙可能改版了")
    data = json.loads(m.group(1))
    ep = data["props"]["pageProps"]["episode"]
    return {
        "title": ep.get("title", "").strip(),
        "podcast": (ep.get("podcast") or {}).get("title", "").strip(),
        "author": (ep.get("podcast") or {}).get("author", "").strip(),
        "duration": ep.get("duration") or 0,
        "audio_url": (ep.get("enclosure") or {}).get("url", ""),
        "source": url,
    }


def download(audio_url: str, dest: str, source: str = "") -> str:
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        log(f"[fetch] 已有音频，跳过下载：{dest}")
        return dest
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    log(f"[fetch] 下载音频 → {dest}")
    data = _get(audio_url, referer=source or "https://www.xiaoyuzhoufm.com/", timeout=900)
    tmp = dest + ".part"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, dest)
    log(f"[fetch] 完成 {len(data)/1048576:.1f} MB")
    return dest


def parse_episode_no(title: str) -> str:
    """从「153. xxx」「E251 xxx」里取期号，取不到返回空串。"""
    m = re.match(r"^\s*(?:第)?(\d+)\s*[.、:：]", title)
    if m:
        return m.group(1)
    m = re.search(r"\bE(\d+)\b", title)
    if m:
        return "E" + m.group(1)
    return ""


def parse_topic(title: str) -> str:
    """去掉期号前缀，保留完整话题（含「和XX聊YY：」这种前缀，由调用方决定怎么用）。"""
    t = re.sub(r"^\s*(?:第)?\d+\s*[.、:：]\s*", "", title).strip()
    t = re.sub(r"^\s*E\d+\s*", "", t).strip()
    return t
