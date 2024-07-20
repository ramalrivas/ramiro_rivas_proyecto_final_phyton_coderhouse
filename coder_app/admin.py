from django.contrib import admin
from .models import Image  

class ImageAdmin(admin.ModelAdmin):  
    list_display = ('id', 'title', 'image', 'uploaded_by')

admin.site.register(Image, ImageAdmin)  
