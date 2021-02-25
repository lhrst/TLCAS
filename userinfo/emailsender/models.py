from django.db import models
from userinfo.models import UserInformation
# Create your models here.
class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField(UserInformation, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{name}({code})'.format(name=self.user.username, code=self.code)
    
    class Meta:
        ordering = ['-create_time']
        verbose_name = '确认码'
        verbose_name_plural = verbose_name