# apply permite aplicar una funcion a una fila o columna con el metodo lamba

import pandas as pd

data_estudiantes = 'C:/xampp/htdocs/Python/data/notasestudiantes.xlsx'

df = pd.read_excel(data_estudiantes)
df['promedio'] = (df['Nota1']+df['Nota2']+df['Nota3'])/3

df['estado'] = df['promedio'].apply(
    lambda x: 'aprobado' if x >= 3 else 'reprobado')


print(df)


# applymap permite aplicar cuniones a todos los registros que concidan


df = df.applymap(lambda x: x.upper() if type(x) == str else x)
# df = df.applymap(lambda x: x.upper() if isinstance(x, str) else x)

print(df)
