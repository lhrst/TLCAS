from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return HttpResponse('register')

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')

def user_confirm(request):
    return HttpResponse('user_confirm')