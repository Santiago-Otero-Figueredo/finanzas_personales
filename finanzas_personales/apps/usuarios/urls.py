from django.urls import path

from .views import prueba

app_name = 'usuarios'

urlpatterns = [
    path('prueba/', prueba, name='prueba')
    #nada importante
]