from django.contrib import admin
from .models import *

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Examenes)
admin.site.register(Tareas)

# Register your models here.
