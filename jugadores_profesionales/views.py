from django.shortcuts import render
from .models import JugadorProfesional
from .forms import JugadorFilterForm
from django.core.paginator import Paginator

def lista_jugadores(request):
    form = JugadorFilterForm(request.GET)
    jugadores = JugadorProfesional.objects.all()

    if form.is_valid():
        if form.cleaned_data['ciudad']:
            jugadores = jugadores.filter(
                ciudad_nacimiento__icontains=form.cleaned_data['ciudad']
            )
        if form.cleaned_data['equipo']:
            jugadores = jugadores.filter(equipo=form.cleaned_data['equipo'])
        if form.cleaned_data['campeonato']:
            jugadores = jugadores.filter(campeonato=form.cleaned_data['campeonato'])

    # Configurar la paginación
    paginator = Paginator(jugadores, 6)  # 6 jugadores por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'jugadores': page_obj
    }
    return render(request, 'jugadores_profesionales/lista_jugadores.html', context)
