from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import Profile
from django import forms




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, min_length=12)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
   

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']
        
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        
class ProfileUpdateForm_admin(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['permiso']