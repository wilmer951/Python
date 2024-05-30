import pandas as pd

try:
    archivo = 'C:/xampp/htdocs/Python/Ejerciciospracticos/Ejercicio1/cotizacion.csv'

    df = pd.read_csv(archivo,sep=';')


    df = df['Nombre']

    print(df)
except Exception as e:

    print('error',e)