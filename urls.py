from django.urls import path
from .views import *

urlpatterns = [
    
    path('reporteusuarios/',ReporteUsuariosPdf.as_view(), name="ReporteUsuarios"),
    path('reportemascotas/',ReporteMascotasPdf.as_view(), name="ReporteMascotas"),
    path('reportemascotasinscritas/',ReporteMascotasInscritasPdf.as_view(), name="ReporteMascotasInscritas"),
    path('reporteaccionesrealizadas/',ReporteAccionesRealizadasPdf.as_view(), name="ReporteAccionesRealizadas"),

]
