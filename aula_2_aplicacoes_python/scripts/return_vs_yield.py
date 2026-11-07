# Compara o uso de 'return' (retorna tudo de uma vez) e 
# 'yield' (retorna item por item usando geradores).

import time
from typing import Any, Generator  # noqa: UP035


def get_coxinhas(*pedidos) -> list: # * == variadic arguments
    print("--- [Return] Preparando TODA a fornada de coxinhas de uma vez...")
    time.sleep(1) # Simula um processo demorado
    return[f'{pedido} coxinhas' for pedido in pedidos]

def get_joelho(*pedidos) -> Generator[Any, Any, Any]:
    for pedido in pedidos:
        print(f"--- [Yield] Saindo um pedido de {pedido} joelho(s) agora!")
        yield f'{pedido} joelho(s)'

if __name__ == "__main__":
    print("SOLICITANDO COXINHAS (Return):")
    salgados_return = get_coxinhas(4, 6, 8)
    print("Recebi a lista completa:", salgados_return)

    print("\n" + "="*30 + "\n")
    print("SOLICITANDO JOELHOS (Yield):")
    pedidos_joelho = get_joelho(4, 6, 8)
    for salgado in pedidos_joelho:
        print(f"Cliente recebeu: {salgado}")