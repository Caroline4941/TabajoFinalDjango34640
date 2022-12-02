from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Estudiante, Profesor, Tareas, Examenes
from django.template import Template, Context, loader
from AppClassBook.forms import CursoForm, EstudianteForm


# Create your views here.



def inicio(request):
     return render(request,"AppClassBook/inicio.html")

def cursos(request):

     if request.method=="POST":
          form=CursoForm(request.POST)
          if form.is_valid():
               informacion=form.cleaned_data
               nombre1=informacion["nombre"]
               camada1=informacion["camada"]

               curso1=Curso(nombre=nombre1,camada=camada1)
               curso1.save()
               return render(request,"AppClassBook/inicio.html")
     else:
          formulario=CursoForm()

     return render(request,"AppClassBook/cursos.html", {"form1":formulario})

def estudiantes(request):
     if request.method=="POST":
          form=EstudianteForm(request.POST)
          if form.is_valid():
               informacion1=form.cleaned_data
               nombre2=informacion1["nombre"]
               apellido1=informacion1["apellido"]
               libreta1=informacion1["libreta"]
               email1=informacion1["email"]

               estudiante1=Estudiante(nombre=nombre2,apellido=apellido1,libreta=libreta1,email=email1)
               estudiante1.save()
               return render(request,"AppClassBook/inicio.html")
     else:
          formulario1=EstudianteForm()

     return render(request,"AppClassBook/estudiantes.html", {"form2":formulario1})

def profesores(request):
     if request.method=="POST":
          form=CursoForm(request.POST)
          if form.is_valid():
               informacion=form.cleaned_data
               nombre1=informacion["nombre"]
               camada1=informacion["camada"]

               curso1=Curso(nombre=nombre1,camada=camada1)
               curso1.save()
               return render(request,"AppClassBook/inicio.html")
     else:
          formulario=CursoForm()

     return render(request,"AppClassBook/cursos.html", {"form1":formulario})

def tareas(request):
     if request.method=="POST":
          form=CursoForm(request.POST)
          if form.is_valid():
               informacion=form.cleaned_data
               nombre1=informacion["nombre"]
               camada1=informacion["camada"]

               curso1=Curso(nombre=nombre1,camada=camada1)
               curso1.save()
               return render(request,"AppClassBook/inicio.html")
     else:
          formulario=CursoForm()

     return render(request,"AppClassBook/cursos.html", {"form1":formulario})

def examenes(request):
     if request.method=="POST":
          form=CursoForm(request.POST)
          if form.is_valid():
               informacion=form.cleaned_data
               nombre1=informacion["nombre"]
               camada1=informacion["camada"]

               curso1=Curso(nombre=nombre1,camada=camada1)
               curso1.save()
               return render(request,"AppClassBook/inicio.html")
     else:
          formulario=CursoForm()

     return render(request,"AppClassBook/cursos.html", {"form1":formulario})







