import pandas as pd

dados = {
    'Produto': ['Impressora', 'Tablet', 'SSD', 'Mouse'],
    'Avaliações': [
        [5, 4, 4, 3],    # Impressora
        [4, 5, 5, 5],    # Tablet
        [5, 5, 5, 4],    # SSD
        [3, 4, 3, 4]     # Mouse
    ]
}

df = pd.DataFrame(dados)

# Criando uma coluna com a média das avaliações
df['Média Avaliações'] = df['Avaliações'].apply(lambda x: sum(x) / len(x))

# Filtrando produtos com média de avaliações maior ou igual a 4.5
produtos_bem_avaliados = df[df['Média Avaliações'] >= 4.5]

# Ordenando os produtos pela média das avaliações em ordem decrescente
df_ordenado = df.sort_values('Média Avaliações', ascending=False)

print("DataFrame com a média das avaliações:\n", df)
print("\nProdutos com média de avaliações >= 4.5:\n", produtos_bem_avaliados)
print("\nDataFrame ordenado pela média das avaliações (decrescente):\n", df_ordenado)
