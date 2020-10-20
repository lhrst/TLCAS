from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'prediction/index.html')

def result(request):
    if request.method == 'POST':
        name = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
    print(name, content, author)
    return render(request, 'prediction/result.html')
