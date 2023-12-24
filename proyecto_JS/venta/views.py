from django.shortcuts import render,redirect
from venta.models import Cliente, Venta
from venta.forms import ClienteFormulario, VentaFormulario

# Create your views here.
########################################################CLIENTES
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

def BD_Cliente(request):
    BD_Cliente=Cliente.objects.all()
    return render (request, "leer_cliente.html",{"BD_Cliente": BD_Cliente})

def eliminar_cliente(request, nombre):
    cliente = Cliente.objects.get(nombre_apellido=nombre)
    cliente.delete()
    return redirect('BD_Cliente')

def editar_cliente(request, nombre_apellido):
    cliente = Cliente.objects.get(nombre_apellido=nombre_apellido)
    
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente.nombre_apellido = informacion['nombre_apellido']
            cliente.nro_cuit = informacion['nro_cuit']
            cliente.email = informacion['email']
            cliente.save()
            return render(request, "index.html")
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "editar_cliente.html", {"mi_formulario": mi_formulario})

############################################################ VENTAS
def crear_venta(request):
    form= VentaFormulario

    if request.method == "POST":
        form = VentaFormulario(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.cliente = Cliente.objects.get(pk=request.POST["cliente"])
            venta.save()
            return render(request, "index.html")
        
        else:
            print(form.errors)
    else:
        form = VentaFormulario()
  
    return render(request, 'venta_formulario.html', {'form': form})

def Lista_venta(request):
    Lista_venta=Venta.objects.all()
    return render (request, "Leer_venta.html",{"Lista_venta":Lista_venta})

