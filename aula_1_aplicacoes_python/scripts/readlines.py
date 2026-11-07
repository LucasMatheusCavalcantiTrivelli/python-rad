# Demonstra a leitura completa de um arquivo, armazenando todas 
# as linhas em uma lista usando readlines().

def ler_arquivo(caminho):
    arquivo = open(caminho, 'r', encoding='utf-8')  # noqa: SIM115
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas, start=1):
        print(f'Linha {i}: {linha.strip()}')
    arquivo.close()

if __name__ == '__main__':
    caminho_arquivo = "arquivos/nomes.txt"
    ler_arquivo(caminho_arquivo)