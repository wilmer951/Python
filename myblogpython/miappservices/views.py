from django.shortcuts import render
from .models import Services

# Create your views here.


def Services_list(request):

    servicios = Services.objects.all()

    return render(request, "miappservices/services.html", {'servicios': servicios})
