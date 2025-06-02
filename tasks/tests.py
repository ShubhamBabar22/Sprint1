"""
Test cases for the task management application.

This module contains test cases for models, views, and forms.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task
from .forms import TaskForm, CustomUserCreationForm

class TaskModelTest(TestCase):
    """
    Test cases for the Task model.
    Tests task creation, string representation, and default values.
    """
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            user=self.user
        )

    def test_task_creation(self):
        """Test that a task can be created with required fields."""
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertEqual(self.task.user, self.user)
        self.assertEqual(self.task.status, 'pending')

    def test_task_str(self):
        """Test the string representation of a task."""
        self.assertEqual(str(self.task), 'Test Task')

class TaskFormTest(TestCase):
    """
    Test cases for the TaskForm.
    Tests form validation and field requirements.
    """
    def test_task_form_valid(self):
        """Test that the form is valid with required fields."""
        form_data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'priority': 'medium'
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        """Test that the form is invalid without required fields."""
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

class CustomUserCreationFormTest(TestCase):
    """
    Test cases for the CustomUserCreationForm.
    Tests user registration form validation and field requirements.
    """
    def test_user_form_valid(self):
        """Test that the form is valid with required fields."""
        form_data = {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'email': 'test@example.com'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_user_form_invalid(self):
        """Test that the form is invalid without required fields."""
        form = CustomUserCreationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)
        self.assertIn('password2', form.errors)
