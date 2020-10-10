import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password

from userinfo import models as user_models
from userinfo.mycaptcha import views as captcha_views
from userinfo.emailsender import models as email_models
from userinfo.emailsender import views as email_views

def verify_account(username, email, password1, password2, hashkey, captcha) -> str:
    if not captcha_views.verify_captcha(captcha, hashkey):
        return '验证码错误'
    try:
        validate_email(email)
    except:
        return '邮箱格式不正确'
    if password1 != password2:
        return '两次输入的密码不相同'
    if len(password1) < 8 or len(password1) > 128:
        return '密码的长度不应小于8，大于128'
    if user_models.UserInformation.objects.filter(username=username, is_active=True):
        return '用户名[{}]已被注册'.format(username)
    if user_models.UserInformation.objects.filter(email=email, is_active=True):
        return '邮箱[{}]已被注册'.format(email)
    return ''

# Create your views here.
def register(request):
    if request.method == "GET":
        newcaptcha = captcha_views.generate_captcha()
        return render(request, "userinfo/register.html", {"captcha": newcaptcha})
    elif request.method == "POST":
        rq_hashkey = request.POST.get('captcha_0', '')
        rq_captcha = request.POST.get('captcha_1', '')
        rq_username = request.POST.get('username', '').strip()
        rq_email = request.POST.get('email', '').strip()
        rq_password1 = request.POST.get('password1', '').strip()
        rq_password2 = request.POST.get('password2', '').strip()
        message = verify_account(rq_username, rq_email, rq_password1, rq_password2, rq_hashkey, rq_captcha)
        if len(message) == 0:
            newuser = user_models.UserInformation.objects.create(
                username=rq_username,
                email=rq_email,
                password=make_password(rq_password1),
                is_active=False
            )
            # send email
            code = email_views.make_confirm_string(newuser)
            email_views.send_email(rq_email, code)
            return redirect("/")
        else:
            newcaptcha = captcha_views.generate_captcha()
            return render(request, "userinfo/register.html", {"captcha": newcaptcha, "message": message})


def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')

def user_confirm(request):
    code = request.GET.get('code', None)
    try:
        confirm = email_models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'userinfo/confirm.html', {'message': message})

    c_time = confirm.create_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'userinfo/confirm.html', {'message': message})
    else:
        confirm.user.is_active = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'userinfo/confirm.html', {'message': message})