from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    CATEGORY_CHOICES = (
        ('remeras', 'Remeras'),
        ('hoodies', 'Hoodies'),
        ('pantalones', 'Pantalones'),
        ('shorts', 'Shorts'),
        ('camperas', 'Camperas'),
        ('zapatillas', 'Zapatillas'),
        ('botas', 'Botas'),
        ('carteleras', 'carteleras'),
        ('galerias', 'Galerias'),
        
    )
    
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='user_images/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)  

    def __str__(self):
        return self.title if self.title else f"Image {self.id}"
    

#-------------------------
class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"  