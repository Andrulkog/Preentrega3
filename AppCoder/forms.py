from django import forms


class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    codigo = forms.IntegerField()
    
class EmpleadoFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email = forms.EmailField()
    

class MedicamentosFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    fechaDeVencimiento = forms.DateField()
    entregado = forms.BooleanField()