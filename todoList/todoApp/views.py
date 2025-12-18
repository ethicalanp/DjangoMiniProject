from django.shortcuts import render,redirect
from .models import todo

# Create your views here.

def todo_list(request):
    todos=todo.objects.all()
    if request.method=="POST":
        task = request.POST.get('task')
        if task:
            todo.objects.create(task=task)
        return redirect ('todo_list')
    return render(request,'index.html',{'todos':todos})

def complete(request,todo_id):
    Todo = todo.objects.get(id=todo_id)
    Todo.complete = True
    Todo.save()
    return redirect('todo_list')

def delete(request,todo_id):
    Todo=todo.objects.get(id=todo_id)
    Todo.delete()
    return redirect('todo_list')

def edit(request,todo_id):
    Todo = todo.objects.get(id=todo_id)
    if request.method=='POST':
        task = request.POST.get('task')
        if task:
            Todo.task = task
            Todo.save()
        return redirect('todo_list')
    return render(request,'index.html',{'todo':Todo,'edit_mode':True,'todos':todo.objects.all()})


