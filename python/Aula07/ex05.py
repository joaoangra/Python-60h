print("insira um número inteiro positivo (se ele for negativo, o programa será encerrado):")
numero = int(input())
while numero >= 0:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    print("insira um número inteiro positivo (se ele for negativo, o programa será encerrado):")
    numero = int(input())
print("Programa encerrado.")