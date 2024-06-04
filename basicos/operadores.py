
import pandas as pd


from sqlalchemy import create_engine

# datos conexion base de datos
nombrebasededatos = 'basededatos'
usuario = 'root'
password = ''

try:

    engine = create_engine(
        f'mysql+mysqlconnector://{usuario}:{password}@localhost/{nombrebasededatos}')
    connection = engine.connect()
    print('Conexión exitosa')


# ******************************************************************************************************************

    sql_query = 'SELECT * FROM tbprueba'
    df = pd.read_sql(sql_query, engine)

    df = df[(df['Materia'] == 'sociales') & (
        df['Edad'] > 19)][['Nombre', 'Materia']]
    print(df)


# ******************************************************************************************************************

    # Cerrar la conexión explícitamente cuando hayas terminado
    connection.close()
    print('Conexión cerrada')

except Exception as e:
    print("Error:", type(e).__name__, "-", e)
