from django.shortcuts import render
from AppEstudio.models import FormularioContacto
from django.views.generic import CreateView
from AppEstudio.forms import Contacto

# Create your views here.

def index(request):
    return render(request, 'AppEstudio/index.html')

def formularioContacto(request):
    if request.method == "POST":
      miFormulario= Contacto(request.POST)
      if miFormulario.is_valid():
        informacion= miFormulario.cleaned_data
        cliente = FormularioContacto(

              nombre = informacion["nombre"],
              apellido = informacion["apellido"],
              email = informacion["email"],
              telefono = informacion["telefono"],
              consulta = informacion["consulta"])

          
        cliente.save()
        return render(request, 'AppEstudio/index.html')
    else: 
        miFormulario = Contacto()
    
    return render(request, "AppEstudio/index.html", {"miFormulario": miFormulario})    

class ContactoF(CreateView):

    model = FormularioContacto(CreateView)
    success_url = "../estudio/index"
    fields = ['nombre','apellido', 'email', 'telefono', 'consulta']