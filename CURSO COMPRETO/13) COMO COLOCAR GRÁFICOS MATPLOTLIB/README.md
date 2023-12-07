# COMO COLOCAR GRÁFICOS MATPLOTLIB 
Você pode integrar gráficos do Matplotlib em aplicações Tkinter usando o widget `FigureCanvasTkAgg` do pacote `matplotlib.backends.backend_tkagg`. Aqui está um exemplo básico de como fazer isso:

```python
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

class GraficoMatplotlibApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Gráfico Matplotlib no Tkinter")

        # Criando um frame para conter o gráfico
        self.frame_grafico = ttk.Frame(janela)
        self.frame_grafico.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Criando uma figura do Matplotlib
        self.figura = Figure(figsize=(5, 4), dpi=100)
        self.grafico = self.figura.add_subplot(111)

        # Criando dados fictícios para o gráfico
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]

        # Plotando o gráfico
        self.grafico.plot(x, y, label="Primos")

        # Adicionando rótulos e título
        self.grafico.set_xlabel("Eixo X")
        self.grafico.set_ylabel("Eixo Y")
        self.grafico.set_title("Números Primos")

        # Adicionando uma legenda
        self.grafico.legend()

        # Criando um widget CanvasTkAgg para exibir o gráfico na interface Tkinter
        self.canvas = FigureCanvasTkAgg(self.figura, master=self.frame_grafico)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Adicionando um toolbar (opcional)
        toolbar = ttk.Toolbar(self.janela)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        toolbar.update()

    def iniciar(self):
        self.janela.mainloop()

# Criando a janela principal
janela = tk.Tk()

# Criando uma instância da aplicação
app = GraficoMatplotlibApp(janela)

# Iniciando o loop principal da aplicação
app.iniciar()
```

Neste exemplo, criamos uma classe `GraficoMatplotlibApp` que possui um frame para conter o gráfico Matplotlib. O gráfico é criado usando a biblioteca Matplotlib, e um widget `FigureCanvasTkAgg` é usado para integrá-lo ao Tkinter.

Certifique-se de instalar a biblioteca Matplotlib, caso ainda não tenha feito isso, utilizando o comando:

```bash
pip install matplotlib
```

Você pode personalizar o gráfico de acordo com suas necessidades, ajustando os dados, adicionando mais linhas, mudando os tipos de gráficos, entre outras customizações disponíveis no Matplotlib.