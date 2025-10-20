print("Digite um número de 1 a 10 para ver sua tabuada:")
num = int(input())
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")