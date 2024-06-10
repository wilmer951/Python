
import pandas as pd
import mysql.connector

try:

    # CONSULTAR ARCHIVO EXCEL A IMPORTAR
    archivo = 'C:/xampp/htdocs/Python/data/estudiantes.xlsx'
    df = pd.read_excel(archivo)

    # CONEXION A BASE DE DATOS
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="basededatos")
    print("conexion exitosa")


# IMPORTACION DE DATOS DE EXCEL A MYSQL
    cursor = conexion.cursor()

    for indice_fila, fila in df.iterrows():

        query = "INSERT INTO tbprueba (Nombre, Materia) VALUES (%s, %s)"
        valores = (fila['Nombre'], fila['Materia'])
        cursor.execute(query, valores)
        print("Inserción exitosa para la fila:", indice_fila)

# envio de datos.
    conexion.commit()

# Cierra la conexión
    conexion.close()


except Exception as e:
    print("Error de conexion:", type(e).__name__, "-", e)
