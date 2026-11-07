# Demonstra a substituição de palavras com replace() 
# e verificação de início/fim com startswith() e endswith().

def adicionar_texto(texto: str):    # Texto de exemplo = "Nossa aula manipulando string."

    novo_texto = texto.replace("manipulando", "trabalhando com")    # Troca a palavra "manipulado" por "trabalhando com".
    print(novo_texto)                                               # Vai ditar a frase com a palavra trocada.

    print(texto.startswith("Nossa"))    # Verifica se começa com essa palavra.
    print(texto.startswith("aula"))     # Verifica se começa com essa palavra.

    print(texto.endswith("aula"))   # Verifica se finaliza a frase com essa palavra.
    print(texto.endswith("."))      # Verifica se finaliza a frase com esse caractere.

if __name__ == "__main__":
    texto1 = "Nossa aula manipulando string."
    texto2 = "Aula de hoje é sobre manipulação de strings." # A letra maiúscula importa.
    adicionar_texto(texto1, texto2)