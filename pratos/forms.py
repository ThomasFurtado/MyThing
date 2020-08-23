from django import forms
from .models import Choice

class AddForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'
