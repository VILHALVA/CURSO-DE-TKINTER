from tkinter import *

janela = Tk()
janela.title("LABEL!")
janela.geometry("200x200")

label = Label(janela, text="PRIMEIRO LABEL", font=("Arial Bold", 50), bg="green", fg="white")
label.grid(column=0, row=0)

janela.mainloop()

