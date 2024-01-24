# CURSO DE TKINTER
👨‍⚖️TKINTER É UMA BIBLIOTECA EM PYTHON PARA CRIAÇÃO DE INTERFACES GRÁFICAS. ELA PERMITE CRIAR JANELAS, BOTÕES, CAIXAS DE DIÁLOGO E OUTROS ELEMENTOS VISUAIS EM PROGRAMAS PYTHON.

[![GitHub Repo stars](https://img.shields.io/badge/VILHALVA-GITHUB-03A9F4?logo=github)](https://github.com/VILHALVA) 
[![GitHub Repo stars](https://img.shields.io/badge/VEJA-DOCUMENTAÇÃO-03A9F4?logo=google)](https://docs.python.org/pt-br/3/library/tk.html) 
[![GitHub Repo stars](https://img.shields.io/badge/LINGUAGEM%20DE-PROGRAMAÇÃO-03A9F4?logo=github)](https://github.com/VILHALVA/CURSO-DE-PYTHON) 
[![GitHub Repo stars](https://img.shields.io/badge/-PLAYLIST%20DO%20YOUTUBE-blueviolet)](https://youtube.com/playlist?list=PLGFzROSPU9oWZZNGPJvyWO4JAnHGPNVEt&si=N4T2p31RGGu4R845)

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

# CARACTERÍSTICAS
## POSITIVAS:
- **Leve e Simples:** Tkinter é uma biblioteca leve e simples para a criação de interfaces gráficas em Python.

- **Parte da Biblioteca Padrão:** Tkinter faz parte da biblioteca padrão do Python, o que significa que não é necessário instalar bibliotecas adicionais para começar a usá-lo.

- **Multiplataforma:** Oferece suporte a múltiplos sistemas operacionais, incluindo Windows, Linux e macOS, proporcionando consistência em diferentes ambientes.

- **Rápido Desenvolvimento:** Permite o desenvolvimento rápido de interfaces gráficas devido à sua simplicidade e à disponibilidade de widgets prontos para uso.

- **Ampla Documentação:** Tkinter possui uma documentação abrangente e uma comunidade ativa, o que facilita o aprendizado e a resolução de problemas.

- **Integração com Python:** Integra-se de maneira natural com o ecossistema Python, facilitando o desenvolvimento de aplicações GUI em conjunto com outras bibliotecas Python.

## NEGATIVAS:
- **Aparência Básica:** A aparência das interfaces criadas com Tkinter pode ser considerada básica em comparação com tecnologias mais avançadas.

- **Limitações Gráficas:** Para aplicações que requerem recursos gráficos mais avançados, Tkinter pode apresentar limitações em comparação com outras bibliotecas GUI.

- **Menos Flexibilidade de Layout:** Em comparação com algumas tecnologias mais avançadas, Tkinter oferece menos flexibilidade em termos de layout e posicionamento de componentes.

- **Ferramentas de Design Limitadas:** As ferramentas de design visual para Tkinter são menos avançadas do que em algumas outras ferramentas GUI.

- **Curva de Aprendizado Inicial:** Iniciantes podem enfrentar uma curva de aprendizado inicial ao trabalhar com Tkinter, especialmente se não estiverem familiarizados com GUI em Python.

- **Personalização Limitada:** A personalização avançada da aparência dos widgets pode ser limitada em comparação com tecnologias mais robustas.

