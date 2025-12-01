import pandas as pd

dados = {
    'nome': ['Ana Souza', 'João Lima', 'Carla Mendes', 'Pedro Rocha'],
    'idade': [28, 32, 41, 22],
    'salario': [3500, 4200, 5100, 2800]
    }

#Mostrando somente os funcionários com salário acima da média
df = pd.DataFrame(dados)
media_salario = df['salario'].mean()
print("Média salarial: R$", media_salario)
funcionarios_acima_media = df[ df['salario'] > media_salario ]
print("\nFuncionários com salário acima da média:\n", funcionarios_acima_media)

#Orgnizando os dados em ordem decrescente de salário
df_ordenado = df.sort_values('salario', ascending=False)
print("\nFuncionários ordenados por salário (decrescente):\n", df_ordenado)

#Filtrando funcionários com idade menor que 30
jovens = df[ df['idade'] < 30 ]
print("\nFuncionários com idade menor que 30:\n", jovens)
