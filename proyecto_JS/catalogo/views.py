from django.shortcuts import render
from catalogo.models import Producto
from catalogo.forms import productoFormulario


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
    
    return render(request, 'producto_formulario.html')from django.shortcuts import render

# Create your views here.
