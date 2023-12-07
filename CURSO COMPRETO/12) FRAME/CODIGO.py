import tkinter as tk

class CadastroUsuarioApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cadastro de Usuário")

        # Criando frames para diferentes seções do formulário
        self.frame_pessoal = tk.Frame(janela, borderwidth=2, relief="groove")
        self.frame_endereco = tk.Frame(janela, borderwidth=2, relief="groove")
        self.frame_botoes = tk.Frame(janela)

        # Adicionando widgets ao frame_pessoal
        self.label_nome = tk.Label(self.frame_pessoal, text="Nome:")
        self.entry_nome = tk.Entry(self.frame_pessoal)

        self.label_idade = tk.Label(self.frame_pessoal, text="Idade:")
        self.entry_idade = tk.Entry(self.frame_pessoal)

        # Adicionando widgets ao frame_endereco
        self.label_endereco = tk.Label(self.frame_endereco, text="Endereço:")
        self.entry_endereco = tk.Entry(self.frame_endereco)

        self.label_cidade = tk.Label(self.frame_endereco, text="Cidade:")
        self.entry_cidade = tk.Entry(self.frame_endereco)

        # Adicionando botões ao frame_botoes
        self.botao_salvar = tk.Button(self.frame_botoes, text="Salvar", command=self.salvar_cadastro)
        self.botao_limpar = tk.Button(self.frame_botoes, text="Limpar", command=self.limpar_formulario)

        # Posicionando os frames na janela principal
        self.frame_pessoal.pack(pady=10)
        self.frame_endereco.pack(pady=10)
        self.frame_botoes.pack()

        # Posicionando os widgets dentro dos frames_pessoal e frame_endereco
        self.label_nome.grid(row=0, column=0, sticky="e")
        self.entry_nome.grid(row=0, column=1)

        self.label_idade.grid(row=1, column=0, sticky="e")
        self.entry_idade.grid(row=1, column=1)

        self.label_endereco.grid(row=0, column=0, sticky="e")
        self.entry_endereco.grid(row=0, column=1)

        self.label_cidade.grid(row=1, column=0, sticky="e")
        self.entry_cidade.grid(row=1, column=1)

        # Posicionando os botões no frame_botoes
        self.botao_salvar.pack(side=tk.LEFT, padx=5)
        self.botao_limpar.pack(side=tk.LEFT, padx=5)

    def salvar_cadastro(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        endereco = self.entry_endereco.get()
        cidade = self.entry_cidade.get()

        # Aqui você pode adicionar a lógica para salvar os dados em um banco de dados, arquivo, etc.
        print(f"Usuário cadastrado: Nome={nome}, Idade={idade}, Endereço={endereco}, Cidade={cidade}")

    def limpar_formulario(self):
        # Limpa todos os campos de entrada
        self.entry_nome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)
        self.entry_cidade.delete(0, tk.END)

# Criando a janela principal
janela = tk.Tk()

# Criando uma instância da aplicação
app = CadastroUsuarioApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
