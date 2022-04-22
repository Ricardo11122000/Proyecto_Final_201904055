from re import template
from django.urls import path, reverse_lazy
from ProyectoFinal2App import views
from django.conf import settings
from django.urls import re_path as url, reverse
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from adopcion.views import  *
#SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('mascotasactuales/', views.MascotasActuales, name="MascotasActuales"),
    path('solicitudadopcion/', Solicitudes, name="solicitud_listar"),
    path('solicitudnueva/', SolicitudCreate.as_view(), name="solicitud_crear"),
    path('ingresomascotas/', views.IngresoMascotas, name="IngresoMascotas"),
    path('ingresovacuna/', views.Ingresovacuna, name="IngresoVacuna"),
    path('asignarmascota/', views.asignar_mascota, name="AsignarMascota"),
    path('EditarMascota/<id>',views.mascota_edit, name = "mascota_edit"),
    path('EditarMiMascota/<id>',views.mascota_edit_cliente, name = "mascota_edit_cliente"),
    path('EliminarMascota/<id>',views.mascota_delete, name = "mascota_delete"),
    path('solicitud/editar/<int:pk>/', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('solicitud/eliminar/<int:pk>/',SolicitudDelete.as_view(), name='solicitud_eliminar'),
    path('usuarios/',views.Usuarios, name='usuarios'),
    path('eliminarusuario/<id>',views.usuario_delete, name = "usuario_delete"),
    path('aceptacion/', views.index, name="EnviarAceptacion"), 
    path('desbloquearusuarios/', views.DesbloquearUsuarios, name="DesbloquearUsuarios"), 
    path('confirmar/<id>', views.UsuarioDesbloquear, name="UsuarioDesbloquear"), 
    path('mi_mascota/', views.MiMascota, name="MiMascota"),
    path('cap/', views.captcha, name="Captcha"),
    
    
    
    
    path('password_reset/', PasswordResetView.as_view(template_name = 'ProyectoFinal2App/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name = 'ProyectoFinal2App/password_reset_done.html'), name='password_reset_done'),
    url('password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/',PasswordResetConfirmView.as_view(template_name = 'ProyectoFinal2App/password_reset_confirm.html'), name='password_reset_confirm'),
    url('password_reset/complete/', PasswordResetCompleteView.as_view(template_name = 'ProyectoFinal2App/password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)