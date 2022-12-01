from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    camada=models.IntegerField()

    def __str__(self):
        return self.nombre+" "+str(self.camada)

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    libreta=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.nombre+" "+self.apellido

class Tareas(models.Model):
    titulo=models.CharField(max_length=50)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
    def __str__(self):
        return self.titulo+" "+str(self.fechaDeEntrega)

class Examenes(models.Model):
    titulo=models.CharField(max_length=50)
    nota=models.IntegerField()

def __str__(self):
        return self.titulo+" "+str(self.nota)

