import pandas as pd
import os

base = r'C:\Users\Instrutor\Desktop\Python-60h\python\Aula14\Arquivos'
src = os.path.join(base, 'funcionarios.xlsx')
dst = os.path.join(base, 'vendas_atualizado.xlsx')

os.makedirs(base, exist_ok=True)

if os.path.exists(src):
    funcionarios = pd.read_excel(src)
else:
    funcionarios = pd.DataFrame(columns=['ID', 'Nome', 'Setor', 'Salário'])
    funcionarios.to_excel(src, index=False)
    print("Arquivo de origem não encontrado. Um novo arquivo vazio foi criado:", src)

# identifica coluna de setor e de salário (suporta variações de nome)
sector_col = next((c for c in funcionarios.columns if 'set' in c.lower()), None)
salary_col = next((c for c in funcionarios.columns if 'sal' in c.lower()), None)

if sector_col is None:
    print("Coluna de setor não encontrada. Ajuste o arquivo para incluir uma coluna 'Setor'.")
else:
    # filtra funcionários do setor 'Vendas' (case-insensitive)
    mask_vendas = funcionarios[sector_col].astype(str).str.strip().str.lower() == 'vendas'
    vendas = funcionarios.loc[mask_vendas].copy()

    if vendas.empty:
        print("Nenhum funcionário encontrado no setor 'Vendas'.")
        # salva um arquivo vazio com mesmas colunas para manter consistência
        vendas.to_excel(dst, index=False)
        print(f"Arquivo salvo em: {dst} (0 registros)")
    else:
        # garante coluna de salário e converte para numérico
        if salary_col is None:
            # cria coluna de salário se não existir
            salary_col = 'Salário'
            vendas[salary_col] = pd.Series(dtype=float)

        vendas[salary_col] = pd.to_numeric(vendas[salary_col], errors='coerce').fillna(0.0)

        # aumenta salário em 15%
        vendas[salary_col] = (vendas[salary_col] * 1.15).round(2)

        vendas.to_excel(dst, index=False)
        print(f"{len(vendas)} funcionários do setor 'Vendas' tiveram salário aumentado em 15% e salvos em: {dst}")
        print(vendas.head(5))
