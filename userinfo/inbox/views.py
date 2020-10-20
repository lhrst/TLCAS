from django.http.response import HttpResponse, JsonResponse
from userinfo import inbox
from django.shortcuts import render, redirect
import userinfo.models as userinfo_models
import userinfo.inbox.models as inbox_models


# Create your views here.
def inbox_overview(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    if request.method == "GET":
        page = request.GET.get('page', 'unread')
        inbox_message = None
        if page == "unread":
            inbox_message = inbox_models.InboxMessage.objects.filter(user=request.user, has_read=False).order_by("-send_time")
        elif page == "read":
            inbox_message = inbox_models.InboxMessage.objects.filter(user=request.user, has_read=True).order_by("-send_time")
        return render(request, "userinfo/inbox_overview.html", {"inbox_message": inbox_message})
    return JsonResponse({"status": "error", "msg": "GET support only"})

def inbox_detail(request, id):
    return HttpResponse("TODO")

def inbox_check_all_unread(request):
    if check_all_inbox(request.user):
        return redirect('/inbox/')    
    else:
        return render(request, "userinfo/inbox_overview.html", {"message": "操作非法"})

# 发送通知，user传入UserInformation对象
def send_inbox(user, title:str, content:str) -> bool:
    try:
        if not user.is_authenticated : return False
        inbox_models.InboxMessage.objects.create(user=user, title=title, content=content)
        user.unread_message += 1
        user.save()
        return True
    except:
        return False

# 用户查看通知
def check_inbox(user, inbox) -> bool:
    try:
        if not user.is_authenticated: return False
        if not inbox.has_read:
            user.unread_message -= 1
            inbox.has_read = False
            user.save
            inbox.save()
        return True
    except:
        return False

# 查看所有未读
def check_all_inbox(user) -> bool:
    try:
        if not user.is_authenticated: return False
        user.unread_message = 0
        user.save()
        inbox_models.InboxMessage.objects.filter(user=user).update(has_read=True)
    except:
        return False
