peso = float(input("Digite seu Peso (kg): "))
altura = float(input("Digite sua Altura (m): "))

IMC = peso / (altura * altura)

print(f"Seu IMC é: {IMC:.2f}")

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso ideal")
elif IMC < 30:
    print("Levemente acima do peso")
elif IMC < 35:
    print("Obesidade I")
elif IMC < 40:
    print("Obesidade II (Severa)")
else:
    print("Obesidade III (Mórbida)")