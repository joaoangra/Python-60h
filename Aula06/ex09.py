import calendar

ano = int(input("Digite um ano: "))

if calendar.isleap(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")