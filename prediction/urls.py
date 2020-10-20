from django.urls import path

from prediction import views  #添加的

urlpatterns = [
    # 展示主界面
    path('prediction/', views.index, name='index'),
    path('prediction/result/', views.result, name='result'),
]