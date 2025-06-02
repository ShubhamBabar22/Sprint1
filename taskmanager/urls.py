"""
URL configuration for taskmanager project.

This module defines the URL patterns for the task manager application.
Each URL pattern maps to a specific view function or class.
"""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from tasks import views

# List of URL patterns for the project
urlpatterns = [
    # Core pages
    path('', views.home, name='home'),  # Home page (landing page)
    path('dashboard/', views.dashboard, name='dashboard'),  # User dashboard (main task list)
    path('profile/', views.profile, name='profile'),  # User profile page
    
    # Authentication
    path('register/', views.register, name='register'),  # User registration page
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),  # User login page
    path('logout/', views.logout_view, name='logout'),  # User logout (custom view)

    # Task management URLs
    path('task/create/', views.task_create, name='task_create'),  # Create a new task
    path('task/<int:pk>/', views.task_detail, name='task_detail'),  # View task details
    path('task/<int:pk>/update/', views.task_update, name='task_update'),  # Update a task
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),  # Delete a task
    path('task/<int:pk>/complete/', views.task_complete, name='task_complete'),  # Mark task as complete
]
