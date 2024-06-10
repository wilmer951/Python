
import mysql.connector


try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="basededatos")

    print("conexion exitosa")

    conexion.close()

except Exception as e:
    print("Error de conexion:", type(e).__name__, "-", e)
