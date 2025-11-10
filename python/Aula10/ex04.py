import math
try:
    num = float(input("Digite um número: "))
    if num < 0:
        raise ValueError("Número negativo.")
    print("Raiz quadrada:", math.sqrt(num))
except ValueError as e:
    print("Erro:", e)
