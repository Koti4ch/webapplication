from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import createNewTaskForm
from authuser.models import User
from .models import Task
from django.utils.text import slugify
# Create your views here.



def startCreateTask(request):
    if request.method == 'GET':
        createtaskform = createNewTaskForm()
        return render(request, 'tasksapp/createnewtask_page.html', {'createtaskform': createtaskform})

    if request.method == "POST":
        createtaskform = createNewTaskForm(data=request.POST)
        if createtaskform.is_valid():
            try:
                userObj = User.objects.get(username=request.user)
            except:
                print("Can't identify")
                userObj = User.objects.get(username='noname')

            taskInstance = createtaskform.save(commit=False)
            taskInstance.open_by = userObj
            # TODO : troubles with russian letters
            taskInstance.task_slug = slugify(taskInstance.task_title + str(taskInstance.task_id)[-13:], allow_unicode=True)

            taskInstance.save()

            # for _k, _v in taskInstance.__dict__.items():
            #     print('{} \t: {}'.format(_k, _v))
            


            messages.add_message(request, messages.INFO,
                                 'Задание открыто.')
        return redirect('index')

# TODO: create it in class
class TaskApp():
    pass


class TaskManagerView(View):
    '''
    Taskmanager help us to change task status
    '''
    def get(self, request):
        if 'sort_by' in request.GET:
            if request.GET['sort_by'] == 'all':
                tasklist = Task.objects.all().order_by('-create_time')
            else:
                tasklist = Task.objects.filter(task_status=request.GET['sort_by']).order_by('-create_time')
        else:
            tasklist = Task.objects.all().order_by('-create_time')
        content = {"tasklist": tasklist}
        
        return render(request, 'tasksapp/taskmanager_page.html', content)


class TaskManagerActionsView(View):
    '''
    TasmanagerActions help us to change task statuses 
    '''
    def post(self, request, action, task):
        print(request.user.username, request.user.id)
        obj = Task.objects.get(pk=task)
        if action == 'start':
            obj.task_status = obj.STATUSES[1][0]
            obj.save()
        elif action == 'delete':
            obj.task_status = obj.STATUSES[3][0]
            obj.closed_by = User.objects.get(pk=request.user.id)
            obj.delete()
        elif action == 'success':
            obj.task_status = obj.STATUSES[2][0]
            obj.closed_by = User.objects.get(pk=request.user.id)
            obj.save()


        return redirect('taskmanager')