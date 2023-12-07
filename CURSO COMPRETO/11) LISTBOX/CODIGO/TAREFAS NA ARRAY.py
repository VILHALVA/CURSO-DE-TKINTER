from tkinter import *

class ListaTarefasApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Lista de Tarefas")

        # Lista para armazenar as tarefas
        self.tarefas = []

        # Criando o Listbox
        self.lista_tarefas = Listbox(janela, selectmode=SINGLE)
        self.lista_tarefas.pack(pady=10)

        # Entrada de texto para adicionar novas tarefas
        self.entrada_tarefa = Entry(janela)
        self.entrada_tarefa.pack(pady=5)

        # Botões para adicionar e remover tarefas
        self.botao_adicionar = Button(janela, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_remover = Button(janela, text="Remover Tarefa", command=self.remover_tarefa)

        self.botao_adicionar.pack(pady=5)
        self.botao_remover.pack(pady=5)

    def adicionar_tarefa(self):
        nova_tarefa = self.entrada_tarefa.get()
        if nova_tarefa:
            self.tarefas.append(nova_tarefa)
            self.atualizar_lista_tarefas()
            self.entrada_tarefa.delete(0, END)  # Limpa a entrada de texto

    def remover_tarefa(self):
        indices_selecionados = self.lista_tarefas.curselection()

        if indices_selecionados:
            indice_selecionado = indices_selecionados[0]
            self.tarefas.pop(indice_selecionado)
            self.atualizar_lista_tarefas()

    def atualizar_lista_tarefas(self):
        self.lista_tarefas.delete(0, END)  # Limpa o Listbox

        for tarefa in self.tarefas:
            self.lista_tarefas.insert(END, tarefa)

# Criando a janela principal
janela = Tk()

# Criando uma instância da aplicação
app = ListaTarefasApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
