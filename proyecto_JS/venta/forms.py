from django import forms
from .models import Venta

class ClienteFormulario(forms.Form):
    nombre_apellido = forms.CharField()
    nro_cuit = forms.IntegerField()
    email = forms.EmailField()

class VentaFormulario(forms.ModelForm):
    class Meta:
        model= Venta
        fields=['cliente', 'nro_factura', 'producto', 'cantidad']