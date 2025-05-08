from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    contexto = {
        'estudiantes' : estudiantes
    }
    return render(request, 'web/estudiantes_list.html', contexto)

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request,'web/estudiante_detail.html', {'estudiante' : estudiante})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    contexto = {
        'profesores' : profesores
    }
    return render(request, 'web/profesores_list.html', contexto)

def detalle_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    return render(request,'web/profesor_detail.html', {'profesor' : profesor})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'web/cursos_list.html', {'cursos': cursos})