from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

import os, socket

# Create your models here.
class User(AbstractUser):
    rmg_to_reg = models.CharField(max_length=25, blank=False, null=False, default=socket.gethostname, verbose_name='Created from compname')
    last_rmg_used = models.CharField(max_length=25, blank=True, null=True, verbose_name='Last connect from')
    login_to_reg = models.CharField(max_length=50, default=os.getlogin, blank=False, null=False, verbose_name='Created by login')



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

    avatara = models.ImageField(upload_to='users/', blank=True)
    radio_chanal = models.CharField(max_length=2, choices=RADIO_CHANALS, default=RADIO_CHANALS[5])
    radio_room = models.CharField(max_length=9, blank=True)
    working_position = models.CharField(max_length=25, blank=True)
    user_birthday = models.DateField(null=True, blank=True)
    user_telephone = models.CharField(max_length=15, blank=True)
    user_about = models.TextField(max_length=255, blank=True)
    # friendlist = 

    def __str__(self):
        return 'about {}'.format(self.user.username)
    
    def find_choice(self, shortname):
        for _ in self.RADIO_CHANALS:
            if _[0] == shortname:
                return _[1]
    


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_addition_info(sender, instance, created, **kwargs):
    if created:
        try:
            print(instance.personaluserinfo)
        except ObjectDoesNotExist as e:
            PersonalUserInfo.objects.create(user=instance)
            print(e)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def resave_userinfo(sender, instance, **kwargs):
#     instance.personaluserinfo.save()
#     print('Profile for {} updated!'.format(instance.username))




