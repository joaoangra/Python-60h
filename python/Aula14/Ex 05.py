import pandas as pd
import os

base = r'C:\Users\Instrutor\Desktop\Python-60h\python\Aula14\Arquivos'
src = os.path.join(base, 'clientes.xlsx')
dst = os.path.join(base, 'clientes_adultos.xlsx')

os.makedirs(base, exist_ok=True)

if os.path.exists(src):
    clientes = pd.read_excel(src)
else:
    clientes = pd.DataFrame(columns=['ID', 'Nome', 'Idade'])
    clientes.to_excel(src, index=False)
    print("Arquivo de origem não encontrado. Um novo arquivo vazio foi criado:", src)

# detecta coluna de idade (suporta 'idade' ou 'age')
age_col = next((c for c in clientes.columns if 'idade' in c.lower() or 'age' in c.lower()), None)

if age_col is None:
    print("Coluna de idade não encontrada. Ajuste o arquivo para incluir uma coluna 'Idade'.")
    clientes.to_excel(dst, index=False)
    print(f"Arquivo salvo em: {dst} (0 registros)")
else:
    clientes[age_col] = pd.to_numeric(clientes[age_col], errors='coerce')
    adultos = clientes[clientes[age_col] >= 18].copy()
    adultos.to_excel(dst, index=False)
    print(f"{len(adultos)} clientes com 18+ salvos em: {dst}")
    print(adultos.head(5))
