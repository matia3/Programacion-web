from django.shortcuts import render, redirect
from .models import productos
from .forms import productosForm

def index(request):
    context = {}
    return render(request, 'productos/index.html', context)

def listar_productos(request, categoria):
    var_productos = productos.objects.filter(categoria=categoria)
    context = {
        'productos': var_productos,
        'categoria': categoria,
    }
    return render(request, 'productos/productos.html', context)

def agregar_productos(request):
    if request.method == 'POST':
        form = productosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = productosForm()
    return render(request, 'productos/agregarproductos.html', {'form': form})

def editar_producto(request, id):
    producto = productos.objects.get(id=id)
    if request.method == 'POST':
        form = productosForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = productosForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

def eliminar_producto(request, id):
    producto = productos.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

def crud(request):
    var_productos = productos.objects.all()
    context = {'productos': var_productos}
    return render(request, 'crud/productos_list.html', context)

def productosAdd(request):
    if request.method == "POST":
        form = productosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = productosForm()
    return render(request, 'crud/productos_add.html', {'form': form})
