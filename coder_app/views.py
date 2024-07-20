from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import ImageUploadForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Image
from django.urls import reverse
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html')

def indumentaria(request):
    return render(request, 'coder_app/indumentaria.html')

def eventos(request):
    return render(request, 'coder_app/eventos.html')

@login_required (login_url='index')
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
    return render(request, 'coder_app/botas.html', {'images': images_botas, 'form_botas': form_botas})
pass

@login_required (login_url='index')
def camperas(request):
    
    if request.method == 'POST':
        form_campera = ImageUploadForm(request.POST, request.FILES)
        if form_campera.is_valid():
            image = form_campera.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'camperas'  
            image.save()
            messages.success(request, 'Imagen de campera subida correctamente.')
            return redirect('camperas')
        else:
            messages.error(request, 'Error al subir la imagen de campera.')
    else:
        form_campera = ImageUploadForm()

    images_camperas = Image.objects.filter(category='camperas')  
    return render(request, 'coder_app/camperas.html', {'images': images_camperas, 'form_campera': form_campera})
pass

@login_required (login_url='index')
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
    return render(request, 'coder_app/hoodies.html', {'images': images_hoodies, 'form_hoodies': form_hoodies})
pass

@login_required (login_url='index')
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
    return render(request, 'coder_app/pantalones.html', {'images': images_pantalones, 'form_pantalones': form_pantalones})
pass

@login_required (login_url='index')
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
    return render(request, 'coder_app/remeras.html', {'images': images_remeras, 'form_remera': form_remera})
pass
    

@login_required (login_url='index')
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
    return render(request, 'coder_app/shorts.html', {'images': images_shorts, 'form_shorts': form_shorts})
pass

@login_required (login_url='index')
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
    return render(request, 'coder_app/zapatillas.html', {'images': images_zapatillas, 'form_zapatillas': form_zapatillas})
pass

@login_required (login_url='index')
def galerias(request):
    if request.method == 'POST' and 'submit_galerias' in request.POST:
        form_galerias = ImageUploadForm(request.POST, request.FILES)
        if form_galerias.is_valid():
            image = form_galerias.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'galerias'
            image.save()
            messages.success(request, 'Imagen de galeria subida correctamente.')
            return redirect('galerias')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_galerias = ImageUploadForm()
    
    images_galerias = Image.objects.filter(category='galerias')
    return render(request, 'coder_app/galerias.html', {'images': images_galerias, 'form_galerias': form_galerias})
pass

@login_required (login_url='index')
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
    return render(request, 'coder_app/carteleras.html', {'images': images_carteleras, 'form_carteleras': form_carteleras})
pass

def user_login(request):
    if request.method == 'POST':
        print("Login Data:", request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
           
            return render(request, 'index.html', {'error': 'Usuario o contraseña incorrectos'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso. Por favor, inicia sesión.')
            return redirect('index')
        else:
            print(form.errors)  
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión exitosamente.')
    return redirect('index')

@login_required
def upload_image_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.uploaded_by = request.user
            image.save()
            messages.success(request, 'Imagen subida correctamente.')
            return redirect('camisas')  
        else:
            messages.error(request, 'Error al subir la imagen.')
    else:
        form = ImageUploadForm()
    return render(request, 'coder_app/camisas.html', {'form': form})

def mi_vista_restringida(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Debes iniciar sesión para ver esta página.')
        return redirect('index')

@staff_member_required
def delete_image(request, pk):
    image = get_object_or_404(Image, pk=pk)
    category = image.category  
    image.delete()
    messages.success(request, 'Imagen eliminada correctamente.')

      
    if category == 'remeras':
        return redirect('remeras')
    
    if category == 'hoodies':
        return redirect('hoodies')
    elif category == 'pantalones':
        return redirect('pantalones')
    
    if category == 'shorts':
        return redirect('shorts')
    elif category == 'camperas':
        return redirect('camperas')
    
    if category == 'zapatillas':
        return redirect('zapatillas')
    elif category == 'botas':
        return redirect('botas')   

    if category == 'carteleras':
        return redirect('carteleras')
    elif category == 'galerias':
        return redirect('galerias')
    else:
        return redirect('index')
