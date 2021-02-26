from django.urls import path, include
from userinfo import views as user_views
from userinfo.mycaptcha import views as captcha_views
from userinfo.inbox import views as inbox_views


urlpatterns = [ 
    path('login/', user_views.login, name="login"),
    path('register/', user_views.register, name="register"),
    path('logout/', user_views.logout, name="logout"),
    path('confirm/', user_views.user_confirm, name="confirm"),
    path('profile/<str:uuid>/', user_views.profile_view, name="profile"),
    path('profile/<str:uuid>/revise/', user_views.profile_revise, name="revise"),
    path('inbox/', inbox_views.inbox_overview, name="inbox"),
    path('inbox/<int:id>/', inbox_views.inbox_detail, name="inbox_detail"),
    path('inbox/check_all_unread/', inbox_views.inbox_check_all_unread, name="check_all_unread"),
    path('captcha/', include('captcha.urls')),
    path('refresh_captcha/', captcha_views.refresh_captcha),
]