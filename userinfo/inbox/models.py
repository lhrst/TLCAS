from django.db import models
from userinfo import models as userinfo_models
# Create your models here.

class InboxMessage(models.Model):
    user = models.ForeignKey(userinfo_models.UserInformation, on_delete=models.CASCADE)
    title = models.CharField(max_length=32, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    has_read = models.BooleanField(default=False)
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{username} [{title}]'.format(username=self.user.username, title=self.title)
    
    class Meta:
        verbose_name = '站内通知'
        verbose_name_plural = verbose_name