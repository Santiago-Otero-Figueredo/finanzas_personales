# Modulos Django
from django import forms

# Modulos de plugin externos

# Modulos de otras apps

# Modulos internos de la app
from .models import Movimiento

class RegistrarMovimiento(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ('tipo', 'cantidad', 'descripcion')
