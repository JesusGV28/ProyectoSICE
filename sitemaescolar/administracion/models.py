from django.db.models import ManyToManyField
from django.db import models

# Create your models here.
class Horario(models.Model):
    grupo=models.ForeignKey('Grupo', on_delete=models.CASCADE,related_name='horario_grupos')
    dia_semana = models.CharField(max_length=10, help_text="Dia de la semana")
    hora_inicio = models.TimeField(help_text="Hora de inicio")
    hora_fin = models.TimeField(help_text="Hora de fin")
    aula = models.CharField(max_length=25, help_text="Aula o salon")

    def __str__(self):
        return f"{self.dia_semana} {self.hora_inicio} - {self.hora_fin} ({self.aula})"


class Profesor(models.Model):
    rfc = models.CharField(max_length=13, primary_key=True,serialize=True)
    nombre = models.CharField(max_length=100, help_text="Nombre del profesor")
    apellidos = models.CharField(max_length=100, help_text="Apellidos del profesor")
    correo = models.EmailField(help_text="Correo electronico del profesor")

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.rfc})"


class Carrera(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True,serialize=True)
    nombre = models.CharField(max_length=100, help_text="Nombre de la carrera")
    creditos = models.IntegerField(help_text="Creditos de la carrera")
    duracion_semestral = models.IntegerField(help_text="Duracion semestral de la carrera")
    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Materia(models.Model):
    carreras=ManyToManyField(Carrera,related_name='materias')
    codigo=models.CharField(max_length=10, primary_key=True,serialize=True)
    nombre=models.CharField(max_length=100, help_text="Nombre de la materia")
    creditos=models.IntegerField(help_text="Creditos de la materia")
    unidades=models.IntegerField(help_text="Unidades de la materia")

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"

class Grupo(models.Model):
    profesor=models.ForeignKey('Profesor', on_delete=models.SET_NULL,null=True,related_name='grupos')
    materia=models.ForeignKey('Materia', on_delete=models.CASCADE,related_name='grupos')
    codigo=models.CharField(max_length=10, primary_key=True,serialize=True)
    cupo=models.IntegerField(help_text="Cupo del grupo")
    num_alumnos=models.IntegerField(help_text="Numero de alumnos")
    def __str__(self):
        return f"Grupo {self.codigo} - {self.materia.nombre}"

class Alumno(models.Model):
    matricula=models.CharField(max_length=10, primary_key=True,serialize=True)
    nombre=models.CharField(max_length=100, help_text="Nombre del alumno")
    apellidos=models.CharField(max_length=100, help_text="Apellidos del alumno")
    correo=models.EmailField(help_text="Correo electronico del alumno")
    semestre=models.IntegerField(help_text="Semestre del alumno")
    STATUS=[
        ('Aspirante','Aspirante'),
        ('Estudiante','Estudiante'),
    ]
    status=models.CharField(max_length=15, choices=STATUS, default='Aspirante', help_text="Estado del alumno")
    grupos = models.ManyToManyField('Grupo', through='Calificacion', related_name='alumnos')
    carrera = models.ForeignKey('Carrera', on_delete=models.SET_NULL, null=True, related_name='alumnos')



    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.matricula})"

class Calificacion(models.Model):
    alumno=models.ForeignKey('Alumno', on_delete=models.CASCADE,related_name='calificaciones')
    grupo=models.ForeignKey('Grupo', on_delete=models.CASCADE,related_name='calificaciones')
    calificacion_final=models.FloatField(help_text="Calificacion del alumno")
    fecha_registro = models.DateTimeField(auto_now_add=True, help_text="Fecha de registro")
    def __str__(self):
        return f"{self.alumno.nombre} - Grupo {self.grupo.codigo}: {self.calificacion_final}"

    
    
    


    
    
