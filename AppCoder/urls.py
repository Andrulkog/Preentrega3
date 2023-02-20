from django.urls import path
from AppCoder import views

#views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('empleados', views.empleados, name="Empleados"),
    path('compradores', views.compradores, name="Compradores"),
    path('medicamentos', views.medicamentos, name="Medicamentos"),
    path('productoFormulario', views.productos, name="productoFormulario"),
    path('busquedaProducto', views.busquedaProducto, name="busquedaProducto"),
    path('buscar/', views.buscar),
   
]