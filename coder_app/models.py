from django.db import models
from django.contrib.auth.models import User

# ------------------ AVATAR --------------

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares")

    def __str__(self):
        return f"{self.user.username}"
    

# ------------------ POSTEOS (EDIT, DELETE, UPLOAD) --------------
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
    