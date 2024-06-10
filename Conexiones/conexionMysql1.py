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


# ****************************************************************************************************************************************************************
# Datos de conexión a la base de datos  2

    import mysql.connector

    # Establecer la conexión
    conexion = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        passwd="tu_contraseña",
        database="nombre_de_la_base_de_datos")
    print("conexion exitosa")

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM mi_tabla")

    # Obtener todos los registros
    registros = cursor.fetchall()


# extreaer informacion
    for registro in registros:
        print(registro)

        columnas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(registros, columns=columnas)
        print(df)


# Cerrar la conexión explícitamente cuando hayas terminado
    conexion.close()


except Exception as e:
    print("Error de conexion:", type(e).__name__, "-", e)
