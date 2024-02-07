# SINTAXE
Criar um projeto simples em Tkinter é uma ótima maneira de começar a explorar a criação de interfaces gráficas em Python. Abaixo, vou fornecer um exemplo de um projeto básico que consiste em uma janela com um botão que exibe uma mensagem quando clicado:

```python
import tkinter as tk
from tkinter import messagebox

# Função para exibir uma mensagem quando o botão é clicado
def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Olá, mundo!")

# Cria a janela principal
root = tk.Tk()
root.title("Projeto Tkinter")

# Cria um botão na janela
botao = tk.Button(root, text="Clique-me!", command=mostrar_mensagem)
botao.pack(pady=20)

# Inicia o loop principal da aplicação
root.mainloop()
```

Neste projeto, importamos o módulo `tkinter` e o renomeamos como `tk` para facilitar a referência. Em seguida, importamos a classe `messagebox` do módulo `tkinter` para exibir caixas de mensagem. Criamos uma função `mostrar_mensagem()` que será chamada quando o botão for clicado, exibindo uma mensagem de diálogo simples.

Em seguida, criamos a janela principal (`root`) usando `tk.Tk()` e definimos um título para ela. Em seguida, criamos um botão usando `tk.Button()` e associamos a função `mostrar_mensagem()` ao evento de clique do botão usando o argumento `command`.

Finalmente, usamos o método `pack()` para exibir o botão na janela e iniciamos o loop principal da aplicação com `root.mainloop()`.

Este é apenas um exemplo simples para começar. Você pode expandir este projeto adicionando mais widgets, como caixas de entrada, rótulos e menus, para criar uma interface gráfica mais complexa e interativa. Experimente explorar a documentação do Tkinter para aprender mais sobre os recursos disponíveis e como utilizá-los em seus projetos.