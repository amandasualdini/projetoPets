from django import forms
from pets.models import petEncontrado

class petEncontradoForm(forms.ModelForm):
    class Meta:
        model = petEncontrado
        fields = ['id', 'Nome', 'Raca']