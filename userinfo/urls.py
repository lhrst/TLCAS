from django.urls import path, include
from userinfo import views as user_views
from userinfo.mycaptcha import views as captcha_views

urlpatterns = [ 
    path('login/', user_views.login),
    path('register/', user_views.register),
    path('logout/', user_views.logout),
    path('confirm/', user_views.user_confirm),

    path('captcha/', include('captcha.urls')),
    path('refresh_captcha/', captcha_views.refresh_captcha),
]