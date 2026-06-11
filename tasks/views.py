from django.shortcuts import render, redirect,get_object_or_404, reverse

from tasks.models import Task
from tasks.forms import TaskForm


def tasks(request):
    if request.method == 'POST':
        id_list = request.POST.getlist('id_list')
        if id_list:
            tasks = Task.objects.filter(id__in=id_list)
            tasks.delete()
            return redirect('main')

    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)


def details(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    context = {'task': task}
    return render(request, "tasks/details.html", context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('details', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('main')
    return render(request, 'tasks/delete_task.html', {'task': task})
