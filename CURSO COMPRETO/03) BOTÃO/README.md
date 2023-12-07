# BOTÃO
## CONCEITO:
O widget `Button` em Tkinter é utilizado para criar botões interativos em uma interface gráfica. Quando o botão é clicado, você pode associar uma função (chamada de retorno) que será executada em resposta ao evento de clique. Aqui está um exemplo básico de como criar e usar um botão em Tkinter:

```python
from tkinter import *

# Função chamada quando o botão é clicado
def botao_clicado():
    label.config(text="Botão Clicado!")

# Criação da janela principal
janela = Tk()

# Criação de um rótulo inicial
label = Label(janela, text="Olá, Tkinter!")
label.pack()

# Criação de um botão
botao = Button(janela, text="Clique-me!", command=botao_clicado)
botao.pack()

# Inicia o loop principal da aplicação
janela.mainloop()
```

Explicação do código:

1. **`def botao_clicado():`**: Define uma função chamada `botao_clicado`, que será executada quando o botão for clicado. Neste exemplo, ela apenas altera o texto do rótulo.

2. **`botao = Button(janela, text="Clique-me!", command=botao_clicado)`**: Cria um botão com os seguintes parâmetros:
   - `janela`: Indica que este botão pertence à janela principal.
   - `text="Clique-me!"`: Define o texto exibido no botão.
   - `command=botao_clicado`: Associa a função `botao_clicado` ao evento de clique do botão.

3. **`botao.pack()`**: Adiciona o botão à janela usando o método `pack()`. Este método organiza o widget na janela de acordo com a geometria do contêiner.

4. **`janela.mainloop()`**: Inicia o loop principal da aplicação.

Ao executar este código, uma janela será exibida com um rótulo inicial e um botão. Quando você clicar no botão, a função `botao_clicado` será chamada, e o texto do rótulo será alterado para "Botão Clicado!".

Essa é uma introdução básica à criação de botões em Tkinter. Você pode expandir essa lógica para realizar diferentes ações quando os botões são clicados, como chamar outras funções, abrir novas janelas ou realizar operações específicas do seu aplicativo. Se tiver mais perguntas ou precisar de esclarecimentos adicionais, sinta-se à vontade para perguntar!

## CODIGO:
Essas linhas de código criam um botão usando Tkinter, configuram seu texto, associam uma função de callback (função chamada quando o botão é clicado) e, em seguida, o posicionam na janela usando o método `pack`. Vamos explicar cada parte:

```python
botao1 = Button(janela, text="Botão 1", command=botao1_clicado)
```

1. **`Button(janela, text="Botão 1", command=botao1_clicado)`:** Aqui, você está criando um objeto do tipo `Button` (botão). Os parâmetros são:
   - `janela`: Indica que este botão pertence à janela principal.
   - `text="Botão 1"`: Define o texto exibido no botão como "Botão 1".
   - `command=botao1_clicado`: Associa a função `botao1_clicado` ao evento de clique do botão. Quando este botão for clicado, a função `botao1_clicado` será chamada.

```python
botao1.pack(side=LEFT, padx=10)
```

2. **`botao1.pack(side=LEFT, padx=10)`:** Aqui, você está usando o método `pack` para organizar o botão na janela. Os parâmetros são:
   - `side=LEFT`: Indica que o botão deve ser posicionado à esquerda do espaço disponível. Outras opções podem ser `RIGHT` (DIREITA), `TOP` (ACIMA) e `BOTTOM` (ABAIXO).
   - `padx=10`: Adiciona um preenchimento de 10 pixels à esquerda do botão. Isso ajuda a criar um espaçamento entre o botão e outros widgets.

Então, no geral, essas duas linhas criam um botão chamado "Botão 1", associam a função `botao1_clicado` ao seu evento de clique, e o posicionam à esquerda da janela com um espaçamento de 10 pixels à esquerda. Esse botão, quando clicado, executará a função `botao1_clicado`.