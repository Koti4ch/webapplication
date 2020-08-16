from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
import uuid
# Create your models here.


class Task(models.Model):
    '''
    Model for tasks
    '''
    task_id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    task_title = models.CharField(max_length=50, blank=False, null=False, verbose_name='Заголовок задания', help_text='Не более 50 символов')
    task_slug = models.SlugField(
        max_length=50, blank=False, null=False, verbose_name='task slug title')
    task_msg = models.TextField(max_length=255,verbose_name='Описание задания', blank=False, null=False, help_text='')

    STATUSES = (
        ('1', 'Открыто'),
        ('2', 'В процессе выполнения'),
        ('3', 'Выполнено'),
        ('0', 'Закрыто'),
    )

    task_status = models.CharField(max_length=1, blank=False, null=False, choices=STATUSES, default=STATUSES[0], verbose_name='Состояние заявки', help_text='')
    # related_name обязательно, когда надо в форенкея.
    open_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='open_by')
    closed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='closed_by', null=True, blank=True)

    create_time = models.DateTimeField(default=timezone.datetime.now, blank=True, null=False)
    closed_time = models.DateTimeField(blank=True, null=True)

    # TODO : need add username from comp who create a task
    # current_user_name = models.CharField(max_length=20, ${blank=True, null=True})

    #def __str__(self):
    #    return task_title
