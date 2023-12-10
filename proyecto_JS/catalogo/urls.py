from django.urls import path
from catalogo.views import crear_producto

urlpatterns = [
    path('crear_producto/', crear_producto, name= 'crear_producto')
]