from django.urls import path

from analysis import views  #添加的

urlpatterns = [
    # 展示主界面
    path('analysis/', views.index, name='index'),
    path('analysis/AAAI/', views.AAAI, name='AAAI'),
    path('analysis/ACL/', views.ACL, name='ACL'),
    path('analysis/CVPR/', views.CVPR, name='CVPR'),
    path('analysis/ICML/', views.ICML, name='ICML'),
    path('analysis/ICCV/', views.ICCV, name='ICCV'),
    path('analysis/NIPS/', views.NIPS, name='NIPS'),
    path('analysis/IJCAI/', views.IJCAI, name='IJCAI'),
]