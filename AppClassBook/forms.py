from django import forms

class CursoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    camada=forms.IntegerField()

class EstudianteForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    libreta=forms.IntegerField()
    email=forms.EmailField()


class ProfesorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
