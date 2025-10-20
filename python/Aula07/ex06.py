from random import randint

print("Tente Adivinhar o número que estou pensando entre 1 e 10:")
numero_secreto = randint(1, 10)

while True:
    try:
        tentativa = int(input("Qual é o seu palpite?: "))
    except ValueError:
        print("Por favor, insira um número inteiro entre 1 e 10.")
        continue

    if tentativa == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Voce errou!")
        continuar = input("Deseja tentar novamente? (s/n): ")
        if continuar.lower() != 's':
            print(f"O número secreto era {numero_secreto}. Até a próxima!")
            break