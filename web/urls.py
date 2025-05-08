from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, lista_profesores, detalle_profesor , lista_cursos, crear_estudiante, index


app_name = 'web'

urlpatterns = [
    path('estudiantes/',lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/',detalle_estudiante, name='detalle_estudiante'),
    path('profesores/',lista_profesores, name='lista_profesores'),
    path('profesores/<int:pk>/',detalle_profesor, name='detalle_profesor'),
    path('cursos/', lista_cursos, name='lista_cursos'),
    path('estudiantes/crear/', crear_estudiante, name='crear_estudiante'),
    path('',index, name = 'index'),
]