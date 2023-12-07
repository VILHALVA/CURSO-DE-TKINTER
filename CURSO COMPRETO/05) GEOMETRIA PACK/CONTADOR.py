from tkinter import *

class ContadorApp:
    def __init__(self, janela):
        self.valor_contador = 0

        # Rótulo para exibir o contador
        self.rotulo_contador = Label(janela, text=str(self.valor_contador), font=("Arial", 20))
        self.rotulo_contador.pack(pady=20)

        # Botão para incrementar o contador
        self.botao_incrementar = Button(janela, text="Incrementar", command=self.incrementar)
        self.botao_incrementar.pack(side=LEFT, padx=10)

        # Botão para decrementar o contador
        self.botao_decrementar = Button(janela, text="Decrementar", command=self.decrementar)
        self.botao_decrementar.pack(side=RIGHT, padx=10)

    def incrementar(self):
        self.valor_contador += 1
        self.atualizar_rotulo()

    def decrementar(self):
        self.valor_contador -= 1
        self.atualizar_rotulo()

    def atualizar_rotulo(self):
        self.rotulo_contador.config(text=str(self.valor_contador))

# Criando a janela principal
janela = Tk()
janela.title("Contador App")

# Criando uma instância da aplicação
app = ContadorApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
