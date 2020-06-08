from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image

import os, socket

# Create your models here.
class User(AbstractUser):
    rmg_to_reg = models.CharField(max_length=25, blank=False, null=False, default=socket.gethostname, verbose_name='Created from compname')
    last_rmg_used = models.CharField(max_length=25, blank=True, null=True, verbose_name='Last connect from')
    login_to_reg = models.CharField(max_length=50, default=os.getlogin, blank=False, null=False, verbose_name='Created by login')
    email = models.EmailField(max_length=25, unique=True)



class PersonalUserInfo(models.Model):
    RADIO_CHANALS = (
        ('1k', '1й Канал'),
        ('st', 'Столица'),
        ('kl', 'Культура'),
        ('ra', 'Радиус ФМ'),
        ('bl', '"Беларусь"'),
        ('na', 'Не определилась'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    avatara = models.ImageField(upload_to='users_avas/', blank=True, null=True, default='base.jpg')
    radio_chanal = models.CharField(max_length=2, choices=RADIO_CHANALS, default=RADIO_CHANALS[5], verbose_name='Канал')
    radio_room = models.CharField(max_length=9, blank=True, verbose_name='Кабинет')
    working_position = models.CharField(max_length=25, blank=True, verbose_name='Должность')
    user_birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    user_telephone = models.CharField(max_length=15, blank=True, verbose_name='Номер телефона')
    user_about = models.TextField(max_length=255, blank=True)
    # friendlist = 

    def __str__(self):
        return 'about {}'.format(self.user.username)

    
    def find_choice(self, shortname):
        for _ in self.RADIO_CHANALS:
            if _[0] == shortname:
                return _[1]
    

    def save(self):
        super().save()
        with Image.open(self.avatara.path) as userava:
            if userava.height > 256 or userava.width > 256:
                resize = (256, 256)
                userava.thumbnail(resize)
                userava.save(self.avatara.path)



# @receiver(post_delete, sender=PersonalUserInfo)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     if instance.avatara:
#         if os.path.isfile(instance.avatara.path):
#             os.remove(instance.avatara.path)
#             # instance.avatara.delete(True)
#             instance.avatara = 'base.jpg'
#     else:
#         instance.avatara = 'base.jpg'

# @receiver(pre_save, sender=PersonalUserInfo)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     if not instance.pk:
#         return False
    
#     try:
#         old_file = PersonalUserInfo.objects.get(pk=instance.pk).avatara
#     except PersonalUserInfo.DoesNotExist:
#         return False

#     new_file = instance.avatara
#     if old_file != 'base.jpg':
#         if not old_file == new_file:
#             if os.path.isfile(old_file.path):
#                 os.remove(old_file.path)

