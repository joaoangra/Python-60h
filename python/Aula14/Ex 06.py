import pandas as pd
import os

base = r'C:\Users\Instrutor\Desktop\Python-60h\python\Aula14\Arquivos'
src = os.path.join(base, 'vendas.xlsx')
dst = os.path.join(base, 'vendas_comissao.xlsx')

os.makedirs(base, exist_ok=True)

if os.path.exists(src):
    vendas = pd.read_excel(src)
else:
    vendas = pd.DataFrame(columns=['ID', 'Data', 'Valor', 'Comissao'])
    vendas.to_excel(src, index=False)
    print("Arquivo de origem não encontrado. Um novo arquivo vazio foi criado:", src)

# detecta coluna de comissão (suporta variações de nome)
com_col = next((c for c in vendas.columns if 'comiss' in c.lower() or 'comissao' in c.lower()), None)

if com_col is None:
    # cria coluna se não existir
    com_col = 'Comissao'
    vendas[com_col] = pd.Series(dtype=float)

# garante numérico
vendas[com_col] = pd.to_numeric(vendas[com_col], errors='coerce')

mean_val = vendas[com_col].mean(skipna=True)
if pd.isna(mean_val):
    mean_val = 0.0
    print("A coluna de comissão está vazia; valores nulos serão preenchidos com 0.0")
else:
    mean_val = round(mean_val, 2)

vendas[com_col].fillna(mean_val, inplace=True)
vendas[com_col] = vendas[com_col].round(2)

vendas.to_excel(dst, index=False)
print(f"Valores nulos em '{com_col}' substituídos pela média ({mean_val}). Resultado salvo em: {dst}")
print(vendas.head(5))
