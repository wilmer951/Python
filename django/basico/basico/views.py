import pandas as pd
from django.http import HttpResponse

from django.shortcuts import render

from .conexion.conexion import Çlassonexion


def dataframe(request):

    archivo = 'C:/xampp/htdocs/Python/data/clientes.xlsx'
    df = pd.read_excel(archivo, skiprows=0)
    df = df.set_index(df.columns[0])
    df_html = df.to_html()

    return render(request, 'pagedataframe.html', {'data': df_html})


def home(request):

    return render(request, 'home.html')


def db(request):
    try:
        # Crear instancia de Conexion
        mi_conexion = Çlassonexion()

        # Llamar al método conectar para obtener la conexión
        conexion = mi_conexion.conectar()
        resultado = "Conexión exitosa."

        sql_query = 'SELECT * FROM tbprueba'
        df = pd.read_sql(sql_query, conexion)
        conexion.close()
        df_html = df.to_html(index=False)

        # Cerrar la conexión cuando haya terminado
        resulconexion = 'ok'
    except Exception as e:
        resulconexion = f"No se pudo conectar: {str(e)}"
        df_html = None

    return render(request, 'db.html', {'resulconexion': resulconexion, 'resultado': df_html})
