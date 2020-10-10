from django.urls import path
from papers import views

urlpatterns = [ 
    path('papers/show_list/<pindex>', views.index, name='index'),
    path('papers/<int:paper_id>/', views.detail, name='detail'),
]
