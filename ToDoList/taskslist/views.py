from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import CreateTask

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('date')
    
    if request.method == 'POST':
        form = CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:taskslist')
    else:
            form = CreateTask()
    return render(request, 'taskslist/tasks_list.html', {
        'tasks': tasks,
        'form': form
    })
    
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:taskslist')
    return redirect('tasks:taskslist')
    
    