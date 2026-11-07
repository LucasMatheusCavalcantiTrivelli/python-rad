# Demonstra o uso de defaultdict para evitar erros de
# KeyError ao criar listas dentro de dicionários.

from collections import defaultdict


def salas_de_aula(estudantes: list, salas: list) -> dict:
    estudantes_por_salas = defaultdict(list)
    num_salas = len(salas)

    for i, estudante in enumerate(estudantes):
        sala_destino = salas[i % num_salas]
        estudantes_por_salas[sala_destino].append(estudante)
    return dict(estudantes_por_salas)

if __name__ == "__main__":
    alunos = ["Raphael", "Gilson", "Sara", "Vanessa", "Ana"]
    salas = ["307A", "308A"]
    print(salas_de_aula(alunos, salas))