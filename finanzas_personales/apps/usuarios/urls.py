from django.urls import path

from .views import Registro, IniciarSesion, PaginaPrincipal, logout_view

app_name = 'usuarios'

urlpatterns = [
    path('registro/', Registro.as_view(), name='registro'),
    path('iniciar_sesion/', IniciarSesion.as_view(), name='iniciar_sesion'),
    path('pagina_principal/', PaginaPrincipal.as_view(), name='pagina_principal'),
    path('cerrar_sesion/', logout_view, name='cerrar_sesion'),
]