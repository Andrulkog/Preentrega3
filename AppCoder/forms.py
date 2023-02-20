from django import forms


class ProductoFormulario(forms.Form):
    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class EmpleadoFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class PruebaFormulario(forms.Form):
    Cliente = forms.CharField(max_length = 200)
    Campaña = forms.CharField(max_length = 200)