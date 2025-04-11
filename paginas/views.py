from django.shortcuts import render, redirect
from .models import Pagina
from tienda.models import Producto
from django.shortcuts import redirect, get_object_or_404
# Create your views here.

def get_pagina(request, slug):
    pagina = Pagina.objects.get(slug = slug)
    return render(request, 'paginas/pagina.html',
                  {
                      'pagina':pagina
                  })


def inicio(request):
    # request.session['carrito'] = []  # Borrar carrito al entrar
    return render(request, 'paginas/inicio.html')

def verTodosLosProductos(request):
    return render(request, 'paginas/productosTodos.html')

def verProductosPerro(request):
    return render(request,'paginas/productosPerro.html')

def verProductosGato(request):
    return render(request,'paginas/productosGato.html')

def verProductosPez(request):
    return render(request, 'paginas/productosPez.html')

def agregarAlCarrito(request, producto_id):
    print("Producto agregado al carrito:", producto_id)

    # Obtenemos el carrito como diccionario
    carrito = request.session.get('carrito', {})

    producto_id_str = str(producto_id)

    if producto_id_str in carrito:
        carrito[producto_id_str] += 1
    else:
        carrito[producto_id_str] = 1

    request.session['carrito'] = carrito
    return redirect('ver_carrito')
    

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos_carrito = []

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, pk=producto_id)
        productos_carrito.append({
            'id': producto.id,
            'nombre': producto.name,
            'descripcion': producto.description,
            'precio': producto.price,
            'imagen': producto.image,
            'cantidad': cantidad
        })

    return render(request, 'paginas/carrito.html', {'productos_carrito': productos_carrito})

    

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto_id_str = str(producto_id)

    if producto_id_str in carrito:
        if carrito[producto_id_str] > 1:
            carrito[producto_id_str] -= 1
        else:
            del carrito[producto_id_str]
        

    request.session['carrito'] = carrito
    return redirect('ver_carrito')

