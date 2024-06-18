import pandas as pd
from django.http import HttpResponse

from django.shortcuts import render


def dataframe(request):

    archivo = 'C:/xampp/htdocs/Python/data/clientes.xlsx'
    df = pd.read_excel(archivo, skiprows=0)
    df = df.set_index(df.columns[0])
    df_html = df.to_html()

    return render(request, 'pagedataframe.html', {'data': df_html})


def home(request):

    return render(request, 'home.html')
