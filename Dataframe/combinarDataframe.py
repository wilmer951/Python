import pandas as pd


data_clientes = 'C:/xampp/htdocs/Python/data/clientes.xlsx'
data_ventas = 'C:/xampp/htdocs/Python/data/ventas.xlsx'


df_clientes = pd.read_excel(data_clientes)
df_ventas = pd.read_excel(data_ventas)

df_clientes = df_clientes.set_index('idclientes')
df_ventas = df_ventas.set_index('Idventascliente')


# en caso de que las columnas no tengan el mismo nombre
df_resumen = df_clientes.merge(
    df_ventas, left_on='idclientes', right_on='Idventascliente', how='outer')


# encaso de qeu las columnas tengan el mismo nombre
# df= pd.merge(df1,df2,on='Nombre',how='right')


print(df_resumen)


# ********************************************************************************************************
# filtrado por filas

# concatena la informacion de los dos csv axix es opcional 0 significa que agregara las fialas.

# df = pd.concat([df1,df2],axis=0)
# Imprime todo el df
#   print(df)

# Imprime el df filrado por mayores de 30.
#   print(df[df.Edad>30])


# ********************************************************************************************************
# filtrado por Columnas


# concatena la informacion de los dos csv axix es opcional 1 significa que agregara las Columnas.

# df4 = pd.concat([df1,df3],axis=1)
# print(df4)


# ********************************************************************************************************
