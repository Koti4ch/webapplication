from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

import os, socket
# Create your models here.
class User(AbstractUser):
    rmg_to_reg = models.CharField(max_length=25, blank=False, null=False, default=socket.gethostname, verbose_name='Created from compname')
    last_rmg_used = models.CharField(max_length=25, blank=True, null=True, verbose_name='Last connect from')
    login_to_reg = models.CharField(max_length=50, default=os.getlogin, blank=False, null=False, verbose_name='Created by login')


class PersonalUserInfo(models.Model):
    RADIO_CHANALS = (
        ('1k', '1 канал'),
        ('St', 'Стлица'),
        ('Ku', 'Культура'),
        ('Ra', 'РадиусФМ'),
    )
    radio_chanal = models.CharField(max_length=2, choices=RADIO_CHANALS)
    radio_room = models.CharField(max_length=3, blank=True)
    working_position = models.CharField(max_length=35, blank=True)
    user_birthday = models.DateField(null=True)
    user_telephon = models.CharField(max_length=35, blank=True)
    user_about = models.TextField(max_length=255, blank=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Friends_list = ???????????????

    def __str__(self):
        return "Профиль {}".format(self.user.username)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print(instance)
        PersonalUserInfo.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    print(instance)
    instance.personaluserinfo.save()