from django.contrib import admin
from .models import Profesor, Alumno, Grupo, Materia, Carrera, Horario, Calificacion
# Register your models here.
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Grupo)
admin.site.register(Materia)
admin.site.register(Carrera)
admin.site.register(Horario)
admin.site.register(Calificacion)
