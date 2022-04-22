from django.contrib import admin
from .models import Solicitud
from import_export import resources
from import_export.admin import ImportExportModelAdmin



class SolicitudResources(resources.ModelResource):
    fields = (
        'persona',
        'mascota',
        'razones',
    )
    class Meta:
        model = Solicitud

@admin.register(Solicitud)
class SolicitudAdmin(ImportExportModelAdmin):
    resource_class = SolicitudResources
    list_display = (
        'persona',
        'mascota',
        'razones',
    )
