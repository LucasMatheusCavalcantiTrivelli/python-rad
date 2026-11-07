# Demonstra a diferença e o uso dos métodos split() (string para lista) 
# e join() (lista para string).

def adicionar_palavra(texto: str):  # Texto de exemplo = "Nossa aula manipulando string."

    texto.split()                   # Divide o texto em uma lista de palavras, usando espaços como delimitadores
    print(' '.join(texto))          # Imprime o texto com palavras separadas por espaços
    print(texto.split())            # Imprime uma lista com as palavras do texto
    print(' '.join(texto.split()))  # Imprime o texto com palavras separadas por espaços

if __name__ == "__main__":
    texto = "Nossa aula manipulando string."  # Texto de exemplo para teste.
    adicionar_palavra(texto)