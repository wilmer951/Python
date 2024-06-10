import pandas as pd


data_clientes = 'C:/xampp/htdocs/Python/data/clientes.xlsx'
data_ventas = 'C:/xampp/htdocs/Python/data/ventas.xlsx'


df_clientes = pd.read_excel(data_clientes)
df_ventas = pd.read_excel(data_ventas)

df_clientes = df_clientes.set_index('idclientes')
df_ventas = df_ventas.set_index('Idventascliente')


df_resumen = df_clientes.merge(
    df_ventas, left_on='idclientes', right_on='Idventascliente', how='outer')


print(df_resumen)
