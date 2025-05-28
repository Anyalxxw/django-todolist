from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('taskslist/', views.task_list, name='taskslist'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
]

