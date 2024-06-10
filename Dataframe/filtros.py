import pandas as pd

data_estudiantes = 'C:/xampp/htdocs/Python/data/notasestudiantes.xlsx'

df = pd.read_excel(data_estudiantes)

# Calculate the average grade for each student
df['Promedio'] = (df['Nota1'] + df['Nota2'] + df['Nota3']) / 3

print("Todos los estudiantes:")
print(df)

# Filter out the students who passed (Promedio > 3)
df_aprobados = df[(df['Promedio'] >= 3) & (df['Edad'] > 18)]

print('\nEstudiantes aprobados:')
print(df_aprobados)
