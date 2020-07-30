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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name+" "+self.last_name
    