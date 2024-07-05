# cart_filters.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (TypeError, ValueError):
        return 0

@register.filter
def total_carrito(items):
    return sum(item.cantidad * item.producto.precio for item in items)
    