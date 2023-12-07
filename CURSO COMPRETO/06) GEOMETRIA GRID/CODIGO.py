from tkinter import *

janela = Tk()
janela.title("Exemplo de Tabela com Grid")

# Cabeçalhos de coluna
cabecalhos = ["Nome", "Idade", "Cidade"]

# Dados
dados = [
    ["Alice", 25, "Cidade A"],
    ["Bob", 30, "Cidade B"],
    ["Charlie", 22, "Cidade C"],
    ["David", 35, "Cidade D"],
]

# Adiciona cabeçalhos de coluna à tabela
for col, cabecalho in enumerate(cabecalhos):
    Label(janela, text=cabecalho, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=10, pady=5)

# Adiciona dados à tabela
for row, linha in enumerate(dados, start=1):
    for col, valor in enumerate(linha):
        Label(janela, text=str(valor)).grid(row=row, column=col, padx=10, pady=5)

janela.mainloop()
