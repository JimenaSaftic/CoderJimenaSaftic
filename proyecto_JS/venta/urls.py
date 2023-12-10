from django.urls import path
from venta.views import crear_cliente, crear_venta



urlpatterns = [
    path('crear_cliente/', crear_cliente, name='crear_cliente'),
    path('crear_venta/', crear_venta, name='crear_venta'),
]