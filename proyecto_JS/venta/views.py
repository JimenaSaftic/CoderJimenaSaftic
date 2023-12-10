from django.shortcuts import render
from venta.models import Cliente, Venta
from venta.forms import ClienteFormulario, VentaFormulario

# Create your views here.

def crear_cliente(request):
    print("Mostrar request.post:")
    print(request.POST)

    if request.method == "POST":
        nuevo_cliente = Cliente(
                nombre_apellido=request.POST["nombre"],
                nro_cuit= request.POST["nro_cuit"],
                email=request.POST["email"]
                )
        nuevo_cliente.save()
        return render(request, "index.html")
  
    return render(request,'cliente_formulario.html')

def crear_venta(request):
    print("Mostrar request.post:")
    print(request.POST)

    if request.method == "POST":
        nueva_venta= Venta(
                cliente= request.POST["nombre"],
                nro_factura= request.POST["nro_factura"],
                producto=request.POST["producto"],
                cantidad= request.POST["cantidad"],
                )
        nueva_venta.save()
        return render(request, "index.html")
  
    return render(request, 'venta_formulario.html')