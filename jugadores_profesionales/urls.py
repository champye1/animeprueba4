from django.urls import path
from . import views

app_name = 'jugadores_profesionales'

urlpatterns = [
    path('', views.lista_jugadores, name='lista_jugadores'),
] 