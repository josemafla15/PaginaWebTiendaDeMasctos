from .models import Pagina



def get_paginas(request):
    paginas = Pagina.objects.filter(visible=True).values_list('id', 'name', 'slug', 'content')

    return {
        'paginas': paginas
    }


