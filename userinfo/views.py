from django.shortcuts import render
from django.http import HttpResponse

from userinfo.mycaptcha import views as captcha_views

# Create your views here.
def register(request):
    if request.method == "GET":
        newcaptcha = captcha_views.generate_captcha()
        return render(request, "userinfo/register.html", {"captcha": newcaptcha})
    elif request.method == "POST":
        rq_hashkey = request.POST.get('captcha_0', '')
        rq_captcha = request.POST.get('captcha_1', '')
        if captcha_views.verify_captcha(rq_captcha, rq_hashkey):
            return HttpResponse("正确")
        else:
            return HttpResponse("错误")

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')

def user_confirm(request):
    return HttpResponse('user_confirm')
