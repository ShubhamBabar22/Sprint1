from django.urls import path
from . import views

# URL patterns for the tasks app
urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Main dashboard (default route)
    path('register/', views.register, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
    path('logout/', views.logout_view, name='logout'),  # User logout
    path('profile/', views.profile, name='profile'),  # User profile
    path('task/create/', views.task_create, name='task_create'),  # Create a new task
    path('task/<int:pk>/', views.task_detail, name='task_detail'),  # View task details
    path('task/<int:pk>/update/', views.task_update, name='task_update'),  # Update a task
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),  # Delete a task
    path('task/<int:pk>/complete/', views.task_complete, name='task_complete'),  # Mark task as complete
] 