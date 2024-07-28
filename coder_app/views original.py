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
    return render(request, 'index.html')

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


# ------------------------------ POSTEO  ---------------------- #    

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

@staff_member_required
def delete_image(request, pk):
    if request.method == 'POST':
        try:
            image = get_object_or_404(Image, pk=pk)
            image.delete()
            return redirect('botas')
        except Image.DoesNotExist:
            print(f"La imagen {pk} seleccionada no existe")
            return HttpResponse("Image not found", status=404)
    else:
        print(f"Request method was {request.method}, not POST")
        return HttpResponse(status=405)

@login_required
def edit_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('botas')  
    else:
        form = ImageForm(instance=image)
    return render(request, 'coder_app/indumentaria/edit_image.html', {'form': form, 'image': image})

# ------------------------- SECCIÓN EVENTOS ------------------------- #
def eventos(request):
    return render(request, 'coder_app/eventos.html')

@login_required 
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

@login_required 
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

@login_required 
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

@login_required 
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
            messages.error(request, 'Error al subir la imagen de campera.')
    else:
        form_campera = ImageUploadForm()

    images_guantes = Image.objects.filter(category='guantes')  
    return render(request, 'coder_app/indumentaria/guantes.html', {'images': images_guantes, 'form_campera': form_campera})
pass

@login_required 
def hoodies(request):
    if request.method == 'POST' and 'submit_hoodies' in request.POST:
        form_hoodies = ImageUploadForm(request.POST, request.FILES)
        if form_hoodies.is_valid():
            image = form_hoodies.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'hoodies'
            image.save()
            messages.success(request, 'Imagen de hoodie subida correctamente.')
            return redirect('hoodies')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_hoodies = ImageUploadForm()
    
    images_hoodies = Image.objects.filter(category='hoodies')
    return render(request, 'coder_app/indumentaria/hoodies.html', {'images': images_hoodies, 'form_hoodies': form_hoodies})
pass

@login_required 
def pantalones(request):
    if request.method == 'POST' and 'submit_pantalones' in request.POST:
        form_pantalones = ImageUploadForm(request.POST, request.FILES)
        if form_pantalones.is_valid():
            image = form_pantalones.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'pantalones'
            image.save()
            messages.success(request, 'Imagen de pantalon subida correctamente.')
            return redirect('pantalones')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_pantalones = ImageUploadForm()
    
    images_pantalones = Image.objects.filter(category='pantalones')
    return render(request, 'coder_app/indumentaria/pantalones.html', {'images': images_pantalones, 'form_pantalones': form_pantalones})
pass

@login_required 
def remeras(request):
    if request.method == 'POST' and 'submit_remera' in request.POST:
        form_remera = ImageUploadForm(request.POST, request.FILES)
        if form_remera.is_valid():
            image = form_remera.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'remeras'
            image.save()
            messages.success(request, 'Imagen de remera subida correctamente.')
            return redirect('remeras')
        else:
            messages.error(request, 'Error al subir la imagen de remera.')
    else:
        form_remera = ImageUploadForm()
    
    images_remeras = Image.objects.filter(category='remeras')
    return render(request, 'coder_app/indumentaria/remeras.html', {'images': images_remeras, 'form_remera': form_remera})
pass
    

@login_required 
def shorts(request):
    if request.method == 'POST' and 'submit_shorts' in request.POST:
        form_shorts = ImageUploadForm(request.POST, request.FILES)
        if form_shorts.is_valid():
            image = form_shorts.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'shorts'
            image.save()
            messages.success(request, 'Imagen de short subida correctamente.')
            return redirect('shorts')
        else:
            messages.error(request, 'Error al subir la imagen de short.')
    else:
        form_shorts = ImageUploadForm()
    
    images_shorts = Image.objects.filter(category='shorts')
    return render(request, 'coder_app/indumentaria/shorts.html', {'images': images_shorts, 'form_shorts': form_shorts})
pass

@login_required 
def zapatillas(request):
    if request.method == 'POST' and 'submit_zapatillas' in request.POST:
        form_zapatillas = ImageUploadForm(request.POST, request.FILES)
        if form_zapatillas.is_valid():
            image = form_zapatillas.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'zapatillas'
            image.save()
            messages.success(request, 'Imagen de zapatilla subida correctamente.')
            return redirect('zapatillas')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_zapatillas = ImageUploadForm()
    
    images_zapatillas = Image.objects.filter(category='zapatillas')
    return render(request, 'coder_app/indumentaria/zapatillas.html', {'images': images_zapatillas, 'form_zapatillas': form_zapatillas})
pass

