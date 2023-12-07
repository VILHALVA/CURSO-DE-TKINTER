from tkinter import *

# Funções chamadas pelos botões
def botao1_clicado():
    label.config(text="Botão 1 Clicado!")

def botao2_clicado():
    label.config(text="Botão 2 Clicado!")
    
def botao3_clicado():
    label.config(text="Botão 3 Clicado!")

# Criação da janela principal
janela = Tk()
janela.title("Exemplo de Botões")

# Rótulo inicial
label = Label(janela, text="Pressione um botão.")
label.pack()

# Botão 1
botao1 = Button(janela, text="Botão 1", bg="green", fg="blue", width="10", command=botao1_clicado)
botao1.pack(side=LEFT, padx=10)

# Botão 2
botao2 = Button(janela, text="Botão 2", bg="red", fg="white", width="30", command=botao2_clicado)
botao2.pack(side=RIGHT, padx=10)

# Botão 3
botao3 = Button(janela, text="Botão 3", bg="yellow", fg="black", width="20", height="20", command=botao3_clicado)
botao3.pack(side=RIGHT, padx=13)

# Inicia o loop principal da aplicação
janela.mainloop()
