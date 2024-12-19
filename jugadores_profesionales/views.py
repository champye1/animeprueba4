from django.shortcuts import render
from .models import JugadorProfesional

def lista_jugadores(request):
    jugadores = JugadorProfesional.objects.all()
    return render(request, 'jugadores_profesionales/lista_jugadores.html', {
        'jugadores': jugadores
    })
