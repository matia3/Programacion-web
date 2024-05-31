from django import forms

from .models import productos



class productosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = ['nombre', 'precio', 'imagen', 'categoria']  # fields to be displayed in the form
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto',
            'imagen': 'Imagen del producto',
            'categoria': 'Categoria del producto',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
        }