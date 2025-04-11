from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre: ")
    description = models.TextField(verbose_name="Descripción: ")
    created_at = models.DateField(auto_now_add = True, verbose_name="Fecha creación: ")
    edited_at = models.DateField(auto_now = True, verbose_name="Fecha edición: ")

    class Meta():
        verbose_name = 'Categoría'  
        verbose_name_plural = 'Categorías'
    
    def __str__(self):
        return self.name

class Producto(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre: ")    
    description = models.TextField(verbose_name="Descripción: ")
    price = models.IntegerField( verbose_name="Precio: ")
    stock = models.IntegerField(verbose_name="Stock: ")
    image = models.ImageField(default='null',upload_to='productos/', verbose_name="Imagen: ")
    categoria = models.ForeignKey(Categoria, verbose_name="Categoría: ", on_delete=models.CASCADE)
    descuento = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add = True, verbose_name="Fecha creación: ")
    edited_at = models.DateField(auto_now = True, verbose_name="Fecha edición: ")


    class Meta():
        verbose_name = 'Producto'  
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.name