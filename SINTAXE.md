# SINTAXE
## 1. CONFIGURANDO O TKINTER:
Primeiro, precisamos importar o Tkinter e criar uma janela principal.

```python
import tkinter as tk

# Cria a janela principal
root = tk.Tk()
root.title("Exemplo de Tkinter")
root.geometry("300x200")  # Define o tamanho da janela
```

## 2. LABEL:
Um label é um widget que exibe texto ou imagem.

```python
# Cria um label
label = tk.Label(root, text="Olá, Tkinter!", font=("Helvetica", 16))
# Posiciona o label na janela
label.pack(pady=20)
```

**Explicação:**
- `tk.Label` cria um label. Aqui, passamos `root` como o pai do label.
- `text` define o texto a ser exibido.
- `font` define a fonte e o tamanho do texto.
- `pack` é usado para posicionar o widget na janela. `pady` adiciona um preenchimento vertical.

## 3. BOTÃO:
Um botão é um widget que pode ser clicado para executar uma ação.

```python
# Função que será chamada quando o botão for clicado
def on_button_click():
    label.config(text="Botão clicado!")

# Cria um botão
button = tk.Button(root, text="Clique aqui", command=on_button_click)
# Posiciona o botão na janela
button.pack(pady=20)
```

**Explicação:**
- `tk.Button` cria um botão. `command` define a função a ser chamada quando o botão for clicado.
- `on_button_click` é uma função simples que muda o texto do label quando o botão é clicado.
- `pack` posiciona o botão na janela.

## 4. ENTRADA DE TEXTO (ENTRY):
Um widget de entrada de texto permite ao usuário digitar texto.

```python
# Cria uma entrada de texto
entry = tk.Entry(root, width=20)
# Posiciona a entrada na janela
entry.pack(pady=20)
```

**Explicação:**
- `tk.Entry` cria um widget de entrada de texto. `width` define a largura do widget.
- `pack` posiciona a entrada de texto na janela.

## 5. COMBINAÇÃO DE WIDGETS:
Vamos combinar todos os widgets acima em uma única aplicação.

```python
import tkinter as tk

def on_button_click():
    texto = entry.get()
    label.config(text=f"Você digitou: {texto}")

root = tk.Tk()
root.title("Exemplo Completo de Tkinter")
root.geometry("300x300")

label = tk.Label(root, text="Digite algo:", font=("Helvetica", 16))
label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=10)

button = tk.Button(root, text="Clique aqui", command=on_button_click)
button.pack(pady=10)

root.mainloop()
```

**Explicação:**
- `entry.get()` obtém o texto digitado no widget de entrada.
- `label.config(text=...)` altera o texto do label para exibir o texto digitado.
- `root.mainloop()` inicia o loop principal da aplicação Tkinter, mantendo a janela aberta.

Esses são os conceitos básicos para trabalhar com Tkinter. Você pode combinar esses widgets e ajustar suas propriedades para criar interfaces mais complexas. 