from tkinter import *

class LanguageApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Escolha de Idioma")

        # Variáveis IntVar para armazenar o estado dos Checkbuttons
        self.var_portugues = IntVar()
        self.var_ingles = IntVar()
        self.var_espanhol = IntVar()

        # Criando os Checkbuttons
        self.check_portugues = Checkbutton(janela, text="Português", variable=self.var_portugues)
        self.check_ingles = Checkbutton(janela, text="Inglês", variable=self.var_ingles)
        self.check_espanhol = Checkbutton(janela, text="Espanhol", variable=self.var_espanhol)

        # Botão para exibir os idiomas selecionados
        self.botao_exibir = Button(janela, text="Exibir Idiomas", command=self.exibir_idiomas)

        # Rótulo para exibir os idiomas selecionados
        self.label_resultado = Label(janela, text="")

        # Posicionando os widgets
        self.check_portugues.pack(pady=5)
        self.check_ingles.pack(pady=5)
        self.check_espanhol.pack(pady=5)
        self.botao_exibir.pack(pady=10)
        self.label_resultado.pack(pady=10)

    def exibir_idiomas(self):
        idiomas_selecionados = []

        if self.var_portugues.get() == 1:
            idiomas_selecionados.append("Português")

        if self.var_ingles.get() == 1:
            idiomas_selecionados.append("Inglês")

        if self.var_espanhol.get() == 1:
            idiomas_selecionados.append("Espanhol")

        if idiomas_selecionados:
            resultado_texto = "Idiomas Selecionados: " + ", ".join(idiomas_selecionados)
        else:
            resultado_texto = "Nenhum idioma selecionado."

        self.label_resultado.config(text=resultado_texto)

# Criando a janela principal
janela = Tk()

# Criando uma instância da aplicação
app = LanguageApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
