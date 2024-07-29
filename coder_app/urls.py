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
    path('edit_image/<int:pk>/botas/', edit_image, {'template_name': 'coder_app/edit_image.html', 'redirect_url': 'botas'}, name='edit_image_botas'),
    # Zapatillas
    path('upload_image/zapatillas/', upload_image_view, {'template_name': 'coder_app/indumentaria/zapatillas.html', 'redirect_url': 'zapatillas'}, name='upload_image_zapatillas'),
    path('delete_image/<int:pk>/zapatillas/', delete_image, {'redirect_url': 'zapatillas'}, name='delete_image_zapatillas'),
    path('edit_image/<int:pk>/zapatillas/', edit_image, {'template_name': 'coder_app/edit_image.html', 'redirect_url': 'zapatillas'}, name='edit_image_zapatillas'),
    # Guantes
    path('upload_image/guantes/', upload_image_view, {'template_name': 'coder_app/indumentaria/guantes.html', 'redirect_url': 'guantes'}, name='upload_image_guantes'),
    path('delete_image/<int:pk>/guantes/', delete_image, {'redirect_url': 'guantes'}, name='delete_image_guantes'),
    path('edit_image/<int:pk>/guantes/', edit_image, {'template_name': 'coder_app/edit_image.html', 'redirect_url': 'guantes'}, name='edit_image_guantes'),

    # >>>>>>>>> EVENTOS <<<<<<<<<<
    # Eventos MGM.
    path('upload_image/carteleras/', upload_image_view, {'template_name': 'coder_app/eventos/carteleras.html', 'redirect_url': 'carteleras'}, name='upload_image_carteleras'),
    path('delete_image/<int:pk>/carteleras/', delete_image, {'redirect_url': 'carteleras'}, name='delete_image_carteleras'),
    path('edit_image/<int:pk>/carteleras/', edit_image, {'template_name': 'coder_app/edit_image.html', 'redirect_url': 'carteleras'}, name='edit_image_carteleras'),
    # Eventos Olímpicos-Mundiales.
    path('upload_image/olimpicos_mundiales/', upload_image_view, {'template_name': 'coder_app/eventos/olimpicos_mundiales.html', 'redirect_url': 'olimpicos_mundiales'}, name='upload_image_olimpicos_mundiales'),
    path('delete_image/<int:pk>/olimpicos_mundiales/', delete_image, {'redirect_url': 'olimpicos_mundiales'}, name='delete_image_olimpicos_mundiales'),
    path('edit_image/<int:pk>/olimpicos_mundiales/', edit_image, {'template_name': 'coder_app/edit_image.html', 'redirect_url': 'olimpicos_mundiales'}, name='edit_image_olimpicos_mundiales'),

# COMENTARIOS (UPLOAD, DELETE, EDIT)
    path('comentario/agregar/', views.agregar_comentario, name='agregar_comentario'),
    path('comentario/<int:pk>/editar/', views.editar_comentario, name='editar_comentario'),
    path('comentario/<int:pk>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
    path('comentarios/', views.listar_comentarios, name='listar_comentarios'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)