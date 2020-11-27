# Modulos Django
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

# Modulos de plugin externos
from rest_framework.response import Response
from rest_framework.views import APIView

# Modulos de otras apps

# Modulos internos de la app
from .forms import RegistrarMovimiento
from .models import Movimiento

# Create your views here.
class RegistrarMovimiento(CreateView,LoginRequiredMixin):
    model = Movimiento
    form_class = RegistrarMovimiento
    template_name = 'movimientos/index.html'
    success_url = reverse_lazy('movimientos:registrar')

    def get_context_data(self, **kwargs):
        context = super(RegistrarMovimiento, self).get_context_data(**kwargs)
        movimientos = Movimiento.objects.filter(usuario=self.request.user).order_by('-fecha_inscripcion')
        context['movimientos'] = movimientos
        return context


    