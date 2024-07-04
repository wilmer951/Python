from django.contrib import admin

from miapp.models import Producto

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "modelo", "precio")
    search_fields = ("nombre", "descripcion", "modelo", "precio")
    list_filter = ("descripcion",)


admin.site.register(Producto, ProductoAdmin)
