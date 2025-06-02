"""
Utility functions for the task management application.

This module contains utility functions for working with tasks and related data.
"""

from django.utils import timezone
from datetime import timedelta
from .models import Task

# Get all overdue tasks for a user (due date in the past and not completed)
def get_overdue_tasks(user):
    """
    Get all overdue tasks for a user.
    Args:
        user: The user to get overdue tasks for
    Returns:
        QuerySet: A queryset of overdue tasks
    """
    return Task.objects.filter(
        user=user,
        status__in=['pending', 'in_progress'],
        due_date__lt=timezone.now()
    )

# Get tasks due in the next specified number of days
def get_upcoming_tasks(user, days=7):
    """
    Get tasks due in the next specified number of days.
    Args:
        user: The user to get upcoming tasks for
        days: Number of days to look ahead (default: 7)
    Returns:
        QuerySet: A queryset of upcoming tasks
    """
    return Task.objects.filter(
        user=user,
        status__in=['pending', 'in_progress'],
        due_date__range=[
            timezone.now(),
            timezone.now() + timedelta(days=days)
        ]
    )

# Calculate task statistics for a user (total, completed, pending, overdue, completion rate)
def get_task_statistics(user):
    """
    Calculate task statistics for a user.
    Args:
        user: The user to calculate statistics for
    Returns:
        dict: Dictionary containing task statistics
    """
    today = timezone.now().date()
    
    # Get all tasks for the user
    tasks = Task.objects.filter(user=user)
    
    # Calculate statistics
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='completed').count()
    pending_tasks = tasks.filter(status__in=['pending', 'in_progress']).count()
    overdue_tasks = tasks.filter(
        due_date__lt=today,
        status__in=['pending', 'in_progress']
    ).count()
    
    # Calculate completion rate
    if total_tasks > 0:
        completion_rate = int((completed_tasks / total_tasks) * 100)
    else:
        completion_rate = 0
    
    return {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
        'completion_rate': completion_rate,
    }

# Format a duration value into a human-readable string (minutes, hours, days)
def format_duration(duration, unit):
    """
    Format a duration into a human-readable string.
    Args:
        duration: The duration value
        unit: The unit of duration (minutes, hours, days)
    Returns:
        str: A formatted duration string
    """
    if unit == 'minutes':
        if duration < 60:
            return f'{duration} minutes'
        hours = duration // 60
        minutes = duration % 60
        return f'{hours} hours {minutes} minutes'
    elif unit == 'hours':
        if duration < 24:
            return f'{duration} hours'
        days = duration // 24
        hours = duration % 24
        return f'{days} days {hours} hours'
    else:  # days
        return f'{duration} days'

# Get a summary of a user's tasks (statistics, overdue, upcoming)
def get_task_summary(user):
    """
    Get a summary of a user's tasks.
    Args:
        user: The user to get the summary for
    Returns:
        dict: A dictionary containing task summary information
    """
    return {
        'statistics': get_task_statistics(user),
        'overdue_tasks': get_overdue_tasks(user),
        'upcoming_tasks': get_upcoming_tasks(user),
    } 