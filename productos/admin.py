from django.contrib import admin
from .models import productos, Carrito, CarritoItem

@admin.register(productos)
class MyTableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')

admin.site.register(Carrito)
admin.site.register(CarritoItem)