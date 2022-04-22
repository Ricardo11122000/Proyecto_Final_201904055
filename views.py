from contextvars import Context
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.http import HttpResponse
from .utils import render_to_pdf
from IngresoMascotas.models import Ingresomascotas, Ingresomascotas_solicitud, Vacuna
from django.contrib.admin.models import LogEntry

class ReporteUsuariosPdf(View):

    def get(self, request, *args, **kwargs):
        Usuarios = User.objects.all()
        data = {
            'usuarios_creados': Usuarios
        }
        pdf = render_to_pdf('ProyectoFinal2App/Reporteusuarios.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class ReporteMascotasPdf(View):

    def get(self, request, *args, **kwargs):
        Mascotas = Ingresomascotas.objects.all()
        MascotaAdoptada = Ingresomascotas_solicitud.objects.all()
        data = {
            'mascotas': Mascotas,
            'Mascotas_adoptadas':MascotaAdoptada
        }
        pdf = render_to_pdf('ProyectoFinal2App/ReporteMascotas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class ReporteMascotasInscritasPdf(View):

    def get(self, request, *args, **kwargs):
        Mascotas = Ingresomascotas.objects.all()
        Vacunas = Vacuna.objects.all()
        data = {
            'mascotas': Mascotas,
            'vacunas': Vacunas
        }
        pdf = render_to_pdf('ProyectoFinal2App/ReporteMascotasAtributos.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

logs = LogEntry.objects.all() 

class ReporteAccionesRealizadasPdf(View):

    def get(self, request, *args, **kwargs):
        logs = LogEntry.objects.all() 
        data = {
            'acciones': logs
        }
        pdf = render_to_pdf('ProyectoFinal2App/ReporteAccionesRealizadas.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    
