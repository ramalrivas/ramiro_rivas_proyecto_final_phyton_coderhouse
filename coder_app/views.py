from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


# ------------------------- INDEX -------------------------

def index(request):
    comentarios = Comentario.objects.all() 
    return render(request, 'index.html', {'comentarios': comentarios})

# ------------------------- MENSAJES DE SISTEMA -------------------------
def mensajes(request):
    messages.success(request, 'Operación exitosa.')
    return redirect('index')

# ------------------------- MANEJO DE SESION DE USUARIOS, REGISTRO, AVATAR, PERFIL, -------------------------

def loginRequest(request):
    if request.method == "POST":
        miForm = CustomAuthenticationForm(data=request.POST)
        if miForm.is_valid():
            username = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                avatar = Avatar.objects.filter(user=user).first()
                if avatar:
                    request.session["avatar_url"] = avatar.imagen.url
                else:
                    request.session["avatar_url"] = None
                
                messages.success(request, "Inicio de sesión exitoso")
                return redirect('index')
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Formulario no válido")
    else:
        miForm = CustomAuthenticationForm()
    
    return render(request, "sessions/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            messages.success(request, "Registro exitoso. Por favor, inicie sesión.")
            return redirect('index')
        else:
            messages.error(request, "Formulario de registro no válido.")
    else:
        miForm = RegistroForm()

    return render(request, "sessions/registro.html", {"form": miForm})

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=usuario)
        avatar_form = AvatarForm(request.POST, request.FILES)
        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            avatar = Avatar.objects.filter(user=usuario).first()
            if avatar:
                avatar.imagen = avatar_form.cleaned_data['imagen']
                avatar.save()
            else:
                Avatar.objects.create(user=usuario, imagen=avatar_form.cleaned_data['imagen'])
            request.session["avatar_url"] = usuario.avatar.imagen.url
            messages.success(request, 'Perfil actualizado exitosamente')
            return redirect('index')
        else:
            messages.error(request, "Formulario de edición no válido.")
    else:
        user_form = UserEditForm(instance=usuario)
        avatar_form = AvatarForm()
    return render(request, "sessions/editarPerfil.html", {"user_form": user_form, "avatar_form": avatar_form})


# ------------------------------ IMAGENES ----------------------

@login_required
def upload_image_view(request, template_name, redirect_url):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = request.user
            image.save()
            messages.success(request, 'Imagen subida correctamente.')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Error al subir la imagen.')
    else:
        form = ImageUploadForm()
    return render(request, template_name, {'form': form})

@login_required
def delete_image(request, pk, redirect_url):
    if request.method == 'POST':
        try:
            image = get_object_or_404(Image, pk=pk)
            image.delete()
            return redirect(redirect_url)
        except Image.DoesNotExist:
            print(f"La imagen {pk} seleccionada no existe")
            return HttpResponse("Imagen no Encontrada", status=404)
    else:
        print(f"Request method was {request.method}, not POST")
        return HttpResponse(status=405)

@login_required
def edit_image(request, pk, template_name, redirect_url):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = ImageForm(instance=image)
    return render(request, template_name, {'form': form, 'image': image})


# ------------------------- SECCIÓN EVENTOS -------------------------
def eventos(request):
    return render(request, 'coder_app/eventos.html')

def olimpicos_mundiales(request):
    if request.method == 'POST' and 'submit_olimpicos_mundiales' in request.POST:
        form_olimpicos_mundiales = ImageUploadForm(request.POST, request.FILES)
        if form_olimpicos_mundiales.is_valid():
            image = form_olimpicos_mundiales.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'olimpicos_mundiales'
            image.save()
            messages.success(request, 'Imagen de galeria subida correctamente.')
            return redirect('olimpicos_mundiales')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_olimpicos_mundiales = ImageUploadForm()
    
    images_olimpicos_mundiales = Image.objects.filter(category='olimpicos_mundiales')
    return render(request, 'coder_app/eventos/olimpicos_mundiales.html', {'images': images_olimpicos_mundiales, 'form_olimpicos_mundiales': form_olimpicos_mundiales})
pass


def carteleras(request):
    if request.method == 'POST' and 'submit_carteleras' in request.POST:
        form_carteleras = ImageUploadForm(request.POST, request.FILES)
        if form_carteleras.is_valid():
            image = form_carteleras.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'carteleras'
            image.save()
            messages.success(request, 'Imagen de lanzamiento subida correctamente.')
            return redirect('carteleras')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_carteleras = ImageUploadForm()
    
    images_carteleras = Image.objects.filter(category='carteleras')
    return render(request, 'coder_app/eventos/carteleras.html', {'images': images_carteleras, 'form_carteleras': form_carteleras})
pass


# ------------------------------- SECCION INDUMENTARIA -------------------------
def indumentaria(request):
    return render(request, 'coder_app/indumentaria.html')


def botas(request):
    if request.method == 'POST':
        form_botas = ImageUploadForm(request.POST, request.FILES)
        if form_botas.is_valid():
            image = form_botas.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'botas'  
            image.save()
            messages.success(request, 'Imagen de botas subida correctamente.')
            return redirect('botas')
        else:
            messages.error(request, 'Error al subir la imagen de botas.')
    else:
        form_botas = ImageUploadForm()
        images_botas = Image.objects.filter(category='botas')  
    return render(request, 'coder_app/indumentaria/botas.html', {'images': images_botas, 'form_botas': form_botas})
pass



def zapatillas(request):
    if request.method == 'POST' and 'submit_zapatillas' in request.POST:
        form_zapatillas = ImageUploadForm(request.POST, request.FILES)
        if form_zapatillas.is_valid():
            image = form_zapatillas.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'zapatillas'
            image.save()
            messages.success(request, 'Imagen de zapatillas subida correctamente.')
            return redirect('zapatillas')
        else:
            messages.error(request, 'Error al subir la imagen de Zapatillas.')
    else:
        form_zapatillas = ImageUploadForm()
    
    images_zapatillas = Image.objects.filter(category='zapatillas')
    return render(request, 'coder_app/indumentaria/zapatillas.html', {'images': images_zapatillas, 'form_zapatillas': form_zapatillas})
pass


 
def guantes(request):
    
    if request.method == 'POST':
        form_campera = ImageUploadForm(request.POST, request.FILES)
        if form_campera.is_valid():
            image = form_campera.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'guantes'  
            image.save()
            messages.success(request, 'Imagen de campera subida correctamente.')
            return redirect('guantes')
        else:
            messages.error(request, 'Error al subir la imagen de Guantes.')
    else:
        form_campera = ImageUploadForm()

    images_guantes = Image.objects.filter(category='guantes')  
    return render(request, 'coder_app/indumentaria/guantes.html', {'images': images_guantes, 'form_campera': form_campera})
pass

# COMENTARIOS (UPLOAD, DELETE, EDIT)

@login_required
def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.save()
            return redirect('/#comments')
    else:
        form = ComentarioForm()
    return render(request, 'coder_app/comentarios/comentario_form.html', {'form': form})

@login_required
def editar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            return redirect('/#comments')
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, 'coder_app/comentarios/comentario_form.html', {'form': form})

@login_required
def eliminar_comentario(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    if request.method == 'POST':
        comentario.delete()
        return redirect('/#comments')
    return render(request, 'coder_app/comentarios/confirmar_eliminacion.html', {'comentario': comentario})

def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, 'coder_app/comentarios/comentarios_list.html', {'comentarios': comentarios})
