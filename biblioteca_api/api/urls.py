from django.urls import path
from .views import (
    AutorListCreate, AutorRetrieveUpdateDestroy,
    EditorialListCreate, EditorialRetrieveUpdateDestroy,
    LibroListCreate, LibroRetrieveUpdateDestroy,
    MiembroListCreate, MiembroRetrieveUpdateDestroy,
    PrestamoListCreate, PrestamoRetrieveUpdateDestroy
)

urlpatterns = [
    path('autores/', AutorListCreate.as_view(), name='autor-list-create'),
    path('autores/<int:pk>/', AutorRetrieveUpdateDestroy.as_view(), name='autor-detail'),
    path('editoriales/', EditorialListCreate.as_view(), name='editorial-list-create'),
    path('editoriales/<int:pk>/', EditorialRetrieveUpdateDestroy.as_view(), name='editorial-detail'),
    path('libros/', LibroListCreate.as_view(), name='libro-list-create'),
    path('libros/<int:pk>/', LibroRetrieveUpdateDestroy.as_view(), name='libro-detail'),
    path('miembros/', MiembroListCreate.as_view(), name='miembro-list-create'),
    path('miembros/<int:pk>/', MiembroRetrieveUpdateDestroy.as_view(), name='miembro-detail'),
    path('prestamos/', PrestamoListCreate.as_view(), name='prestamo-list-create'),
    path('prestamos/<int:pk>/', PrestamoRetrieveUpdateDestroy.as_view(), name='prestamo-detail'),
]