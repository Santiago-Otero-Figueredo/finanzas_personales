# Django
from django.shortcuts import render
from django.views.generic.edit import CreateView

# Terceros

# Propios
from finanzas_personales.apps.usuarios.models import Usuario
from .forms import FormularioCreacionUsuario

class IniciarSesion(CreateView):
    model = Usuario
    form_class = FormularioCreacionUsuario
    template_name = 'usuarios/iniciar_sesion.html'
    
