"""公共工具：时间格式、文件名、JSON 读写、日志。"""
from __future__ import annotations

import json
import os
import re
import sys
import unicodedata


def setup_console() -> None:
    """把标准输出/错误切到 UTF-8。

    日志里全是中文与「—／≈／≥」这类符号，Windows 上输出被重定向到文件时默认按
    本地代码页（cp936）编码，会直接抛 UnicodeEncodeError。Windows 与 POSIX 都无害。
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def log(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def ts(sec: float) -> str:
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


def srt_ts(sec: float) -> str:
    h, rem = divmod(int(sec * 1000), 3600000)
    m, rest = divmod(rem, 60000)
    s, ms = divmod(rest, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def read_json(path: str, default=None):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, obj) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def slugify(s: str, maxlen: int = 40) -> str:
    """把标题压成可做文件名的短串：去装饰符号、去相邻的短拉丁串、截断。

    例：「张小珺Jùn｜商业访谈录」→「张小珺商业访谈录」。
    """
    s = unicodedata.normalize("NFKD", s)
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    s = unicodedata.normalize("NFKC", s)
    # 紧贴中文的短拉丁串多是英文名点缀（Jùn、FM 之类），去掉
    s = re.sub(r"(?<=[\u4e00-\u9fff])[A-Za-z]{1,3}(?=[\u4e00-\u9fff｜|])", "", s)
    s = re.sub(r"[\\/:*?\"<>|｜·、，。！？；：“”‘’（）()\[\]【】《》\s]+", "", s)
    # Windows 上文件名不能以点或空格结尾，也不能是保留设备名
    s = s.rstrip(". ")
    if s.upper().split(".")[0] in {"CON", "PRN", "AUX", "NUL", *(f"COM{i}" for i in range(1, 10)),
                                   *(f"LPT{i}" for i in range(1, 10))}:
        s = "_" + s
    return s[:maxlen]


def next_index(outdir: str) -> int:
    """扫描输出目录里已有的 NN- 前缀，返回下一个可用编号。"""
    nums = []
    if os.path.isdir(outdir):
        for name in os.listdir(outdir):
            m = re.match(r"^(\d+)-", name)
            if m:
                nums.append(int(m.group(1)))
    return max(nums) + 1 if nums else 0


def chunk_windows(items, size: int):
    """把 [(start, end, text)] 按累计字符数切成若干窗。"""
    win, cur = [], 0
    for it in items:
        n = len(it[2])
        if cur and cur + n > size:
            yield win
            win, cur = [], 0
        win.append(it)
        cur += n
    if win:
        yield win


def _balance(text: str) -> str | None:
    """若 text 是被截断的 JSON，尝试补齐括号救回来；救不回返回 None。"""
    for cut in range(len(text), 0, -1):
        ch = text[cut - 1]
        if ch not in "}]":
            continue
        frag = text[:cut]
        depth_brace = depth_brack = 0
        instr = esc = False
        for c in frag:
            if instr:
                if esc:
                    esc = False
                elif c == "\\":
                    esc = True
                elif c == '"':
                    instr = False
                continue
            if c == '"':
                instr = True
            elif c == "{":
                depth_brace += 1
            elif c == "}":
                depth_brace -= 1
            elif c == "[":
                depth_brack += 1
            elif c == "]":
                depth_brack -= 1
        if instr or depth_brace < 0 or depth_brack < 0:
            continue
        try:
            return json.loads(frag + "]" * depth_brack + "}" * depth_brace)
        except Exception:
            continue
    return None


def extract_json(text: str):
    """从模型回复里抠出 JSON（兼容 ```json 围栏、前后废话、以及被截断的回复）。"""
    fence = re.search(r"```(?:json)?\s*(.+?)\s*```", text, re.S)
    if fence:
        text = fence.group(1)
    start = min([i for i in (text.find("{"), text.find("[")) if i >= 0] or [-1])
    if start < 0:
        raise ValueError("回复中没有 JSON")
    depth, instr, esc = 0, False, False
    opener = text[start]
    closer = "}" if opener == "{" else "]"
    for i in range(start, len(text)):
        ch = text[i]
        if instr:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                instr = False
            continue
        if ch == '"':
            instr = True
        elif ch == opener:
            depth += 1
        elif ch == closer:
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    salvaged = _balance(text[start:])
    if salvaged is not None:
        return salvaged
    raise ValueError("JSON 不完整")
