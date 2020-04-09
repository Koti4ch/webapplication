from django.db import models
from django.contrib.auth.models import AbstractUser

import os, socket
# Create your models here.
class User(AbstractUser):
    rmg_to_reg = models.CharField(max_length=25, blank=False, null=False, default=socket.gethostname, verbose_name='Created from compname')
    last_rmg_used = models.CharField(max_length=25, blank=True, null=True, verbose_name='Last connect from')
    login_to_reg = models.CharField(max_length=50, default=os.getlogin, blank=False, null=False, verbose_name='Created by login')

    # def comp_name()