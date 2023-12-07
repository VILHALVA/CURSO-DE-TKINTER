import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

class GraficoComplexoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Gráfico Complexo Tkinter")

        # Dados fictícios para o gráfico de linha
        x_linha = np.linspace(0, 10, 100)
        y_linha = np.sin(x_linha)

        # Dados fictícios para o gráfico de dispersão
        x_dispersao = np.random.rand(50) * 10
        y_dispersao = np.random.rand(50) * 2 + np.sin(x_dispersao)

        # Criando uma figura do Matplotlib
        self.figura = Figure(figsize=(8, 6), dpi=100)

        # Adicionando gráficos à figura
        grafico_linha = self.figura.add_subplot(211)
        grafico_dispersao = self.figura.add_subplot(212)

        # Plotando o gráfico de linha
        grafico_linha.plot(x_linha, y_linha, label="Função Seno", color='blue')

        # Adicionando rótulos e título
        grafico_linha.set_xlabel('Eixo X')
        grafico_linha.set_ylabel('Função Seno')
        grafico_linha.set_title('Gráfico de Linha')

        # Adicionando uma legenda
        grafico_linha.legend()

        # Plotando o gráfico de dispersão
        grafico_dispersao.scatter(x_dispersao, y_dispersao, label="Pontos Aleatórios", color='green')

        # Adicionando rótulos e título
        grafico_dispersao.set_xlabel('Eixo X')
        grafico_dispersao.set_ylabel('Eixo Y')
        grafico_dispersao.set_title('Gráfico de Dispersão')

        # Adicionando uma legenda
        grafico_dispersao.legend()

        # Criando um widget CanvasTkAgg para exibir o gráfico na interface Tkinter
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.janela)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Adicionando uma barra de ferramentas (Toolbar)
        toolbar = NavigationToolbar2Tk(self.canvas, self.janela)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def iniciar(self):
        self.janela.mainloop()

# Criando a janela principal
janela = tk.Tk()

# Criando uma instância da aplicação
app = GraficoComplexoApp(janela)

# Iniciando o loop principal da aplicação
app.iniciar()
