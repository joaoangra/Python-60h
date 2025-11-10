print ("Jogo de adivinhação!")

import random

num =random.randint (1, 100)

resp = 0

while resp != num:
    resp = int (input("Digite um número entre 1 a 100: "))
    if resp < num:
        print("Chute muito baixo, tente novamente.")
    elif resp > num:
        print("Chute alto demais, tente novamente.")
    else:
        print("Boa, boa, você acertou!")