import pandas as pd

dados = {
    'Produto' : ['Mouse', 'Teclado', 'Monitor', 'Cabo HDMI'],
    'Preço' : [50, 120, 900, 35],
    'Estoque' : [20, 15, 8, 50]
}

df = pd.DataFrame(dados)

#Criar nova coluna
df['Total'] = df['Preço'] * df['Estoque']

#Filtrar produtos com preço maior que 100
produtos_caro = df[ df['Preço'] > 100 ]
print("Produtos com preço maior que 100:\n", produtos_caro)

#Salvar em csv
produtos_caro.to_csv('preço_loja.csv', index=False)


print("tabela completa:\n", df)
print("\nArquivo 'preço_loja.csv' criado com sucesso!")