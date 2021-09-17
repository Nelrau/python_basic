import pandas as pd
import openpyxl
dados = pd.read_excel("Vendas.xlsx")
#print(dados)
# panorama faturamento
faturamento = dados['Valor Final'].sum()
print(f'Total: {faturamento}')
#faturamento por loja
loja = dados[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(f'{loja}')
# produto de sucesso
produto= dados[['ID Loja','Produto','Valor Final']].groupby(['ID Loja','Produto']).sum()
print(f'{produto}')