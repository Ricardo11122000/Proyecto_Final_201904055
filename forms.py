from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    profile = forms.FileField(label='Profile', required=False)
    apellidoPaterno = forms.CharField(label='Apellido Paterno', max_length=35, required=False)
    apellidoMaterno = forms.CharField(label='Apellido Materno', max_length=35, required=False)
    nombres = forms.CharField(label='Nombres', max_length=35, required=False)
    edad = forms.IntegerField(label='Edad', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}