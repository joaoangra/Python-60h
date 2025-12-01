import pandas as pd
import os

# Nome do arquivo de dados
arquivo = 'C:\Users\Instrutor\Desktop\Python-60h\python\Aula14\Demonstração\Produtos_Cadastro.xlsx'

# Verifica se o arquivo já existe
if os.path.exists(arquivo):
    produtos = pd.read_excel(arquivo)
    print("Arquivo Existente Carregado com Sucesso! \n", produtos)
else:
    produtos = pd.DataFrame(columns=['ID', 'Nome', 'Preço', 'Estoque'])
    print("Nenhum arquivo encontrado. Um novo foi criado.\n", produtos)

    produtos.to_excel(arquivo, index=False)
    print("Arquivo Criado com Sucesso! \n", produtos)
# Adiciona um novo produto
novo_produto = {
    'ID': [1],
    'Nome': ['Caderno'],
    'Preço': [12.00],
    'Estoque': [100]
}
novo_df = pd.DataFrame(novo_produto)
produtos = pd.concat([produtos, novo_df], ignore_index=True)
produtos.to_excel(arquivo, index=False)
print("Novo produto adicionado e arquivo atualizado:\n", produtos)
# Atualiza o estoque de um produto existente
produtos.to_excel(arquivo, index=False)
print("Estoque atualizado e arquivo salvo:\n", produtos)
produtos.loc[produtos['ID'] == 1, 'Estoque'] = 50
