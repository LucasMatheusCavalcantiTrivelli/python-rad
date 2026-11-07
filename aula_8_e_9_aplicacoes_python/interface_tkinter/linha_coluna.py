# Compara duas formas de criar um layout em grade: usandoFrames individuais
# vs. aplicando o grid diretamente nos widgets.

import tkinter as tk


class GridApp:
    def __init__(self, raiz):
        for linha in range(3):
            for coluna in range(3):
                frame = tk.Frame(raiz, relief = tk.RAISED, bd = 1)
                frame.grid(row = linha, column = coluna, padx = 5, pady = 5)
                texto = f"Linha {linha}\nColuna {coluna}"
                tk.Label(frame, text = texto).pack()

class GridResponsivoApp:
    def __init__(self, raiz):
        for posicao in range(3):
            raiz.columnconfigure(posicao, weight = 1, minsize = 75)
            raiz.rowconfigure(posicao, weight = 1, minsize = 50)
        for linha in range(3):
            for coluna in range(3):
                texto = f"{linha}, {coluna}"
                label = tk.Label(raiz, text = texto, relief = tk.RAISED)
                label.grid(row = linha, column = coluna, padx = 5, pady = 5, sticky = "nsew")

if __name__ == "__main__":
    raiz = tk.Tk()
    GridApp(raiz)               # Sempre o último será priorizado, a dessa linha é ignorada.
    GridResponsivoApp(raiz)
    raiz.mainloop()