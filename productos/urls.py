from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='index'),
    path("productos/<str:categoria>", views.listar_productos, name='listar_productos'),
    path("editar/<int:id>", views.editar_producto, name='editar'),
    path("eliminar/<int:id>", views.eliminar_producto, name='eliminar'),
    path("crud", views.crud, name="crud"),
    path("productosAdd", views.productosAdd, name="productosAdd"),
    path("menu", views.menu, name="menu"),  
    path("accounts/", include("django.contrib.auth.urls")),
    path("registration/", views.register_view, name="registrarse"),
    path("carrito/", views.ver_carrito, name="ver_carrito"),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path("carrito/eliminar/<int:item_id>/", views.eliminar_del_carrito, name="eliminar_del_carrito"),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
