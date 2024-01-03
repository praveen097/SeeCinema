# myapp/forms.py
from django import forms
from .models import Theatre

class TheatreForm(forms.ModelForm):
    class Meta:
        model = Theatre
        fields = '__all__'  # You can specify the fields you want to include if needed
