from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(categoria)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Cliente)
admin.site.register(Checkout)