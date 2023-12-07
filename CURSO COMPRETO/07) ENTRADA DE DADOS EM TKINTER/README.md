# ENTRADA DE DADOS EM TKINTER
Em Tkinter, você pode usar o widget Entry para receber entradas de dados do usuário. O widget Entry permite que os usuários digitem texto ou números em um campo de entrada.

Aqui está um exemplo simples que demonstra como criar uma janela com um campo de entrada e um botão que, ao ser clicado, exibe o texto inserido no campo de entrada:

```python
from tkinter import *

def exibir_entrada():
    texto = campo_entrada.get()
    resultado.config(text=f"Texto inserido: {texto}")

# Criando a janela principal
janela = Tk()
janela.title("Entrada de Dados em Tkinter")

# Campo de entrada
campo_entrada = Entry(janela, width=30)
campo_entrada.pack(pady=10)

# Botão para exibir a entrada
botao_exibir = Button(janela, text="Exibir Entrada", command=exibir_entrada)
botao_exibir.pack()

# Rótulo para exibir o resultado
resultado = Label(janela, text="")
resultado.pack(pady=10)

# Iniciando o loop principal da aplicação
janela.mainloop()
```

Neste exemplo:

1. Criamos uma janela (`Tk`) com um campo de entrada (`Entry`), um botão (`Button`) e um rótulo (`Label`).
2. A função `exibir_entrada` é chamada quando o botão é clicado. Ela obtém o texto do campo de entrada usando `campo_entrada.get()` e atualiza o rótulo com o resultado.
3. O texto inserido é exibido em um rótulo.

Você pode adaptar esse exemplo de acordo com suas necessidades, incluindo validações de entrada, manipulação de dados, etc. O uso de funções como `get()` em widgets Entry permite que você acesse o conteúdo inserido pelo usuário.