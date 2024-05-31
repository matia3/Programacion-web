from django.contrib import admin
from .models import productos

@admin.register(productos)
class MyTableAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria')
