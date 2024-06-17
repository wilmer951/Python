import pandas as pd
from django.http import HttpResponse
from django.template.loader import get_template


def prueba(request):

    archivo = 'C:/xampp/htdocs/Python/data/clientes.xlsx'
    df = pd.read_excel(archivo, skiprows=0)
    df = df.set_index(df.columns[0])

    df_html = df.to_html()

    template = get_template('templatebasic.html')
    respuesta = template.render({'data': df_html})

    return HttpResponse(respuesta)
