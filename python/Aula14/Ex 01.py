import pandas as pd
import os

arquivo = r'C:\Users\Instrutor\Desktop\Python-60h\python\Aula14\Arquivos\produtos.xlsx'

os.makedirs(os.path.dirname(arquivo), exist_ok=True)

if os.path.exists(arquivo):
    produtos = pd.read_excel(arquivo)
    print("Arquivo existente carregado com sucesso!")
else:
    produtos = pd.DataFrame(columns=['ID', 'Nome', 'Preço', 'Estoque'])
    produtos.to_excel(arquivo, index=False)
    print("Nenhum arquivo encontrado. Um novo foi criado.")

print(produtos.head(5))
