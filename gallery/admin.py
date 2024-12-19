from django.contrib import admin
from .models import Galeria

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'fecha_estreno')
    search_fields = ('title', 'author')


