from django.urls import path
from miapp import views


urlpatterns = [

    path('services/', views.services),
    path('about/', views.about),
    path('blog/', views.blog),
    path('contactus/', views.contactus),



]
