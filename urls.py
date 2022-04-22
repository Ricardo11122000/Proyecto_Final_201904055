from django import views
from django.urls import path
from .views import RegistroUsuario, cerrar_sesion, acceder, profile, profile_admin

urlpatterns = [
    
    path('registrousuario/',RegistroUsuario.as_view(), name="RegistroUsuario"),
    path('cerrar_sesion',cerrar_sesion, name="cerrar_sesion"),
    path('acceder/',acceder, name="acceder"),
    path('profile/',profile, name="profile"),
    path('profile_admin/<id>', profile_admin, name='profile_admin'),
]
