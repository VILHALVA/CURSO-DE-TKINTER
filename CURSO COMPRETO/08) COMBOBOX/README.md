# COMBOBOX
O widget Combobox em Tkinter é usado para criar uma caixa de combinação, que é uma combinação de uma caixa de entrada de texto e uma lista suspensa. Isso permite que os usuários escolham uma opção a partir de uma lista predefinida ou insiram uma opção personalizada.

Aqui está um exemplo simples de como usar o Combobox em Tkinter:

```python
from tkinter import *
from tkinter import ttk  # Importe o módulo ttk para o Combobox

def selecionar_opcao(event):
    # Obtém a opção selecionada na Combobox
    opcao_selecionada = combo.get()
    resultado.config(text=f"Opção selecionada: {opcao_selecionada}")

# Criando a janela principal
janela = Tk()
janela.title("Exemplo de Combobox")

# Criando uma lista de opções para o Combobox
opcoes = ["Opção 1", "Opção 2", "Opção 3", "Outra Opção"]

# Criando a Combobox
combo = ttk.Combobox(janela, values=opcoes)
combo.pack(pady=10)

# Configurando a opção padrão
combo.set("Escolha uma opção")

# Adicionando um evento de seleção à Combobox
combo.bind("<<ComboboxSelected>>", selecionar_opcao)

# Rótulo para exibir o resultado
resultado = Label(janela, text="")
resultado.pack(pady=10)

# Iniciando o loop principal da aplicação
janela.mainloop()
```

Neste exemplo:

1. Importamos a classe `ttk.Combobox` do módulo ttk.
2. Criamos uma lista de opções.
3. Criamos uma Combobox usando `ttk.Combobox`, especificando as opções.
4. Configuramos a opção padrão usando `combo.set`.
5. Adicionamos um evento de seleção para capturar a opção escolhida usando `combo.bind`.
6. Um rótulo exibe a opção selecionada.

Ao executar este código, você verá uma janela com uma Combobox que permite ao usuário escolher uma opção da lista suspensa. O evento `<<ComboboxSelected>>` é acionado quando o usuário faz uma seleção, e a função `selecionar_opcao` é chamada para exibir a opção selecionada. Este é um exemplo básico, e você pode personalizar conforme necessário para atender aos requisitos específicos do seu projeto.