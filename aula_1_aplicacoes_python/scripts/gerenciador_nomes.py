# Simula um gerenciador simples: adiciona nomes a um arquivo de texto 
# no modo append ('a') e depois lê o conteúdo.

def caminho_arquivo(caminho):
    arquivo = open(caminho, 'a', encoding='utf-8')  # noqa: SIM115
    return arquivo

def adicionar_nome(arquivo, nome):
    arquivo.write(nome + '\n')

def ler_nomes(nome):
    arquivo = open(nome, 'r', encoding='utf-8')  # noqa: SIM115
    nomes = arquivo.readlines()
    arquivo.close()
    return nomes

if __name__ == '__main__':
    digite_caminho = "arquivos/nomes.txt"
    for n in ["Ana", "Bruno", "Carla"]:
        with caminho_arquivo(digite_caminho) as arquivo:
            adicionar_nome(arquivo, n)
        print(f"Nome '{n}' adicionado ao arquivo.")

    print("Nomes no arquivo:")
    for nome in ler_nomes(digite_caminho):
        print(nome.strip())