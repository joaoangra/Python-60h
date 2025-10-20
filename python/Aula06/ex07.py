n1 = int(input("Digite o Primeiro lado do triangulo: "))
n2 = int(input("Digite o Segundo lado do triangulo: "))
n3 = int(input("Digite o Terceiro lado do triangulo: "))

if n1 == n2 and n2 == n3:
    print("O triangulo é esquiláteros")
elif n1 == n2 or n1 == n3 or n2 == n3:
    print("O triangulo é isósceles")
else:
    print("O triangulo é escaleno")

