from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Profesor, Curso, Camada
from .forms import EstudianteForm
from django.db.models import Count, Max

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

def crear_estudiante(request):
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.save()
            curso_id = request.POST.get("curso")
            curso = Curso.objects.get(pk=curso_id)
            asignar_estudiante_a_curso(estudiante, curso)
            return redirect("web:lista_estudiantes")
    else:
        form = EstudianteForm()

    cursos = Curso.objects.all()
    return render(request, "web/crear_estudiante.html", {"form": form, "cursos": cursos})

def asignar_estudiante_a_curso(estudiante, curso):
    # Buscar camada con cupo disponible
    camada_disponible = curso.camadas.annotate(
        cantidad=Count('estudiantes')
    ).filter(cantidad__lt=5).first()

    if not camada_disponible:
        # Obtener el número de camada siguiente
        ultimo_numero = curso.camadas.aggregate(Max('numero'))['numero__max'] or 0
        camada_disponible = Camada.objects.create(curso=curso, numero=ultimo_numero + 1)

    camada_disponible.estudiantes.add(estudiante)
    return camada_disponible