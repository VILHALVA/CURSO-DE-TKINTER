from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Importe do módulo Pillow para manipulação de imagem

class AnimalApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Escolha um Animal")

        # Lista de opções para a Combobox
        self.opcoes_animais = ["Cachorro", "Gato", "Pássaro", "Peixe"]

        # Criando a Combobox
        self.combo_animais = ttk.Combobox(janela, values=self.opcoes_animais, state="readonly")
        self.combo_animais.set("Escolha um animal")
        self.combo_animais.pack(pady=10)

        # Rótulo para exibir a imagem
        self.rotulo_imagem = Label(janela)
        self.rotulo_imagem.pack(pady=10)

        # Botão para exibir a imagem do animal selecionado
        self.botao_exibir_imagem = Button(janela, text="Exibir Imagem", command=self.exibir_imagem)
        self.botao_exibir_imagem.pack()

    def exibir_imagem(self):
        animal_selecionado = self.combo_animais.get()

        # Mapeamento do animal para o nome do arquivo de imagem
        mapa_animais = {
            "Cachorro": "dog.png",
            "Gato": "cat.png",
            "Pássaro": "bird.png",
            "Peixe": "fish.png",
        }


        # Verifica se o animal selecionado tem uma imagem correspondente
        if animal_selecionado in mapa_animais:
            nome_arquivo = mapa_animais[animal_selecionado]

            # Carrega a imagem usando Pillow (PIL)
            imagem = Image.open(nome_arquivo.replace("\\", "/"))
            imagem = imagem.resize((200, 200))  # Redimensiona a imagem para 200x200 pixels
            imagem_tk = ImageTk.PhotoImage(imagem)

            # Atualiza o rótulo com a nova imagem
            self.rotulo_imagem.configure(image=imagem_tk)
            self.rotulo_imagem.imagem_tk = imagem_tk  # Evita que a imagem seja coletada pelo coletor de lixo

        else:
            # Se o animal não tiver uma imagem correspondente, exibe uma mensagem
            self.rotulo_imagem.configure(text="Não há imagem disponível para este animal")

# Criando a janela principal
janela = Tk()

# Criando uma instância da aplicação
app = AnimalApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
