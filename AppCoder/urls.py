from django.urls import path
from AppCoder import views
#from AppCoder import curso
#views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    #path('cursos', views.cursos, name="Cursos"),
    path('prueba', views.prueba, name="Prueba"),
    path('empleados', views.empleados, name="Empleados"),
    path('compradores', views.compradores, name="Compradores"),
    path('medicamentos', views.medicamentos, name="Medicamentos"),
    path('productoFormulario', views.productos, name="productoFormulario"),
    path('busquedaCamada', views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
   # path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
   # path('eliminarProfesor/<profesor_nombre>/', views.eliminarProfesor, name="EliminarProfesor"),
   # path('editarProfesor/<profesor_nombre>/', views.editarProfesor, name="EditarProfesor"),
    
   # path('curso/list', views.CursoList.as_view(), name='List'),
   # path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
   # path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
   # path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
   # path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
]