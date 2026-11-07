# Demonstra o uso dos blocos try, except, else e 
# finally para o tratamento seguro de exceções.

def divide(x, y):
    try:
        resultado = x/y
    except ZeroDivisionError:
        print("Opa, para aí! Você está tentando dividir por zero!!!")
    else:
        print("Certa! A sua resposta: ", resultado)
    finally:
        print('Esse texto sempre aparecerá')

if __name__ == "__main__":
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    divide(x, y)