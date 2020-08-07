from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Task(models.Model):
    '''
    Model for tasks
    '''
    task_title = models.CharField(max_length=50, blank=False, null=False, verbose_name='Заголовок задания', help_text='Не более 50 символов')
    task_msg = models.CharField(max_length=800,verbose_name='Описание задания', blank=False, null=False, help_text='')

    STATUSES = (
        (1, 'Открыто'),
        (2, 'В процессе выполнения'),
        (3, 'Выполнено'),
        (0, 'Закрыто'),
    )

    task_status = models.CharField(max_length=1, blank=False, null=False, choices=STATUSES, default=STATUSES[0], verbose_name='Состояние заявки', help_text='')
    # TODO: подумать какие тут связи будут!
    who_open = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    who_close = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    create_time = models.DateTimeField(default=timezone.now, blank=True, null=False)
    closed_time = models.DateTimeField(default='', blank=True, null=False)