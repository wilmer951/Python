import pandas as pd


data_estudiantes = 'C:/xampp/htdocs/Python/data/notasestudiantes.xlsx'

df = pd.read_excel(data_estudiantes)

intervalos = [0, 17, 29, 60]
etiquetas = ['nino', 'joven', 'adulto']

df['grupo'] = pd.cut(df['Edad'], bins=intervalos, labels=etiquetas)
print(df)


print(df)
