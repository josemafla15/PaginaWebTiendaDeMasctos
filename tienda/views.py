from django.shortcuts import render

from .models import Producto, Categoria

def productos_perros(request):
    categoria_perros = Categoria.objects.filter(name="Alimento para perro").first()
    productos = Producto.objects.filter(categoria=categoria_perros)

    return render(request, 'productos_perros.html', {'productos': productos})