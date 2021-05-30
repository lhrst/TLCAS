from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'analysis/index.html')

def AAAI(request):
    return render(request, 'analysis/AAAI.html')
def AAAI1(request):
    return render(request, 'analysis/AAAI1.html')
def AAAI2(request):
    return render(request, 'analysis/AAAI2.html')

def ACL(request):
    return render(request, 'analysis/ACL.html')
def ACL1(request):
    return render(request, 'analysis/ACL1.html')
def ACL2(request):
    return render(request, 'analysis/ACL2.html')

def CVPR(request):
    return render(request, 'analysis/CVPR.html')
def CVPR1(request):
    return render(request, 'analysis/CVPR1.html')
def CVPR2(request):
    return render(request, 'analysis/CVPR2.html')

def ICML(request):
    return render(request, 'analysis/ICML.html')
def ICML1(request):
    return render(request, 'analysis/ICML1.html')
def ICML2(request):
    return render(request, 'analysis/ICML2.html')

def ICCV(request):
    return render(request, 'analysis/ICCV.html')
def ICCV1(request):
    return render(request, 'analysis/ICCV1.html')
def ICCV2(request):
    return render(request, 'analysis/ICCV2.html')

def NIPS(request):
    return render(request, 'analysis/NIPS.html')
def NIPS1(request):
    return render(request, 'analysis/NIPS1.html')
def NIPS2(request):
    return render(request, 'analysis/NIPS2.html')

def IJCAI(request):
    return render(request, 'analysis/IJCAI.html')
def IJCAI1(request):
    return render(request, 'analysis/IJCAI1.html')
def IJCAI2(request):
    return render(request, 'analysis/IJCAI2.html')