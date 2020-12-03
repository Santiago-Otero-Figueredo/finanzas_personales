from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class Usuario(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con ese correo.'
        }
    )

    telefono_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="El numero debe tener entre 9 y 15 caracteres."
    )
    telefono = models.CharField(validators=[telefono_regex], max_length=17, blank=True)
    fecha_nacimiento = models.DateTimeField(blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name+" "+self.last_name
    

    def obtener_movimientos_anio_mes(self, anio, mes, tipo):
        movimientos = self.movimiento_usuario.filter(tipo__nombre=tipo, fecha_inscripcion__year=anio, fecha_inscripcion__month=mes)
        return movimientos
    
    def obtener_suma_cantidad_movimientos_anio_mes(self, anio, mes, tipo):
        from django.db.models import Sum
        return self.obtener_movimientos_anio_mes(anio, mes, tipo).aggregate(total=Sum('cantidad'))
    
    def obtener_suma_cantidad_movimientos(self):
        from django.db.models import Sum
        ingresos = self.movimiento_usuario.filter(tipo__nombre='Ingreso').aggregate(total=Sum('cantidad'))
        gastos = self.movimiento_usuario.filter(tipo__nombre='Gasto').aggregate(total=Sum('cantidad'))

        lista_retorno = [ {
            "category": "ingresos",
            "cantidad": float(ingresos['total'])},
            {"grafica_tortas": "gastos",
            "cantidad": float(gastos['total'])}
        ]
        return lista_retorno
    
    def obtener_rendimientos_rango_fecha(self, fecha_inicio, fecha_fin):
        anio_inicio = fecha_inicio.year
        mes_inicio = fecha_inicio.month
        
        
        mes_fin = fecha_fin.month
        
        lista_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        lista_retorno = []
        while mes_inicio <= mes_fin:
            ingresos = self.obtener_suma_cantidad_movimientos_anio_mes(anio=anio_inicio, mes=mes_inicio, tipo='Ingreso')
            gastos = self.obtener_suma_cantidad_movimientos_anio_mes(anio=anio_inicio, mes=mes_inicio, tipo='Gasto')
            lista_retorno.append({
                'category': lista_meses[mes_inicio-1],
                'ingresos': int(ingresos['total']/1000),
                'gastos': int(gastos['total']/1000),
            })           
            mes_inicio += 1
        for l in lista_retorno:
            print(l)  

        return lista_retorno
    
    
'''
    [
    {
        category: 'Place #1',
        ingresos: 40,
        gastos: 55,        
    },
    {
        category: 'Place #2',
        ingresos: 30,
        gastos: 78,       
    },
    {
        category: 'Place #3',
        ingresos: 27,
        gastos: 40,        
    },
    {
        category: 'Place #4',
        ingresos: 50,
        gastos: 33,        
    }
]'''