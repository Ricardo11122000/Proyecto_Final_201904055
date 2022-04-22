from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProyectoFinal2App.urls')),
    path('', include('RegistroUsuario.urls')),
    path('', include('Reportes.urls')),
    path('captcha/', include('captcha.urls')),
]