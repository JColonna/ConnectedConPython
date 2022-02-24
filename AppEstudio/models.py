from django.db import models

# Create your models here.

class FormularioContacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()
    consulta = models.CharField(max_length=200)
    def __str__(self):
        return (f'Nombre: {self.nombre},Apellido: {self.apellido}, Email: {self.email}, Telefono: {self.telefono}, Consulta: {self.consulta}')