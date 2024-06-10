import pandas as pd


try:

    data_clientes = 'C:/xampp/htdocs/Python/data/clientes.xlsx'
    data_ventas = 'C:/xampp/htdocs/Python/data/ventas.xlsx'

    df_clientes = pd.read_excel(data_clientes)
    df_ventas = pd.read_excel(data_ventas)

    df_resumen = df_ventas.merge(
        df_clientes, left_on='Idventascliente', right_on='idclientes', how='outer')

    print(df_resumen)

    df_resumen_pivot = pd.pivot_table(
        data=df_resumen, index='Idventascliente', values='ventas', aggfunc='sum', margins=True)

    print(df_resumen_pivot)

except Exception as e:
    print("Error:", type(e).__name__, "-", e)
