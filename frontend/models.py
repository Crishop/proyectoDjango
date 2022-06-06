from django.db import models

# Create your models here.
class categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="ID categoría")
    nombreCategoria=models.CharField(max_length=30, verbose_name="Nombre Categoría")

    def __str__(self):
        return (self.nombreCategoria)


class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="ID Producto")
    nombreProducto=models.CharField(max_length=30, verbose_name="Nombre Producto")
    imagen=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, verbose_name="Imagen Producto")
    precio=models.IntegerField(verbose_name="Precio Producto")
    stock=models.IntegerField(verbose_name="Stock Producto")
    categoria=models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='productos')
    def __str__(self):
        return (self.nombreProducto)

producto=models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='productos')
def __str__(self):
    return (self.nombreCarrito)

class Checkout(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='productos')
    def __str__(self):
        return (self.nombreCarrito)