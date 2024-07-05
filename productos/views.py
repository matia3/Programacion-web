from django.shortcuts import render, redirect, get_object_or_404
from .models import productos, Carrito, CarritoItem
from .forms import productosForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST

def index(request):
    var_productos = productos.objects.all()
    context = {
         'productos': var_productos,
    }
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

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
            form = UserCreationForm()
    return render(request, 'registration/registrarse.html', {"form": form })



def ver_carrito(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito})



def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id, carrito__usuario=request.user)
    item.delete()
    return redirect('ver_carrito')

def detalle_producto(request, pk):
    producto = get_object_or_404(productos, pk=pk)
    context = {'producto': producto}
    return render(request, 'producto.html', context)

@require_POST
def actualizar_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, id=item_id)
    nueva_cantidad = request.POST.get('cantidad')
    if nueva_cantidad:
        item.cantidad = int(nueva_cantidad)
        item.save()
    return redirect('ver_carrito')

@login_required
def menu(request):
    usuario=request.session.get("usuario")
    context ={"usuario":usuario}
    return render(request, 'productos/index.html', context)

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(productos, pk=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito_item, item_created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not item_created:
        carrito_item.cantidad += 1
        carrito_item.save()

    return redirect('ver_carrito')