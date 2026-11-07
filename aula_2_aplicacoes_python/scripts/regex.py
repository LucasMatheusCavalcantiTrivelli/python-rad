# Introdução ao módulo 're': busca um padrão de número de 
# telefone no formato (XXX) XXX-XXXX.

import re


def verifica_regex(texto: str) -> None:
    padrao = r'\(\d{3}\) \d{3}-\d{4}' # Padrão para encontrar número de telefone no formato (XXX) XXX-XXXX
    resultado = re.search(padrao, texto)
    if resultado:
        numero_telefone = resultado.group()
        print("Número de telefone encontrado:", numero_telefone)
    else:
        print("Número de telefone não encontrado.")

if __name__ == "__main__":
    texto = "O número de telefone de Raphael é (123) 456-7890."
    verifica_regex(texto)