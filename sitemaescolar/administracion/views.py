from django.shortcuts import render
from django.views.generic import ListView
from .models import Alumno
# Create your views here.
class AlumnoListView(ListView):
    model = Alumno
    template_name = 'alumno_list.html'
    context_object_name = 'alumnos'