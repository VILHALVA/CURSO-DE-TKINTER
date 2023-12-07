# CURSO DE TKINTER
👨‍⚖️TKINTER É UMA BIBLIOTECA EM PYTHON PARA CRIAÇÃO DE INTERFACES GRÁFICAS. ELA PERMITE CRIAR JANELAS, BOTÕES, CAIXAS DE DIÁLOGO E OUTROS ELEMENTOS VISUAIS EM PROGRAMAS PYTHON.

[![GitHub Repo stars](https://img.shields.io/badge/VILHALVA-GITHUB-03A9F4?logo=github)](https://github.com/VILHALVA) 
[![GitHub Repo stars](https://img.shields.io/badge/VEJA%20OS-VIDEOS-03A9F4?logo=youtube)](https://www.youtube.com/@vilhalva100/search?query=TKINTER)
[![GitHub Repo stars](https://img.shields.io/badge/VEJA-DOCUMENTAÇÃO-03A9F4?logo=google)](https://docs.python.org/pt-br/3/library/tk.html) 
[![GitHub Repo stars](https://img.shields.io/badge/LINGUAGEM%20DE-PROGRAMAÇÃO-03A9F4?logo=github)](https://github.com/VILHALVA/CURSO-DE-PYTHON) <br>

[![GitHub Repo stars](https://img.shields.io/badge/-PLAYLIST%20DO%20YOUTUBE-blueviolet)](https://youtube.com/playlist?list=PLGFzROSPU9oWZZNGPJvyWO4JAnHGPNVEt&si=N4T2p31RGGu4R845)

<img src="https://play-lh.googleusercontent.com/98JfuGoUOxFK63NBn6Qd3TR1dSGcV_mJ17o_wRjPqWoKcDa7PyCG1K2C9jgH1Pb1N6Gj" align="center" width="280"> <br>

![](https://i.imgur.com/waxVImv.png)

# CONCEITO:
O Tkinter é uma biblioteca gráfica padrão do Python usada para criar interfaces gráficas do usuário (GUI). Ele fornece widgets (elementos gráficos como botões, caixas de texto, etc.) e métodos para criar janelas, gerenciar eventos e construir interfaces de usuário interativas.

Vamos começar com um exemplo simples que cria uma janela usando Tkinter:

```python
import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

# Adiciona um rótulo à janela
rotulo = tk.Label(janela, text="Olá, Tkinter!")
rotulo.pack()

# Inicia o loop principal
janela.mainloop()
```

Explicação do código:

1. `import tkinter as tk`: Importa a biblioteca tkinter e a renomeia como `tk` para facilitar o uso.

2. `janela = tk.Tk()`: Cria a janela principal da aplicação.

3. `rotulo = tk.Label(janela, text="Olá, Tkinter!")`: Cria um rótulo (label) com o texto "Olá, Tkinter!" para exibir na janela.

4. `rotulo.pack()`: Adiciona o rótulo à janela.

5. `janela.mainloop()`: Inicia o loop principal da aplicação, aguardando interações do usuário.

Ao executar este código, você deve ver uma janela com o rótulo "Olá, Tkinter!".

