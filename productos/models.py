from django.db import models
from django.contrib.auth.models import User

CATEGORIAS = (
    ('Procesadores', 'Procesadores'),
    ('Placa Madre', 'Placa Madre'),
    ('Tarjetas de Video', 'Tarjetas de Video'),
    ('RAM', 'RAM'),
    ('Fuentes de Poder', 'Fuentes de Poder'),
    ('Almacenamiento', 'Almacenamiento'),
    ('Gabinetes', 'Gabinetes'),
    ('Refrigeración', 'Refrigeración'),
    ('Notebooks', 'Notebooks'),
    ('PC', 'PC'),
)

class productos(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    imagen = models.ImageField(upload_to='productos/static/img/', null=True, blank=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    def __str__(self):
        return self.nombre

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrito de {self.usuario.username}"
    

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
