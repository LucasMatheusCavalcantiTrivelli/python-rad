# Aplica o tratamento de exceções (FileNotFoundError, OSError) na leitura de
# arquivos para evitar que o programa quebre.

def ler_arquivo(caminho):
    try:
        f = open(caminho)  # noqa: SIM115
        s = f.readline()
        i = str(s.strip())
    except FileNotFoundError:
        print(f"Arquivo '{caminho}' não encontrado.")
        return
    except OSError:
        print("Erro na abertura do arquivo.")
        return
    except ValueError:
        print("Formato inválido encontrado no arquivo.")
        return
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise
    finally:
        f.close()
    print(f"{i}")

if __name__ == "__main__":
    inserir_caminho = "arquivos/nomes.txt"
    ler_arquivo(inserir_caminho)