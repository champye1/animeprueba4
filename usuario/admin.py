from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_nacimiento')
    search_fields = ('usuario__username', 'biografia')
