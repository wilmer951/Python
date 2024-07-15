from django.urls import path
from . import views


urlpatterns = [
    path('blog/', views.Blog, name='blog'),
    path('blog/category/<int:category_id>',
         views.Category_list, name='category'),
]
