from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.expressions import OrderBy
from django.utils import timezone
from papers import models as papers_models

class UserInformation(AbstractUser):
    password = models.CharField(max_length=128, null=True, blank=True)
    uuid = models.CharField(max_length=36, null=True, blank=True)
    unread_message = models.IntegerField(default=0)

    def __str__(self):
        return '{name}({email})'.format(name=self.username, email=self.email)
    
    class Meta:
        ordering = ["-date_joined"]
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

class PaperViewHistory(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    paper = models.ForeignKey(papers_models.PaperInfo, on_delete=models.CASCADE)
    view_times = models.IntegerField(default=1)
    view_time = models.DateTimeField(auto_now_add=True)
    already_deleted = models.BooleanField(default=False)  # 超过一定时间的浏览记录应标记为already_deleted=True, 定期清理数据库

    def __str__(self):
        return '{name}({title})'.format(name=self.user.username, title=self.paper.paper_title)
    
    class Meta:
        ordering = ["-view_time"]
        verbose_name = "论文浏览记录"
        verbose_name_plural = verbose_name

class UserCollect(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    paper = models.ForeignKey(papers_models.PaperInfo, on_delete=models.CASCADE)
    record_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '用户论文收藏'
        verbose_name_plural = verbose_name
