lista = [10, 20, 30]
try:
    i = int(input("Digite o índice que deseja acessar (0 a 2): "))
    print("Valor:", lista[i])
except IndexError:
    print("Erro: Índice fora do intervalo.")
except ValueError:
    print("Erro: Índice inválido.")
