from django import forms

class productoFormulario(forms.Form):
    nombre = forms.CharField()
    descripcion = forms.CharField()
    cantidad_en_stock = forms.IntegerField()