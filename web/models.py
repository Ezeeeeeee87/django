from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    email= models.EmailField()
    edad = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Profesor(models.Model):
    nombre= models.CharField(max_length=100)
    apellido= models.CharField(max_length=100)
    email= models.EmailField()
    profesion= models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.profesion}"
    

class Curso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Camada(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="camadas")
    numero = models.PositiveIntegerField()  
    estudiantes = models.ManyToManyField('Estudiante', blank=True)

    def __str__(self):
        return f"{self.curso.nombre} - Camada {self.numero}"

    def tiene_cupo(self):
        return self.estudiantes.count() < 10
