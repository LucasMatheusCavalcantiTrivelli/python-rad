# Cria a interface inicial de uma árvore (Treeview) e instancia
# a classe de controle para adicionar pessoas.

import tkinter as tk
from tkinter import ttk

from arvore_pessoa import Arvore_Pessoa
from pessoas import Pessoas


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo Treeview")
        self.root.geometry("520x300")

        self.tree = ttk.Treeview(root, columns=("idade",), show="tree headings")
        self.tree.heading("#0", text="Nome", anchor="center")
        self.tree.heading("idade", text="Idade", anchor="center")
        self.tree.column("#0", anchor="w")
        self.tree.column("idade", anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.minha_arvore = Arvore_Pessoa(tree = self.tree)

        self.minha_arvore.adicionar_pessoa(Pessoas("Ana", 25))
        self.minha_arvore.adicionar_pessoa(Pessoas("Bruno", 30))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()