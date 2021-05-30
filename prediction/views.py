from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    return render(request, 'prediction/index.html')

def result(request):
    a=random.randint(1,7)
    s = 'A'
    if(a==1): s='AAAI'
    if(a==2): s='ACL'
    if(a==3): s='CVPR'
    if(a==4): s='ICCV'
    if(a==5): s='ICML'
    if(a==6): s='IJCAI'
    if(a==7): s='NIPS'
    if request.method == 'POST':
        name = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
    print(name, content, author)
    return render(request, 'prediction/result.html', {'name': name, 'content': content,'author': author,'s': s})
