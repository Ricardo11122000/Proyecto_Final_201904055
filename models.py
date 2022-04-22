from asyncio.windows_events import NULL
from errno import EADDRNOTAVAIL, EDEADLK
from msilib.schema import Class
from tabnanny import verbose
from tkinter import Widget
from django.db import models
from django.forms import CheckboxSelectMultiple
from django.contrib.auth.models import User


class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}'.format(self.nombre)

class Ingresomascotas(models.Model):
    alimentacion = models.CharField('Alimentacion',max_length=50)
    vacunacion = models.ManyToManyField(Vacuna, blank=True)
    edad = models.BigIntegerField('Edad')
    nombre = models.CharField('Nombre',max_length=50)
    fechaderescate = models.DateTimeField('Fecha de Rescate')
    raza = models.CharField('Raza',max_length=50)
    enfermedadespasadas = models.CharField('Enfermedades',max_length=50)
    foto = models.FileField()
    id = models.CharField('Id',primary_key=True, max_length=4)
    
    def __str__(self):
        return '{}'.format(self.nombre)


class Ingresomascotas_solicitud(models.Model):      
    adoptante = models.OneToOneField(User,blank=False, on_delete=models.CASCADE)
    mascota = models.OneToOneField(Ingresomascotas, on_delete = models.CASCADE)

    def __str__(self):
        return self
