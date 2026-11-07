# Demonstra como remover espaços em branco de uma 
# string usando strip(), rstrip() e lstrip().

def adicionar_palavra(nome: str):   # Texto de exemplo = "Raphael"

    print(f'Olá, {nome}!')          # Imprime uma saudação com o nome fornecido.

    print(f'Olá, {nome.strip()}!')  # Imprime uma saudação com o nome fornecido, removendo espaços em branco no início e no final.

    print(f'Olá, {nome.rstrip()}!') # Imprime uma saudação com o nome fornecido, removendo espaços em branco no final.

    print(f'Olá, {nome.lstrip()}!') # Imprime uma saudação com o nome fornecido, removendo espaços em branco no início.

if __name__ == "__main__":
    nome = "   Lucas Matheus   "    # Nome de exemplo para teste.
    adicionar_palavra(nome)