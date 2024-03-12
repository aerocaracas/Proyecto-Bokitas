from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Formularios
class SignUpForm(UserCreationForm):
    Name = forms.CharField(label='Nombre',widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Correo',widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Clave',widget=forms.TextInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirmar Clave',widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ('Name','email','username','password1','password2')
        

# Login 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
    