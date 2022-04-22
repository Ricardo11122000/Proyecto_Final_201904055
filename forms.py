from django import forms
from django.forms import ModelForm
from .models import Ingresomascotas, Vacuna, Ingresomascotas_solicitud
        
class MascotaForm(ModelForm):
    
    class Meta:
        model = Ingresomascotas
        fields = "__all__"
        widgets = { 'vacunacion': forms.CheckboxSelectMultiple(), }
                    
        
class VacunaForm(ModelForm):
    
    class Meta:
        model = Vacuna
        fields = "__all__"

class AdoptForm(ModelForm):
    
    class Meta:
        model = Ingresomascotas_solicitud
        fields = ['adoptante','mascota']

class MascotaFormCliente(ModelForm):
    
    class Meta:
        model = Ingresomascotas
        fields = ['alimentacion', 'nombre', 'vacunacion']
        widgets = { 'vacunacion': forms.CheckboxSelectMultiple(), }