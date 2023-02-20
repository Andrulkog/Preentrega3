from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import ProductoFormulario, EmpleadoFormulario, MedicamentosFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
        
    return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})        

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
        
    return render(request, "AppCoder/entregables.html", {"miFormulario":miFormulario}) 


def compradores(request):
    return render(request, 'AppCoder/estudiantes.html')
    #return HttpResponse('vista estudiantes')

def prueba(request):
    return render(request, 'AppCoder/prueba.html')

"""def medicamentos(request):
    return render(request, 'AppCoder/entregables.html')
    #return HttpResponse('vista entregables') """

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
        
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})        


def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        cursos = Producto.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultadoBusqueda.html", {"cursos":cursos, "camada":camada})
        #return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta = "No enviaste datos" 

        
    return HttpResponse(respuesta)
    
"""    
def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)
    
def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    profesor = Profesor.objects.all()
    contexto= {"profesores":profesores}
    return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre =profesor_nombre)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido'] 
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            
            profesor.save()
            
            return render(request, "AppCoder/inicio.html")
        
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre, 
                                                   'apellido':profesor.apellido, 
                                                   'email':profesor.email, 
                                                   'profesion': profesor.profesion})
        
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})        

class CursoList(ListView):
    model = Curso
    template_name = "AppCoder/cursos_list.html"
    
class CursoDetalle(DetailView):
    model = Curso
    template_name = "AppCoder/curso_detalle.html"
    
class CursoCreacion(CreateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    fields = ['nombre', 'camada']  
    
class CursoDelete(DeleteView):
    model = Curso
    success_url = "/AppCoder/curso/list"

def prueba(request):
    context ={}
    context['form']= PruebaFormulario()
    return render(request, "prueba.html", context)
    """