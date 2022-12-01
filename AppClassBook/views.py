from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from django.template import Template, Context, loader
# Create your views here.

def curso(request):

    matematicas=Curso(nombre="MatematicasII",camada=123456)
    matematicas.save()

    return render(request, "AppClassBook/curso.html")

def inicio(request):
     return render(request,"AppClassBook/inicio.html")

def cursos(request):
     return render(request,"AppClassBook/cursos.html")

def estudiantes(request):
     return render(request,"AppClassBook/estudiantes.html")

def profesores(request):
     return render(request,"AppClassBook/profesores.html")

def tareas(request):
     return render(request,"AppClassBook/tareas.html")

def examenes(request):
     return render(request,"AppClassBook/examenes.html")







