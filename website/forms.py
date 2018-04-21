from django import forms
from django.forms import ModelForm
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['biggest_problem', 'email_contact']
        widgets = {
            'biggest_problem': forms.TextInput(attrs={'size': '100',}),
        }
        labels = {
            'biggest_problem': 'What is your biggest problem that you think data could solve?',
        }