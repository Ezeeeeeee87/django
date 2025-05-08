from django.contrib import admin
from .models import Estudiante,Profesor,Curso,Camada

# Register your models here.

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'edad')  # muestra columnas en la lista
    search_fields = ('nombre', 'apellido', 'email')          # barra de búsqueda
    list_filter = ('edad',)                                  # filtro lateral por edad
admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Camada)