from django import forms
from .models import Estudiante, Curso

class EstudianteForm(forms.ModelForm):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), label="Curso")

    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'edad', 'curso']