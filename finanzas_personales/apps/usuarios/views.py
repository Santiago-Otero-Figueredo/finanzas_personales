# Modulos Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

# Modulos de plugin externos

# Modulos de otras apps
from finanzas_personales.apps.usuarios.models import Usuario
from finanzas_personales.apps.movimientos.views import RegistrarMovimiento
# Modulos internos de la app
from .forms import FormularioCreacionUsuario, FormularioInicioSesion


class Registro(CreateView):
    model = Usuario
    form_class = FormularioCreacionUsuario
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('usuarios:iniciar_sesion')

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.username = form.instance.email
        usuario.save()
        return super(Registro, self).form_valid(form)

class IniciarSesion(LoginView):    
    template_name = 'usuarios/iniciar_sesion.html'    
    form_class = FormularioInicioSesion
    def dispatch(self, request, *args, **kwargs):        
        if request.user.is_authenticated:            
            return redirect('movimientos:registrar')
        return super(IniciarSesion, self).dispatch(request, *args, **kwargs)

#class PaginaPrincipal(LoginRequiredMixin, TemplateView):
#    template_name = 'usuarios/pagina_principal/index.html'
    
def logout_view(request):
    logout(request)
    return redirect('usuarios:iniciar_sesion')
