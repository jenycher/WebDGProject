from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    #return HttpResponse("<h1>Это мой первый проект на Django</h1>")
    data ={
        'caption': "CatDjango"
    }
    return render (request, 'main/index.html', data)

def new(request):
    #return HttpResponse("<h1>Это вторая страница моего проекта на Django</h1>")
    return render(request, 'main/new.html')