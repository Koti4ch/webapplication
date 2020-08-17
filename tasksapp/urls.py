from django.urls import path

from . import views as taskviews

urlpatterns = [
    path('', taskviews.startCreateTask, name='taskapp'),
    path('taskmanager/', taskviews.TaskManagerView.as_view(), name='taskmanager'),
    path('taskmanager/<action>/<task>/', taskviews.TaskManagerActionsView.as_view(), name='taskmanageraction'),
]