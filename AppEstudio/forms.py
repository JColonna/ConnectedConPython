from django import forms
from AppEstudio import models

class Contacto(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    telefono = forms.IntegerField()
    consulta = forms.CharField()