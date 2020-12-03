from django.urls import path

from .views import CalculadoraIntereses, Analitica

app_name = 'funcionalidades'

urlpatterns = [
    path('caluladora-intereses', CalculadoraIntereses.as_view(), name='calculadora_intereses'),
    path('analitica/', Analitica.as_view(), name='analitica'),

]