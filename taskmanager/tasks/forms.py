from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('created_on', 'updated_on', 'created_by', 'updated_by')