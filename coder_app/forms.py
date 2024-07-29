from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm 


# PERFIL DE USUARIOS (REGISTRO, LOGIN/LOGOUT, EDITAR PERFIL Y AVATAR)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario", max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

# POSTEO DE CONTENIDO (UPLOAD, DELETE, EDIT)

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image  
        fields = ['title', 'image', 'description'] 

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'image']

# COMENTARIOS (UPLOAD, DELETE, EDIT)

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
