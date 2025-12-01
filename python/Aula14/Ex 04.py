import pandas as pd
import os

base = r'C:\Users\Instrutor\Desktop\Python-60h\python\Aula14\Arquivos'
src = os.path.join(base, 'estoque.xlsx')
dst = os.path.join(base, 'estoque_atualizado.xlsx')

os.makedirs(base, exist_ok=True)

if os.path.exists(src):
    estoque = pd.read_excel(src)
else:
    estoque = pd.DataFrame(columns=['ID', 'Nome', 'Preço', 'Quantidade'])
    estoque.to_excel(src, index=False)
    print("Arquivo de origem não encontrado. Um novo arquivo vazio foi criado:", src)

# identifica colunas de preço e quantidade (suporta variações de nome)
price_col = next((c for c in estoque.columns if 'pre' in c.lower()), None)
qty_col = next((c for c in estoque.columns if 'quant' in c.lower() or 'qtd' in c.lower()), None)

if price_col is None or qty_col is None:
    print("Colunas 'Preço' ou 'Quantidade' não encontradas. Ajuste o arquivo para incluir essas colunas.")
else:
    # garante que sejam numéricas
    estoque[price_col] = pd.to_numeric(estoque[price_col], errors='coerce').fillna(0.0)
    estoque[qty_col] = pd.to_numeric(estoque[qty_col], errors='coerce').fillna(0.0)

    # calcula ValorTotal
    estoque['ValorTotal'] = (estoque[price_col] * estoque[qty_col]).round(2)

    # salva resultado
    estoque.to_excel(dst, index=False)
    print(f"Arquivo salvo em: {dst} ({len(estoque)} registros)")
    print(estoque.head(5))
