# Demonstra o uso de pop-ups (messagebox) para exibir mensagens de sucesso ou
# alerta com base na entrada do usuário.

import tkinter as tk
from tkinter import messagebox


class Nome:
    def __init__(self, nome: str) -> None:
        self.nome = nome

class Funcionalidades:
    def mostrar_nome(self):
        texto = entrada.get().strip()
        if texto:
            usuario = Nome(texto)
            messagebox.showinfo("Cadastro", f"Olá, {usuario.nome}!")
        else:
            messagebox.showwarning("Atenção", "Informe seu nome.")

if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Cadastro")
    janela.geometry("300x100")
    
    tk.Label(janela, text="Nome:").pack(pady=5)
    
    entrada = tk.Entry(janela)
    entrada.pack(padx=16)
    
    app = Funcionalidades()
    
    tk.Button(janela, text="Enviar", command=app.mostrar_nome).pack(pady=10)
    
    janela.mainloop()