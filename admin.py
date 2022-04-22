from django.contrib import admin
from .models import Ingresomascotas, Ingresomascotas_solicitud
from import_export import resources
from import_export.admin import ImportExportModelAdmin





class IngresomascotasResources(resources.ModelResource):
    fields = (
        'alimentacion',
        'edad',
        'nombre',
        'fechaderescate',
        'raza',
        'enfermedadespasadas',
        'id',
    )
    class Meta:
        model = Ingresomascotas

@admin.register(Ingresomascotas)
class IngresomascotasAdmin(ImportExportModelAdmin):
    resource_class = IngresomascotasResources
    list_display = (
        'alimentacion',
        'edad',
        'nombre',
        'fechaderescate',
        'raza',
        'enfermedadespasadas',
        'id',
    )

class Ingresomascotas_solicitudResources(resources.ModelResource):
    fields = (
        'adoptante',
        'mascota',
    )
    class Meta:
        model = Ingresomascotas_solicitud

@admin.register(Ingresomascotas_solicitud)
class Ingresomascotas_solicitudAdmin(ImportExportModelAdmin):
    resource_class = Ingresomascotas_solicitudResources
    list_display = (
        'adoptante',
        'mascota',
    )
