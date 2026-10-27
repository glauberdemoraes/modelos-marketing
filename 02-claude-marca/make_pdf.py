from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from xml.sax.saxutils import escape

HERE = Path(__file__).parent
OUT = HERE / '7-prompts-claude-marca.pdf'
URL = 'https://github.com/glauberdemoraes/modelos-marketing'
pdfmetrics.registerFont(TTFont('Arial', r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', r'C:\Windows\Fonts\arialbd.ttf'))
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCustom', fontName='Arial-Bold', fontSize=22, leading=27, textColor=HexColor('#15233a'), spaceAfter=16))
styles.add(ParagraphStyle(name='IntroCustom', fontName='Arial', fontSize=10.5, leading=15, textColor=HexColor('#263548'), spaceAfter=10))
styles.add(ParagraphStyle(name='PromptCustom', fontName='Arial', fontSize=10.3, leading=15, textColor=HexColor('#17263b'), spaceAfter=13))
styles.add(ParagraphStyle(name='SmallCustom', fontName='Arial', fontSize=9.5, leading=13, textColor=HexColor('#43546b'), spaceAfter=10))

def para(s, style='PromptCustom'):
    return Paragraph(s, styles[style])

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

doc = SimpleDocTemplate(str(OUT), pagesize=A4, leftMargin=42, rightMargin=42, topMargin=42, bottomMargin=61,
                        title='7 prompts para usar Claude sem copiar outra marca', author='Glauber Moraes Mkt')
story = [para('7 prompts para usar Claude<br/>sem copiar outra marca', 'TitleCustom')]
story.append(para('<b>Antes de começar.</b> Separe sua bio, cinco posts seus, três marcas de referência e comentários de clientes sem dados pessoais. Envie esse material ao Claude. Use os prompts na ordem e revise as respostas antes de publicar.', 'IntroCustom'))
items = [
    ('1. Padrões verificáveis', 'Com base APENAS nos materiais fornecidos, identifique até três temas recorrentes de cada marca. Para cada tema, cite o trecho, post ou arquivo que o sustenta. Sem evidência, escreva “não demonstrado”. Separe observação de hipótese.'),
    ('2. Sinal visual', 'Compare cores, enquadramento e elementos repetidos nas referências. Sugira três combinações diferentes para [minha marca], compatíveis com [meus recursos]. Explique como cada uma evita copiar uma referência.'),
    ('3. Opinião própria', 'Leia meus posts e encontre uma ideia do mercado que eu já contestei com exemplo real. Formule três versões curtas. Se meus materiais não mostrarem essa posição, faça perguntas antes de escrever.'),
    ('4. Promessa concreta', 'Reescreva minha oferta [colar oferta] em uma frase: para quem é, mudança observável buscada e limite da promessa. Evite resultado garantido ou prazo sem comprovação.'),
    ('5. Origem', 'Com base neste relato [colar relato], monte uma história de até 120 palavras: problema visto de perto, decisão tomada e método atual. Não invente eventos, números nem falas. Liste dúvidas a confirmar.'),
    ('6. Cliente ideal', 'A partir de [conversas anonimizadas], descreva situação de compra, objeções reais, critérios de escolha e sinal observável de progresso. Separe o que aparece nos dados do que precisa ser entrevistado.'),
    ('7. Síntese e teste', 'Junte os resultados em uma página: ideia central, opinião, promessa, sinal visual, tom, público e três posts. Marque o que ficou parecido demais com uma referência. Proponha um teste de 30 dias com uma métrica simples.'),
]
for title, body in items:
    story.append(KeepTogether([para(f'<font color="#e45b22"><b>{escape(title)}</b></font><br/>{escape(body)}'), Spacer(1, 2)]))
story.append(para('<b>Mini instruções.</b> Escolha uma versão, publique três conteúdos com a mesma ideia central e peça a uma pessoa do público que diga o que entendeu da sua oferta. Ajuste a partir da resposta.', 'SmallCustom'))
story.append(para(f'Mais modelos e versão editável: <link href="{URL}" color="#235aa6">{URL}</link>', 'SmallCustom'))
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT)
