# Exemplo básico de criação de janela e exibição de um
# rótulo simples (Hello World).

import tkinter as tk

janela = tk.Tk()
ola = tk.Label(text="Hello World!")
ola.pack()
janela.mainloop()