from django.conf.urls import url
from django.contrib import admin

from prediction import views  #添加的

urlpatterns = [
    url(r'^prediction',views.home),
]