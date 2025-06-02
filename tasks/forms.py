"""
Forms for the task management application.

This module contains form classes for user registration and task management.
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

# Custom user registration form with additional fields
class CustomUserCreationForm(UserCreationForm):
    """
    Custom user registration form that extends Django's UserCreationForm.
    Adds email and name fields to the default registration form.
    """
    email = forms.EmailField(required=False)  # Optional email field
    name = forms.CharField(max_length=100, required=False)  # Optional name field

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        """Save the user with the provided email."""
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()
        return user

# Form for creating and editing tasks
class TaskForm(forms.ModelForm):
    """
    Form for creating and editing tasks.
    Provides fields for task title, description, due date, and priority.
    """
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),  # Styled input for title
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' ', 'rows': 4}),  # Styled textarea
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': ' ', 'type': 'date'}),  # Date picker
            'priority': forms.Select(attrs={'class': 'form-select', 'placeholder': ' '}),  # Dropdown for priority
        } 