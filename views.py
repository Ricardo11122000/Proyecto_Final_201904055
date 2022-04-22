from email.policy import default
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from axes.models import *
from .forms import *
from django.contrib.auth.models import User 
import psycopg2




def acceder(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=password, request=request)
            if usuario is not None:
                login(request, usuario)
                return redirect("Inicio")
            else:
                messages.error(request, "Los datos son incorrectos")
        else:
            messages.error(request, "Los datos son incorrectos")
            Fallos = form.cleaned_data
            nombre_user = Fallos['username']
            intentos = AccessAttempt.objects.get(username = nombre_user)
            conexion = psycopg2.connect(
            host = "localhost",
            port =  "5432",
            user = "postgres", 
            password = "11122000", 
            dbname = "BaseDeDatosProyectoFinal")
            cursor = conexion.cursor()
            SQL = f"SELECT failures_since_start FROM axes_accessattempt WHERE username = '{nombre_user}';"
            cursor.execute(SQL)
            informacion = cursor.fetchall()
            for numero in informacion:
                for numero_intentos in numero:
                    print (numero_intentos)
            if numero_intentos >= 3:
                return redirect('Captcha')
    
    form = AuthenticationForm()
    context = { "form": form}
    return render(request, "ProyectoFinal2App/Login.html", context)


class RegistroUsuario(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "ProyectoFinal2App/RegistroUsuario.html", {"form": form})

    # noinspection PyMethodMayBeStatic
    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get("username")
            login(request, usuario, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("Inicio")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "ProyectoFinal2App/RegistroUsuario.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect("Inicio")

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("Inicio")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'ProyectoFinal2App/Profile.html', context)

def profile_admin(request, id):
    usuario=User.objects.get(id=id)
    profile=Profile.objects.get(id=id)
    if request.method == 'POST': 
        u_form = UserUpdateForm(request.POST, instance=usuario)
        p_form = ProfileUpdateForm_admin(request.POST, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("Inicio")
    else:
        u_form = UserUpdateForm(instance=usuario)
        p_form = ProfileUpdateForm_admin(instance=usuario.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'ProyectoFinal2App/Profile.html', context)



