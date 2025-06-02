from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils import timezone
from django.db.models import Q
from .utils import get_task_statistics

# Custom user registration form with additional fields
class CustomUserCreationForm(UserCreationForm):
    """
    Custom user registration form that extends Django's UserCreationForm.
    Adds email and name fields to the default registration form.
    """
    email = forms.EmailField(required=False)
    name = forms.CharField(max_length=100, required=False)

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
    """Form for creating and editing tasks."""
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

# Home page view (landing page)
def home(request):
    """View for the home page."""
    return render(request, 'tasks/home.html')

# Dashboard view showing user's tasks and statistics
@login_required
def dashboard(request):
    """View for the user's dashboard with task list and statistics."""
    # Get filter parameters from query string
    priority = request.GET.get('priority')
    status = request.GET.get('status')
    due_date = request.GET.get('due_date')

    # Base queryset: all tasks for the current user
    tasks = Task.objects.filter(user=request.user)

    # Apply filters if present
    if priority:
        tasks = tasks.filter(priority=priority)
    if status:
        tasks = tasks.filter(status=status)
    if due_date:
        tasks = tasks.filter(due_date=due_date)

    # Get task statistics for the user
    stats = get_task_statistics(request.user)

    context = {
        'tasks': tasks,
        'total_tasks': stats['total_tasks'],
        'completed_tasks': stats['completed_tasks'],
        'pending_tasks': stats['pending_tasks'],
        'overdue_tasks': stats['overdue_tasks'],
    }
    return render(request, 'tasks/dashboard.html', context)

# User registration view (handles GET and POST)
def register(request):
    """
    View for user registration.
    Handles both GET (display form) and POST (process registration) requests.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please login')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

# Profile page showing user info and statistics
@login_required
def profile(request):
    """View for displaying user profile and statistics."""
    stats = get_task_statistics(request.user)
    return render(request, 'tasks/profile.html', {
        'user': request.user,
        'stats': stats
    })

# Create a new task
@login_required
def task_create(request):
    """View for creating a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Create'})

# Update an existing task
@login_required
def task_update(request, pk):
    """View for updating an existing task."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Update'})

# Delete a task
@login_required
def task_delete(request, pk):
    """View for deleting a task."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('dashboard')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

# Mark a task as complete
@login_required
def task_complete(request, pk):
    """View for marking a task as complete."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.status = 'completed'
    task.save()
    messages.success(request, 'Task marked as complete!')
    return redirect('dashboard')

# View task details
@login_required
def task_detail(request, pk):
    """View for displaying task details."""
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request, 'tasks/task_detail.html', {'task': task})

# Custom logout view
def logout_view(request):
    """
    Custom logout view.
    Logs out the user and redirects to home page.
    """
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')
