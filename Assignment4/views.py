from django.shortcuts import render
from django.shortcuts import redirect
from .forms import TaskForm
from .models import Todo
import datetime
# Create your views here.

def index(request):
    tasks = Todo.objects.all()
    form = TaskForm(request.POST or None)

    context = {'tasks' : tasks, 'form' : form}
    return render(request, 'index.html', context)

def add(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        return render(request, 'index.html', {'form':form})
def delete(request,id):
    task = Todo.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'delete.html', {'task': task})
def update(request,id):
    task = Todo.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'update.html', {'form': form})
def complete_task(request, id):
    task = Todo.objects.get(id=id)
    task.completed = True
    task.save()
    return redirect('index')
