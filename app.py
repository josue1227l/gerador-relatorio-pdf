import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import date

dados = pd.read_csv("dados.csv")

total = dados["Valor"].sum()

arquivo_pdf = "relatorio.pdf"

c = canvas.Canvas(arquivo_pdf, pagesize=A4)
largura, altura = A4

c.setFont("Helvetica-Bold", 16)
c.drawString(50, altura - 50, "Relatório Automático")

c.setFont("Helvetica", 10)
data_hoje = date.today().strftime("%d/%m/%Y")
c.drawString(50, altura - 80, f"Data de geração: {data_hoje}")

y = altura - 120
c.setFont("Helvetica", 11)

for _, row in dados.iterrows():
    c.drawString(50, y, f"Nome: {row['Nome']} - Valor: R$ {row['Valor']}")
    y -= 20

y -= 20
c.setFont("Helvetica-Bold", 12)
c.drawString(50, y, f"Total gerado: R$ {total:.2f}")

c.save()

print("Relatório gerado com sucesso!")
