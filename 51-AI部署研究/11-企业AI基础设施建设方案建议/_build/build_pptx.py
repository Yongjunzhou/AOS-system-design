# -*- coding: utf-8 -*-
"""把 11-企业AI基础设施建设方案建议.md 生成 .pptx（40 页 · 16:9）"""
import re, math, os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, '..', '11-企业AI基础设施建设方案建议.md')
OUT = os.path.join(BASE, '..', '11-企业AI基础设施建设方案建议.pptx')
DIAG = {25: 'diagram_01.png', 27: 'diagram_02.png', 29: 'diagram_03.png',
        30: 'diagram_04.png', 34: 'diagram_05.png', 54: 'diagram_06.png'}

W, H = 13.333, 7.5
C_TOP, C_BOT = 1.52, 6.90
NAVY = RGBColor(0x1F, 0x38, 0x64)
BLUE = RGBColor(0x2E, 0x74, 0xB5)
INK  = RGBColor(0x33, 0x38, 0x3F)
GRAY = RGBColor(0x6B, 0x72, 0x7C)
LIGHT= RGBColor(0xEF, 0xF3, 0xF9)
LINE = RGBColor(0xC9, 0xD6, 0xE8)
WHITE= RGBColor(0xFF, 0xFF, 0xFF)
FONT = '微软雅黑'
PART = {frozenset(range(1, 5)): '开场与口径', frozenset(range(5, 9)): '目的',
        frozenset(range(9, 14)): '目标', frozenset(range(14, 20)): '指标认知（原理与人感）',
        frozenset(range(20, 29)): '需求与量化锚', frozenset(range(29, 38)): '内容（引擎 A · 在线）',
        frozenset(range(38, 45)): '理由 · 构成推导',
        frozenset(range(45, 54)): '引擎 B · 机载专用模型训练（02 号）',
        frozenset(range(54, 57)): '统一推进 · 指标收口 · 汇报收口'}
def part_of(p):
    for k, v in PART.items():
        if p in k:
            return v
    return ''

def cjk_eff(s):
    return sum(1.9 if ord(c) > 0x2E80 else 1.0 for c in s.replace('**', ''))

def _ea(rPr):
    for tag in ('a:ea', 'a:cs'):
        el = rPr.find(qn(tag))
        if el is None:
            el = rPr.makeelement(qn(tag), {})
            rPr.append(el)
        el.set('typeface', FONT)

def style_run(r, text, bold=False, color=INK, size=14):
    r.text = text
    f = r.font
    f.name = FONT; f.bold = bold; f.size = Pt(size); f.color.rgb = color
    _ea(r._r.get_or_add_rPr())

def para_runs(tf, first, runs, size=14, color=INK, space=5, line=1.12,
              align=PP_ALIGN.LEFT, bullet=None, bullet_color=BLUE):
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.line_spacing = line
    p.space_after = Pt(space); p.space_before = Pt(0)
    if isinstance(runs, str):
        runs = [(runs, False)]
    if bullet:
        r = p.add_run(); style_run(r, bullet, False, bullet_color, size)
    for t, b in runs:
        r = p.add_run(); style_run(r, t, b, color, size)
    return p

def split_bold(s):
    parts = s.split('**')
    return [(seg, i % 2 == 1) for i, seg in enumerate(parts) if seg]

def add_textbox(slide, x, y, w, h):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.margin_left = tf.margin_right = Pt(0)
    tf.margin_top = tf.margin_bottom = Pt(0)
    return tf

def add_rect(slide, x, y, w, h, color):
    sp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    sp.fill.solid(); sp.fill.fore_color.rgb = color
    sp.line.fill.background(); sp.shadow.inherit = False
    return sp

def hdr(slide, page, title):
    add_rect(slide, 0, 0, 0.16, H, NAVY)
    add_rect(slide, 0.16, 0, 0.05, H, BLUE)
    tf = add_textbox(slide, 8.9, 0.26, 4.2, 0.3)
    para_runs(tf, True, [('编号 11 · 企业 AI 基础设施建设方案建议', False)],
              size=9, color=GRAY, align=PP_ALIGN.RIGHT, space=0)
    tf = add_textbox(slide, 0.55, 0.36, 8, 0.3)
    para_runs(tf, True, [(part_of(page) + ' · ' + f'{page} / 56', False)],
              size=10.5, color=BLUE, space=0)
    size = 23
    while len(title) * size * 0.0205 > 11.9 and size > 15:
        size -= 1
    tf = add_textbox(slide, 0.55, 0.68, W - 1.2, 0.75)
    para_runs(tf, True, [(title, True)], size=size, color=NAVY, space=0, line=1.0)
    add_rect(slide, 0.56, 1.42, W - 1.12, 0.016, LINE)

def text_paras(lines):
    paras = []
    for ln in lines:
        s = ln.strip()
        m = re.match(r'^(\s*)([-*])\s+(.*)$', ln)
        if m:
            depth = len(m.group(1))
            glyph = ('▪  ' if depth == 0 else ('   –  ' if depth == 1 else '      ·  '))
            paras.append({'pre': glyph, 'runs': split_bold(m.group(3))})
            continue
        m = re.match(r'^(\s*)(\d+[.)])\s+(.*)$', ln)
        if m:
            pad = '   ' * len(m.group(1))
            paras.append({'pre': pad + m.group(2) + '  ', 'runs': split_bold(m.group(3))})
            continue
        paras.append({'pre': '', 'runs': split_bold(s)})
    return paras

def est_paras_h(paras, w, size):
    cap = max(1, w * 72 * 0.96 / (size * 1.0))
    lines = 0
    for pa in paras:
        eff = cjk_eff(pa['pre']) + sum(cjk_eff(t) for t, _ in pa['runs'])
        lines += max(1, math.ceil(eff / cap)) + 0.16
    return lines * size * 1.28 / 72 + 0.06

def render_paras(slide, x, y, w, paras, size, color=INK, space=5):
    tf = add_textbox(slide, x, y, w, max(0.4, est_paras_h(paras, w, size)))
    for j, pa in enumerate(paras):
        p = tf.paragraphs[0] if j == 0 else tf.add_paragraph()
        p.line_spacing = 1.14
        p.space_after = Pt(space); p.space_before = Pt(0)
        if pa['pre']:
            r = p.add_run(); style_run(r, pa['pre'], pa.get('boldpre', False), BLUE, size)
        for t, b in pa['runs']:
            r = p.add_run(); style_run(r, t, b, color, size)
    return tf

def est_table_h(rows, w, fs):
    nc = max(len(r) for r in rows)
    cellw = w / nc
    total = 0.04
    for ri, row in enumerate(rows):
        mx = 1
        for c in row:
            cap = max(1, cellw * 72 * 0.9 / (fs * 1.02))
            mx = max(mx, math.ceil(cjk_eff(c) / cap))
        total += 0.12 + mx * fs * 1.22 / 72 + (0.06 if ri == 0 else 0)
    return total

def render_table(slide, x, y, w, rows, fs):
    nc = max(len(r) for r in rows)
    rows2 = [r + [''] * (nc - len(r)) for r in rows]
    gfx = slide.shapes.add_table(len(rows2), nc, Inches(x), Inches(y), Inches(w), Inches(0.4))
    tbl = gfx.table
    tbl.first_row = False; tbl.horz_banding = False
    for ci in range(nc):
        tbl.columns[ci].width = Inches(w / nc)
    for ri, row in enumerate(rows2):
        rowH = 0.22 + max(1, 1) * 0.18
        tbl.rows[ri].height = Inches(0.3)
        for ci, cell_text in enumerate(row):
            cell = tbl.cell(ri, ci)
            cell.margin_left = cell.margin_right = Inches(0.06)
            cell.margin_top = cell.margin_bottom = Inches(0.02)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            hdrflag = (ri == 0)
            if hdrflag:
                cell.fill.solid(); cell.fill.fore_color.rgb = NAVY
                color, bold = WHITE, True
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = LIGHT if ri % 2 == 0 else WHITE
                color, bold = INK, False
            tfc = cell.text_frame; tfc.word_wrap = True
            runs = split_bold(cell_text) or [('', False)]
            p = tfc.paragraphs[0]
            p.line_spacing = 1.05
            for j, (t, b) in enumerate(runs):
                r = p.add_run() if j > 0 or not p.runs else p.runs[0]
                style_run(r, t, b or bold, color, fs)
    return tbl

def group_band(items):
    """把 items 里连续 text 合并，返回 [(kind, payload)]: text→行列表; table→rows; image"""
    out = []
    for it in items:
        if it[0] == 'image':
            out.append(('image', None)); continue
        if it[0] == 'table':
            out.append(('table', it[1])); continue
        if out and out[-1][0] == 'text':
            out[-1][1].append(it[1])
        else:
            out.append(('text', [it[1]]))
    return out

def est_band_h(band, w, fs):
    h = 0.0
    for kind, pl in band:
        if kind == 'text':
            h += est_paras_h(text_paras(pl), w, fs) + 0.05
        elif kind == 'table':
            h += est_table_h(pl, w, fs - 2.5) + 0.08
        else:
            h += 0.1
    return h

def render_band(slide, band, x, y, w, fs, bottom):
    cur = y
    for kind, pl in band:
        if kind == 'text':
            paras = text_paras(pl)
            hh = est_paras_h(paras, w, fs) + 0.03
            render_paras(slide, x, cur, w, paras, fs, space=5)
            cur += hh
        elif kind == 'table':
            hh = est_table_h(pl, w, fs - 2.5) + 0.06
            render_table(slide, x, cur, w, pl, fs - 2.5)
            cur += hh
    return cur

def cover(slide, note):
    add_rect(slide, 0, 0, W, H, WHITE)
    add_rect(slide, 0, 0, 0.35, H, NAVY)
    add_rect(slide, 0.35, 0, 0.07, H, BLUE)
    tf = add_textbox(slide, 1.0, 1.0, 11, 0.4)
    para_runs(tf, True, [('编号 11   ·   高层汇报稿', False)], size=15, color=BLUE, space=0)
    tf = add_textbox(slide, 1.0, 2.0, 11.8, 1.4)
    para_runs(tf, True, [('企业 AI 基础设施建设', True)], size=52, color=NAVY, space=0, line=1.0)
    tf = add_textbox(slide, 1.0, 3.15, 11.8, 1.2)
    para_runs(tf, True, [('方案建议', True)], size=52, color=NAVY, space=0, line=1.0)
    add_rect(slide, 1.05, 4.55, 3.2, 0.05, BLUE)
    tf = add_textbox(slide, 1.0, 5.0, 11.8, 2.2)
    para_runs(tf, True, [('一个底座，支撑四类企业 AI 需求——产品智能化、产品数据开发、AI 技术研究、AI 办公', False)],
              size=18, color=INK, space=10)
    para_runs(tf, False, [('引擎 A · 在线推理一期 96 卡（12 台 8 卡机）：一次性 CapEx ¥850~1100 万 · 年运营 ¥110~160 万（估算·待询价）', False)],
              size=15, color=GRAY, space=8)
    para_runs(tf, False, [('整体预算边界（A+B 上界，估算·待询价）≈ ¥3000~4400 万 · C 与人力另计（见 P56）', False)],
              size=13, color=GRAY, space=8)
    para_runs(tf, False, [('汇报人 / 2026-09-09', False)], size=12, color=GRAY, space=0)

def place_image(slide, png, x, y, w, h):
    from PIL import Image
    im = Image.open(png); iw, ih = im.size; ar = iw / ih
    bw, bh = w, h
    if bw / bh > ar:
        bw = bh * ar
    else:
        bh = bw / ar
    px = x + (w - bw) / 2
    py = y + (h - bh) / 2
    slide.shapes.add_picture(png, Inches(px), Inches(py), Inches(bw), Inches(bh))

def render(slide, page, items):
    # P27 竖长漏斗：左右双栏特排（左图右文+表），避免漏斗被压窄
    if page == 27:
        band = group_band([it for it in items if it[0] != 'image'])
        xr, wr = 3.75, W - 1.3 - 3.75 + 0.1
        fs = 12
        if est_band_h(band, wr, fs) > (C_BOT - C_TOP):
            fs = 11
        render_band(slide, band, xr, C_TOP, wr, fs, C_BOT)
        place_image(slide, os.path.join(BASE, DIAG[27]), 0.45, C_TOP, 3.0, C_BOT - C_TOP)
        return
    x, w = 0.62, W - 1.3
    has_img = any(it[0] == 'image' for it in items)
    if has_img:
        img_i = [i for i, it in enumerate(items) if it[0] == 'image'][0]
        before = group_band(items[:img_i])
        after = group_band(items[img_i + 1:])
        hb = est_band_h(before, w, 13) if before else 0
        ha = est_band_h(after, w, 11) if after else 0
        img_av = (C_BOT - C_TOP) - hb - ha - 0.22
        img_av = max(1.35, min(img_av, 4.6))
        cur = C_TOP
        if before:
            render_band(slide, before, x, cur, w, 13, C_BOT)
            cur += hb + 0.05
        place_image(slide, os.path.join(BASE, DIAG[page]), x, cur, w, img_av)
        cur += img_av + 0.06
        if after:
            render_band(slide, after, x, cur, w, 11, C_BOT)
        return
    band = group_band(items)
    fs = 14
    if est_band_h(band, w, fs) > (C_BOT - C_TOP) and len(items) > 6:
        fs = 12
    if est_band_h(band, w, fs) > (C_BOT - C_TOP):
        fs = 11
    render_band(slide, band, x, C_TOP, w, fs, C_BOT)

def notes(slide, text):
    if not text:
        return
    tf = slide.notes_slide.notes_text_frame
    tf.text = '讲者备注\n' + text.strip()

# ---------- 解析 ----------
def parse():
    with open(SRC, encoding='utf-8') as f:
        lines = f.read().splitlines()
    slides = []
    cur = None
    i, N = 0, len(lines)
    while i < N:
        ln = lines[i].rstrip()
        m = re.match(r'^## P(\d+)\s*·\s*(.*)$', ln)
        if m:
            if cur:
                slides.append(cur)
            cur = {'page': int(m.group(1)), 'title': m.group(2).strip(),
                   'body': [], 'note': ''}
            i += 1
            continue
        if cur is not None:
            if ln.startswith('> 备注'):
                note_lines = []
                while i < N and lines[i].startswith('>'):
                    note_lines.append(lines[i].lstrip('> '))
                    i += 1
                cur['note'] = '\n'.join(note_lines).strip()
                continue
            if 'mermaid' in ln and ln.startswith('```'):
                i += 1
                while i < N and not lines[i].startswith('```'):
                    i += 1
                cur['body'].append('@IMAGE@')
                i += 1
                continue
            cur['body'].append(ln)
        i += 1
    if cur:
        slides.append(cur)
    for s in slides:
        items = []
        table_buf = []
        def flush():
            if not table_buf:
                return
            rows = []
            for row in table_buf:
                cells = [c.strip() for c in row.strip().strip('|').split('|')]
                if all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                    continue
                rows.append(cells)
            if rows:
                items.append(('table', rows))
            table_buf.clear()
        for ln in s['body']:
            if ln == '@IMAGE@':
                flush(); items.append(('image', None)); continue
            if ln.strip() == '':
                flush(); continue
            if ln.startswith('|'):
                table_buf.append(ln); continue
            flush()
            if ln == '---':
                continue
            items.append(('text', ln))
        flush()
        s['items'] = items
    return slides

def main():
    slides = parse()
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    blank = prs.slide_layouts[6]
    for s in slides:
        page = s['page']
        slide = prs.slides.add_slide(blank)
        if page == 1:
            cover(slide, s['note'])
        else:
            hdr(slide, page, s['title'])
            render(slide, page, s['items'])
        notes(slide, s['note'])
        if page != 1:
            tf = add_textbox(slide, 0.6, 7.12, 8, 0.28)
            para_runs(tf, True, [('企业 AI 基础设施 · 依据 01 号研究报告', False)],
                      size=8.5, color=GRAY, space=0)
            tf = add_textbox(slide, W - 2.4, 7.12, 1.9, 0.28)
            para_runs(tf, True, [(f'{page} / 56', False)], size=8.5, color=GRAY,
                      align=PP_ALIGN.RIGHT, space=0)
    prs.save(OUT)
    print('saved slides:', len(slides))

if __name__ == '__main__':
    main()
