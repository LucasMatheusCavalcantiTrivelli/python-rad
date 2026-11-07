# Demonstra a leitura de um arquivo linha por linha de 
# forma sequencial utilizando o método readline().

def ler_arquivo(caminho):
    arquivo = open(caminho, 'r')  # noqa: SIM115

    linha1 = arquivo.readline()
    print(f'Linha 1: {linha1}'.strip())
    linha2 = arquivo.readline()
    print(f'Linha 2: {linha2}'.strip())
    linha3 = arquivo.readline()
    print(f'Linha 3: {linha3}'.strip())
    linha4 = arquivo.readline()
    print(f'Linha 4: {linha4}'.strip())
    linha5 = arquivo.readline()
    print(f'Linha 5: {linha5}'.strip())

    arquivo.close()
    return linha1, linha2, linha3, linha4, linha5

if __name__ == '__main__':
    caminho_arquivo = "arquivos/nomes.txt"
    ler_arquivo(caminho_arquivo)