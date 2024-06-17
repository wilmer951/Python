import pandas as pd

datos = {'MES': ['Enero', 'Febrero', 'Marzo', 'Abril'],
         'Ventas': ['30500', '35600', '28300', '33900'],
         'Gastos ': ['22000', '23400', '18100', '18100']}

df = pd.DataFrame(datos)

print(df)
