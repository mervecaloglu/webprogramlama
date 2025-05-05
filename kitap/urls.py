from django.urls import path
from . import views

urlpatterns = [
    path('', views.kitap_listesi, name='kitap_listesi'),
]
