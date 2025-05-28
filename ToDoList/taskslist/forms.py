from django import forms
from . import models


class CreateTask(forms.ModelForm):
    class Meta():
        model = models.Task
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'title-input',
                'placeholder': 'Write a task...'
            })
        }