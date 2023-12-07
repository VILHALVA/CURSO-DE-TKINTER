from tkinter import *

def mover_esquerda():
    r1.place(x=r1.winfo_x() - 10, y=r1.winfo_y())

def mover_direita():
    r1.place(x=r1.winfo_x() + 10, y=r1.winfo_y())

janela = Tk()
janela.title("Exemplo de Place")
janela.geometry("500x500")

# Criando um rótulo inicial
r1 = Label(janela, text="Movimente-me!")
r1.place(x=50, y=50)

# Criando botões para mover o rótulo
botao_esquerda = Button(janela, text="Mover para a Esquerda", command=mover_esquerda)
botao_esquerda.place(x=30, y=100)

botao_direita = Button(janela, text="Mover para a Direita", command=mover_direita)
botao_direita.place(x=180, y=100)

janela.mainloop()
