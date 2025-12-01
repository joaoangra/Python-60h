import pandas as pd
import os

base = r'C:\Users\Instrutor\Desktop\Python-60h\python\Aula14\Arquivos'
src = os.path.join(base, 'transacoes.xlsx')
dst = os.path.join(base, 'resumo_transacoes.xlsx')

os.makedirs(base, exist_ok=True)

if os.path.exists(src):
    trans = pd.read_excel(src)
else:
    trans = pd.DataFrame(columns=['ID', 'Cliente', 'Valor', 'Data'])
    trans.to_excel(src, index=False)
    print("Arquivo de origem não encontrado. Um novo arquivo vazio foi criado:", src)

# tenta identificar a coluna de cliente (suporta 'cliente' ou 'client' ou 'nome')
cliente_col = next((c for c in trans.columns if 'cliente' in c.lower() or 'client' in c.lower() or 'nome' in c.lower()), None)

if cliente_col is None:
    if len(trans.columns) == 0:
        resumo = pd.DataFrame(columns=['Cliente', 'TotalTransacoes'])
    else:
        cliente_col = trans.columns[0]
        resumo = trans.groupby(cliente_col).size().reset_index(name='TotalTransacoes')
else:
    resumo = trans.groupby(cliente_col).size().reset_index(name='TotalTransacoes')

resumo.to_excel(dst, index=False)
print(f"Resumo de transações por cliente salvo em: {dst} ({len(resumo)} registros)")
print(resumo.head(5))
