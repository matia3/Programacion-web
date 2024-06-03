from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='index'),
    path("productos/<str:categoria>", views.listar_productos, name='listar_productos'),
    path("agregarproductos", views.agregar_productos, name='agregar_productos'),
    path("crud", views.crud, name="crud"),
    path("productosAdd", views.productosAdd, name="productosAdd"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
