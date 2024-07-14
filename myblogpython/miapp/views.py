from django.shortcuts import render


# Create your views here.


def Home(request):

    return render(request, "miapp/home.html")


def ContactUs(request):

    return render(request, "miapp/contactus.html")


def Blog(request):

    return render(request, "miapp/blog.html")


def About(request):

    return render(request, "miapp/about.html")
