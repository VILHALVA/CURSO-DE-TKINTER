from tkinter import *

class BotoesColoridosApp:
    def __init__(self, janela):
        # Botão à ESQUERDA
        self.botao_esquerda = Button(janela, text="ESQUERDA", bg="red", command=self.clique_esquerda)
        self.botao_esquerda.pack(side=LEFT, padx=10)

        # Botão à DIREITA
        self.botao_direita = Button(janela, text="DIREITA", bg="green", command=self.clique_direita)
        self.botao_direita.pack(side=RIGHT, padx=10)

        # Botão ABAIXO
        self.botao_abaixo = Button(janela, text="ABAIXO", bg="blue", command=self.clique_abaixo)
        self.botao_abaixo.pack(side=BOTTOM, pady=10)

        # Botão ACIMA
        self.botao_acima = Button(janela, text="ACIMA", bg="orange", command=self.clique_acima)
        self.botao_acima.pack(side=TOP, pady=10)

    def clique_esquerda(self):
        print("Botão ESQUERDA clicado!")

    def clique_direita(self):
        print("Botão DIREITA clicado!")

    def clique_abaixo(self):
        print("Botão ABAIXO clicado!")

    def clique_acima(self):
        print("Botão ACIMA clicado!")

# Criando a janela principal
janela = Tk()
janela.title("Botoes Coloridos App")

# Criando uma instância da aplicação
app = BotoesColoridosApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
