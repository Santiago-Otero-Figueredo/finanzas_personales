from django.urls import path

from .views import IniciarSesion

app_name = 'usuarios'

urlpatterns = [
    path('iniciar_sesion/', IniciarSesion.as_view(), name='iniciar_sesion')    
]