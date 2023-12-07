# RADIOBUTTON
O `Radiobutton` em Tkinter é um widget que representa botões de opção, onde os usuários podem escolher uma opção de um conjunto exclusivo de opções. Quando um `Radiobutton` é selecionado, os outros no mesmo grupo são automaticamente deselecionados.

Aqui está um exemplo simples de como usar o `Radiobutton` em Tkinter:

```python
from tkinter import *

class PizzaApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Escolha de Pizza")

        # Variável StringVar para armazenar a opção selecionada
        self.variavel_sabor = StringVar()

        # Criando os Radiobuttons
        self.radio_margherita = Radiobutton(janela, text="Margherita", variable=self.variavel_sabor, value="Margherita")
        self.radio_calabresa = Radiobutton(janela, text="Calabresa", variable=self.variavel_sabor, value="Calabresa")
        self.radio_quatro_queijos = Radiobutton(janela, text="Quatro Queijos", variable=self.variavel_sabor, value="Quatro Queijos")

        # Botão para exibir a opção selecionada
        self.botao_exibir = Button(janela, text="Exibir Opção", command=self.exibir_opcao)

        # Rótulo para exibir a opção selecionada
        self.label_resultado = Label(janela, text="")

        # Posicionando os widgets
        self.radio_margherita.pack(pady=5)
        self.radio_calabresa.pack(pady=5)
        self.radio_quatro_queijos.pack(pady=5)
        self.botao_exibir.pack(pady=10)
        self.label_resultado.pack(pady=10)

    def exibir_opcao(self):
        opcao_selecionada = self.variavel_sabor.get()
        resultado_texto = f"Opção Selecionada: {opcao_selecionada}"
        self.label_resultado.config(text=resultado_texto)

# Criando a janela principal
janela = Tk()

# Criando uma instância da aplicação
app = PizzaApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
```

Neste exemplo:

1. Criamos uma classe `PizzaApp` para encapsular a lógica da aplicação.
2. Utilizamos três `Radiobuttons` para representar opções de pizza: Margherita, Calabresa e Quatro Queijos.
3. Um botão permite ao usuário exibir a opção selecionada.
4. Um rótulo exibe a opção selecionada.

Os `Radiobuttons` compartilham a mesma variável (`self.variavel_sabor`) e têm valores diferentes (`"Margherita"`, `"Calabresa"`, `"Quatro Queijos"`). Quando um `Radiobutton` é selecionado, a variável `self.variavel_sabor` é atualizada com o valor correspondente, e isso permite que você saiba qual opção foi escolhida.