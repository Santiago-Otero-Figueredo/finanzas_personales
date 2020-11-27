# Modulos Django
from django import forms

# Modulos de plugin externos

# Modulos de otras apps

# Modulos internos de la app
from .models import Movimiento

class RegistrarMovimiento(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegistrarMovimiento, self).__init__(*args, **kwargs)
        self.fields['cantidad'].label = ''
        self.fields['descripcion'].label = ''
        self.fields['cantidad'].widget.attrs['placeholder'] = 'Cantidad'
        self.fields['descripcion'].widget.attrs['placeholder'] = 'Descripcion'

    class Meta:
        model = Movimiento
        fields = ('tipo', 'cantidad', 'descripcion')

