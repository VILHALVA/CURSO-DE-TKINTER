# MANUAL
Neste curso, você aprenderá a desenvolver interfaces gráficas (GUI) manualmente utilizando o Tkinter, a biblioteca padrão do Python para criação de GUIs. Vamos focar em entender os conceitos fundamentais e aprender a construir projetos a partir do zero.

## DESENVOLVIMENTO MANUAL:
Trabalhar diretamente com o código Tkinter permite:

- **Compreensão Profunda**: Você entenderá como cada widget funciona e como eles podem ser combinados para criar interfaces complexas.
- **Personalização Completa**: Ter controle total sobre o código permite personalizar e ajustar os detalhes da interface conforme necessário.
- **Melhor Debugging**: Conhecendo o código por dentro, fica mais fácil encontrar e corrigir erros.

## EXEMPLO DE CRIAÇÃO MANUAL DE UMA INTERFACE COM TKINTER:
Aqui está um exemplo básico para criar uma janela com um label, um botão e um campo de entrada de texto:

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

## USO DE FERRAMENTAS DE DESIGN VISUAL:
Para aqueles que preferem uma abordagem mais visual ou que desejam acelerar o processo de design, existem ferramentas de terceiros que permitem criar interfaces gráficas de forma visual e gerar o código Tkinter correspondente. Aqui estão algumas opções populares:

### 1. PAGE (PYTHON AUTOMATIC GUI GENERATOR):
**PAGE** é uma ferramenta que permite criar GUIs de forma visual e exportar o código Tkinter.

- **Instalação**:
  ```sh
  pip install page
  ```
- **Uso**:
  - Abra o PAGE (execute `page` no terminal).
  - Crie o layout arrastando e soltando componentes.
  - Exporte o código gerado e edite conforme necessário.

### 2. VISUAL TKINTER (VISUALTCL):
**Visual Tkinter** é outra ferramenta para criação visual de interfaces Tkinter.

- **Instalação e Download**:
  - Disponível em [onworks.net](https://www.onworks.net/pt/software/windows/app-visual-tkinter-python-ide).
- **Uso**:
  - Baixe e instale a ferramenta.
  - Crie o layout visualmente.
  - Gere e exporte o código para edição posterior.

## CONCLUSÃO:
Neste curso, nosso foco será na criação manual de interfaces para que você desenvolva uma compreensão sólida dos conceitos e técnicas fundamentais do Tkinter. No entanto, saiba que você também tem a opção de usar ferramentas como PAGE e Visual Tkinter para criar interfaces de maneira mais visual e rápida. Estas ferramentas podem ser especialmente úteis para projetos maiores ou quando o tempo é um fator crítico.

