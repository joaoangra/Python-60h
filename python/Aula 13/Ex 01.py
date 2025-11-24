import pandas as pd

dados = {
    'Produto': ['Caderno', 'Lapis', 'Borracha', 'Mochila'],
    'Preço': [12, 2, 85, 3],
    'Vendidos': [40, 150, 10, 80]
}

df = pd.DataFrame(dados)
df['Faturamento'] = df['Preço'] * df['Vendidos']

# Ordena todos os produtos em ordem alfabética
df_ordenado = df.sort_values('Produto')
print("Produtos ordenados alfabeticamente:\n", df_ordenado)

# Filtrar produtos com faturamento maior que 500 e ordenar
produtos_lucrativos = df[df['Faturamento'] > 500].sort_values('Produto')
print("\nProdutos com faturamento maior que 500 (ordenados):\n", produtos_lucrativos)

# Série de faturamento dos produtos lucrativos (index = Produto)
produtos_lucrativos_series = produtos_lucrativos.set_index('Produto')['Faturamento']
print("\nSérie de faturamento dos produtos lucrativos:\n", produtos_lucrativos_series)
