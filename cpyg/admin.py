from django.contrib import admin
from .models import Categoria, Producto, Cliente
# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Categoria)