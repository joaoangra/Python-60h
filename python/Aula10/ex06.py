try:
    c = float(input("Digite a temperatura em Celsius: "))
    f = (c * 9/5) + 32
    print("Temperatura em Fahrenheit:", f)
except ValueError:
    print("Erro: Entrada inválida.")
