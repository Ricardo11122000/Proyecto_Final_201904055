from django import forms
from django.db import models
from .models import Persona, Solicitud
from django import forms


class SolicitudForm(forms.ModelForm):
    
    class Meta:
        model = Solicitud
        fields = ['mascota', 'razones',]
        labels = {'mascota': 'Mascota', 'razones':'Razones para adoptar'}
        
class PersonaForm(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 
                  'edad', 'email', 'domicilio']
        labels = {'nombre': 'Nombre',
                  'apellido': 'Apellido',
                  'edad': 'Edad',
                  'email': 'Email',
                  'domicilio': 'Domicilio'}
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'apellido': forms.TextInput(attrs={'class': 'form-control'}),
                   'edad': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
                   }