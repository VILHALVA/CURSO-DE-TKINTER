from tkinter import *

def processar_entrada():
    try:
        # Obter o número da entrada
        numero = float(entrada_numero.get())

        # Exibir o dobro do número
        resultado_numero.config(text=f"Dobro do número: {2 * numero}")
    except ValueError:
        resultado_numero.config(text="Por favor, insira um número válido.")

    # Obter o texto da entrada
    texto = entrada_texto.get()

    # Exibir o texto repetido
    resultado_texto.config(text=f"Texto repetido: {texto * 2}")

# Criando a janela principal
janela = Tk()
janela.geometry("500x500")
janela.title("Entrada de Números e Texto em Tkinter")

# Entrada para números
rotulo_numero = Label(janela, text="Insira um número:")
rotulo_numero.pack()

entrada_numero = Entry(janela)
entrada_numero.pack()

# Entrada para texto
rotulo_texto = Label(janela, text="Insira um texto:")
rotulo_texto.pack()

entrada_texto = Entry(janela)
entrada_texto.pack()

# Botão para processar a entrada
botao_processar = Button(janela, text="Processar Entrada", command=processar_entrada)
botao_processar.pack(pady=10)

# Rótulo para exibir o resultado do número
resultado_numero = Label(janela, text="")
resultado_numero.pack()

# Rótulo para exibir o resultado do texto
resultado_texto = Label(janela, text="")
resultado_texto.pack()

# Iniciando o loop principal da aplicação
janela.mainloop()
