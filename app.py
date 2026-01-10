import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Ler os dados do CSV
dados = pd.read_csv("dados.csv")

# Criar o PDF
pdf = canvas.Canvas("relatorio.pdf", pagesize=A4)
largura, altura = A4

# Título
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, altura - 50, "Relatório Automático")

# Conteúdo
pdf.setFont("Helvetica", 12)
y = altura - 100

for index, row in dados.iterrows():
    linha = f"Nome: {row['Nome']} | Valor: R$ {row['Valor']}"
    pdf.drawString(50, y, linha)
    y -= 20

# Finalizar PDF
pdf.save()

print("Relatório gerado com sucesso!")
