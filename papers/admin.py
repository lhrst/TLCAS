from django.contrib import admin

from .models import PaperInfo, ConferenceInfo

admin.site.register(PaperInfo)
admin.site.register(ConferenceInfo)
# Register your models here.
