# GEOMETRIA GRID
O gerenciador de geometria `grid` em Tkinter é utilizado para organizar widgets em uma grade, semelhante a um sistema de coordenadas (Como uma tabela). Ele permite posicionar os widgets em linhas e colunas, tornando-o especialmente útil para layouts mais complexos e alinhamentos precisos. A `grid` é uma ótima escolha quando você precisa organizar os elementos de forma mais estruturada.

Aqui estão alguns conceitos chave ao usar `grid`:

- **Row (Linha):** Refere-se à posição vertical na grade.
- **Column (Coluna):** Refere-se à posição horizontal na grade.
- **Rowspan e Columnspan:** Permite que um widget ocupe mais de uma linha ou coluna na grade.
- **Sticky:** Define a direção em que o widget se estende para preencher o espaço alocado (Norte, Sul, Leste, Oeste ou qualquer combinação).

Aqui está um exemplo simples usando `grid`:

```python
from tkinter import *

janela = Tk()
janela.title("Exemplo de Grid")

# Rótulo na linha 0, coluna 0
rotulo1 = Label(janela, text="Linha 0, Coluna 0")
rotulo1.grid(row=0, column=0)

# Botão na linha 1, coluna 0
botao1 = Button(janela, text="Linha 1, Coluna 0")
botao1.grid(row=1, column=0)

# Botão na linha 0, coluna 1
botao2 = Button(janela, text="Linha 0, Coluna 1")
botao2.grid(row=0, column=1)

# Rótulo na linha 1, coluna 1 e se estende para a direção Leste (E)
rotulo2 = Label(janela, text="Linha 1, Coluna 1")
rotulo2.grid(row=1, column=1, sticky=E)

janela.mainloop()
```

Neste exemplo:

- `rotulo1` está na linha 0, coluna 0.
- `botao1` está na linha 1, coluna 0.
- `botao2` está na linha 0, coluna 1.
- `rotulo2` está na linha 1, coluna 1 e se estende para a direção Leste.

Você pode ajustar a disposição dos widgets na grade alterando os valores dos parâmetros `row`, `column`, `rowspan`, `columnspan` e `sticky`. A `grid` oferece uma flexibilidade significativa para layouts mais elaborados.