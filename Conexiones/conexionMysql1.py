import sqlalchemy as sa
from sqlalchemy import create_engine

# Datos de conexión a la base de datos
nombre_basededatos = 'basededatos'
usuario = 'root'
password = ''


try:
    engine = create_engine(
        f'mysql+mysqlconnector://{usuario}:{password}@localhost/{nombre_basededatos}')
    connection = engine.connect()
    print('Conexión exitosa')

    # Cerrar la conexión explícitamente cuando hayas terminado
    connection.close()
    print('Conexión cerrada')

except Exception as e:
    print("Error:", type(e).__name__, "-", e)
