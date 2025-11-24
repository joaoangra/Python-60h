import pandas as pd

dados = {
    'nome': ['Ana', 'Bruno', 'Carlos'],
    'idade': [23, 35, 45],
    'salario': [5000, 7000, 9000]
    }

df = pd.DataFrame(dados)
df['bonus'] = df['salario'] * 0.1
print(df)

df = df.drop(columns=['bonus'])

print(df)