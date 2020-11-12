from django import template

register = template.Library()

@register.filter(name='calcular_diferencia')
def calcular_diferencia(id_usuario):
    from finanzas_personales.apps.movimientos.models import Movimiento
    gastos = Movimiento.obtener_suma_movimientos(id_usuario, 'Gasto')
    ingresos = Movimiento.obtener_suma_movimientos(id_usuario, 'Ingreso')
    return ingresos-gastos