import pandas as pd
import mysql.connector


try:

    archivo = 'C:/xampp/htdocs/Python/PythonDataset/prueba.xlsx'

    df =pd.read_excel(archivo)


    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='basededatos'
    )
    cursor = conexion.cursor()

except Exception as e:
    print("Error Presentado:", e)

# Itera sobre cada fila del DataFrame y realiza la inserción en la base de datos


for indice_fila, fila in df.iterrows():
    try:
        # Suponiendo que tu tabla en MySQL tiene las mismas columnas que el DataFrame
        query = "INSERT INTO tbprueba (Nombre, Materia) VALUES (%s, %s)"
        valores = (fila['Nombre'], fila['Materia'])
        cursor.execute(query, valores)
        print("Inserción exitosa para la fila:", indice_fila)
    except mysql.connector.Error as error:
        print("Error al insertar fila:", indice_fila, "-", error)




# Confirma los cambios en la base de datos
conexion.commit()

# Cierra la conexión
conexion.close()