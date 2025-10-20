n1 = float(input("Digite quanto voce ganha por hora: "))
n2 = int(input("Digite quantas horas voce trabalhou no mês: "))

SB = n1 * n2

IR = SB * 0.11

INSS = SB * 0.08

Sindicato =  SB * 0.05

Descontos = IR + INSS + Sindicato

SL = SB - Descontos

print("Seu salario Bruto sera de: ", SB)
print("Seu Desconto de Imposto de Renda sera de: ", IR)
print("Seu Desconto de INSS sera de: ", INSS)
print("Seu Desconto do Sindicato sera de: ", Sindicato)
print("Seu salario Liquido sera de: ", SL)