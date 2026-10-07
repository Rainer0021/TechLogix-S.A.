from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de Categoría")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre de Producto")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock")
    sku = models.CharField(max_length=50, unique=True, verbose_name="SKU")
    fecha_ingreso = models.DateField(auto_now_add=True, verbose_name="Fecha de Ingreso")

    def __str__(self):
        return f"{self.nombre} ({self.sku})"