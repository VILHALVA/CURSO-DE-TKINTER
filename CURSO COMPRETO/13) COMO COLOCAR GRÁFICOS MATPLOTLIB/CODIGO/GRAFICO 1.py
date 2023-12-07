import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class GraficoBarrasApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Gráfico de Barras Tkinter")

        # Dados fictícios para o gráfico de barras
        produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']
        vendas = [150, 200, 120, 250]

        # Criando uma figura do Matplotlib
        self.figura = Figure(figsize=(6, 4), dpi=100)
        self.grafico = self.figura.add_subplot(111)

        # Plotando o gráfico de barras
        self.grafico.bar(produtos, vendas, color='blue')

        # Adicionando rótulos e título
        self.grafico.set_xlabel('Produtos')
        self.grafico.set_ylabel('Vendas')
        self.grafico.set_title('Contagem de Vendas por Produto')

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
app = GraficoBarrasApp(janela)

# Iniciando o loop principal da aplicação
app.iniciar()
