# Utiliza o Counter da biblioteca 'collections' para contar
# a frequência de elementos em uma lista.

from collections import Counter


def funcao_corta_palavras(texto:str) -> int:
    palavras = texto.split()
    contagem = Counter(palavras)
    return contagem

if __name__ == "__main__":
    texto = "maçã banana maçã laranja banana maçã"
    print(f"Contagem de palavras: {funcao_corta_palavras(texto)}")
    print(f"Palavras mais comuns: {funcao_corta_palavras(texto).most_common(2)}")