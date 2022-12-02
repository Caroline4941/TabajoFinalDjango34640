from django import forms

class CursoForm(forms.Form):
    nombre=forms.CharField(max_length=70)
    camada=forms.IntegerField