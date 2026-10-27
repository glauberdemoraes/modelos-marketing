from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = Path(__file__).parent
OUT = HERE / 'modelo-posicionamento.pdf'
URL = 'https://github.com/glauberdemoraes/modelos-marketing'
pdfmetrics.registerFont(TTFont('Arial', r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', r'C:\Windows\Fonts\arialbd.ttf'))
w, h = A4
c = canvas.Canvas(str(OUT), pagesize=A4)
c.setTitle('Modelo de posicionamento em quatro linhas')
c.setAuthor('Glauber Moraes Mkt')

def text(x, y, value, size=11, color='#142338', bold=False):
    c.setFillColor(HexColor(color))
    c.setFont('Arial-Bold' if bold else 'Arial', size)
    c.drawString(x, y, value)

def rule(y):
    c.setStrokeColor(HexColor('#cbd5df'))
    c.setLineWidth(1)
    c.line(48, y, w-48, y)

c.setFillColor(HexColor('#142338'))
c.rect(0, h-155, w, 155, fill=1, stroke=0)
text(48, h-50, 'MODELO PRÁTICO', 12, '#ff914d', True)
text(48, h-88, 'Posicionamento em 4 linhas', 24, '#ffffff', True)
text(48, h-117, 'Explique sua oferta antes de discutir preço.', 12, '#ffffff')
y = h-190
items = [
    ('1  PÚBLICO', 'Ajudo [pessoa ou empresa específica].'),
    ('2  PROBLEMA', 'Ela enfrenta [situação concreta] e busca [mudança desejada].'),
    ('3  CAMINHO', 'Trabalho por meio de [método em até três etapas].'),
    ('4  PRÓXIMO PASSO', 'Se fizer sentido, [ação simples] até [prazo real].'),
]
for title, value in items:
    text(48, y, title, 11, '#e76426', True)
    text(48, y-24, value, 11)
    rule(y-47)
    y -= 84
text(48, y+5, 'EXEMPLO FICTÍCIO', 11, '#e76426', True)
example = [
    'Ajudo lojas de bairro que recebem pedidos pelo WhatsApp,',
    'mas perdem vendas ao demorar para responder. Organizo',
    'respostas frequentes, contatos e retomada de orçamentos',
    'em três etapas. Quer avaliar sua loja? Envie três conversas',
    'sem dados pessoais até sexta para um diagnóstico inicial.'
]
for i, line in enumerate(example):
    text(48, y-20-i*17, line, 10)
y -= 130
text(48, y, 'MINI INSTRUÇÕES', 11, '#e76426', True)
text(48, y-23, 'Preencha as quatro linhas. Leia em voz alta para alguém de fora.', 10)
text(48, y-40, 'Reescreva qualquer trecho vago. Use um prazo que você pode cumprir.', 10)
text(48, y-69, 'Arquivos editáveis e próximos modelos:', 10, '#142338', True)
text(48, y-86, URL, 9, '#235aa6')
c.linkURL(URL, (48, y-90, 390, y-73), relative=0)
text(48, 38, '@glauber.moraes.mkt  |  Material gratuito', 9, '#64748b')
c.save()
print(OUT)
