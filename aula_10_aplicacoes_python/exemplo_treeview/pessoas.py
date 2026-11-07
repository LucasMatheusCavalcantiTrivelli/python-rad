# Modelo de dados (entidade) que representa uma Pessoa
# com nome e idade.

class Pessoas:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade