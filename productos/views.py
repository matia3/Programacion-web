from django.shortcuts import render
from .models import productos
# Create your views here.


def index(request):
    context={}
    return render(request, 'productos/index.html', context)

def listar_productos(request, categoria):
    var_productos = productos.objects.filter(categoria=categoria)
    context={
        'productos':var_productos,
        'categoria':categoria,
    }
    return render(request, 'productos/productos.html', context)


def agregar_productos(request):
    context={}
    return render(request, 'agregarproductos.html', context)

def crud(request):
    var_productos = productos.objects.all()
    context = {'productos': var_productos}
    return render(request,'crud/productos_list.html', context)

def productosAdd(request):
    if request.method is not "post":
        context={}
        return render(request,'crud/productos_add.html',context)