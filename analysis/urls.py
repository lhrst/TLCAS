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

    path('analysis/AAAI1/', views.AAAI1, name='AAAI1'),
    path('analysis/ACL1/', views.ACL1, name='ACL1'),
    path('analysis/CVPR1/', views.CVPR1, name='CVPR1'),
    path('analysis/ICML1/', views.ICML1, name='ICML1'),
    path('analysis/ICCV1/', views.ICCV1, name='ICCV1'),
    path('analysis/NIPS1/', views.NIPS1, name='NIPS1'),
    path('analysis/IJCAI1/', views.IJCAI1, name='IJCAI1'),

    path('analysis/AAAI2/', views.AAAI2, name='AAAI2'),
    path('analysis/ACL2/', views.ACL2, name='ACL2'),
    path('analysis/CVPR2/', views.CVPR2, name='CVPR2'),
    path('analysis/ICML2/', views.ICML2, name='ICML2'),
    path('analysis/ICCV2/', views.ICCV2, name='ICCV2'),
    path('analysis/NIPS2/', views.NIPS2, name='NIPS2'),
    path('analysis/IJCAI2/', views.IJCAI2, name='IJCAI2'),
]