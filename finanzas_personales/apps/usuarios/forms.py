# Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

# Terceros
from tempus_dominus.widgets import DatePicker

# Propias
from finanzas_personales.apps.usuarios.models import Usuario



class FormularioInicioSesion(AuthenticationForm):
    username = forms.EmailField(error_messages={
        'required': 'Este campo es requerido',
        'invalid': 'Introduzca un correo valido'
    })
    #password = forms.PasswordInput(label="Contraseña")

    def __init__(self, *args, **kwargs):
        super(FormularioInicioSesion, self).__init__(*args, **kwargs)
        print(self.fields)
        self.fields['username'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['username'].label = ''
        self.fields['password'].label = ''

    class Meta:
        model = Usuario
        fields = ('username', 'password')
        

class FormularioCreacionUsuario(UserCreationForm):
    fecha_nacimiento = forms.DateField(
        widget=DatePicker(
            options={
                'locale': 'es',
                'format': 'YYYY-MM-DD',
                'minDate': '1900-01-1',
                #'maxDate': '2017-01-20',
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': False,                
            },
        ),
       
    )
    def __init__(self, *args, **kwargs):
        super(FormularioCreacionUsuario, self).__init__(*args, **kwargs)
        for field in self.fields:            
            self.fields[field].help_text = ""
        
        self.fields['first_name'].label = 'Nombres'
        self.fields['last_name'].label = 'Apellidos'
        self.fields['email'].label = 'Correo electrónico'
        self.fields['telefono'].label = 'Teléfono'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmación de contraseña'
    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'email', 'telefono', 'fecha_nacimiento', 'password1', 'password2')
       