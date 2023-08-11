from django.shortcuts import render, redirect
from .forms import AddTaskForm

def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')  # Redirect to 'show_tasks' page
    else:
        form = AddTaskForm()
    return render(request, 'add_task.html', {'form': form})
  
from django.shortcuts import render
from .models import TaskModel

def show_tasks(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})






from django.shortcuts import redirect
from .models import TaskModel

def delete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.delete()
    return redirect('show_tasks')
  
  

from django.shortcuts import render, redirect
from .forms import AddTaskForm
from .models import TaskModel

def edit_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
    else:
        form = AddTaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})
  

from django.shortcuts import redirect
from .models import TaskModel

def complete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.is_completed = True
    task.save()
    return redirect('completed_tasks')
  

def completed_tasks(request):
    completed_tasks = TaskModel.objects.filter(is_completed=True)
    return render(request, 'completed_tasks.html', {'completed_tasks': completed_tasks})
  

def complete_task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    task.is_completed = True
    task.save()
    return redirect('show_tasks') 
  
  
