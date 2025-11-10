try:
    with open("arquivo.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    with open("arquivo.txt", "w") as f:
        f.write("Erro: arquivo não existia e foi criado.")
    print("Arquivo não encontrado. Criado novo arquivo com mensagem de erro.")
