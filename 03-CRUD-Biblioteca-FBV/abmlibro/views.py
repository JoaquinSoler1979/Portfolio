from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse as hr
from .models import Libro
from .serializers import LibroSerializer
from rest_framework import viewsets



def getLanding(self):

    plantilla = loader.get_template('landing.html')
    return hr(plantilla.render())

def getListado(request):
    
    libros = Libro.objects.all()
    return render(request, 'listadoDeLibros.html', {'libros': libros})

def guardarLibro(request):
    if request.method == 'POST':
        libro = Libro()
        libro.nombre = request.POST['nombre']
        libro.autor = request.POST['autor']        
        libro.fecha_publicacion = request.POST['año_publicacion']
        libro.save()

        return getListado(request)
    
def actualizarLibro(request):

    if request.method == 'POST':
        libro = Libro()
        libro.id = request.POST['id']
        libro.nombre = request.POST['nombre']
        libro.autor = request.POST['autor']        
        libro.fecha_publicacion = request.POST['fecha_publicacion']
        libro.save()

        return getListado(request)
    
def eliminarLibro(request):
    if request.method == 'POST':
        libro = get_object_or_404(Libro, id=request.POST['id'])
        libro.delete()

        return getListado(request)
        



    


