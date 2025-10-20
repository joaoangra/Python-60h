print("CALCULADORA!")

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
calc = input("Digite o operador (+, -, /, *): ")

if calc == '+':
    print(f"O valor SOMADO é", {n1 + n2})
elif calc == '-':
    print(f"O valor SUBTRAIDO é", {n1 - n2})
elif calc == '*':
    print(f"O valor MULTIPLICADO é", {n1 * n2})
elif calc == '-':
    print(f"O valor DIVIDIDO é", {n1 / n2})