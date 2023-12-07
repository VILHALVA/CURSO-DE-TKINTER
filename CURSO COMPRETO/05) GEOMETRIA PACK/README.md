# GEOMETRIA PACK
## CONCEITO:
O método `pack` em Tkinter é um gerenciador de geometria usado para organizar widgets dentro de contêineres de maneira simplificada. Ele organiza os widgets em blocos antes de colocá-los no contêiner, tornando a disposição dos elementos relativamente fácil. Aqui está um exemplo básico usando `pack`:

```python
from tkinter import *

janela = Tk()
janela.title("Exemplo de Pack")

# Criando três botões e usando pack para organizá-los
botao1 = Button(janela, text="Botão 1")
botao1.pack(side=LEFT, padx=10)

botao2 = Button(janela, text="Botão 2")
botao2.pack(side=LEFT, padx=10)

botao3 = Button(janela, text="Botão 3")
botao3.pack(side=LEFT, padx=10)

janela.mainloop()
```

Neste exemplo:

1. Criamos uma janela com o título "Exemplo de Pack".
2. Criamos três botões (`botao1`, `botao2` e `botao3`).
3. Usamos o método `pack` para organizá-los lado a lado. O parâmetro `side` indica a direção em que os widgets serão empacotados (neste caso, à esquerda) e `padx` adiciona um espaço horizontal entre eles.

Você pode empacotar os widgets em diferentes direções (topo, fundo, esquerda, direita) e também especificar se eles devem preencher a direção inteira ou apenas uma parte dela.

```python
from tkinter import *

janela = Tk()
janela.title("Exemplo de Pack")

# Criando três botões e usando pack para organizá-los
botao1 = Button(janela, text="Botão 1")
botao1.pack(side=TOP, pady=10)

botao2 = Button(janela, text="Botão 2")
botao2.pack(side=LEFT, padx=10)

botao3 = Button(janela, text="Botão 3")
botao3.pack(side=RIGHT, padx=10)

janela.mainloop()
```

Neste exemplo, o primeiro botão é empacotado no topo, o segundo à esquerda e o terceiro à direita. O uso de `pady` e `padx` adiciona espaçamento vertical e horizontal, respectivamente.

O método `pack` é útil para layouts simples, mas pode se tornar mais desafiador em layouts complexos. Para layouts mais avançados, considera-se o uso do método `grid` ou `place`. Escolha o método que melhor atenda às necessidades específicas do seu projeto.

## O "SIDE" E "PADX":
Os parâmetros `side` e `padx` são opções usadas ao empregar o método `pack` em Tkinter para organizar widgets dentro de um contêiner. Aqui está uma explicação para cada um deles:

1. **`side` (lado):**
   - O parâmetro `side` especifica em que lado do contêiner o widget deve ser empacotado.
   - Os valores comuns para `side` incluem:
     - `TOP`: Empacota o widget no topo do contêiner.
     - `BOTTOM`: Empacota o widget na parte inferior do contêiner.
     - `LEFT`: Empacota o widget à esquerda do contêiner.
     - `RIGHT`: Empacota o widget à direita do contêiner.
   - Dependendo do valor escolhido para `side`, os widgets empacotados subsequentemente podem ser colocados acima, abaixo, à esquerda ou à direita dos widgets anteriores.

2. **`padx` (espaçamento horizontal):**
   - O parâmetro `padx` adiciona um espaço horizontal entre os widgets empacotados e também entre os widgets e as bordas do contêiner.
   - É usado para dar um espaço visualmente agradável entre os widgets.
   - O valor de `padx` é geralmente especificado em pixels.

Aqui está um exemplo para ilustrar o uso de `side` e `padx`:

```python
from tkinter import *

janela = Tk()
janela.title("Exemplo de Pack")

# Criando três botões e usando pack para organizá-los
botao1 = Button(janela, text="Botão 1")
botao1.pack(side=TOP, pady=10)

botao2 = Button(janela, text="Botão 2")
botao2.pack(side=LEFT, padx=10)

botao3 = Button(janela, text="Botão 3")
botao3.pack(side=RIGHT, padx=10)

janela.mainloop()
```

Neste exemplo, `botao1` é empacotado no topo (`TOP`), `botao2` à esquerda (`LEFT`) com um espaçamento horizontal de 10 pixels (`padx=10`), e `botao3` à direita (`RIGHT`) também com um espaçamento horizontal de 10 pixels. O parâmetro `pady` é usado para adicionar um espaçamento vertical de 10 pixels entre `botao1` e os demais widgets.

