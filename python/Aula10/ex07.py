try:
    numeros = input("Digite números separados por vírgula: ").split(",")
    numeros = [float(x) for x in numeros]
    media = sum(numeros) / len(numeros)
    print("Média:", media)
except ValueError:
    print("Erro: Entrada inválida. Use apenas números.")
except ZeroDivisionError:
    print("Erro: Lista vazia.")
