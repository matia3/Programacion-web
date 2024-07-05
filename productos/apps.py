from django.apps import AppConfig


class ProductosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'productos'


class ProductosConfig(AppConfig):
    name = 'productos'

    def ready(self):
        import productos.signals
