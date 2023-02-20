from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre= models.CharField(max_length=40)
    codigo= models.CharField(max_length=30)
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Codigo: {self.codigo}"
    
class Comprador(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - email: {self.email} "

    
class Empleado(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email = models.EmailField()
        
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email}"
    
class Medicamento(models.Model):
    nombre=models.CharField(max_length=40)
    fechaDeVencimiento = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de Vencimiento: {self.fechaDeVencimiento} - entregado: {self.entregado}"
    

