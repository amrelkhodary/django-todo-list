from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Task

class AddTaskForm(forms.Form):
    title = forms.CharField(max_length= 256)


def index(request):
    current_active_user = request.session['user']['username']

    if request.method == "POST":
        #write code to get data from request
        #add data to database 
        title = request.POST.get('title')
        if Task.objects.filter(title = title, user = current_active_user).exists():
            #delete the task
            existing_task = Task.objects.get(title = title, user = current_active_user)
            existing_task.delete()
        else:
            new_task_owner = current_active_user
            new_task = Task(title = title, user = new_task_owner)
            new_task.save()

    
    tasks = Task.objects.filter(user = current_active_user)
    task_names = [task.title for task in tasks]
    request.session["tasks"] = task_names
    context = {"tasks": task_names}
    return render(request, 'index.html', context)

def add_task(request):
    context = {"form": AddTaskForm()}
    return render(request, 'add-task.html', context)
