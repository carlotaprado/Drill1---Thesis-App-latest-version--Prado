from django import forms
from .models import Thesis

class ThesisForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = ['title', 'author', 'abstract', 'year']
