# LISTBOX
O `Listbox` em Tkinter é um widget que permite exibir uma lista de itens para o usuário, onde cada item pode ser selecionado. Ele é útil para apresentar uma lista de opções para escolha ou para mostrar informações em formato de lista.

Aqui está um exemplo simples de como usar o `Listbox` em Tkinter:

```python
from tkinter import *

class ListaApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Exemplo de Listbox")

        # Criando o Listbox
        self.lista_itens = Listbox(janela, selectmode=SINGLE)  # selectmode define que apenas um item pode ser selecionado
        self.lista_itens.pack(pady=10)

        # Adicionando itens ao Listbox
        itens = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
        for item in itens:
            self.lista_itens.insert(END, item)

        # Botão para obter item selecionado
        self.botao_obter_selecionado = Button(janela, text="Obter Selecionado", command=self.obter_selecionado)
        self.botao_obter_selecionado.pack(pady=10)

        # Rótulo para exibir o item selecionado
        self.label_resultado = Label(janela, text="")
        self.label_resultado.pack(pady=10)

    def obter_selecionado(self):
        indices_selecionados = self.lista_itens.curselection()

        if indices_selecionados:
            indice_selecionado = indices_selecionados[0]
            item_selecionado = self.lista_itens.get(indice_selecionado)
            resultado_texto = f"Item Selecionado: {item_selecionado}"
        else:
            resultado_texto = "Nenhum item selecionado."

        self.label_resultado.config(text=resultado_texto)

# Criando a janela principal
janela = Tk()

# Criando uma instância da aplicação
app = ListaApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
```

Neste exemplo:

1. Criamos uma classe `ListaApp` para encapsular a lógica da aplicação.
2. Utilizamos um `Listbox` para exibir uma lista de itens.
3. Adicionamos alguns itens ao `Listbox` usando o método `insert`.
4. Um botão permite ao usuário obter o item selecionado.
5. Um rótulo exibe o item selecionado.

O `Listbox` possui um parâmetro `selectmode` que define o modo de seleção. No exemplo, `selectmode=SINGLE` significa que apenas um item pode ser selecionado de cada vez. Você pode ajustar o código conforme necessário para atender aos requisitos específicos do seu projeto.