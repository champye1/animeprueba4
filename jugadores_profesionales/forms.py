from django import forms
from .models import Equipo, Campeonato

class JugadorFilterForm(forms.Form):
    ciudad = forms.CharField(required=False)
    equipo = forms.ModelChoiceField(
        queryset=Equipo.objects.all(),
        required=False,
        empty_label="Todos los equipos"
    )
    campeonato = forms.ModelChoiceField(
        queryset=Campeonato.objects.all(),
        required=False,
        empty_label="Todos los campeonatos"
    ) 