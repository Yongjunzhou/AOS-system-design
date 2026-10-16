#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""《架构师是个怎样的物种？》比喻密度体检（口径 v1，2026-10-16 重建）

**用途**：量"术语化比喻词"的命中、密度、在用套数与单章并用套数——对应
`00-风格参考.md` §3.5（本书语体指纹）与 §6.4（比喻准入·纪律 2／纪律 3）。

**★ 重建说明（必须先读）**：2026-09-26 首次测量所用脚本
（`.work-style/audit_metaphor_density.py`，原输出 2125 次／5.52 次每千字／39 词／28 套）**已丢失、
全仓库无副本**；本次按 `00-风格参考.md` §3.5 的可见词表（24 词）＋ §6.4 与
`claude-memory/pending-metaphor-audit.md` 点名的装饰型比喻词，**重建为 39 词**并把词表写死在本文件里。
故：**本脚本的输出是"重建后的新基线"，与 2026-09-26 那组读数不可直接比较**（词表来源不同、阈值定义不同）。

口径
- 计量单位：汉字 `[\\u4e00-\\u9fff]`；**分母＝章主体**（剔除「参考文献」「版本变更记录」块），
  与随库量尺 `00-风格参考-量尺.py` 同口径。
- **命中**：词表逐词在正文里的出现次数之和（允许重叠计数；不做词形归并）。
- **密度**：命中次数 ÷（章主体汉字 ÷ 1000）。
- **在用套数**：全书命中 **≥10 次**的比喻词个数（＝"在用系统"）。
- **单章并用套数**：该章命中 **≥3 次**的比喻词个数（排除偶发一次）。
- **明喻连接词**：像／好像／如同／仿佛／犹如／好比／宛如／似的／一样（次/千字）——"类比多"不等于"像……一样"多。

用法：在本书目录下 `python 00-风格参考-比喻量尺.py`。**本文件是随库正本**（与 `00-风格参考-量尺.py` 同地位）；
`.work-style/audit_metaphor_density.py` 是采集现场的同一份副本。
"""
import os
import re
import glob
import statistics
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BOOK = os.path.dirname(os.path.abspath(__file__))   # ★ 随库正本：本文件与 18 章正文同目录
HAN = re.compile(r'[\u4e00-\u9fff]')
SKIP = ['参考文献', '版本变更记录']

# ── 39 词词表（① 前 24 词逐字取自 00-风格参考.md §3.5 可见词表；② 后 15 词取自 §6.4 与隐喻审计记忆点名的装饰型）──
WORDS = [
    # ① §3.5 可见词表（24）
    '尺子', '标尺', '地基', '基座', '承重柱', '闸门', '免疫系统', '流水线', '工位', '工件', '法庭',
    '地图', '枢纽', '锚点', '投影', '抽屉', '骨架', '枝干', '枝梢', '叶节点', '接缝', '过滤器', '门槛', '镜照',
    # ② §6.4／pending-metaphor-audit 点名（15）
    '杠杆', '方向盘', '承重件', '看门人', '试金石', '冰山', '菜谱', '掌舵', '划桨', '力量倍增器',
    '磨边', '分形', '传送带', '里程桩', '收费站',
]
SIMILE = ['好像', '如同', '仿佛', '犹如', '好比', '宛如', '似的', '像']   # 取最长匹配，不重复计数
SIMILE_RE = re.compile('|'.join(SIMILE))


def han(s):
    return len(HAN.findall(s))


def blocks(path):
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


def chapters(root):
    for f in sorted(glob.glob(os.path.join(root, '*.md'))):
        n = os.path.basename(f)
        if re.match(r'\d\d-第\d+章', n) and '从教材到问题分析' not in n:
            yield n[:2], f


rows = []
for ch, path in chapters(BOOK):
    text = '\n'.join(b for h, b in blocks(path) if not any(k in h for k in SKIP))
    tot = han(text)
    hits = {w: text.count(w) for w in WORDS}
    sm = len(SIMILE_RE.findall(text))
    rows.append(dict(ch=ch, tot=tot, hits=hits, n=sum(hits.values()), sm=sm,
                     sets=sum(1 for v in hits.values() if v >= 3)))

book_tot = sum(r['tot'] for r in rows)
book_hit = sum(r['n'] for r in rows)
book_sm = sum(r['sm'] for r in rows)
dens = lambda r: 1000.0 * r['n'] / r['tot'] if r['tot'] else 0.0

print('=== 比喻密度体检（口径 v1·2026-10-16 重建；词表 %d 词，已写死在本脚本） ===' % len(WORDS))
print('章   总汉字   命中   密度/千字   单章并用套数(≥3 次)   明喻/千字')
for r in rows:
    print('{}  {:>6}  {:>5}  {:>10.2f}  {:>18}  {:>9.2f}'.format(
        r['ch'], r['tot'], r['n'], dens(r), r['sets'], 1000.0 * r['sm'] / r['tot']))
print('—' * 68)
print('全书：汉字 {}｜命中 {} 次｜密度 {:.2f} 次/千字（章中位 {:.1f}）｜明喻 {:.2f} 次/千字（章中位 {:.2f}）'.format(
    book_tot, book_hit, 1000.0 * book_hit / book_tot,
    statistics.median([dens(r) for r in rows]),
    1000.0 * book_sm / book_tot,
    statistics.median([1000.0 * r['sm'] / r['tot'] for r in rows])))

print()
print('=== ① 在用套数（全书命中 ≥10 次＝"在用系统"） ===')
inuse = sorted(((w, sum(r['hits'][w] for r in rows)) for w in WORDS), key=lambda x: -x[1])
print('命中 ≥10 次的词：%d 个' % sum(1 for _, v in inuse if v >= 10))
print('  ' + '／'.join('%s %d' % (w, v) for w, v in inuse if v >= 10))
print('命中 1~9 次的词：' + '／'.join('%s %d' % (w, v) for w, v in inuse if 0 < v < 10))
print('全书零命中：' + '／'.join(w for w, v in inuse if v == 0))

print()
print('=== ② 单章并用套数排行（≥3 次记一套） ===')
for r in sorted(rows, key=lambda r: -r['sets'])[:6]:
    top = sorted(((w, v) for w, v in r['hits'].items() if v >= 3), key=lambda x: -x[1])
    print('  ch{}  {} 套：{}'.format(r['ch'], r['sets'], '／'.join('%s %d' % t for t in top)))

print()
print('=== ③ 密度排行 ===')
for r in sorted(rows, key=lambda r: -dens(r))[:6]:
    print('  ch{}  {:.2f} 次/千字'.format(r['ch'], dens(r)))
print('  最疏：', '／'.join('ch{} {:.2f}'.format(r['ch'], dens(r))
                          for r in sorted(rows, key=dens)[:3]))
print()
print('注：本脚本为 2026-10-16 重建件（原脚本丢失）；输出为**新基线**，与 2026-09-26 那组读数不可直接比较。')
