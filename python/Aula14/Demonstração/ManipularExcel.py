import pandas as pd
import os

arquivo = 'Produtos_Cadastro.xlsx'

if os.path.exists(arquivo):
    produtos = pd.read_excel(arquivo)
    print("Arquivo Existente Carregado com Sucesso! \n", produtos)
else:
    dados = {
        'Produto': ['Caderno', 'Lapis', 'Borracha', 'Mochila'],
        'Preço': [12, 2, 85, 3],
        'Vendidos': [40, 150, 10, 80]
    }
    produtos = pd.DataFrame(dados)
    produtos.to_excel(arquivo, index=False)
    print("Arquivo Criado com Sucesso! \n", produtos)