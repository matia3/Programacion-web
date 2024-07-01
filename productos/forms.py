from django import forms
from .models import productos

class productosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = ['nombre', 'precio', 'imagen', 'categoria']
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


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control titulo', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control titulo', 'placeholder': 'Password'})
    )
