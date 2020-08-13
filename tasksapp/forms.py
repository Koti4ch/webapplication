from django import forms
from django.conf import settings
from .models import Task


class createNewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
