from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# PERFIL DE USUARIOS (REGISTRO, LOGIN/LOGOUT, EDITAR PERFIL Y AVATAR)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares")

    def __str__(self):
        return f"{self.user.username}"
    

# POSTEO DE CONTENIDO (UPLOAD, DELETE, EDIT)

class Image(models.Model):
    CATEGORY_CHOICES = (

        #indumentaria
        ('guantes', 'Guantes'),
        ('zapatillas', 'Zapatillas'),
        ('botas', 'Botas'),

        #Eventos
        ('olimpicos_mundiales', 'Olimpicos-mundiales'),
        ('carteleras', 'Carteleras'),
    )
    
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='user_images/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"

# COMENTARIOS (UPLOAD, DELETE, EDIT)

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario.username} - {self.fecha_publicacion}'

    def fecha_publicacion_formateada(self):
        return self.fecha_publicacion.strftime('%A, %d de %B de %Y. %H:%M')
