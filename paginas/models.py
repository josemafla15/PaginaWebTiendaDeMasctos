from django.db import models



class Pagina(models.Model):
    name = models.CharField( max_length=100, verbose_name="Nombre: ")
    content = models.TextField(verbose_name="Contenido: ")
    visible = models.BooleanField(verbose_name="¿Visible?")
    slug = models.CharField(unique=True, max_length=50, verbose_name='Url amigable: ')
    created_at = models.DateField(auto_now_add = True, verbose_name="Fecha creación: ")
    edited_at = models.DateField(auto_now = True, verbose_name="Fecha edición: ")

    class Meta():
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        return self.name 


