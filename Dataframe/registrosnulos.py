import pandas as pd


data_clientes = 'C:/xampp/htdocs/Python/data/clientesnulos.xlsx'

df = pd.read_excel(data_clientes)


# mostrara los registros con false sin hay datos y como true si esta nulo
# df = df.isna()

# elimna registros que tengan campos nulos
# df = df.dropna()

# a los valores nulos se les asiganra un valor
df = df.fillna(0)

print(df)
