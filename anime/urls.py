from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuario import views as usuario_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('gallery/', include('gallery.urls')),
    path('jugadores/', include('jugadores_profesionales.urls')),
    
    # URLs de usuario
    path('registro/', usuario_views.registro, name='registro'),
    path('perfil/', usuario_views.perfil, name='perfil'),
    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', usuario_views.logout_view, name='logout'),
    path('contacto/', include('contacto.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

