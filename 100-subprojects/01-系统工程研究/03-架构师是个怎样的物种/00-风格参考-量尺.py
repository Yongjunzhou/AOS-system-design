#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《架构师是个怎样的物种？》章级配比量尺（口径 v3）

用途：章级语体配比与红线自查。**这是本书配比数字的单一量尺**——写作方与审查方共用，
     口径变更必须先改本文件并在 `00-风格参考.md` §3.3 留痕（"量法本身就是判据"）。

口径 v3（2026-09-26 定；块边界与归类规则自 v2 起未变）
- 计量单位：汉字 `[\\u4e00-\\u9fff]`；**分母＝章主体**（剔除「参考文献」「版本变更记录」；
  自查＋练习外移附录 E 落地后，同步从分母剔除）。
- 块边界：**下一个任意级标题**（`##` 或 `###`）——案例进展块常插在幕中间，只认 `##` 会把
  紧随的论证节误并进"叙事"（v1 曾因此虚高 ch2 22.1／ch8 23.8／ch11 33 个百分点）。
- 归类：章首（标题含"误解现场"）／案例进展（含"案例进展"）／论证（其余正文块）／
  章末核心件（概念总图＋认知反转＋本章判据）／章末可压件（概念总图＋认知反转＋自查＋练习＋小结）。
- 三口径：A＝判据＋可压件（旧表）／B＝判据移出红线（**v1.3 起为红线口径**）／
  C＝再外移"自查＋练习"（拟迁附录 E，落地后可复算）。
- 红线（v1.3）：章首 ≤4%／案例进展合计 ≤12% 且单块 ≤700 汉字／论证 ≥60%／
  可压件 ≤22%／认知反转 硬线 ≤1000、提示线 ≤800；硬门＝同一概念点不得两处各讲一遍（人工判读）。

用法：在本目录下 `python 00-风格参考-量尺.py`。
"""
import os
import re
import glob
import statistics
import sys

if hasattr(sys.stdout, 'reconfigure'):      # Windows 控制台按 UTF-8 输出，防乱码
    sys.stdout.reconfigure(encoding='utf-8')

BOOK = os.path.dirname(os.path.abspath(__file__))
HAN = re.compile(r'[\u4e00-\u9fff]')
SKIP = ['参考文献', '版本变更记录']
KEYS = ['open', 'case', 'argue', 'map', 'reversal', 'criteria', 'selfcheck', 'exercise', 'summary']


def han(s):
    return len(HAN.findall(s))


def kind(h):
    """按标题归类；顺序即优先级。"""
    if any(k in h for k in SKIP):
        return 'skip'
    if '误解现场' in h:
        return 'open'
    if '案例进展' in h:
        return 'case'
    if '概念总图' in h or '能力级' in h:
        return 'map'          # 2026-09-26：「本章的能力级」升为独立节（### B），与总图同归 map 类
    if '认知反转' in h:
        return 'reversal'
    if '本章判据' in h:
        return 'criteria'
    if '自查' in h:
        return 'selfcheck'
    if '练习' in h:
        return 'exercise'
    if '小结' in h:
        return 'summary'
    return 'argue'


def chapters(root):
    for f in sorted(glob.glob(os.path.join(root, '*.md'))):
        n = os.path.basename(f)
        if re.match(r'\d\d-第\d+章', n) and '从教材到问题分析' not in n:
            yield n[:2], f


def blocks(path):
    """按任意级标题切块，返回 [(标题, 正文)]。"""
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
    return out


pc = lambda v, d: 100.0 * v / d if d else 0.0

rows = []
for ch, path in chapters(BOOK):
    a = dict.fromkeys(KEYS, 0)
    big = []
    for h, body in blocks(path):
        k = kind(h)
        if k == 'skip':
            continue
        v = han(body)
        a[k] += v
        if k == 'case' and v > 700:
            big.append(v)
    rows.append(dict(ch=ch, tot=sum(a.values()), big=big, **a))

print('=== ① 逐章语体配比（口径 v3） ===')
print('章   总汉字  章首%  案例%  叙事%  论证%  核心尾%  可压件%(B)  认知反转  案例块>700')
for r in rows:
    core = r['map'] + r['reversal'] + r['criteria']
    press = r['map'] + r['reversal'] + r['selfcheck'] + r['exercise'] + r['summary']
    narr = r['open'] + r['case']
    print('{}  {:>6}  {:>5.1f}  {:>5.1f}  {:>5.1f}  {:>5.1f}  {:>7.1f}  {:>10.1f}  {:>8}  {}'.format(
        r['ch'], r['tot'], pc(r['open'], r['tot']), pc(r['case'], r['tot']), pc(narr, r['tot']),
        pc(r['argue'], r['tot']), pc(core, r['tot']), pc(press, r['tot']), r['reversal'],
        '、'.join(str(v) for v in r['big']) or '—'))

med = lambda k: round(statistics.median([pc(r[k], r['tot']) for r in rows]), 1)
print('—' * 96)
print('中位：章首 {}%  案例 {}%  叙事 {}%  论证 {}%  核心尾件 {}%  可压件%(B) {}%  认知反转 {} 汉字'.format(
    med('open'), med('case'), med('open') and round(statistics.median(
        [pc(r['open'] + r['case'], r['tot']) for r in rows]), 1), med('argue'),
    round(statistics.median([pc(r['map'] + r['reversal'] + r['criteria'], r['tot']) for r in rows]), 1),
    round(statistics.median([pc(r['map'] + r['reversal'] + r['selfcheck'] + r['exercise'] + r['summary'],
                                r['tot']) for r in rows]), 1),
    int(statistics.median([r['reversal'] for r in rows]))))

print()
print('=== ② 三口径下的「章末件占比」 ===')
print('口径 A＝判据＋可压件（旧）｜B＝判据移出红线（v1.3 红线口径）｜C＝再外移自查＋练习（拟迁附录 E）')
print('章    A(旧)     B(现)     C(外移后)')
over_b, over_c = [], []
for r in rows:
    moved = r['selfcheck'] + r['exercise']
    newtot = r['tot'] - moved
    a = pc(r['map'] + r['reversal'] + r['criteria'] + r['selfcheck'] + r['exercise'] + r['summary'], r['tot'])
    b = pc(r['map'] + r['reversal'] + r['selfcheck'] + r['exercise'] + r['summary'], r['tot'])
    c = pc(r['map'] + r['reversal'] + r['summary'], newtot)
    if b > 22:
        over_b.append('ch%s %.1f%%' % (r['ch'], b))
    if c > 22:
        over_c.append('ch%s %.1f%%' % (r['ch'], c))
    print('{}  {:>6.1f}%  {:>7.1f}%  {:>9.1f}%{}'.format(r['ch'], a, b, c, '  ←B 超线' if b > 22 else ''))
print('口径B 超 22%：', '、'.join(over_b) if over_b else '无')
print('口径C 超 22%：', '、'.join(over_c) if over_c else '无')

print()
print('=== ③ 红线自查（超线项汇总） ===')
print('章首 >4%：', '、'.join('ch%s %.1f%%' % (r['ch'], pc(r['open'], r['tot'])) for r in rows
                             if pc(r['open'], r['tot']) > 4) or '无（ch1 5.3% 为方法论章例外，已登记）')
print('案例合计 >12%：', '、'.join('ch%s %.1f%%' % (r['ch'], pc(r['case'], r['tot'])) for r in rows
                               if pc(r['case'], r['tot']) > 12) or '无')
print('论证 <60%：', '、'.join('ch%s %.1f%%' % (r['ch'], pc(r['argue'], r['tot'])) for r in rows
                             if pc(r['argue'], r['tot']) < 60) or '无')
print('可压件 >22%（口径B）：', '、'.join(over_b) if over_b else '无')
print('认知反转 >1000（硬线）：', '、'.join('ch%s %d' % (r['ch'], r['reversal']) for r in rows
                                   if r['reversal'] > 1000) or '无')
print('认知反转 >800（提示线）：', '、'.join('ch%s %d' % (r['ch'], r['reversal']) for r in rows
                                   if r['reversal'] > 800) or '无')
print('案例单块 >700：', '、'.join('ch%s %s' % (r['ch'], '／'.join(str(v) for v in r['big']))
                              for r in rows if r['big']) or '无')
print()
print('注：硬门「同一概念点不得两处各讲一遍」为人工判读，本脚本不判；')
print('    处置顺序＝改口径 → 外移自查＋练习 → 压认知反转 → 去重复 → 才轮到叙事（见 00-风格参考.md §6.1）。')
