from django.urls import path

from .views import CalculadoraIntereses

app_name = 'funcionalidades'

urlpatterns = [
    path('caluladora-intereses', CalculadoraIntereses.as_view(), name='calculadora_intereses'),

]