from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('show_tasks/', views.show_tasks, name='show_tasks'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),  
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('completed_tasks/', views.completed_tasks, name='completed_tasks'),
    
]

