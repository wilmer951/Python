import pandas as pd


try:
    ventas = [['Enero','30500','22000'],
          ['Febrero','35600','23400'],
          ['Marzo','28300','18100'],
          ['Abril','33900','20700']]

    df = pd.DataFrame(ventas, columns=['Mes', 'Ventas', 'Gastos'])
  

  
    df['Ventas'] = pd.to_numeric(df['Ventas'])
    df['Gastos'] = pd.to_numeric(df['Gastos'])

    # Agregamos una nueva columna 'Ganancia' calculada como la diferencia entre 'Venta' y 'Gastos'
    df['Ganancia'] = df['Ventas'] - df['Gastos']

    sumatotal=df['Ganancia'].sum()

    print(df)

    
    print('Suma total',sumatotal)





    df_filtrado = df.loc[df['Mes'].isin(['Enero', 'Marzo'])]

    print(df_filtrado)

    sumatotal=df_filtrado['Ganancia'].sum()

    print('Suma total',sumatotal)




except Exception as e:
    print("Error:", type(e).__name__, "-", e)


