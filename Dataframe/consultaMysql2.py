
import pandas as pd
import mysql.connector


try:
    # Establecer la conexión
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="basededatos")
    print("conexion exitosa")

    # realiza conexión a base de datos
    cursor = conexion.cursor()
    # consulta la tabla
    cursor.execute("SELECT * FROM tbprueba")

    # Obtener todos los registros
    registros = cursor.fetchall()

    # ***********************************************************

    # Obtener todos los registros

    for registro in registros:

        columnas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(registros, columns=columnas)

    print(df)

    # ******************************************************************

    # cierra coenxion
    conexion.close()


except Exception as e:
    print("Error de conexion:", type(e).__name__, "-", e)
