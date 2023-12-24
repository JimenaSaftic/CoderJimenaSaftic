from django.shortcuts import render, redirect
from catalogo.models import Producto
from catalogo.forms import productoFormulario
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def crear_producto(request): 
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_producto = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            cantidad_en_stock = request.POST["cantidad_en_stock"]
        )
        nuevo_producto.save()
        return render(request, "index.html")
    
    return render(request, 'producto_formulario.html')

def busqueda_en_bd(request):
    if request.GET.get("nombre", False): 
        busqueda = request.GET["nombre"]
        lista_productos = Producto.objects.filter(nombre__icontains=busqueda)
        
        return render(request, 'busqueda.html', {'lista': lista_productos})
    
    return render(request, 'busqueda.html')

def eliminar_producto(request, nombre):
    producto = Producto.objects.get(producto=nombre)
    producto.delete()
    return redirect ('busqueda_en_bd')