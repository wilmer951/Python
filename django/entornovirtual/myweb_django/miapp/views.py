from django.shortcuts import render


# Create your views here.


def services(request):

    return render(request, 'miapp/services.html')


def about(request):

    return render(request, 'miapp/about.html')


def blog(request):

    return render(request, 'miapp/blog.html')


def contactus(request):

    return render(request, 'miapp/contactus.html')
