from django.contrib import admin
from .models import Profile
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProfileResources(resources.ModelResource):
    fields = (
        'user',
        'permiso',
    )
    class Meta:
        model = Profile

@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResources
    list_display = (
        'user',
        'permiso',
    )
