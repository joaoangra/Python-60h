try:
    n = int(input("Digite um número inteiro: "))
    print("Você digitou:", n)
except ValueError:
    print("Erro: Não é um número inteiro.")
