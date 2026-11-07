# Utiliza a biblioteca pickle para serializar (salvar) e desserializar (carregar)
# objetos Python em arquivos binários.

import pickle


def salva_binario(nome_arquivo: str):
    dados = {"nome": "Raphael", "idade": 41, "profissão": "Desenvolvedor"}
    try:
        with open(nome_arquivo, "wb") as salva_binario:
            pickle.dump(dados, salva_binario)
        print("Dados salvos com sucesso!")
    except Exception as e:  # noqa: BLE001
        print(f"Ocorreu um erro ao salvar os dados: {e}")

def carrega_binario(nome_arquivo: str):
    try:
        with open(nome_arquivo, "rb") as carrega_binario:
            dados_carregados = pickle.load(carrega_binario)
        print("Dados carregados com sucesso:", dados_carregados)
    except Exception as e:  # noqa: BLE001
        print(f"Ocorreu um erro ao carregar os dados: {e}")

if __name__ == "__main__":
    digite_nome_arquivo = "arquivos/binario.pkl"
    salva_binario(digite_nome_arquivo)
    carrega_binario(digite_nome_arquivo)