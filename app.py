import pandas as pd
from PyPDF2 import PdfWriter

# Lê os dados do arquivo CSV
dados = pd.read_csv("dados.csv")

# Cria o objeto PDF
pdf = PdfWriter()

# Cria uma página em branco (tamanho A4)
pdf.add_blank_page(width=595, height=842)

pagina = pdf.pages[0]

# Texto inicial do relatório
texto = "RELATÓRIO AUTOMÁTICO\n\n"

# Adiciona os dados do CSV ao texto
for index, row in dados.iterrows():
    texto += f"Nome: {row['Nome']} | Valor: R$ {row['Valor']}\n"

# Insere o texto no PDF
pagina.insert_text(texto, 50, 800)

# Salva o arquivo PDF
with open("relatorio.pdf", "wb") as arquivo:
    pdf.write(arquivo)

print("Relatório em PDF gerado com sucesso!")
