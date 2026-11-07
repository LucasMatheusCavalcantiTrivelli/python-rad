# Demonstra a manipulação de bytes puros: converte texto para binário,
# salva em arquivo e exibe a representação em bits.

import os

diretorio_aula4 = os.path.dirname(os.path.abspath(__file__))
diretorio_pai = os.path.dirname(diretorio_aula4)
dados_binarios_nome = os.path.join(diretorio_pai, "arquivos", "dados_puros.bin")

frase = "Raphael"
dados_binarios = frase.encode('utf-8')

try:
    with open(dados_binarios_nome, "wb") as salva_binario:
        salva_binario.write(dados_binarios)
    print("Dados binários salvos com sucesso!")
except Exception as e:  # noqa: BLE001
    print(f"Ocorreu um erro ao salvar os dados binários: {e}")

if os.path.exists(dados_binarios_nome):
    try:
        with open(dados_binarios_nome, "rb") as carrega_binario:
            dados_carregados_bytes = carrega_binario.read()
            dados_carregados_texto = dados_carregados_bytes.decode('utf-8')
            binario_real = " ".join(f"{byte:08b}" for byte in dados_carregados_bytes)
        print("Dados carregados com sucesso:")
        print(f"{binario_real} -> {dados_carregados_texto}")
    except Exception as e:  # noqa: BLE001
        print(f"Ocorreu um erro ao carregar os dados binários: {e}")