from django.contrib import admin
from .models import Category, Post

# Register your models here.


class AdminCategory(admin.ModelAdmin):
    # Campos que deseas mostrar en modo solo lectura
    readonly_fields = ('created', 'updated')
    list_display = ("title_category", "description")
    list_filter = ("title_category",)


class AdminPost(admin.ModelAdmin):
    # Campos que deseas mostrar en modo solo lectura
    readonly_fields = ('created', 'updated')
    list_display = ("title_post", "contenet", "image",
                    "autor", "created", "updated")
    list_filter = ("title_post",)


admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)
