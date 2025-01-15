import requests
import pandas as pd

# Rutas de los archivos
file_origen = 'C:/xampp/htdocs/Python/prueba/origen.xlsx'
file_lista = 'C:/xampp/htdocs/Python/prueba/lista.xlsx'
file_llaveform = 'C:/xampp/htdocs/Python/prueba/llaveform.txt'

# Leer los archivos Excel
df = pd.read_excel(file_origen)
df2 = pd.read_excel(file_lista)


# Leer el archivo de texto usando pandas (suponiendo que la clave está en la primera fila)
df3 = pd.read_csv(file_llaveform, header=None)

# Obtener el valor de la primera fila (la clave que necesitas)


# Obtener las preguntas desde el archivo de origen
pregunta1 = df.loc[0, 'valor']
pregunta2 = df.loc[1, 'valor']
pregunta3 = df.loc[2, 'valor']
pregunta4 = df.loc[3, 'valor']


form_url1 = "https://docs.google.com/forms/u/0/d/e/"
form_url2 = df3.iloc[0, 0]  # Acceder al primer valor de la primera columna
form_url3 = "/formResponse"

# Formulario URL
form_url = f"{form_url1}{form_url2}{form_url3}"

# Iterar sobre las filas del archivo de lista y enviar las respuestas
for index, row in df2.iterrows():
    # Obtener las respuestas de cada fila
    respuesta1 = row['respuesta1']
    respuesta2 = row['respuesta2']
    respuesta3 = row['respuesta3']
    respuesta4 = row['respuesta4']

    # Datos a enviar al formulario (reemplaza 'entry.XXXX' con los identificadores correctos)
    data = {
        pregunta1: respuesta1,
        pregunta2: respuesta2,
        pregunta3: respuesta3,
        pregunta4: respuesta4
    }

    # Enviar los datos al formulario
    response = requests.post(form_url, data=data)

    # Verificar si el envío fue exitoso
    if response.status_code == 200:
        print(
            f"Formulario enviado correctamente para el conjunto de respuestas {index+1}.")
    else:
        print(f"Error al enviar el formulario para el conjunto de respuestas {
              index+1}: {response.status_code}")
