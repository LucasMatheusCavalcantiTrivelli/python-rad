# Demonstra como escrever múltiplas linhas de uma vez em um 
# arquivo a partir de uma lista usando writelines().

def caminho_arquivo(caminho):
    linhas = [
        "Esta é a primeira linha.\n",
        "Esta é a segunda linha.\n",
        "Esta é a terceira linha.\n"
    ]
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(linhas)

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

if __name__ == "__main__":
    write_caminho = 'arquivos/writelines.txt'
    caminho_arquivo(write_caminho)