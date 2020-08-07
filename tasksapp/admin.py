from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdminPanel(admin.ModelAdmin):
    readonly_fields = ['task_title', 'task_msg']