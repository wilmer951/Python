import pandas as pd

from sqlalchemy import create_engine

# Parámetros de conexión
server = '192.168.0.16'
database = 'basededatos'
username = 'adm'
password = 'Colombia2024'
driver = 'ODBC Driver 17 for SQL Server'  # Esto puede variar según tu configuración
#driver = 'ODBC+Driver+17+for+SQL+Server'  # Nombre del controlador 



# Cadena de conexión


try:
    # Conexión
    engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}')
    connection = engine.connect()
    print('Conexión exitosa')
    
#****************************************************************************

   

    archivo = 'C:/xampp/htdocs/Python/data/estudiantes.xlsx'
    df=pd.read_excel(archivo)
    df=df[['Nombre','Materia']]

    print(df)


   

    #se inserta en base de datos.
    df.to_sql('tbprueba', con=engine, if_exists='append', index=False)

    print("Inserccion exitosa")

        
    
#****************************************************************************
    # Cerrar conexión
    engine.dispose()

except Exception as e:
    print("Error:", type(e).__name__, "-", e)

  