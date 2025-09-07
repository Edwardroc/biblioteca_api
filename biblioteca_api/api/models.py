from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, blank=True, null=True)

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    año_publicacion = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros')

class Miembro(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_membresia = models.DateField(auto_now_add=True)

class Prestamo(models.Model):
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='prestamos')