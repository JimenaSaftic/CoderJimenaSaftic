from django import forms

class ClienteFormulario(forms.Form):
    nombre_apellido = forms.CharField()
    nro_cuit = forms.IntegerField()
    email = forms.EmailField()

class VentaFormulario(forms.Form):
    cliente = forms.CharField()
    nro_factura = forms.IntegerField()
    producto = forms.CharField()
    cantidad = forms.IntegerField()