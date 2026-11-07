# Demonstra como abrir um arquivo no modo de escrita ('w')
# e inserir dados usando write() e writelines().

def escrever_arquivo(caminho):

    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.write('Esta é a primeira linha.\n')
        arquivo.write('Esta é a segunda linha.\n')

        linhas = ['Esta é a primeira linha em uma lista.\n', 'Esta é a segunda linha em uma lista.\n']
        arquivo.writelines(linhas)

if __name__ == '__main__':
    caminho_arquivo = "arquivos/escrevendo.txt"
    escrever_arquivo(caminho_arquivo)