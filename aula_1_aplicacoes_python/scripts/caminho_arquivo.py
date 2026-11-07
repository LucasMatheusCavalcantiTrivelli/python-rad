# Demonstra o uso dos métodos seek() e tell() para manipular 
# a posição do cursor de leitura/escrita no arquivo.

def caminho_arquivo(caminho):

    with open(caminho, "w", encoding="utf-8") as f:
        f.write("Exemplo de uso dos métodos seek() e tell() em Python.\n")

    with open(caminho, "r", encoding="utf-8") as f:
        print("Posição inicial do cursor:", f.tell())

        conteudo = f.read(10)
        print("Conteúdo lido:", conteudo)
        print("Posição do cursor após ler 10 caracteres:", f.tell())

        f.seek(0, 0)
        print("Posição do cursor após seek(0, 0):", f.tell())

        f.seek(15,0)
        print("Posição do cursor após seek(15, 0):", f.tell())
        parte = f.read(5)
        print("Conteúdo lido após seek(15, 0):", parte)

        pos_atual = f.tell()
        f.seek(pos_atual - 5, 0)
        print("Posição do cursor após retroceder 5 caracteres:", f.tell())
        parte2 = f.read(5)
        print("Conteúdo lido após retroceder 5 caracteres:", parte2)

        f.seek(0, 2)
        print("Posição do cursor no fim do arquivo:", f.tell())

if __name__ == "__main__":
    exemplo_caminho = "arquivos/exemplo.txt"
    caminho_arquivo(exemplo_caminho)