import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

dados = pd.read_csv("dados.csv")
total = dados["Valor"].sum()

c = canvas.Canvas("relatorio.pdf", pagesize=A4)
largura, altura = A4

c.setFont("Helvetica-Bold", 16)
c.drawString(50, altura - 50, "Relatório Automático")

y = altura - 100
c.setFont("Helvetica", 11)

for _, row in dados.iterrows():
    c.drawString(50, y, f"Nome: {row['Nome']} - Valor: R$ {row['Valor']}")
    y -= 20

c.setFont("Helvetica-Bold", 12)
c.drawString(50, y - 20, f"Total gerado: R$ {total:.2f}")

c.save()
print("Relatório gerado com sucesso!")
