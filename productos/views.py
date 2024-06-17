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


def editar_producto(request, id):
    producto = productos.objects.get(id=id)
    if request.method == 'POST':
        form = productosForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('crud')
    else:
        form = productosForm(instance=producto)
    return render(request, 'crud/productos_edit.html', {'form': form, 'producto': producto})


def eliminar_producto(request, id):
    producto = productos.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('crud')
    return render(request, 'crud/productos_delete.html', {'producto': producto})

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
