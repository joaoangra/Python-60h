import pandas as pd
import os

base = r'C:\Users\Instrutor\Desktop\Python-60h\python\Aula14\Arquivos'
src = os.path.join(base, 'produtos.xlsx')
dst = os.path.join(base, 'produtos_acima_50.xlsx')

os.makedirs(base, exist_ok=True)

if os.path.exists(src):
    produtos = pd.read_excel(src)
else:
    produtos = pd.DataFrame(columns=['ID', 'Nome', 'Preço', 'Estoque'])
    produtos.to_excel(src, index=False)
    print("Arquivo de origem não encontrado. Um novo arquivo vazio foi criado:", src)

# Assegura que 'Preço' seja numérico antes de filtrar
produtos['Preço'] = pd.to_numeric(produtos.get('Preço', pd.Series(dtype=float)), errors='coerce')

filtrado = produtos[produtos['Preço'] > 50].copy()

filtrado.to_excel(dst, index=False)
print(f"Produtos com preço > R$50 salvos em: {dst} ({len(filtrado)} registros)")
print(filtrado.head(5))
