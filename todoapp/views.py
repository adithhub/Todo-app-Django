from django.shortcuts import render, get_object_or_404, redirect
from .models import Task

def task_view(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        if name and desc and priority:
            obj = Task(name=name, desc=desc, priority=priority, date=date)
            obj.save()
    return render(request, 'task_view.html', {'obj1': obj1})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_view')  # Assuming 'task_view' is the name of the URL pattern for your task list view
    return render(request, 'delete_task.html', {'task': task})
