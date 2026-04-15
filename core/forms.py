from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'role', 'password1', 'password2']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'due_date', 'assignee']