from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from jugadores_profesionales.models import JugadorProfesional  # Ajusta según tu modelo

class Command(BaseCommand):
    help = 'Crear grupo de editores con permisos CRUD para jugadores profesionales'

    def handle(self, *args, **kwargs):
        # Crear grupo de editores
        grupo_editores, created = Group.objects.get_or_create(name='Editores_LoL')

        # Obtener content type del modelo JugadorProfesional
        content_type = ContentType.objects.get_for_model(JugadorProfesional)

        # Asignar permisos CRUD
        permisos = Permission.objects.filter(
            content_type=content_type,
            codename__in=[
                'add_jugadorprofesional',
                'change_jugadorprofesional',
                'delete_jugadorprofesional',
                'view_jugadorprofesional'
            ]
        )
        
        for permiso in permisos:
            grupo_editores.permissions.add(permiso)

        self.stdout.write(
            self.style.SUCCESS(
                'Grupo Editores_LoL creado/actualizado con permisos CRUD para jugadores profesionales'
            )
        ) 