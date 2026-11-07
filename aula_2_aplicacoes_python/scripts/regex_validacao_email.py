# Valida uma lista de e-mails utilizando Expressões Regulares para checar o formato correto.

import re

PADRAO_EMAIL = re.compile(r'^\w+([\.-]?\w+)*@\w{4,}+([\.-]?\w+)*(\.\w{2,3})+$')

def validar_email(email: list[str]) -> list[bool]:
    return bool(PADRAO_EMAIL.match(email))

if __name__ == "__main__":
    exemplos_emails = [
        "usuario@email.com",        # Válido
        "nome+tag@email.com",       # Inválido
        "a@b.co",                   # Inválido, domínio curto
        "usuario@email.co.uk",      # Válido
        "@email.com",               # Inválido, sem usuário
        "usuario@.com",             # Inválido
        "usuario@email",            # Inválido, sem TLD(Top Level Domain)
        "usu ario@email..com",      # Inválido, espaço
    ]
    for email in exemplos_emails:
        if validar_email(email):
            print(f"{email} é um endereço de e-mail válido.")
        else:
            print(f"{email} é um endereço de e-mail inválido.")