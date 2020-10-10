from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInformation(AbstractUser):
    aliasname = models.CharField(max_length=32, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name