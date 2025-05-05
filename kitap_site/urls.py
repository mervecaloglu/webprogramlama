from django.contrib import admin
from django.urls import path, include  # include ekledik

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kitap.urls')),  # kitap.urls dosyasını bağladık
]
