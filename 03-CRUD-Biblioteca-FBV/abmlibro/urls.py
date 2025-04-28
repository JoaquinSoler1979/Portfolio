from django.urls import path, include
from .views import getLanding, getListado,guardarLibro, actualizarLibro, eliminarLibro


urlpatterns = [
    path('', getLanding),
    path('listadoDeLibros/', getListado, name = 'listar_libros'),
    path('guardarLibro/', guardarLibro, name = 'guardar_libro'),
    path('actualizarLibro/', actualizarLibro, name = 'actualizar_libro'),
    path('eliminarLibro/', eliminarLibro, name = 'eliminar_libro'),
]
