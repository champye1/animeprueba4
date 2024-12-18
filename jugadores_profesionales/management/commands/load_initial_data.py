from django.core.management.base import BaseCommand
from jugadores_profesionales.fixtures.datos_iniciales import *

class Command(BaseCommand):
    help = 'Carga los datos iniciales de equipos y jugadores'

    def handle(self, *args, **kwargs):
        self.stdout.write('Cargando datos iniciales...')
        # El código se ejecutará automáticamente al importar el módulo
        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente')) 