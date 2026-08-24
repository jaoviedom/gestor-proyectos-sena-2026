from django.db import models

class Proyecto(models.Model):
  '''
  Modelo que representa un proyecto
  '''
  nombre = models.CharField(max_length=100) # Campo de texto (varchar)
  descripcion = models.TextField() # Campo de texto largo
  duracion = models.IntegerField() # Campo numérico entero

class Tarea(models.Model):
  '''
  Modelo que representa una tarea de un proyecto
  '''

  PRIORIDAD_CHOICES = [
    ('BAJA', 'Baja'),
    ('MEDIA', 'Media'),
    ('ALTA', 'Alta'),
  ]

  ESTADO_CHOICES = [
    ('PENDIENTE', 'Pendiente'),
    ('EN_PROGRESO', 'En Progreso'),
    ('COMPLETADA', 'Completada'),
  ]

  # Relación 1 a muchos: Un proyecto tiene muchas tareas
  proyecto = models.ForeignKey(
    Proyecto,
    on_delete=models.CASCADE,
    related_name='tareas'
  )
  titulo = models.CharField(max_length=50)
  prioridad = models.CharField(
    max_length=5,
    choices=PRIORIDAD_CHOICES,
    default='MEDIA'
  )
  estado = models.CharField(
    max_length=11,
    choices=ESTADO_CHOICES,
    default='PENDIENTE'
  )