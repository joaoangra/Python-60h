class DivisaoPorZeroError(Exception):
    pass

def dividir(a, b):
    if b == 0:
        raise DivisaoPorZeroError("Divisão por zero não é permitida.")
    return a / b

try:
    x = float(input("Digite o numerador: "))
    y = float(input("Digite o denominador: "))
    print("Resultado:", dividir(x, y))
except DivisaoPorZeroError as e:
    print("Erro:", e)
except ValueError:
    print("Erro: Entrada inválida.")
