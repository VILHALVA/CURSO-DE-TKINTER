# CHECKBUTTON
O `Checkbutton` em Tkinter é um widget que representa uma caixa de seleção. Ele é usado para permitir que o usuário faça escolhas binárias, como ligar/desligar ou selecionar/deselecionar uma opção.

Aqui está um exemplo simples de como usar o `Checkbutton` em Tkinter:

```python
from tkinter import *

def atualizar_label():
    estado_check = check_var.get()
    if estado_check == 1:
        label_resultado.config(text="Checkbutton selecionado")
    else:
        label_resultado.config(text="Checkbutton deselecionado")

# Criando a janela principal
janela = Tk()
janela.title("Exemplo de Checkbutton")

# Variável IntVar para armazenar o estado do Checkbutton
check_var = IntVar()

# Criando o Checkbutton
checkbutton = Checkbutton(janela, text="Selecionar", variable=check_var, command=atualizar_label)
checkbutton.pack(pady=10)

# Rótulo para exibir o resultado
label_resultado = Label(janela, text="")
label_resultado.pack(pady=10)

# Iniciando o loop principal da aplicação
janela.mainloop()
```

Neste exemplo:

1. Criamos uma janela (`Tk`) com um `Checkbutton` e um rótulo (`Label`).
2. Utilizamos uma variável `IntVar` (`check_var`) para armazenar o estado do `Checkbutton`. O valor será 1 quando o `Checkbutton` estiver selecionado e 0 quando deselecionado.
3. A função `atualizar_label` é chamada sempre que o estado do `Checkbutton` é alterado. Essa função verifica o estado atual do `Checkbutton` e atualiza o rótulo de acordo.

Você pode personalizar o código conforme necessário, adicionando mais `Checkbuttons`, ajustando os rótulos ou incorporando funcionalidades adicionais. O `Checkbutton` é frequentemente usado para implementar opções de configuração ou para permitir que o usuário faça escolhas binárias em uma interface gráfica.