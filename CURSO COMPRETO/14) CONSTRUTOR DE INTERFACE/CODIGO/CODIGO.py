import tkinter as tk
from tkinter import ttk

def clicar():
    label1.config(text="Botão Clicado!")

root = tk.Tk()
root.geometry("300x200")

label1 = ttk.Label(root, text="Olá, Tkinter!")
label1.pack(pady=10)

button1 = ttk.Button(root, text="Clique em Mim!", command=clicar)
button1.pack(pady=10)

root.mainloop()
