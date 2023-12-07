# CONSTRUTOR DE INTERFACE
O PAGE (Python Automatic GUI Generator) é uma ferramenta gráfica para criar interfaces gráficas de usuário (GUI) em Tkinter. Ele oferece uma abordagem de arrastar e soltar para construir interfaces gráficas, o que pode ser útil para aqueles que preferem uma abordagem visual ao invés de codificação manual. Vou guiá-lo através do processo básico de criação de uma interface simples usando o PAGE.

**Passo 1: Instalação do PAGE**

Antes de começar, você precisa instalar o PAGE. Você pode fazer isso usando o pip:

```bash
pip install PAGE
```

```bash
pip install brotli
```

```bash
pip install pyyaml
```

```bash
pip install jinja2
```

```bash
pip install markdown2
```

**Passo 2: page.yml:**

Você pode tentar criar manualmente o arquivo `page.yml` usando um editor de texto, como o Bloco de Notas, e adicionar o conteúdo básico. Abra um editor de texto, insira o seguinte conteúdo e salve-o como `page.yml` no mesmo diretório onde você está executando o comando `page`.

```yaml
name: SeuProjeto
geometry: 400x300
```

Substitua "SeuProjeto" pelo nome desejado e ajuste as dimensões conforme necessário.

Após criar o arquivo manualmente, execute o comando `page new .` novamente. Certifique-se de estar no diretório correto ao executar os comandos.

**Passo 3: Criar uma Interface Gráfica com o PAGE**

Depois de instalar o PAGE, você pode começar a criar sua interface gráfica:

1. Abra o prompt de comando ou terminal e execute o seguinte comando para iniciar o PAGE:

```bash
page
```

2. Isso abrirá uma interface gráfica. No menu, escolha `File -> New` para criar um novo projeto.

3. Você será apresentado a uma tela em branco. No lado direito, há uma barra de ferramentas com widgets disponíveis. Selecione o widget desejado (por exemplo, `Label`, `Button`, etc.) e arraste-o para a tela principal.

4. Ajuste as propriedades do widget (como texto, fonte, cor, etc.) usando o painel à direita.

5. Continue adicionando widgets conforme necessário, ajustando as propriedades de cada um.

6. Quando terminar, vá para `File -> Save` para salvar o projeto.

7. Depois de salvar, você pode gerar o código Python correspondente indo para `File -> Save As -> Python` e salvando o arquivo Python.

**Exemplo de código gerado pelo PAGE:**

Aqui está um exemplo muito simples de código gerado pelo PAGE:

```python
import tkinter as tk
from tkinter import ttk

def clicar():
    label1.config(text="Botão Clicado!")

root = tk.Tk()
root.geometry("300x200")

label1 = ttk.Label(root, text="Olá, Tkinter!")
label1.pack(pady=10)

button1 = ttk.Button(root, text="Clique em Mim!", command=clicar)
button1.pack(pady=10)

root.mainloop()
```

Este é um exemplo muito básico e não reflete totalmente o potencial do PAGE para interfaces mais complexas. Ao explorar a ferramenta, você poderá criar interfaces gráficas mais sofisticadas com facilidade. Lembre-se de ajustar o código gerado conforme necessário para atender aos seus requisitos específicos.