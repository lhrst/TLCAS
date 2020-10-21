from django.urls import path
from papers import views

urlpatterns = [
    # 展示主界面
    path('', views.index, name='index'),
    # 论文单独展示界面
    path('papers/pp<int:paper_id>/', views.detail, name='detail'),
    # 搜索结果界面
    path('search/?s=<searchword>/page=<pindex>/', views.search, name='search')
]
