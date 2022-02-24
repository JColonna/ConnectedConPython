from AppEstudio import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name='Index'),
    path('contacto', views.formularioContacto, name='Contacto'),
   
    ]