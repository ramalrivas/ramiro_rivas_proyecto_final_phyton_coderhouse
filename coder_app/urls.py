from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views
from .views import *




urlpatterns = [
#INDEX 
    path('', views.index, name='index'),

# PERFIL DE USUARIOS (REGISTRO, LOGIN/LOGOUT, EDITAR PERFIL Y AVATAR)
    
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registro/', register, name="registro"),
    path('mensajes_sys/', views.mensajes, name="mensajes"),
    path('editarPerfil/', views.editProfile, name='editarPerfil'),

# SECCION DE CONTENIDO EXCLUSIVO
    
    # Indumentaria
    path('indumentaria/', views.indumentaria, name='indumentaria'),
    path('indumentaria/botas/', views.botas, name='botas'),
    path('indumentaria/zapatillas/', views.zapatillas, name='zapatillas'),
    path('indumentaria/guantes/', views.guantes, name='guantes'),
    
    # Eventos
    path('eventos/', views.eventos, name='eventos'),
    path('eventos/carteleras/', views.carteleras, name='carteleras'),  
    path('eventos/olimpicos_mundiales/', views.olimpicos_mundiales, name='olimpicos_mundiales'), 
    
    # Equipamiento
    # path(path('equipamiento/', views.equipamiento, name='equipamiento')

# POSTEO DE CONTENIDO (UPLOAD, DELETE, EDIT)
    
    # >>>>>>>>> INDUMENTARIA <<<<<<<<<<
    # Botas
    path('upload_image/botas/', upload_image_view, {'template_name': 'coder_app/indumentaria/botas.html', 'redirect_url': 'botas'}, name='upload_image_botas'),
    path('delete_image/<int:pk>/botas/', delete_image, {'redirect_url': 'botas'}, name='delete_image_botas'),
    path('edit_image/<int:pk>/botas/', edit_image, {'template_name': 'coder_app/indumentaria/edit_image.html', 'redirect_url': 'botas'}, name='edit_image_botas'),
    # Zapatillas
    path('upload_image/zapatillas/', upload_image_view, {'template_name': 'coder_app/indumentaria/zapatillas.html', 'redirect_url': 'zapatillas'}, name='upload_image_zapatillas'),
    path('delete_image/<int:pk>/zapatillas/', delete_image, {'redirect_url': 'zapatillas'}, name='delete_image_zapatillas'),
    path('edit_image/<int:pk>/zapatillas/', edit_image, {'template_name': 'coder_app/indumentaria/edit_image.html', 'redirect_url': 'zapatillas'}, name='edit_image_zapatillas'),
    # Guantes
    path('upload_image/botas/', upload_image_view, {'template_name': 'coder_app/indumentaria/botas.html', 'redirect_url': 'botas'}, name='upload_image_botas'),
    path('delete_image/<int:pk>/botas/', delete_image, {'redirect_url': 'botas'}, name='delete_image_botas'),
    path('edit_image/<int:pk>/botas/', edit_image, {'template_name': 'coder_app/indumentaria/edit_image.html', 'redirect_url': 'botas'}, name='edit_image_botas'),

    # >>>>>>>>> EVENTOS <<<<<<<<<<
    # Eventos MGM.

    # Eventos Olímpicos-Mundiales.

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)