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
from .models import Movimiento, Tipo

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
        #scroto(self.request)
        return context





def scroto(request):
    import numpy as np
    lista_gastos = [56715,
        454225,
        307300,
        310000,
        910725,
        700725,
        1035725,
        215500,
        205950,
        584926,
        252320,
        222180]

    
    usuario = request.user
    mes = 1
    while mes<=12:
        usuario
        ingreso = Tipo.objects.get(nombre="Ingreso")
        Movimiento.objects.create(usuario=usuario, tipo=ingreso, cantidad=500000, descripcion='Pago Nomina')

        gasto = Tipo.objects.get(nombre="Gasto")
        dia = 1
        aux = lista_gastos[mes-1]
        print("################## MES: ", mes)
        while dia <= 28 and aux>0:
            if dia != 28:
                if aux >= 10000:
                    cantidad = np.random.randint(10000, aux)
                else:
                    cantidad = aux
                aux -= cantidad
            else:
                cantidad = aux
            
            Movimiento.objects.create(usuario=usuario, tipo=gasto, cantidad=cantidad, descripcion='Gasto')

            print("         cantidad: ", cantidad)            
            dia += 1

        mes += 1

    