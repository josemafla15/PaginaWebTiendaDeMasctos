from django.urls import path
from . import views

urlpatterns = [
    path('paginas/<str:slug>/', views.get_pagina, name='paginas'),
    path('inicio/', views.inicio, name='inicio'),
    path('todosLosProductos/', views.verTodosLosProductos, name='todosLosProductos'),
    path('productosPerro/', views.verProductosPerro, name='productosPerro'),
    path('productosGato/', views.verProductosGato, name='productosGato'),
    path('productosPez/', views.verProductosPez, name='productosPez'),
    path('agregarAlCarrito/<int:producto_id>/', views.agregarAlCarrito, name='agregarAlCarrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]
