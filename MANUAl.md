# MANUAL
## 1. INSTALAÇÃO DO TKINTER:
### TKINTER JÁ VEM COM O PYTHON INSTALADO!
Se você já tem o **Python 3** instalado, **provavelmente o Tkinter já está incluído**.

### COMO VERIFICAR SE O TKINTER ESTÁ INSTALADO:
Abra o terminal ou prompt de comando e digite:

```bash
python -m tkinter
```

Se aparecer uma **janela de teste do Tkinter**, está tudo certo! Se der erro, pode instalar com:

### PARA WINDOWS/LINUX:
```bash
sudo apt-get install python3-tk
```

### PARA MACOS:
Normalmente o Tkinter já está incluso. Mas se necessário:

```bash
brew install python-tk
```

## 2. CONFIGURANDO O AMBIENTE:
Você pode usar qualquer editor de código. Vamos usar o **VS Code** (Visual Studio Code):

### CONFIGURANDO:
1. Instale o [VS Code](https://code.visualstudio.com/)
2. Instale a **extensão Python** (procure por “Python” no marketplace)
3. Crie uma pasta para o projeto, ex: `meu_primeiro_tkinter`
4. Crie um arquivo `app.py`

## 3. PRIMEIRO PROJETO COM TKINTER:
Vamos criar um app simples com um **campo de texto e um botão**.

### CÓDIGO: `app.py`:
```python
import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("Meu Primeiro App")
janela.geometry("300x200")

# Campo de entrada
entrada = tk.Entry(janela, width=25)
entrada.pack(pady=10)

# Função para o botão
def clicar():
    nome = entrada.get()
    label_resultado.config(text=f"Olá, {nome}!")

# Botão
botao = tk.Button(janela, text="Clique aqui", command=clicar)
botao.pack(pady=5)

# Label para mostrar resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack(pady=10)

# Rodar o app
janela.mainloop()
```

## 4. COMO EXECUTAR O PROJETO?
Abra o terminal dentro da pasta do projeto e digite:

```bash
python app.py
```

Uma janela aparecerá com:
- Um campo para digitar seu nome
- Um botão
- Uma mensagem de "Olá, [seu nome]!" ao clicar

