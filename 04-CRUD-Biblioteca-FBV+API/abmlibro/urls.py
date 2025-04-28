from django.urls import path, include
from .views import getLanding, getListado,guardarLibro, actualizarLibro, eliminarLibro
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet)  # Registra el ViewSet

urlpatterns = [
    path('', getLanding),
    path('listadoDeLibros/', getListado, name = 'listar_libros'),
    path('guardarLibro/', guardarLibro, name = 'guardar_libro'),
    path('actualizarLibro/', actualizarLibro, name = 'actualizar_libro'),
    path('eliminarLibro/', eliminarLibro, name = 'eliminar_libro'),
    path('api/', include(router.urls)),  # Incluye las URLs generadas por el router
]
