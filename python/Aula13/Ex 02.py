import pandas as pd

dados = {
    'Item' : ['Pendrive', 'Headset', 'Webcam', 'Tecaldo MK'],
    'Quantidade' : [25, 12, 8, 15],
    'Preço Unitário' : [30, 150, 220, 95]
}

#Calculando o valor total em estoque de cada item
df = pd.DataFrame(dados)
df['Valor Total'] = df['Quantidade'] * df['Preço Unitário']
print("Tabela completa com valor total em estoque:\n", df)

#Calculando a média de preços unítarios
media_preco = df['Preço Unitário'].mean()
print("\nMédia de preços unitários: R$", media_preco)

#Filtrando itens com valor total em estoque maior que 100
dados = df[df['Preço Unitário'] > 100]
print("\nItens com preço unitário maior que 100:\n", dados)
