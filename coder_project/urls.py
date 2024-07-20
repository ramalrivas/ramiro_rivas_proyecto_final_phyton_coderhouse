# coder_project/urls.py

from django.contrib import admin
from django.urls import include, path
from coder_app import views
from coder_app import views as coder_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coder_app/', include('coder_app.urls')),
    path('', views.index, name='home'),
    path('logout/', coder_views.user_logout, name='logout'),
    path('upload/', views.upload_image_view, name='upload_image_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)