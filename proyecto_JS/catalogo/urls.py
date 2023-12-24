from django.urls import path
from catalogo.views import crear_producto, busqueda_en_bd

urlpatterns = [
    path('crear_producto/', crear_producto, name= 'crear_producto'),
    path('busqueda_bd/', busqueda_en_bd, name='busqueda en bd'),
]