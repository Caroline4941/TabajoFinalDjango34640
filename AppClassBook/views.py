from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Estudiante, Profesor
from django.template import Template, Context, loader
from AppClassBook.forms import CursoForm, EstudianteForm, ProfesorForm


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
          form=ProfesorForm(request.POST)
          if form.is_valid():
               informacion2=form.cleaned_data
               nombre3=informacion2["nombre"]
               apellido2=informacion2["apellido"]
               email2=informacion2["email"]

               profesor1=Profesor(nombre=nombre3,apellido=apellido2,email=email2)
               profesor1.save()
               return render(request,"AppClassBook/inicio.html")
     else:
          formulario=ProfesorForm()

     return render(request,"AppClassBook/profesores.html", {"form3":formulario})


def BusquedaEstudiante(request):
     return render(request, "AppClassBook/BusquedaEstudiante.html")

def buscar(request):

     if request.GET["libreta"]:
          libreta=request.GET['libreta']
          estudiantes=Estudiante.objects.filter(libreta__icontains=libreta)
          return render(request, "AppClassBook/ResultadoBusquedaEst.html", {"estudiantes":estudiantes, "libreta":libreta })

     else:
          respuesta="No enviaste datos"
     return HttpResponse(respuesta) 








