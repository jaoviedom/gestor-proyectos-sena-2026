from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Proyecto, Tarea

def home(request):
  return render(request, 'home.html')

def mostrar_proyectos(request):
  proyectos = Proyecto.objects.all()
  return render(request, 'proyectos.html', {'proyectos': proyectos})

def nuevos_registros(request):
  Proyecto.objects.create(nombre="Aplicación bancaria", descripcion="Aplicación web gestionar cuentas bancarias", duracion=1000)
  
  return HttpResponse("Registros guardados.")

def ver_proyecto(request, id):
  proyecto = Proyecto.objects.get(id=id)
  print(proyecto.tareas)
  return render(request,'detalle-proyecto.html', {'proyecto': proyecto})

def nuevo_proyecto(request):
  if request.method == "POST":
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    duracion = request.POST.get('duracion')

    if nombre and descripcion and duracion:
      proyecto = Proyecto(
        nombre=nombre,
        descripcion=descripcion,
        duracion=duracion
      )
      proyecto.save()
    
      return redirect('proyectos')

  return render(request, 'nuevo-proyecto.html')

def eliminar_proyecto(request, id):
  proyecto = Proyecto.objects.get(id=id)
  proyecto.delete()
  return redirect('proyectos')

def editar_proyecto(request, id):
  proyecto = Proyecto.objects.get(id=id)

  if request.method == "POST":
    nombre = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    duracion = request.POST.get('duracion')

    if nombre and descripcion and duracion:
      proyecto.nombre = nombre
      proyecto.descripcion = descripcion
      proyecto.duracion = int(duracion)
      proyecto.save()

      return redirect('ver_proyecto', id=proyecto.id)

  return render(request, 'editar-proyecto.html', {'proyecto': proyecto})

def crear_tarea(request, proyecto_id):
  proyecto = get_object_or_404(Proyecto, id=proyecto_id)

  if request.method == "POST":
    titulo = request.POST.get('titulo')
    prioridad = request.POST.get('prioridad')
    estado = request.POST.get('estado')
    if titulo and prioridad and estado:
      Tarea.objects.create(
        proyecto=proyecto,
        titulo=titulo,
        prioridad=prioridad,
        estado=estado
      )

      return redirect('ver_proyecto', id=proyecto_id)

  datos = {
    'proyecto': proyecto,
    'prioridad_choices': Tarea.PRIORIDAD_CHOICES,
    'estado_choices': Tarea.ESTADO_CHOICES
  }

  return render(request, 'crear-tarea.html', datos)
