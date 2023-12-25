from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'director', 'is_published', 'release_date', 'total_time_minutes', 'poster']

    widgets = {
        'release_date': forms.DateInput(attrs={'type': 'date'}),
    }
