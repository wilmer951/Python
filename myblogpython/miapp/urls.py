from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('contactus/', views.ContactUs, name='contactus'),
    path('about/', views.About, name='about'),

]
