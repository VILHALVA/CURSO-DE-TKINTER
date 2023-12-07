# LABEL
## CONCEITO:
O widget `Label` em Tkinter é usado para exibir texto ou imagens na interface gráfica do usuário (GUI). Ele fornece uma maneira simples de adicionar rótulos informativos ou explicativos à sua aplicação. Aqui está um exemplo básico de como usar o widget `Label`:

```python
from tkinter import *

# Criação da janela principal
janela = Tk()

# Criação de um rótulo
rotulo = Label(janela, text="Olá, Tkinter!")

# Adiciona o rótulo à janela
rotulo.pack()

# Inicia o loop principal da aplicação
janela.mainloop()
```

Explicação do código:

1. **`rotulo = Label(janela, text="Olá, Tkinter!")`**: Cria uma instância do widget `Label`. O argumento `janela` indica que o rótulo pertence à janela principal. O argumento `text` é usado para definir o texto exibido no rótulo.

2. **`rotulo.pack()`**: Adiciona o rótulo à janela usando o método `pack()`. Este método organiza o widget na janela de acordo com a geometria do contêiner. Neste caso, o rótulo será centralizado na janela.

3. **`janela.mainloop()`**: Inicia o loop principal da aplicação, permitindo a exibição da janela e interações do usuário.

Ao executar este código, uma janela será exibida com um rótulo contendo o texto "Olá, Tkinter!".

Você também pode personalizar o rótulo ajustando suas propriedades. Por exemplo, pode mudar a fonte, a cor do texto, o tamanho, etc. Aqui está um exemplo de como você pode fazer isso:

```python
from tkinter import *

janela = Tk()

# Criação de um rótulo com propriedades personalizadas
rotulo_personalizado = Label(janela, text="Olá, Tkinter!", font=("Arial", 16), fg="blue")

# Adiciona o rótulo à janela
rotulo_personalizado.pack()

janela.mainloop()
```

Neste exemplo, o rótulo tem uma fonte Arial com tamanho 16 e a cor do texto é azul. Você pode experimentar diferentes propriedades para personalizar o aspecto do seu rótulo de acordo com suas preferências e necessidades.

## CODIGO:
Esse código cria um rótulo (label) com algumas propriedades específicas usando Tkinter. Aqui está uma explicação linha por linha:

```python
label = Label(janela, text="PRIMEIRO LABEL", font=("Arial Bold", 50), bg="green", fg="white")
label.grid(column=0, row=0)
```

1. **`label = Label(janela, text="PRIMEIRO LABEL", font=("Arial Bold", 50), bg="green", fg="white")`**: Cria um objeto `Label` com os seguintes parâmetros:
   - `janela`: Indica que este rótulo pertence à janela principal.
   - `text="PRIMEIRO LABEL"`: Define o texto exibido no rótulo como "PRIMEIRO LABEL".
   - `font=("Arial Bold", 50)`: Define a fonte do texto como "Arial Bold" com um tamanho de 50 pontos.
   - `bg="green"`: Define a cor de fundo (background) do rótulo como verde.
   - `fg="white"`: Define a cor do texto como branca.

2. **`label.grid(column=0, row=0)`**: Usa o gerenciador de geometria "grid" para posicionar o rótulo na janela. Neste caso, o rótulo é colocado na coluna 0 e na linha 0.

Em resumo, este código cria um rótulo com o texto "PRIMEIRO LABEL", uma fonte específica, um fundo verde e texto branco. Em seguida, o rótulo é posicionado na janela usando o gerenciador de geometria "grid". O uso do método `grid` permite organizar os widgets em uma grade, especificando a coluna e a linha em que cada widget deve ser colocado.

Ao executar esse código, você verá uma janela com um rótulo exibindo o texto "PRIMEIRO LABEL" e as propriedades visuais definidas. Este é um exemplo básico de como você pode usar o widget `Label` e o método `grid` para organizar elementos na sua interface gráfica.