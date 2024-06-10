import pandas as pd

data_items = 'C:/xampp/htdocs/Python/data/remplazardatos.xlsx'

df = pd.read_excel(data_items)

print(df)

# remplaza todos los registros que tengan la palabra a remaplzar
# df = df.replace('inactivo', 'debaja')

# remplaza todos los registro solo de la columna indicada.   regex = funcioa como un like de base de datos en caso de que este true consutla conincidenicas
df = df.replace({'estado': r'inactivo'}, {'estado': 'debaja'}, regex=True)


print(df)
