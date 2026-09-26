#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《架构师是个怎样的物种？》三条线索核对器

用途：核对三条线索在正文里的落地情况——**明线可机械判**（两件回收件）、
     **暗线给候选位供人工判**（"一份产品数据动一下"是语义判断，脚本只导出末段原文）、
     **案例线给出场矩阵**（按名字出现统计；出现≠有台词，台词级判定以 00-案例设定.md §十 为准）。

用法：`python 00-三条线索-核对.py`（在本目录下运行）。
口径与台账见同目录 `00-三条线索.md`（线索的单一权威）。
"""
import os
import re
import glob
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BOOK = os.path.dirname(os.path.abspath(__file__))
HAN = re.compile(r'[\u4e00-\u9fff]')
SKIP = ['参考文献', '版本变更记录']
MEMBERS = [('冰链', '水忠'), ('冰链', '文正'), ('冰链', '永兵'), ('冰链', '董勐'),
           ('冰链', '李旭'), ('冰链', '逸人'),
           ('恒信', '万辉'), ('恒信', '徐漾'), ('恒信', '满海'),
           ('恒信', '玉杰'), ('恒信', '小白'), ('恒信', '黄程')]
# 主案例章（该线六人应全员在场）
MAIN_ICE = [3, 5, 7, 10, 11, 13]
MAIN_HX = [2, 4, 6, 8, 12, 14, 15, 16]


def chapters():
    out = []
    for f in sorted(glob.glob(os.path.join(BOOK, '*.md'))):
        n = os.path.basename(f)
        if re.match(r'\d\d-第\d+章', n) and '从教材到问题分析' not in n:
            out.append((n[:2], f))
    return out


def blocks(path):
    """按任意级标题切块，返回 [(标题, 正文)]，并剔除参考文献与版本记录。"""
    out, cur_h, cur = [], None, []
    for ln in open(path, encoding='utf-8').read().split('\n'):
        if re.match(r'^#{2,3} ', ln):
            if cur_h is not None:
                out.append((cur_h, '\n'.join(cur)))
            cur_h, cur = re.sub(r'^#+\s*', '', ln).strip(), []
        else:
            cur.append(ln)
    if cur_h is not None:
        out.append((cur_h, '\n'.join(cur)))
    return [(h, b) for h, b in out if not any(k in h for k in SKIP)]


def last_para(text, n=2):
    """取末 n 段：跳过分隔线、表格、围栏；引用块去掉 > 前缀后参与判读。
    取两段是因为**站句常在末段的前一段**（末段多是"下一章……"的转场句）。"""
    out = []
    for blk in reversed([b.strip() for b in text.split('\n\n') if b.strip()]):
        b = '\n'.join(l[1:].strip() if l.startswith('>') else l for l in blk.split('\n')).strip()
        if not b or set(b) <= set('-—_*· \t'):
            continue
        if b.startswith(('|', '```')):
            continue
        out.append(b)
        if len(out) >= n:
            break
    return '  ‖  '.join(reversed(out))


data = []
for ch, path in chapters():
    bl = blocks(path)
    body = '\n'.join(b for _, b in bl)
    rev = next((b for h, b in bl if '认知见转' in h or '认知反转' in h), '')
    summ = next((b for h, b in bl if '小结' in h), '')
    # 收束句自 2026-09-26 起移入章末「本章的能力级」清点块（框架 §五 第 12 条）；
    # 迁到一半的章两处都查，迁完的章查清点块，故取二者之并。
    cap = next((b for h, b in bl if '能力级' in h), '')
    line_src = rev + '\n' + cap
    data.append(dict(
        ch=ch, body=body, rev=rev, summ=summ,
        line=('才算拥有' in line_src) or ('才算真正拥有' in line_src),
        layer='§1.3.5' in body,
        members={m: body.count(m) for _, m in MEMBERS},
    ))

print('=== ① 明线核对（两件回收件，逐章） ===')
print('章  收束句"才算拥有"  §1.3.5 刻度行   所在层级')
for d in data:
    lv = re.search(r'第\s*([①②③④])?\s*层|§1\.3\.5[^\n]{0,40}', d['body'])
    print('{}  {:^14}  {:^14}  {}'.format(
        d['ch'], '✓' if d['line'] else '✗ 缺', '✓' if d['layer'] else '✗ 缺',
        (lv.group(0)[:26].replace('\n', ' ') if lv else '—')))
miss_line = [d['ch'] for d in data if not d['line']]
miss_layer = [d['ch'] for d in data if not d['layer']]
print('收束句缺章：', '、'.join(miss_line) if miss_line else '无（18/18）')
print('刻度行缺章：', '、'.join(miss_layer) if miss_layer else '无（ch2~ch18 共 17/17；ch1 为源章不计）')

print()
print('=== ② 暗线核对（脚本只导出候选位：各章「小结」末两段，供人工判"有没有让一份产品数据动一下"） ===')
for d in data:
    tail = last_para(d['summ']) if d['summ'] else '（本章无小结块）'
    print('{}  {}'.format(d['ch'], tail[:230] if tail else '—'))
print('注：判据＝该段里有没有一份**产品数据物件**被写下／补起／守住；只有"认账"或"判词"的记变体站。')
print('    落点在「案例进展」而非小结的章（ch10／ch15／ch16），本表看不到，须回该章案例进展核。')

print()
print('=== ③ 案例线在场矩阵（按名字出现统计；●=出现 ·=未出现） ===')
hdr = '成员  线   ' + ' '.join('%2s' % d['ch'] for d in data)
print(hdr)
for line_name, m in MEMBERS:
    row = ' '.join(' ●' if d['members'][m] else ' ·' for d in data)
    print('{:4}  {}  {}'.format(m, line_name, row))

print()
print('主案例章全员核对（该线六人是否都出现）:')
for line_name, chs in (('冰链', MAIN_ICE), ('恒信', MAIN_HX)):
    names = [m for ln, m in MEMBERS if ln == line_name]
    for c in chs:
        d = next(x for x in data if int(x['ch']) == c)
        lack = [m for m in names if not d['members'][m]]
        mark = '全员在场' if not lack else '缺：' + '、'.join(lack)
        print('  {} ch{:>2}  {}'.format(line_name, c, mark))
duo_miss = {d['ch']: [m for m in ('满海', '永兵') if not d['members'][m]] for d in data}
print('双线章（ch1/9/17/18）缺场：', {k: v for k, v in duo_miss.items() if v and k in ('01', '09', '17', '18')})

print()
print('注：三条线的口径、台账与维护纪律见 00-三条线索.md；未决项见 claude-memory/pending-three-lines-integrity.md。')
