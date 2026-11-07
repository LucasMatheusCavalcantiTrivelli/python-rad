# Demonstra métodos de formatação de caixa de texto:
# lower(), upper(), capitalize(), title() e swapcase().

def adicionar_palavra(texto:str):   # Texto de exemplo = "Nossa aula manipulando string."

    print(texto.lower())            # Vai ditar a frase toda em letras minúsculas.

    print(texto.upper())            # Vai ditar a frase toda em letras maiúsculas.

    print(texto.capitalize())       # Vai ditar a frase com a primeira letra em maiúscula e o restante em minúscula.

    print(texto.title())            # Vai ditar a frase com a primeira letra de cada palavra em maiúscula e o restante em minúscula.

    print(texto.swapcase())         # Vai ditar a frase com as letras maiúsculas em minúsculas e as letras minúsculas em maiúsculas.

if __name__ == "__main__":
    texto = "Nossa aula manipulando string."
    adicionar_palavra(texto)