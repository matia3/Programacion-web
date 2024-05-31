from django.db import models

class productos(models.Model):
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    imagen = models.ImageField(upload_to='productos/static/img/', null=True, blank=True)  # ImageField to handle image uploads
    categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
