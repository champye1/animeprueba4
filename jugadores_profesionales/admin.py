from django.contrib import admin
from .models import Equipo, Campeonato, JugadorProfesional

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')
    search_fields = ('nombre', 'pais')

@admin.register(Campeonato)
class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region')
    search_fields = ('nombre', 'region')

@admin.register(JugadorProfesional)
class JugadorProfesionalAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'nombre', 'equipo', 'rol']
    search_fields = ['nickname', 'nombre', 'equipo']
    list_filter = ['equipo', 'rol']
