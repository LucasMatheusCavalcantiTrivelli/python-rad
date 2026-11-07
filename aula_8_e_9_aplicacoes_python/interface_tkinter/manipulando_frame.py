# Manipula o tamanho de Frames usando pack() com osparâmetros fill
# e expand para criar um layout flexível.

import tkinter as tk


class PackApp:
    def __init__(self, raiz):
        tamanhos = [(100, "red"), (50, "green"), (25, "blue")]
        for tamanho, cor in tamanhos:
            frame = tk.Frame(raiz, width = tamanho, height = tamanho, bg = cor)
            frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True) 
            # Esse frame.pack() afeta diretamente a exibição da função na janela!

if __name__ == "__main__":
    raiz = tk.Tk()
    PackApp(raiz)
    raiz.mainloop()