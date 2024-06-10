import pandas as pd

data_clientes = 'C:/xampp/htdocs/Python/data/resumen.xlsx'


df = pd.read_excel(data_clientes)

df = df.T
# df = df.transpose()

print(df)
