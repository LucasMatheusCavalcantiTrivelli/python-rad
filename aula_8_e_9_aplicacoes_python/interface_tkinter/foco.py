# Usa eventos de foco (FocusIn/FocusOut) para criar um texto de
# espaço reservado (placeholder) em um campo de entrada.

import tkinter as tk


class FocoApp:
    def __init__(self, raiz):
        self.texto_padrao = "Digite seu nome aqui!"
        self.entrada = tk.Entry(raiz, fg = "gray", width = 30)
        self.entrada.insert(0, self.texto_padrao)
        self.entrada.pack(pady = 20)
        self.entrada.bind("<FocusIn>", self.limpar)
        self.entrada.bind("<FocusOut>", self.restaurar)

    def limpar(self, _):
        if self.entrada.get() == self.texto_padrao:
            self.entrada.delete(0, tk.END)
            self.entrada.config(fg = "black")

    def restaurar(self, _):
        if not self.entrada.get():
            self.entrada.insert(0, self.texto_padrao)
            self.entrada.config(fg = "gray")

if __name__ == "__main__":
    raiz = tk.Tk()
    FocoApp(raiz)
    raiz.mainloop()