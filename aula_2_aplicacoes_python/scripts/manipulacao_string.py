# Demonstra técnicas de fatiamento (slicing),
# contagem de caracteres e busca de substrings em uma string.

def adicionar_texto(texto: str):

    print(texto[2])                 # Vai ditar a letra que está na posição 2 da string, no caso a letra "s".

    print(texto[:15])               # Vai ditar os caracteres da posição 0 até a 14.

    print(texto[0:20:2])            # Vai ditar os caracteres da posição 0 até a 19, pulando de 2 em 2.
    print(len(texto))               # Vai ditar o comprimento da string.

    print(texto.count("a"))         # Vai ditar a quantidade de vezes que a letra "a" aparece na string.

    print(texto.count("a", 5, 30))  # Vai ditar a quantidade de vezes que a letra "a" aparece na string, entre as posições 5 e 30.

    print(texto.find("aula"))       # Vai ditar a posição da primeira ocorrência da palavra "aula" na string.

    print(texto.find("Python"))     # Vai ditar a posição da primeira ocorrência da palavra "Python" na string.

    print('String' in texto)        # Vai ditar se a palavra "String" está presente na string.

    print("Raphael" in texto)       # Vai ditar se a palavra "Raphael" está presente na string.

if __name__ == "__main__":
    texto = "Esta é uma aula de Python, onde vamos aprender sobre String."
    adicionar_texto(texto)