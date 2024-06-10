import pandas as pd

data_clientes = 'C:/xampp/htdocs/Python/data/resumen.xlsx'


df = pd.read_excel(data_clientes)

df = df.T
df.columns = [''] * len(df.columns)

# df = df.transpose()

print(df)
