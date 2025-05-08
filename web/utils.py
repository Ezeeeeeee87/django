from .models import Curso, Camada, Estudiante
from django.db.models import Count, Max

def asignar_estudiante_a_curso(estudiante, curso):
    # Buscar camada con cupo disponible
    camada_disponible = curso.camadas.annotate(
        cantidad=Count('estudiantes')
    ).filter(cantidad__lt=30).first()

    if not camada_disponible:
        # Obtener el número de camada siguiente
        ultimo_numero = curso.camadas.aggregate(Max('numero'))['numero__max'] or 0
        camada_disponible = Camada.objects.create(curso=curso, numero=ultimo_numero + 1)

    camada_disponible.estudiantes.add(estudiante)
    return camada_disponible