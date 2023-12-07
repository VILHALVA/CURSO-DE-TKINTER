# INTRODUÇÃO, INSTALAÇÃO E CONFIGURAÇÃO:
## Introdução ao Tkinter:
Tkinter é a biblioteca gráfica padrão para a criação de interfaces gráficas do usuário (GUI) em Python. Ele fornece uma maneira fácil e rápida de criar janelas, botões, caixas de texto e outros elementos de interface gráfica.

Alguns conceitos básicos do Tkinter incluem:

1. **Janela (Window):** A janela é a principal área de exibição da interface gráfica. Você pode criar uma janela usando a classe `Tk()`.

2. **Widget:** Um widget é um elemento gráfico, como botões, rótulos, caixas de texto, etc., que você pode adicionar à janela para interação do usuário.

3. **Frame:** Um frame é um contêiner para agrupar e organizar widgets.

4. **Rótulo (Label):** Exibe texto ou imagem.

5. **Botão (Button):** Um botão clicável pelo usuário.

6. **Caixa de Texto (Entry):** Uma caixa de entrada de texto para o usuário.

## Instalação do Tkinter:
Tkinter geralmente já está incluído na instalação padrão do Python. No entanto, você pode verificar se o Tkinter está instalado executando o seguinte comando no terminal:

```bash
python -m tkinter
```

Se o Tkinter estiver instalado, você verá uma pequena janela pop-up. Se não estiver instalado, você precisará instalá-lo.

## Configuração do Ambiente de Desenvolvimento:
1. **Instalação do Python:**
   Certifique-se de ter o Python instalado. Você pode baixar a versão mais recente em [python.org](https://www.python.org/downloads/).

2. **Verificação do Tkinter:**
   Verifique se o Tkinter está instalado executando o comando mencionado acima.

3. **IDE (Ambiente de Desenvolvimento Integrado):**
   Escolha um IDE para desenvolver em Python. Exemplos incluem VSCode, PyCharm, IDLE (incluso com a instalação padrão do Python).

4. **Editor de Texto:**
   Se preferir um editor de texto simples, você pode usar o Notepad++ ou o Visual Studio Code.

## PRIMEIRO CÓDIGO:
```python
from tkinter import *

# Criação da janela principal
janela = Tk()

# Define o título da janela
janela.title("OLÁ MUNDO!")

# Define as dimensões da janela (largura x altura)
janela.geometry("500x500")

# Inicia o loop principal da aplicação
janela.mainloop()
```

1. **`from tkinter import *`**: Esta linha importa todos os símbolos (funções, classes, etc.) do módulo `tkinter`. O asterisco (`*`) é usado para importar tudo. No entanto, em práticas mais avançadas, é recomendável importar apenas o que é necessário para evitar conflitos de nomeação.

2. **`janela = Tk()`**: Cria uma instância da classe `Tk`, que representa a janela principal da aplicação. `Tk` é uma classe fornecida pelo módulo `tkinter` que inicializa uma janela gráfica.

3. **`janela.title("OLÁ MUNDO!")`**: Define o título da janela como "OLÁ MUNDO!". O título aparecerá na barra de título da janela.

4. **`janela.geometry("500x500")`**: Define as dimensões da janela. Neste caso, a largura é 500 pixels e a altura é 500 pixels.

5. **`janela.mainloop()`**: Inicia o loop principal da aplicação. Este método é responsável por exibir a janela na tela e aguardar interações do usuário. O programa ficará bloqueado nesta linha até que o usuário feche a janela.

Ao executar este código, uma janela gráfica será exibida com o título "OLÁ MUNDO!" e dimensões de 500x500 pixels. A aplicação continuará executando até que o usuário feche a janela.

Este é um exemplo muito simples para criar uma janela Tkinter. À medida que você avança no aprendizado de Tkinter, poderá adicionar mais widgets e funcionalidades à sua interface gráfica.

