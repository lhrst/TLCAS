from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'analysis/index.html')
    
def AAAI(request):
    return render(request, 'analysis/AAAI.html')

def ACL(request):
    return render(request, 'analysis/ACL.html')

def CVPR(request):
    return render(request, 'analysis/CVPR.html')

def ICML(request):
    return render(request, 'analysis/ICML.html')

def ICCV(request):
    return render(request, 'analysis/ICCV.html')

def NIPS(request):
    return render(request, 'analysis/NIPS.html')

def IJCAI(request):
    return render(request, 'analysis/IJCAI.html')