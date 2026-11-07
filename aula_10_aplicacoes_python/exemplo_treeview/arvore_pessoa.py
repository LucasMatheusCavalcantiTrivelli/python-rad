# Isola a lógica de manipulação da árvore (Treeview), recebendo
# a tree e gerenciando a lista de pessoas.

from pessoas import Pessoas


class Arvore_Pessoa:
    def __init__(self, tree):
        self.lista_pessoas = []
        self.tree = tree

    def adicionar_pessoa(self, pessoa: Pessoas):
        self.lista_pessoas.append(pessoa)
        self.tree.insert("", "end", text=pessoa.nome, values=(pessoa.idade,))

    def ler_pessoas(self):
        for pessoa in self.lista_pessoas:
            self.tree.insert("", "end", text=pessoa.nome, values=(pessoa.idade,))