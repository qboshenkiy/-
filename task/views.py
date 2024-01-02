# tasks/views.py
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    context = {'form': form}
    return render(request, 'task/add_task.html', context)

def task_list(request):
    not_started_tasks = Task.objects.filter(status='not_started').order_by('order')
    in_progress_tasks = Task.objects.filter(status='in_progress').order_by('order')
    completed_tasks = Task.objects.filter(status='completed').order_by('order')

    task_form = TaskForm()

    context = {
        'not_started_tasks': not_started_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'task_form': task_form,
    }

    return render(request, 'task/index.html', context)

def move_task(request, task_id, status):
    task = Task.objects.get(pk=task_id)
    task.status = status
    task.save()
    return redirect('task_list')
