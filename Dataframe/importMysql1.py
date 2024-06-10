import pandas as pd


from sqlalchemy import create_engine

# datos conexion base de datos
nombrebasededatos = 'basededatos'
usuario = 'root'
password = ''


try:
 # se muestran solo las columnas seleccioandas.
    engine = create_engine(
        f'mysql+mysqlconnector://{usuario}:{password}@localhost/{nombrebasededatos}')
    connection = engine.connect()
    print('Conexión exitosa')


# ******************************************************************************************************************

 # Extrear informacion de archivo fuente
    archivo = 'C:/xampp/htdocs/Python/data/estudiantes.xlsx'
    df = pd.read_excel(archivo)
    df = df[['Nombre', 'Materia']]

    print(df)

 # se crea la conexion
    engine = create_engine(
        f'mysql+mysqlconnector://{usuario}:{password}@localhost/{nombrebasededatos}')

    # se inserta en base de datos.
    df.to_sql('tbprueba', con=engine, if_exists='append', index=False)

    print("Inserccion exitosa")


# ******************************************************************************************************************

    # Cerrar la conexión explícitamente cuando hayas terminado
    connection.close()
    print('Conexión cerrada')


except Exception as e:
    print("Error:", type(e).__name__, "-", e)
