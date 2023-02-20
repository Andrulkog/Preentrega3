from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import ProductoFormulario, EmpleadoFormulario, MedicamentosFormulario


# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')
  
 
def empleados(request):
    if request.method == 'POST':
        miFormulario = EmpleadoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empleado = Empleado(nombre=informacion['nombre'], apellido=informacion['apellido'], 
                                email=informacion['email'],)
            empleado.save()
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario = EmpleadoFormulario()
        
    return render(request, "AppCoder/empleados.html", {"miFormulario":miFormulario})        

def medicamentos(request):
    if request.method == 'POST':
        miFormulario = MedicamentosFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            medicamento = Medicamento(nombre=informacion['nombre'], fechaDeVencimiento=informacion['fechaDeVencimiento'], 
                                entregado=informacion['entregado'],)
            medicamento.save()
            return render(request, "AppCoder/inicio.html")  
        
    else:
        miFormulario = MedicamentosFormulario()
        
    return render(request, "AppCoder/medicamentos.html", {"miFormulario":miFormulario}) 


def compradores(request):
    return render(request, 'AppCoder/compradores.html')
    

def productos(request):
    if request.method == 'POST':
        miFormulario = ProductoFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            producto = Producto(nombre=informacion['nombre'], codigo=informacion['codigo'])
            producto.save()
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario = ProductoFormulario()
        
    return render(request, "AppCoder/productos.html", {"miFormulario":miFormulario})        

def buscarproducto(request):
    query = request.GET.get('codigo')
    if query is not None:
        resultados = Producto.objects.filter(codigo__icontains=query)
    else:
        resultados = []
    return render(request, 'AppCoder/busquedaProducto.html', {'resultados': resultados})




"""
def busquedaProducto(request):
    return render(request, "AppCoder/busquedaProducto.html")

def buscar(request):
    if request.GET["codigo"]:
        codigo = request.GET['codigo']
        producto = Producto.objects.filter(codigo__icontains=codigo)
        return render(request, "AppCoder/resultadoBusqueda.html", {"producto":producto, "codigo":codigo})
        
    else:
        respuesta = "No se ingresaron datos" 

        
    return HttpResponse(respuesta) """
