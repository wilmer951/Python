from django.shortcuts import render
from django.http import HttpRequest
from miapp.models import Producto

# Create your views here.


def FormSearch(request):

    return render(request, "formsearch.html")


def Search(request):

    get_producto = request.GET["nameproduct"]

    if request.GET["nameproduct"]:

        productos = Producto.objects.filter(nombre__icontains=get_producto)

        mensaje = f"Producto a buscar: {get_producto}"

        return render(request, "formsearch.html", {"respuesta": mensaje, "query": productos})

    else:
        mensaje = " Ningun resultado"

        return render(request, "formsearch.html", {"respuesta": mensaje})
