# Cria uma janela com um rótulo e um botão, demonstrando o
# empilhamento vertical com pack().

import tkinter as tk


def contruir_janela(texto: str = "Placeholder"):
    texto = tk.Label(
        text = texto,
        foreground = "red",
        background = "black",
        width = 80, # Eixo X, o valor é em caracteres, com proporção de 1/2 com height.
        height = 40 # Eixo Y, o valor é em linhas, com proporção de 2/1 com width.
    )
    texto.pack()

def contruir_botao(texto: str = "Placeholder"):
    botao = tk.Button(
        text = texto,
        width = 25,
        height = 5,
        bg = "blue",
        fg = "yellow"
    )
    botao.pack()

if __name__=="__main__":
    janela = tk.Tk()
    contruir_janela("Janela de Teste")  # Executando os dois ao mesmo tempo
    contruir_botao("Botão")             # irá fundir ele em uma janela só.
    janela.mainloop()