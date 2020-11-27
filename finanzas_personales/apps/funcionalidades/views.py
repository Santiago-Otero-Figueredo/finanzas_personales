# Modulos Django
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Modulos de plugin externos

# Modulos de otras apps

# Modulos internos de la app

# Create your views here.

class CalculadoraIntereses(LoginRequiredMixin, TemplateView):
    template_name = 'funcionalidades/calculadora_intereses.html'
    success_url = reverse_lazy('funcionalidades:calculadora_intereses')

    def get_context_data(self, **kwargs):
        context = super(CalculadoraIntereses, self).get_context_data(**kwargs)
    
        if self.request.GET:
            cantidad = float(self.request.GET['cantidad'])
            cuotas = int(self.request.GET['cuotas'])
            tasa_interes = float(self.request.GET['tasa_interes'])

            context['cuotas_mensuales'] = round((cantidad/cuotas)*tasa_interes, 2)
            
            #print("##{}-{}-{}".format(cuotas_mensuales, cuotas, tasa_interes))
        return context