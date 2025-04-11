from tienda.models import Producto, Categoria

def get_productos(request):
    
    productos = Producto.objects.filter(stock__gt=0).values_list('id', 'name', 'description', 'price', 'stock', 'image', 'categoria', 'descuento','created_at', 'edited_at')


    return {
        'productos': productos
    }

