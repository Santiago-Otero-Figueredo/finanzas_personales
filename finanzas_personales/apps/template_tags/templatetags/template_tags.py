from django import template

register = template.Library()

@register.simple_tag(name='restar_dos_numero')
def restar_dos_numero(numero1, numero2):
    return numero1 - numero2