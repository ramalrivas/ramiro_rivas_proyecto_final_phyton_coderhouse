from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from . import views
from .views import *




urlpatterns = [
    # Index
    path('', views.index, name='index'),
    # Contenido Exclusivo
    path('indumentaria/', views.indumentaria, name='indumentaria'),
    path('eventos/', views.eventos, name='eventos'),

    # Indumentaria
    path('indumentaria/botas/', views.botas, name='botas'),
    path('indumentaria/camperas/', views.camperas, name='camperas'),  
    path('indumentaria/hoodies/', views.hoodies, name='hoodies'),  
    path('indumentaria/pantalones/', views.pantalones, name='pantalones'),  
    path('indumentaria/remeras/', views.remeras, name='remeras'),  
    path('indumentaria/shorts/', views.shorts, name='shorts'),  
    path('indumentaria/zapatillas/', views.zapatillas, name='zapatillas'),  

    # Eventos
    path('eventos/carteleras/', views.carteleras, name='carteleras'),  
    path('eventos/galerias/', views.galerias, name='galerias'),  

    # Inicia Sesión, Registro, Log-Out
    
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registro/', register, name="registro"),

    #___ Edición de Perfil / Avatar
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),

    # Funciones del usuario Logueado.
    path('upload/', views.upload_image_view, name='upload_image_view'),
    path('delete-image/<int:pk>/', delete_image, name='delete_image'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)