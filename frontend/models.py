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
    imagen=models.CharField(max_length=256)
    precio=models.IntegerField(verbose_name="Precio Producto")
    stock=models.IntegerField(verbose_name="Stock Producto")
    categoria=models.ForeignKey(categoria, on_delete=models.CASCADE, related_name='productos')
    def __str__(self):
        return (self.nombreProducto)

class Carrito(models.Model):
    idCarrito=models.IntegerField(primary_key=True, verbose_name="ID Carrito")
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='c_productos')
    def __str__(self):
        return (self.producto)

class Cliente(models.Model):
    idCliente=models.IntegerField(primary_key=True, verbose_name="ID Cliente")
    nombreCliente=models.CharField(max_length=30, verbose_name="Nombre Cliente")
    apellidoCliente=models.CharField(max_length=30, verbose_name="Apellido Cliente")
    correoCliente=models.CharField(max_length=420, verbose_name="Correo Cliente")
    direccionCliente=models.CharField(max_length=420, verbose_name="Dirección Cliente")
    def __str__(self):
        return (self.nombreCliente)

class Checkout(models.Model):
    carrito=models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='carrito')
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='ch_productos')
    cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente')
    def __str__(self):
        return (self.producto)


class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email