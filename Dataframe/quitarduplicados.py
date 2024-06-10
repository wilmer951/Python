import pandas as pd


data_clientes = 'C:/xampp/htdocs/Python/data/clientesduplicados.xlsx'

df = pd.read_excel(data_clientes)


# borar las filas que estan completamente duplicadas
# df = df.drop_duplicates()


# borar las filas que estan completamente duplicadas dentro de una columna
df = df.drop_duplicates(subset=['Nombre', 'area'])

print(df)
