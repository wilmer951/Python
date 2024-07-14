from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('contactus/', views.ContactUs, name='contactus'),
    path('blog/', views.Blog, name='blog'),
    path('about/', views.About, name='about'),

]
