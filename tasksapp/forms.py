from django import forms
from django.conf import settings
from .models import Task


class createNewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('task_title', 'task_msg',)

        widgets = {
            'task_title': forms.TextInput(attrs={'class': "standart_form--input", "autocomplete": "off"}),
            'task_msg': forms.TextInput(attrs={'class': "standart_form--input", "autocomplete": "off"}),
        }
