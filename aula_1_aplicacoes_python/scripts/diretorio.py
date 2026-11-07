# Utiliza o módulo 'os' para construir e verificar caminhos relativos
# e absolutos de arquivos em subdiretórios.

import os


def diretorio_arquivo(nome_arquivo):
    diretorio = os.path.dirname(os.path.abspath(__file__))
    diretorio_raiz = os.path.dirname(diretorio)

    caminho_relativo = os.path.join('arquivos', nome_arquivo)
    caminho_absoluto = os.path.join(diretorio_raiz, caminho_relativo)

    print(f'Caminho relativo: {caminho_relativo}')
    print(f'Caminho absoluto: {caminho_absoluto}')

    print(f'Arquivo existente: {os.path.isfile(caminho_absoluto)}')
    # Se tiver um arquivo chamado 'diretorio.txt' dentro da pasta 'arquivos', 
    # o resultado será True, caso contrário, False.

if __name__ == '__main__':
    diretorio_arquivo('diretorio.txt')