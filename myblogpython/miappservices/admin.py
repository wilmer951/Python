from django.contrib import admin
from .models import Services


# Register your models here.


# Define la clase para personalizar el admin
class ServicesAdmin(admin.ModelAdmin):
    # Campos que deseas mostrar en modo solo lectura
    readonly_fields = ('created', 'updated')
    list_display = ("title", "content", "image", "created", "updated")
    list_filter = ("title",)


admin.site.register(Services, ServicesAdmin)
