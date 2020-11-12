from django.urls import path

from .views import RegistrarMovimiento

app_name = 'movimientos'

urlpatterns = [
    path('registrar', view=RegistrarMovimiento.as_view(), name='registrar'),
]