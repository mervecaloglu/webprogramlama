from django.urls import path
from . import views

urlpatterns = [
    path('', views.kitap_listesi, name='kitap_listesi'),
    path('kitap/<int:pk>/', views.kitap_detay, name='kitap_detay'),  # 👈 detay sayfası için yeni yol
]
