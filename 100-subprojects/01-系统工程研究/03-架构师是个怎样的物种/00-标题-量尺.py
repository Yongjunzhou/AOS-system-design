#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《架构师是个怎样的物种？》标题量尺（口径 v1，块题／节题层）

用途：块题与节题的自查与清单产出。**这是标题层病种的单一量尺**——写作方与审查方共用；
     口径变更必须先改本文件并在 `00-逐章修订手册.md` §2.6 留痕（"量法本身就是判据"）。

口径 v1（2026-10-17 立；配套 `00-风格参考.md` §6.8 四律、手册 §2.6 七条硬规则与判据⑥）
- 读数单位：**汉字** `[\\u4e00-\\u9fff]`；编号（`1.2`）、标点、拉丁字母与阿拉伯数字不计。
- 层级：块题＝`N.M`（含 `N.1 引言`）／节题＝`N.M.K`；章题＝`第N章 …`。
- 八类病（机扫；**判读仍在人**——本尺只报，不判"该不该改"）：
  ① 四问名块题（以 是什么／不是什么／怎么用／怎么做成 收尾；手册 §2.6 规则 5 明禁）
  ② 阿拉伯数字
  ③ 顿号并列（≥2 个 `、`）
  ④ 问号（**只报不判**：节题层允许问句，见 `feedback-标题易懂优先.md`）
  ⑤ 指代（它／这／那／此 等；题面单独读到不知指谁的才违，需人工判）
  ⑥ 超 15 汉字
  ⑦ 与本章章题撞句（块／节题与章题副题同句，或章题副题被原样复现）
  ⑧ 与正文首句重复（题面在冒号后那一句里**原样出现**）
- 另报：**目录 ↔ 正文标题逐字差异**（按章），以及各章块题/节题条数。

用法：在本目录下 `python 00-标题-量尺.py`（只读，不改文件）。
"""
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BOOK = os.path.dirname(os.path.abspath(__file__))
HAN = re.compile(r'[\u4e00-\u9fff]')
TOC = os.path.join(BOOK, '00-目录.md')

RE_CH = re.compile(r'^\s*- \*\*第(\d+)章\s+(.+?)\*\*\s*$')
RE_SEC = re.compile(r'^(\s+)- ((\d+)\.(\d+)(?:\.(\d+))?) (.+?)\s*$')
RE_H2 = re.compile(r'^## ((\d+)\.(\d+)) (.+?)\s*$')
RE_H3 = re.compile(r'^### ((\d+)\.(\d+)\.(\d+)) (.+?)\s*$')
FOURQ = ('是什么', '不是什么', '怎么用', '怎么做成')
PRON = ['它', '这', '那', '此']
TEMPLATE = ('误解现场', '本章要回答什么', '本章的骨架', '认知反转', '小结', '附录')


def han(s):
    return len(HAN.findall(s))


def parse_toc():
    chapters, blocks, subs = {}, [], []
    cur = None
    with open(TOC, encoding='utf-8') as f:
        for line in f:
            m = RE_CH.match(line.rstrip('\n'))
            if m:
                cur = int(m.group(1))
                chapters[cur] = m.group(2)
                continue
            m = RE_SEC.match(line.rstrip('\n'))
            if m and cur:
                num = m.group(2)
                title = m.group(6)
                item = (cur, num, title)
                if m.group(5):
                    subs.append(item)
                else:
                    blocks.append(item)
    return chapters, blocks, subs


def chapter_files():
    out = {}
    for name in os.listdir(BOOK):
        m = re.match(r'^(\d\d)-第(\d+)章-(.+)\.md$', name)
        if m and '分析' not in name:
            out[int(m.group(2))] = os.path.join(BOOK, name)
    return out


def body_titles(path):
    """返回 [(号, 题面, 级别, 该节首句)]"""
    rows = []
    with open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')
    for i, line in enumerate(lines):
        m = RE_H2.match(line)
        lvl = 'block'
        if not m:
            m = RE_H3.match(line)
            lvl = 'sub'
        if not m:
            continue
        num = m.group(1)
        title = line.split(' ', 2)[2] if line.count(' ') >= 2 else ''
        title = re.sub(r'^#{2,3} ', '', line).strip()
        title = title[len(num):].strip()
        first = ''
        for j in range(i + 1, min(i + 12, len(lines))):
            t = lines[j].strip()
            if not t or t.startswith('#') or t.startswith('|') or t.startswith('>') or t.startswith('```') or t.startswith('---'):
                continue
            first = t
            break
        rows.append((num, title, lvl, first))
    return rows


def main():
    chapters, blocks, subs = parse_toc()
    files = chapter_files()
    print('=' * 78)
    print('标题量尺（口径 v1）—— 章 %d／块题 %d／节题 %d' % (len(chapters), len(blocks), len(subs)))
    print('=' * 78)

    stats = {'block': 0, 'sub': 0}
    flags = {'四问名块题': [], '阿拉伯数字': [], '顿号并列': [], '问号': [],
             '指代': [], '超15字': [], '撞章题': [], '首句复现': []}
    body_map = {}
    for ch, path in files.items():
        body_map[ch] = body_titles(path)

    def scan(ch, num, title, kind):
        stats[kind] += 1
        n = han(title)
        tag = '块' if kind == 'block' else '节'
        label = '%s %s（%d字）' % (num if num else '', title, n)
        if kind == 'block' and title.rstrip('。').endswith(FOURQ):
            flags['四问名块题'].append('%s%s' % (('第%d章 ' % ch) if kind == 'block' else '', label))
        if re.search(r'[0-9]', title):
            flags['阿拉伯数字'].append('第%d章 %s' % (ch, label))
        if title.count('、') >= 2:
            flags['顿号并列'].append('第%d章 %s' % (ch, label))
        if '？' in title or '?' in title:
            flags['问号'].append('第%d章 %s' % (ch, label))
        for p in PRON:
            if p in title:
                flags['指代'].append('第%d章 %s  ←「%s」' % (ch, label, p))
                break
        if n > 15:
            flags['超15字'].append('第%d章 %s' % (ch, label))
        cht = chapters.get(ch, '')
        if '：' in cht:
            sub = cht.split('：', 1)[1]
            if sub and (sub in title or (title in sub and len(title) >= 4)):
                flags['撞章题'].append('第%d章 %s  ←章题副题「%s」' % (ch, label, sub))
        for bnum, btitle, blvl, first in body_map.get(ch, []):
            if bnum == num and first:
                core = title.rstrip('。')
                if core and core in first:
                    flags['首句复现'].append('第%d章 %s  ←首句「%s…」' % (ch, label, first[:28]))
                break

    for ch, num, title in sorted(blocks):
        if title in TEMPLATE:
            continue
        scan(ch, num, title, 'block')
    for ch, num, title in sorted(subs):
        if title in TEMPLATE:
            continue
        scan(ch, num, title, 'sub')

    print('\n【规模】块题 %d 条（含引言 %d）｜节题 %d 条' % (
        stats['block'], sum(1 for c, n, t in blocks if t == '引言'), stats['sub']))
    over = len(flags['超15字'])
    print('【长度】超 15 汉字：%d 条' % over)

    order = ['四问名块题', '阿拉伯数字', '顿号并列', '问号', '指代', '超15字', '撞章题', '首句复现']
    print('\n【按病种】' + '　'.join('%s %d' % (k, len(flags[k])) for k in order))
    for k in order:
        print('\n—— %s（%d）——' % (k, len(flags[k])))
        for row in flags[k]:
            print('   ' + row)

    print('\n【目录 ↔ 正文 逐字差异】')
    diff = 0
    for ch in sorted(files):
        toc_titles = set()
        for c, num, t in blocks:
            if c == ch:
                toc_titles.add(num + ' ' + t)
        for c, num, t in subs:
            if c == ch:
                toc_titles.add(num + ' ' + t)
        body = set()
        for num, title, lvl, first in body_map[ch]:
            body.add(num + ' ' + title)
        only_toc = sorted(toc_titles - body)
        only_body = sorted(body - toc_titles)
        if only_toc or only_body:
            print('  第%d章：目录多 %d／正文多 %d' % (ch, len(only_toc), len(only_body)))
            for x in only_toc:
                print('     目录独有 ' + x)
            for x in only_body:
                print('     正文独有 ' + x)
            diff += len(only_toc) + len(only_body)
    print('  合计差异 %d 处' % diff)


if __name__ == '__main__':
    main()
