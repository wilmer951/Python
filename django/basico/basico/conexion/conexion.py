import sqlalchemy as sa
from sqlalchemy import create_engine


class Çlassonexion:

    def conectar(self):

        # Datos de conexión a la base de datos
        nombre_basededatos = 'basededatos'
        usuario = 'root'
        password = ''

        engine = create_engine(
            f'mysql+mysqlconnector://{usuario}:{password}@localhost/{nombre_basededatos}')
        connection = engine.connect()

        return connection
