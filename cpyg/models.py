from django.db import models

# Create your models here.

class Categoria (models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='ID Categoria')
    nombreCategoria=models.CharField(max_length=20, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class Cliente(models.Model):
    rut = models.CharField(max_length=6, primary_key=True, verbose_name='rut')
    nombre = models.CharField(max_length=20, verbose_name='nombre')
    correo =models.CharField(max_length=20, verbose_name='correo')
    telefono =models.CharField(max_length=20, verbose_name='telefono')
    direccion = models.CharField(max_length=20, verbose_name='direccion')
    

    def __str__(self):
        return self.rut


class Producto(models.Model):
    idProducto=models.IntegerField(primary_key=True, verbose_name='idProducto')
    nombre=models.CharField(max_length=50, verbose_name='Nombre')
    marca= models.CharField(max_length=20, verbose_name='Marca')
    precio= models.IntegerField(verbose_name='Precio')
    imagen=models.ImageField(upload_to="producto", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.idProducto




