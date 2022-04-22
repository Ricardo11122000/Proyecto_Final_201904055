from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponse
from IngresoMascotas.models import Ingresomascotas
from django.contrib.auth.models import User
from IngresoMascotas.forms import MascotaForm, VacunaForm, AdoptForm, MascotaFormCliente
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from RegistroUsuario.forms import ProfileUpdateForm_admin
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from IngresoMascotas.models import Ingresomascotas_solicitud
from axes.admin import AccessAttempt
from RegistroUsuario.models import Profile
from django.contrib.auth.models import User
from .forms import CaptchaForm
from django.contrib.auth.forms import AuthenticationForm


def Inicio(request):

    Usuarios = User.objects.all()
    
    return render(request, "ProyectoFinal2App/Inicio.html", context={"Usuarios":Usuarios})

def Login(request):
    
    return render(request, "ProyectoFinal2App/Login.html")

def MascotasActuales(request):
    
    Mascotas_adoptadas = Ingresomascotas_solicitud.objects.all()
    
    ingresomascotas = Ingresomascotas.objects.all()
    
    return render(request, "ProyectoFinal2App/MascotasActuales.html",{"ingresomascotas": ingresomascotas, "Mascotas_adoptadas":Mascotas_adoptadas })


def IngresoMascotas(request):
    
    submitted = False
    if request.method == "POST":
        form = MascotaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ingresomascotas?submitted=True')
    else:
        form = MascotaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "ProyectoFinal2App/IngresoMascotas.html",{"form":form, 'submitted':submitted})  

def Ingresovacuna(request):
    
    submitted = False
    if request.method == "POST":
        form = VacunaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ingresovacuna?submitted=True')
    else:
        form = VacunaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "ProyectoFinal2App/IngresoVacuna.html",{"form":form, 'submitted':submitted})  

def asignar_mascota(request):
    
    submitted = False
    if request.method == "POST":
        form = AdoptForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/asignarmascota?submitted=True')
    else:
        form = AdoptForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "ProyectoFinal2App/AsignarMascota.html",{"form":form, 'submitted':submitted})  


def mascota_edit(request, id):
    mascota = Ingresomascotas.objects.get(id=id)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('MascotasActuales')
    return render(request, 'ProyectoFinal2App/IngresoMascotas.html', {'form':form})

def mascota_delete(request, id):
    mascota = Ingresomascotas.objects.get(id=id)
    if request.method == 'POST':
        mascota.delete()
        return redirect('MascotasActuales')
    return render(request, 'ProyectoFinal2App/MascotaDelete.html', {'mascota':mascota})

def Usuarios(request):
    
    usuarios_creados = User.objects.all()
    
    return render(request, "ProyectoFinal2App/Usuarios.html",{"usuarios_creados": usuarios_creados})

def usuario_delete(request, id):
    Usuario = User.objects.get(id=id)
    if request.method == 'POST':
        Usuario.delete()
        return redirect('usuarios')
    return render(request, 'ProyectoFinal2App/UsuariosDelete.html', {'usuario':Usuario})

def usuario_edit(request, id):
    usuario = User.objects.get(id=id)
    if request.method == 'GET':
        form = ProfileUpdateForm_admin(instance=usuario)
    else:
        form = ProfileUpdateForm_admin(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    return render(request, 'ProyectoFinal2App/Profile.html', {'form':form})




def send_email(Email):
    context = {'Email':Email}
    template = get_template('ProyectoFinal2App/AceptarSolicitud.html')
    content = template.render(context)
    
    email = EmailMultiAlternatives(
        'Solicitud de adopcion aprobada',
        'Proyecto',
        settings.EMAIL_HOST_USER,
        [Email]       
    )
    
    email.attach_alternative(content, 'text/html')
    email.send()

def index(request):
    if request.method == 'POST':
        mail = request.POST.get('Email')
        
        send_email(mail)
        return redirect('solicitud_listar')
        
    return render(request, 'ProyectoFinal2App/AceptacionForm.html', {})

def DesbloquearUsuarios(request):
    
    IntentosLogin = AccessAttempt.objects.all()
    Usuarios = User.objects.all()
    
    return render(request, "ProyectoFinal2App/DesbloquearUsuarios.html",{"IntentosLogin": IntentosLogin, "Usuarios": Usuarios})

def UsuarioDesbloquear(request, id):
    IntentoLogin = AccessAttempt.objects.get(id=id)
    if request.method == 'POST':
        IntentoLogin.delete()
        return redirect('DesbloquearUsuarios')
    return render(request, 'ProyectoFinal2App/UsuarioDesbloquear.html', {'Intento': IntentoLogin})


def MiMascota(request):
    
    return render(request, 'ProyectoFinal2App/MascotaAdoptada.html')


def mascota_edit_cliente(request, id):
    mascota = Ingresomascotas.objects.get(id=id)
    if request.method == 'GET':
        form = MascotaFormCliente(instance=mascota)
    else:
        form = MascotaFormCliente(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('MiMascota')
    return render(request, 'ProyectoFinal2App/IngresoMascotas.html', {'form':form})
        
  
def captcha(request):
    if request.method == "POST":
        form = CaptchaForm(request.POST)

        if form.is_valid():
            return redirect('acceder')
    else:
        form = CaptchaForm()

    form = CaptchaForm()
    return render(request, 'ProyectoFinal2App/captcha.html', {'form': form})

