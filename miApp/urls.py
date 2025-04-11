from django.urls import path
from . import views
from paginas import views as paginas_views

urlpatterns = [
    
    path('', paginas_views.inicio, name='index' )
    
]
