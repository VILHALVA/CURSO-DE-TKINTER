# FRAME
O `Frame` em Tkinter é um contêiner retangular que pode ser usado para organizar e agrupar outros widgets. Ele fornece uma maneira de estruturar a interface gráfica, permitindo que você agrupe widgets relacionados e organize-os dentro da janela principal.

Aqui está um exemplo simples que utiliza `Frame` para organizar um botão em duas seções diferentes:

```python
import tkinter as tk

class AppComFrames:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Exemplo de Frame")

        # Criando dois frames
        self.frame1 = tk.Frame(janela, borderwidth=2, relief="groove")
        self.frame2 = tk.Frame(janela, borderwidth=2, relief="groove")

        # Adicionando widgets ao frame1
        self.label1 = tk.Label(self.frame1, text="Frame 1")
        self.botao1 = tk.Button(self.frame1, text="Botão 1", command=self.clicar_botao1)

        # Adicionando widgets ao frame2
        self.label2 = tk.Label(self.frame2, text="Frame 2")
        self.botao2 = tk.Button(self.frame2, text="Botão 2", command=self.clicar_botao2)

        # Posicionando os frames na janela
        self.frame1.pack(side=tk.LEFT, padx=10)
        self.frame2.pack(side=tk.RIGHT, padx=10)

        # Posicionando os widgets dentro dos frames
        self.label1.pack()
        self.botao1.pack()

        self.label2.pack()
        self.botao2.pack()

    def clicar_botao1(self):
        print("Botão 1 clicado!")

    def clicar_botao2(self):
        print("Botão 2 clicado!")

# Criando a janela principal
janela = tk.Tk()

# Criando uma instância da aplicação
app = AppComFrames(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
```

Neste exemplo:

- Criamos dois `Frames` chamados `frame1` e `frame2`.
- Adicionamos widgets (rótulos e botões) a cada `Frame`.
- Posicionamos os `Frames` na janela principal usando o método `pack`.
- Posicionamos os widgets dentro dos `Frames`.
- Os métodos `clicar_botao1` e `clicar_botao2` são chamados quando os botões são clicados.

Os `Frames` ajudam a organizar a interface gráfica e a melhorar a legibilidade do código, especialmente em aplicações mais complexas. Eles também fornecem uma maneira de agrupar widgets relacionados e aplicar estilos ou opções de layout específicos a esses grupos.