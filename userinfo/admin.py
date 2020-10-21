from django.contrib import admin
from userinfo.models import UserInformation, PaperViewHistory

# Register your models here.
admin.site.register(UserInformation)
admin.site.register(PaperViewHistory)