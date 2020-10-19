from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'prediction/index.html')

def result(request):
    return render(request, 'prediction/result.html')