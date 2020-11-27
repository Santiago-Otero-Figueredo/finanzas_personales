# Modulos Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django_currentuser.db.models import CurrentUserField
  
# Modulos de plugin externos
from decimal import Decimal
# Modulos de otras apps

# Modulos internos de la app

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=15, verbose_name="Nombre movimiento", blank=False, null=False)

    class Meta:
        ordering = ('nombre',)
    
    def __str__(self):
        return self.nombre

class Movimiento(models.Model):
    usuario = CurrentUserField()
    tipo = models.ForeignKey(Tipo, verbose_name="Tipo movimiento", related_name="movimiento_tipo", on_delete=models.CASCADE, blank=False, null=False)
    cantidad = models.DecimalField(decimal_places=2, max_digits=12, validators=[MaxValueValidator(Decimal('100000000000.00')), MinValueValidator(Decimal('0.00'))])
    descripcion = models.CharField(max_length=30, verbose_name="Descripción", blank=False, null=False)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def obtener_suma_movimientos(id_usuario, tipo):
        from django.db.models import Sum
        movimiento = Movimiento.objects.filter(tipo__nombre=tipo, usuario__pk=id_usuario).aggregate(total=Sum('cantidad'))
        
        print(movimiento)
        if  movimiento['total']:
            return movimiento['total']
        else:
            return 0