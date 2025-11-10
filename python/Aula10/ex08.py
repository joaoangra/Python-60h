d = {"a": 1, "b": 2, "c": 3}
try:
    chave = input("Digite a chave que deseja acessar: ")
    print("Valor:", d[chave])
except KeyError:
    print("Erro: Chave inexistente.")
