from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserInformation(AbstractUser):
    password = models.CharField(max_length=128, null=True, blank=True)
    
    def __str__(self):
        return '{name}({email})'.format(name=self.username, email=self.email)
    
    class Meta:
        ordering = ["-date_joined"]
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name