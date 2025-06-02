from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# The Task model represents a to-do item or task for a user
class Task(models.Model):
    """
    Task model for storing user tasks.
    
    Attributes:
        PRIORITY_CHOICES: Available priority levels for tasks
        STATUS_CHOICES: Available status options for tasks
        title: The title of the task
        description: Detailed description of the task
        created_date: When the task was created
        due_date: When the task is due
        priority: Task priority level (low/medium/high)
        status: Current status of the task (pending/completed)
        user: Foreign key to the User who owns the task
    """
    
    # Priority choices for tasks (used in the priority field)
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    # Status choices for tasks (used in the status field)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    
    # Task fields
    title = models.CharField(max_length=100)  # Short title for the task
    description = models.TextField(blank=True)  # Optional detailed description
    created_date = models.DateTimeField(default=timezone.now)  # When the task was created
    due_date = models.DateField(null=True, blank=True)  # Optional due date
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')  # Priority level
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # Task status
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who owns this task

    def __str__(self):
        """String representation of the task (shows the title in admin and shell)."""
        return self.title

    class Meta:
        """Meta options for the Task model."""
        ordering = ['-created_date']  # Order tasks by creation date, newest first
