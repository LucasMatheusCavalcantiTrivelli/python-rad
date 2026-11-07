# Utiliza Expressões Regulares (Regex) para localizar
# e ocultar endereços de e-mail em um texto.

import re


def pesquisa_email(texto: str, escondido: bool) -> None:
    padrao = r'\b[0-9._%+-]+@[a-z]+\.[a-z]{3,}\b'

    if escondido:
        novo_texto = re.sub(padrao, "[email oculto]", texto)
        print("Resultado:", novo_texto)
    else:
        emails_encontrados = re.findall(padrao, texto)
        if emails_encontrados:
            print("E-mails encontrados:", ", ".join(emails_encontrados))
        else:
            print("Nenhum e-mail encontrado.")

if __name__ == "__main__":
    texto = "Meu e-mail é exemplo@email.com, 22@66.88, 22@aa.bbb, entre em contato."
    pesquisa_email(texto, True)