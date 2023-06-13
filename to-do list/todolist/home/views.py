from django.shortcuts import render,redirect
from home.models import Task

# Create your views here.
def home(request):
    context={'Success':False}
    if request.method=="POST":
       title=request.POST['title']
       desc=request.POST['desc']

      # print(title ,desc)
       ins = Task(taskTitle=title, taskDesc=desc)
       ins.save()
       context={'Success':True}
       print("The data had been return to the db")

    return render(request, 'index.html', context)

    
def tasks(request):
    allTasks=Task.objects.all()
    #for item in allTasks:
        #print(item.taskDesc)
    context={'tasks':allTasks}
    return render(request, 'tasks.html' ,context)

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('tasks')