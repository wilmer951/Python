
import pandas as pd

from sqlalchemy import create_engine

# Parámetros de conexión
server = '10.0.0.13,2616'
database = 'ESP_TransactionPay'
username = 'smartadmin'
password = 'smartadmin'
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
    sql_query = "SELECT [CLIENTE],[MEDIOPAGO],[FECHA],[CODIGOTRANSACCION],[CONCEPTO] ,CAST(VALORPAGADO AS int) as VALORPAGADO FROM [ESP_TransactionPay].[dbo].[ESPV_TransaccionesClientes] where year(FECHA)=2024 and month(FECHA)=05and Estado='APROBADO' and MEDIOPAGO = 'DAVIPLATA'"
    df = pd.read_sql(sql_query, engine)

    print(df)

# ****************************************************************************
    # Cerrar conexión
    engine.dispose()

except Exception as e:
    print("Error:", type(e).__name__, "-", e)
