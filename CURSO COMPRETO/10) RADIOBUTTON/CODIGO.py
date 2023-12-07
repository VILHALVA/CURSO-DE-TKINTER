from tkinter import *

class BebidaApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Escolha de Bebida")

        # Variável StringVar para armazenar a opção selecionada
        self.variavel_bebida = StringVar()

        # Criando os Radiobuttons
        self.radio_coca_cola = Radiobutton(janela, text="Coca-Cola", variable=self.variavel_bebida, value="Coca-Cola")
        self.radio_pepsi = Radiobutton(janela, text="Pepsi", variable=self.variavel_bebida, value="Pepsi")
        self.radio_guarana = Radiobutton(janela, text="Guaraná", variable=self.variavel_bebida, value="Guaraná")

        # Botão para exibir a opção selecionada
        self.botao_exibir = Button(janela, text="Exibir Bebida", command=self.exibir_bebida)

        # Rótulo para exibir a opção selecionada
        self.label_resultado = Label(janela, text="")

        # Posicionando os widgets
        self.radio_coca_cola.pack(pady=5)
        self.radio_pepsi.pack(pady=5)
        self.radio_guarana.pack(pady=5)
        self.botao_exibir.pack(pady=10)
        self.label_resultado.pack(pady=10)

    def exibir_bebida(self):
        bebida_selecionada = self.variavel_bebida.get()
        resultado_texto = f"Bebida Selecionada: {bebida_selecionada}"
        self.label_resultado.config(text=resultado_texto)

# Criando a janela principal
janela = Tk()

# Criando uma instância da aplicação
app = BebidaApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
