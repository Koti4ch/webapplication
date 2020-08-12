from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdminPanel(admin.ModelAdmin):
    # readonly_fields = ['task_slug',]
    prepopulated_fields = {'task_slug': ('open_by', 'task_title',), }
    list_display = ('task_title', 'open_by', 'closed_by', 'task_status', 'create_time')
    list_filter = ('task_status',)
    ordering = ('create_time', 'task_title')
