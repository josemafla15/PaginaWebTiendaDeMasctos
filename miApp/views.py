from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, ('miApp/index.html'),
                  {'titulo':'Inicio'}
                  )