import tkinter as tk
import json
from tkinter import messagebox

class ListaTarefasApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Lista de Tarefas")

        # Carrega as tarefas do arquivo ou cria uma lista vazia se o arquivo não existir
        self.tarefas = self.carregar_tarefas()

        # Criando o Listbox
        self.lista_tarefas = tk.Listbox(janela, selectmode=tk.SINGLE)
        self.lista_tarefas.pack(pady=10)

        # Entrada de texto para adicionar novas tarefas
        self.entrada_tarefa = tk.Entry(janela)
        self.entrada_tarefa.pack(pady=5)

        # Botões para adicionar e remover tarefas
        self.botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_remover = tk.Button(janela, text="Remover Tarefa", command=self.remover_tarefa)

        self.botao_adicionar.pack(pady=5)
        self.botao_remover.pack(pady=5)

        # Atualiza o Listbox com as tarefas carregadas
        self.atualizar_lista_tarefas()

    def adicionar_tarefa(self):
        nova_tarefa = self.entrada_tarefa.get()
        if nova_tarefa:
            self.tarefas.append(nova_tarefa)
            self.salvar_tarefas()
            self.atualizar_lista_tarefas()
            self.entrada_tarefa.delete(0, tk.END)  # Limpa a entrada de texto

    def remover_tarefa(self):
        indices_selecionados = self.lista_tarefas.curselection()

        if indices_selecionados:
            indice_selecionado = indices_selecionados[0]
            self.tarefas.pop(indice_selecionado)
            self.salvar_tarefas()
            self.atualizar_lista_tarefas()

    def atualizar_lista_tarefas(self):
        self.lista_tarefas.delete(0, tk.END)  # Limpa o Listbox

        for tarefa in self.tarefas:
            self.lista_tarefas.insert(tk.END, tarefa)

    def salvar_tarefas(self):
        try:
            with open("settings.json", "w") as arquivo:
                json.dump(self.tarefas, arquivo)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar as tarefas: {e}")

    def carregar_tarefas(self):
        try:
            with open("settings.json", "r") as arquivo:
                return json.load(arquivo)
        except FileNotFoundError:
            return []
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar as tarefas: {e}")
            return []

# Criando a janela principal
janela = tk.Tk()

# Criando uma instância da aplicação
app = ListaTarefasApp(janela)

# Iniciando o loop principal da aplicação
janela.mainloop()
