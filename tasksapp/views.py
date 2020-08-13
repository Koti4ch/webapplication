from django.shortcuts import render
from .forms import createNewTaskForm
# Create your views here.



def startCreateTask(request):
    if request.method == 'GET':
        createtaskform = createNewTaskForm()
        return render(request, 'tasksapp/createnewtask_page.html', {'createtaskform': createtaskform})

# TODO: create it in class
class TaskApp():
    pass
