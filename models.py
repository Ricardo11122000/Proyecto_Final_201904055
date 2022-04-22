from django.db import models

from tkinter import CASCADE
from django.db import models
from IngresoMascotas.models import Ingresomascotas


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    domicilio = models.TextField()
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
    
class Solicitud(models.Model):
    persona = models.ForeignKey(Persona, blank=True, on_delete=models.CASCADE)
    mascota = models.OneToOneField(Ingresomascotas,blank=False, on_delete=models.CASCADE)
    razones = models.TextField()
