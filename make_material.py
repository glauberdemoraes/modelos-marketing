"""Render a compact, readable PDF from one material.json. Usage: py -3 make_material.py 03-slug"""
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).parent
folder = ROOT / sys.argv[1]
data = json.loads((folder / 'material.json').read_text(encoding='utf-8'))
out = folder / data['filename']
pdfmetrics.registerFont(TTFont('Arial', r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', r'C:\Windows\Fonts\arialbd.ttf'))
title = ParagraphStyle('title', fontName='Arial-Bold', fontSize=22, leading=27, textColor=HexColor('#13233b'), spaceAfter=12)
body = ParagraphStyle('body', fontName='Arial', fontSize=10.3, leading=14, textColor=HexColor('#263548'), spaceAfter=8)
section = ParagraphStyle('section', fontName='Arial', fontSize=10.1, leading=14, textColor=HexColor('#17263b'), spaceAfter=9)
small = ParagraphStyle('small', fontName='Arial', fontSize=9.5, leading=13, textColor=HexColor('#43546b'), spaceAfter=8)

def p(text, style=body):
    return Paragraph(escape(text).replace('\n', '<br/>'), style)

def footer(c, doc):
    c.saveState()
    w, _ = A4
    c.setStrokeColor(HexColor('#d7dee8'))
    c.line(42, 44, w-42, 44)
    c.setFont('Arial', 8.5)
    c.setFillColor(HexColor('#66768a'))
    c.drawString(42, 29, '@glauber.moraes.mkt  |  Material gratuito')
    c.drawRightString(w-42, 29, str(doc.page))
    c.restoreState()

story = [p(data['title'], title), p(data['intro'])]
for item in data['sections']:
    story.append(KeepTogether([
        Paragraph(f'<font color="#e45b22"><b>{escape(item["heading"])}</b></font>', section),
        p(item['text'], section),
        Spacer(1, 0),
    ]))
story.append(p(data['outro'], small))
repo = 'https://github.com/glauberdemoraes/modelos-marketing'
story.append(Paragraph(f'Mais modelos e arquivos editáveis: <link href="{repo}" color="#235aa6">{repo}</link>', small))
doc = SimpleDocTemplate(str(out), pagesize=A4, leftMargin=42, rightMargin=42, topMargin=38, bottomMargin=55, title=data['title'], author='Glauber Moraes Mkt')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(out)
