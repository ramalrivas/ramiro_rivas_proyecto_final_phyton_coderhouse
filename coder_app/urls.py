from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
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

    #Login/Logout
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),

    # Funciones del usuario Logueado.
    path('logout/', views.user_logout, name='logout'),
    path('upload/', views.upload_image_view, name='upload_image_view'),
    path('delete-image/<int:pk>/', delete_image, name='delete_image'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)