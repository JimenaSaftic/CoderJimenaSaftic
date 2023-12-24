from django.urls import path
from venta.views import crear_cliente, BD_Cliente, eliminar_cliente, editar_cliente, crear_venta, Lista_venta


urlpatterns = [
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('BD_Cliente/', BD_Cliente, name='BD_Cliente'),
    path('crear_venta/', crear_venta, name='crear_venta'),
    path('eliminar_cliente/<nombre>', eliminar_cliente, name='eliminar_cliente'),
    path('editar_cliente/<nombre_apellido>', editar_cliente, name='editar_cliente'),
    path('Lista_venta/', Lista_venta, name="Lista_venta"),
]