from django.urls import path
from userinfo import views

urlpatterns = [ 
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
]