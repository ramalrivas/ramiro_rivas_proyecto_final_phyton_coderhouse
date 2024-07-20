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

def ropa_femenina(request):
    return render(request, 'coder_app/ropa-femenina.html')

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
def camisas(request):
    if request.method == 'POST' and 'submit_camisa' in request.POST:
        form_camisa = ImageUploadForm(request.POST, request.FILES)
        if form_camisa.is_valid():
            image = form_camisa.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'camisas'  
            image.save()
            messages.success(request, 'Imagen de camisa subida correctamente.')
            return redirect('camisas')
        else:
            messages.error(request, 'Error al subir la imagen de camisa.')
    else:
        form_camisa = ImageUploadForm()

    images_camisas = Image.objects.filter(category='camisas')
    return render(request, 'coder_app/camisas.html', {'images': images_camisas, 'form_camisa': form_camisa})
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
def botasf(request):
    if request.method == 'POST' and 'submit_botasf' in request.POST:
        form_botasf = ImageUploadForm(request.POST, request.FILES)
        if form_botasf.is_valid():
            image = form_botasf.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'botasf'
            image.save()
            messages.success(request, 'Imagen de botas subida correctamente.')
            return redirect('botasf')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_botasf = ImageUploadForm()
    
    images_botasf = Image.objects.filter(category='botasf')
    return render(request, 'coder_app/botasf.html', {'images': images_botasf, 'form_botasf': form_botasf})
pass

@login_required (login_url='index')
def blusas(request):
    if request.method == 'POST' and 'submit_blusas' in request.POST:
        form_blusas = ImageUploadForm(request.POST, request.FILES)
        if form_blusas.is_valid():
            image = form_blusas.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'blusas'
            image.save()
            messages.success(request, 'Imagen de blusa subida correctamente.')
            return redirect('blusas')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_blusas = ImageUploadForm()
    
    images_blusas = Image.objects.filter(category='blusas')
    return render(request, 'coder_app/blusas.html', {'images': images_blusas, 'form_blusas': form_blusas})
pass

@login_required (login_url='index')
def camperasf(request):
    if request.method == 'POST' and 'submit_camperasf' in request.POST:
        form_camperasf = ImageUploadForm(request.POST, request.FILES)
        if form_camperasf.is_valid():
            image = form_camperasf.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'camperasf'
            image.save()
            messages.success(request, 'Imagen de campera subida correctamente.')
            return redirect('camperasf')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_camperasf = ImageUploadForm()
    
    images_camperasf = Image.objects.filter(category='camperasf')
    return render(request, 'coder_app/camperasf.html', {'images': images_camperasf, 'form_camperasf': form_camperasf})
pass

@login_required (login_url='index')
def faldas(request):
    if request.method == 'POST' and 'submit_faldas' in request.POST:
        form_faldas = ImageUploadForm(request.POST, request.FILES)
        if form_faldas.is_valid():
            image = form_faldas.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'faldas'
            image.save()
            messages.success(request, 'Imagen de falda subida correctamente.')
            return redirect('faldas')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_faldas = ImageUploadForm()
    
    images_faldas = Image.objects.filter(category='faldas')
    return render(request, 'coder_app/faldas.html', {'images': images_faldas, 'form_faldas': form_faldas})
pass

@login_required (login_url='index')
def pantalonesf(request):
    if request.method == 'POST' and 'submit_pantalonesf' in request.POST:
        form_pantalonesf = ImageUploadForm(request.POST, request.FILES)
        if form_pantalonesf.is_valid():
            image = form_pantalonesf.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'pantalonesf'
            image.save()
            messages.success(request, 'Imagen de pantalon subida correctamente.')
            return redirect('pantalonesf')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_pantalonesf = ImageUploadForm()
    
    images_pantalonesf = Image.objects.filter(category='pantalonesf')
    return render(request, 'coder_app/pantalonesf.html', {'images': images_pantalonesf, 'form_pantalonesf': form_pantalonesf})
pass

@login_required (login_url='index')
def vestidos(request):
    if request.method == 'POST' and 'submit_vestidos' in request.POST:
        form_vestidos = ImageUploadForm(request.POST, request.FILES)
        if form_vestidos.is_valid():
            image = form_vestidos.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'vestidos'
            image.save()
            messages.success(request, 'Imagen de vestido subida correctamente.')
            return redirect('vestidos')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_vestidos = ImageUploadForm()
    
    images_vestidos = Image.objects.filter(category='vestidos')
    return render(request, 'coder_app/vestidos.html', {'images': images_vestidos, 'form_vestidos': form_vestidos})
pass
	
@login_required (login_url='index')
def shortsf(request):
    if request.method == 'POST' and 'submit_shortsf' in request.POST:
        form_shortsf = ImageUploadForm(request.POST, request.FILES)
        if form_shortsf.is_valid():
            image = form_shortsf.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'shortsf'
            image.save()
            messages.success(request, 'Imagen de short subida correctamente.')
            return redirect('shortsf')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_shortsf = ImageUploadForm()
    
    images_shortsf = Image.objects.filter(category='shortsf')
    return render(request, 'coder_app/shortsf.html', {'images': images_shortsf, 'form_shortsf': form_shortsf})
pass

@login_required (login_url='index')
def zapatillasf(request):
    if request.method == 'POST' and 'submit_zapatillasf' in request.POST:
        form_zapatillasf = ImageUploadForm(request.POST, request.FILES)
        if form_zapatillasf.is_valid():
            image = form_zapatillasf.save(commit=False)
            image.uploaded_by = request.user
            image.category = 'zapatillasf'
            image.save()
            messages.success(request, 'Imagen de zapatillas subida correctamente.')
            return redirect('zapatillasf')
        else:
            messages.error(request, 'Error al subir la imagen de hoodie.')
    else:
        form_zapatillasf = ImageUploadForm()
    
    images_zapatillasf = Image.objects.filter(category='zapatillasf')
    return render(request, 'coder_app/zapatillasf.html', {'images': images_zapatillasf, 'form_zapatillasf': form_zapatillasf})
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

      
    if category == 'camisas':
        return redirect('camisas')
    elif category == 'remeras':
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

    if category == 'blusas':
        return redirect('blusas')
    elif category == 'botasf':
        return redirect('botasf')
    
    if category == 'camperasf':
        return redirect('camperasf')
    elif category == 'faldas':
        return redirect('faldas')
    
    if category == 'pantalonesf':
        return redirect('pantalonesf')
    elif category == 'shortsf':
        return redirect('shortsf')
    
    if category == 'zapatillasf':
        return redirect('zapatillasf')
    elif category == 'vestidos':
        return redirect('vestidos')
    
    if category == 'carteleras':
        return redirect('carteleras')
    elif category == 'galerias':
        return redirect('galerias')
    
    else:
        return redirect('index')
