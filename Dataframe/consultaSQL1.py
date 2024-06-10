
import pandas as pd

from sqlalchemy import create_engine

# Parámetros de conexión
server = '192.168.0.16'
database = 'basededatos'
username = 'adm'
password = 'Colombia2024'
# Esto puede variar según tu configuración
driver = 'ODBC Driver 17 for SQL Server'
# driver = 'ODBC+Driver+17+for+SQL+Server'  # Nombre del controlador


# Cadena de conexión


try:

    # Conexión
    engine = create_engine(
        f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}')
    connection = engine.connect()
    print('Conexión exitosa')


# ****************************************************************************

    sql_query = 'SELECT * FROM tbprueba'
    df = pd.read_sql(sql_query, engine)

    print(df)


# ****************************************************************************
    # Cerrar conexión
    engine.dispose()

except Exception as e:
    print("Error:", type(e).__name__, "-", e)
